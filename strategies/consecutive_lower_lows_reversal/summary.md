# consecutive_lower_lows_reversal: optimization summary

Updated 2026-11-25T15:07:13Z · backtest.py version `bd39259938` · 5,200 parameter sets tested with this version (5,200 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

468 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | WMB | 100% | 4.0 | 6.1 | 9.7 | 5.8 | -0.5 | 28 |
| 2 | KLAC | 100% | 3.8 | 10.4 | 11.1 | 2.3 | 1.8 | 43 |
| 3 | OMC | 100% | 2.4 | 4.0 | 14.2 | 2.1 | 0.5 | 21 |
| 4 | ROP | 98% | 2.4 | 6.7 | 18.5 | 3.5 | -0.7 | 1 |
| 5 | ITW | 98% | 1.4 | 3.7 | 12.8 | 1.1 | 2.0 | 18 |
| 6 | FISV | 98% | 1.3 | 3.4 | 17.2 | 1.0 | 0.2 | 20 |
| 7 | CB | 97% | 1.4 | 3.0 | 16.0 | 2.1 | -0.7 | 19 |
| 8 | MCK | 97% | 1.0 | 3.8 | 11.6 | 1.3 | 2.1 | 37 |
| 9 | HON | 97% | 0.8 | 2.5 | 11.3 | 0.6 | -1.3 | 34 |
| 10 | AMAT | 95% | 2.5 | 4.7 | 10.9 | 2.6 | 0.8 | 31 |
| 11 | CSCO | 95% | 1.8 | 6.7 | 14.0 | 1.7 | -0.8 | 9 |
| 12 | PCG | 95% | 1.4 | 2.4 | 7.6 | 1.4 | 0.1 | 52 |
| 13 | HD | 92% | 2.2 | 4.3 | 14.7 | 2.6 | -0.9 | 0 |
| 14 | HUBB | 92% | 1.0 | 3.4 | 10.2 | 3.4 | 1.2 | 25 |
| 15 | TFC | 92% | 0.6 | 1.9 | 10.4 | 0.8 | -1.8 | 11 |
| 16 | NESN.SW | 90% | 0.9 | 2.2 | 10.9 | 1.2 | -3.4 | 5 |
| 17 | APH | 84% | 1.2 | 2.6 | 18.7 | 1.6 | 1.6 | 28 |
| 18 | EG | 82% | 1.1 | 3.9 | 12.2 | 1.0 | -1.0 | 14 |
| 19 | RJF | 80% | 1.9 | 4.2 | 17.2 | -0.0 | -0.5 | 0 |
| 20 | LIN | 80% | 1.7 | 5.0 | 13.5 | 1.9 | 2.3 | 45 |
| 21 | NVO | 80% | 0.9 | 5.7 | 23.4 | 1.0 | 2.9 | 47 |
| 22 | GPC | 80% | 0.6 | 1.6 | 9.9 | 1.2 | 1.6 | 38 |
| 23 | WRB | 80% | 0.6 | 2.1 | 13.7 | 1.2 | 1.9 | 39 |
| 24 | REG | 80% | 0.5 | 2.9 | 13.3 | 0.0 | -1.6 | 0 |
| 25 | PCAR | 79% | 0.9 | 3.3 | 15.9 | 1.3 | -3.3 | 0 |
| 26 | CAH | 79% | 0.4 | 1.2 | 12.1 | -0.0 | 0.0 | 3 |
| 27 | EFX | 77% | 0.7 | 3.8 | 15.2 | 1.1 | -0.8 | 14 |
| 28 | CCL | 75% | 1.2 | 2.9 | 10.3 | 1.8 | 2.2 | 11 |
| 29 | HSIC | 75% | 0.8 | 3.6 | 11.6 | 1.2 | 1.7 | 24 |
| 30 | D | 75% | 0.5 | 1.3 | 11.6 | 1.3 | 0.5 | 42 |
| 31 | DUK | 74% | 1.2 | 3.8 | 8.7 | 1.9 | -0.5 | 7 |
| 32 | MRSH | 74% | 0.4 | 1.5 | 10.0 | 0.0 | 0.2 | 11 |
| 33 | EXR | 72% | 3.8 | 8.8 | 24.0 | 5.6 | -0.8 | 0 |
| 34 | EXPE | 72% | 3.6 | 11.6 | 22.7 | 4.4 | 0.3 | 5 |
| 35 | WAT | 72% | 3.3 | 6.7 | 16.9 | 3.5 | -0.7 | 1 |
| 36 | ODFL | 72% | 3.2 | 7.3 | 17.2 | 5.7 | 1.1 | 22 |
| 37 | TER | 72% | 2.9 | 5.4 | 4.5 | 3.7 | -2.2 | 1 |
| 38 | JBL | 72% | 2.9 | 6.4 | 20.7 | 4.1 | -1.5 | 0 |
| 39 | GLW | 72% | 2.6 | 4.6 | 5.0 | 3.0 | 5.8 | 34 |
| 40 | ALGN | 72% | 2.5 | 4.4 | 21.6 | 2.8 | 8.4 | 41 |

(428 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [consecutive_lower_lows_reversal__broad__max-income__v002.md](symbols/broad/consecutive_lower_lows_reversal__broad__max-income__v002.md) | 2.8 | 2.0 | 2.0 | -12.2 | 73.3 | 57821/34550 |
| broad | balanced | [consecutive_lower_lows_reversal__broad__balanced__v002.md](symbols/broad/consecutive_lower_lows_reversal__broad__balanced__v002.md) | 2.1 | 1.2 | 1.2 | -10.5 | 73.6 | 41954/24826 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 5,200 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
