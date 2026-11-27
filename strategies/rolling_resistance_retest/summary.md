# rolling_resistance_retest: optimization summary

Updated 2026-11-26T01:41:39Z · backtest.py version `629aa0a90b` · 12,880 parameter sets tested with this version (12,880 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rolling_resistance_retest__max-income__v001.md](rolling_resistance_retest__max-income__v001.md) | 12880 | `{"max_candles": 78, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | flat (data up to 2026-11-25 16:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 361.95 | 68.36 |
| return % | 3.62 | 0.68 |
| return %/year | 0.6 | 0.2 |
| gross profit | 7,840.70 | 1,517.44 |
| gross loss | 7,478.75 | 1,449.07 |
| trades | 27 | 7 |
| win rate % | 44.4 | 42.9 |
| avg win | 653.39 | 505.81 |
| avg loss | -498.58 | -362.27 |
| avg result / trade | 13.41 | 9.77 |
| largest single loss | -1,036.86 | -444.17 |
| largest loss % of equity | -9.41 | -3.86 |
| max drawdown | -2,220.84 | -1,918.01 |
| max drawdown % | -17.65 | -16.00 |
| profit factor | 1.05 | 1.05 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 7.7 | 6.7 |
| time in market % | 2.3 | 1.1 |
| buy & hold return % | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.40 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | 0.0 |
| 2019 | -1.3 |
| 2020 | 11.7 |
| 2021 | 5.3 |
| 2022 | -0.6 |
| 2023 | -10.1 |
| 2024 (OOS) | 0.7 |
| 2025 (OOS) | 0.0 |
| 2026 (OOS) | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.6% from a peak in-sample and 16.0% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 44 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.6% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 57% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 255 | `{"max_candles": 96, "n": 40, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 431.77 | 0.7 | -26.6 | 40.7 | 329.37 | 1.1 | -19.6 | 1.57 | 27/10 | 0.43 |
| 258 | `{"max_candles": 96, "n": 45, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 431.77 | 0.7 | -26.6 | 40.7 | 198.02 | 0.7 | -17.0 | 0.94 | 27/7 | 0.57 |
| 1272 | `{"max_candles": 78, "n": 40, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 106.00 | 0.4 | -18.6 | 0.62 | 27/10 | not checked |
| 1276 | `{"max_candles": 69, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 68.36 | 0.2 | -16.0 | 0.40 | 27/7 | not checked |
| 1277 | `{"max_candles": 87, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 68.36 | 0.2 | -16.0 | 0.40 | 27/7 | not checked |
| 1278 | `{"max_candles": 78, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 68.36 | 0.2 | -16.0 | 0.40 | 27/7 | 0.75 |
| 1759 | `{"max_candles": 60, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 68.36 | 0.2 | -16.0 | 0.40 | 27/7 | not checked |
| 2245 | `{"max_candles": 87, "n": 40, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 106.00 | 0.4 | -18.6 | 0.62 | 27/10 | not checked |
| 2739 | `{"max_candles": 69, "n": 40, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 106.00 | 0.4 | -18.6 | 0.62 | 27/10 | not checked |
| 5265 | `{"max_candles": 96, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 68.36 | 0.2 | -16.0 | 0.40 | 27/7 | not checked |
| 8117 | `{"max_candles": 51, "n": 40, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 106.00 | 0.4 | -18.6 | 0.62 | 27/10 | not checked |
| 8611 | `{"max_candles": 60, "n": 40, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 106.00 | 0.4 | -18.6 | 0.62 | 27/10 | not checked |
| 9629 | `{"max_candles": 51, "n": 45, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 68.36 | 0.2 | -16.0 | 0.40 | 27/7 | not checked |
| 9761 | `{"max_candles": 96, "n": 40, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 361.95 | 0.6 | -17.6 | 44.4 | 106.00 | 0.4 | -18.6 | 0.62 | 27/10 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XRPUSDT | 89% | 4.8 | 17.5 | 5.0 | 6.4 | 11.3 | 34 |
| 2 | TRXUSDT | 77% | 2.7 | 17.8 | 54.0 | 1.9 | 6.1 | 44 |
| 3 | DASHUSDT | 61% | 5.8 | 21.3 | -20.4 | 5.2 | 2.2 | 11 |
| 4 | BCHUSDT | 39% | 0.1 | 12.7 | 2.9 | -2.2 | -3.2 | 0 |
| 5 | XLMUSDT | 39% | -0.9 | 16.8 | -11.6 | -4.0 | 0.5 | 22 |
| 6 | ETCUSDT | 32% | 4.2 | 19.7 | 34.4 | 5.6 | -9.9 | 0 |
| 7 | JSTUSDT | 24% | 12.9 | 39.1 | 4.5 | -0.2 | -9.6 | 0 |
| 8 | BTCUSDT | 24% | -1.5 | 2.9 | 27.1 | -3.3 | 1.7 | 11 |
| 9 | DOGEUSDT | 18% | 5.1 | 29.9 | 156.4 | 0.0 | 11.5 | 8 |
| 10 | VETUSDT | 16% | -4.9 | 9.0 | 53.1 | -12.2 | -0.6 | 5 |
| 11 | ADAUSDT | 13% | -5.7 | 8.0 | 45.0 | -1.4 | 7.8 | 6 |
| 12 | UNIUSDT | 10% | 1.4 | 5.0 | -37.0 | 5.9 | 9.0 | 3 |
| 13 | LTCUSDT | 8% | -5.3 | 1.8 | -8.6 | -10.9 | -6.0 | 0 |
| 14 | SOLUSDT | 6% | -6.0 | 4.7 | 214.4 | -9.3 | -1.8 | 1 |
| 15 | NEARUSDT | 5% | -1.4 | 2.3 | -15.6 | -5.3 | -2.7 | 1 |
| 16 | BNBUSDT | 5% | -4.6 | 4.7 | 74.8 | -8.0 | -4.5 | 3 |
| 17 | ZECUSDT | 3% | -7.9 | 4.8 | -11.3 | -6.3 | 19.9 | 2 |
| 18 | AVAXUSDT | 3% | -9.3 | 4.3 | 14.6 | -7.7 | 7.6 | 2 |
| 19 | ETHUSDT | 2% | -4.6 | 0.6 | 13.4 | -5.3 | -4.9 | 1 |
| 20 | ATOMUSDT | 2% | -9.3 | 7.1 | 36.8 | -14.1 | 8.4 | 1 |
| 21 | INJUSDT | 0% | 11.3 | n/a | 44.0 | 2.1 | -6.8 | 0 |
| 22 | ALGOUSDT | 0% | -6.9 | n/a | -3.8 | -12.2 | 0.9 | 0 |
| 23 | ICPUSDT | 0% | -7.3 | n/a | -41.6 | -8.5 | 3.6 | 0 |
| 24 | AAVEUSDT | 0% | -8.7 | n/a | -36.5 | -15.2 | 9.3 | 0 |
| 25 | STXUSDT | 0% | -8.9 | n/a | 105.8 | -11.3 | -12.1 | 0 |
| 26 | LINKUSDT | 0% | -10.1 | n/a | 37.9 | -16.8 | -1.3 | 0 |
| 27 | SHIBUSDT | 0% | -10.2 | n/a | -41.9 | -6.8 | 1.7 | 0 |
| 28 | FILUSDT | 0% | -10.6 | n/a | -67.5 | -5.6 | -7.7 | 0 |
| 29 | DOTUSDT | 0% | -11.2 | n/a | -20.7 | -15.0 | 0.7 | 0 |
| 30 | HBARUSDT | 0% | -12.5 | n/a | 26.6 | -17.6 | -2.7 | 0 |
| 31 | CAKEUSDT | 0% | -14.8 | n/a | -48.5 | -14.5 | -5.5 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [rolling_resistance_retest__broad__max-income__v002.md](symbols/broad/rolling_resistance_retest__broad__max-income__v002.md) | 9.1 | 3.0 | 3.0 | -11.1 | 29.8 | 1222/941 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 12,880 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
