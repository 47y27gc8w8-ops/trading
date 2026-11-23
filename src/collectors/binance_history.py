"""Backfill 1m spot klines from the Binance public archive (data.binance.vision).

- Monthly zips from `crypto_history_start` to last month, daily zips for the
  current month (and for last month if its monthly zip isn't published yet).
- SHA256 checksum verified, 404 = "no data" (pair not listed yet).
- Already ingested periods are skipped (marker files in data/crypto/1m/_ingested).

Usage: python -m src.collectors.binance_history [--symbols BTCUSDT ...] [--keep-raw]
"""
from __future__ import annotations

import argparse
import hashlib
import io
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta, timezone

import pandas as pd
import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from src.common.storage import (
    CRYPTO_1M, CRYPTO_COLUMNS, RAW_BINANCE, load_config, setup_logging, to_utc_ns, write_crypto,
)

log = setup_logging("binance_history")
BASE = "https://data.binance.vision/data/spot"
RAW_COLUMNS = CRYPTO_COLUMNS + ["ignore"]
MARKERS = CRYPTO_1M / "_ingested"
session = requests.Session()


class Retryable(Exception):
    pass


@retry(retry=retry_if_exception_type((Retryable, requests.ConnectionError, requests.Timeout)),
       wait=wait_exponential(multiplier=2, max=120), stop=stop_after_attempt(8), reraise=True)
def fetch(url: str) -> bytes | None:
    r = session.get(url, timeout=60)
    if r.status_code == 404:
        return None
    if r.status_code in (418, 429) or r.status_code >= 500:
        raise Retryable(f"HTTP {r.status_code} for {url}")
    r.raise_for_status()
    return r.content


def to_utc(col: pd.Series) -> pd.Series:
    """Archive timestamps are ms (older files) or µs (newer spot files): detect by magnitude."""
    col = col.astype("int64")
    us = col >= 10**14
    ms = col.where(~us, col // 1000)
    return to_utc_ns(pd.to_datetime(ms, unit="ms", utc=True))


def parse_zip(blob: bytes) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        with z.open(z.namelist()[0]) as f:
            df = pd.read_csv(f, header=None, names=RAW_COLUMNS, dtype=str)
    # a few archive files contain a header row: drop anything non-numeric
    df["open_time"] = pd.to_numeric(df["open_time"], errors="coerce")
    df = df.dropna(subset=["open_time"])
    df["close_time"] = pd.to_numeric(df["close_time"])
    df["open_time"] = to_utc(df["open_time"])
    df["close_time"] = to_utc(df["close_time"])
    for c in ["open", "high", "low", "close", "volume", "quote_volume", "taker_buy_base", "taker_buy_quote"]:
        df[c] = df[c].astype("float64")
    df["trades"] = df["trades"].astype("int64")
    return df[CRYPTO_COLUMNS]


def ingest(symbol: str, kind: str, period: str, keep_raw: bool) -> str:
    """Download, verify and store one archive file. Returns 'ok', 'skip' or 'missing'."""
    marker = MARKERS / symbol / period
    if marker.exists():
        return "skip"
    name = f"{symbol}-1m-{period}.zip"
    url = f"{BASE}/{kind}/klines/{symbol}/1m/{name}"
    blob = fetch(url)
    if blob is None:
        return "missing"
    checksum = fetch(url + ".CHECKSUM")
    if checksum is None:
        raise RuntimeError(f"no checksum for {name}")
    expected = checksum.decode().split()[0].lower()
    actual = hashlib.sha256(blob).hexdigest()
    if actual != expected:
        raise RuntimeError(f"checksum mismatch for {name}: {actual} != {expected}")
    raw = RAW_BINANCE / symbol / name
    if keep_raw:
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(blob)
    df = parse_zip(blob)
    added = write_crypto(symbol, df)
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(f"{len(df)} rows, {added} new, {datetime.now(timezone.utc).isoformat()}\n")
    log.info("%s %s: %d rows (%d new)", symbol, period, len(df), added)
    return "ok"


def ingest_days(symbol: str, year: int, month: int, keep_raw: bool) -> dict:
    """Daily files for one month, up to yesterday (UTC)."""
    yesterday = datetime.now(timezone.utc).date() - timedelta(days=1)
    d = date(year, month, 1)
    stats: dict[str, int] = {}
    while d.month == month and d <= yesterday:
        res = ingest(symbol, "daily", d.isoformat(), keep_raw)
        stats[res] = stats.get(res, 0) + 1
        d += timedelta(days=1)
    return stats


def month_task(symbol: str, year: int, month: int, keep_raw: bool, recent: bool) -> dict:
    period = f"{year}-{month:02d}"
    res = ingest(symbol, "monthly", period, keep_raw)
    if res == "missing" and recent:
        # monthly zip for last month is published a few days into the new month
        return ingest_days(symbol, year, month, keep_raw)
    return {res: 1}


def months(start: str, end: date):
    y, m = map(int, start.split("-"))
    while (y, m) <= (end.year, end.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def main() -> None:
    cfg = load_config()
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", nargs="*", default=cfg["crypto"])
    ap.add_argument("--start", default=str(cfg.get("crypto_history_start", "2017-08")))
    ap.add_argument("--keep-raw", action="store_true", help="keep downloaded zips in data/raw/binance")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    today = datetime.now(timezone.utc).date()
    last_month = (today.replace(day=1) - timedelta(days=1))
    totals: dict[str, int] = {}
    errors = 0
    for symbol in args.symbols:
        log.info("backfilling %s from %s", symbol, args.start)
        with ThreadPoolExecutor(args.workers) as pool:
            futs = {
                pool.submit(month_task, symbol, y, m, args.keep_raw, (y, m) == (last_month.year, last_month.month)): (y, m)
                for y, m in months(args.start, last_month)
            }
            for fut in as_completed(futs):
                try:
                    for k, v in fut.result().items():
                        totals[k] = totals.get(k, 0) + v
                except Exception:
                    errors += 1
                    log.exception("%s %s failed", symbol, futs[fut])
        # current month: daily files up to yesterday
        try:
            for k, v in ingest_days(symbol, today.year, today.month, args.keep_raw).items():
                totals[k] = totals.get(k, 0) + v
        except Exception:
            errors += 1
            log.exception("%s daily files for current month failed", symbol)

    log.info("done: %s, errors=%d", totals, errors)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
