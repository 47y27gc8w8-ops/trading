"""Generate strategies/<name>/backtest.py + strategy.md for library specs (SHARD1).

Takes the user's template strategies/backtest.py (main checkout, untouched), replaces the
"Strategy definition" block per strategy, and applies one shared machinery patch:
  - frozen ATR(14) stop/target from the signal bar (EXECUTION.md "Protective stops")
  - entry veto: no entry when the strategy's own close-based exit is true on the signal bar
  - after an intrabar stop/target exit, the next signal may come from the next bar on
  - a resting target fills at the target (never better on a favorable gap)
Run on the host: python3 scripts/library_gen.py <worktree root> [names...]
"""
from __future__ import annotations

import sys
from pathlib import Path

TEMPLATE = Path("/home/luca/trading/strategies/backtest.py")
BEGIN = "# --------------------------------------------------------------------------\n# Strategy definition"
END = "# --------------------------------------------------------------------------\n# Generic machinery below"

# ---------------------------------------------------------------- shared indicator code
INDICATORS = r'''
# Indicators per ../../INDICATORS.md (EMA/RMA seeded with the SMA of the first n values,
# population std, Wilder ATR). Memoized per data frame and arguments: the optimizer
# calls the signal functions thousands of times on the same bars.
from numpy.lib.stride_tricks import sliding_window_view as _swv

_MEMO: dict = {}


def _memo(key, fn):
    if key not in _MEMO:
        if len(_MEMO) > 4000:
            _MEMO.clear()
        _MEMO[key] = fn()
    return _MEMO[key]


def _seeded(x: pd.Series, n: int, alpha: float) -> pd.Series:
    a = x.to_numpy(float)
    out = np.full(len(a), np.nan)
    ok = np.flatnonzero(~np.isnan(a))
    if len(ok) < n:
        return pd.Series(out, index=x.index)
    s = ok[0]
    seed_end = s + n - 1
    if np.isnan(a[s:seed_end + 1]).any():          # require n consecutive valid values
        return pd.Series(out, index=x.index)
    prev = a[s:seed_end + 1].mean()
    out[seed_end] = prev
    for i in range(seed_end + 1, len(a)):
        v = a[i]
        if not np.isnan(v):
            prev = prev + alpha * (v - prev)
        out[i] = prev
    return pd.Series(out, index=x.index)


def sma(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(int(n)).mean()


def ema(x: pd.Series, n: int) -> pd.Series:
    return _seeded(x, int(n), 2.0 / (int(n) + 1))


def rma(x: pd.Series, n: int) -> pd.Series:
    return _seeded(x, int(n), 1.0 / int(n))


def true_range(df: pd.DataFrame) -> pd.Series:
    pc = df["close"].shift(1)
    return pd.concat([df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()], axis=1).max(axis=1)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return _memo(("atr", id(df), n), lambda: rma(true_range(df), n))


def rsi_ind(x: pd.Series, n: int, key=None) -> pd.Series:
    def f():
        d = x.diff()
        up, dn = rma(d.clip(lower=0), n), rma((-d).clip(lower=0), n)
        r = 100 - 100 / (1 + up / dn)
        r = r.where(dn != 0, 100.0).where(~((up == 0) & (dn == 0)), 50.0)
        return r.where(up.notna() & dn.notna())
    return _memo(("rsi", key, n), f) if key is not None else f()


def cross_above(x: pd.Series, y) -> pd.Series:
    y = y if isinstance(y, pd.Series) else pd.Series(float(y), index=x.index)
    return (x > y) & (x.shift(1) <= y.shift(1))


def bbands(close: pd.Series, n: int, k: float):
    mid = sma(close, n)
    sd = close.rolling(int(n)).std(ddof=0)
    return mid - k * sd, mid, mid + k * sd


def adx(df: pd.DataFrame, n: int = 14) -> pd.Series:
    def f():
        h, l = df["high"], df["low"]
        up, down = h - h.shift(1), l.shift(1) - l
        pdm = up.where((up > down) & (up > 0), 0.0).where(up.notna())
        mdm = down.where((down > up) & (down > 0), 0.0).where(down.notna())
        a = atr(df, n)
        dip = (100 * rma(pdm, n) / a).where(a != 0, 0.0)
        dim = (100 * rma(mdm, n) / a).where(a != 0, 0.0)
        s = dip + dim
        dx = (100 * (dip - dim).abs() / s).where(s != 0, 0.0)
        return rma(dx, n)
    return _memo(("adx", id(df), n), f)


def aroon(df: pd.DataFrame, n: int):
    def f():
        out = []
        for col, pick in (("high", np.argmax), ("low", np.argmin)):
            a = df[col].to_numpy(float)
            res = np.full(len(a), np.nan)
            if len(a) > n:
                w = _swv(a, n + 1)[:, ::-1]           # newest first: ties pick the most recent extreme
                since = pick(w, axis=1)
                res[n:] = 100.0 * (n - since) / n
            out.append(pd.Series(res, index=df.index))
        return tuple(out)
    return _memo(("aroon", id(df), n), f)


def cci(df: pd.DataFrame, n: int) -> pd.Series:
    tp = ((df["high"] + df["low"] + df["close"]) / 3).to_numpy(float)
    res = np.full(len(tp), np.nan)
    if len(tp) >= n:
        w = _swv(tp, n)
        m = w.mean(axis=1)
        md = np.abs(w - m[:, None]).mean(axis=1)
        with np.errstate(divide="ignore", invalid="ignore"):
            v = np.where(md > 0, (tp[n - 1:] - m) / (0.015 * md), 0.0)
        res[n - 1:] = v
    return pd.Series(res, index=df.index)


def adl(df: pd.DataFrame) -> pd.Series:
    def f():
        h, l, c, v = df["high"], df["low"], df["close"], df["volume"]
        rng = h - l
        inc = (((2 * c - h - l) / rng) * v).where(rng != 0, 0.0).fillna(0.0)
        return inc.cumsum()
    return _memo(("adl", id(df)), f)


def adl_increment(df: pd.DataFrame) -> pd.Series:
    h, l, c, v = df["high"], df["low"], df["close"], df["volume"]
    rng = h - l
    return (((2 * c - h - l) / rng) * v).where(rng != 0, 0.0).fillna(0.0)


def clv01(df: pd.DataFrame) -> pd.Series:
    rng = df["high"] - df["low"]
    return ((df["close"] - df["low"]) / rng).where(rng != 0, 0.5)


def roc(x: pd.Series, n: int) -> pd.Series:
    return 100 * (x / x.shift(int(n)) - 1)


def percent_rank_prior(x: pd.Series, n: int) -> pd.Series:
    """PR(X,n): share of the prior n values strictly below X[t] (+0.5 per tie); t excluded."""
    a = x.to_numpy(float)
    res = np.full(len(a), np.nan)
    if len(a) > n:
        w = _swv(a[:-1], n)                          # w[k] = a[k .. k+n-1], reference for t = k+n
        cur = a[n:]
        less = (w < cur[:, None]).sum(axis=1)
        eq = (w == cur[:, None]).sum(axis=1)
        v = 100.0 * (less + 0.5 * eq) / n
        bad = np.isnan(w).any(axis=1) | np.isnan(cur)
        res[n:] = np.where(bad, np.nan, v)
    return pd.Series(res, index=x.index)


def streak(close: pd.Series) -> pd.Series:
    c = close.to_numpy(float)
    out = np.zeros(len(c))
    for i in range(1, len(c)):
        if c[i] > c[i - 1]:
            out[i] = out[i - 1] + 1 if out[i - 1] > 0 else 1
        elif c[i] < c[i - 1]:
            out[i] = out[i - 1] - 1 if out[i - 1] < 0 else -1
    return pd.Series(out, index=close.index)


def connors_rsi(df: pd.DataFrame) -> pd.Series:
    def f():
        c = df["close"]
        return (rsi_ind(c, 3) + rsi_ind(streak(c), 2) + percent_rank_prior(roc(c, 1), 100)) / 3
    return _memo(("crsi", id(df)), f)


def weekly_ohlc(df: pd.DataFrame) -> pd.DataFrame:
    """Completed weeks ending Friday, labelled by the week's last trading day."""
    g = df.groupby(df.index.to_period("W-FRI"))
    w = pd.DataFrame({"open": g["open"].first(), "high": g["high"].max(), "low": g["low"].min(),
                      "close": g["close"].last(),
                      "last_day": pd.Series(df.index, index=df.index).groupby(df.index.to_period("W-FRI")).last()})
    return w.set_index("last_day")


def on_daily(weekly: pd.Series, daily_index: pd.DatetimeIndex) -> pd.Series:
    """Weekly values on daily bars: a week's value becomes visible at the close of its last
    trading day (the week is complete then); earlier days see the previous week."""
    return weekly.reindex(daily_index, method="ffill")


def reference_close(symbol: str, index: pd.DatetimeIndex) -> pd.Series:
    """A reference instrument's close aligned to the traded symbol's dates (no forward fill)."""
    ref = load_bars(CONFIG["asset_class"], symbol, CONFIG["timeframe"])["close"]
    return ref.reindex(index)
'''

