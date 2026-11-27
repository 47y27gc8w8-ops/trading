# crypto_utc_overnight_window: optimization summary

Updated 2026-11-26T08:08:49Z · backtest.py version `93730bbf50` · 1,430 parameter sets tested with this version (1,430 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

33 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | JSTUSDT | 0% | -8.4 | n/a | 1.9 | -11.1 | -47.7 | 0 |
| 2 | STXUSDT | 0% | -25.8 | n/a | 88.6 | -27.3 | -35.2 | 0 |
| 3 | HBARUSDT | 0% | -30.7 | n/a | 36.2 | -30.5 | -34.9 | 0 |
| 4 | NEARUSDT | 0% | -32.1 | n/a | 52.8 | -31.2 | -51.4 | 0 |
| 5 | QNTUSDT | 0% | -34.2 | n/a | -26.0 | -34.3 | -30.5 | 0 |
| 6 | BNBUSDT | 0% | -35.0 | n/a | 58.2 | -34.7 | -49.5 | 0 |
| 7 | DASHUSDT | 0% | -37.2 | n/a | -30.4 | -36.2 | -47.4 | 0 |
| 8 | BCHUSDT | 0% | -37.9 | n/a | -9.5 | -39.5 | -48.4 | 0 |
| 9 | XLMUSDT | 0% | -37.9 | n/a | -12.6 | -37.0 | -46.4 | 0 |
| 10 | FILUSDT | 0% | -38.2 | n/a | -37.4 | -37.5 | -54.7 | 0 |
| 11 | RAYUSDT | 0% | -38.6 | n/a | -59.6 | -37.0 | -46.3 | 0 |
| 12 | ATOMUSDT | 0% | -39.0 | n/a | 15.4 | -38.8 | -45.2 | 0 |
| 13 | ETCUSDT | 0% | -39.8 | n/a | 11.2 | -40.9 | -43.6 | 0 |
| 14 | ALGOUSDT | 0% | -40.0 | n/a | -19.9 | -38.7 | -45.0 | 0 |
| 15 | SHIBUSDT | 0% | -40.6 | n/a | 11.7 | -40.6 | -42.0 | 0 |
| 16 | AVAXUSDT | 0% | -41.1 | n/a | 107.0 | -40.2 | -39.4 | 0 |
| 17 | CAKEUSDT | 0% | -41.8 | n/a | -52.3 | -41.6 | -38.1 | 0 |
| 18 | ICPUSDT | 0% | -42.0 | n/a | -35.4 | -41.4 | -43.6 | 0 |
| 19 | DOGEUSDT | 0% | -42.1 | n/a | 130.1 | -41.3 | -41.7 | 0 |
| 20 | ZECUSDT | 0% | -43.2 | n/a | -18.6 | -42.6 | -49.6 | 0 |
| 21 | DOTUSDT | 0% | -43.2 | n/a | 23.9 | -43.0 | -45.8 | 0 |
| 22 | UNIUSDT | 0% | -43.4 | n/a | 27.7 | -42.2 | -42.5 | 0 |
| 23 | LTCUSDT | 0% | -44.5 | n/a | -16.7 | -44.1 | -49.2 | 0 |
| 24 | AAVEUSDT | 0% | -44.9 | n/a | 7.2 | -44.3 | -44.8 | 0 |
| 25 | LINKUSDT | 0% | -46.5 | n/a | 104.9 | -47.3 | -48.5 | 0 |
| 26 | ADAUSDT | 0% | -48.8 | n/a | 27.0 | -48.8 | -40.2 | 0 |
| 27 | ETHUSDT | 0% | -48.9 | n/a | 20.8 | -49.1 | -49.4 | 0 |
| 28 | VETUSDT | 0% | -49.6 | n/a | 21.6 | -49.6 | -33.2 | 0 |
| 29 | XRPUSDT | 0% | -49.7 | n/a | 4.9 | -49.1 | -55.5 | 0 |
| 30 | BTCUSDT | 0% | -50.2 | n/a | 20.6 | -50.2 | -50.6 | 0 |
| 31 | SOLUSDT | 0% | -53.2 | n/a | 211.6 | -54.3 | -47.1 | 0 |
| 32 | TRXUSDT | 0% | -53.1 | n/a | 35.9 | -52.5 | -57.1 | 0 |
| 33 | INJUSDT | 0% | -62.8 | n/a | 115.0 | -63.8 | -51.5 | 0 |

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

Searching 1,430 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
