# donchian_channel_breakout: optimization summary

Updated 2026-11-26T00:02:16Z · backtest.py version `c132114b2c` · 839 parameter sets tested with this version (839 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [donchian_channel_breakout__max-income__v002.md](donchian_channel_breakout__max-income__v002.md) | 838 | `{"exit_n": 25, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [donchian_channel_breakout__balanced__v002.md](donchian_channel_breakout__balanced__v002.md) | 838 | `{"exit_n": 25, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [donchian_channel_breakout__safe-starter__v002.md](donchian_channel_breakout__safe-starter__v002.md) | 839 | `{"exit_n": 15, "max_candles": 36, "n": 45, "stop_atr": 1.5, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 31,705.32 | 2,503.92 | 31,705.32 | 2,503.92 | 14,551.39 | 3,344.95 |
| return % | 317.05 | 25.04 | 317.05 | 25.04 | 145.51 | 33.45 |
| return %/year | 29.4 | 8.0 | 29.4 | 8.0 | 17.6 | 10.5 |
| gross profit | 43,248.24 | 6,880.18 | 43,248.24 | 6,880.18 | 32,513.78 | 8,349.70 |
| gross loss | 11,542.93 | 4,376.25 | 11,542.93 | 4,376.25 | 17,962.39 | 5,004.75 |
| trades | 26 | 15 | 26 | 15 | 36 | 16 |
| win rate % | 53.9 | 33.3 | 53.9 | 33.3 | 38.9 | 43.8 |
| avg win | 3,089.16 | 1,376.04 | 3,089.16 | 1,376.04 | 2,322.41 | 1,192.81 |
| avg loss | -961.91 | -437.63 | -961.91 | -437.63 | -816.47 | -556.08 |
| avg result / trade | 1,219.44 | 166.93 | 1,219.44 | 166.93 | 404.21 | 209.06 |
| largest single loss | -1,658.05 | -577.79 | -1,658.05 | -577.79 | -1,598.51 | -647.76 |
| largest loss % of equity | -6.86 | -4.49 | -6.86 | -4.49 | -8.17 | -4.63 |
| max drawdown | -5,119.28 | -2,338.74 | -5,119.28 | -2,338.74 | -4,687.72 | -2,977.53 |
| max drawdown % | -33.92 | -16.51 | -33.92 | -16.51 | -21.38 | -19.86 |
| profit factor | 3.75 | 1.57 | 3.75 | 1.57 | 1.81 | 1.67 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 11.2 | 8.3 | 11.2 | 8.3 | 11.6 | 10.5 |
| time in market % | 16.9 | 14.7 | 16.9 | 14.7 | 21.1 | 18.4 |
| buy & hold return % | 547.53 | 44.90 | 547.53 | 44.90 | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |  | 0.27 |  | 0.60 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | 0.0 | 0.0 | -6.7 |
| 2019 | 34.5 | 34.5 | 30.5 |
| 2020 | 18.0 | 18.0 | 13.3 |
| 2021 | 91.0 | 91.0 | 59.4 |
| 2022 | -5.4 | -5.4 | -10.9 |
| 2023 | 45.4 | 45.4 | 25.3 |
| 2024 (OOS) | 20.0 | 20.0 | 18.0 |
| 2025 (OOS) | 7.1 | 7.1 | 11.3 |
| 2026 (OOS) | -2.8 | -2.8 | 1.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 33.9% from a peak in-sample and 16.5% out-of-sample, and the worst single trade cost 4.5% of the account out-of-sample. About 54 of every 100 trades won in-sample. Out-of-sample it earned 8.0% a year against 29.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 29% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 33.9% from a peak in-sample and 16.5% out-of-sample, and the worst single trade cost 4.5% of the account out-of-sample. About 54 of every 100 trades won in-sample. Out-of-sample it earned 8.0% a year against 29.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 29% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 21.4% from a peak in-sample and 19.9% out-of-sample, and the worst single trade cost 4.6% of the account out-of-sample. About 39 of every 100 trades won in-sample. Out-of-sample it earned 10.5% a year against 17.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 47% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 376 | `{"exit_n": 25, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | 31,705.32 | 29.4 | -33.9 | 53.9 | 2,503.92 | 8.0 | -16.5 | 0.27 | 26/15 | 1.00 |
| 388 | `{"exit_n": 20, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | 31,705.32 | 29.4 | -33.9 | 53.9 | 2,576.14 | 8.2 | -16.0 | 0.28 | 26/15 | not checked |
| 389 | `{"exit_n": 30, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | 31,705.32 | 29.4 | -33.9 | 53.9 | 2,503.92 | 8.0 | -16.5 | 0.27 | 26/15 | not checked |
| 715 | `{"exit_n": 35, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | 31,705.32 | 29.4 | -33.9 | 53.9 | 2,503.92 | 8.0 | -16.5 | 0.27 | 26/15 | not checked |
| 790 | `{"exit_n": 40, "max_candles": 42, "n": 65, "stop_atr": 1.25, "take_profit_atr": 4.5}` | 31,705.32 | 29.4 | -33.9 | 53.9 | 2,503.92 | 8.0 | -16.5 | 0.27 | 26/15 | not checked |
| 410 | `{"exit_n": 30, "max_candles": 36, "n": 60, "stop_atr": 1.75, "take_profit_atr": 4.5}` | 30,079.96 | 28.4 | -21.5 | 59.3 | 2,704.15 | 8.6 | -15.0 | 0.30 | 27/14 | not checked |
| 486 | `{"exit_n": 25, "max_candles": 36, "n": 60, "stop_atr": 1.75, "take_profit_atr": 4.5}` | 30,079.96 | 28.4 | -21.5 | 59.3 | 2,704.15 | 8.6 | -15.0 | 0.30 | 27/14 | not checked |
| 560 | `{"exit_n": 35, "max_candles": 36, "n": 60, "stop_atr": 1.75, "take_profit_atr": 4.5}` | 30,079.96 | 28.4 | -21.5 | 59.3 | 2,704.15 | 8.6 | -15.0 | 0.30 | 27/14 | not checked |
| 763 | `{"exit_n": 40, "max_candles": 36, "n": 60, "stop_atr": 1.75, "take_profit_atr": 4.5}` | 30,079.96 | 28.4 | -21.5 | 59.3 | 2,704.15 | 8.6 | -15.0 | 0.30 | 27/14 | not checked |
| 526 | `{"exit_n": 15, "max_candles": 36, "n": 40, "stop_atr": 1.25, "take_profit_atr": 5.0}` | 23,482.78 | 24.3 | -21.4 | 40.5 | 2,529.61 | 8.1 | -21.4 | 0.33 | 37/18 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

29 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | BNBUSDT | 98% | 29.9 | 73.5 | 85.8 | 6.5 | 11.7 | 41 |
| 2 | ETHUSDT | 92% | 19.6 | 58.0 | 31.8 | 18.6 | -12.2 | 14 |
| 3 | VETUSDT | 91% | 35.4 | 133.6 | 38.6 | 47.8 | 23.8 | 31 |
| 4 | BTCUSDT | 89% | 13.8 | 31.9 | 40.0 | 1.4 | -5.3 | 10 |
| 5 | ADAUSDT | 88% | 31.2 | 88.7 | 71.3 | 29.9 | -14.5 | 10 |
| 6 | ETCUSDT | 26% | 6.2 | 86.7 | 24.9 | 4.6 | -15.6 | 6 |
| 7 | XRPUSDT | 23% | 4.1 | 17.4 | 15.2 | 12.4 | 7.0 | 6 |
| 8 | LTCUSDT | 22% | -4.7 | 28.1 | 3.9 | -2.5 | -14.4 | 0 |
| 9 | ALGOUSDT | 14% | 22.1 | 37.7 | 5.0 | 10.5 | 2.6 | 5 |
| 10 | TRXUSDT | 12% | -12.0 | 31.0 | 34.3 | -18.4 | 7.2 | 6 |
| 11 | ATOMUSDT | 11% | -0.6 | 18.1 | 21.4 | -12.7 | -11.4 | 0 |
| 12 | XLMUSDT | 9% | -16.7 | 32.5 | 4.9 | -5.8 | 25.4 | 4 |
| 13 | DOGEUSDT | 8% | 1.2 | 31.6 | 165.4 | -14.7 | 9.9 | 4 |
| 14 | LINKUSDT | 8% | -16.9 | 26.9 | 50.7 | -28.3 | -10.2 | 0 |
| 15 | INJUSDT | 6% | 33.4 | 61.1 | 75.0 | 45.4 | -25.6 | 0 |
| 16 | HBARUSDT | 6% | 12.1 | 17.5 | 22.5 | -6.0 | -7.7 | 1 |
| 17 | NEARUSDT | 6% | 8.2 | 51.0 | 13.7 | 15.9 | -4.3 | 0 |
| 18 | SOLUSDT | 5% | 53.0 | 22.2 | 40.8 | 52.8 | -20.2 | 2 |
| 19 | AVAXUSDT | 3% | 25.2 | 33.1 | 68.8 | 45.3 | 27.2 | 0 |
| 20 | STXUSDT | 3% | -5.0 | 40.2 | 71.6 | 9.4 | -17.2 | 0 |
| 21 | BCHUSDT | 2% | -3.1 | 14.7 | 5.2 | 7.6 | -14.9 | 0 |
| 22 | DOTUSDT | 2% | -3.1 | 5.5 | -32.1 | -1.6 | -14.2 | 0 |
| 23 | ZECUSDT | 2% | -24.8 | 3.5 | -11.6 | -21.6 | 69.0 | 1 |
| 24 | FILUSDT | 0% | 12.2 | n/a | -61.2 | 12.8 | -16.9 | 0 |
| 25 | CAKEUSDT | 0% | 6.7 | n/a | -48.0 | -10.3 | 6.3 | 0 |
| 26 | JSTUSDT | 0% | 4.2 | n/a | -26.7 | 0.7 | -11.9 | 0 |
| 27 | AAVEUSDT | 0% | -6.8 | n/a | -41.0 | -15.7 | -9.9 | 0 |
| 28 | UNIUSDT | 0% | -15.0 | n/a | -31.7 | 5.0 | -18.4 | 0 |
| 29 | DASHUSDT | 0% | -24.9 | n/a | -27.1 | -24.9 | 8.0 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [donchian_channel_breakout__broad__max-income__v002.md](symbols/broad/donchian_channel_breakout__broad__max-income__v002.md) | 46.0 | 14.8 | 14.8 | -38.6 | 49.3 | 606/463 |
| broad | balanced | [donchian_channel_breakout__broad__balanced__v002.md](symbols/broad/donchian_channel_breakout__broad__balanced__v002.md) | 16.4 | 7.6 | 7.6 | -13.3 | 50.9 | 633/431 |
| broad | safe-starter | [donchian_channel_breakout__broad__safe-starter__v001.md](symbols/broad/donchian_channel_breakout__broad__safe-starter__v001.md) | 11.8 | 9.3 | 9.3 | -16.9 | 51.8 | 454/298 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 839 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
