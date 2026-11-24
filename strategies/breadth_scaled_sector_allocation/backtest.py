"""Breadth-scaled sector allocation: portfolio backtest adapted from the generic template (see _simulate_portfolio).

Copy this file into strategies/<name>/backtest.py and adapt the copy: CONFIG,
PARAMS, SPACE, valid(), buy_signal(), sell_signal(). Don't edit this template
for one strategy.

Run inside the backtest container (repo root is /app):

    docker compose run --rm -T backtest python strategies/<name>/backtest.py --period is
    docker compose run --rm -T backtest python strategies/<name>/backtest.py --period oos --params '{"rsi_n": 3}'
    ... --symbols ETHUSDT,SOLUSDT   run on other symbols than CONFIG["symbols"]
    ... --period live               start -> newest data (ignores "end"): is a position open right now?
    ... --trades                    also print the trade list

Simulation rules
- Signals are computed from bar t's close (and earlier bars). Orders fill at
  the OPEN of bar t+1, so nothing uses information from the future.
- Indicators are computed on the whole history, then only trades inside the
  chosen period are simulated. Each period starts flat with CONFIG["capital"].
- Optional exits (any param set to 0 or missing = off):
    stop_loss_pct     exit when price falls this % below the entry fill
    take_profit_pct   exit when price rises this % above the entry fill
    trailing_stop_pct exit when price falls this % below the highest high since entry
    max_bars          exit at the open after this many bars in the trade
  Stops/targets are checked intrabar with high/low. A gap through the level
  fills at the open. If stop and target are both touched in one bar, the stop
  is assumed (conservative). Signal exits fill at the next open.
- Fees: CONFIG["fee_pct"] of the traded value on every buy and every sell.
  Slippage: CONFIG["slippage_pct"] moves every fill against us.
- Each symbol starts trading only after CONFIG["warmup_bars"] bars of its own
  history, so indicators are warmed up (matters for coins listed after "start").
- A "big loss" is a trade that loses more than CONFIG["big_loss_pct"] % of equity
  AND more than CONFIG["big_loss_mult"] x the strategy's median losing trade, i.e. an
  unusually bad trade for this strategy, not every ordinary stop-out.
- Several symbols: capital is split equally and each symbol trades on its own.
  Equity curves are summed for the drawdown.
- A position still open at the end of the period is closed at the last close
  (flagged with open_at_end).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name != "strategies" else Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# --------------------------------------------------------------------------
# Strategy definition: adapt everything in this block in the copy.
# --------------------------------------------------------------------------
# Portfolio strategy: the whole symbol list is ONE portfolio (breadth is measured across it),
# not independent per-symbol trades. run() below therefore uses _simulate_portfolio instead of
# the template's per-symbol _simulate (machinery change, logged in optimization.log).
CONFIG = {
    "name": "breadth_scaled_sector_allocation",
    "asset_class": "etf",            # Yahoo daily, dividend/split adjusted (= total return)
    "symbols": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "timeframe": "1d",               # daily bars for fills and stop monitoring; decisions at month-end
    "start": "2000-07-01",           # first fill; 9 SPDRs listed 1998-12-22 -> ~380 bars warm-up (SMA up to 380)
    "oos_start": "2016-01-01",       # repo precedent for ETF strategies
    "end": "2026-11-23",             # frozen at setup (last complete daily bar)
    "capital": 10_000.0,
    "position_pct": 1.0,             # whole sleeve; per-holding weight = 1/N_universe (= B / count(eligible))
    "fee_pct": 0.05,                 # US ETF default
    "slippage_pct": 0.03,
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 0,                # not used: a symbol joins the universe once its SMA(n) exists
}

PARAMS = {
    "n": 200,                # SMA length (daily bars) for eligibility and breadth
    "stop_loss_pct": 15.0,   # hard stop below each holding's cost basis (never loosened)
    "max_candles": 252,      # held daily bars per holding before a forced exit at the next open
}

SPACE = {
    "n": {"min": 100, "max": 300, "step": 10, "hard_min": 20, "hard_max": 380},
    "stop_loss_pct": {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0},
    "max_candles": {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260},
}


def valid(p: dict) -> bool:
    return p["n"] >= 2 and p["stop_loss_pct"] > 0 and p["max_candles"] >= 1


def buy_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Eligibility at a bar's close: close > SMA(n). Only used at month-end decisions."""
    return df["close"] > df["close"].rolling(int(p["n"]), min_periods=int(p["n"])).mean()


