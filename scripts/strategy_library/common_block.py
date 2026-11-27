# ---- Library indicators (INDICATORS.md conventions), inlined by scripts/strategy_library/build.py ----
_MEMO: dict = {}


def _memo(key, fn):
    """Cache per bar frame (frames are cached in _BARS, so id(df) is stable) and parameter values."""
    if key not in _MEMO:
        _MEMO[key] = fn()
    return _MEMO[key]


def _seeded_ewm(x: pd.Series, n: int, alpha: float) -> pd.Series:
    """Recursive average seeded with the SMA of the first n valid values (EMA / Wilder RMA)."""
    x = x.astype(float)
    v = x.dropna()
    out = pd.Series(np.nan, index=x.index)
    if len(v) < n:
        return out
    first = x.index.get_loc(v.index[0])
    s = x.copy()
    s.iloc[: first + n - 1] = np.nan
    s.iloc[first + n - 1] = v.iloc[:n].mean()
    return s.ewm(alpha=alpha, adjust=False, ignore_na=True).mean()


def ema(x: pd.Series, n: int) -> pd.Series:
    return _seeded_ewm(x, int(n), 2.0 / (int(n) + 1))


def rma(x: pd.Series, n: int) -> pd.Series:
    return _seeded_ewm(x, int(n), 1.0 / int(n))


def sma(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(int(n), min_periods=int(n)).mean()


def true_range(df: pd.DataFrame) -> pd.Series:
    pc = df["close"].shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()], axis=1).max(axis=1)
    tr.iloc[0] = np.nan                      # first bar has no previous close
    return tr


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return _memo(("atr", id(df), int(n)), lambda: rma(true_range(df), n))


def rsi_w(x: pd.Series, n: int) -> pd.Series:
    """Wilder RSI; both averages 0 -> 50, no losses -> 100, no gains -> 0."""
    d = x.diff()
    up, dn = rma(d.clip(lower=0), n), rma((-d).clip(lower=0), n)
    r = 100 - 100 / (1 + up / dn)
    r = r.where(dn != 0, 100.0).where(~((up == 0) & (dn == 0)), 50.0)
    return r.where(up.notna() & dn.notna())


def rsi_c(df: pd.DataFrame, n: int) -> pd.Series:
    return _memo(("rsi", id(df), int(n)), lambda: rsi_w(df["close"], n))


def clv01(df: pd.DataFrame) -> pd.Series:
    rng = df["high"] - df["low"]
    return ((df["close"] - df["low"]) / rng).where(rng != 0, 0.5)


def roc(x: pd.Series, n: int) -> pd.Series:
    return 100 * (x / x.shift(int(n)) - 1)


def hh(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(int(n), min_periods=int(n)).max()


def ll(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(int(n), min_periods=int(n)).min()


def std0(x: pd.Series, n: int) -> pd.Series:
    return x.rolling(int(n), min_periods=int(n)).std(ddof=0)


def cross_above(x: pd.Series, y) -> pd.Series:
    y1 = y.shift(1) if isinstance(y, pd.Series) else y
    return (x > y) & (x.shift(1) <= y1)


def cross_below(x: pd.Series, y) -> pd.Series:
    y1 = y.shift(1) if isinstance(y, pd.Series) else y
    return (x < y) & (x.shift(1) >= y1)


def dmi(df: pd.DataFrame, n: int = 14) -> tuple[pd.Series, pd.Series, pd.Series]:
    """(DI+, DI-, ADX), Wilder; flat denominators -> 0."""
    def calc():
        up = df["high"].diff()
        dn = -df["low"].diff()
        pdm = up.where((up > dn) & (up > 0), 0.0)
        mdm = dn.where((dn > up) & (dn > 0), 0.0)
        pdm.iloc[0] = mdm.iloc[0] = np.nan
        a = atr(df, n)
        dip = (100 * rma(pdm, n) / a).where(a != 0, 0.0)
        dim = (100 * rma(mdm, n) / a).where(a != 0, 0.0)
        s = dip + dim
        dx = (100 * (dip - dim).abs() / s).where(s != 0, 0.0).where(dip.notna() & dim.notna())
        return dip, dim, rma(dx, n)
    return _memo(("dmi", id(df), int(n)), calc)


def mfi(df: pd.DataFrame, n: int = 14) -> pd.Series:
    def calc():
        tp = (df["high"] + df["low"] + df["close"]) / 3
        mf = tp * df["volume"]
        d = tp.diff()
        pos = mf.where(d > 0, 0.0).rolling(n, min_periods=n).sum()
        neg = mf.where(d < 0, 0.0).rolling(n, min_periods=n).sum()
        out = 100 - 100 / (1 + pos / neg)
        out = out.where(neg != 0, 100.0).where(~((pos == 0) & (neg == 0)), 50.0)
        out.iloc[: n] = np.nan               # first TP difference is undefined
        return out
    return _memo(("mfi", id(df), int(n)), calc)


def stoch_rsi(df: pd.DataFrame, n: int) -> pd.Series:
    def calc():
        r = rsi_c(df, n)
        lo, hi = ll(r, n), hh(r, n)
        return ((r - lo) / (hi - lo)).where(hi != lo, 0.5).where(lo.notna())
    return _memo(("stochrsi", id(df), int(n)), calc)


def vwma(df: pd.DataFrame, n: int) -> pd.Series:
    n = int(n)
    return (df["close"] * df["volume"]).rolling(n, min_periods=n).sum() / df["volume"].rolling(n, min_periods=n).sum()


def bbands(df: pd.DataFrame, n: int, k: float) -> tuple[pd.Series, pd.Series, pd.Series]:
    mid = sma(df["close"], n)
    sd = std0(df["close"], n)
    return mid - k * sd, mid, mid + k * sd


def keltner(df: pd.DataFrame, n: int, a: int, k: float) -> tuple[pd.Series, pd.Series, pd.Series]:
    mid = ema(df["close"], n)
    at = atr(df, a)
    return mid - k * at, mid, mid + k * at


def prior_quantile(x: pd.Series, n: int, q: float) -> pd.Series:
    """Quantile (linear interpolation) of the preceding n values t-n..t-1."""
    return x.shift(1).rolling(int(n), min_periods=int(n)).quantile(q, interpolation="linear")


def bars_since_period_start(df: pd.DataFrame, freq: str) -> tuple[pd.Series, pd.Series]:
    """(period key, open of the current period) for UTC days ('D') or Monday-start UTC weeks ('W')."""
    idx = df.index.tz_convert("UTC").tz_localize(None)
    key = idx.to_period("W-SUN" if freq == "W" else "D")
    k = pd.Series(key, index=df.index)
    return k, df["open"].groupby(k.to_numpy()).transform("first")
# ---- end library indicators ----
