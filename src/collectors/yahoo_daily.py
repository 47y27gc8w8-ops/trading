"""Full daily history per ticker from Yahoo Finance (yfinance).

Keeps both Close and Adj Close plus dividends and splits. On re-runs only the
missing tail is fetched; if the tail contains a new dividend or split (which
changes past Adj Close values) the full history is re-downloaded.
"""
from __future__ import annotations

import argparse
import time
from datetime import timedelta

import pandas as pd

from src.common.storage import etf_daily_path, load_config, merge_write, setup_logging
from src.common.yahoo import history, utc

log = setup_logging("yahoo_daily")
SLEEP_BETWEEN = 3


def normalise(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={"stock_splits": "splits", "datetime": "date"})
    # daily bars: store the trading date as UTC midnight
    df["date"] = utc(pd.to_datetime(df["date"].dt.strftime("%Y-%m-%d")))
    keep = ["date", "open", "high", "low", "close", "adj_close", "volume", "dividends", "splits"]
    for c in keep:
        if c not in df:
            df[c] = 0.0
    return df[keep]


def update(ticker: str, full: bool) -> None:
    path = etf_daily_path(ticker)
    if path.exists() and not full:
        old = pd.read_parquet(path, columns=["date"])
        start = (old.date.max() - timedelta(days=7)).strftime("%Y-%m-%d")
        tail = normalise(history(ticker, start=start, interval="1d", auto_adjust=False, actions=True))
        new_tail = tail[tail.date > old.date.max()]
        if ((new_tail.dividends != 0) | (new_tail.splits != 0)).any():
            log.info("%s: new dividend/split in tail -> full refresh (Adj Close changes)", ticker)
            return update(ticker, full=True)
        added = merge_write(path, tail, "date")
        log.info("%s: tail from %s, %d new rows", ticker, start, added)
        return
    df = normalise(history(ticker, period="max", interval="1d", auto_adjust=False, actions=True))
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    merge_write(path, df, "date")
    log.info("%s: full history %s -> %s, %d rows", ticker, df.date.min().date(), df.date.max().date(), len(df))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", nargs="*", default=load_config()["etf"])
    ap.add_argument("--full", action="store_true", help="re-download full history")
    args = ap.parse_args()
    errors = 0
    for i, t in enumerate(args.tickers):
        if i:
            time.sleep(SLEEP_BETWEEN)
        try:
            update(t, args.full)
        except Exception:
            errors += 1
            log.exception("%s failed", t)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
