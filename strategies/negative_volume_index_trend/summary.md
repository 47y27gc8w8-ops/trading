# negative_volume_index_trend: optimization summary

Updated 2026-11-25T06:00:03Z · backtest.py version `ddb1343918` · 35,491 parameter sets tested with this version (35,491 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

39 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLI | 64% | 0.2 | 1.8 | 7.3 | 0.8 | 0.0 | 0 |
| 2 | XLV | 62% | 0.1 | 1.3 | 10.3 | 0.3 | 1.3 | 23 |
| 3 | XLU | 44% | 0.1 | 2.1 | 8.4 | -0.8 | 0.2 | 11 |
| 4 | IEF | 43% | 0.3 | 1.6 | 5.1 | 0.5 | -0.4 | 0 |
| 5 | XLK | 38% | -0.3 | 2.9 | 8.2 | -1.1 | 0.0 | 0 |
| 6 | TLT | 34% | 0.3 | 3.2 | 7.0 | -0.1 | 0.0 | 0 |
| 7 | XLY | 26% | -0.1 | 2.3 | 9.2 | -0.8 | 0.0 | 0 |
| 8 | VTV | 23% | 0.8 | 2.4 | 11.7 | 0.8 | 0.0 | 2 |
| 9 | LQD | 21% | 0.0 | 1.6 | 6.2 | -0.5 | -0.2 | 0 |
| 10 | XLF | 20% | -0.2 | 3.1 | 0.2 | -0.3 | 1.0 | 7 |
| 11 | XLP | 16% | 0.0 | 1.4 | 10.3 | -0.2 | 0.9 | 7 |
| 12 | IWM | 13% | 0.1 | 1.0 | 6.2 | 0.3 | 0.0 | 0 |
| 13 | SMH | 7% | -1.3 | 0.6 | 5.6 | -2.0 | 0.6 | 2 |
| 14 | IVV | 5% | 0.4 | 0.4 | 6.8 | 0.3 | 0.4 | 0 |
| 15 | XLE | 5% | 0.2 | 1.8 | 6.7 | 0.0 | -0.4 | 0 |
| 16 | AGG | 3% | -0.1 | 0.1 | 3.6 | -0.0 | -0.1 | 0 |
| 17 | SHY | 3% | -0.3 | 0.2 | 1.3 | -0.2 | -0.4 | 0 |
| 18 | SOXX | 3% | -3.6 | 0.8 | 4.6 | -4.0 | 0.2 | 0 |
| 19 | DBC | 2% | 0.1 | 0.4 | -16.6 | 1.0 | 0.4 | 1 |
| 20 | DIA | 0% | 0.6 | n/a | 6.8 | 0.8 | 0.0 | 0 |
| 21 | RSP | 0% | 0.5 | n/a | 18.0 | -0.8 | -0.4 | 0 |
| 22 | QQQ | 0% | 0.3 | n/a | 11.5 | 0.1 | 0.6 | 0 |
| 23 | EFA | 0% | 0.1 | n/a | 0.3 | -0.8 | 0.0 | 0 |
| 24 | SPY | 0% | 0.0 | n/a | 4.7 | -0.2 | 0.0 | 0 |
| 25 | VTI | 0% | 0.0 | n/a | 6.0 | 0.0 | 0.0 | 0 |
| 26 | VEA | 0% | 0.0 | n/a | 2.5 | 0.0 | 0.8 | 0 |
| 27 | EEM | 0% | 0.0 | n/a | 6.2 | 0.0 | 0.1 | 0 |
| 28 | HYG | 0% | 0.0 | n/a | 0.1 | 0.0 | 0.2 | 0 |
| 29 | USO | 0% | 0.0 | n/a | -29.1 | 0.0 | -1.7 | 0 |
| 30 | VIG | 0% | 0.0 | n/a | 10.9 | 0.0 | 0.0 | 0 |
| 31 | VNQ | 0% | 0.0 | n/a | 12.4 | 0.0 | -0.4 | 0 |
| 32 | VUG | 0% | 0.0 | n/a | 13.4 | 0.0 | 0.0 | 0 |
| 33 | TIP | 0% | -0.1 | n/a | 2.7 | -0.1 | -0.3 | 0 |
| 34 | SLV | 0% | -0.3 | n/a | -20.3 | 0.0 | -2.1 | 0 |
| 35 | XLB | 0% | -0.3 | n/a | 6.3 | -1.3 | 0.0 | 0 |
| 36 | BND | 0% | -0.5 | n/a | 1.6 | -0.6 | -0.7 | 0 |
| 37 | VWO | 0% | -0.6 | n/a | -4.0 | -1.2 | 0.0 | 0 |
| 38 | GLD | 0% | -0.6 | n/a | -5.0 | -1.0 | 0.8 | 0 |
| 39 | GDX | 0% | -1.3 | n/a | -26.5 | 0.0 | 2.0 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [negative_volume_index_trend__broad__max-income__v002.md](symbols/broad/negative_volume_index_trend__broad__max-income__v002.md) | 1.1 | 2.0 | 1.1 | -5.8 | 39.4 | 911/1249 |
| broad | balanced | [negative_volume_index_trend__broad__balanced__v001.md](symbols/broad/negative_volume_index_trend__broad__balanced__v001.md) | 0.2 | 0.4 | 0.2 | -3.7 | 47.1 | 911/1249 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 35,491 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
