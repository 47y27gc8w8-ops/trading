"""Build EURUSD 15-minute UTC bars from the HistData.com 1-minute files in data/raw.

HistData ASCII M1: "YYYYMMDD HHMMSS;open;high;low;close;vol", BID prices.
HistData documents the timestamps as "EST without DST" (fixed UTC-5), but checks
against scheduled releases show otherwise: the US payrolls spike sits at 08:30
in the raw files in summer *and* winter, so outside the DST changeover weeks the
raw clock is New York local time (UTC-4 summer / UTC-5 winter).  Inside the
weeks where US and EU DST disagree (mid-March, late Oct/early Nov) the raw clock
follows different rules in different years (FOMC at raw 13:00 vs 14:00), so
those days are flagged `dst_ambiguous` and excluded from the backtest.

Outputs
  data/eurusd_m1.parquet   1-minute UTC bars (all years)
  data/eurusd_m15.parquet  15-minute UTC bars (label = bar start), n_min = minutes present
  data/data_quality.json   coverage report per year + list of weekdays with thin Asian/London data
"""
from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
RAW = HERE / "data" / "raw"


def read_zip(p: Path) -> pd.DataFrame:
    z = zipfile.ZipFile(p)
    name = next(n for n in z.namelist() if n.endswith(".csv"))
    df = pd.read_csv(io.BytesIO(z.read(name)), sep=";", header=None,
                     names=["ts", "open", "high", "low", "close", "vol"])
    ts = pd.to_datetime(df["ts"], format="%Y%m%d %H%M%S")
    df["ts"] = ts.dt.tz_localize("America/New_York", ambiguous="NaT",
                                 nonexistent="NaT").dt.tz_convert("UTC")
    df = df.dropna(subset=["ts"])
    return df.drop(columns="vol")


def dst_ambiguous(day: pd.Timestamp) -> bool:
    """True when US (New York) and EU (London) DST status differ on this date."""
    d = pd.Timestamp(day.date()) + pd.Timedelta(hours=12)
    ny = d.tz_localize("America/New_York").utcoffset() == pd.Timedelta(hours=-4)
    ld = d.tz_localize("Europe/London").utcoffset() == pd.Timedelta(hours=1)
    return bool(ny != ld)


def main() -> None:
    m1 = pd.concat([read_zip(p) for p in sorted(RAW.glob("*.zip"))], ignore_index=True)
    m1 = m1.drop_duplicates("ts").sort_values("ts").set_index("ts")
    m1.to_parquet(HERE / "data" / "eurusd_m1.parquet")

    agg = {"open": "first", "high": "max", "low": "min", "close": "last"}
    m15 = m1.resample("15min", label="left", closed="left").agg(agg)
    m15["n_min"] = m1["close"].resample("15min", label="left", closed="left").count()
    m15 = m15.dropna(subset=["close"])
    m15.to_parquet(HERE / "data" / "eurusd_m15.parquet")

    # quality: minutes present per weekday session window
    wk = m1[m1.index.day_of_week < 5]
    day = wk.index.normalize()
    hour = wk.index.hour
    asia = wk[(hour < 7)].groupby(day[hour < 7]).size()          # max 420
    london = wk[(hour >= 7) & (hour < 16)].groupby(day[(hour >= 7) & (hour < 16)]).size()  # max 540
    days = pd.DataFrame({"asia_min": asia, "london_min": london}).fillna(0)
    days["year"] = days.index.year
    days["dst_ambiguous"] = [dst_ambiguous(d) for d in days.index]
    rep = {
        "source": "histdata.com ASCII M1 EURUSD (bid); raw clock treated as America/New_York -> UTC",
        "first_bar": str(m1.index.min()), "last_bar": str(m1.index.max()),
        "n_minutes": int(len(m1)),
        "per_year": {
            int(y): {"weekdays": int(len(g)),
                      "asia_cov": round(float(g.asia_min.sum() / (420 * len(g))), 3),
                      "london_cov": round(float(g.london_min.sum() / (540 * len(g))), 3),
                      "days_asia_lt_80pct": int((g.asia_min < 336).sum()),
                      "days_london_lt_80pct": int((g.london_min < 432).sum())}
            for y, g in days.groupby("year")},
        "thin_days": [str(d.date()) for d in days.index[(days.asia_min < 336) | (days.london_min < 432)]],
        "dst_ambiguous_days": [str(d.date()) for d in days.index[days.dst_ambiguous]],
    }
    (HERE / "data" / "data_quality.json").write_text(json.dumps(rep, indent=1))
    days.to_parquet(HERE / "data" / "day_quality.parquet")
    print(json.dumps(rep["per_year"]))
    print("thin days:", len(rep["thin_days"]), "dst-ambiguous days:", len(rep["dst_ambiguous_days"]))


if __name__ == "__main__":
    main()
