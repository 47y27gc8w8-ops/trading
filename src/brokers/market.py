"""Market data for the bots: public endpoints only, no API keys, retried with backoff.

- Crypto: Binance spot klines through ccxt's public API (an exchange object WITHOUT keys).
  The kline volume used is the quote volume, matching the project's 1m history.
- ETFs/stocks: Yahoo Finance daily bars through yfinance (dividend/split adjusted).
- FX: USDCHF=X from Yahoo. USDT is treated as USD.
- NYSE regular hours with the exchange's holidays and early closes.

Each returned frame includes the bar that is still forming, so the strategy's own simulation
can act on it (entries fill at the open of the bar after a signal, stops trigger intrabar).
"""
from __future__ import annotations

import logging
import time
from datetime import date, datetime, time as dtime
from zoneinfo import ZoneInfo

import pandas as pd

log = logging.getLogger("brokers.market")
NY = ZoneInfo("America/New_York")


class DataError(RuntimeError):
    """A data source failed after all retries."""


on_retry = None   # optional callback(what, error, attempt, wait): the bot journals data-source retries


def retry(fn, what: str, attempts: int = 5, base: float = 2.0, cap: float = 60.0):
    """Call fn(); on an exception wait base, 2*base, 4*base ... (capped) and try again."""
    for k in range(attempts):
        try:
            return fn()
        except Exception as ex:  # noqa: BLE001 - any source failure is retried
            if k == attempts - 1:
                raise DataError(f"{what}: {type(ex).__name__}: {ex}") from ex
            wait = min(cap, base * 2 ** k)
            log.warning("%s failed (%s: %s), retry %d/%d in %.0fs", what, type(ex).__name__, str(ex)[:200], k + 1, attempts - 1, wait)
            if on_retry:
                try:
                    on_retry(what, f"{type(ex).__name__}: {str(ex)[:300]}", k + 1, wait)
                except Exception:  # noqa: BLE001 - logging must never break data fetching
                    pass
            time.sleep(wait)


# ------------------------------------------------------------------ crypto ---
_EX = None


def _exchange():
    global _EX
    if _EX is None:
        import ccxt
        _EX = ccxt.binance({"enableRateLimit": True, "timeout": 20000})
        # Paper only: this object never gets credentials, so private endpoints (orders,
        # balances) are unusable. Guard against someone adding keys later.
        assert not _EX.apiKey and not _EX.secret, "brokers are paper only: no exchange keys allowed"
    return _EX


_TF = {"1d": "1d", "1D": "1d", "4h": "4h", "1h": "1h"}


def crypto_bars(symbol: str, timeframe: str, limit: int = 60) -> pd.DataFrame:
    """Latest `limit` klines (UTC open times) incl. the forming one."""
    interval = _TF[timeframe]
    rows = retry(lambda: _exchange().publicGetKlines({"symbol": symbol, "interval": interval, "limit": limit}),
                 f"binance klines {symbol} {interval}")
    if not rows:
        raise DataError(f"binance returned no klines for {symbol}")
    df = pd.DataFrame(rows).iloc[:, :8]
    df.columns = ["t", "open", "high", "low", "close", "base_volume", "close_t", "volume"]
    df.index = pd.to_datetime(df["t"].astype("int64"), unit="ms", utc=True)
    df.index.name = "date"
    return df[["open", "high", "low", "close", "volume"]].astype(float)


# --------------------------------------------------------------------- Yahoo ---
def yahoo_daily(symbols: list[str], period: str = "1mo") -> dict[str, pd.DataFrame]:
    """Adjusted daily bars per symbol (index = UTC midnight of the exchange date), incl. today."""
    import yfinance as yf

    def get():
        raw = yf.download(symbols, period=period, interval="1d", auto_adjust=True, group_by="ticker",
                          threads=False, progress=False)
        if raw is None or raw.empty:
            raise DataError("yfinance returned nothing")
        return raw

    raw = retry(get, f"yahoo daily {','.join(symbols)[:60]}")
    out = {}
    for s in symbols:
        try:
            df = raw[s] if isinstance(raw.columns, pd.MultiIndex) else raw
        except KeyError:
            continue
        df = df.rename(columns=str.lower)[["open", "high", "low", "close", "volume"]].dropna(subset=["open", "close"])
        if df.empty:
            continue
        df.index = pd.DatetimeIndex(pd.to_datetime(pd.Index(df.index).date)).tz_localize("UTC")
        df.index.name = "date"
        out[s] = df.astype(float)
    missing = set(symbols) - set(out)
    if missing:
        raise DataError(f"yahoo: no data for {sorted(missing)}")
    return out


def usdchf() -> float:
    import yfinance as yf

    def get():
        h = yf.Ticker("USDCHF=X").history(period="5d", interval="1h")
        v = float(h["Close"].dropna().iloc[-1])
        if not 0.3 < v < 3:
            raise DataError(f"implausible USDCHF {v}")
        return v

    return retry(get, "yahoo USDCHF=X")


# ----------------------------------------------------------- NYSE calendar ---
# Full-day closures and 13:00 early closes, from the NYSE holiday schedule. Extend yearly.
NYSE_HOLIDAYS = {date.fromisoformat(d) for d in (
    "2026-01-01 2026-01-19 2026-02-16 2026-04-03 2026-05-25 2026-06-19 2026-07-03 2026-09-07 2026-11-26 2026-12-25 "
    "2027-01-01 2027-01-18 2027-02-15 2027-03-26 2027-05-31 2027-06-18 2027-07-05 2027-09-06 2027-11-25 2027-12-24 "
    "2028-01-17 2028-02-21 2028-04-14 2028-05-29 2028-06-19 2028-07-04 2028-09-04 2028-11-23 2028-12-25"
).split()}
NYSE_EARLY_CLOSE = {date.fromisoformat(d) for d in "2026-11-27 2026-12-24 2027-11-26 2028-07-03 2028-11-24".split()}


def nyse_open(now: datetime | None = None, settle_minutes: int = 2) -> bool:
    """True during regular NYSE hours. The first `settle_minutes` after the bell are skipped so
    Yahoo has published the day's opening price."""
    t = (now or datetime.now(NY)).astimezone(NY)
    d = t.date()
    if d.weekday() >= 5 or d in NYSE_HOLIDAYS:
        return False
    if d.year > max(h.year for h in NYSE_HOLIDAYS):
        log.warning("NYSE holiday table ends before %s: extend NYSE_HOLIDAYS in src/brokers/market.py", d.year)
    close = dtime(13, 0) if d in NYSE_EARLY_CLOSE else dtime(16, 0)
    return dtime(9, 30 + settle_minutes) <= t.time() < close
