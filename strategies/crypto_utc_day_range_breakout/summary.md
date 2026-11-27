# crypto_utc_day_range_breakout: optimization summary

Updated 2026-11-26T07:25:41Z · backtest.py version `b58bb2def8` · 10,531 parameter sets tested with this version (10,531 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 1h bars)
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
| 1 | AVAXUSDT | 28% | -23.2 | 25.6 | 107.0 | -38.9 | -20.6 | 0 |
| 2 | DOGEUSDT | 25% | -13.8 | 11.7 | 130.1 | -18.9 | -41.6 | 0 |
| 3 | RAYUSDT | 15% | -13.9 | 5.2 | -59.6 | -21.8 | -52.0 | 0 |
| 4 | ETHUSDT | 8% | -8.0 | 1.7 | 20.8 | -11.0 | -39.8 | 0 |
| 5 | FILUSDT | 5% | -18.6 | 1.1 | -37.4 | -29.8 | -38.6 | 0 |
| 6 | BNBUSDT | 5% | -23.1 | 2.7 | 58.2 | -30.6 | -25.2 | 0 |
| 7 | TRXUSDT | 3% | -20.8 | 1.6 | 35.9 | -34.1 | -26.6 | 0 |
| 8 | SOLUSDT | 2% | -18.2 | 11.9 | 211.6 | -26.8 | -47.8 | 0 |
| 9 | ADAUSDT | 0% | -22.0 | n/a | 27.0 | -32.5 | -56.7 | 0 |
| 10 | BCHUSDT | 0% | -23.3 | n/a | -9.5 | -24.7 | -57.2 | 0 |
| 11 | JSTUSDT | 0% | -25.9 | n/a | 1.9 | -24.9 | -32.2 | 0 |
| 12 | ETCUSDT | 0% | -26.7 | n/a | 11.2 | -32.8 | -35.7 | 0 |
| 13 | XRPUSDT | 0% | -26.9 | n/a | 4.9 | -33.9 | -35.8 | 0 |
| 14 | QNTUSDT | 0% | -27.1 | n/a | -26.0 | -39.8 | -36.3 | 0 |
| 15 | DOTUSDT | 0% | -29.0 | n/a | 23.9 | -35.5 | -36.8 | 0 |
| 16 | DASHUSDT | 0% | -30.0 | n/a | -30.4 | -27.3 | -30.1 | 0 |
| 17 | INJUSDT | 0% | -32.7 | n/a | 115.0 | -19.3 | -36.9 | 0 |
| 18 | SHIBUSDT | 0% | -32.7 | n/a | 11.7 | -38.9 | -39.2 | 0 |
| 19 | BTCUSDT | 0% | -33.5 | n/a | 20.6 | -34.6 | -35.7 | 0 |
| 20 | HBARUSDT | 0% | -33.9 | n/a | 36.2 | -39.4 | -27.7 | 0 |
| 21 | LINKUSDT | 0% | -37.7 | n/a | 104.9 | -45.9 | -34.6 | 0 |
| 22 | STXUSDT | 0% | -37.9 | n/a | 88.6 | -48.3 | -32.8 | 0 |
| 23 | VETUSDT | 0% | -40.5 | n/a | 21.6 | -37.0 | -38.4 | 0 |
| 24 | AAVEUSDT | 0% | -41.0 | n/a | 7.2 | -47.1 | -48.4 | 0 |
| 25 | UNIUSDT | 0% | -41.0 | n/a | 27.7 | -53.2 | -45.4 | 0 |
| 26 | LTCUSDT | 0% | -41.8 | n/a | -16.7 | -41.9 | -44.3 | 0 |
| 27 | XLMUSDT | 0% | -42.8 | n/a | -12.6 | -46.1 | -37.3 | 0 |
| 28 | ZECUSDT | 0% | -43.7 | n/a | -18.6 | -47.1 | -19.6 | 0 |
| 29 | ATOMUSDT | 0% | -45.5 | n/a | 15.4 | -50.2 | -54.1 | 0 |
| 30 | ALGOUSDT | 0% | -47.1 | n/a | -19.9 | -44.8 | -32.6 | 0 |
| 31 | NEARUSDT | 0% | -48.2 | n/a | 52.8 | -49.6 | -53.5 | 0 |
| 32 | CAKEUSDT | 0% | -49.5 | n/a | -52.3 | -52.8 | -42.8 | 0 |
| 33 | ICPUSDT | 0% | -64.0 | n/a | -35.4 | -62.1 | -51.6 | 0 |

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
