"""Backfill 1m spot klines from the Binance public archive (data.binance.vision).

- The bucket is listed per symbol, so exactly the published files are fetched:
  monthly zips, plus daily zips for the months after the newest monthly zip.
- SHA256 checksum verified.
- Already ingested periods are skipped (marker files in data/crypto/1m/_ingested).
- --all-usdt: every USDT pair Binance ever listed, including delisted ones (for
  survivorship-bias-free backtests). Stablecoin/fiat legs and leveraged tokens are skipped.

Usage: python -m src.collectors.binance_history [--symbols BTCUSDT ...] [--all-usdt] [--keep-raw]
"""
from __future__ import annotations

import argparse
import io
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import pandas as pd

from src.common import binance_archive as arc
from src.common.budget import allow_backfill
from src.common.storage import (
    CRYPTO_1M, CRYPTO_COLUMNS, RAW_BINANCE, load_config, setup_logging, to_utc_ns, write_crypto,
)

log = setup_logging("binance_history")
RAW_COLUMNS = CRYPTO_COLUMNS + ["ignore"]
MARKERS = CRYPTO_1M / "_ingested"


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
    blob = arc.download(f"data/spot/{kind}/klines/{symbol}/1m/{name}")
    if blob is None:
        return "missing"
    if keep_raw:
        raw = RAW_BINANCE / symbol / name
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(blob)
    df = parse_zip(blob)
    added = write_crypto(symbol, df)
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(f"{len(df)} rows, {added} new, {datetime.now(timezone.utc).isoformat()}\n")
    log.info("%s %s: %d rows (%d new)", symbol, period, len(df), added)
    return "ok"


def plan(symbol: str, start: str) -> list[tuple[str, str]]:
    """[(kind, period)] still to ingest for a symbol, from the bucket listing."""
    monthly = sorted(p for p in arc.zips(f"data/spot/monthly/klines/{symbol}/1m/") if p >= start)
    todo = [("monthly", p) for p in monthly if not (MARKERS / symbol / p).exists()]
    # daily files for the months after the newest monthly zip (still listed pairs only)
    now = datetime.now(timezone.utc)
    cur = now.strftime("%Y-%m")
    last = monthly[-1] if monthly else None
    y, m = (int(x) for x in (last or cur).split("-"))
    months = []
    while f"{y}-{m:02d}" <= cur:
        if last is None or f"{y}-{m:02d}" > last:
            months.append(f"{y}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    today = now.strftime("%Y-%m-%d")
    for mon in months:
        for d in sorted(arc.zips(f"data/spot/daily/klines/{symbol}/1m/{symbol}-1m-{mon}")):
            if d < today and not (MARKERS / symbol / d).exists():
                todo.append(("daily", d))
    return todo


def backfill_symbol(symbol: str, start: str, keep_raw: bool, workers: int) -> tuple[dict, int]:
    totals: dict[str, int] = {}
    errors = 0
    todo = plan(symbol, start)
    if todo:
        log.info("%s: %d files to ingest", symbol, len(todo))
    with ThreadPoolExecutor(workers) as pool:
        futs = {pool.submit(ingest, symbol, k, p, keep_raw): p for k, p in todo}
        for fut in as_completed(futs):
            try:
                res = fut.result()
                totals[res] = totals.get(res, 0) + 1
            except Exception:
                errors += 1
                log.exception("%s %s failed", symbol, futs[fut])
    return totals, errors


def main() -> None:
    cfg = load_config()
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", nargs="*", default=None)
    ap.add_argument("--all-usdt", action="store_true",
                    help="also every USDT pair in the archive, incl. delisted (config: history.klines_all_usdt)")
    ap.add_argument("--start", default=str(cfg.get("crypto_history_start", "2017-08")))
    ap.add_argument("--keep-raw", action="store_true", help="keep downloaded zips in data/raw/binance")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    symbols = list(args.symbols or cfg["crypto"])
    if args.all_usdt or (args.symbols is None and cfg.get("history", {}).get("klines_all_usdt")):
        extra = [s for s in arc.all_usdt_pairs() if s not in symbols]
        log.info("all-usdt: %d extra pairs from the archive listing", len(extra))
        symbols += extra
    totals: dict[str, int] = {}
    errors = 0
    for i, symbol in enumerate(symbols, 1):
        if i % 10 == 1 and not allow_backfill():
            errors += 1
            break
        try:
            t, e = backfill_symbol(symbol, args.start, args.keep_raw, args.workers)
        except Exception:
            log.exception("%s: listing failed", symbol)
            t, e = {}, 1
        errors += e
        for k, v in t.items():
            totals[k] = totals.get(k, 0) + v
        if i % 50 == 0:
            log.info("progress: %d/%d symbols, %s, errors=%d", i, len(symbols), totals, errors)
    log.info("done: %d symbols, %s, errors=%d", len(symbols), totals, errors)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
