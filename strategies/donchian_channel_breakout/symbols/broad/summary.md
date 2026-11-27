# donchian_channel_breakout__broad: optimization summary

Updated 2026-11-26T00:02:15Z · backtest.py version `39d8ffecaf` · 1,371 parameter sets tested with this version (1,371 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [donchian_channel_breakout__broad__max-income__v002.md](donchian_channel_breakout__broad__max-income__v002.md) | 1370 | `{"exit_n": 20, "max_candles": 37, "n": 22, "stop_atr": 3.25, "take_profit_atr": 7.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [donchian_channel_breakout__broad__balanced__v002.md](donchian_channel_breakout__broad__balanced__v002.md) | 1371 | `{"exit_n": 15, "max_candles": 6, "n": 52, "stop_atr": 2.5, "take_profit_atr": 8.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [donchian_channel_breakout__broad__safe-starter__v001.md](donchian_channel_breakout__broad__safe-starter__v001.md) | 476 | `{"exit_n": 10, "max_candles": 78, "n": 65, "stop_atr": 3.0, "take_profit_atr": 3.5}` | long JSTUSDT since 2026-11-10 00:00 @ 0.145185 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 71,619.90 | 4,930.08 | 13,182.22 | 2,368.06 | 8,584.67 | 2,937.66 |
| return % | 716.20 | 49.30 | 131.82 | 23.68 | 85.85 | 29.38 |
| return %/year | 46.0 | 14.8 | 16.4 | 7.6 | 11.8 | 9.3 |
| gross profit | 131,153.98 | 22,730.70 | 29,231.43 | 9,971.57 | 25,805.82 | 11,868.35 |
| gross loss | 59,534.08 | 17,800.62 | 16,049.21 | 7,603.52 | 17,221.15 | 8,930.69 |
| trades | 606 | 463 | 633 | 431 | 454 | 298 |
| win rate % | 49.3 | 41.0 | 50.9 | 44.1 | 51.8 | 50.7 |
| avg win | 438.64 | 119.64 | 90.78 | 52.48 | 109.81 | 78.60 |
| avg loss | -193.92 | -65.20 | -51.61 | -31.55 | -78.64 | -60.75 |
| avg result / trade | 118.18 | 10.65 | 20.82 | 5.49 | 18.91 | 9.86 |
| largest single loss | -3,881.89 | -1,196.30 | -404.17 | -182.69 | -446.69 | -528.81 |
| largest loss % of equity | -14.62 | -25.68 | -20.74 | -15.88 | -16.79 | -21.69 |
| max drawdown | -14,840.11 | -5,034.49 | -1,508.47 | -1,421.85 | -2,983.94 | -1,955.98 |
| max drawdown % | -21.14 | -38.61 | -11.90 | -13.32 | -16.87 | -15.80 |
| profit factor | 2.20 | 1.28 | 1.82 | 1.31 | 1.50 | 1.33 |
| unusually bad trades | 7 | 5 | 53 | 40 | 1 | 1 |
| … threshold (% of equity) | 32.0 | 31.2 | 17.1 | 14.6 | 32.9 | 30.2 |
| time in market % | 21.3 | 30.9 | 5.8 | 7.5 | 8.4 | 10.4 |
| buy & hold return % | 368.58 | 81.24 | 368.58 | 81.24 | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.32 |  | 0.47 |  | 0.79 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -1.4 | -0.1 | 0.0 |
| 2019 | 11.3 | 2.0 | 4.8 |
| 2020 | 49.3 | 13.8 | 10.0 |
| 2021 | 208.5 | 52.0 | 45.7 |
| 2022 | 0.7 | 1.4 | -3.4 |
| 2023 | 60.5 | 29.8 | 14.7 |
| 2024 (OOS) | -0.5 | 14.0 | 4.2 |
| 2025 (OOS) | 10.2 | 1.1 | 3.1 |
| 2026 (OOS) | -14.4 | -1.9 | -0.9 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 21.1% from a peak in-sample and 38.6% out-of-sample, and the worst single trade cost 25.7% of the account out-of-sample. About 49 of every 100 trades won in-sample. Out-of-sample it earned 14.8% a year against 46.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 11.9% from a peak in-sample and 13.3% out-of-sample, and the worst single trade cost 15.9% of the account out-of-sample. About 51 of every 100 trades won in-sample. Out-of-sample it earned 7.6% a year against 16.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 75% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 16.9% from a peak in-sample and 15.8% out-of-sample, and the worst single trade cost 21.7% of the account out-of-sample. About 52 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 59% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1247 | `{"exit_n": 20, "max_candles": 37, "n": 22, "stop_atr": 3.5, "take_profit_atr": 7.0}` | 72,119.60 | 46.1 | -21.9 | 50.8 | 4,185.17 | 12.8 | -39.4 | 0.28 | 595/461 | not checked |
| 1248 | `{"exit_n": 20, "max_candles": 37, "n": 22, "stop_atr": 3.25, "take_profit_atr": 7.0}` | 71,619.90 | 46.0 | -21.1 | 49.3 | 4,930.08 | 14.8 | -38.6 | 0.32 | 606/463 | 1.00 |
| 1191 | `{"exit_n": 20, "max_candles": 43, "n": 22, "stop_atr": 3.25, "take_profit_atr": 7.0}` | 65,091.38 | 43.8 | -20.9 | 49.1 | 4,132.81 | 12.7 | -39.3 | 0.29 | 590/460 | not checked |
| 1021 | `{"exit_n": 20, "max_candles": 48, "n": 22, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 62,662.71 | 43.0 | -20.7 | 47.9 | 3,700.17 | 11.5 | -37.1 | 0.27 | 622/473 | not checked |
| 984 | `{"exit_n": 20, "max_candles": 31, "n": 22, "stop_atr": 3.0, "take_profit_atr": 6.5}` | 57,263.32 | 41.0 | -20.4 | 48.9 | 5,563.39 | 16.5 | -36.2 | 0.40 | 644/491 | not checked |
| 982 | `{"exit_n": 15, "max_candles": 31, "n": 22, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 54,322.54 | 39.9 | -19.9 | 49.8 | 5,920.88 | 17.4 | -34.0 | 0.44 | 655/491 | not checked |
| 939 | `{"exit_n": 15, "max_candles": 31, "n": 22, "stop_atr": 3.0, "take_profit_atr": 6.5}` | 53,576.94 | 39.6 | -19.1 | 47.8 | 7,779.03 | 22.0 | -34.1 | 0.56 | 648/495 | not checked |
| 1165 | `{"exit_n": 15, "max_candles": 37, "n": 22, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 51,571.20 | 38.8 | -18.8 | 47.8 | 4,952.29 | 14.9 | -34.0 | 0.39 | 645/489 | not checked |
| 1207 | `{"exit_n": 20, "max_candles": 37, "n": 27, "stop_atr": 3.0, "take_profit_atr": 7.0}` | 45,649.56 | 36.2 | -17.6 | 48.0 | 3,592.42 | 11.2 | -35.0 | 0.31 | 561/431 | not checked |
| 1181 | `{"exit_n": 20, "max_candles": 37, "n": 27, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 36,941.60 | 32.1 | -17.0 | 46.6 | 3,997.44 | 12.3 | -33.8 | 0.38 | 569/435 | not checked |
| 941 | `{"exit_n": 10, "max_candles": 30, "n": 25, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 32,544.19 | 29.8 | -15.9 | 43.7 | 5,718.94 | 16.9 | -28.3 | 0.57 | 631/488 | not checked |
| 965 | `{"exit_n": 20, "max_candles": 24, "n": 25, "stop_atr": 2.25, "take_profit_atr": 6.5}` | 27,458.54 | 26.9 | -14.6 | 44.8 | 2,779.09 | 8.8 | -30.3 | 0.33 | 665/496 | not checked |
| 1130 | `{"exit_n": 30, "max_candles": 7, "n": 52, "stop_atr": 4.5, "take_profit_atr": 10.5}` | 20,816.77 | 22.5 | -13.6 | 51.1 | 2,610.32 | 8.3 | -14.1 | 0.37 | 605/406 | not checked |
| 630 | `{"exit_n": 20, "max_candles": 30, "n": 25, "stop_atr": 1.5, "take_profit_atr": 5.0}` | 17,254.98 | 19.8 | -13.5 | 33.8 | 1,650.93 | 5.4 | -25.8 | 0.27 | 767/553 | not checked |
| 1353 | `{"exit_n": 10, "max_candles": 7, "n": 77, "stop_atr": 4.75, "take_profit_atr": 9.5}` | 15,472.85 | 18.4 | -12.6 | 51.0 | 3,145.62 | 9.9 | -11.1 | 0.54 | 465/325 | not checked |
| 1101 | `{"exit_n": 10, "max_candles": 6, "n": 47, "stop_atr": 2.5, "take_profit_atr": 9.0}` | 14,144.01 | 17.2 | -11.7 | 51.6 | 2,190.87 | 7.1 | -16.2 | 0.41 | 672/451 | not checked |
| 1156 | `{"exit_n": 15, "max_candles": 6, "n": 47, "stop_atr": 2.5, "take_profit_atr": 9.0}` | 14,144.01 | 17.2 | -11.7 | 51.6 | 2,190.10 | 7.1 | -16.2 | 0.41 | 672/451 | not checked |
| 892 | `{"exit_n": 15, "max_candles": 6, "n": 52, "stop_atr": 1.5, "take_profit_atr": 8.5}` | 9,061.14 | 12.3 | -11.0 | 42.0 | 1,949.40 | 6.3 | -11.3 | 0.52 | 664/444 | not checked |
| 1057 | `{"exit_n": 15, "max_candles": 1, "n": 57, "stop_atr": 2.5, "take_profit_atr": 9.0}` | 2,789.81 | 4.5 | -6.9 | 43.3 | 1,357.57 | 4.5 | -4.8 | 0.99 | 856/532 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,371 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
