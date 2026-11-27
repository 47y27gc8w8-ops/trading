# double_inside_compression: optimization summary

Updated 2026-11-25T23:07:41Z · backtest.py version `02fa540f24` · 2,470 parameter sets tested with this version (2,470 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
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
| 1 | VOO | 0% | 0.9 | n/a | 11.9 | 0.8 | 0.2 | 0 |
| 2 | HYG | 0% | 0.8 | n/a | 4.8 | 0.6 | 0.2 | 0 |
| 3 | ACWI | 0% | 0.7 | n/a | 4.7 | 0.5 | 0.0 | 0 |
| 4 | ^VIX | 0% | 0.6 | n/a | 1.2 | 0.6 | 0.0 | 0 |
| 5 | SPY | 0% | 0.5 | n/a | 9.3 | 0.4 | 0.2 | 0 |
| 6 | SMH | 0% | 0.5 | n/a | -0.3 | 0.5 | -0.7 | 0 |
| 7 | XLP | 0% | 0.5 | n/a | 6.4 | 0.5 | -0.0 | 0 |
| 8 | IVV | 0% | 0.4 | n/a | 4.6 | 0.4 | 0.2 | 0 |
| 9 | CSSMI.SW | 0% | 0.4 | n/a | 3.3 | 0.4 | -0.2 | 0 |
| 10 | TQQQ | 0% | 0.3 | n/a | 58.3 | 0.3 | -1.1 | 0 |
| 11 | ^GSPC | 0% | 0.2 | n/a | 7.4 | 0.2 | 0.1 | 0 |
| 12 | ^FTSE | 0% | 0.2 | n/a | 3.5 | 0.3 | 0.0 | 0 |
| 13 | EEM | 0% | 0.2 | n/a | 7.9 | 0.1 | 0.3 | 0 |
| 14 | ^SSMI | 0% | 0.2 | n/a | 5.9 | 0.1 | -0.1 | 0 |
| 15 | VNQ | 0% | 0.1 | n/a | 8.5 | 0.1 | 0.1 | 0 |
| 16 | ^GDAXI | 0% | 0.1 | n/a | 8.1 | 0.1 | -0.2 | 0 |
| 17 | EFA | 0% | 0.1 | n/a | 5.8 | 0.0 | 0.3 | 0 |
| 18 | VIG | 0% | 0.1 | n/a | 7.0 | 0.1 | -0.2 | 0 |
| 19 | XLI | 0% | 0.1 | n/a | 5.6 | 0.2 | -0.2 | 0 |
| 20 | XLB | 0% | 0.1 | n/a | 5.4 | 0.4 | 0.1 | 0 |
| 21 | IWM | 0% | 0.1 | n/a | 7.5 | 0.1 | 0.5 | 0 |
| 22 | BND | 0% | 0.1 | n/a | 4.3 | 0.1 | 0.0 | 0 |
| 23 | VWO | 0% | 0.0 | n/a | 4.5 | 0.0 | -0.2 | 0 |
| 24 | DIA | 0% | 0.0 | n/a | 6.2 | 0.0 | -0.1 | 0 |
| 25 | SHY | 0% | 0.0 | n/a | 2.1 | -0.0 | -0.0 | 0 |
| 26 | AGG | 0% | 0.0 | n/a | 4.0 | -0.0 | -0.1 | 0 |
| 27 | VUG | 0% | 0.0 | n/a | 8.1 | 0.0 | -0.6 | 0 |
| 28 | ^DJI | 0% | 0.0 | n/a | 7.5 | 0.0 | -0.0 | 0 |
| 29 | VEA | 0% | 0.0 | n/a | -0.3 | 0.0 | 0.2 | 0 |
| 30 | XLK | 0% | 0.0 | n/a | 1.8 | 0.0 | -0.2 | 0 |
| 31 | XLV | 0% | 0.0 | n/a | 7.1 | 0.0 | 0.3 | 0 |
| 32 | TIP | 0% | 0.0 | n/a | 4.2 | 0.0 | -0.2 | 0 |
| 33 | USMV | 0% | 0.0 | n/a | 13.5 | 0.0 | 0.5 | 0 |
| 34 | CSNDX.SW | 0% | 0.0 | n/a | 18.0 | 0.0 | -0.1 | 0 |
| 35 | VWRL.SW | 0% | 0.0 | n/a | 7.2 | 0.0 | 0.4 | 0 |
| 36 | IWDA.AS | 0% | 0.0 | n/a | 13.5 | 0.0 | -0.1 | 0 |
| 37 | CSPX.L | 0% | 0.0 | n/a | 11.3 | 0.0 | 0.0 | 0 |
| 38 | ^STOXX50E | 0% | 0.0 | n/a | -3.0 | 0.0 | 0.6 | 0 |
| 39 | XLY | 0% | -0.0 | n/a | 7.4 | -0.0 | 0.0 | 0 |
| 40 | RSP | 0% | -0.0 | n/a | 9.4 | -0.0 | -0.2 | 0 |

(25 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [double_inside_compression__broad__max-income__v001.md](symbols/broad/double_inside_compression__broad__max-income__v001.md) | 0.0 | 0.0 | 0.0 | -0.6 | 37.0 | 146/133 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 2,470 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
