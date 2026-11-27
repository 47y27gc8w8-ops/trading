# drawdown_from_recent_high__broad: optimization summary

Updated 2026-11-26T00:05:22Z · backtest.py version `721094815c` · 889 parameter sets tested with this version (889 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [drawdown_from_recent_high__broad__max-income__v002.md](drawdown_from_recent_high__broad__max-income__v002.md) | 887 | `{"dip": 17, "max_candles": 6, "n": 7, "stop_atr": 2.25, "take_profit_atr": 0.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [drawdown_from_recent_high__broad__balanced__v002.md](drawdown_from_recent_high__broad__balanced__v002.md) | 888 | `{"dip": 16, "max_candles": 10, "n": 2, "stop_atr": 2.0, "take_profit_atr": 0.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [drawdown_from_recent_high__broad__safe-starter__v001.md](drawdown_from_recent_high__broad__safe-starter__v001.md) | 889 | `{"dip": 17, "max_candles": 12, "n": 7, "stop_atr": 2.0, "take_profit_atr": 0.5}` | long UNIUSDT since 2026-11-16 00:00 @ 5.188183 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 5,869.41 | 910.49 | 2,182.26 | 322.14 | 5,097.94 | 776.18 |
| return % | 58.69 | 9.10 | 21.82 | 3.22 | 50.98 | 7.76 |
| return %/year | 8.7 | 3.1 | 3.6 | 1.1 | 7.7 | 2.6 |
| gross profit | 9,981.28 | 3,815.64 | 2,374.93 | 471.54 | 9,844.73 | 4,135.53 |
| gross loss | 4,111.87 | 2,905.14 | 192.67 | 149.40 | 4,746.79 | 3,359.35 |
| trades | 387 | 266 | 70 | 23 | 379 | 270 |
| win rate % | 82.2 | 75.6 | 91.4 | 87.0 | 84.2 | 79.6 |
| avg win | 31.39 | 18.98 | 37.11 | 23.58 | 30.86 | 19.24 |
| avg loss | -59.59 | -44.69 | -32.11 | -49.80 | -79.11 | -61.08 |
| avg result / trade | 15.17 | 3.42 | 31.18 | 14.01 | 13.45 | 2.87 |
| largest single loss | -345.78 | -116.96 | -52.92 | -132.78 | -247.49 | -148.84 |
| largest loss % of equity | -29.71 | -25.07 | -9.64 | -29.50 | -26.44 | -27.03 |
| max drawdown | -1,660.79 | -1,011.14 | -364.96 | -205.26 | -1,617.06 | -973.20 |
| max drawdown % | -12.77 | -9.35 | -3.16 | -1.97 | -12.65 | -8.60 |
| profit factor | 2.43 | 1.31 | 12.33 | 3.16 | 2.07 | 1.23 |
| unusually bad trades | 18 | 16 | 1 | 1 | 1 | 1 |
| … threshold (% of equity) | 19.2 | 19.2 | 11.3 | 7.3 | 36.3 | 37.4 |
| time in market % | 1.8 | 2.4 | 0.3 | 0.2 | 2.2 | 3.1 |
| buy & hold return % | 368.58 | 81.24 | 368.58 | 81.24 | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.35 |  | 0.30 |  | 0.34 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | 0.0 | 0.0 | 0.0 |
| 2019 | -0.9 | 0.0 | -2.1 |
| 2020 | 7.0 | 2.8 | 6.2 |
| 2021 | 47.0 | 18.2 | 43.8 |
| 2022 | -2.5 | -0.1 | -3.6 |
| 2023 | 4.4 | 0.4 | 4.7 |
| 2024 (OOS) | 12.9 | 2.1 | 10.5 |
| 2025 (OOS) | -1.0 | 2.1 | -2.0 |
| 2026 (OOS) | -1.3 | -1.1 | -0.7 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 12.8% from a peak in-sample and 9.3% out-of-sample, and the worst single trade cost 25.1% of the account out-of-sample. About 82 of every 100 trades won in-sample. Out-of-sample it earned 3.1% a year against 8.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 78% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 3.2% from a peak in-sample and 2.0% out-of-sample, and the worst single trade cost 29.5% of the account out-of-sample. About 91 of every 100 trades won in-sample. Out-of-sample it earned 1.1% a year against 3.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 12.7% from a peak in-sample and 8.6% out-of-sample, and the worst single trade cost 27.0% of the account out-of-sample. About 84 of every 100 trades won in-sample. Out-of-sample it earned 2.6% a year against 7.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 79% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 377 | `{"dip": 18, "max_candles": 10, "n": 7, "stop_atr": 2.25, "take_profit_atr": 0.5}` | 5,919.84 | 8.7 | -12.5 | 84.8 | 1,087.11 | 3.6 | -8.5 | 0.41 | 336/218 | not checked |
| 408 | `{"dip": 18, "max_candles": 8, "n": 7, "stop_atr": 2.25, "take_profit_atr": 0.5}` | 5,903.84 | 8.7 | -12.5 | 83.5 | 983.74 | 3.3 | -8.5 | 0.38 | 339/219 | not checked |
| 379 | `{"dip": 18, "max_candles": 12, "n": 7, "stop_atr": 2.5, "take_profit_atr": 0.5}` | 5,787.09 | 8.6 | -12.3 | 85.9 | 1,510.56 | 5.0 | -6.3 | 0.58 | 333/212 | not checked |
| 571 | `{"dip": 18, "max_candles": 10, "n": 7, "stop_atr": 2.5, "take_profit_atr": 0.5}` | 5,735.23 | 8.5 | -12.2 | 84.7 | 1,707.44 | 5.6 | -6.3 | 0.66 | 334/213 | not checked |
| 430 | `{"dip": 18, "max_candles": 8, "n": 7, "stop_atr": 2.5, "take_profit_atr": 0.5}` | 5,726.36 | 8.5 | -12.1 | 83.4 | 1,534.28 | 5.1 | -6.3 | 0.59 | 338/214 | not checked |
| 544 | `{"dip": 17, "max_candles": 6, "n": 7, "stop_atr": 2.75, "take_profit_atr": 0.5}` | 5,573.64 | 8.3 | -12.0 | 82.3 | 1,473.50 | 4.9 | -6.5 | 0.58 | 385/260 | not checked |
| 442 | `{"dip": 18, "max_candles": 4, "n": 7, "stop_atr": 2.5, "take_profit_atr": 0.5}` | 4,713.55 | 7.2 | -11.9 | 78.9 | 914.81 | 3.1 | -6.3 | 0.43 | 355/226 | not checked |
| 524 | `{"dip": 17, "max_candles": 4, "n": 7, "stop_atr": 2.75, "take_profit_atr": 0.5}` | 4,505.12 | 6.9 | -11.9 | 77.7 | 962.92 | 3.2 | -6.4 | 0.47 | 399/274 | not checked |
| 592 | `{"dip": 18, "max_candles": 4, "n": 7, "stop_atr": 3.0, "take_profit_atr": 0.5}` | 4,461.02 | 6.9 | -11.3 | 78.6 | 940.59 | 3.2 | -6.2 | 0.46 | 351/226 | not checked |
| 564 | `{"dip": 18, "max_candles": 2, "n": 7, "stop_atr": 2.25, "take_profit_atr": 0.5}` | 2,928.13 | 4.7 | -10.6 | 70.5 | 509.38 | 1.7 | -8.4 | 0.36 | 403/255 | not checked |
| 554 | `{"dip": 18, "max_candles": 2, "n": 7, "stop_atr": 2.5, "take_profit_atr": 0.5}` | 2,742.54 | 4.5 | -10.6 | 70.5 | 930.99 | 3.1 | -6.3 | 0.70 | 403/251 | not checked |
| 525 | `{"dip": 15, "max_candles": 8, "n": 2, "stop_atr": 2.0, "take_profit_atr": 0.5}` | 2,454.54 | 4.0 | -4.6 | 88.5 | 370.43 | 1.3 | -2.0 | 0.31 | 87/31 | not checked |
| 433 | `{"dip": 15, "max_candles": 8, "n": 2, "stop_atr": 1.75, "take_profit_atr": 0.5}` | 2,412.57 | 4.0 | -4.6 | 88.5 | 309.92 | 1.1 | -1.8 | 0.27 | 87/31 | not checked |
| 518 | `{"dip": 15, "max_candles": 10, "n": 2, "stop_atr": 2.0, "take_profit_atr": 0.5}` | 2,396.59 | 4.0 | -4.6 | 88.5 | 386.41 | 1.3 | -2.0 | 0.33 | 87/31 | not checked |
| 435 | `{"dip": 15, "max_candles": 10, "n": 2, "stop_atr": 1.75, "take_profit_atr": 0.5}` | 2,356.03 | 3.9 | -4.6 | 88.5 | 330.24 | 1.1 | -1.8 | 0.29 | 87/31 | not checked |
| 755 | `{"dip": 16, "max_candles": 8, "n": 2, "stop_atr": 2.0, "take_profit_atr": 0.5}` | 2,264.97 | 3.8 | -3.2 | 91.4 | 306.16 | 1.1 | -2.0 | 0.28 | 70/23 | not checked |
| 762 | `{"dip": 16, "max_candles": 8, "n": 2, "stop_atr": 2.25, "take_profit_atr": 0.5}` | 2,264.97 | 3.8 | -3.2 | 91.4 | 289.73 | 1.0 | -2.1 | 0.26 | 70/23 | not checked |
| 399 | `{"dip": 16, "max_candles": 14, "n": 2, "stop_atr": 1.75, "take_profit_atr": 0.5}` | 1,910.01 | 3.2 | -3.1 | 92.9 | 256.30 | 0.9 | -1.8 | 0.28 | 70/23 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 889 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
