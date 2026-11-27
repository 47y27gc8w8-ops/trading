"""bond_duration_momentum_switch: monthly ROC rotation SHY/IEF/TLT or cash (adapted template copy).

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
CONFIG = {
    "name": "bond_duration_momentum_switch",
    "asset_class": "etf",           # Yahoo daily, dividend/split adjusted (= total return)
    "symbols": ["SHY", "IEF", "TLT"],   # the rotation universe (ONE portfolio, not separate trades per symbol)
    "timeframe": "1d",              # daily bars for fills and stop monitoring; decisions at month-end closes
    "start": "2003-07-01",          # data from 2002-07-30; ~230 daily bars of warm-up before the first decision
    "oos_start": "2016-01-01",      # repo precedent for ETF strategies
    "end": "2026-11-23",            # frozen at setup (last daily bar)
    "capital": 10_000.0,
    "position_pct": 1.0,            # spec: 100% of the sleeve in the selected ETF
    "fee_pct": 0.05,
    "slippage_pct": 0.03,
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 0,               # warm-up comes from "start"; a decision needs every member's ROC(n)
}

PARAMS = {
    "n": 63,                 # ROC lookback, daily bars
    "stop_loss_pct": 15.0,   # hard stop below each holding's entry fill
    "max_candles": 252,      # held daily bars (entry bar = 1) before a time exit at the next open
}

SPACE = {
    "n": {"min": 21, "max": 126, "step": 3, "hard_min": 5, "hard_max": 220},
    "stop_loss_pct": {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 1.0, "hard_max": 60.0},
    "max_candles": {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260},
}


def valid(p: dict) -> bool:
    return p["n"] >= 1 and p["stop_loss_pct"] > 0 and p["max_candles"] >= 1


_MEMO: dict = {}


def _memo(key, fn):
    if key not in _MEMO:
        _MEMO[key] = fn()
    return _MEMO[key]


def _universe(symbols: tuple) -> pd.DataFrame:
    """Aligned daily OHLC of the universe on the dates where every member has a bar
    (no forward fill). Columns are a (field, symbol) MultiIndex."""
    def build():
        frames = {s: load_bars(CONFIG["asset_class"], s, CONFIG["timeframe"]) for s in symbols}
        idx = None
        for f in frames.values():
            idx = f.index if idx is None else idx.intersection(f.index)
        return pd.concat({s: frames[s].loc[idx, ["open", "high", "low", "close"]] for s in symbols}, axis=1) \
                 .swaplevel(axis=1).sort_index(axis=1)
    return _memo(("u", symbols), build)


def _month_end(idx: pd.DatetimeIndex) -> np.ndarray:
    """True on the last daily bar of a calendar month that is complete in the data
    (the next bar exists and falls in a later month)."""
    per = pd.Series(idx.tz_localize(None).to_period("M"), index=idx)
    nxt = per.shift(-1)
    return (per.ne(nxt) & nxt.notna()).to_numpy(bool)


def _targets(symbols: tuple, n: int) -> np.ndarray:
    """Month-end decision per bar: -2 = no decision (not a month end, or a member lacks ROC(n)
    history -> skip the rebalance), -1 = cash (leader's ROC <= 0), k >= 0 = hold symbols[k].
    Leader = highest ROC(n) on total-return closes; ties go to the alphabetically first ticker."""
    def build():
        u = _universe(symbols)
        close = u["close"][list(symbols)].to_numpy(float)
        roc = np.full_like(close, np.nan)
        roc[n:] = close[n:] / close[:-n] - 1
        me = _month_end(u.index)
        order = np.argsort(np.array(symbols))           # alphabetical tie-break
        out = np.full(len(u), -2, dtype=int)
        for t in np.flatnonzero(me):
            r = roc[t]
            if not np.all(np.isfinite(r)):
                continue
            best = order[np.argmax(r[order])]           # argmax returns the first max in alphabetical order
            out[t] = best if r[best] > 0 else -1
        return out
    return _memo(("t", symbols, n), build)


def buy_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Not used by the rotation simulator (see run()); kept for the template interface."""
    return pd.Series(False, index=df.index)


def sell_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Not used by the rotation simulator (see run()); kept for the template interface."""
    return pd.Series(False, index=df.index)

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


def _simulate_rotation(u: pd.DataFrame, symbols: tuple, p: dict, lo: int, hi: int, capital: float):
    """bond_duration_momentum_switch: one portfolio that holds at most one universe member.
    Bar j's open processes, in order: time exit / month-end rebalance sell (reported as "stop" if
    the open gaps through the stop), then the rebalance buy (never the ticker that was time-exited
    at this same open). During bar j: hard stop at E*(1-stop_loss_pct/100) on the low, active from
    the entry bar. Decisions only happen at month ends, so a stopped holding stays out until then."""
    cols = list(symbols)
    o = u["open"][cols].to_numpy(float)
    l = u["low"][cols].to_numpy(float)
    c = u["close"][cols].to_numpy(float)
    idx = u.index
    tgt = _targets(symbols, int(p["n"]))
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    sl, max_c = p["stop_loss_pct"] / 100, int(p["max_candles"])
    st = {"cash": capital, "k": -1, "qty": 0.0, "E": 0.0, "S": 0.0, "age": 0, "e": 0, "eq": 0.0}
    trades, equity = [], np.empty(hi - lo)

    def close_pos(j, price, reason):
        fill = price * (1 - slip)
        proceeds = st["qty"] * fill * (1 - fee)
        pnl = proceeds - st["eq"]
        trades.append({"symbol": symbols[st["k"]], "entry_time": str(idx[st["e"]]), "exit_time": str(idx[j]),
                       "entry_price": st["E"], "exit_price": fill, "qty": st["qty"], "pnl": pnl,
                       "pnl_pct_of_equity": pnl / st["eq"] * 100, "bars": j - st["e"], "exit_reason": reason})
        st["cash"] += proceeds
        st["k"], st["qty"] = -1, 0.0

    for j in range(lo, hi):
        decision = tgt[j - 1] if j - 1 >= lo else -2      # decided at the previous close, inside the period
        blocked = -1
        k = st["k"]
        if k >= 0:
            why = "max_bars" if st["age"] >= max_c else ("signal" if decision != -2 and decision != k else None)
            if why:
                if why == "max_bars":
                    blocked = k
                close_pos(j, o[j, k], "stop" if o[j, k] <= st["S"] else why)
        if st["k"] < 0 and decision >= 0 and decision != blocked:
            k = decision
            E = o[j, k] * (1 + slip)
            qty = st["cash"] * CONFIG["position_pct"] / (E * (1 + fee))
            st.update(k=k, E=E, S=E * (1 - sl), qty=qty, age=0, e=j, eq=st["cash"])
            st["cash"] -= qty * E * (1 + fee)
        k = st["k"]
        if k >= 0 and l[j, k] <= st["S"]:                  # intrabar stop (gap below -> open)
            close_pos(j, min(o[j, k], st["S"]), "stop")
        k = st["k"]
        if k >= 0:
            st["age"] += 1
            equity[j - lo] = st["cash"] + st["qty"] * c[j, k]
        else:
            equity[j - lo] = st["cash"]
    if st["k"] >= 0:
        close_pos(hi - 1, c[hi - 1, st["k"]], "end")
        trades[-1]["bars"] += 1                            # the last bar was held too
        equity[-1] = st["cash"]
    return trades, pd.Series(equity, index=idx[lo:hi])


def run(params: dict | None = None, period: str = "is", symbols: list[str] | None = None) -> dict:
    """Backtest one parameter set on one period ("is", "oos", "all", "live").
    bond_duration_momentum_switch: the symbols are ONE rotation universe (capital is not split).
    Returns {"metrics", "trades", "equity"}."""
    p = {**PARAMS, **(params or {})}
    syms = tuple(symbols or CONFIG["symbols"])
    u = _universe(syms)
    lo, hi = _bounds(u.index, period)
    if hi - lo < 2:
        raise ValueError(f"no bars for period {period}")
    trades, equity = _simulate_rotation(u, syms, p, lo, hi, CONFIG["capital"])
    trades.sort(key=lambda t: t["exit_time"])
    m = metrics(trades, equity, 1)
    m["open_positions"] = [{"symbol": t["symbol"], "since": t["entry_time"], "entry_price": round(t["entry_price"], 6)}
                           for t in trades if t["exit_reason"] == "end"]
    bh = [u["close"][s].iloc[hi - 1] / u["open"][s].iloc[lo] - 1 for s in syms]
    m["buy_hold_return_pct"] = round(float(np.mean(bh)) * 100, 2)
    return {"metrics": m, "trades": trades, "equity": equity}


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