ATR_PARAMS_DOC = """Exits shared by every library spec (EXECUTION.md):
#   stop_atr / take_profit_atr: stop = E - stop_atr*A, target = E + take_profit_atr*A, with
#   E = entry fill and A = ATR(14) of the signal bar, both frozen at entry.
#   max_bars = the spec's max_candles (entry bar counts as 1, exit at the next open)."""


def atr_space(mc_start, mc_min, mc_max):
    step = max(1, round((mc_max - mc_min) / 12))
    return {
        "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25},
        "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
        "max_bars": {"min": mc_min, "max": mc_max, "step": step, "hard_min": 1},
    }


# ---------------------------------------------------------------- the strategies
# Each: base symbols, screening universe, warmup, params(start) + space, valid, buy/sell code,
# and rule text for strategy.md. Fixed literals in the spec stay literal (spec: "Numeric
# literals not represented in this table are fixed constants").
S = {}

S["annual_high_breakout"] = dict(
    symbols=["MSFT"], universe="stock", warmup=320, mc=(48, 24, 96),
    params={"n": 252}, space={"n": {"min": 126, "max": 300, "step": 6, "hard_min": 20}},
    valid="True",
    buy='''c, v = df["close"], df["volume"]
    hh = df["high"].rolling(p["n"]).max().shift(1)
    return (c > hh) & (v > 1.5 * sma(v, 20).shift(1))''',
    sell='''return df["close"] < df["low"].rolling(20).min().shift(1)''',
    buy_txt="`C > HH(H, n)[1]` AND `V > 1.5 × SMA(V, 20)[1]`",
    sell_txt="`C < LL(L, 20)[1]`",
    ptab=[("n", "breakout lookback (bars)", "252", "126–300", "6")],
)

