# trix_zero_trend: optimization summary

Updated 2026-11-26T01:05:22Z · backtest.py version `0b037e701c` · 37,180 parameter sets tested with this version (37,180 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

29 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ETHUSDT | 70% | 8.0 | 28.4 | 31.8 | 7.2 | 0.3 | 9 |
| 2 | TRXUSDT | 69% | 9.7 | 52.8 | 34.3 | 22.1 | 0.6 | 20 |
| 3 | BTCUSDT | 69% | 3.8 | 12.8 | 40.0 | 4.8 | 3.3 | 14 |
| 4 | BNBUSDT | 67% | 8.4 | 31.3 | 85.8 | 4.7 | 5.8 | 1 |
| 5 | LINKUSDT | 61% | 5.0 | 30.1 | 50.7 | 8.8 | 2.5 | 2 |
| 6 | LTCUSDT | 59% | 3.3 | 36.0 | 3.9 | 9.4 | -18.3 | 5 |
| 7 | VETUSDT | 49% | 7.6 | 48.8 | 38.6 | 8.2 | -0.1 | 6 |
| 8 | XRPUSDT | 44% | -1.4 | 21.2 | 15.2 | 4.0 | -5.0 | 7 |
| 9 | ETCUSDT | 38% | -0.9 | 34.8 | 24.9 | 5.7 | 6.1 | 12 |
| 10 | BCHUSDT | 34% | 1.1 | 31.3 | 5.2 | 2.1 | -26.6 | 7 |
| 11 | XLMUSDT | 26% | -5.6 | 41.4 | 4.9 | -0.5 | -15.8 | 1 |
| 12 | DASHUSDT | 21% | 3.9 | 32.8 | -27.1 | 11.6 | -10.4 | 3 |
| 13 | ADAUSDT | 16% | 5.8 | 26.4 | 71.3 | 12.1 | 5.7 | 0 |
| 14 | DOGEUSDT | 10% | -11.6 | 28.3 | 165.4 | -16.2 | -1.6 | 0 |
| 15 | ZECUSDT | 8% | -0.2 | 27.4 | -11.6 | -3.1 | 16.6 | 3 |
| 16 | ALGOUSDT | 7% | 1.8 | 19.6 | 5.0 | -5.9 | 4.1 | 0 |
| 17 | ATOMUSDT | 7% | -2.1 | 13.0 | 21.4 | 7.4 | -17.2 | 2 |
| 18 | JSTUSDT | 0% | 8.9 | n/a | -26.7 | 10.1 | 11.3 | 0 |
| 19 | STXUSDT | 0% | 8.9 | n/a | 71.6 | -6.0 | 5.3 | 0 |
| 20 | INJUSDT | 0% | 5.4 | n/a | 75.0 | 13.5 | -19.4 | 0 |
| 21 | AVAXUSDT | 0% | 4.9 | n/a | 68.8 | -12.1 | -9.4 | 0 |
| 22 | DOTUSDT | 0% | 4.0 | n/a | -32.1 | 0.3 | 7.5 | 0 |
| 23 | HBARUSDT | 0% | 3.9 | n/a | 22.5 | -10.6 | 4.0 | 0 |
| 24 | NEARUSDT | 0% | -0.5 | n/a | 13.7 | 14.0 | 9.2 | 0 |
| 25 | FILUSDT | 0% | -1.9 | n/a | -61.2 | -14.2 | -16.2 | 0 |
| 26 | CAKEUSDT | 0% | -4.0 | n/a | -48.0 | -4.0 | -5.9 | 0 |
| 27 | UNIUSDT | 0% | -11.3 | n/a | -31.7 | 4.5 | 2.7 | 0 |
| 28 | AAVEUSDT | 0% | -12.7 | n/a | -41.0 | 1.0 | -11.8 | 0 |
| 29 | SOLUSDT | 0% | -13.9 | n/a | 40.8 | -11.6 | -6.0 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [trix_zero_trend__broad__max-income__v001.md](symbols/broad/trix_zero_trend__broad__max-income__v001.md) | 12.2 | 6.9 | 6.9 | -19.5 | 52.5 | 219/211 |
| broad | balanced | [trix_zero_trend__broad__balanced__v002.md](symbols/broad/trix_zero_trend__broad__balanced__v002.md) | 10.9 | 2.8 | 2.8 | -18.2 | 51.0 | 253/244 |
| broad | safe-starter | [trix_zero_trend__broad__safe-starter__v003.md](symbols/broad/trix_zero_trend__broad__safe-starter__v003.md) | 4.9 | 2.9 | 2.9 | -20.8 | 46.3 | 201/139 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 37,180 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
