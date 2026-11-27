# nr7_breakout: optimization summary

Updated 2026-11-25T07:17:21Z · backtest.py version `e4696ff4fd` · 18,590 parameter sets tested with this version (18,590 rows in results.csv in total) · last run ended: see base optimization.log

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

49 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | LQD | 100% | 0.8 | 1.5 | 5.4 | 0.3 | -1.3 | 0 |
| 2 | TQQQ | 98% | 5.3 | 14.3 | 58.3 | 2.4 | -10.7 | 0 |
| 3 | MTUM | 87% | 2.8 | 5.0 | 15.5 | 2.0 | -3.1 | 0 |
| 4 | VT | 87% | 0.7 | 3.0 | 11.4 | 0.6 | -2.9 | 0 |
| 5 | VEA | 85% | 1.6 | 3.4 | -0.3 | 1.3 | -3.9 | 0 |
| 6 | EEM | 74% | 0.6 | 2.3 | 7.9 | -0.1 | -3.6 | 0 |
| 7 | SCHD | 70% | 0.7 | 2.4 | 12.3 | -0.4 | -0.4 | 0 |
| 8 | VUG | 66% | 0.8 | 2.2 | 8.1 | -0.2 | -0.7 | 4 |
| 9 | USMV | 64% | 0.2 | 1.9 | 13.5 | 0.1 | 1.0 | 18 |
| 10 | VWO | 54% | 0.1 | 3.2 | 4.5 | 0.7 | -4.1 | 0 |
| 11 | EFA | 52% | 0.1 | 1.3 | 5.8 | -0.6 | -3.5 | 0 |
| 12 | XLU | 51% | 0.0 | 2.3 | 6.0 | -0.7 | -0.7 | 1 |
| 13 | RSP | 49% | -0.0 | 1.4 | 9.4 | -1.0 | -1.4 | 0 |
| 14 | SMH | 41% | -0.1 | 1.8 | -0.3 | 0.8 | -3.7 | 0 |
| 15 | QQQ | 38% | -0.2 | 2.1 | 4.8 | -0.8 | -3.8 | 0 |
| 16 | SLV | 38% | -1.2 | 4.3 | 2.0 | -4.8 | -3.3 | 13 |
| 17 | HYG | 36% | -0.5 | 3.7 | 4.8 | 0.4 | -0.6 | 0 |
| 18 | VXUS | 34% | -0.5 | 3.1 | 1.2 | -1.4 | -3.8 | 0 |
| 19 | USO | 33% | -1.1 | 3.1 | -17.2 | -2.4 | -5.9 | 3 |
| 20 | ACWI | 26% | -1.1 | 0.9 | 4.7 | -1.3 | -3.3 | 0 |
| 21 | XLK | 23% | -2.5 | 0.9 | 1.8 | -3.6 | -1.3 | 0 |
| 22 | QUAL | 18% | 1.5 | 2.3 | 9.0 | 1.1 | -1.8 | 0 |
| 23 | IWM | 15% | -0.8 | 0.7 | 7.5 | -1.3 | -1.7 | 0 |
| 24 | BND | 8% | -0.5 | 0.1 | 4.3 | -1.0 | -1.7 | 0 |
| 25 | VOO | 7% | -2.6 | 0.4 | 11.9 | -3.0 | -1.2 | 0 |
| 26 | TIP | 5% | -0.5 | 0.1 | 4.2 | -0.5 | -1.4 | 0 |
| 27 | XLP | 5% | -0.7 | 0.4 | 6.4 | -1.5 | -0.8 | 0 |
| 28 | XLV | 5% | -1.4 | 0.2 | 7.1 | -3.6 | -1.9 | 0 |
| 29 | VIG | 3% | -2.4 | 0.1 | 7.0 | -3.0 | -0.7 | 0 |
| 30 | VTI | 2% | -1.1 | 0.1 | 7.3 | -2.1 | -1.1 | 0 |
| 31 | SOXX | 2% | -1.3 | 0.2 | 2.2 | -1.8 | -4.1 | 0 |
| 32 | VTV | 2% | -1.3 | 0.2 | 7.2 | -1.4 | 0.5 | 0 |
| 33 | AGG | 0% | -0.7 | n/a | 4.0 | -0.9 | -1.8 | 0 |
| 34 | SHY | 0% | -1.4 | n/a | 2.1 | -1.7 | -1.9 | 0 |
| 35 | DIA | 0% | -1.6 | n/a | 6.2 | -1.9 | -1.1 | 0 |
| 36 | DBC | 0% | -2.0 | n/a | -5.7 | -2.4 | -1.1 | 0 |
| 37 | IEF | 0% | -2.0 | n/a | 5.2 | -1.6 | -1.9 | 0 |
| 38 | GLD | 0% | -2.2 | n/a | 8.5 | -2.0 | -0.3 | 0 |
| 39 | SPY | 0% | -2.2 | n/a | 9.3 | -3.5 | -1.3 | 0 |
| 40 | IVV | 0% | -2.2 | n/a | 4.6 | -2.7 | -1.6 | 0 |

(9 more in screen.csv)

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

Searching 18,590 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
