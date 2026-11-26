# hammer_reversal_quantified: optimization summary

Updated 2026-11-26T02:24:59Z · backtest.py version `2300b232a1` · 27,170 parameter sets tested with this version (27,170 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: GLD (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

63 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ^RUT | 44% | 1.3 | 2.2 | 7.5 | 1.7 | -0.0 | 18 |
| 2 | ^FTSE | 44% | 0.4 | 0.8 | 3.5 | 0.4 | -0.4 | 12 |
| 3 | ^IXIC | 43% | 0.1 | 1.8 | 9.5 | 0.5 | -0.3 | 2 |
| 4 | XLB | 31% | 0.2 | 1.2 | 5.7 | 0.8 | 0.3 | 5 |
| 5 | XLY | 23% | 0.1 | 0.9 | 7.4 | -0.1 | -1.7 | 0 |
| 6 | SPY | 21% | 0.3 | 0.8 | 9.3 | 0.5 | 0.4 | 6 |
| 7 | XLP | 21% | 0.2 | 0.6 | 7.5 | 0.0 | 0.2 | 1 |
| 8 | XLU | 15% | -0.0 | 0.4 | 6.4 | -0.3 | 0.1 | 9 |
| 9 | XLI | 13% | 0.6 | 2.0 | 5.9 | 1.1 | 0.6 | 4 |
| 10 | ^SSMI | 13% | 0.2 | 0.7 | 5.9 | 0.4 | 0.1 | 0 |
| 11 | ^DJI | 11% | 0.1 | 0.2 | 7.5 | -0.1 | -0.2 | 0 |
| 12 | ^GDAXI | 2% | 0.1 | 0.1 | 8.1 | 0.3 | 0.1 | 1 |
| 13 | TQQQ | 0% | 2.2 | n/a | 40.4 | 3.5 | -0.6 | 0 |
| 14 | SCHD | 0% | 0.9 | n/a | 12.3 | 1.0 | -0.6 | 0 |
| 15 | USMV | 0% | 0.9 | n/a | 13.4 | 0.9 | -0.2 | 0 |
| 16 | IWDA.AS | 0% | 0.8 | n/a | 13.1 | 0.9 | -0.2 | 0 |
| 17 | XLK | 0% | 0.8 | n/a | -0.1 | 1.1 | 0.4 | 0 |
| 18 | VNQ | 0% | 0.8 | n/a | 7.8 | 1.3 | -0.1 | 0 |
| 19 | CSNDX.SW | 0% | 0.8 | n/a | 15.9 | 1.3 | 1.3 | 0 |
| 20 | VOO | 0% | 0.8 | n/a | 16.7 | 0.9 | 0.1 | 0 |
| 21 | CSSMI.SW | 0% | 0.7 | n/a | 8.7 | 0.5 | 0.5 | 0 |
| 22 | IVV | 0% | 0.7 | n/a | 5.2 | 0.6 | -0.0 | 0 |
| 23 | EFA | 0% | 0.6 | n/a | 6.7 | 0.2 | 0.3 | 0 |
| 24 | HYG | 0% | 0.5 | n/a | 5.0 | 0.6 | 0.2 | 0 |
| 25 | DIA | 0% | 0.5 | n/a | 6.1 | 0.8 | -0.5 | 0 |
| 26 | ^VIX | 0% | 0.5 | n/a | 1.2 | 1.4 | -1.6 | 0 |
| 27 | VUG | 0% | 0.4 | n/a | 8.6 | 0.5 | 0.2 | 0 |
| 28 | IWM | 0% | 0.4 | n/a | 7.0 | 0.6 | -0.3 | 0 |
| 29 | XLF | 0% | 0.4 | n/a | 2.2 | 0.6 | -0.4 | 0 |
| 30 | VTV | 0% | 0.3 | n/a | 6.9 | -0.1 | -0.8 | 0 |
| 31 | VIG | 0% | 0.2 | n/a | 6.2 | -0.1 | 0.1 | 0 |
| 32 | QQQ | 0% | 0.1 | n/a | 0.6 | 0.1 | 0.2 | 0 |
| 33 | RSP | 0% | 0.1 | n/a | 8.5 | 0.1 | -0.0 | 0 |
| 34 | BND | 0% | 0.1 | n/a | 3.9 | -0.1 | -0.1 | 0 |
| 35 | GDX | 0% | 0.1 | n/a | -10.7 | 0.6 | -1.0 | 0 |
| 36 | DBC | 0% | 0.1 | n/a | -6.1 | 0.6 | -0.6 | 0 |
| 37 | VWO | 0% | 0.0 | n/a | 2.9 | -0.6 | 0.2 | 0 |
| 38 | TLT | 0% | 0.0 | n/a | 6.9 | 0.0 | -0.1 | 0 |
| 39 | ^N225 | 0% | 0.0 | n/a | -0.2 | 0.3 | 0.3 | 0 |
| 40 | AGG | 0% | 0.0 | n/a | 4.1 | -0.1 | -0.1 | 0 |

(23 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [hammer_reversal_quantified__broad__max-income__v001.md](symbols/broad/hammer_reversal_quantified__broad__max-income__v001.md) | 0.2 | 0.1 | 0.1 | -1.5 | 70.5 | 616/595 |
| broad | balanced | [hammer_reversal_quantified__broad__balanced__v002.md](symbols/broad/hammer_reversal_quantified__broad__balanced__v002.md) | 0.2 | 0.1 | 0.1 | -1.3 | 73.4 | 621/599 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 27,170 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
