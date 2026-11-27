# weekly_high_with_daily_trigger: optimization summary

Updated 2026-11-26T00:53:33Z · backtest.py version `d0055b4125` · 39,629 parameter sets tested with this version (39,629 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [weekly_high_with_daily_trigger__max-income__v002.md](weekly_high_with_daily_trigger__max-income__v002.md) | 39627 | `{"max_candles": 36, "stop_atr": 1.75, "take_profit_atr": 8.5, "weeks": 6}` | flat (data up to 2026-11-24 00:00) |
| balanced | [weekly_high_with_daily_trigger__balanced__v002.md](weekly_high_with_daily_trigger__balanced__v002.md) | 39628 | `{"max_candles": 36, "stop_atr": 1.25, "take_profit_atr": 8.0, "weeks": 6}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [weekly_high_with_daily_trigger__safe-starter__v002.md](weekly_high_with_daily_trigger__safe-starter__v002.md) | 39629 | `{"max_candles": 36, "stop_atr": 1.25, "take_profit_atr": 9.0, "weeks": 6}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 88,696.64 | 4,331.17 | 65,232.44 | 3,617.64 | 53,690.69 | 3,182.80 |
| return % | 886.97 | 43.31 | 652.32 | 36.18 | 536.91 | 31.83 |
| return %/year | 51.1 | 13.2 | 43.9 | 11.3 | 39.6 | 10.0 |
| gross profit | 126,230.57 | 9,542.91 | 92,809.77 | 9,257.76 | 78,902.29 | 8,986.82 |
| gross loss | 37,533.93 | 5,211.74 | 27,577.33 | 5,640.12 | 25,211.60 | 5,804.01 |
| trades | 27 | 15 | 31 | 17 | 30 | 17 |
| win rate % | 59.3 | 46.7 | 48.4 | 35.3 | 46.7 | 35.3 |
| avg win | 7,889.41 | 1,363.27 | 6,187.32 | 1,542.96 | 5,635.88 | 1,497.80 |
| avg loss | -3,412.18 | -651.47 | -1,723.58 | -512.74 | -1,575.73 | -527.64 |
| avg result / trade | 3,285.06 | 288.74 | 2,104.27 | 212.80 | 1,789.69 | 187.22 |
| largest single loss | -6,275.92 | -810.20 | -3,405.72 | -687.09 | -3,031.92 | -704.03 |
| largest loss % of equity | -9.49 | -5.35 | -7.93 | -6.09 | -6.86 | -6.09 |
| max drawdown | -17,649.84 | -3,695.54 | -10,441.25 | -3,898.90 | -10,141.91 | -4,098.33 |
| max drawdown % | -30.68 | -21.32 | -21.38 | -24.51 | -21.38 | -24.51 |
| profit factor | 3.36 | 1.83 | 3.37 | 1.64 | 3.13 | 1.55 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 14.8 | 10.3 | 10.4 | 7.8 | 9.8 | 7.8 |
| time in market % | 26.2 | 26.5 | 22.4 | 19.8 | 22.5 | 20.9 |
| buy & hold return % | 547.53 | 44.90 | 547.53 | 44.90 | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |  | 0.26 |  | 0.25 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -7.7 | -5.6 | -5.6 |
| 2019 | 62.5 | 57.3 | 28.8 |
| 2020 | 223.4 | 142.4 | 155.7 |
| 2021 | 54.2 | 47.0 | 65.3 |
| 2022 | -12.6 | -9.3 | -9.3 |
| 2023 | 51.0 | 56.7 | 36.8 |
| 2024 (OOS) | 40.2 | 28.7 | 46.9 |
| 2025 (OOS) | 7.1 | 9.6 | 9.6 |
| 2026 (OOS) | -4.5 | -3.4 | -11.0 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 30.7% from a peak in-sample and 21.3% out-of-sample, and the worst single trade cost 5.3% of the account out-of-sample. About 59 of every 100 trades won in-sample. Out-of-sample it earned 13.2% a year against 51.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 33% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 21.4% from a peak in-sample and 24.5% out-of-sample, and the worst single trade cost 6.1% of the account out-of-sample. About 48 of every 100 trades won in-sample. Out-of-sample it earned 11.3% a year against 43.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 21.4% from a peak in-sample and 24.5% out-of-sample, and the worst single trade cost 6.1% of the account out-of-sample. About 47 of every 100 trades won in-sample. Out-of-sample it earned 10.0% a year against 39.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 39080 | `{"max_candles": 36, "stop_atr": 1.75, "take_profit_atr": 8.5, "weeks": 6}` | 88,696.64 | 51.1 | -30.7 | 59.3 | 4,331.17 | 13.2 | -21.3 | 0.26 | 27/15 | 1.00 |
| 39291 | `{"max_candles": 30, "stop_atr": 1.75, "take_profit_atr": 9.5, "weeks": 7}` | 75,028.35 | 47.1 | -28.5 | 58.6 | 5,231.09 | 15.7 | -18.0 | 0.33 | 29/14 | not checked |
| 39500 | `{"max_candles": 36, "stop_atr": 1.25, "take_profit_atr": 10.0, "weeks": 6}` | 67,683.66 | 44.7 | -21.4 | 48.3 | 3,840.31 | 11.9 | -24.5 | 0.27 | 29/17 | not checked |
| 824 | `{"max_candles": 96, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 1310 | `{"max_candles": 66, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 7713 | `{"max_candles": 36, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 9012 | `{"max_candles": 48, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 9967 | `{"max_candles": 54, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 11277 | `{"max_candles": 90, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 13913 | `{"max_candles": 72, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 14663 | `{"max_candles": 30, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 20638 | `{"max_candles": 78, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 24463 | `{"max_candles": 42, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 27814 | `{"max_candles": 84, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 30233 | `{"max_candles": 60, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 38963 | `{"max_candles": 114, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 39015 | `{"max_candles": 102, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |
| 39170 | `{"max_candles": 108, "stop_atr": 1.5, "take_profit_atr": 2.0, "weeks": 25}` | 10,275.91 | 13.6 | -20.7 | 64.0 | 1,116.78 | 3.7 | -11.6 | 0.28 | 25/12 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

29 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | BTCUSDT | 60% | 22.6 | 60.6 | 40.0 | 7.1 | -6.1 | 17 |
| 2 | BNBUSDT | 58% | 29.7 | 87.8 | 85.8 | 12.5 | -0.6 | 12 |
| 3 | ETHUSDT | 54% | 15.2 | 48.7 | 31.8 | 15.6 | -3.8 | 16 |
| 4 | ADAUSDT | 37% | 16.7 | 98.0 | 71.3 | 9.8 | -11.7 | 2 |
| 5 | VETUSDT | 31% | 19.7 | 93.9 | 38.6 | 19.8 | 24.0 | 9 |
| 6 | LTCUSDT | 19% | -3.7 | 18.0 | 3.9 | -2.6 | 10.1 | 3 |
| 7 | ETCUSDT | 15% | 23.0 | 77.2 | 24.9 | -5.3 | -15.5 | 1 |
| 8 | LINKUSDT | 13% | 9.5 | 53.0 | 50.7 | -13.2 | -1.1 | 1 |
| 9 | TRXUSDT | 9% | -7.1 | 32.7 | 34.3 | -6.9 | -5.6 | 6 |
| 10 | STXUSDT | 6% | 45.8 | 38.0 | 71.6 | 41.6 | -11.2 | 0 |
| 11 | XRPUSDT | 6% | 0.5 | 17.7 | 15.2 | 7.2 | -1.8 | 3 |
| 12 | ALGOUSDT | 4% | 24.6 | 40.4 | 5.0 | 19.1 | 38.8 | 2 |
| 13 | DOGEUSDT | 4% | 16.9 | 31.9 | 165.4 | 1.9 | -2.0 | 2 |
| 14 | HBARUSDT | 1% | 11.5 | 5.1 | 22.5 | -18.9 | 4.7 | 0 |
| 15 | ATOMUSDT | 1% | -3.7 | 8.0 | 21.4 | -6.7 | -15.8 | 0 |
| 16 | ZECUSDT | 1% | -20.4 | 15.3 | -11.6 | -30.5 | 101.7 | 1 |
| 17 | XLMUSDT | 1% | -20.7 | 4.1 | 4.9 | -24.7 | 3.2 | 0 |
| 18 | SOLUSDT | 0% | 42.9 | n/a | 40.8 | 47.9 | -3.2 | 0 |
| 19 | INJUSDT | 0% | 40.6 | n/a | 75.0 | -10.6 | -25.7 | 0 |
| 20 | AVAXUSDT | 0% | 17.1 | n/a | 68.8 | 26.1 | 11.1 | 0 |
| 21 | DOTUSDT | 0% | 2.5 | n/a | -32.1 | -7.8 | -9.0 | 0 |
| 22 | NEARUSDT | 0% | 0.2 | n/a | 13.7 | 13.6 | 25.4 | 0 |
| 23 | AAVEUSDT | 0% | -0.3 | n/a | -41.0 | 5.7 | 7.3 | 0 |
| 24 | CAKEUSDT | 0% | -2.3 | n/a | -48.0 | -3.6 | 1.7 | 0 |
| 25 | JSTUSDT | 0% | -2.5 | n/a | -26.7 | -0.4 | 10.7 | 0 |
| 26 | FILUSDT | 0% | -5.5 | n/a | -61.2 | 20.7 | -21.9 | 0 |
| 27 | BCHUSDT | 0% | -8.3 | n/a | 5.2 | -3.4 | 11.4 | 0 |
| 28 | UNIUSDT | 0% | -8.3 | n/a | -31.7 | -19.7 | -10.9 | 0 |
| 29 | DASHUSDT | 0% | -19.5 | n/a | -27.1 | -32.0 | 35.1 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [weekly_high_with_daily_trigger__broad__max-income__v002.md](symbols/broad/weekly_high_with_daily_trigger__broad__max-income__v002.md) | 39.1 | 18.1 | 18.1 | -33.9 | 52.4 | 504/378 |
| broad | balanced | [weekly_high_with_daily_trigger__broad__balanced__v002.md](symbols/broad/weekly_high_with_daily_trigger__broad__balanced__v002.md) | 11.4 | 6.4 | 6.4 | -8.3 | 56.6 | 235/166 |
| broad | safe-starter | [weekly_high_with_daily_trigger__broad__safe-starter__v002.md](symbols/broad/weekly_high_with_daily_trigger__broad__safe-starter__v002.md) | 2.8 | 3.4 | 2.8 | -11.4 | 11.0 | 408/301 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 39,629 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
