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
# --------------------------------------------------------------------------
def _exits_space(mc_lo, mc_hi, mc_step):
    return {
        "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
        "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
        "max_candles": {"min": mc_lo, "max": mc_hi, "step": mc_step, "hard_min": 1},
    }


# ---- indicators (INDICATORS.md conventions) -------------------------------
_MEMO: dict = {}   # per-frame cache: frames live in _BARS, so id(df) is stable


def _memo(key, fn):
    if key not in _MEMO:
        if len(_MEMO) > 4000:
            _MEMO.clear()
        _MEMO[key] = fn()
    return _MEMO[key]


def _seeded(x: pd.Series, n: int, alpha: float) -> pd.Series:
    """Recursive average seeded with the SMA of the first n valid values (EMA / Wilder RMA)."""
    x = x.astype(float)
    v = x.to_numpy(float)
    valid = np.flatnonzero(np.isfinite(v))
    out = np.full(len(v), np.nan)
    if len(valid) < n:
        return pd.Series(out, index=x.index)
    f = valid[0]
    seg = v[f:]
    if not np.all(np.isfinite(seg[:n])):          # gaps inside the seed window: no value
        return pd.Series(out, index=x.index)
    y = seg.copy()
    y[:n - 1] = np.nan
    y[n - 1] = seg[:n].mean()
    s = pd.Series(y).ewm(alpha=alpha, adjust=False, ignore_na=True).mean().to_numpy().copy()
    s[:n - 1] = np.nan
    out[f:] = s
    return pd.Series(out, index=x.index)


def _ema(x: pd.Series, n: int) -> pd.Series:
    return _seeded(x, int(n), 2.0 / (int(n) + 1))


def _rma(x: pd.Series, n: int) -> pd.Series:
    return _seeded(x, int(n), 1.0 / int(n))


def _sma(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(int(n), min_periods=int(n)).mean()


def _tr(df: pd.DataFrame) -> pd.Series:
    pc = df["close"].shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()], axis=1).max(axis=1)
    tr.iloc[0] = np.nan                           # first bar has no previous close
    return tr


def _atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return _memo(("atr", id(df), int(n)), lambda: _rma(_tr(df), n))


def _c_sma(df, n):
    return _memo(("sma", id(df), int(n)), lambda: _sma(df["close"], n))


def _c_ema(df, n):
    return _memo(("ema", id(df), int(n)), lambda: _ema(df["close"], n))


def _xabove(a, b) -> pd.Series:
    """a crosses above b: a[t] > b[t] and a[t-1] <= b[t-1] (b may be a constant)."""
    b1 = b.shift(1) if isinstance(b, pd.Series) else b
    return (a > b) & (a.shift(1) <= b1)


def _xbelow(a, b) -> pd.Series:
    b1 = b.shift(1) if isinstance(b, pd.Series) else b
    return (a < b) & (a.shift(1) >= b1)


def aux(df: pd.DataFrame, p: dict) -> dict:
    """Per-bar inputs for the entry-dependent exits in _simulate: ATR(14) of the signal bar."""
    return {"atr": _atr(df, 14).to_numpy(float)}


CONFIG = {
    "name": "macd_signal_cross",
    "asset_class": "etf",           # Yahoo daily, dividend/split adjusted
    "symbols": ['AAPL'],
    "timeframe": "1d",
    "start": "1995-01-01",
    "oos_start": "2016-01-01",      # repo precedent for ETF/stock strategies
    "end": "2026-11-23",            # frozen at setup (last daily bar)
    "capital": 10_000.0,
    "position_pct": 1.0,            # user's choice: 100% of equity (spec's risk_fraction sizing not used)
    "fee_pct": 0.05,
    "slippage_pct": 0.03,
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 250,             # >= 5x the longest recursive period and the longest window at range max
}

# Default parameter values (the spec's Start column).
PARAMS = {'signal': 9, 'stop_atr': 2.0, 'take_profit_atr': 3.0, 'max_candles': 96}

SPACE = {
    'signal': {'min': 5, 'max': 15, 'step': 1, 'hard_min': 2},
    **_exits_space(48, 192, 8),
}


def valid(p: dict) -> bool:
    return (True) and p["stop_atr"] > 0 and p["take_profit_atr"] > 0 and p["max_candles"] >= 1


def _macd(df):
    return _memo(("macd", id(df)), lambda: _c_ema(df, 12) - _c_ema(df, 26))


def buy_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """True on bars whose close triggers a buy (filled at the next open)."""
    m = _macd(df)
    return _xabove(m, _ema(m, p["signal"])) & (df["close"] > _c_sma(df, 200))


def sell_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """True on bars whose close triggers a sell of an open position (filled at the next open)."""
    m = _macd(df)
    return _xbelow(m, _ema(m, p["signal"]))

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


def _simulate(df: pd.DataFrame, buy: np.ndarray, sell: np.ndarray, p: dict, lo: int, hi: int, capital: float, symbol: str,
              ax: dict | None = None):
    # Library adaptation (EXECUTION.md): stop = E - stop_atr*A and target = E + take_profit_atr*A,
    # A = ATR(14) of the signal bar, both frozen at entry; skip the entry if A <= 0/NaN or stop <= 0.
    # max_candles = time exit at the open after N completed held bars (entry bar = 1).
    # After an intrabar stop/target exit the next signal may come from the following bar on
    # (one fully flat bar). The entry veto (buy & ~sell) is applied in run().
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    sl, tp = p.get("stop_loss_pct", 0) / 100, p.get("take_profit_pct", 0) / 100
    trail, max_bars = p.get("trailing_stop_pct", 0) / 100, int(p.get("max_bars", 0) or p.get("max_candles", 0) or 0)
    atr = ax["atr"] if ax else None
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
        sl_lvl = tp_lvl = None
        if atr is not None:
            A = atr[s]
            sl_lvl = entry - p["stop_atr"] * A if np.isfinite(A) else np.nan
            if not np.isfinite(A) or A <= 0 or not sl_lvl > 0:
                equity[i - lo:e - lo] = cash        # skip: invalid ATR or non-positive stop
                i = e
                continue
            tp_lvl = entry + p["take_profit_atr"] * A
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
            if sl_lvl is not None and l[j] <= sl_lvl:
                x, price, reason = j, min(o[j], sl_lvl), "stop"
                break
            if tp_lvl is not None and h[j] >= tp_lvl:
                x, price, reason = j, max(o[j], tp_lvl), "target"
                break
            if tp and h[j] >= entry * (1 + tp):
                x, price, reason = j, max(o[j], entry * (1 + tp)), "target"
                break
            peak = max(peak, h[j])
            if sell[j] and j + 1 < hi:
                x, price, reason = j + 1, o[j + 1], "signal"
                break
            j += 1
            if not (sl or tp or trail or max_bars or atr is not None):  # pure signal exit: jump straight to it
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
        i = x + 1 if reason in ("stop", "target") else x   # intrabar exit: bar x was not fully flat
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
        buy = buy & ~sell                          # entry veto: exit condition already true
        t, eq = _simulate(df, buy, sell, p, lo, hi, per_cap, sym, aux(df, p))
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
