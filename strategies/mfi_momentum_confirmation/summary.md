# mfi_momentum_confirmation: optimization summary

Updated 2026-11-26T04:55:53Z · backtest.py version `bd5de2f5c1` · 36,583 parameter sets tested with this version (36,583 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [mfi_momentum_confirmation__max-income__v001.md](mfi_momentum_confirmation__max-income__v001.md) | 36581 | `{"level": 75.0, "max_candles": 33, "stop_atr": 2.5, "take_profit_atr": 6.5}` | flat (data up to 2026-11-26 00:00) |
| balanced | [mfi_momentum_confirmation__balanced__v001.md](mfi_momentum_confirmation__balanced__v001.md) | 36582 | `{"level": 87.5, "max_candles": 78, "stop_atr": 2.25, "take_profit_atr": 3.0}` | flat (data up to 2026-11-26 00:00) |
| safe-starter | [mfi_momentum_confirmation__safe-starter__v001.md](mfi_momentum_confirmation__safe-starter__v001.md) | 36583 | `{"level": 87.5, "max_candles": 96, "stop_atr": 1.0, "take_profit_atr": 2.5}` | flat (data up to 2026-11-26 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 13,339.94 | 1,188.24 | 9,109.44 | 2,753.85 | 2,484.63 | 1,371.80 |
| return % | 133.40 | 11.88 | 91.09 | 27.54 | 24.85 | 13.72 |
| return %/year | 15.4 | 4.0 | 11.6 | 8.8 | 3.8 | 4.5 |
| gross profit | 51,005.71 | 12,027.06 | 14,452.72 | 4,739.14 | 6,852.50 | 2,687.14 |
| gross loss | 37,665.77 | 10,838.81 | 5,343.28 | 1,985.30 | 4,367.87 | 1,315.34 |
| trades | 80 | 40 | 28 | 12 | 29 | 12 |
| win rate % | 48.8 | 35.0 | 64.3 | 66.7 | 41.4 | 50.0 |
| avg win | 1,307.84 | 859.08 | 802.93 | 592.39 | 571.04 | 447.86 |
| avg loss | -918.68 | -416.88 | -534.33 | -496.32 | -256.93 | -219.22 |
| avg result / trade | 166.75 | 29.71 | 325.34 | 229.49 | 85.68 | 114.32 |
| largest single loss | -3,290.06 | -783.30 | -962.84 | -670.45 | -326.31 | -274.67 |
| largest loss % of equity | -10.83 | -5.38 | -5.57 | -4.99 | -2.88 | -2.39 |
| max drawdown | -10,024.44 | -4,533.90 | -2,213.50 | -1,182.96 | -1,255.45 | -524.13 |
| max drawdown % | -32.36 | -28.84 | -12.80 | -8.77 | -10.52 | -5.03 |
| profit factor | 1.35 | 1.11 | 2.71 | 2.39 | 1.57 | 2.04 |
| unusually bad trades | 9 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 6.7 | 7.4 | 7.9 | 8.1 | 5.0 | 4.0 |
| time in market % | 8.8 | 8.6 | 2.0 | 1.3 | 0.7 | 0.6 |
| buy & hold return % | 110.38 | -25.03 | 110.38 | -25.03 | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |  | 0.76 |  | 1.19 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | 17.8 | 0.9 | -8.1 |
| 2019 | 23.5 | 3.5 | 5.8 |
| 2020 | 73.8 | 36.4 | 4.3 |
| 2021 | -16.2 | 7.0 | 6.3 |
| 2022 | 0.5 | 16.4 | 15.0 |
| 2023 | 9.6 | 7.7 | 0.6 |
| 2024 (OOS) | 20.5 | 19.4 | 4.5 |
| 2025 (OOS) | 14.4 | 6.8 | 7.6 |
| 2026 (OOS) | -18.8 | 0.0 | 1.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 32.4% from a peak in-sample and 28.8% out-of-sample, and the worst single trade cost 5.4% of the account out-of-sample. About 49 of every 100 trades won in-sample. Out-of-sample it earned 4.0% a year against 15.4% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 31% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 12.8% from a peak in-sample and 8.8% out-of-sample, and the worst single trade cost 5.0% of the account out-of-sample. About 64 of every 100 trades won in-sample. With 100% of equity per trade; about 78% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 10.5% from a peak in-sample and 5.0% out-of-sample, and the worst single trade cost 2.4% of the account out-of-sample. About 41 of every 100 trades won in-sample. With 100% of equity per trade; about 95% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 16477 | `{"level": 75.0, "max_candles": 33, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 13,339.94 | 15.4 | -32.4 | 48.8 | 1,188.24 | 4.0 | -28.8 | 0.26 | 80/40 | 1.00 |
| 23054 | `{"level": 75.0, "max_candles": 33, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 11,320.73 | 13.7 | -30.1 | 46.3 | 1,093.07 | 3.6 | -28.9 | 0.27 | 82/40 | not checked |
| 1237 | `{"level": 80.0, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 11,063.10 | 13.4 | -25.9 | 54.2 | 4,354.85 | 13.3 | -18.4 | 0.99 | 59/23 | 0.83 |
| 27123 | `{"level": 80.0, "max_candles": 24, "stop_atr": 4.5, "take_profit_atr": 5.5}` | 10,523.09 | 12.9 | -25.1 | 54.2 | 4,354.85 | 13.3 | -18.4 | 1.03 | 59/23 | not checked |
| 12979 | `{"level": 87.5, "max_candles": 78, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | 1.00 |
| 12990 | `{"level": 87.5, "max_candles": 69, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 12991 | `{"level": 87.5, "max_candles": 87, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 14097 | `{"level": 87.5, "max_candles": 51, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 15399 | `{"level": 87.5, "max_candles": 60, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 17137 | `{"level": 87.5, "max_candles": 42, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 24757 | `{"level": 87.5, "max_candles": 33, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 27094 | `{"level": 87.5, "max_candles": 96, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 31737 | `{"level": 87.5, "max_candles": 114, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 32293 | `{"level": 87.5, "max_candles": 105, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 9,109.44 | 11.6 | -12.8 | 64.3 | 2,753.85 | 8.8 | -8.8 | 0.76 | 28/12 | not checked |
| 13082 | `{"level": 87.5, "max_candles": 96, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 13571 | `{"level": 87.5, "max_candles": 60, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 16133 | `{"level": 87.5, "max_candles": 78, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 18601 | `{"level": 87.5, "max_candles": 42, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 18777 | `{"level": 87.5, "max_candles": 51, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 18994 | `{"level": 87.5, "max_candles": 87, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 23591 | `{"level": 87.5, "max_candles": 69, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 24355 | `{"level": 87.5, "max_candles": 24, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 26451 | `{"level": 87.5, "max_candles": 33, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 27728 | `{"level": 87.5, "max_candles": 114, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |
| 33191 | `{"level": 87.5, "max_candles": 105, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 3,746.80 | 5.5 | -10.5 | 41.4 | 1,991.23 | 6.5 | -5.0 | 1.17 | 29/12 | not checked |

(13 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SOLUSDT | 67% | 8.6 | 64.8 | 214.4 | 0.6 | -12.7 | 5 |
| 2 | ETHUSDT | 67% | 2.7 | 19.8 | 13.4 | 1.3 | -19.1 | 15 |
| 3 | DOGEUSDT | 66% | 10.4 | 66.8 | 156.4 | -1.7 | -7.3 | 20 |
| 4 | ADAUSDT | 66% | 5.3 | 31.6 | 45.0 | 3.5 | -14.1 | 18 |
| 5 | ETCUSDT | 59% | 3.3 | 37.0 | 34.4 | -13.0 | -2.4 | 3 |
| 6 | XRPUSDT | 52% | 4.8 | 32.0 | 5.0 | -0.4 | -17.4 | 3 |
| 7 | TRXUSDT | 47% | 0.6 | 37.9 | 54.0 | -3.5 | -4.2 | 4 |
| 8 | BNBUSDT | 45% | 0.1 | 21.8 | 74.8 | 2.9 | -4.6 | 4 |
| 9 | XLMUSDT | 44% | -0.8 | 27.2 | -11.6 | -13.6 | 1.4 | 26 |
| 10 | VETUSDT | 42% | -1.5 | 24.0 | 53.1 | -13.1 | 8.7 | 9 |
| 11 | AVAXUSDT | 41% | -4.5 | 44.8 | 14.6 | -7.8 | -19.7 | 3 |
| 12 | AAVEUSDT | 38% | -2.7 | 19.6 | -36.5 | 1.3 | 5.5 | 9 |
| 13 | BTCUSDT | 36% | -0.7 | 6.5 | 27.1 | 1.7 | -8.9 | 5 |
| 14 | JSTUSDT | 34% | -3.4 | 27.3 | 4.5 | -25.6 | -0.7 | 5 |
| 15 | LTCUSDT | 31% | -4.4 | 9.4 | -8.6 | -3.8 | -8.9 | 6 |
| 16 | BCHUSDT | 28% | -6.8 | 30.2 | 2.9 | -11.7 | 0.7 | 4 |
| 17 | NEARUSDT | 25% | -4.1 | 23.1 | -15.6 | -39.1 | 14.6 | 10 |
| 18 | LINKUSDT | 23% | -4.2 | 22.4 | 37.9 | -21.2 | -14.8 | 6 |
| 19 | DASHUSDT | 23% | -8.2 | 21.9 | -20.4 | -29.5 | -12.2 | 5 |
| 20 | INJUSDT | 23% | -12.0 | 41.3 | 44.0 | 32.1 | -26.4 | 1 |
| 21 | ZECUSDT | 22% | -5.7 | 23.3 | -11.3 | -7.4 | 51.6 | 6 |
| 22 | ICPUSDT | 20% | -1.4 | 52.2 | -41.6 | 3.0 | -9.6 | 6 |
| 23 | STXUSDT | 14% | -12.9 | 16.0 | 105.8 | -18.0 | -0.6 | 2 |
| 24 | ALGOUSDT | 12% | -11.2 | 25.2 | -3.8 | -11.4 | 24.8 | 4 |
| 25 | FILUSDT | 11% | -4.7 | 14.9 | -67.5 | -0.5 | -9.9 | 0 |
| 26 | SHIBUSDT | 11% | -5.6 | 14.0 | -41.9 | 1.1 | 7.5 | 4 |
| 27 | CAKEUSDT | 9% | -7.4 | 25.3 | -48.5 | -12.2 | 3.3 | 1 |
| 28 | ATOMUSDT | 9% | -10.0 | 13.4 | 36.8 | -17.9 | 9.3 | 1 |
| 29 | HBARUSDT | 9% | -13.9 | 16.4 | 26.6 | -14.4 | 7.0 | 1 |
| 30 | UNIUSDT | 2% | -13.6 | 0.9 | -37.0 | -15.8 | -20.6 | 0 |
| 31 | DOTUSDT | 0% | -15.9 | n/a | -20.7 | -23.5 | -8.3 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [mfi_momentum_confirmation__broad__max-income__v002.md](symbols/broad/mfi_momentum_confirmation__broad__max-income__v002.md) | 6.0 | 4.1 | 4.1 | -14.7 | 41.8 | 796/572 |
| broad | balanced | [mfi_momentum_confirmation__broad__balanced__v002.md](symbols/broad/mfi_momentum_confirmation__broad__balanced__v002.md) | 4.5 | 2.3 | 2.3 | -6.5 | 45.4 | 361/265 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 36,583 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