S["aroon_trend_onset"] = dict(
    symbols=["GLD"], universe="etf", warmup=260, mc=(96, 48, 192),
    params={"n": 25, "level": 70},
    space={"n": {"min": 14, "max": 50, "step": 2, "hard_min": 5},
           "level": {"min": 60, "max": 90, "step": 2.5, "hard_min": 50, "hard_max": 100}},
    valid="True",
    buy='''up, dn = aroon(df, p["n"])
    return cross_above(up, p["level"]) & (dn < 30)''',
    sell='''up, dn = aroon(df, p["n"])
    return up < dn''',
    buy_txt="`AroonUp(n)` crosses above `level` AND `AroonDown(n) < 30`",
    sell_txt="`AroonUp(n) < AroonDown(n)`",
    ptab=[("n", "Aroon length", "25", "14–50", "2"), ("level", "AroonUp cross level", "70", "60–90", "2.5")],
)

S["bollinger_band_walk"] = dict(
    symbols=["QQQ"], universe="etf", warmup=120, mc=(48, 24, 96),
    params={"n": 3}, space={"n": {"min": 2, "max": 5, "step": 1, "hard_min": 1, "hard_max": 10}},
    valid="True",
    buy='''c = df["close"]
    lo, mid, up = bbands(c, 20, 2.0)
    above = (c > up).astype(float).where(up.notna())
    walk = above.rolling(p["n"]).sum() == p["n"]
    return walk & (mid > mid.shift(5))''',
    sell='''return df["close"] < sma(df["close"], 10)''',
    buy_txt="each of the last `n` closes > its own `BB_upper(20, 2)` AND `SMA(20) > SMA(20)[5]`",
    sell_txt="`C < SMA(10)`",
    ptab=[("n", "closes above the upper band in a row", "3", "2–5", "1")],
)