def sell_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Not eligible (close <= SMA(n)); NaN SMA -> not part of the universe (handled in the simulator)."""
    return ~buy_signal(df, p)


_PANEL: dict = {}


def _panel(symbols: tuple) -> dict:
    """Aligned OHLC arrays on the union of trading days (NaN before listing / on missing bars, no ffill)."""
    if symbols in _PANEL:
        return _PANEL[symbols]
    dfs = {s: load_bars(CONFIG["asset_class"], s, CONFIG["timeframe"]) for s in symbols}
    idx = dfs[symbols[0]].index
    for d in dfs.values():
        idx = idx.union(d.index)
    al = {s: d.reindex(idx) for s, d in dfs.items()}
    per = idx.tz_localize(None).to_period("M")
    nxt = pd.Series(per, index=idx).shift(-1)
    month_end = (pd.Series(per, index=idx).ne(nxt) & nxt.notna()).to_numpy(bool)   # last bar of a complete month
    out = {"idx": idx, "dfs": al, "month_end": month_end, "sma": {}}
    for k in ("open", "high", "low", "close"):
        out[k] = np.column_stack([al[s][k].to_numpy(float) for s in symbols])
    _PANEL[symbols] = out
    return out


def _sma(P: dict, n: int) -> np.ndarray:
    if n not in P["sma"]:
        # rolling over each symbol's own valid bars (no window across the pre-listing NaNs)
        cols = []
        for j in range(P["close"].shape[1]):
            c = pd.Series(P["close"][:, j])
            v = c.dropna()
            cols.append(v.rolling(n, min_periods=n).mean().reindex(c.index).to_numpy(float))
        P["sma"][n] = np.column_stack(cols)
    return P["sma"][n]


def _simulate_portfolio(P: dict, syms: list, p: dict, lo: int, hi: int, capital: float):
    """Month-end breadth allocation with per-holding hard stop and time cap.

    Decision at the close of the last bar of each complete month t:
      universe U = symbols with a valid close and a defined SMA(n) at t (point-in-time: not yet
      listed / not yet warmed up = not in U); eligible = close > SMA(n); B = |eligible| / |U|;
      target weight per eligible = B / |eligible| = 1 / |U|; rest cash (0% yield).
      If a listed universe member has no bar at t, the rebalance is skipped (weights unchanged).
    Execution at the open of bar t+1, in this order on every bar:
      1. time exit: holding has completed max_candles held bars -> sell at the open
      2. gap stop: open <= stop -> sell at the open
      3. rebalance (only on execution bars): sell ineligible, trim overweight (keep cost E and age),
         then buy underweight / new; buys scaled down if cash is short. Symbols exited on this
         bar are not re-bought on it. Additions: E = weighted-average cost,
         stop = max(old stop, E_new * (1 - sl)).
      4. intrabar stop: low <= stop -> sell at the stop.
    A stopped holding stays out until the next month-end decision (buys only happen there).
    """
    o, h, l, c = P["open"], P["high"], P["low"], P["close"]
    sma = _sma(P, int(p["n"]))
    idx, me = P["idx"], P["month_end"]
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    sl = p["stop_loss_pct"] / 100
    max_c = int(p["max_candles"])
    k = len(syms)
    qty = np.zeros(k)
    cost = np.zeros(k)          # cash paid incl. fees for the open position (for weighted-average E)
    E = np.zeros(k)             # average cost per unit (fill prices)
    stop = np.zeros(k)
    entry_i = np.full(k, -1)
    entry_eq = np.zeros(k)
    flows = np.zeros(k)         # net cash flow of the open position (proceeds - payments)
    cash = capital
    trades: list = []
    equity = np.full(hi - lo, np.nan)
    pending = None              # target weights decided at the previous close

    def sell(j: int, i: int, units: float, price: float, reason: str | None):
        nonlocal cash
        fill = price * (1 - slip)
        proceeds = units * fill * (1 - fee)
        cash += proceeds
        flows[j] += proceeds
        qty[j] -= units
        if reason is not None or qty[j] <= 1e-12:      # fully closed -> one trade record
            qty[j] = 0.0
            trades.append({
                "symbol": syms[j], "entry_time": str(idx[entry_i[j]]), "exit_time": str(idx[i]),
                "entry_price": E[j], "exit_price": fill, "qty": units, "pnl": flows[j],
                "pnl_pct_of_equity": flows[j] / entry_eq[j] * 100 if entry_eq[j] > 0 else 0.0,
                "bars": i - entry_i[j], "exit_reason": reason or "signal",
            })
            cost[j] = E[j] = stop[j] = flows[j] = 0.0
            entry_i[j] = -1
        else:
            cost[j] *= qty[j] / (qty[j] + units)        # partial reduction keeps E, stop and age

    def equity_at(i: int, price: np.ndarray) -> float:
        px = np.where(np.isnan(price[i]), 0.0, price[i])
        return cash + float((qty * px).sum())

    for i in range(lo, hi):
        exited = np.zeros(k, bool)
        for j in range(k):
            if qty[j] <= 0:
                continue
            if i - entry_i[j] >= max_c and not np.isnan(o[i, j]):
                sell(j, i, qty[j], o[i, j], "max_bars")
                exited[j] = True
            elif not np.isnan(o[i, j]) and o[i, j] <= stop[j]:
                sell(j, i, qty[j], o[i, j], "stop")
                exited[j] = True
        if pending is not None:
            w = pending
            pending = None
            eq_open = equity_at(i, o)
            target = w * eq_open
            val = np.where(np.isnan(o[i]), 0.0, qty * o[i])
            for j in range(k):                          # sells first
                if qty[j] > 0 and not np.isnan(o[i, j]) and val[j] > target[j]:
                    if target[j] <= 0:
                        sell(j, i, qty[j], o[i, j], "signal")
                    else:
                        sell(j, i, (val[j] - target[j]) / o[i, j], o[i, j], None)
            need = np.zeros(k)
            for j in range(k):
                if target[j] > 0 and not exited[j] and not np.isnan(o[i, j]):
                    need[j] = max(0.0, target[j] - qty[j] * o[i, j])
            total = need.sum() * (1 + slip) * (1 + fee)
            scale = min(1.0, cash / total) if total > 0 else 0.0
            for j in range(k):
                if need[j] <= 0:
                    continue
                fill = o[i, j] * (1 + slip)
                pay = need[j] * scale * (1 + slip) * (1 + fee)
                units = pay / (fill * (1 + fee))
                if units <= 0:
                    continue
                if qty[j] <= 0:
                    entry_i[j] = i
                    entry_eq[j] = eq_open
                    flows[j] = 0.0
                cash -= pay
                flows[j] -= pay
                cost[j] += units * fill
                qty[j] += units
                old_stop = stop[j]
                E[j] = cost[j] / qty[j]
                stop[j] = max(old_stop, E[j] * (1 - sl))
        for j in range(k):                              # intrabar stops (active from the entry bar)
            if qty[j] > 0 and not np.isnan(l[i, j]) and l[i, j] <= stop[j]:
                sell(j, i, qty[j], min(o[i, j], stop[j]), "stop")
        equity[i - lo] = equity_at(i, c)
        if me[i] and i + 1 < hi:                        # month-end decision for the next open
            listed = ~np.isnan(sma[i]) | (qty > 0)
            if np.any(np.isnan(c[i]) & listed):
                continue                                 # missing bar for a member: skip, keep weights
            in_u = ~np.isnan(sma[i])
            nu = int(in_u.sum())
            w = np.zeros(k)
            if nu:
                w[in_u & (c[i] > sma[i])] = 1.0 / nu     # = B / count(eligible)
            pending = w
    last = hi - 1
    for j in range(k):                                  # close what is still open at the last close
        if qty[j] > 0:
            px = c[last, j]
            if np.isnan(px):
                px = pd.Series(c[:last + 1, j]).dropna().iloc[-1]
            sell(j, last, qty[j], px, "end")
    eq = pd.Series(equity, index=idx[lo:hi]).ffill().fillna(capital)
    return trades, eq

# --------------------------------------------------------------------------
# Generic machinery below: normally no changes needed.
# --------------------------------------------------------------------------

_BARS: dict = {}


def load_bars(asset_class: str, symbol: str, timeframe: str) -> pd.DataFrame:
    """OHLCV with a UTC DatetimeIndex, using the project's loaders."""
    key = (asset_class, symbol, timeframe)
    if key in _BARS:
        return _BARS[key]
    from src.backtest import data  # project loader: Yahoo daily, adjusted for dividends and splits

    if asset_class == "crypto":
        df = _crypto_bars(symbol, "1D" if timeframe == "1d" else timeframe)
    elif timeframe == "1d":
        df = data.load(asset_class, symbol)
    else:
        raise ValueError("Yahoo symbols only have daily history long enough to backtest (1m data covers ~1 month)")
    df = df[["open", "high", "low", "close", "volume"]].astype(float).dropna(subset=["open", "close"])
    _BARS[key] = df
    return df


