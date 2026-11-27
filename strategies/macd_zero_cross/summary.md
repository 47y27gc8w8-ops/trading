# macd_zero_cross: optimization summary

Updated 2026-11-26T04:41:03Z · backtest.py version `d83cf0d490` · 701 parameter sets tested with this version (701 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ATOMUSDT | 87% | 16.6 | 41.7 | 36.8 | 40.2 | -24.0 | 0 |
| 2 | SOLUSDT | 77% | 14.2 | 70.8 | 214.4 | 4.9 | -25.1 | 3 |
| 3 | BNBUSDT | 69% | 7.3 | 32.6 | 74.8 | 20.7 | 3.3 | 6 |
| 4 | INJUSDT | 64% | 11.8 | 66.2 | 44.0 | 38.8 | -30.4 | 0 |
| 5 | JSTUSDT | 64% | 9.7 | 77.0 | 4.5 | 52.2 | 7.3 | 17 |
| 6 | LINKUSDT | 46% | -0.8 | 21.1 | 37.9 | -14.9 | -20.5 | 0 |
| 7 | TRXUSDT | 39% | -1.6 | 26.8 | 54.0 | 3.5 | -1.7 | 0 |
| 8 | AVAXUSDT | 39% | -5.4 | 42.2 | 14.6 | -7.0 | -44.0 | 0 |
| 9 | ADAUSDT | 31% | -2.5 | 18.9 | 45.0 | -22.9 | -23.4 | 0 |
| 10 | HBARUSDT | 31% | -9.1 | 27.0 | 26.6 | -4.4 | 6.9 | 1 |
| 11 | LTCUSDT | 30% | -10.3 | 15.1 | -8.6 | -10.6 | -25.4 | 0 |
| 12 | ETCUSDT | 26% | -10.1 | 20.0 | 34.4 | -21.2 | -31.0 | 0 |
| 13 | DOGEUSDT | 21% | -8.3 | 15.0 | 156.4 | -12.7 | -25.3 | 0 |
| 14 | VETUSDT | 20% | -8.3 | 21.7 | 53.1 | -4.2 | -4.5 | 0 |
| 15 | ICPUSDT | 16% | -15.8 | 7.6 | -41.6 | -23.4 | -15.9 | 1 |
| 16 | NEARUSDT | 13% | -10.7 | 8.7 | -15.6 | -19.5 | -17.6 | 1 |
| 17 | AAVEUSDT | 13% | -15.7 | 14.7 | -36.5 | -4.5 | -5.3 | 1 |
| 18 | DOTUSDT | 11% | -17.3 | 9.7 | -20.7 | -21.2 | -33.9 | 0 |
| 19 | ZECUSDT | 10% | -12.2 | 10.8 | -11.3 | -8.8 | 52.6 | 6 |
| 20 | XLMUSDT | 8% | -12.5 | 14.2 | -11.6 | -32.5 | -13.8 | 0 |
| 21 | CAKEUSDT | 8% | -20.9 | 13.8 | -48.5 | -13.0 | 11.3 | 5 |
| 22 | UNIUSDT | 8% | -27.0 | 13.6 | -37.0 | -26.1 | -41.6 | 0 |
| 23 | ALGOUSDT | 7% | -16.1 | 14.7 | -3.8 | -16.1 | -21.5 | 0 |
| 24 | FILUSDT | 7% | -18.3 | 18.9 | -67.5 | 12.0 | -20.0 | 0 |
| 25 | ETHUSDT | 3% | -9.1 | 4.0 | 13.4 | -11.7 | -41.1 | 0 |
| 26 | STXUSDT | 3% | -17.3 | 23.2 | 105.8 | -19.5 | -9.1 | 0 |
| 27 | BTCUSDT | 2% | -13.7 | 3.8 | 27.1 | -12.0 | -19.5 | 0 |
| 28 | BCHUSDT | 2% | -15.7 | 1.4 | 2.9 | -14.2 | -4.5 | 0 |
| 29 | DASHUSDT | 0% | -15.3 | n/a | -20.4 | -17.7 | -15.1 | 0 |
| 30 | SHIBUSDT | 0% | -20.7 | n/a | -41.9 | -28.9 | -6.6 | 0 |
| 31 | XRPUSDT | 0% | -24.9 | n/a | 5.0 | -16.2 | -18.6 | 0 |

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

Searching 701 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
