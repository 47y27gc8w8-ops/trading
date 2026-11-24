"""anchored_vwap_breakout_reclaim: adapted copy of strategies/backtest.py (long-only, one position per symbol).

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
    "name": "anchored_vwap_breakout_reclaim",
    "asset_class": "crypto",        # Binance USDT spot pairs
    "symbols": ["BTCUSDT"],         # spec: BTC/USD spot -> Binance BTCUSDT
    "timeframe": "1h",              # spec signal timeframe, built from 1m bars (UTC)
    "start": "2018-01-01",          # BTC 1m data from 2017-08-17; leaves warm-up
    "oos_start": "2024-01-01",      # repo precedent for crypto strategies
    "end": "2026-11-23",            # frozen at setup: last complete day
    "capital": 10_000.0,
    "position_pct": 1.0,            # user's choice for library specs: 100% of equity (risk_fraction sizing not used)
    "fee_pct": 0.10,                # EXECUTION.md crypto commission 10 bps per side
    "slippage_pct": 0.10,           # EXECUTION.md crypto half-spread 5 bps + adverse slippage 5 bps (market/stop fills)
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 400,             # > n at its widest possible range (168 * 1.25^3 = 328) and 5 x ATR(14)
}

# Spec start values. risk_fraction is not a parameter here (100%-equity sizing).
PARAMS = {
    "n": 48,                 # breakout lookback: C[t-2] > max(H over the n bars before t-2)
    "stop_atr": 2.0,         # stop = entry fill - stop_atr * ATR(14) of the signal bar
    "take_profit_atr": 3.0,  # target = entry fill + take_profit_atr * the same ATR
    "max_candles": 48,       # exit at the next open after this many completed held bars
}

SPACE = {
    "n": {"min": 24, "max": 168, "step": 12, "hard_min": 2},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 24, "max": 96, "step": 6, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return p["n"] >= 2 and p["stop_atr"] > 0 and p["take_profit_atr"] > 0 and p["max_candles"] >= 1


_MEMO: dict = {}   # per-frame cache (frames are cached in _BARS, so id() is stable)


def _memo(key, fn):
    if key not in _MEMO:
        _MEMO[key] = fn()
    return _MEMO[key]


def _atr14(df: pd.DataFrame) -> np.ndarray:
    """ATR(14) = Wilder RMA of true range, seeded with the SMA of the first 14 values (INDICATORS.md)."""
    def calc():
        h, l, c = (df[k].to_numpy(float) for k in ("high", "low", "close"))
        pc = np.r_[np.nan, c[:-1]]
        tr = np.nanmax(np.vstack([h - l, np.abs(h - pc), np.abs(l - pc)]), axis=0)
        tr[0] = h[0] - l[0]
        out = np.full(len(tr), np.nan)
        n = 14
        if len(tr) >= n:
            prev = tr[:n].mean()
            out[n - 1] = prev
            for i in range(n, len(tr)):
                prev += (tr[i] - prev) / n
                out[i] = prev
        return out
    return _memo(("atr", id(df)), calc)


def _vwap_sums(df: pd.DataFrame) -> tuple:
    """Prefix sums for anchored VWAP = sum(TP*V)/sum(V) with base-unit volume V.
    The bars carry quote volume Q (USDT); V is approximated as Q/TP, so TP*V = Q.
    Returns (P, W): P[k] = sum of Q over bars < k, W[k] = sum of Q/TP over bars < k."""
    def calc():
        q = df["volume"].to_numpy(float)
        tp = ((df["high"] + df["low"] + df["close"]) / 3).to_numpy(float)
        w = np.where(tp > 0, q / np.where(tp > 0, tp, 1.0), 0.0)
        return np.r_[0.0, np.cumsum(q)], np.r_[0.0, np.cumsum(w)]
    return _memo(("vw", id(df)), calc)


def anchored_vwap(df: pd.DataFrame, anchor: int, j: int) -> float:
    """VWAP of bars anchor..j inclusive (NaN if no volume)."""
    P, W = _vwap_sums(df)
    den = W[j + 1] - W[anchor]
    return (P[j + 1] - P[anchor]) / den if den > 0 else np.nan


def buy_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """At t: bar t-2 closed above the highest high of the n bars before it (anchor = t-2),
    bar t-1 closed below the VWAP anchored at t-2, bar t closes above that VWAP and above its open.
    Also requires ATR(14) > 0 on bar t (stop/target need it)."""
    n = int(p["n"])
    c, o = df["close"], df["open"]
    brk = c > df["high"].rolling(n).max().shift(1)          # breakout at this bar
    q = df["volume"]
    tp = (df["high"] + df["low"] + df["close"]) / 3
    w = (q / tp).where(tp > 0, 0.0)
    av_prev = (q.rolling(2).sum() / w.rolling(2).sum()).shift(1)   # VWAP of bars t-2..t-1
    av_now = q.rolling(3).sum() / w.rolling(3).sum()                # VWAP of bars t-2..t
    atr = pd.Series(_atr14(df), index=df.index)
    return brk.shift(2, fill_value=False) & (c.shift(1) < av_prev) & (c > av_now) & (c > o) & (atr > 0)


def sell_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Unused: the exit (close below the VWAP anchored at the entry's breakout bar) depends on
    the entry, so _simulate evaluates it per trade."""
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
    """Adapted for this spec (EXECUTION.md):
    - entry at the open after the signal bar s; E = actual fill (incl. slippage);
      stop S = E - stop_atr * ATR14[s], target T = E + take_profit_atr * ATR14[s], both frozen;
      the signal is skipped if S <= 0.
    - per held bar j, in this order: time exit at the open once max_candles bars are held;
      stop (intrabar low; a gap below fills at the open; less slippage); target (resting limit:
      fills at T exactly, commission only, no slippage, also on a favourable gap); stop wins if
      both are touched in one bar; signal exit = close below the VWAP anchored at bar s-2,
      filled at the next open.
    - re-entry needs one fully completed flat bar: after an intrabar stop/target in bar j the
      next signal may come from bar j+1 at the earliest; after an exit at an open, from that bar."""
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    atr = _atr14(df)
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    k_sl, k_tp, max_c = float(p["stop_atr"]), float(p["take_profit_atr"]), int(p["max_candles"])
    idx = df.index
    cash, trades = capital, []
    equity = np.full(hi - lo, np.nan)
    i = lo
    while True:
        s = _first(buy, i)
        if s < 0 or s + 1 >= hi:
            equity[i - lo:] = cash
            break
        e = s + 1
        entry = o[e] * (1 + slip)
        stop, target = entry - k_sl * atr[s], entry + k_tp * atr[s]
        equity[i - lo:e - lo] = cash
        if not (stop > 0) or s < 2:
            i = e
            continue
        anchor = s - 2
        qty = cash * CONFIG["position_pct"] / (entry * (1 + fee))
        cash_after = cash - qty * entry * (1 + fee)
        x, fill, reason, nxt = None, None, None, None
        j = e
        while j < hi:
            if j - e >= max_c:
                x, fill, reason, nxt = j, o[j] * (1 - slip), "max_bars", j
                break
            if l[j] <= stop:
                x, fill, reason, nxt = j, min(o[j], stop) * (1 - slip), "stop", j + 1
                break
            if h[j] >= target:
                x, fill, reason, nxt = j, target, "target", j + 1
                break
            if j + 1 < hi and c[j] < anchored_vwap(df, anchor, j):
                x, fill, reason, nxt = j + 1, o[j + 1] * (1 - slip), "signal", j + 1
                break
            j += 1
        open_at_end = x is None
        if open_at_end:
            x, fill, reason = hi - 1, c[hi - 1] * (1 - slip), "end"
        proceeds = qty * fill * (1 - fee)
        pnl = cash_after + proceeds - cash
        intrabar = reason in ("stop", "target")
        equity[e - lo:x - lo] = cash_after + qty * c[e:x]
        trades.append({
            "symbol": symbol, "entry_time": str(idx[e]), "exit_time": str(idx[x]),
            "entry_price": entry, "exit_price": fill, "qty": qty, "pnl": pnl,
            "pnl_pct_of_equity": pnl / cash * 100, "bars": x - e + (1 if intrabar else 0),
            "exit_reason": reason, "anchor_time": str(idx[anchor]),
            "stop": round(stop, 6), "target": round(target, 6),
        })
        cash = cash_after + proceeds
        if open_at_end:
            equity[x - lo:] = cash
            break
        if intrabar:
            equity[x - lo] = cash          # flat at the close of the exit bar
        i = nxt
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
    Returns {"metrics", "trades", "equity"}."""
    p = {**PARAMS, **(params or {})}
    syms = list(symbols or CONFIG["symbols"])
    per_cap = CONFIG["capital"] / len(syms)
    all_trades, curves, bh = [], [], []
    for sym in syms:
        df = load_bars(CONFIG["asset_class"], sym, CONFIG["timeframe"])
        lo, hi = _bounds(df.index, period)
        if hi - lo < 2:
            continue
        buy = buy_signal(df, p).fillna(False).to_numpy(bool)
        sell = sell_signal(df, p).fillna(False).to_numpy(bool)
        t, eq = _simulate(df, buy, sell, p, lo, hi, per_cap, sym)
        all_trades += t
        curves.append(eq)
        bh.append(df["close"].iloc[hi - 1] / df["open"].iloc[lo] - 1)
    if not curves:
        raise ValueError(f"no bars for period {period}")
    equity = pd.concat(curves, axis=1).sort_index().ffill()
    equity = equity.fillna(per_cap).sum(axis=1)
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
