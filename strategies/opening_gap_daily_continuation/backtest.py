"""Generic trade-level backtest template (long-only, one position per symbol).

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
# opening_gap_daily_continuation: research-library spec (original.md), formalized in strategy.md.
# --------------------------------------------------------------------------
CONFIG = {
    'name': 'opening_gap_daily_continuation',
    'asset_class': 'etf',
    'symbols': ['NVDA'],
    'timeframe': '1d',
    'start': '1995-01-01',
    'oos_start': '2016-01-01',
    'end': '2026-11-23',
    'capital': 10000.0,
    'position_pct': 1.0,
    'fee_pct': 0.05,
    'slippage_pct': 0.03,
    'big_loss_pct': 2.0,
    'big_loss_mult': 2.0,
    'warmup_bars': 100,
}

# Spec start values. Exits: stop/target = entry fill -/+ k * ATR(14) of the signal bar (frozen),
# max_candles = completed held bars (entry bar = 1). risk_fraction not used: 100% of equity per trade.
PARAMS = {
    'gap': 1.0,
    'stop_atr': 2.0,
    'take_profit_atr': 3.0,
    'max_candles': 48,
}

SPACE = {
    'gap': {"min": 0.5, "max": 3.0, "step": 0.25, "hard_min": 0.0},
    'stop_atr': {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    'take_profit_atr': {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    'max_candles': {"min": 24, "max": 96, "step": 6, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return bool(True) and p['stop_atr'] > 0 and p['take_profit_atr'] > 0 and p['max_candles'] >= 1

# ---- indicators, as defined in INDICATORS.md (Wilder RMA / EMA seeded with the SMA of the
# first n valid values; population std; flat denominators as the spec says) ----------------
_MEMO: dict = {}   # per-frame LRU caches by indicator kind: frames are cached in _BARS, so id(df) is stable
_MEMO_CAP = {"reg": 300}   # regression frames are large; everything else keeps up to 1500 entries per kind


def _memo(key, fn):
    from collections import OrderedDict
    c = _MEMO.setdefault(key[0], OrderedDict())
    if key in c:
        c.move_to_end(key)
        return c[key]
    v = c[key] = fn()
    if len(c) > _MEMO_CAP.get(key[0], 1500):
        c.popitem(last=False)
    return v


def _seeded_ewm(x: pd.Series, n: int, alpha: float) -> pd.Series:
    x = x.astype(float)
    v = x.dropna()
    if len(v) < n:
        return pd.Series(np.nan, index=x.index)
    pos = x.index.get_loc(v.index[n - 1])
    tail = x.iloc[pos:].copy()
    tail.iloc[0] = v.iloc[:n].mean()
    out = tail.ewm(alpha=alpha, adjust=False, ignore_na=True).mean()
    return pd.concat([pd.Series(np.nan, index=x.index[:pos]), out])


def _rma(x: pd.Series, n: int) -> pd.Series:
    return _seeded_ewm(x, n, 1 / n)


def _ema(x: pd.Series, n: int) -> pd.Series:
    return _seeded_ewm(x, n, 2 / (n + 1))


def _sma(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(n, min_periods=n).mean()


def _std(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(n, min_periods=n).std(ddof=0)


def _crosses_above(x: pd.Series, y) -> pd.Series:
    y1 = y.shift(1) if isinstance(y, pd.Series) else y
    return (x > y) & (x.shift(1) <= y1)


def buy_signal(df, p):
    o, h, c, v = df["open"], df["high"], df["close"], df["volume"]
    return (o > h.shift(1) * (1 + p["gap"] / 100)) & (c > o) & (v > 1.5 * _sma(v, 20).shift(1))


def sell_signal(df, p):
    return df["close"] < _ema(df["close"], 10)


# --------------------------------------------------------------------------
# Generic machinery below. Library change: _simulate replaced by the ATR-exit engine
# (see the block comment above it) and the entry veto in run().
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


# Library engine block: replaces the template's _simulate (and the call in run()).
# Spec exits (EXECUTION.md): stop = E - stop_atr*A, target = E + take_profit_atr*A, with
# E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen at entry; time exit after
# max_candles completed held bars (entry bar = 1) at the next open; entry skipped if A<=0 or
# stop<=0; stop before target in the same bar; a target fills at its level (never better);
# after an intrabar stop/target exit, one fully flat bar must complete before a new signal.
# Entry veto (signal exit already true on the signal bar) is applied in run().


def _atr14(df: pd.DataFrame) -> np.ndarray:
    key = ("atr14", id(df))
    if key not in _BARS:
        h, l, c = df["high"], df["low"], df["close"]
        pc = c.shift(1)
        tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
        tr.iloc[0] = np.nan
        _BARS[key] = _rma(tr, 14).to_numpy(float)
    return _BARS[key]


def _simulate(df: pd.DataFrame, buy: np.ndarray, sell: np.ndarray, p: dict, lo: int, hi: int, capital: float, symbol: str):
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    atr = _atr14(df)
    k_sl, k_tp = float(p.get("stop_atr", 0) or 0), float(p.get("take_profit_atr", 0) or 0)
    max_bars = int(p.get("max_candles", 0) or 0)
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
        A = atr[s]
        sl_lvl = entry - k_sl * A if k_sl else -np.inf
        if not np.isfinite(A) or A <= 0 or (k_sl and not sl_lvl > 0):
            equity[i - lo:e - lo] = cash             # skip: invalid ATR or non-positive stop
            i = e
            continue
        tp_lvl = entry + k_tp * A if k_tp else np.inf
        equity[i - lo:e - lo] = cash
        stake = cash * CONFIG["position_pct"]
        qty = stake / (entry * (1 + fee))
        cash_after = cash - qty * entry * (1 + fee)
        x, price, reason = None, None, None
        j = e
        while j < hi:
            if max_bars and j - e >= max_bars:
                x, price, reason = j, o[j], "max_bars"
                break
            if l[j] <= sl_lvl:
                x, price, reason = j, min(o[j], sl_lvl), "stop"
                break
            if h[j] >= tp_lvl:
                x, price, reason = j, tp_lvl, "target"
                break
            if sell[j] and j + 1 < hi:
                x, price, reason = j + 1, o[j + 1], "signal"
                break
            j += 1
        open_at_end = x is None
        if open_at_end:
            x, price, reason = hi - 1, c[hi - 1], "end"
        fill = price * (1 - slip)
        proceeds = qty * fill * (1 - fee)
        pnl = cash_after + proceeds - cash
        equity[e - lo:x - lo] = cash_after + qty * c[e:x]
        trades.append({
            "symbol": symbol, "entry_time": str(idx[e]), "exit_time": str(idx[x]),
            "entry_price": entry, "exit_price": fill, "qty": qty, "pnl": pnl,
            "pnl_pct_of_equity": pnl / cash * 100, "bars": x - e, "exit_reason": reason,
        })
        cash = cash_after + proceeds
        if open_at_end:
            equity[x - lo:] = cash
            break
        i = x + 1 if reason in ("stop", "target") else x   # intrabar exit: bar x isn't a flat bar
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
        buy = buy & ~sell                             # entry veto: exit already true on the signal bar
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
