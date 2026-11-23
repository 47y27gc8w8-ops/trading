"""Every individual spot trade from the Binance archive (data.binance.vision), for the
top-N coins of config `crypto` (config: history.trades_top_n, history.trades_start).

Layout: data/crypto/trades/symbol=<S>/year=<Y>/month=<MM>/<period>.parquet
  period = YYYY-MM (monthly zip) or YYYY-MM-DD (daily zips, until the monthly one exists;
  they are deleted once the monthly file for that month is ingested).
Columns: trade_id, price, qty, quote_qty, time (UTC, µs), is_buyer_maker
  is_buyer_maker = True means the taker sold (hit the bid).

Files are streamed (zip -> CSV batches -> Parquet row groups), so a 1 GB BTC month
never has to fit in memory. A finished Parquet file = ingested (atomic rename).
Stops cleanly when the storage budget is >= 95 % used.

Usage: python -m src.collectors.binance_trades [--symbols ...] [--top 20] [--start 2023-12] [--workers 3]
"""
from __future__ import annotations

import argparse
import os
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.csv as pacsv
import pyarrow.parquet as pq

from src.common import binance_archive as arc
from src.common.budget import allow_backfill
from src.common.storage import DATA, load_config, setup_logging

log = setup_logging("binance_trades")
TRADES = DATA / "crypto" / "trades"
TMP = DATA / "raw" / "tmp_trades"
NAMES = ["trade_id", "price", "qty", "quote_qty", "time", "is_buyer_maker", "is_best_match"]
TYPES = {"trade_id": pa.int64(), "price": pa.float64(), "qty": pa.float64(), "quote_qty": pa.float64(),
         "time": pa.int64(), "is_buyer_maker": pa.bool_(), "is_best_match": pa.bool_()}
SCHEMA = pa.schema([("trade_id", pa.int64()), ("price", pa.float64()), ("qty", pa.float64()),
                    ("quote_qty", pa.float64()), ("time", pa.timestamp("us", tz="UTC")), ("is_buyer_maker", pa.bool_())])


def out_path(symbol: str, period: str):
    return TRADES / f"symbol={symbol}" / f"year={period[:4]}" / f"month={period[5:7]}" / f"{period}.parquet"


def convert(zip_path, dest) -> int:
    """Stream one archive zip into a Parquet file. Returns the number of trades."""
    tmp = dest.with_name("." + dest.name + ".tmp")
    dest.parent.mkdir(parents=True, exist_ok=True)
    rows = 0
    with zipfile.ZipFile(zip_path) as z, z.open(z.namelist()[0]) as f:
        reader = pacsv.open_csv(
            f, read_options=pacsv.ReadOptions(column_names=NAMES, block_size=64 << 20),
            convert_options=pacsv.ConvertOptions(column_types=TYPES, include_columns=NAMES[:6]))
        with pq.ParquetWriter(tmp, SCHEMA, compression="zstd", compression_level=6) as w:
            for batch in reader:
                t = batch.column("time")
                # archive timestamps: ms until 2024, µs from 2025 -> always µs
                us = pc.if_else(pc.less(t, 10 ** 14), pc.multiply(t, 1000), t)
                tbl = pa.table([batch.column(c) for c in NAMES[:4]] + [us.cast(pa.timestamp("us", tz="UTC")),
                                                                      batch.column("is_buyer_maker")], schema=SCHEMA)
                w.write_table(tbl, row_group_size=2_000_000)
                rows += len(tbl)
    os.replace(tmp, dest)
    return rows


def ingest(symbol: str, kind: str, period: str) -> str:
    dest = out_path(symbol, period)
    if dest.exists():
        return "skip"
    key = f"data/spot/{kind}/trades/{symbol}/{symbol}-trades-{period}.zip"
    zpath = TMP / f"{symbol}-trades-{period}.zip"
    try:
        if arc.download(key, zpath) is None:
            return "missing"
        n = convert(zpath, dest)
    finally:
        zpath.unlink(missing_ok=True)
    if kind == "monthly":  # monthly file supersedes the daily files of that month
        for d in dest.parent.glob(f"{period}-*.parquet"):
            d.unlink()
    log.info("%s %s: %s trades, %.0f MB", symbol, period, f"{n:,}", dest.stat().st_size / 1e6)
    return "ok"


def plan(symbol: str, start: str) -> list[tuple[str, str]]:
    monthly = sorted(p for p in arc.zips(f"data/spot/monthly/trades/{symbol}/") if p >= start)
    todo = [("monthly", p) for p in monthly if not out_path(symbol, p).exists()]
    now = datetime.now(timezone.utc)
    cur, today = now.strftime("%Y-%m"), now.strftime("%Y-%m-%d")
    y, m = (int(x) for x in (monthly[-1] if monthly else start).split("-"))
    months = []
    while f"{y}-{m:02d}" <= cur:
        if not monthly or f"{y}-{m:02d}" > monthly[-1]:
            months.append(f"{y}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    for mon in months:
        for d in sorted(arc.zips(f"data/spot/daily/trades/{symbol}/{symbol}-trades-{mon}")):
            if d < today and d[:7] >= start and not out_path(symbol, d).exists():
                todo.append(("daily", d))
    return todo


def main() -> None:
    cfg = load_config()
    h = cfg.get("history", {}) or {}
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", nargs="*")
    ap.add_argument("--top", type=int, default=int(h.get("trades_top_n", 20)))
    ap.add_argument("--start", default=str(h.get("trades_start", "2023-12")))
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()
    symbols = args.symbols or list(cfg["crypto"])[: args.top]
    TMP.mkdir(parents=True, exist_ok=True)
    for f in TMP.glob("*"):  # leftovers from an interrupted run
        f.unlink()

    todo = []
    for s in symbols:
        p = plan(s, args.start)
        log.info("%s: %d files to ingest", s, len(p))
        todo += [(s, k, per) for k, per in p]
    # newest first: recent months are the most useful if the run is interrupted
    todo.sort(key=lambda t: t[2], reverse=True)
    stats: dict[str, int] = {}
    errors = 0
    with ThreadPoolExecutor(args.workers) as pool:
        futs = {}
        it = iter(todo)
        def submit_next():
            for job in it:
                futs[pool.submit(ingest, *job)] = job
                return True
            return False
        for _ in range(args.workers * 2):
            submit_next()
        done_n = 0
        while futs:
            fut = next(as_completed(futs))
            job = futs.pop(fut)
            try:
                r = fut.result()
                stats[r] = stats.get(r, 0) + 1
            except Exception:
                errors += 1
                log.exception("%s %s failed", job[0], job[2])
            done_n += 1
            if done_n % 10 == 0 and not allow_backfill():
                break
            if done_n % 25 == 0:
                log.info("progress: %d/%d files, %s, errors=%d", done_n, len(todo), stats, errors)
            submit_next()
    log.info("done: %s, errors=%d", stats, errors)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
