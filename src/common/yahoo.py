"""Thin yfinance wrapper: disk cache location, error raising and 429 backoff."""
from __future__ import annotations

import logging

import pandas as pd
import yfinance as yf
from tenacity import before_sleep_log, retry, retry_if_exception, stop_after_attempt, wait_exponential
from yfinance.exceptions import (
    YFInvalidPeriodError, YFPricesMissingError, YFTickerMissingError, YFTzMissingError,
)

from src.common.storage import DATA, to_utc_ns

log = logging.getLogger("yahoo")
(DATA / ".yf_cache").mkdir(parents=True, exist_ok=True)
yf.set_tz_cache_location(str(DATA / ".yf_cache"))
# Raise errors instead of returning empty frames (yfinance >= 1.x; `raise_errors=` is deprecated)
yf.config.debug.hide_exceptions = False


class NoData(Exception):
    pass


# Permanent errors: retrying won't help (bad ticker, range outside Yahoo's window, ...)
PERMANENT = (NoData, YFPricesMissingError, YFTickerMissingError, YFTzMissingError, YFInvalidPeriodError)


@retry(retry=retry_if_exception(lambda e: not isinstance(e, PERMANENT)),
       wait=wait_exponential(multiplier=5, min=5, max=300), stop=stop_after_attempt(6),
       before_sleep=before_sleep_log(log, logging.WARNING), reraise=True)
def history(ticker: str, **kwargs) -> pd.DataFrame:
    """yf.Ticker.history with exceptions enabled (yf.download swallows errors, so
    rate limits would silently look like "no data"). Retries with exponential backoff."""
    df = yf.Ticker(ticker).history(**kwargs)
    if df is None or df.empty:
        raise NoData(f"{ticker}: empty response for {kwargs}")
    df = df.reset_index()
    df.columns = [str(c).lower().replace(" ", "_") for c in df.columns]
    return df


def utc(s: pd.Series) -> pd.Series:
    return to_utc_ns(s)
