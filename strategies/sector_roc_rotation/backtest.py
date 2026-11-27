"""Sector ROC rotation: month-end portfolio backtest adapted from the generic template.

Built by scripts/portfolio_lib/build.py (strategy block below + shared portfolio simulator
core.py + the template's generic machinery). The symbol list is ONE portfolio, not independent
per-symbol trades, so run() uses _simulate_portfolio instead of the template's per-symbol _simulate.

    docker compose run --rm -T backtest python strategies/sector_roc_rotation/backtest.py --period is [--trades]
    ... --period oos | all | live    --params '{"stop_loss_pct": 12}'

Rules (EXECUTION.md "Sizing and portfolio sleeves", see strategy.md):
- Decide at the close of the last bar of each complete month; fill at the next bar's open.
- Sells/trims first, then buys to target; buys scaled down if cash is short. Rest is cash (0 %).
- Each holding: hard stop stop_loss_pct below its cost basis (gap -> open, else intrabar at the
  stop; never loosened on additions), time exit after max_candles held bars at the next open.
  A stopped holding can only come back at a later month-end decision.
- Fees CONFIG["fee_pct"] per side on traded value, slippage CONFIG["slippage_pct"] against every fill.
- A trade = one holding from first buy to full exit; partial trims don't close it.
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
    "name": "sector_roc_rotation",
    "asset_class": "etf",               # Yahoo daily, dividend/split adjusted (= total return)
    "symbols": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "reference": ["SPY"],   # signal-only series, never traded
    "timeframe": "1d",               # daily bars for fills and stop monitoring; decisions at month-end
    "start": "2000-07-01",           # first simulated bar; members join once listed and warmed up
    "oos_start": "2016-01-01",
    "end": "2026-11-23",             # frozen at setup (last complete daily bar)
    "capital": 10_000.0,
    "position_pct": 1.0,             # whole sleeve, split by target_weights()
    "fee_pct": 0.05,                # library convention for US ETFs (spec: 1 bp commission; more conservative)
    "slippage_pct": 0.03,           # spec: half-spread 2 bp + slippage 2 bp per fill
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 0,                # not used: a member is eligible once its indicators exist
}

PARAMS = {
    "k": 3,      # holdings
    "n": 63,     # ROC lookback (daily bars)
    "stop_loss_pct": 15.0,   # hard stop below each holding's cost basis (never loosened)
    "max_candles": 252,      # held daily bars per holding before a forced exit at the next open
}

SPACE = {
    "k": {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11},
    "n": {"min": 21, "max": 252, "step": 21, "hard_min": 5, "hard_max": 380},
    "stop_loss_pct": {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0},
    "max_candles": {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260},
}


def valid(p: dict) -> bool:
    return (p["k"] >= 1 and p["n"] >= 2) and p["stop_loss_pct"] > 0 and p["max_candles"] >= 1


def target_weights(P: dict, i: int, p: dict) -> np.ndarray:
    """Top k sectors by ROC(n), only while SPY > SMA(200) (SPY is a reference, not traded); equal weight."""
    K = P["close"].shape[1]
    spy = ref_close(P, "SPY")
    if not spy[i] > sma(P, 200, spy)[i]:
        return np.zeros(K)
    r = roc(P, int(p["n"]))[i]
    cands = [((-r[j], j), j) for j in range(K) if np.isfinite(r[j])]
    return equal(K, top_k(cands, int(p["k"])))


# --------------------------------------------------------------------------
# Portfolio machinery (shared by the library's month-end allocation specs).
# Built from scripts/portfolio_lib/core.py; generalizes breadth_scaled_sector_allocation's
# _simulate_portfolio: target_weights() above decides, everything below executes.
# --------------------------------------------------------------------------
_PANEL: dict = {}


def _panel(symbols: tuple) -> dict:
    """Aligned OHLC arrays on the union of trading days (NaN before listing / on missing bars, no ffill).
    Reference series (CONFIG["reference"], e.g. SPY as a market filter) are loaded alongside but never traded."""
    refs = tuple(r for r in CONFIG.get("reference", []) if r not in symbols)
    key = symbols + refs
    if key in _PANEL:
        return _PANEL[key]
    dfs = {s: load_bars(CONFIG["asset_class"], s, CONFIG["timeframe"]) for s in key}
    idx = dfs[key[0]].index
    for d in dfs.values():
        idx = idx.union(d.index)
    al = {s: d.reindex(idx) for s, d in dfs.items()}
    per = idx.tz_localize(None).to_period("M")
    nxt = pd.Series(per, index=idx).shift(-1)
    month_end = (pd.Series(per, index=idx).ne(nxt) & nxt.notna()).to_numpy(bool)   # last bar of a complete month
    out = {"idx": idx, "month_end": month_end, "cache": {}, "syms": list(symbols),
           "ref": {r: al[r]["close"].to_numpy(float) for r in key}}
    for k in ("open", "high", "low", "close"):
        out[k] = np.column_stack([al[s][k].to_numpy(float) for s in symbols])
    first = []
    for j in range(len(symbols)):
        v = np.flatnonzero(~np.isnan(out["close"][:, j]))
        first.append(int(v[0]) if v.size else len(idx))
    out["first"] = np.array(first)
    _PANEL[key] = out
    return out


def _own(P: dict, name: str, fn, series: np.ndarray | None = None) -> np.ndarray:
    """fn applied to each symbol's own valid closes (no window spans pre-listing NaNs), cached by name.
    series=None -> all traded symbols as columns; otherwise one 1-D series (a reference)."""
    ck = (name, None if series is None else id(series))
    if ck not in P["cache"]:
        def one(col: np.ndarray) -> np.ndarray:
            c = pd.Series(col)
            v = c.dropna()
            return fn(v).reindex(c.index).to_numpy(float)
        if series is None:
            P["cache"][ck] = np.column_stack([one(P["close"][:, j]) for j in range(P["close"].shape[1])])
        else:
            P["cache"][ck] = one(series)
    return P["cache"][ck]


def sma(P, n, series=None):
    """SMA(n) of close."""
    return _own(P, f"sma{n}", lambda v: v.rolling(n, min_periods=n).mean(), series)


def roc(P, n, series=None):
    """ROC(n) as a DECIMAL (C/C[n]-1); INDICATORS.md: portfolio scores use decimal units."""
    return _own(P, f"roc{n}", lambda v: v / v.shift(n) - 1, series)


def vol(P, n):
    """Population std (ddof=0) of decimal simple daily returns over n returns."""
    return _own(P, f"vol{n}", lambda v: (v / v.shift(1) - 1).rolling(n, min_periods=n).std(ddof=0))


def downside_dev(P, n):
    """sqrt(mean(min(r,0)^2)) over n decimal daily returns, measured around zero."""
    return _own(P, f"ddev{n}", lambda v: np.sqrt((np.minimum(v / v.shift(1) - 1, 0) ** 2).rolling(n, min_periods=n).mean()))


def hh(P, n, series=None):
    """HH(C, n): rolling max of close."""
    return _own(P, f"hh{n}", lambda v: v.rolling(n, min_periods=n).max(), series)


def rets(P):
    """Decimal simple daily returns per symbol on its own bars (NaN where no bar)."""
    return _own(P, "ret", lambda v: v / v.shift(1) - 1)


def ref_close(P, sym):
    return P["ref"][sym]


def month_closes(P, j: int, i: int, n: int) -> np.ndarray | None:
    """Closes at the last n+1 month-end bars up to and including bar i (None if any is missing)."""
    me = np.flatnonzero(P["month_end"][: i + 1])
    if me.size < n + 1:
        return None
    c = P["close"][me[-(n + 1):], j]
    return None if np.isnan(c).any() else c


def top_k(cands: list, k: int) -> list:
    """cands = [(sort_key_tuple, j)], ascending sort; ties fall back to ticker order because j is
    the alphabetical column index. Returns the first k column indices."""
    return [j for _, j in sorted(cands)[:k]]


def equal(k_total: int, sel: list) -> np.ndarray:
    w = np.zeros(k_total)
    if sel:
        w[sel] = 1.0 / len(sel)
    return w


def cov_window(P, i: int, cols: list, n: int) -> np.ndarray | None:
    """Sample covariance (ddof=1) of the last n aligned daily returns of cols, regularized as in
    INDICATORS.md. Rows where any of cols has no return are dropped (common complete intersection)."""
    R = rets(P)[max(0, i - n + 1): i + 1][:, cols]
    R = R[~np.isnan(R).any(axis=1)]
    if R.shape[0] < max(3, int(0.9 * n)):
        return None
    C = np.cov(R, rowvar=False, ddof=1).reshape(len(cols), len(cols))
    N = len(cols)
    C = C + 1e-6 * max(np.trace(C) / N, 1e-12) * np.eye(N)
    return C if np.isfinite(C).all() else None


def min_variance(C: np.ndarray) -> np.ndarray | None:
    """Exact long-only minimum variance (0<=w<=1, sum w=1) by enumerating active sets: for every
    support S the equality-constrained optimum is C_S^-1 1 / (1' C_S^-1 1); the best feasible one is
    the global optimum of this convex QP. Same target as INDICATORS.md's SLSQP, solved exactly
    (scipy isn't in the backtest image). N<=11 here, so at most 2047 small solves."""
    N = C.shape[0]
    if N == 1:
        return np.ones(1)
    best, best_v = None, np.inf
    for mask in range(1, 1 << N):
        S = [j for j in range(N) if mask >> j & 1]
        try:
            x = np.linalg.solve(C[np.ix_(S, S)], np.ones(len(S)))
        except np.linalg.LinAlgError:
            continue
        s = x.sum()
        if not np.isfinite(s) or s <= 0:
            continue
        x = x / s
        if (x < -1e-12).any():
            continue
        w = np.zeros(N)
        w[S] = np.clip(x, 0, None)
        v = float(w @ C @ w)
        if v < best_v - 1e-18:
            best, best_v = w / w.sum(), v
    return best


def erc(C: np.ndarray) -> np.ndarray | None:
    """Long-only equal-risk-contribution weights. For a positive-definite C the ERC point is unique
    and is where INDICATORS.md's objective sum((w_i(Cw)_i - w'Cw/N)^2)/(w'Cw)^2 equals 0. Solved by
    cyclical coordinate descent on 0.5x'Cx - (1/N)sum(log x), w = x/sum(x) (Griveau-Billion et al.);
    validated like the spec: finite, sum 1 within 1e-6, contributions equal within 1e-6 (else None -> cash)."""
    N = C.shape[0]
    if N == 1:
        return np.ones(1)
    d = np.diag(C)
    if (d <= 0).any():
        return None
    x = 1.0 / np.sqrt(d)
    for _ in range(2000):
        x_old = x.copy()
        for i in range(N):
            a = C[i] @ x - d[i] * x[i]
            x[i] = (-a + np.sqrt(a * a + 4 * d[i] / N)) / (2 * d[i])
        if np.max(np.abs(x - x_old) / x_old) < 1e-12:
            break
    w = x / x.sum()
    rc = w * (C @ w)
    tot = float(w @ C @ w)
    if not np.isfinite(w).all() or abs(w.sum() - 1) > 1e-6 or tot <= 0 or np.max(np.abs(rc / tot - 1 / N)) > 1e-6:
        return None
    return w


def _simulate_portfolio(P: dict, syms: list, p: dict, lo: int, hi: int, capital: float):
    """Month-end allocation with per-holding hard stop and time cap (EXECUTION.md "Sizing and portfolio sleeves").

    Decision at the close of the last bar of each complete month t: target_weights(P, t, p) gives the
    weights (sum <= 1, rest cash at 0% yield: the conservative, labelled cash scenario).
    If a listed member has no bar at t, the rebalance is skipped (weights unchanged). A symbol is
    listed from its first bar on; before that it isn't part of the universe (point-in-time).
    Execution at the open of bar t+1, in this order on every bar:
      1. time exit: holding has completed max_candles held bars -> sell at the open
      2. gap stop: open <= stop -> sell at the open
      3. rebalance (only on execution bars): sell removed, trim overweight (keep cost E and age),
         then buy underweight / new; buys scaled down if cash is short. Symbols exited on this
         bar are not re-bought on it. Additions: E = weighted-average cost,
         stop = max(old stop, E_new * (1 - sl)).
      4. intrabar stop: low <= stop -> sell at the stop.
    A stopped holding stays out until the next month-end decision (buys only happen there).
    """
    o, h, l, c = P["open"], P["high"], P["low"], P["close"]
    idx, me, first = P["idx"], P["month_end"], P["first"]
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    sl = p["stop_loss_pct"] / 100
    max_c = int(p["max_candles"])
    k = len(syms)
    qty = np.zeros(k)
    cost = np.zeros(k)          # fill value of the open position (for weighted-average E)
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
                if qty[j] > 0 and not np.isnan(o[i, j]) and val[j] > target[j] + 1e-9:
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
            listed = (first <= i) | (qty > 0)
            if np.any(np.isnan(c[i]) & listed):
                continue                                 # missing bar for a member: skip, keep weights
            w = np.asarray(target_weights(P, i, p), float)
            w = np.where(np.isfinite(w) & (w > 1e-12) & listed, w, 0.0)
            if w.sum() > 1 + 1e-9:
                w = w / w.sum()                          # never more than 100 % of the sleeve
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
    The symbol list is one portfolio (see _simulate_portfolio). Returns {"metrics", "trades", "equity"}."""
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
