# inside_bar_breakout: optimization summary

Updated 2026-11-26T01:33:36Z · backtest.py version `460819d897` · 1,171 parameter sets tested with this version (1,171 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SOLUSDT (crypto, 4h bars)
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
| 1 | INJUSDT | 87% | 12.6 | 23.6 | 44.0 | 20.5 | -5.4 | 0 |
| 2 | ADAUSDT | 61% | 4.6 | 10.2 | 45.0 | 7.6 | -26.7 | 0 |
| 3 | TRXUSDT | 61% | 1.1 | 8.1 | 54.0 | 6.8 | -11.9 | 0 |
| 4 | DOGEUSDT | 41% | -1.4 | 13.1 | 156.4 | -6.9 | -20.1 | 0 |
| 5 | JSTUSDT | 31% | -4.4 | 19.5 | 4.5 | 4.2 | -0.0 | 0 |
| 6 | ETCUSDT | 26% | -9.5 | 20.9 | 34.4 | -11.7 | -22.1 | 0 |
| 7 | ETHUSDT | 15% | -9.1 | 3.9 | 13.4 | -12.9 | -25.9 | 0 |
| 8 | ZECUSDT | 11% | -8.8 | 3.0 | -11.3 | 0.3 | -5.7 | 2 |
| 9 | DASHUSDT | 0% | -11.3 | n/a | -20.4 | -12.2 | -19.9 | 0 |
| 10 | LINKUSDT | 0% | -12.6 | n/a | 37.9 | -9.6 | -21.1 | 0 |
| 11 | SHIBUSDT | 0% | -14.1 | n/a | -41.9 | -22.1 | -34.1 | 0 |
| 12 | XLMUSDT | 0% | -16.3 | n/a | -11.6 | -20.4 | -29.0 | 0 |
| 13 | NEARUSDT | 0% | -17.8 | n/a | -15.6 | -20.4 | -44.6 | 0 |
| 14 | BTCUSDT | 0% | -18.1 | n/a | 27.1 | -23.6 | -21.4 | 0 |
| 15 | VETUSDT | 0% | -22.9 | n/a | 53.1 | -20.6 | -44.0 | 0 |
| 16 | ATOMUSDT | 0% | -22.9 | n/a | 36.8 | -23.3 | -20.6 | 0 |
| 17 | SOLUSDT | 0% | -23.3 | n/a | 214.4 | -30.3 | -16.5 | 0 |
| 18 | ICPUSDT | 0% | -23.3 | n/a | -41.6 | -25.1 | -25.5 | 0 |
| 19 | BCHUSDT | 0% | -24.7 | n/a | 2.9 | -27.3 | -22.5 | 0 |
| 20 | ALGOUSDT | 0% | -27.9 | n/a | -3.8 | -27.2 | -35.9 | 0 |
| 21 | XRPUSDT | 0% | -28.8 | n/a | 5.0 | -38.9 | -16.9 | 0 |
| 22 | UNIUSDT | 0% | -29.2 | n/a | -37.0 | -26.7 | -19.2 | 0 |
| 23 | BNBUSDT | 0% | -29.4 | n/a | 74.8 | -33.3 | -17.4 | 0 |
| 24 | CAKEUSDT | 0% | -29.9 | n/a | -48.5 | -27.7 | -5.2 | 0 |
| 25 | LTCUSDT | 0% | -31.8 | n/a | -8.6 | -33.2 | -24.1 | 0 |
| 26 | AAVEUSDT | 0% | -36.9 | n/a | -36.5 | -34.7 | -31.1 | 0 |
| 27 | AVAXUSDT | 0% | -39.3 | n/a | 14.6 | -42.9 | -23.7 | 0 |
| 28 | HBARUSDT | 0% | -39.8 | n/a | 26.6 | -44.4 | -2.8 | 0 |
| 29 | FILUSDT | 0% | -41.0 | n/a | -67.5 | -36.7 | -18.1 | 0 |
| 30 | STXUSDT | 0% | -44.0 | n/a | 105.8 | -43.5 | -31.9 | 0 |
| 31 | DOTUSDT | 0% | -46.4 | n/a | -20.7 | -44.9 | -23.7 | 0 |

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

Searching 1,171 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