def _crypto_bars(symbol: str, timeframe: str) -> pd.DataFrame:
    """UTC bars of any size built from the Binance 1m partitions, cached per symbol and timeframe
    (rebuilt when the 1m data is newer and the cache is older than 6 h)."""
    import time

    import duckdb

    from src.common.storage import CRYPTO_1M, DATA

    cache = DATA / "cache" / f"bars_{symbol}_{timeframe}.parquet"
    src_dir = CRYPTO_1M / f"symbol={symbol}"
    if not src_dir.exists():
        raise ValueError(f"no crypto data for {symbol}")
    newest = max(p.stat().st_mtime for p in src_dir.rglob("*.parquet"))
    if cache.exists() and (cache.stat().st_mtime >= newest or time.time() - cache.stat().st_mtime < 6 * 3600):
        df = pd.read_parquet(cache)
    else:
        secs = int(pd.Timedelta(timeframe).total_seconds())
        df = duckdb.sql(f"""
            SELECT to_timestamp(floor(epoch(open_time) / {secs}) * {secs}) AS date,
                   arg_min(open, open_time) AS open, max(high) AS high, min(low) AS low,
                   arg_max(close, open_time) AS close, sum(quote_volume) AS volume
            FROM read_parquet('{src_dir}/*/*/*.parquet')
            GROUP BY 1 ORDER BY 1
        """).df()
        df["date"] = pd.to_datetime(df["date"], utc=True)
        df = df.iloc[:-1]  # last bucket may be incomplete
        cache.parent.mkdir(parents=True, exist_ok=True)
        tmp = cache.with_suffix(f".{os.getpid()}.tmp")  # atomic: parallel runs may build the same cache
        df.to_parquet(tmp, index=False)
        tmp.replace(cache)
    return df.set_index("date").sort_index()