S["bollinger_lower_band_reentry"] = dict(
    symbols=["SPY"], universe="etf", warmup=120, mc=(12, 6, 24),
    params={"k": 2.0}, space={"k": {"min": 1.5, "max": 3.0, "step": 0.1, "hard_min": 0.5}},
    valid="True",
    buy='''c = df["close"]
    lo, mid, up = bbands(c, 20, p["k"])
    return (c.shift(1) < lo.shift(1)) & (c > lo) & (adx(df, 14) < 25)''',
    sell='''return df["close"] >= sma(df["close"], 20)''',
    buy_txt="`C[1] < BB_lower(20, k)[1]` AND `C > BB_lower(20, k)` (cross back above) AND `ADX(14) < 25`",
    sell_txt="`C >= SMA(20)`",
    ptab=[("k", "band width in std", "2", "1.5–3", "0.1")],
)

S["bullish_engulfing_trend"] = dict(
    symbols=["AAPL"], universe="stock", warmup=320, mc=(48, 24, 96),
    params={"n": 200}, space={"n": {"min": 100, "max": 300, "step": 10, "hard_min": 20}},
    valid="True",
    buy='''o, c = df["open"], df["close"]
    eng = (c.shift(1) < o.shift(1)) & (c > o) & (o <= c.shift(1)) & (c >= o.shift(1))
    return eng & (c > sma(c, p["n"]))''',
    sell='''return df["close"] < _memo(("ema10", id(df)), lambda: ema(df["close"], 10))''',
    buy_txt="`C[1] < O[1]` AND `C > O` AND `O <= C[1]` AND `C >= O[1]` (bullish engulfing) AND `C > SMA(n)`",
    sell_txt="`C < EMA(10)`",
    ptab=[("n", "trend SMA length", "200", "100–300", "10")],
)

S["cci_correction_recovery"] = dict(
    symbols=["XLF"], universe="etf", warmup=200, mc=(12, 6, 24),
    params={"n": 20}, space={"n": {"min": 10, "max": 30, "step": 2, "hard_min": 5}},
    valid="True",
    buy='''wk = _memo(("wk", id(df)), lambda: weekly_ohlc(df))
    wcci = on_daily(cci(wk, p["n"]), df.index)
    d = _memo(("cci", id(df), p["n"]), lambda: cci(df, p["n"]))
    return (wcci > 0) & cross_above(d, -100)''',
    sell='''wk = _memo(("wk", id(df)), lambda: weekly_ohlc(df))
    wcci = on_daily(cci(wk, p["n"]), df.index)
    d = _memo(("cci", id(df), p["n"]), lambda: cci(df, p["n"]))
    return (d > 100) | (wcci < 0)''',
    buy_txt="last completed weekly `CCI(n) > 0` AND daily `CCI(n)` crosses above −100",
    sell_txt="daily `CCI(n) > 100` OR last completed weekly `CCI(n) < 0`",
    ptab=[("n", "CCI length (daily and weekly)", "20", "10–30", "2")],
)

S["chaikin_oscillator_cross"] = dict(
    symbols=["MSFT"], universe="stock", warmup=120, mc=(48, 24, 96),
    params={"n": 20}, space={"n": {"min": 10, "max": 50, "step": 2, "hard_min": 3}},
    valid="True",
    buy='''a = adl(df)
    osc = _memo(("chosc", id(df)), lambda: ema(a, 3) - ema(a, 10))
    return cross_above(osc, 0) & (a > sma(a, p["n"]))''',
    sell='''a = adl(df)
    osc = _memo(("chosc", id(df)), lambda: ema(a, 3) - ema(a, 10))
    return osc < 0''',
    buy_txt="`ChaikinOsc(3, 10)` crosses above 0 AND `ADL > SMA(ADL, n)`",
    sell_txt="`ChaikinOsc(3, 10) < 0`",
    ptab=[("n", "ADL trend SMA length", "20", "10–50", "2")],
)

