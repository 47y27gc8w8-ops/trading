#!/usr/bin/env python3
"""Download 5-minute US stock/ETF bars from Alpaca's market-data API (free plan: SIP bars older than
15 minutes, history from 2016) into data/etf/5m/<SYMBOL>.parquet, regular session only.

Keys come from the environment (ALPACA_KEY_ID, ALPACA_SECRET_KEY), e.g.

    docker run --rm --env-file /home/luca/trading/.env -v /home/luca/trading/data:/app/data \
      -v $PWD/scripts:/opt/s:ro -w /app trading-pipeline:latest python /opt/s/fetch_alpaca_5m.py SPY QQQ

Bars: adjustment=all (split + dividend adjusted, like the Yahoo daily series), feed=sip.
Timestamps are kept as the bar START in UTC (column "date"); the backtests label by close.
Only bars starting 09:30 <= t < 16:00 America/New_York are kept (half days end earlier by themselves).
Resumable: an existing file is extended from its last bar.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

OUT = Path("/app/data/etf/5m")
URL = "https://data.alpaca.markets/v2/stocks/{sym}/bars"
START = "2016-01-01T00:00:00Z"


def get(sym: str, params: dict) -> dict:
    req = urllib.request.Request(URL.format(sym=sym) + "?" + urllib.parse.urlencode(params), headers={
        "APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"],
        "Accept": "application/json", "User-Agent": "trading-research/1.0"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(2 ** attempt)
                continue
            raise SystemExit(f"{sym}: HTTP {e.code} {e.read()[:300]!r}")
        except (urllib.error.URLError, TimeoutError):
            time.sleep(2 ** attempt)
    raise SystemExit(f"{sym}: giving up after retries")


def fetch(sym: str) -> None:
    f = OUT / f"{sym}.parquet"
    old = pd.read_parquet(f) if f.exists() else None
    start = START if old is None else (old["date"].max() + pd.Timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = (pd.Timestamp.now(tz="UTC") - pd.Timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%SZ")
    rows, token, pages = [], None, 0
    while True:
        params = {"timeframe": "5Min", "start": start, "end": end, "limit": 10000,
                  "adjustment": "all", "feed": "sip", "sort": "asc"}
        if token:
            params["page_token"] = token
        d = get(sym, params)
        rows += d.get("bars") or []
        pages += 1
        token = d.get("next_page_token")
        if not token:
            break
        time.sleep(0.35)                     # free plan: 200 requests/minute
    if not rows:
        print(f"{sym}: no new bars", flush=True)
        return
    df = pd.DataFrame(rows).rename(columns={"t": "date", "o": "open", "h": "high", "l": "low", "c": "close",
                                            "v": "volume", "n": "trades", "vw": "bar_vwap"})
    df["date"] = pd.to_datetime(df["date"], utc=True)
    local = df["date"].dt.tz_convert("America/New_York")
    mins = local.dt.hour * 60 + local.dt.minute
    df = df[(mins >= 570) & (mins < 960)]
    df = df[["date", "open", "high", "low", "close", "volume", "trades", "bar_vwap"]]
    if old is not None:
        df = pd.concat([old, df]).drop_duplicates("date", keep="last")
    df = df.sort_values("date").reset_index(drop=True)
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = f.with_suffix(".tmp")
    df.to_parquet(tmp, index=False)
    tmp.replace(f)
    print(f"{sym}: {pages} pages, {len(df)} regular-session bars {df['date'].min()} -> {df['date'].max()}", flush=True)


if __name__ == "__main__":
    for s in sys.argv[1:] or ["SPY", "QQQ", "IWM", "AAPL", "MSFT", "NVDA"]:
        fetch(s)