def _first(mask: np.ndarray, start: int) -> int:
    """Index of the first True at or after start, or -1 (searches growing windows)."""
    n, w = len(mask), 256
    while start < n:
        hit = np.flatnonzero(mask[start:start + w])
        if hit.size:
            return start + int(hit[0])
        start += w
        w *= 4
    return -1


def _simulate(df: pd.DataFrame, buy: np.ndarray, sell: np.ndarray, p: dict, lo: int, hi: int, capital: float, symbol: str):
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    sl, tp = p.get("stop_loss_pct", 0) / 100, p.get("take_profit_pct", 0) / 100
    trail, max_bars = p.get("trailing_stop_pct", 0) / 100, int(p.get("max_bars", 0) or 0)
    idx = df.index
    cash, trades = capital, []
    equity = np.full(hi - lo, np.nan)
    i = lo
    while True:
        s = _first(buy, i)
        if s < 0 or s + 1 >= hi:
            equity[i - lo:] = cash                  # flat until the end
            break
        e = s + 1                                   # entry bar: fill at its open
        entry = o[e] * (1 + slip)
        equity[i - lo:e - lo] = cash
        stake = cash * CONFIG["position_pct"]
        qty = stake / (entry * (1 + fee))
        cash_after = cash - qty * entry * (1 + fee)
        peak = entry
        x, price, reason = None, None, None
        j = e
        while j < hi:                               # walk the trade bar by bar
            if max_bars and j - e >= max_bars:
                x, price, reason = j, o[j], "max_bars"
                break
            stop = max(entry * (1 - sl) if sl else -np.inf, peak * (1 - trail) if trail else -np.inf)
            if stop > -np.inf and l[j] <= stop:
                x, price, reason = j, min(o[j], stop), "stop"
                break
            if tp and h[j] >= entry * (1 + tp):
                x, price, reason = j, max(o[j], entry * (1 + tp)), "target"
                break
            peak = max(peak, h[j])
            if sell[j] and j + 1 < hi:
                x, price, reason = j + 1, o[j + 1], "signal"
                break
            j += 1
            if not (sl or tp or trail or max_bars):  # pure signal exit: jump straight to it
                k = _first(sell, j)
                j = hi if k < 0 or k >= hi else k
        open_at_end = x is None
        if open_at_end:
            x, price, reason = hi - 1, c[hi - 1], "end"
        fill = price * (1 - slip)
        proceeds = qty * fill * (1 - fee)
        pnl = cash_after + proceeds - cash
        equity[e - lo:x - lo] = cash_after + qty * c[e:x]   # bars e..x-1 close while holding
        trades.append({
            "symbol": symbol, "entry_time": str(idx[e]), "exit_time": str(idx[x]),
            "entry_price": entry, "exit_price": fill, "qty": qty, "pnl": pnl,
            "pnl_pct_of_equity": pnl / cash * 100, "bars": x - e, "exit_reason": reason,
        })
        cash = cash_after + proceeds
        if open_at_end:
            equity[x - lo:] = cash
            break
        i = x
    eq = pd.Series(equity, index=idx[lo:hi]).ffill().fillna(capital)
    return trades, eq


