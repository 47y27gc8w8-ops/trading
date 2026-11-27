# stochrsi_reset: optimization summary

Updated 2026-11-26T02:06:15Z · backtest.py version `67f6dd290d` · 7,451 parameter sets tested with this version (7,451 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 4h bars)
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
| 1 | JSTUSDT | 92% | 25.1 | 60.4 | 4.5 | 40.7 | -4.0 | 8 |
| 2 | INJUSDT | 72% | 7.9 | 49.8 | 44.0 | 9.8 | -40.3 | 1 |
| 3 | NEARUSDT | 57% | 6.4 | 41.0 | -15.6 | -22.3 | -33.0 | 0 |
| 4 | STXUSDT | 44% | -2.4 | 51.8 | 105.8 | 25.3 | -45.2 | 0 |
| 5 | CAKEUSDT | 34% | -3.7 | 16.9 | -48.5 | 14.0 | -38.4 | 0 |
| 6 | SOLUSDT | 31% | -6.7 | 53.6 | 214.4 | -15.0 | -20.2 | 0 |
| 7 | AVAXUSDT | 25% | -10.2 | 28.1 | 14.6 | -20.1 | -9.8 | 0 |
| 8 | ATOMUSDT | 25% | -16.6 | 19.8 | 36.8 | -22.6 | -26.3 | 0 |
| 9 | HBARUSDT | 21% | -8.4 | 37.6 | 26.6 | 5.1 | -26.1 | 0 |
| 10 | UNIUSDT | 21% | -11.7 | 15.1 | -37.0 | -25.0 | -5.2 | 2 |
| 11 | ICPUSDT | 18% | -13.2 | 12.6 | -41.6 | -9.6 | -57.6 | 0 |
| 12 | BCHUSDT | 16% | -14.1 | 13.2 | 2.9 | 13.2 | -47.1 | 0 |
| 13 | VETUSDT | 16% | -15.3 | 17.6 | 53.1 | -13.7 | -38.0 | 0 |
| 14 | DOTUSDT | 3% | -15.7 | 11.1 | -20.7 | -4.6 | -35.1 | 0 |
| 15 | XRPUSDT | 3% | -22.0 | 7.2 | 5.0 | -17.4 | -25.1 | 0 |
| 16 | FILUSDT | 3% | -22.2 | 6.8 | -67.5 | -34.4 | -35.3 | 0 |
| 17 | ALGOUSDT | 3% | -24.2 | 6.1 | -3.8 | -45.2 | -46.2 | 0 |
| 18 | ETHUSDT | 2% | -19.3 | 11.8 | 13.4 | -13.1 | -13.9 | 0 |
| 19 | TRXUSDT | 2% | -19.8 | 6.7 | 54.0 | -25.4 | -12.6 | 0 |
| 20 | ADAUSDT | 2% | -21.5 | 4.7 | 45.0 | -28.6 | -35.9 | 0 |
| 21 | DASHUSDT | 2% | -23.6 | 0.6 | -20.4 | -28.4 | -57.2 | 0 |
| 22 | DOGEUSDT | 2% | -27.9 | 8.7 | 156.4 | -43.4 | -43.3 | 0 |
| 23 | BTCUSDT | 0% | -16.0 | n/a | 27.1 | -18.2 | -26.0 | 0 |
| 24 | BNBUSDT | 0% | -18.4 | n/a | 74.8 | -24.7 | -30.4 | 0 |
| 25 | XLMUSDT | 0% | -19.6 | n/a | -11.6 | -13.9 | -41.5 | 0 |
| 26 | LTCUSDT | 0% | -23.5 | n/a | -8.6 | -21.9 | -34.8 | 0 |
| 27 | ZECUSDT | 0% | -27.3 | n/a | -11.3 | -37.3 | 5.3 | 0 |
| 28 | LINKUSDT | 0% | -27.9 | n/a | 37.9 | -27.6 | -11.5 | 0 |
| 29 | ETCUSDT | 0% | -29.2 | n/a | 34.4 | -36.0 | -8.5 | 0 |
| 30 | AAVEUSDT | 0% | -30.3 | n/a | -36.5 | -26.2 | -2.0 | 0 |
| 31 | SHIBUSDT | 0% | -32.2 | n/a | -41.9 | -26.5 | -32.6 | 0 |

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

Searching 7,451 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
