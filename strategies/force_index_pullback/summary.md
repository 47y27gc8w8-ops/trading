# force_index_pullback: optimization summary

Updated 2026-11-26T02:02:44Z · backtest.py version `e0455f173e` · 9,884 parameter sets tested with this version (9,884 rows in results.csv in total) · last run ended: see base optimization.log

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

65 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 89% | 1.6 | 3.2 | 4.8 | 0.2 | -4.3 | 0 |
| 2 | ^IXIC | 75% | 1.1 | 3.2 | 9.5 | -0.1 | 0.9 | 22 |
| 3 | VWRL.SW | 72% | 1.4 | 4.0 | 7.2 | 2.4 | -4.9 | 0 |
| 4 | EEM | 67% | 0.7 | 2.0 | 7.9 | -0.1 | -2.4 | 0 |
| 5 | GLD | 64% | 1.8 | 6.5 | 8.5 | -0.9 | 0.7 | 19 |
| 6 | VT | 54% | 0.3 | 7.2 | 11.4 | -3.5 | -2.7 | 1 |
| 7 | SLV | 34% | -1.4 | 3.9 | 2.0 | 3.9 | 1.9 | 20 |
| 8 | CSPX.L | 31% | -0.5 | 1.8 | 11.3 | -0.6 | 3.0 | 6 |
| 9 | ^N225 | 30% | -0.7 | 0.9 | -0.2 | -1.7 | -0.3 | 18 |
| 10 | IWDA.AS | 23% | -0.7 | 2.2 | 13.5 | -1.2 | -3.8 | 3 |
| 11 | CSSPX.SW | 23% | -0.9 | 2.9 | 13.6 | -3.7 | -2.3 | 0 |
| 12 | ^RUT | 18% | -1.0 | 0.9 | 7.5 | -2.0 | -5.6 | 0 |
| 13 | VWO | 16% | -1.4 | 1.0 | 4.5 | -1.1 | -2.9 | 0 |
| 14 | ^GDAXI | 13% | -0.6 | 0.7 | 8.1 | -1.6 | -4.7 | 0 |
| 15 | TLT | 10% | -1.7 | 0.5 | 6.7 | -3.1 | -3.2 | 0 |
| 16 | ^STOXX50E | 7% | -1.3 | 0.1 | -3.0 | -1.4 | -5.3 | 0 |
| 17 | DBC | 5% | -3.5 | 0.0 | -5.7 | -5.6 | 1.1 | 3 |
| 18 | XLU | 2% | -2.9 | 0.4 | 6.0 | -3.4 | -4.2 | 0 |
| 19 | USO | 2% | -3.8 | 0.2 | -17.2 | -3.5 | 2.8 | 1 |
| 20 | EFA | 2% | -4.7 | 0.1 | 5.8 | -6.7 | -4.2 | 0 |
| 21 | ^VIX | 0% | 0.0 | n/a | 1.2 | 0.0 | 0.0 | 0 |
| 22 | LQD | 0% | -1.6 | n/a | 5.4 | -1.9 | -3.0 | 0 |
| 23 | VTI | 0% | -2.0 | n/a | 7.3 | -4.1 | -3.8 | 0 |
| 24 | IEF | 0% | -2.1 | n/a | 5.2 | -2.4 | -4.1 | 0 |
| 25 | XLY | 0% | -2.4 | n/a | 7.4 | -3.5 | -1.4 | 0 |
| 26 | XLK | 0% | -2.6 | n/a | 1.8 | -6.0 | 0.7 | 0 |
| 27 | ^SSMI | 0% | -2.7 | n/a | 5.9 | -3.7 | -3.1 | 0 |
| 28 | ^GSPC | 0% | -3.1 | n/a | 7.4 | -3.7 | -3.3 | 0 |
| 29 | VUG | 0% | -3.1 | n/a | 8.1 | -2.7 | 0.6 | 0 |
| 30 | ^DJI | 0% | -3.1 | n/a | 7.5 | -3.4 | -4.8 | 0 |
| 31 | AGG | 0% | -3.2 | n/a | 4.0 | -4.4 | -4.0 | 0 |
| 32 | ACWI | 0% | -3.2 | n/a | 4.7 | -7.1 | -3.2 | 0 |
| 33 | TIP | 0% | -3.4 | n/a | 4.2 | -4.7 | -5.2 | 0 |
| 34 | CSSMI.SW | 0% | -3.6 | n/a | 3.3 | -5.0 | -2.7 | 0 |
| 35 | IWM | 0% | -3.6 | n/a | 7.5 | -4.6 | -6.1 | 0 |
| 36 | BND | 0% | -3.7 | n/a | 4.3 | -4.0 | -4.0 | 0 |
| 37 | SHY | 0% | -3.8 | n/a | 2.1 | -4.6 | -4.8 | 0 |
| 38 | VTV | 0% | -3.9 | n/a | 7.2 | -5.5 | -1.7 | 0 |
| 39 | XLV | 0% | -4.1 | n/a | 7.1 | -5.2 | -1.5 | 0 |
| 40 | QQQ | 0% | -4.1 | n/a | 4.8 | -5.9 | -0.2 | 0 |

(25 more in screen.csv)

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

Searching 9,884 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