def _bounds(idx: pd.DatetimeIndex, period: str) -> tuple[int, int]:
    ts = lambda s: pd.Timestamp(s, tz="UTC") if s else None  # noqa: E731
    start, oos, end = ts(CONFIG["start"]), ts(CONFIG["oos_start"]), ts(CONFIG.get("end"))
    if end is not None:
        end = end + pd.Timedelta(days=1)           # "end" is the last included day
    a, b = {"is": (start, oos), "oos": (oos, end), "all": (start, end), "live": (start, None)}[period]
    lo = idx.searchsorted(a) if a is not None else 0
    hi = idx.searchsorted(b) if b is not None else len(idx)
    if period != "oos":
        lo = max(lo, int(CONFIG.get("warmup_bars", 0)))
    return int(lo), int(hi)


def run(params: dict | None = None, period: str = "is", symbols: list[str] | None = None) -> dict:
    """Backtest one parameter set on one period ("is", "oos", "all", "live").
    The symbol list is one breadth portfolio (see _simulate_portfolio). Returns {"metrics", "trades", "equity"}."""
    p = {**PARAMS, **(params or {})}
    syms = sorted(symbols or CONFIG["symbols"])          # alphabetical = deterministic order
    P = _panel(tuple(syms))
    lo, hi = _bounds(P["idx"], period)
    if hi - lo < 2:
        raise ValueError(f"no bars for period {period}")
    all_trades, equity = _simulate_portfolio(P, syms, p, lo, hi, CONFIG["capital"])
    bh = []
    for j, s in enumerate(syms):                         # buy & hold of each symbol listed in the period
        oc = P["open"][lo:hi, j]
        cc = P["close"][lo:hi, j]
        ok = np.flatnonzero(~np.isnan(oc))
        if ok.size:
            bh.append(cc[~np.isnan(cc)][-1] / oc[ok[0]] - 1)
    all_trades.sort(key=lambda t: t["exit_time"])
    m = metrics(all_trades, equity, len(syms))
    m["open_positions"] = [{"symbol": t["symbol"], "since": t["entry_time"], "entry_price": round(t["entry_price"], 6)}
                           for t in all_trades if t["exit_reason"] == "end"]
    m["buy_hold_return_pct"] = round(float(np.mean(bh)) * 100, 2)
    return {"metrics": m, "trades": all_trades, "equity": equity}


