"""Collect Yahoo 1m bars (Yahoo only serves ~last 30 days, max ~7 days per request).

Run daily after the US close (~22:30 UTC). Each run fetches the last 7 days,
so a failed run is filled by the next one. The first run for a ticker fetches
the full ~30 day window in 7-day chunks. Raises an ALERT in the log if there
has been no successful run for more than 5 days.
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timedelta, timezone

import pandas as pd

from src.common.storage import ETF_1M, LOGS, load_config, safe_ticker, setup_logging, write_etf_1m
from src.common.yahoo import PERMANENT, NoData, history, utc

log = setup_logging("yahoo_intraday")
STATUS = LOGS / "yahoo_intraday_status.json"
ALERT_DAYS = 5
SLEEP_BETWEEN = 3


def normalise(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={"datetime": "timestamp"})
    df["timestamp"] = utc(df["timestamp"])
    return df[["timestamp", "open", "high", "low", "close", "volume"]]


def fetch_ticker(ticker: str) -> int:
    first_run = not (ETF_1M / f"ticker={safe_ticker(ticker)}").exists()
    frames = []
    if first_run:
        now = datetime.now(timezone.utc)
        start = now - timedelta(days=29)  # Yahoo rejects 1m requests starting >30 days back
        while start < now:
            end = min(start + timedelta(days=7), now)
            try:
                frames.append(normalise(history(ticker, start=start, end=end, interval="1m", prepost=False)))
            except PERMANENT:
                log.info("%s: no 1m data %s..%s", ticker, start.date(), end.date())
            start = end
            time.sleep(1)
    else:
        frames.append(normalise(history(ticker, period="7d", interval="1m", prepost=False)))
    df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    if df.empty:
        raise NoData(f"{ticker}: no 1m data")
    added = write_etf_1m(ticker, df)
    log.info("%s: %d bars %s -> %s, %d new%s", ticker, len(df), df.timestamp.min(), df.timestamp.max(),
             added, " (first run, 30d)" if first_run else "")
    return added


def load_status() -> dict:
    return json.loads(STATUS.read_text()) if STATUS.exists() else {}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", nargs="*", default=load_config()["etf"])
    args = ap.parse_args()
    status = load_status()
    now = datetime.now(timezone.utc)
    failed = []
    for i, t in enumerate(args.tickers):
        if i:
            time.sleep(SLEEP_BETWEEN)
        try:
            fetch_ticker(t)
            status.setdefault(t, {})["last_success"] = now.isoformat()
        except Exception:
            failed.append(t)
            log.exception("%s failed", t)
        last = status.get(t, {}).get("last_success")
        if last is None or now - datetime.fromisoformat(last) > timedelta(days=ALERT_DAYS):
            log.error("ALERT: %s has had no successful 1m collection for more than %d days (last: %s). "
                      "Yahoo only keeps ~30 days of 1m data - bars are being lost.", t, ALERT_DAYS, last)
    status["_last_run"] = {"time": now.isoformat(), "failed": failed}
    STATUS.write_text(json.dumps(status, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
