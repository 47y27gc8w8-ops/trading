
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

