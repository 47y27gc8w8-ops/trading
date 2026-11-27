
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