S["close_location_washout"] = dict(
    symbols=["IWM"], universe="etf", warmup=260, mc=(12, 6, 24),
    params={"clv": 0.10}, space={"clv": {"min": 0.05, "max": 0.25, "step": 0.01, "hard_min": 0.0, "hard_max": 1.0}},
    valid="True",
    buy='''c = df["close"]
    return (clv01(df) < p["clv"]) & (roc(c, 1) < -1) & (c > sma(c, 200))''',
    sell='''c = df["close"]
    return (clv01(df) > 0.8) | (c > sma(c, 5))''',
    buy_txt="`CLV01 < clv` AND `ROC(1) < −1` (%) AND `C > SMA(200)`",
    sell_txt="`CLV01 > 0.8` OR `C > SMA(5)`",
    ptab=[("clv", "max close location (0–1)", "0.10", "0.05–0.25", "0.01")],
)

S["cmf_accumulation_cross"] = dict(
    symbols=["XLF"], universe="etf", warmup=160, mc=(48, 24, 96),
    params={"n": 20, "level": 0.10},
    space={"n": {"min": 10, "max": 40, "step": 2, "hard_min": 3},
           "level": {"min": 0.0, "max": 0.25, "step": 0.01, "hard_max": 1.0}},
    valid="True",
    buy='''c = df["close"]
    cmf = adl_increment(df).rolling(p["n"]).sum() / df["volume"].rolling(p["n"]).sum()
    return cross_above(cmf, p["level"]) & (c > sma(c, 100))''',
    sell='''cmf = adl_increment(df).rolling(p["n"]).sum() / df["volume"].rolling(p["n"]).sum()
    return cmf < 0''',
    buy_txt="`CMF(n)` crosses above `level` AND `C > SMA(100)`",
    sell_txt="`CMF(n) < 0`",
    ptab=[("n", "CMF length", "20", "10–40", "2"), ("level", "CMF cross level", "0.10", "0–0.25", "0.01")],
)

S["connors_composite_oversold"] = dict(
    symbols=["IWM"], universe="etf", warmup=260, mc=(12, 6, 24),
    params={"buy": 10, "exit": 70},
    space={"buy": {"min": 5, "max": 20, "step": 1, "hard_min": 1, "hard_max": 99},
           "exit": {"min": 55, "max": 90, "step": 2.5, "hard_min": 1, "hard_max": 99}},
    valid='p["exit"] > p["buy"]',
    buy='''c = df["close"]
    return (connors_rsi(df) < p["buy"]) & (c > sma(c, 200))''',
    sell='''return connors_rsi(df) > p["exit"]''',
    buy_txt="`ConnorsRSI(3, 2, 100) < buy` AND `C > SMA(200)`",
    sell_txt="`ConnorsRSI(3, 2, 100) > exit`",
    ptab=[("buy", "entry level", "10", "5–20", "1"), ("exit", "exit level", "70", "55–90", "2.5")],
    constraints="`exit > buy`",
)

S["connors_rsi2_pullback"] = dict(
    symbols=["SPY"], universe="etf", warmup=260, mc=(12, 6, 24),
    params={"n": 2, "buy": 5},
    space={"n": {"min": 2, "max": 4, "step": 1, "hard_min": 2, "hard_max": 14},
           "buy": {"min": 2, "max": 10, "step": 1, "hard_min": 0.5, "hard_max": 50}},
    valid="True",
    buy='''c = df["close"]
    return (rsi_ind(c, p["n"], key=id(df)) < p["buy"]) & (c > sma(c, 200))''',
    sell='''return df["close"] > sma(df["close"], 5)''',
    buy_txt="`RSI(n) < buy` AND `C > SMA(200)`",
    sell_txt="`C > SMA(5)`",
    ptab=[("n", "RSI length", "2", "2–4", "1"), ("buy", "oversold level", "5", "2–10", "1")],
)

