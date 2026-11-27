# EUR/USD London breakout (baseline run)

Source: `eurusd_breakout.md` (user):
> Mark the high and low of the Asian session (00:00-07:00 UTC) on EURUSD 15 minute candles.
> Buy when price breaks above the Asian high during London hours, stop below the Asian low,
> take profit at 2x the range. Close everything at 16:00 UTC.

## Data (the repo had none for EURUSD)

The pipeline collects crypto, ETFs and stocks only. Yahoo `EURUSD=X` has 15m bars for just 60 days
and 1h bars for ~2 years, and Dukascopy returned 429/503. So 1-minute EURUSD bid bars
2010-01 .. 2026-11-13 were downloaded from HistData.com into `data/raw/` (yearly/monthly zips).

Timezone: HistData says "EST without DST", but the US payrolls spike sits at 08:30 in the raw
files all year round, and hourly returns line up with Yahoo (corr 0.97) only if the raw clock is read
as New York local time. In the weeks when US and EU DST disagree, the files follow different rules in
different years, so those days (~17 a year) are excluded. Days with <80 % minute coverage in the
Asian or London window are excluded too (114 of them in 2023, when HistData lost about half the
minutes after 10:00 UTC from February to July). `data/data_quality.json` has the details.

## Rules as implemented (`strategy.py`)

| point | spec | default used | tuned in grid |
|---|---|---|---|
| Asian range | 00:00-07:00 UTC | high/low of those bars | - |
| "London hours" | not defined | entries 07:00-16:00 UTC | start 7/8, end 9/11/13/16 |
| "breaks above" | not defined | stop order at the high (`touch`, 1m fills) | or 15m close above (`close15`); buffer 0/3 pips |
| stop | below Asian low | at Asian low | or mid-range (`stop_frac` 0.5) |
| take profit | 2x range | entry + 2x range | 0 (none)/1/2/3x |
| exit | 16:00 UTC | 16:00 | 11/13/16 |
| direction | buy only | long | long/short/both |
| range filter | none | none | min 0/15 pips, max none/50 pips |

One trade per day. Stop and TP in the same minute count as the stop. Gaps fill at the worse price. Costs are 1.0 pip
per round trip (stress-tested at 0.5 and 2.0). R = pnl / initial risk. Sharpe uses 1 % risk per trade.

## Method

`prep_data.py` builds the bars. `optimize.py` runs a grid of 9,216 combos (6,912 with ≥300 in-sample trades)
and ranks them on **2010-2019 in-sample Sharpe** only. The top 40 are checked on 2020-2023 validation.
`analyze.py` runs the final picks once on the **2024-2026 holdout**, adds cost stress and drift benchmarks
(trade every day without the breakout), and writes `results/report.md` and `results/final.json`.
The whole run takes about 10 minutes, so it did not need to run overnight.

## Result in one line

The strategy as written loses money (2010-2026 profit factor 0.92, Sharpe -0.56, t = -2.2).
No variant had an edge that held up across in-sample, validation and holdout. See `results/report.md`.

Re-run: `docker run --rm -u $(id -u):$(id -g) -v $PWD:/w -w /w --entrypoint python trading-pipeline:latest <script>.py`
from this folder (prep_data -> optimize -> analyze). Delete `data/days.npz` after changing the data.
