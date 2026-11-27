# volume_climax_rejection: optimization summary

Updated 2026-11-26T05:03:09Z · backtest.py version `9186fdeee3` · 15,264 parameter sets tested with this version (15,264 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 270 | `{"max_candles": 51, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 277 | `{"max_candles": 60, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 284 | `{"max_candles": 69, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 291 | `{"max_candles": 78, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 298 | `{"max_candles": 87, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 305 | `{"max_candles": 96, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.29 |
| 342 | `{"max_candles": 42, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 349 | `{"max_candles": 33, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.38 |
| 357 | `{"max_candles": 24, "rvol": 2.5, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 47.96 | 0.1 | -18.2 | 50.0 | 89.27 | 0.3 | -11.0 | 3.88 | 20/9 | 0.29 |

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLMUSDT | 10% | 2.7 | 10.1 | -11.6 | 2.7 | 3.2 | 6 |
| 2 | ADAUSDT | 3% | 1.6 | 7.2 | 45.0 | -1.8 | 6.1 | 2 |
| 3 | BTCUSDT | 2% | 0.0 | 0.0 | 27.1 | 0.9 | 0.4 | 1 |
| 4 | SOLUSDT | 0% | 8.2 | n/a | 214.4 | 4.5 | 3.2 | 0 |
| 5 | DOTUSDT | 0% | 3.3 | n/a | -20.7 | 0.0 | 9.8 | 0 |
| 6 | BCHUSDT | 0% | 2.8 | n/a | 2.9 | 2.8 | 3.9 | 0 |
| 7 | XRPUSDT | 0% | 1.8 | n/a | 5.0 | 1.1 | -4.0 | 0 |
| 8 | BNBUSDT | 0% | 1.6 | n/a | 74.8 | 2.5 | 0.8 | 0 |
| 9 | AAVEUSDT | 0% | 1.6 | n/a | -36.5 | -0.1 | 1.4 | 0 |
| 10 | CAKEUSDT | 0% | 0.5 | n/a | -48.5 | 0.6 | 3.4 | 0 |
| 11 | ZECUSDT | 0% | 0.3 | n/a | -11.3 | 2.7 | 2.6 | 0 |
| 12 | LINKUSDT | 0% | 0.0 | n/a | 37.9 | -3.5 | 7.0 | 0 |
| 13 | NEARUSDT | 0% | 0.0 | n/a | -15.6 | 0.6 | 4.5 | 0 |
| 14 | LTCUSDT | 0% | 0.0 | n/a | -8.6 | 2.9 | 1.0 | 0 |
| 15 | AVAXUSDT | 0% | 0.0 | n/a | 14.6 | 5.2 | 7.1 | 0 |
| 16 | UNIUSDT | 0% | 0.0 | n/a | -37.0 | -1.1 | 1.8 | 0 |
| 17 | SHIBUSDT | 0% | 0.0 | n/a | -41.9 | 0.0 | 7.2 | 0 |
| 18 | JSTUSDT | 0% | 0.0 | n/a | 4.5 | 0.5 | 2.0 | 0 |
| 19 | ICPUSDT | 0% | 0.0 | n/a | -41.6 | 0.0 | 4.2 | 0 |
| 20 | ALGOUSDT | 0% | 0.0 | n/a | -3.8 | 1.8 | 11.6 | 0 |
| 21 | ATOMUSDT | 0% | 0.0 | n/a | 36.8 | -1.2 | 1.7 | 0 |
| 22 | INJUSDT | 0% | 0.0 | n/a | 44.0 | -2.8 | 5.7 | 0 |
| 23 | STXUSDT | 0% | 0.0 | n/a | 105.8 | 0.0 | -2.9 | 0 |
| 24 | FILUSDT | 0% | 0.0 | n/a | -67.5 | 0.0 | 8.7 | 0 |
| 25 | DASHUSDT | 0% | 0.0 | n/a | -20.4 | 5.0 | 0.8 | 0 |
| 26 | TRXUSDT | 0% | -0.1 | n/a | 54.0 | -1.0 | -0.1 | 0 |
| 27 | ETCUSDT | 0% | -0.3 | n/a | 34.4 | -7.8 | 5.6 | 0 |
| 28 | HBARUSDT | 0% | -0.5 | n/a | 26.6 | 0.5 | 6.9 | 0 |
| 29 | DOGEUSDT | 0% | -3.6 | n/a | 156.4 | -9.5 | 1.9 | 0 |
| 30 | VETUSDT | 0% | -3.8 | n/a | 53.1 | -12.5 | -2.8 | 0 |
| 31 | ETHUSDT | 0% | -4.8 | n/a | 13.4 | -8.0 | 2.3 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [volume_climax_rejection__broad__max-income__v002.md](symbols/broad/volume_climax_rejection__broad__max-income__v002.md) | 2.1 | 3.1 | 2.1 | -9.4 | 61.9 | 231/272 |
| broad | balanced | [volume_climax_rejection__broad__balanced__v002.md](symbols/broad/volume_climax_rejection__broad__balanced__v002.md) | 0.6 | 1.8 | 0.6 | -1.7 | 77.4 | 31/34 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 15,264 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
