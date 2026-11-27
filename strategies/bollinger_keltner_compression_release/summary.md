# bollinger_keltner_compression_release: optimization summary

Updated 2026-11-26T00:11:23Z · backtest.py version `80486c3525` · 12,871 parameter sets tested with this version (12,871 rows in results.csv in total) · last run ended: see base optimization.log

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
| 1 | XRPUSDT | 77% | 5.5 | 34.8 | 5.0 | -2.1 | 2.0 | 6 |
| 2 | ADAUSDT | 74% | 6.2 | 28.8 | 45.0 | 9.0 | 15.2 | 31 |
| 3 | ETHUSDT | 74% | 3.6 | 17.5 | 13.4 | 4.7 | -1.1 | 4 |
| 4 | XLMUSDT | 72% | 4.3 | 20.7 | -11.6 | 0.6 | 5.9 | 24 |
| 5 | TRXUSDT | 39% | -0.5 | 8.4 | 54.0 | -2.6 | -0.7 | 10 |
| 6 | LINKUSDT | 39% | -0.5 | 21.5 | 37.9 | 2.9 | 1.9 | 11 |
| 7 | INJUSDT | 39% | -0.9 | 38.0 | 44.0 | -10.8 | -6.7 | 6 |
| 8 | ZECUSDT | 34% | -0.8 | 29.4 | -11.3 | -0.2 | 6.2 | 14 |
| 9 | BNBUSDT | 30% | -2.2 | 9.0 | 74.8 | -10.7 | -3.3 | 5 |
| 10 | LTCUSDT | 28% | -4.1 | 12.2 | -8.6 | -17.6 | -3.0 | 2 |
| 11 | ETCUSDT | 25% | -4.4 | 15.6 | 34.4 | -6.6 | -11.5 | 2 |
| 12 | JSTUSDT | 20% | -3.9 | 14.0 | 4.5 | 2.1 | -9.9 | 2 |
| 13 | SOLUSDT | 18% | -5.3 | 13.9 | 214.4 | -8.2 | 2.3 | 6 |
| 14 | ALGOUSDT | 18% | -5.9 | 16.6 | -3.8 | -9.0 | 8.2 | 4 |
| 15 | AVAXUSDT | 18% | -6.1 | 19.1 | 14.6 | -11.2 | -7.4 | 2 |
| 16 | DOGEUSDT | 16% | -7.8 | 9.0 | 156.4 | -5.7 | -6.0 | 6 |
| 17 | BTCUSDT | 15% | -4.7 | 9.5 | 27.1 | -1.8 | -5.3 | 0 |
| 18 | ICPUSDT | 15% | -7.8 | 36.1 | -41.6 | -5.1 | -12.7 | 4 |
| 19 | UNIUSDT | 13% | -5.4 | 7.7 | -37.0 | 4.1 | -16.5 | 0 |
| 20 | VETUSDT | 13% | -10.4 | 13.0 | 53.1 | -7.7 | 9.6 | 5 |
| 21 | AAVEUSDT | 8% | -15.2 | 6.5 | -36.5 | -20.1 | 10.7 | 5 |
| 22 | FILUSDT | 7% | -19.4 | 6.2 | -67.5 | -10.0 | 1.1 | 2 |
| 23 | DASHUSDT | 2% | -11.9 | 0.5 | -20.4 | -18.1 | 0.7 | 0 |
| 24 | BCHUSDT | 2% | -12.2 | 2.7 | 2.9 | -20.2 | -9.0 | 0 |
| 25 | HBARUSDT | 2% | -15.8 | 6.7 | 26.6 | -16.9 | 10.7 | 0 |
| 26 | STXUSDT | 2% | -17.5 | 3.0 | 105.8 | -25.8 | -6.9 | 1 |
| 27 | NEARUSDT | 0% | -15.5 | n/a | -15.6 | -17.2 | 23.8 | 0 |
| 28 | DOTUSDT | 0% | -17.2 | n/a | -20.7 | -16.9 | -3.2 | 0 |
| 29 | ATOMUSDT | 0% | -19.0 | n/a | 36.8 | -24.7 | -12.6 | 0 |
| 30 | SHIBUSDT | 0% | -21.1 | n/a | -41.9 | -26.6 | 1.2 | 0 |
| 31 | CAKEUSDT | 0% | -23.2 | n/a | -48.5 | -30.6 | -11.3 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [bollinger_keltner_compression_release__broad__max-income__v001.md](symbols/broad/bollinger_keltner_compression_release__broad__max-income__v001.md) | 0.3 | 3.5 | 0.3 | -33.3 | 31.0 | 2120/1424 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 12,871 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
