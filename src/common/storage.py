"""Shared helpers: config, logging, Parquet read/write with dedup, gap checks.

Layout (all timestamps UTC):
  data/crypto/1m/symbol=<S>/year=<Y>/month=<M>/data.parquet   key: open_time
  data/etf/1d/<ticker>.parquet                                key: date
  data/etf/1m/ticker=<T>/date=<YYYY-MM-DD>/data.parquet       key: timestamp
  data/quotes/source=<S>/date=<D>/hour=<HH>.parquet          key: (symbol, time)  30 s snapshots
  data/quotes/latest.json                                     newest quote per symbol

Despite the "etf" directory name, data/etf holds every Yahoo symbol: ETFs,
indices and stocks.

Writes are atomic (tmp file + rename) and guarded by an flock on a sibling
lock file, so the history backfill and the live collector can safely write to
the same partition at the same time (both containers share the host kernel).
"""
from __future__ import annotations

import fcntl
import logging
import logging.handlers
import os
import sys
from contextlib import contextmanager
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(os.environ.get("APP_ROOT", Path(__file__).resolve().parents[2]))
DATA = ROOT / "data"
LOGS = ROOT / "logs"
CONFIG = ROOT / "config" / "symbols.yaml"

CRYPTO_1M = DATA / "crypto" / "1m"
ETF_1D = DATA / "etf" / "1d"
ETF_1M = DATA / "etf" / "1m"
RAW_BINANCE = DATA / "raw" / "binance"
QUOTES = DATA / "quotes"

CRYPTO_COLUMNS = [
    "open_time", "open", "high", "low", "close", "volume", "close_time",
    "quote_volume", "trades", "taker_buy_base", "taker_buy_quote",
]


def load_config() -> dict:
    with open(CONFIG) as f:
        return yaml.safe_load(f)


def setup_logging(name: str) -> logging.Logger:
    LOGS.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)sZ %(levelname)s %(name)s: %(message)s", "%Y-%m-%dT%H:%M:%S")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    if not root.handlers:
        for h in (logging.StreamHandler(sys.stdout), logging.handlers.RotatingFileHandler(LOGS / f"{name}.log", maxBytes=5_000_000, backupCount=3)):
            h.setFormatter(fmt)
            root.addHandler(h)
    return logging.getLogger(name)


@contextmanager
def locked(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name("." + path.name + ".lock")  # dot-prefix: ignored by pyarrow datasets
    with open(lock, "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def to_utc_ns(s: pd.Series) -> pd.Series:
    """Normalise any datetime-like series to datetime64[ns, UTC]."""
    s = pd.to_datetime(s, utc=True)
    return s.astype("datetime64[ns, UTC]")


def _atomic_write(df: pd.DataFrame, path: Path) -> None:
    tmp = path.with_name("." + path.name + ".tmp")
    df.to_parquet(tmp, index=False, compression="zstd")
    os.replace(tmp, path)


def merge_write(path: Path, new: pd.DataFrame, key: str | list[str]) -> int:
    """Merge `new` into the Parquet file at `path`, dedup on `key` (new wins).

    Returns the number of rows added."""
    if new.empty:
        return 0
    with locked(path):
        if path.exists():
            old = pd.read_parquet(path)
            before = len(old)
            df = pd.concat([old, new], ignore_index=True)
        else:
            before = 0
            df = new
        df = df.drop_duplicates(subset=key, keep="last").sort_values(key).reset_index(drop=True)
        _atomic_write(df, path)
        return len(df) - before


# ---------------------------------------------------------------- crypto ---

def crypto_partition(symbol: str, year: int, month: int) -> Path:
    return CRYPTO_1M / f"symbol={symbol}" / f"year={year}" / f"month={month:02d}" / "data.parquet"


def write_crypto(symbol: str, df: pd.DataFrame) -> int:
    """Write 1m klines (CRYPTO_COLUMNS, open_time UTC) into monthly partitions."""
    if df.empty:
        return 0
    df = df[CRYPTO_COLUMNS]
    added = 0
    for (y, m), part in df.groupby([df.open_time.dt.year, df.open_time.dt.month]):
        added += merge_write(crypto_partition(symbol, y, m), part, "open_time")
    return added


def read_crypto(symbol: str) -> pd.DataFrame:
    files = sorted((CRYPTO_1M / f"symbol={symbol}").glob("year=*/month=*/data.parquet"))
    if not files:
        return pd.DataFrame(columns=CRYPTO_COLUMNS)
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True).sort_values("open_time")


def last_crypto_open_time(symbol: str) -> pd.Timestamp | None:
    files = sorted(
        (CRYPTO_1M / f"symbol={symbol}").glob("year=*/month=*/data.parquet"),
        key=lambda p: (int(p.parent.parent.name.split("=")[1]), int(p.parent.name.split("=")[1])),
    )
    if not files:
        return None
    return pd.read_parquet(files[-1], columns=["open_time"]).open_time.max()


# ------------------------------------------------------------------- ETF ---

def safe_ticker(ticker: str) -> str:
    """Filesystem-safe ticker name (e.g. '^GSPC' stays, '/' is replaced)."""
    return ticker.replace("/", "_")


def etf_daily_path(ticker: str) -> Path:
    return ETF_1D / f"{safe_ticker(ticker)}.parquet"


def etf_1m_partition(ticker: str, date: str) -> Path:
    return ETF_1M / f"ticker={safe_ticker(ticker)}" / f"date={date}" / "data.parquet"


def write_etf_1m(ticker: str, df: pd.DataFrame) -> int:
    if df.empty:
        return 0
    added = 0
    for d, part in df.groupby(df.timestamp.dt.strftime("%Y-%m-%d")):
        added += merge_write(etf_1m_partition(ticker, d), part, "timestamp")
    return added


def read_etf_1m(ticker: str) -> pd.DataFrame:
    files = sorted((ETF_1M / f"ticker={safe_ticker(ticker)}").glob("date=*/data.parquet"))
    if not files:
        return pd.DataFrame()
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True).sort_values("timestamp")


# ------------------------------------------------------------------ misc ---

def count_gaps(ts: pd.Series, freq: pd.Timedelta = pd.Timedelta(minutes=1)) -> tuple[int, int]:
    """Return (number of gaps, total missing bars) in a sorted timestamp series."""
    if len(ts) < 2:
        return 0, 0
    d = ts.sort_values().diff().dropna()
    big = d[d > freq]
    return int(len(big)), int((big / freq - 1).sum())


def dir_size(path: Path) -> int:
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file()) if path.exists() else 0
