"""Print coverage per symbol: first/last timestamp, rows, gaps > 1 minute, size on disk.

Crypto gaps are counted 24/7. ETF 1m gaps are counted only within a trading
session (consecutive bars on the same day), so nights/weekends/holidays don't count.
"""
from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from src.common.storage import (
    CRYPTO_1M, ETF_1M, count_gaps, dir_size, etf_daily_path, load_config, read_crypto, read_etf_1m, safe_ticker,
)


def mb(n: int) -> str:
    return f"{n / 1e6:.1f} MB"


def fmt(ts) -> str:
    return "-" if ts is None or pd.isna(ts) else pd.Timestamp(ts).strftime("%Y-%m-%d %H:%M")


def table(title: str, header: list[str], rows: list[list]) -> None:
    print(f"\n== {title} ==")
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)] if rows else [len(h) for h in header]
    for r in [header, *rows]:
        print("  ".join(str(x).ljust(w) for x, w in zip(r, widths)))


def main() -> None:
    cfg = load_config()
    now = datetime.now(timezone.utc)
    print(f"Data check at {now:%Y-%m-%d %H:%M} UTC")

    rows = []
    for s in cfg["crypto"]:
        df = read_crypto(s)
        if df.empty:
            rows.append([s, "-", "-", 0, "-", "-", "-", "0.0 MB"])
            continue
        n_gaps, missing = count_gaps(df.open_time)
        lag = now - df.open_time.max().to_pydatetime()
        rows.append([s, fmt(df.open_time.min()), fmt(df.open_time.max()), f"{len(df):,}", n_gaps, f"{missing:,}",
                     f"{lag.total_seconds() / 60:.0f} min", mb(dir_size(CRYPTO_1M / f"symbol={s}"))])
    table("Crypto 1m (gaps counted 24/7)", ["symbol", "first", "last", "rows", "gaps", "missing bars", "lag", "size"], rows)

    rows = []
    for t in cfg["etf"]:
        p = etf_daily_path(t)
        if not p.exists():
            rows.append([t, "-", "-", 0, "-"])
            continue
        df = pd.read_parquet(p)
        rows.append([t, fmt(df.date.min())[:10], fmt(df.date.max())[:10], f"{len(df):,}", mb(p.stat().st_size)])
    table("ETF / index daily", ["ticker", "first", "last", "rows", "size"], rows)

    rows = []
    for t in cfg["etf"]:
        df = read_etf_1m(t)
        if df.empty:
            rows.append([t, "-", "-", 0, 0, "-", "-", "0.0 MB"])
            continue
        days = df.timestamp.dt.date
        n_gaps = missing = 0
        for _, g in df.groupby(days):
            a, b = count_gaps(g.timestamp)
            n_gaps += a
            missing += b
        rows.append([t, fmt(df.timestamp.min()), fmt(df.timestamp.max()), f"{len(df):,}", days.nunique(), n_gaps,
                     f"{missing:,}", mb(dir_size(ETF_1M / f"ticker={safe_ticker(t)}"))])
    table("ETF / index 1m (gaps counted within sessions)",
          ["ticker", "first", "last", "rows", "days", "gaps", "missing bars", "size"], rows)


if __name__ == "__main__":
    main()
