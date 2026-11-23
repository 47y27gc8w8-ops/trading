"""Daily OHLC loaders for backtesting.

Crypto: aggregated from the 1m Binance partitions to UTC daily bars with DuckDB
and cached in data/cache/crypto_1d.parquet (rebuilt when older than 12h).
ETF: data/etf/1d/<ticker>.parquet, OHLC rescaled by adj_close/close so returns
include dividends and splits.
"""
from __future__ import annotations

import time
from functools import lru_cache

import duckdb
import pandas as pd

from src.common.storage import CRYPTO_1M, DATA, ETF_1D

CACHE = DATA / "cache" / "crypto_1d.parquet"
MAX_AGE_S = 12 * 3600


def _build_crypto_cache() -> None:
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    glob = str(CRYPTO_1M / "symbol=*" / "*" / "*" / "*.parquet")
    df = duckdb.sql(f"""
        SELECT symbol, date_trunc('day', open_time) AS date,
               arg_min(open, open_time) AS open, max(high) AS high, min(low) AS low,
               arg_max(close, open_time) AS close, sum(quote_volume) AS volume,
               count(*) AS n_minutes
        FROM read_parquet('{glob}', hive_partitioning=true)
        GROUP BY ALL ORDER BY symbol, date
    """).df()
    # drop today's incomplete bar
    df["date"] = pd.to_datetime(df["date"], utc=True)
    df = df[df["date"] < pd.Timestamp.now(tz="UTC").normalize()]
    tmp = CACHE.with_suffix(".tmp")
    df.to_parquet(tmp, index=False)
    tmp.replace(CACHE)


@lru_cache(maxsize=1)
def _crypto_all() -> pd.DataFrame:
    if not CACHE.exists() or time.time() - CACHE.stat().st_mtime > MAX_AGE_S:
        _build_crypto_cache()
    df = pd.read_parquet(CACHE)
    df["date"] = pd.to_datetime(df["date"], utc=True)
    return df


def load_crypto(symbol: str) -> pd.DataFrame:
    df = _crypto_all()
    df = df[df["symbol"] == symbol].set_index("date")[["open", "high", "low", "close", "volume"]]
    if df.empty:
        raise ValueError(f"no crypto data for {symbol}")
    return df.sort_index()


def load_etf(ticker: str) -> pd.DataFrame:
    df = pd.read_parquet(ETF_1D / f"{ticker}.parquet").set_index("date").sort_index()
    f = (df["adj_close"] / df["close"]).fillna(1.0)
    out = pd.DataFrame({c: df[c] * f for c in ("open", "high", "low")})
    out["close"] = df["adj_close"]
    out["volume"] = df["volume"]
    return out.dropna(subset=["close"])


def load(asset_class: str, symbol: str) -> pd.DataFrame:
    return load_crypto(symbol) if asset_class == "crypto" else load_etf(symbol)
