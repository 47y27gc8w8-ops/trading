"""OLS residual pairs: long-A / short-B pair backtest adapted from the generic template.

Built by scripts/portfolio_lib/build_pairs.py (strategy block below + shared panel/indicators from
core.py + pair simulator pair_core.py + the template's generic machinery). CONFIG["symbols"] is ONE
pair strategy (A first), not independent per-symbol trades.

    docker compose run --rm -T backtest python strategies/ols_residual_pairs/backtest.py --period is [--trades]

BORROW COST IS ASSUMED, NOT HISTORICAL: CONFIG["borrow_fee_pct_yr"] (see strategy.md). The spec says
to disable pairs without historical borrow/carry data; the user chose to run them with this labelled
assumption instead (2026-11-27).
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
    "name": "ols_residual_pairs",
    "asset_class": "etf",
    "symbols": ["XLE", "VDE"],   # A first, then B
    "timeframe": "1d",
    "start": "2006-01-01",
    "oos_start": "2016-01-01",
    "end": "2026-11-23",             # frozen at setup (last complete daily bar)
    "capital": 10_000.0,
    "position_pct": 1.0,             # gross pair notional = 100 % of sleeve equity
    "fee_pct": 0.05,                # library convention for US ETFs (spec: 1 bp commission; more conservative)
    "slippage_pct": 0.03,           # spec: half-spread 2 bp + slippage 2 bp per fill
    "borrow_fee_pct_yr": 0.25,       # ASSUMED (user decision 2026-11-27): easy-to-borrow large caps/ETFs; stress runs 1 % and 3 %
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 0,
}

PARAMS = {
    "n": 120,    # prior OLS window (daily bars, excludes t)
    "z": 2.0,    # entry deviation (residual std units)
    "pair_stop_pct": 5.0,   # close-based pair loss, % of entry gross notional
    "leg_stop_pct": 8.0,    # per-leg hard stop, % adverse from that leg's entry fill
    "max_candles": 40,      # held daily bars (entry bar = 1), exit at the next open
}

SPACE = {
    "n": {"min": 60, "max": 250, "step": 10, "hard_min": 20, "hard_max": 504},
    "z": {"min": 1.0, "max": 3.0, "step": 0.25, "hard_min": 0.25, "hard_max": 3.75},
    "pair_stop_pct": {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.5, "hard_max": 30.0},
    "leg_stop_pct": {"min": 4.0, "max": 15.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0},
    "max_candles": {"min": 10, "max": 80, "step": 5, "hard_min": 2, "hard_max": 252},
}


def valid(p: dict) -> bool:
    return (p["n"] >= 20 and 0 < p["z"] < 4) and p["pair_stop_pct"] > 0 and p["leg_stop_pct"] > 0 and p["max_candles"] >= 1


def signals(P: dict, p: dict) -> dict:
    """Daily refit of log(A) = alpha + beta log(B) on t-n..t-1; residual z = (log A - alpha - beta log B)
    / formation residual std. Entry beta > 0 and z < -z (dollar ratio 1:beta, frozen at entry);
    exit refitted z >= 0 or z <= -4."""
    C = P["close"]
    la, lb = np.log(C[:, 0]), np.log(C[:, 1])
    a, b, s = rolling_ols_prior(la, lb, int(p["n"]))
    with np.errstate(invalid="ignore", divide="ignore"):
        Z = np.where(s > 0, (la - a - b * lb) / s, np.nan)
    return {"entry": (b > 0) & (Z < -p["z"]), "exit": (Z >= 0) | (Z <= -4), "ratio": np.where(b > 0, b, np.nan)}


# --------------------------------------------------------------------------
# Panel and indicators (shared with the library's portfolio specs).
# Built from the first half of scripts/portfolio_lib/core.py.
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


# --------------------------------------------------------------------------
# Pair machinery (shared by the library's long-A / short-B specs). Built from
# scripts/portfolio_lib/pair_core.py; signals() above decides, everything below executes.
# --------------------------------------------------------------------------
def corr_ab(P: dict, a: int, b: int, n: int) -> np.ndarray:
    """Rolling n-bar Pearson correlation of the two legs' decimal daily returns (includes t)."""
    R = rets(P)
    return pd.Series(R[:, a]).rolling(n, min_periods=n).corr(pd.Series(R[:, b])).to_numpy(float)


