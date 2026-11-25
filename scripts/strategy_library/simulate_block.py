def _simulate(df: pd.DataFrame, buy: np.ndarray, sell: np.ndarray, p: dict, lo: int, hi: int, capital: float, symbol: str):
    """Library execution contract (EXECUTION.md), replacing the template's _simulate:
    - entry at the open after a signal close; entry veto when the strategy's close-based exit is
      already true on the signal bar
    - stop = E - stop_atr * A and target = E + take_profit_atr * A, with E = entry fill and
      A = ATR(14) of the signal bar, both frozen; skipped if A <= 0/NaN or stop <= 0
    - stop before target in the same bar; gaps fill at the open (stop: worse, target: better)
    - max_candles: held bars counted from the entry bar as 1; exit at the open after bar N
    - optional entry_level(df, p): a level frozen at the signal bar; close < level is a signal exit
    - after an intrabar stop/target exit, one fully flat bar must complete before a new signal
    Sizing stays the template's position_pct of equity (user's choice, not the spec's risk_fraction)."""
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    fee, slip = CONFIG["fee_pct"] / 100, CONFIG["slippage_pct"] / 100
    k_sl, k_tp = float(p.get("stop_atr", 0) or 0), float(p.get("take_profit_atr", 0) or 0)
    max_c = int(p.get("max_candles", 0) or 0)
    a14 = atr(df, 14).to_numpy(float)
    lvl = entry_level(df, p).to_numpy(float) if "entry_level" in globals() else None
    idx = df.index
    cash, trades = capital, []
    equity = np.full(hi - lo, np.nan)
    i = lo
    while True:
        s = _first(buy, i)
        if s < 0 or s + 1 >= hi:
            equity[i - lo:] = cash
            break
        if sell[s]:                                 # entry veto: exit condition already true
            i = s + 1
            continue
        A = a14[s]
        e = s + 1
        entry = o[e] * (1 + slip)
        sl_lvl = entry - k_sl * A if k_sl else -np.inf
        tp_lvl = entry + k_tp * A if k_tp else np.inf
        if (k_sl or k_tp) and (not np.isfinite(A) or A <= 0 or (k_sl and sl_lvl <= 0)):
            i = s + 1                               # invalid ATR or non-positive stop: skip
            continue
        L = lvl[s] if lvl is not None else np.nan
        equity[i - lo:e - lo] = cash
        stake = cash * CONFIG["position_pct"]
        qty = stake / (entry * (1 + fee))
        cash_after = cash - qty * entry * (1 + fee)
        x, price, reason = None, None, None
        j = e
        while j < hi:
            if max_c and j - e >= max_c:
                x, price, reason = j, o[j], "max_bars"
                break
            if l[j] <= sl_lvl:
                x, price, reason = j, min(o[j], sl_lvl), "stop"
                break
            if h[j] >= tp_lvl:
                x, price, reason = j, max(o[j], tp_lvl), "target"
                break
            if (sell[j] or c[j] < L) and j + 1 < hi:
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
        # open exits leave bar x flat; intrabar exits need bar x+1 as the first flat bar
        i = x + 1 if (reason in ("stop", "target") and price != o[x]) else x
    eq = pd.Series(equity, index=idx[lo:hi]).ffill().fillna(capital)
    return trades, eq
