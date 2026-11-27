# pre_holiday_trend_entry: optimization summary

Updated 2026-11-25T10:08:28Z · backtest.py version `dbfcc74235` · 2,730 parameter sets tested with this version (2,730 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

47 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TQQQ | 100% | 5.1 | 5.5 | 46.3 | 5.1 | -0.7 | 0 |
| 2 | GLD | 100% | 1.7 | 2.0 | 5.6 | 1.8 | 0.8 | 53 |
| 3 | XLE | 100% | 1.1 | 1.6 | 6.1 | 1.3 | 0.5 | 58 |
| 4 | ACWI | 100% | 0.8 | 1.2 | 8.8 | 0.9 | -0.5 | 0 |
| 5 | SLV | 100% | 0.7 | 2.3 | 0.2 | 0.6 | 3.5 | 61 |
| 6 | SCHD | 100% | 0.6 | 0.7 | 10.9 | 0.6 | -0.6 | 0 |
| 7 | VUG | 100% | 0.5 | 0.9 | 8.5 | 0.5 | -0.9 | 0 |
| 8 | XLB | 100% | 0.4 | 0.6 | 6.6 | 0.5 | -0.7 | 0 |
| 9 | SOXX | 100% | 0.3 | 0.5 | 7.3 | 0.3 | 0.1 | 32 |
| 10 | SMH | 100% | 0.3 | 0.7 | 2.9 | 0.5 | 0.8 | 61 |
| 11 | EFA | 97% | 0.3 | 0.7 | 7.3 | 0.1 | -0.3 | 3 |
| 12 | VTI | 95% | 0.3 | 0.5 | 9.2 | 0.4 | -0.7 | 0 |
| 13 | VIG | 93% | 0.6 | 0.8 | 5.9 | 0.7 | -0.9 | 0 |
| 14 | VOO | 89% | 1.2 | 1.2 | 14.3 | 1.2 | -0.8 | 0 |
| 15 | VTV | 89% | 0.2 | 0.3 | 6.5 | 0.1 | -0.5 | 0 |
| 16 | VEA | 85% | 0.3 | 0.9 | 8.0 | 0.3 | -0.1 | 5 |
| 17 | VXUS | 82% | 2.1 | 3.5 | 5.9 | 1.9 | -0.3 | 1 |
| 18 | RSP | 69% | 0.1 | 0.4 | 8.8 | -0.1 | -0.8 | 0 |
| 19 | VWO | 66% | 0.1 | 0.6 | 2.6 | 0.1 | -0.0 | 18 |
| 20 | VT | 64% | 0.1 | 0.4 | 7.4 | 0.2 | -0.4 | 0 |
| 21 | EEM | 61% | 0.1 | 0.5 | 7.2 | 0.1 | 0.3 | 36 |
| 22 | IVV | 56% | 0.0 | 0.2 | 6.6 | 0.1 | -0.8 | 0 |
| 23 | QQQ | 49% | -0.0 | 0.3 | 1.8 | -0.3 | -1.0 | 0 |
| 24 | USO | 34% | -0.3 | 1.5 | -17.6 | 0.3 | 0.8 | 21 |
| 25 | XLY | 33% | -0.1 | 0.2 | 7.9 | -0.1 | -0.9 | 0 |
| 26 | IWM | 31% | -0.1 | 0.1 | 8.6 | -0.0 | -1.0 | 0 |
| 27 | USMV | 25% | -0.2 | 0.2 | 12.5 | -0.2 | -0.7 | 0 |
| 28 | VNQ | 13% | -0.2 | 0.2 | 6.8 | 0.1 | -0.0 | 5 |
| 29 | GDX | 8% | -0.4 | 0.7 | -13.3 | -0.0 | 3.0 | 5 |
| 30 | DBC | 8% | -0.9 | 0.3 | -7.0 | -0.5 | 0.6 | 5 |
| 31 | SQQQ | 0% | 0.0 | n/a | -49.3 | 0.0 | -0.1 | 0 |
| 32 | XLI | 0% | -0.3 | n/a | 5.6 | -0.6 | -0.8 | 0 |
| 33 | XLK | 0% | -0.5 | n/a | 0.1 | -0.6 | -1.1 | 0 |
| 34 | XLF | 0% | -0.5 | n/a | 2.2 | -0.7 | -0.2 | 0 |
| 35 | SPY | 0% | -0.5 | n/a | 9.3 | -0.5 | -0.8 | 0 |
| 36 | DIA | 0% | -0.5 | n/a | 5.3 | -0.7 | -1.2 | 0 |
| 37 | XLV | 0% | -0.6 | n/a | 7.5 | -0.5 | -1.2 | 0 |
| 38 | TIP | 0% | -0.8 | n/a | 3.7 | -0.8 | -1.0 | 0 |
| 39 | TLT | 0% | -0.9 | n/a | 6.8 | -0.8 | -1.2 | 0 |
| 40 | HYG | 0% | -1.0 | n/a | 5.7 | -0.8 | -0.9 | 0 |

(7 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 2,730 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
