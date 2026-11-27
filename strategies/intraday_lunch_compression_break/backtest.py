"""Intraday lunch compression break: US 5-minute single-position backtest adapted from the generic template.

Built by scripts/portfolio_lib/build_intraday.py (strategy block below + intraday_core.py: session
features, EXECUTION.md 5-minute execution rules, run() + the template's generic machinery).
Data: data/etf/5m/<SYMBOL>.parquet from Alpaca (scripts/fetch_alpaca_5m.py), regular session.

    docker compose run --rm -T backtest python strategies/intraday_lunch_compression_break/backtest.py --period is [--trades]
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
    "name": "intraday_lunch_compression_break",
    "asset_class": "etf",            # Alpaca SIP 5-minute bars, split + dividend adjusted
    "symbols": ["SPY"],
    "timeframe": "5min",             # regular session 09:30-16:00 America/New_York
    "start": "2016-03-01",           # Alpaca free history starts 2016; 2 months of warm-up
    "oos_start": "2023-01-01",       # last ~4 years held out
    "end": "2026-11-25",             # frozen at setup (last complete session)
    "capital": 10_000.0,
    "position_pct": 1.0,             # 100 % of equity per trade (user choice for risk_fraction specs)
    "fee_pct": 0.05,                 # library convention for US stocks/ETFs (spec: 1 bp commission; more conservative)
    "slippage_pct": 0.03,            # market/stop fills (spec: half-spread 2 bp + slippage 2 bp); target limits: none
    "max_entries_per_session": 1,   # spec: max one entry per session
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 0,                # indicators carry their own warm-up (NaN until ready)
}

PARAMS = {
    "k": 3.0,     # lunch range width must be < k x ATR(14) at 13:00
    "stop_atr": 2.0,         # initial stop, x ATR(14) of the signal bar below the fill
    "take_profit_atr": 3.0,  # resting target, x the same ATR above the fill
    "max_candles": 24,       # held 5-minute bars (entry bar = 1), exit at the next open
}

SPACE = {
    "k": {"min": 1.5, "max": 5.0, "step": 0.25, "hard_min": 0.25, "hard_max": 20.0},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25, "hard_max": 10.0},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.25, "hard_min": 0.25, "hard_max": 15.0},
    "max_candles": {"min": 12, "max": 48, "step": 2, "hard_min": 2, "hard_max": 78},
}


def valid(p: dict) -> bool:
    return (p["k"] > 0) and p["stop_atr"] > 0 and p["take_profit_atr"] > 0 and p["max_candles"] >= 1


def signals(F: dict, p: dict) -> dict:
    """Lunch range = bars 11:30-13:00, frozen with ATR(14) at the bar closing 13:00; width < k x that ATR.
    Bar closing after 13:00 up to 15:00: C crosses above the lunch high and C > VWAP.
    Exit C < lunch-range midpoint. One entry per session."""
    c = F["c"]
    lh, ll = range_frozen(F, 690, 780)
    atr13 = pd.Series(np.where(F["close_min"] == 780, F["atr"], np.nan)).groupby(F["sid"]).transform("max").to_numpy()
    with np.errstate(invalid="ignore"):
        ok = (lh - ll) < p["k"] * atr13
        e = ok & in_window(F, "13:05", "15:00") & cross_above(F, c, lh) & (c > F["vwap"])
        x = c < (lh + ll) / 2
    return {"entry": e, "exit": x}


# --------------------------------------------------------------------------
# Intraday machinery (shared by the library's US 5-minute specs). Built from
# scripts/portfolio_lib/intraday_core.py; signals() above decides, everything below executes.
# --------------------------------------------------------------------------
_FEAT: dict = {}


def _load_5m(symbol: str) -> pd.DataFrame:
    """Regular-session 5-minute bars (bar START in UTC) from data/etf/5m/<SYMBOL>.parquet
    (scripts/fetch_alpaca_5m.py). TSO_5M_DIR overrides the folder (used for tests)."""
    d = Path(os.environ.get("TSO_5M_DIR", str(ROOT / "data" / "etf" / "5m")))
    f = d / f"{symbol}.parquet"
    if not f.exists():
        raise ValueError(f"no 5-minute data for {symbol}: run scripts/fetch_alpaca_5m.py first")
    df = pd.read_parquet(f)
    df["date"] = pd.to_datetime(df["date"], utc=True)
    return df.set_index("date").sort_index()[["open", "high", "low", "close", "volume"]].astype(float)


def _rma(x: np.ndarray, n: int) -> np.ndarray:
    """Wilder RMA (alpha 1/n) seeded with the SMA of the first n valid values."""
    out = np.full(len(x), np.nan)
    v = np.flatnonzero(~np.isnan(x))
    if v.size < n:
        return out
    s = x[v]
    r = np.empty(len(s))
    r[: n - 1] = np.nan
    r[n - 1] = s[:n].mean()
    for t in range(n, len(s)):
        r[t] = r[t - 1] + (s[t] - r[t - 1]) / n
    out[v] = r
    return out


def features(symbol: str) -> dict:
    """Arrays over the symbol's 5-minute bars (all causal: values at bar t use bars <= t only)."""
    if symbol in _FEAT:
        return _FEAT[symbol]
    df = _load_5m(symbol)
    o, h, l, c, v = (df[k].to_numpy(float) for k in ("open", "high", "low", "close", "volume"))
    idx = df.index
    loc = idx.tz_convert("America/New_York")
    start = np.asarray(loc.hour * 60 + loc.minute)
    close_min = start + 5                                   # bars are labelled by their close time
    sess_key = np.asarray(loc.date)
    sid = pd.factorize(pd.Series(sess_key))[0]
    new = np.r_[True, sid[1:] != sid[:-1]]
    last = np.r_[sid[1:] != sid[:-1], True]
    first_i = np.maximum.accumulate(np.where(new, np.arange(len(sid)), 0))
    g = pd.DataFrame({"sid": sid, "o": o, "h": h, "l": l, "c": c})
    day = g.groupby("sid").agg(o=("o", "first"), h=("h", "max"), l=("l", "min"), c=("c", "last"))
    sess_close = pd.Series(close_min).groupby(sid).transform("max").to_numpy()
    prev = day.shift(1)                                    # prior regular session
    tp = (h + l + c) / 3
    cum_pv = pd.Series(tp * v).groupby(sid).cumsum().to_numpy()
    cum_v = pd.Series(v).groupby(sid).cumsum().to_numpy()
    with np.errstate(invalid="ignore", divide="ignore"):
        vwap = np.where(cum_v > 0, cum_pv / cum_v, np.nan)
    pc = np.r_[np.nan, c[:-1]]
    tr = np.nanmax(np.column_stack([h - l, np.abs(h - pc), np.abs(l - pc)]), axis=1)
    atr = _rma(tr, 14)
    atr[:70] = np.nan                                      # warm-up 5 x 14
    up, dn = h - np.r_[np.nan, h[:-1]], np.r_[np.nan, l[:-1]] - l
    pdm = np.where((up > dn) & (up > 0), up, 0.0)
    mdm = np.where((dn > up) & (dn > 0), dn, 0.0)
    pdm[0] = mdm[0] = np.nan
    with np.errstate(invalid="ignore", divide="ignore"):
        dip = np.where(atr > 0, 100 * _rma(pdm, 14) / atr, 0.0)
        dim = np.where(atr > 0, 100 * _rma(mdm, 14) / atr, 0.0)
        dx = np.where(dip + dim > 0, 100 * np.abs(dip - dim) / (dip + dim), 0.0)
    dx[np.isnan(atr)] = np.nan
    adx = _rma(dx, 14)
    slot = start
    vol_tab = pd.DataFrame({"sid": sid, "slot": slot, "v": v}).pivot_table(index="sid", columns="slot", values="v")
    med = vol_tab.rolling(20, min_periods=20).median().shift(1)   # 20 PRECEDING sessions, same slot
    slot_med = med.stack().reindex(pd.MultiIndex.from_arrays([sid, slot])).to_numpy(float)
    F = {"idx": idx, "o": o, "h": h, "l": l, "c": c, "v": v, "start": start, "close_min": close_min,
         "sid": sid, "new": new, "last": last, "first_i": first_i, "sess_close": sess_close,
         "sess_open": o[first_i], "prev_h": prev["h"].to_numpy()[sid], "prev_l": prev["l"].to_numpy()[sid],
         "prev_c": prev["c"].to_numpy()[sid], "vwap": vwap, "atr": atr, "adx": adx, "slot_med_vol": slot_med,
         "cache": {}}
    _FEAT[symbol] = F
    return F


