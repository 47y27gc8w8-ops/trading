# crypto_weekly_open_reclaim: optimization summary

Updated 2026-11-26T02:31:12Z · backtest.py version `ad90d38065` · 10,531 parameter sets tested with this version (10,531 rows in results.csv in total) · last run ended: see base optimization.log

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
| 1 | DASHUSDT | 95% | 20.0 | 46.0 | -20.4 | 7.4 | -2.6 | 0 |
| 2 | AVAXUSDT | 93% | 27.8 | 78.9 | 14.6 | 25.8 | -31.1 | 0 |
| 3 | ETHUSDT | 89% | 19.2 | 37.4 | 13.4 | 21.6 | -6.8 | 1 |
| 4 | JSTUSDT | 84% | 20.4 | 57.3 | 4.5 | 4.5 | -7.0 | 2 |
| 5 | SOLUSDT | 82% | 33.7 | 83.2 | 214.4 | 27.4 | -16.9 | 0 |
| 6 | ATOMUSDT | 64% | 7.2 | 36.9 | 36.8 | 29.4 | 0.0 | 4 |
| 7 | DOTUSDT | 56% | 1.4 | 39.1 | -20.7 | 34.4 | -27.6 | 0 |
| 8 | STXUSDT | 54% | 0.9 | 36.2 | 105.8 | 13.6 | -36.2 | 0 |
| 9 | LTCUSDT | 49% | -2.2 | 22.8 | -8.6 | -6.0 | -13.4 | 0 |
| 10 | XLMUSDT | 46% | -1.4 | 24.7 | -11.6 | -2.4 | -33.0 | 0 |
| 11 | INJUSDT | 44% | -2.4 | 31.3 | 44.0 | -1.6 | -30.2 | 0 |
| 12 | HBARUSDT | 43% | -1.6 | 30.8 | 26.6 | 20.3 | -0.7 | 20 |
| 13 | ETCUSDT | 38% | -7.9 | 18.2 | 34.4 | -9.5 | -5.4 | 1 |
| 14 | VETUSDT | 34% | -3.6 | 18.0 | 53.1 | -3.5 | 2.5 | 3 |
| 15 | BNBUSDT | 26% | -6.0 | 11.3 | 74.8 | -11.2 | -18.8 | 0 |
| 16 | CAKEUSDT | 23% | -5.6 | 15.3 | -48.5 | -1.6 | 20.1 | 12 |
| 17 | ADAUSDT | 23% | -11.1 | 10.9 | 45.0 | -15.5 | -3.0 | 7 |
| 18 | ICPUSDT | 20% | -15.5 | 18.8 | -41.6 | -29.1 | -19.6 | 1 |
| 19 | AAVEUSDT | 18% | -11.7 | 14.3 | -36.5 | -8.6 | -17.4 | 0 |
| 20 | DOGEUSDT | 18% | -14.6 | 6.7 | 156.4 | -12.7 | -35.2 | 0 |
| 21 | TRXUSDT | 13% | -13.2 | 16.0 | 54.0 | -16.6 | -15.4 | 0 |
| 22 | NEARUSDT | 13% | -19.4 | 27.2 | -15.6 | -4.6 | 1.2 | 2 |
| 23 | BTCUSDT | 11% | -7.4 | 3.4 | 27.1 | -6.1 | -17.5 | 0 |
| 24 | BCHUSDT | 10% | -19.7 | 5.8 | 2.9 | -21.9 | -33.5 | 0 |
| 25 | XRPUSDT | 7% | -12.6 | 4.7 | 5.0 | -17.4 | -14.4 | 0 |
| 26 | LINKUSDT | 2% | -15.8 | 9.2 | 37.9 | -19.3 | -19.5 | 0 |
| 27 | SHIBUSDT | 2% | -20.6 | 0.6 | -41.9 | -15.4 | -19.8 | 0 |
| 28 | ZECUSDT | 0% | -20.6 | n/a | -11.3 | -27.2 | -10.2 | 0 |
| 29 | ALGOUSDT | 0% | -27.0 | n/a | -3.8 | -32.9 | -10.4 | 0 |
| 30 | FILUSDT | 0% | -29.7 | n/a | -67.5 | -13.3 | -18.3 | 0 |
| 31 | UNIUSDT | 0% | -37.3 | n/a | -37.0 | -35.9 | -14.2 | 0 |

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

Searching 10,531 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