def metrics(trades: list[dict], equity: pd.Series, n_symbols: int = 1) -> dict:
    pnl = np.array([t["pnl"] for t in trades], float)
    loss_pct = np.array([t["pnl_pct_of_equity"] for t in trades if t["pnl"] <= 0], float)
    big_thr = max(CONFIG["big_loss_pct"], CONFIG.get("big_loss_mult", 0) * abs(float(np.median(loss_pct))) if len(loss_pct) else 0.0)
    years = max((equity.index[-1] - equity.index[0]).days / 365.25, 1 / 365.25)
    growth = 1 + pnl.sum() / CONFIG["capital"]
    wins, losses = pnl[pnl > 0], pnl[pnl <= 0]
    gp, gl = float(wins.sum()), float(-losses.sum())
    dd = equity / equity.cummax() - 1
    dd_abs = (equity - equity.cummax()).min()
    worst = min(trades, key=lambda t: t["pnl"]) if trades else None
    cap = CONFIG["capital"]
    r = lambda v, d=2: round(float(v), d)  # noqa: E731
    return {
        "start": str(equity.index[0]), "end": str(equity.index[-1]),
        "net_profit": r(pnl.sum()), "return_pct": r(pnl.sum() / cap * 100),
        "yearly_return_pct": r((growth ** (1 / years) - 1) * 100 if growth > 0 else -100.0), "years": r(years),
        "gross_profit": r(gp), "gross_loss": r(gl),
        "n_trades": len(pnl), "win_rate": r(len(wins) / len(pnl) * 100 if len(pnl) else 0.0),
        "avg_win": r(wins.mean() if len(wins) else 0.0), "avg_loss": r(losses.mean() if len(losses) else 0.0),
        "avg_trade": r(pnl.mean() if len(pnl) else 0.0),
        "largest_loss": r(min(0.0, pnl.min()) if len(pnl) else 0.0),
        "largest_loss_pct": r(min(0.0, worst["pnl_pct_of_equity"]) if worst else 0.0),
        "max_dd": r(dd_abs), "max_dd_pct": r(dd.min() * 100),
        "profit_factor": r(gp / gl, 3) if gl > 0 else (999.0 if gp > 0 else 0.0),
        "n_big_losses": int(sum(t["pnl_pct_of_equity"] < -big_thr for t in trades)),
        "big_loss_threshold_pct": r(big_thr),
        "exposure_pct": r(sum(t["bars"] for t in trades) / max(1, len(equity)) / n_symbols * 100),
        "open_at_end": bool(trades and trades[-1]["exit_reason"] == "end"),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--period", choices=["is", "oos", "all", "live"], default="is")
    ap.add_argument("--symbols", default=None, help="comma-separated symbols instead of CONFIG['symbols']")
    ap.add_argument("--params", default="{}", help="JSON object overriding PARAMS")
    ap.add_argument("--trades", action="store_true", help="also print the trade list")
    a = ap.parse_args()
    p = {**PARAMS, **json.loads(a.params)}
    if not valid(p):
        sys.exit(f"invalid params: {p}")
    res = run(p, a.period, a.symbols.split(",") if a.symbols else None)
    out = {"config": CONFIG, "params": p, "period": a.period, "metrics": res["metrics"]}
    if a.trades:
        out["trades"] = res["trades"]
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