def wilder_rsi(x: np.ndarray, n: int) -> np.ndarray:
    """RSI(n) with Wilder RMA (alpha 1/n, SMA seed) on the valid part of x; first 5n values NaN (warm-up)."""
    out = np.full(len(x), np.nan)
    v = np.flatnonzero(~np.isnan(x))
    if v.size < 5 * n + 1:
        return out
    s = x[v]
    d = np.diff(s)
    g, l = np.maximum(d, 0), np.maximum(-d, 0)
    ag, al = g[:n].mean(), l[:n].mean()
    rsi = np.full(len(s), np.nan)
    for t in range(n, len(d) + 1):
        if t > n:
            ag = ag + (g[t - 1] - ag) / n
            al = al + (l[t - 1] - al) / n
        rsi[t] = 100.0 if al == 0 and ag > 0 else (50.0 if al == 0 else 100 - 100 / (1 + ag / al))
    rsi[: 5 * n] = np.nan
    out[v] = rsi
    return out


def prior_stats(x: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Mean and population std of x over t-n..t-1 (prior window, excludes t)."""
    s = pd.Series(x)
    return (s.rolling(n, min_periods=n).mean().shift(1).to_numpy(float),
            s.rolling(n, min_periods=n).std(ddof=0).shift(1).to_numpy(float))


def rolling_ols_prior(y: np.ndarray, x: np.ndarray, n: int):
    """OLS y = alpha + beta x on t-n..t-1 for every t: (alpha, beta, residual population std)."""
    Y, X = pd.Series(y), pd.Series(x)
    mx, my = X.rolling(n, min_periods=n).mean(), Y.rolling(n, min_periods=n).mean()
    vx = X.rolling(n, min_periods=n).var(ddof=0)
    vy = Y.rolling(n, min_periods=n).var(ddof=0)
    cxy = X.rolling(n, min_periods=n).cov(Y, ddof=0)
    beta = cxy / vx
    alpha = my - beta * mx
    rstd = np.sqrt((vy - beta * cxy).clip(lower=0))
    sh = lambda z: z.shift(1).to_numpy(float)  # noqa: E731
    return sh(alpha), sh(beta), sh(rstd)


def _norm_cdf(z: float) -> float:
    from math import erf, sqrt
    return 0.5 * (1 + erf(z / sqrt(2)))


def coint_pvalue(y: np.ndarray, x: np.ndarray) -> tuple[float, float, float]:
    """Engle-Granger test as statsmodels coint(y, x, trend="c", maxlag=1, autolag=None):
    OLS y = a + b x; ADF on the residuals with no constant and 1 lagged difference; MacKinnon (1994)
    asymptotic p-value for N=2, regression "c" (constants copied from statsmodels.tsa.adfvalues).
    Returns (p_value, alpha, beta). Near-perfect collinearity -> statistic -inf -> p 0, as statsmodels."""
    X = np.column_stack([np.ones(len(x)), x])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ coef
    r2 = 1 - (e @ e) / (((y - y.mean()) ** 2).sum())
    if r2 >= 1 - 100 * np.sqrt(np.finfo(float).eps):
        return 0.0, float(coef[0]), float(coef[1])
    de = np.diff(e)
    Z = np.column_stack([e[1:-1], de[:-1]])           # x_{t-1}, dx_{t-1}
    yy = de[1:]
    g, *_ = np.linalg.lstsq(Z, yy, rcond=None)
    res = yy - Z @ g
    s2 = (res @ res) / (len(yy) - Z.shape[1])
    se = np.sqrt(s2 * np.linalg.inv(Z.T @ Z)[0, 0])
    t = g[0] / se
    if t > 0.92:
        return 1.0, float(coef[0]), float(coef[1])
    if t < -18.86:
        return 0.0, float(coef[0]), float(coef[1])
    c = [2.92, 1.5012, 3.9796e-2] if t <= -2.62 else [2.1945, 0.64695, -0.29198, -0.042377]
    return _norm_cdf(sum(ci * t ** k for k, ci in enumerate(c))), float(coef[0]), float(coef[1])


def _simulate_pair(P: dict, syms: list, p: dict, lo: int, hi: int, capital: float):
    """Long A / short B (EXECUTION.md "Pair execution"). signals(P, p) returns arrays over the panel:
    entry, exit (bool), ratio (beta: long A = G/(1+beta), short B = beta*G/(1+beta); NaN = no entry),
    optional force (bool: exit at next open, e.g. end of a trading window) and a/b (leg columns per bar).
    Evaluated at bar t's close, filled at the next synchronized open (both legs need a bar):
      - open: pending exit (signal / pair stop / time / force) -> both legs at the open;
              else a leg gapping through its stop -> both legs at the open.
      - intrabar: long leg low <= its stop or short leg high >= its stop -> the stopped leg at its stop,
              the other leg at its worst bar extreme (conservative; A is assumed first if both touch).
      - close: held bars (entry bar = 1) >= max_candles, or net pair P&L incl. fees and borrow
              <= -pair_stop_pct % of entry gross -> exit at the next open.
    Entry veto: no entry if the exit condition is true on the signal bar. No signal on a bar
    where a position was closed. Gross G = 100 % of sleeve equity. Short leg pays a borrow fee
    CONFIG["borrow_fee_pct_yr"] %/yr on its market value (calendar days); short proceeds earn 0 %.
    Total-return (adjusted) prices on both legs: the short leg pays the distributions it is short."""
    sig = signals(P, p)
    o, h, l, c = P["open"], P["high"], P["low"], P["close"]
    idx = P["idx"]
    n = len(idx)
    A_col = sig.get("a", np.zeros(n, int))
    B_col = sig.get("b", np.ones(n, int))
    entry, exit_, ratio = sig["entry"], sig["exit"], sig["ratio"]
    force = sig.get("force", np.zeros(n, bool))
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    borrow = CONFIG["borrow_fee_pct_yr"] / 100
    leg, pstop, max_c = p["leg_stop_pct"] / 100, p["pair_stop_pct"] / 100, int(p["max_candles"])
    days = np.r_[0.0, np.diff(idx.asi8) / 86_400e9]
    cash = capital
    pos = None                 # dict while a pair is open
    pend_in = None             # (a, b, beta) to enter at the next open
    pend_out = None            # reason to exit at the next open
    trades: list = []
    equity = np.full(hi - lo, np.nan)
    last_eq = capital

    def close(i: int, pa: float, pb: float, reason: str):
        nonlocal cash, pos
        fa, fb = pa * (1 - slip), pb * (1 + slip)
        got = pos["qa"] * fa * (1 - fee)
        pay = pos["qb"] * fb * (1 + fee)
        cash += got - pay
        pos["flow"] += got - pay
        a, b = pos["a"], pos["b"]
        trades.append({
            "symbol": f"{syms[a]}/{syms[b]}", "entry_time": str(idx[pos["i"]]), "exit_time": str(idx[i]),
            "entry_price": pos["ea"], "exit_price": fa, "qty": pos["qa"], "pnl": pos["flow"],
            "pnl_pct_of_equity": pos["flow"] / pos["eq"] * 100, "bars": i - pos["i"], "exit_reason": reason,
        })
        pos = None

    for i in range(lo, hi):
        closed_now = False
        if pos is not None:
            a, b = pos["a"], pos["b"]
            if not (np.isnan(o[i, a]) or np.isnan(o[i, b])):
                cost = pos["qb"] * c[i - 1, b] * borrow * days[i] / 365 if not np.isnan(c[i - 1, b]) else 0.0
                cash -= cost
                pos["flow"] -= cost
                if pend_out is not None:
                    close(i, o[i, a], o[i, b], pend_out)
                    closed_now = True
                elif o[i, a] <= pos["sa"] or o[i, b] >= pos["sb"]:
                    close(i, o[i, a], o[i, b], "leg_stop")
                    closed_now = True
                pend_out = None
        elif pend_in is not None:
            a, b, beta = pend_in
            if not (np.isnan(o[i, a]) or np.isnan(o[i, b])):
                G = cash
                fa, fb = o[i, a] * (1 + slip), o[i, b] * (1 - slip)
                qa = G / (1 + beta) / (fa * (1 + fee))
                qb = beta * G / (1 + beta) / fb
                flow = -qa * fa * (1 + fee) + qb * fb * (1 - fee)
                cash += flow
                pos = {"a": a, "b": b, "qa": qa, "qb": qb, "ea": fa, "eb": fb, "i": i, "eq": G, "G": G,
                       "sa": fa * (1 - leg), "sb": fb * (1 + leg), "flow": flow}
            pend_in = None
        if pos is not None and not closed_now:
            a, b = pos["a"], pos["b"]
            if not (np.isnan(l[i, a]) or np.isnan(h[i, b])):
                if l[i, a] <= pos["sa"]:
                    close(i, pos["sa"], h[i, b], "leg_stop")
                    closed_now = True
                elif h[i, b] >= pos["sb"]:
                    close(i, l[i, a], pos["sb"], "leg_stop")
                    closed_now = True
        if pos is not None:
            a, b = pos["a"], pos["b"]
            if not (np.isnan(c[i, a]) or np.isnan(c[i, b])):
                last_eq = cash + pos["qa"] * c[i, a] - pos["qb"] * c[i, b]
                pnl = pos["flow"] + pos["qa"] * c[i, a] * (1 - slip) * (1 - fee) - pos["qb"] * c[i, b] * (1 + slip) * (1 + fee)
                if i - pos["i"] + 1 >= max_c:
                    pend_out = "max_bars"
                elif pnl <= -pstop * pos["G"]:
                    pend_out = "pair_stop"
                elif exit_[i] or force[i]:
                    pend_out = "signal" if exit_[i] else "window_end"
        else:
            last_eq = cash
            if not closed_now and i + 1 < hi and entry[i] and not exit_[i] and not force[i]:
                a, b, beta = int(A_col[i]), int(B_col[i]), float(ratio[i])
                if a >= 0 and b >= 0 and np.isfinite(beta) and beta > 0:
                    pend_in = (a, b, beta)
        equity[i - lo] = last_eq
    if pos is not None:                                   # still open at the last close
        a, b = pos["a"], pos["b"]
        last = hi - 1
        pa = c[last, a] if not np.isnan(c[last, a]) else pd.Series(c[:last + 1, a]).dropna().iloc[-1]
        pb = c[last, b] if not np.isnan(c[last, b]) else pd.Series(c[:last + 1, b]).dropna().iloc[-1]
        close(last, pa, pb, "end")
    eq = pd.Series(equity, index=idx[lo:hi]).ffill().fillna(capital)
    return trades, eq


def run(params: dict | None = None, period: str = "is", symbols: list[str] | None = None) -> dict:
    """Backtest one parameter set on one period ("is", "oos", "all", "live").
    CONFIG["symbols"] is ONE pair strategy (order matters: A first). Returns {"metrics", "trades", "equity"}."""
    p = {**PARAMS, **(params or {})}
    syms = list(symbols or CONFIG["symbols"])
    P = _panel(tuple(syms))
    lo, hi = _bounds(P["idx"], period)
    if hi - lo < 2:
        raise ValueError(f"no bars for period {period}")
    all_trades, equity = _simulate_pair(P, syms, p, lo, hi, CONFIG["capital"])
    all_trades.sort(key=lambda t: t["exit_time"])
    m = metrics(all_trades, equity, 1)
    m["open_positions"] = [{"symbol": t["symbol"], "since": t["entry_time"], "entry_price": round(t["entry_price"], 6)}
                           for t in all_trades if t["exit_reason"] == "end"]
    m["buy_hold_return_pct"] = 0.0                        # a market-neutral spread has no buy & hold benchmark
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