S["consecutive_lower_lows_reversal"] = dict(
    symbols=["AAPL"], universe="stock", warmup=260, mc=(12, 6, 24),
    params={"n": 3}, space={"n": {"min": 2, "max": 5, "step": 1, "hard_min": 1, "hard_max": 10}},
    valid="True",
    buy='''c, l = df["close"], df["low"]
    ll = (l < l.shift(1)).astype(float).where(l.shift(1).notna())
    run = ll.shift(1).rolling(p["n"]).sum() == p["n"]
    return run & (c > df["high"].shift(1)) & (c > sma(c, 200))''',
    sell='''c = df["close"]
    return c > c.rolling(10).max().shift(1)''',
    buy_txt="each of the `n` bars ending t−1 has `L < L[1]` AND `C > H[1]` AND `C > SMA(200)`",
    sell_txt="`C > HH(C, 10)[1]`",
    ptab=[("n", "lower lows in a row", "3", "2–5", "1")],
)

S["cross_market_trend_confirmation"] = dict(
    symbols=["QQQ"], universe="etf", warmup=260, mc=(48, 24, 96),
    params={"n": 20}, space={"n": {"min": 10, "max": 50, "step": 2, "hard_min": 3}},
    valid="True",
    buy='''c = df["close"]
    ref = _memo(("ref", id(df)), lambda: reference_close("SOXX", df.index))
    e = _memo(("ema", id(df), p["n"]), lambda: ema(c, p["n"]))
    return cross_above(c, e) & (ref > sma(ref, 100)) & (roc(ref, 21) > roc(c, 21))''',
    sell='''c = df["close"]
    ref = _memo(("ref", id(df)), lambda: reference_close("SOXX", df.index))
    return (c < _memo(("ema", id(df), p["n"]), lambda: ema(c, p["n"]))) | (ref < sma(ref, 100))''',
    buy_txt="`C` crosses above `EMA(n)` AND `SOXX C > SMA(SOXX, 100)` AND `SOXX ROC(21) > ROC(21)` (traded symbol)",
    sell_txt="`C < EMA(n)` OR `SOXX C < SMA(SOXX, 100)`",
    ptab=[("n", "EMA length on the traded symbol", "20", "10–50", "2")],
    extra_assumptions=["SOXX is the fixed reference for every screened symbol: the spec names it; screening asks which other symbols the same semiconductor-confirmation rule suits.",
                       "SOXX closes are aligned to the traded symbol's dates without forward fill; a missing SOXX bar means no signal (EXECUTION.md). SOXX history starts 2001, so earlier bars never signal."],
)

S["cumulative_rsi_dip"] = dict(
    symbols=["DIA"], universe="etf", warmup=260, mc=(12, 6, 24),
    params={"n": 3, "threshold": 30},
    space={"n": {"min": 2, "max": 5, "step": 1, "hard_min": 1, "hard_max": 10},
           "threshold": {"min": 10, "max": 60, "step": 2, "hard_min": 1}},
    valid="True",
    buy='''c = df["close"]
    r = rsi_ind(c, 2, key=id(df))
    return (r.rolling(p["n"]).sum() < p["threshold"]) & (c > sma(c, 200))''',
    sell='''return rsi_ind(df["close"], 2, key=id(df)) > 65''',
    buy_txt="`sum(RSI(2), last n bars incl. t) < threshold` AND `C > SMA(200)`",
    sell_txt="`RSI(2) > 65`",
    ptab=[("n", "bars summed", "3", "2–5", "1"), ("threshold", "cumulative RSI level", "30", "10–60", "2")],
)