def same_prev(F: dict, k: int = 1) -> np.ndarray:
    """True where bar t-k belongs to the same session as bar t."""
    s = F["sid"]
    out = np.zeros(len(s), bool)
    out[k:] = s[k:] == s[:-k]
    return out


def lag(x: np.ndarray, k: int = 1) -> np.ndarray:
    return np.r_[np.full(k, np.nan), x[:-k]]


def cross_above(F: dict, x: np.ndarray, level: np.ndarray) -> np.ndarray:
    """x[t] > level[t] and x[t-1] <= level[t-1], both bars in the same session (EXECUTION.md crosses)."""
    with np.errstate(invalid="ignore"):
        return (x > level) & (lag(x) <= lag(level)) & same_prev(F)


def in_window(F: dict, a: str, b: str) -> np.ndarray:
    """Bar close time (local) within [a, b], e.g. "10:30", "15:00"."""
    ta, tb = (int(s[:2]) * 60 + int(s[3:]) for s in (a, b))
    return (F["close_min"] >= ta) & (F["close_min"] <= tb)


def range_frozen(F: dict, from_min: int, to_min: int):
    """High/low of the session's bars starting in [from_min, to_min) local minutes, available (frozen)
    from the bar closing at to_min onward; NaN before. Returns (high, low)."""
    key = ("rng", from_min, to_min)
    if key not in F["cache"]:
        m = (F["start"] >= from_min) & (F["start"] < to_min)
        hh = pd.Series(np.where(m, F["h"], np.nan)).groupby(F["sid"]).transform("max").to_numpy()
        ll = pd.Series(np.where(m, F["l"], np.nan)).groupby(F["sid"]).transform("min").to_numpy()
        n_in = pd.Series(m.astype(int)).groupby(F["sid"]).transform("sum").to_numpy()
        ok = (F["close_min"] >= to_min) & (n_in == (to_min - from_min) // 5)   # complete range only
        F["cache"][key] = (np.where(ok, hh, np.nan), np.where(ok, ll, np.nan))
    return F["cache"][key]


def ema(F: dict, n: int) -> np.ndarray:
    """EMA(n) of close (alpha 2/(n+1), SMA seed), continuous across sessions; warm-up 5 x n bars."""
    key = ("ema", n)
    if key not in F["cache"]:
        c = F["c"]
        e = np.full(len(c), np.nan)
        if len(c) > n:
            e[n - 1] = c[:n].mean()
            a = 2 / (n + 1)
            for t in range(n, len(c)):
                e[t] = e[t - 1] + a * (c[t] - e[t - 1])
        e[: 5 * n] = np.nan
        F["cache"][key] = e
    return F["cache"][key]


def _simulate_intraday(F: dict, symbol: str, p: dict, lo: int, hi: int, capital: float):
    """One long position at a time (EXECUTION.md, US 5-minute rules). signals(F, p) -> entry, exit (bool).
    At bar t's close: entry (and not exit: entry veto), flat, not on a bar that closed a position,
    at most CONFIG["max_entries_per_session"] entries (0 = no limit) -> buy at the next open if that open
    is before the earlier of 15:00 and 60 minutes before the session close, and isn't the session's last bar.
    At entry: E = fill, A = ATR(14) of the signal bar; stop S = E - stop_atr A, target T = E + take_profit_atr A
    (skip if A <= 0 or S <= 0); neither moves. Order on every held bar:
      open: last bar of the session -> sell at the open (scheduled liquidation); pending exit -> open;
            open <= S -> open (gap); open >= T -> T (resting limit, never better than its limit)
      intrabar: low <= S -> S (stop first if both touched); high >= T -> T
      close: held bars (entry bar = 1) >= max_candles or exit signal -> sell at the next open.
    100 % of equity per trade (user's sizing choice for risk_fraction specs). Market and stop fills pay
    slippage, the target limit doesn't; every fill pays the fee."""
    sig = signals(F, p)
    entry, exit_ = sig["entry"], sig["exit"]
    o, h, l, c = F["o"], F["h"], F["l"], F["c"]
    atr, last, start, sess_close, sid = F["atr"], F["last"], F["start"], F["sess_close"], F["sid"]
    idx = F["idx"]
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    k_s, k_t, max_c = p["stop_atr"], p["take_profit_atr"], int(p["max_candles"])
    max_e = int(CONFIG.get("max_entries_per_session", 0))
    cash, qty = capital, 0.0
    pos = None
    pend_in = pend_out = None
    entries = {}
    trades, equity = [], np.full(hi - lo, np.nan)

    def sell(i, px, reason, slipped=True):
        nonlocal cash, qty, pos
        fill = px * (1 - slip) if slipped else px
        cash += qty * fill * (1 - fee)
        pnl = cash - pos["eq"]
        trades.append({"symbol": symbol, "entry_time": str(idx[pos["i"]]), "exit_time": str(idx[i]),
                       "entry_price": pos["E"], "exit_price": fill, "qty": qty, "pnl": pnl,
                       "pnl_pct_of_equity": pnl / pos["eq"] * 100, "bars": i - pos["i"], "exit_reason": reason})
        qty, pos = 0.0, None

    cand = np.flatnonzero(entry & ~exit_ & np.isfinite(atr))   # flat stretches are skipped to the next candidate
    i = lo - 1
    while True:
        i += 1
        if i >= hi:
            break
        if pos is None and pend_in is None:
            j = cand[np.searchsorted(cand, i)] if np.searchsorted(cand, i) < len(cand) else hi
            j = min(int(j), hi)
            equity[i - lo:j - lo] = cash
            i = j
            if i >= hi:
                break
        closed = False
        if pos is None and pend_in is not None:
            A = pend_in
            pend_in = None
            if not last[i] and start[i] < min(900, sess_close[i] - 60):
                E = o[i] * (1 + slip)
                S, T = E - k_s * A, E + k_t * A
                if A > 0 and S > 0:
                    eq0 = cash
                    qty = cash / (E * (1 + fee))
                    cash = 0.0
                    pos = {"i": i, "E": E, "S": S, "T": T, "eq": eq0}
                    entries[sid[i]] = entries.get(sid[i], 0) + 1
        elif pos is not None and pos["i"] < i:
            if last[i]:
                sell(i, o[i], "session_end"); closed = True
            elif pend_out is not None:
                sell(i, o[i], pend_out); closed = True
            elif o[i] <= pos["S"]:
                sell(i, o[i], "stop"); closed = True
            elif o[i] >= pos["T"]:
                sell(i, pos["T"], "target", slipped=False); closed = True
            pend_out = None
        if pos is not None and not closed:
            if l[i] <= pos["S"]:
                sell(i, pos["S"], "stop"); closed = True
            elif h[i] >= pos["T"]:
                sell(i, pos["T"], "target", slipped=False); closed = True
        if pos is not None:
            if i - pos["i"] + 1 >= max_c:
                pend_out = "max_bars"
            elif exit_[i]:
                pend_out = "signal"
        elif not closed and i + 1 < hi and entry[i] and not exit_[i] and np.isfinite(atr[i]):
            if max_e == 0 or entries.get(sid[i], 0) < max_e:
                pend_in = atr[i]
        equity[i - lo] = cash + qty * c[i]
    if pos is not None:
        sell(hi - 1, c[hi - 1], "end")
    return trades, pd.Series(equity, index=idx[lo:hi])


def run(params: dict | None = None, period: str = "is", symbols: list[str] | None = None) -> dict:
    """Backtest one parameter set on one period ("is", "oos", "all", "live"). Several symbols:
    capital split equally, each trades on its own (template convention)."""
    p = {**PARAMS, **(params or {})}
    syms = list(symbols or CONFIG["symbols"])
    per_cap = CONFIG["capital"] / len(syms)
    all_trades, curves, bh = [], [], []
    for s in syms:
        F = features(s)
        lo, hi = _bounds(F["idx"], period)
        if hi - lo < 2:
            continue
        t, eq = _simulate_intraday(F, s, p, lo, hi, per_cap)
        all_trades += t
        curves.append(eq)
        bh.append(F["c"][hi - 1] / F["o"][lo] - 1)
    if not curves:
        raise ValueError(f"no bars for period {period}")
    equity = pd.concat(curves, axis=1).sort_index().ffill().fillna(per_cap).sum(axis=1)
    all_trades.sort(key=lambda t: t["exit_time"])
    m = metrics(all_trades, equity, len(syms))
    m["open_positions"] = [{"symbol": t["symbol"], "since": t["entry_time"], "entry_price": round(t["entry_price"], 6)}
                           for t in all_trades if t["exit_reason"] == "end"]
    m["buy_hold_return_pct"] = round(float(np.mean(bh)) * 100, 2)
    return {"metrics": m, "trades": all_trades, "equity": equity}


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
