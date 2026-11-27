
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