COMMON_ASSUMPTIONS = [
    "Sizing: 100% of equity per trade (user's choice for the library, 2026-11-24, so results compare across the leaderboard); the spec's risk_fraction is not used or tuned.",
    "Costs: fee 0.05%/side + slippage 0.03%/fill, the US ETF/stock convention of the user-approved absolute_momentum_monthly setup (above the spec's 1 bp + 2 bp + 2 bp). Exits at the target are charged slippage too (slightly conservative vs a limit order).",
    "Bars: Yahoo daily, dividend/split adjusted OHLC (the project has no separate raw execution series), used for signals and fills.",
    "ATR(14) is Wilder's RMA of true range with an SMA seed; stop and target are frozen at entry from the signal bar's ATR, never move, and are checked intrabar (stop first when both touch). A gap through the stop fills at the open; a target fills at the target price.",
    "max_candles is the template's max_bars (entry bar counts as 1; exit at the next open after bar N).",
    "Entry veto: no entry when the strategy's own close-based exit is true on the signal bar. After an intrabar stop/target exit, the next entry needs a signal from the following bar on (one fully flat bar).",
    "Base symbol = the first listed candidate; the others (and the rest of the universe) are covered by screening, since the spec calls the listed instruments alternatives, not a basket.",
    "Period: in-sample 1995-01-01 (or the symbol's first warmed-up bar) to 2016-01-01, out-of-sample to 2026-11-23 (frozen): repo precedent for ETF strategies.",
]

BLOCK = '''# --------------------------------------------------------------------------
# Strategy definition: adapt everything in this block in the copy.
# --------------------------------------------------------------------------
# Library spec: strategies/{name}/original.md (+ ../../EXECUTION.md, ../../INDICATORS.md).
# Generated by scripts/library_gen.py; strategy.md is the readable version.
CONFIG = {{
    "name": "{name}",
    "asset_class": "etf",           # Yahoo daily, adjusted
    "symbols": {symbols!r},
    "timeframe": "1d",
    "start": "1995-01-01",
    "oos_start": "2016-01-01",      # repo precedent for ETF strategies
    "end": "2026-11-23",            # frozen at setup (last complete daily bar)
    "capital": 10_000.0,
    "position_pct": 1.0,            # user's choice: 100% of equity (spec's risk_fraction not used)
    "fee_pct": 0.05,
    "slippage_pct": 0.03,
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": {warmup},
}}

# {atr_doc}
PARAMS = {params!r}

SPACE = {space!r}


def valid(p: dict) -> bool:
    return bool({valid}) and p["stop_atr"] > 0 and p["take_profit_atr"] > 0 and p["max_bars"] >= 1

{indicators}

def buy_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    {buy}


def sell_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    {sell}

'''

# ---------------------------------------------------------------- machinery patch
PATCHES = [
    # _simulate: ATR levels, skip invalid, resting target fill, re-entry gap
    ("def _simulate(df: pd.DataFrame, buy: np.ndarray, sell: np.ndarray, p: dict, lo: int, hi: int, capital: float, symbol: str):",
     "def _simulate(df: pd.DataFrame, buy: np.ndarray, sell: np.ndarray, p: dict, lo: int, hi: int, capital: float, symbol: str,\n              atr_arr: np.ndarray | None = None):"),
    ("    trail, max_bars = p.get(\"trailing_stop_pct\", 0) / 100, int(p.get(\"max_bars\", 0) or 0)\n",
     "    trail, max_bars = p.get(\"trailing_stop_pct\", 0) / 100, int(p.get(\"max_bars\", 0) or 0)\n"
     "    s_atr, t_atr = float(p.get(\"stop_atr\", 0) or 0), float(p.get(\"take_profit_atr\", 0) or 0)  # library: frozen ATR exits\n"
     "    use_atr = atr_arr is not None and (s_atr or t_atr)\n"),
    ("        entry = o[e] * (1 + slip)\n",
     "        entry = o[e] * (1 + slip)\n"
     "        sl_lvl = tp_lvl = None\n"
     "        if use_atr:                                 # E = fill, A = ATR(14) of the signal bar, both frozen\n"
     "            A = atr_arr[s]\n"
     "            if not np.isfinite(A) or A <= 0 or (s_atr and entry - s_atr * A <= 0):\n"
     "                i = s + 1                           # spec: skip the signal\n"
     "                continue\n"
     "            sl_lvl = entry - s_atr * A if s_atr else None\n"
     "            tp_lvl = entry + t_atr * A if t_atr else None\n"),
    ("            stop = max(entry * (1 - sl) if sl else -np.inf, peak * (1 - trail) if trail else -np.inf)\n",
     "            stop = max(entry * (1 - sl) if sl else -np.inf, peak * (1 - trail) if trail else -np.inf,\n"
     "                       sl_lvl if sl_lvl is not None else -np.inf)\n"),
    ("            if tp and h[j] >= entry * (1 + tp):\n                x, price, reason = j, max(o[j], entry * (1 + tp)), \"target\"\n                break\n",
     "            if tp and h[j] >= entry * (1 + tp):\n                x, price, reason = j, max(o[j], entry * (1 + tp)), \"target\"\n                break\n"
     "            if tp_lvl is not None and h[j] >= tp_lvl:  # resting limit: fills at the target, never better\n"
     "                x, price, reason = j, tp_lvl, \"target\"\n                break\n"),
    ("            if not (sl or tp or trail or max_bars):  # pure signal exit: jump straight to it\n",
     "            if not (sl or tp or trail or max_bars or sl_lvl is not None or tp_lvl is not None):  # pure signal exit\n"),
    ("        i = x\n    eq = pd.Series",
     "        i = x + 1 if reason in (\"stop\", \"target\") else x   # intrabar exit: need one fully flat bar first\n    eq = pd.Series"),
    # run(): entry veto + ATR array
    ("        sell = sell_signal(df, p).fillna(False).to_numpy(bool)\n        t, eq = _simulate(df, buy, sell, p, lo, hi, per_cap, sym)\n",
     "        sell = sell_signal(df, p).fillna(False).to_numpy(bool)\n"
     "        buy = buy & ~sell                           # spec: veto entries whose own exit is already true\n"
     "        t, eq = _simulate(df, buy, sell, p, lo, hi, per_cap, sym, atr(df, 14).to_numpy(float))\n"),
]


def build(name: str, d: dict) -> str:
    tpl = TEMPLATE.read_text()
    a, b = tpl.index(BEGIN), tpl.index(END)
    mc_start, mc_min, mc_max = d["mc"]
    params = {**d["params"], "stop_atr": 2.0, "take_profit_atr": 3.0, "max_bars": mc_start}
    space = {**d["space"], **atr_space(mc_start, mc_min, mc_max)}
    block = BLOCK.format(name=name, symbols=d["symbols"], warmup=d["warmup"], atr_doc=ATR_PARAMS_DOC,
                         params=params, space=space, valid=d["valid"], indicators=INDICATORS.strip("\n"),
                         buy=d["buy"], sell=d["sell"])
    out = tpl[:a] + block + tpl[b:]
    for old, new in PATCHES:
        if out.count(old) != 1:
            raise SystemExit(f"{name}: patch anchor not found exactly once: {old[:60]!r}")
        out = out.replace(old, new)
    return out


def strategy_md(name: str, d: dict) -> str:
    mc_start, mc_min, mc_max = d["mc"]
    title = name.replace("_", " ").title()
    rows = "\n".join(f"| {n} | {m} | {s} | {r} | {st} |" for n, m, s, r, st in d["ptab"])
    step = max(1, round((mc_max - mc_min) / 12))
    assumptions = "\n".join(f"- {x}" for x in COMMON_ASSUMPTIONS + d.get("extra_assumptions", []))
    return f"""# {title}

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: {', '.join(d['symbols'])} (base run); screening universe: `{d['universe']}` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- {d['buy_txt']}
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- {d['sell_txt']} at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
{rows}
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | {mc_start} | {mc_min}–{mc_max} | {step} |

Constraints: {d.get('constraints', 'none beyond positive exits')}. All other numbers in the triggers are fixed constants of the spec.

## Setup
- In-sample (tuning): 1995-01-01 (or the symbol's first bar after {d['warmup']} warm-up bars) → 2016-01-01
- Out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
{assumptions}

## Open questions
- none (library conventions agreed across the library sessions and the user's absolute_momentum_monthly choices)
"""


def main():
    root = Path(sys.argv[1])
    names = sys.argv[2:] or list(S)
    for n in names:
        d = S[n]
        folder = root / "strategies" / n
        assert (folder / "original.md").exists(), n
        (folder / "backtest.py").write_text(build(n, d))
        (folder / "strategy.md").write_text(strategy_md(n, d))
        print("wrote", folder)


if __name__ == "__main__":
    main()
