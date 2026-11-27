# trix_zero_trend__broad: optimization summary

Updated 2026-11-26T01:05:19Z · backtest.py version `a6e29e3860` · 4,447 parameter sets tested with this version (4,447 rows in results.csv in total) · last run ended: converged: no profile improved in the last 3480 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [trix_zero_trend__broad__max-income__v001.md](trix_zero_trend__broad__max-income__v001.md) | 412 | `{"max_candles": 132, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [trix_zero_trend__broad__balanced__v002.md](trix_zero_trend__broad__balanced__v002.md) | 958 | `{"max_candles": 144, "n": 11, "stop_atr": 3.5, "take_profit_atr": 4.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [trix_zero_trend__broad__safe-starter__v003.md](trix_zero_trend__broad__safe-starter__v003.md) | 1549 | `{"max_candles": 108, "n": 33, "stop_atr": 2.5, "take_profit_atr": 4.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 8,984.17 | 2,115.68 | 7,742.60 | 840.63 | 3,045.60 | 866.10 |
| return % | 89.84 | 21.16 | 77.43 | 8.41 | 30.46 | 8.66 |
| return %/year | 12.2 | 6.9 | 10.9 | 2.8 | 4.9 | 2.9 |
| gross profit | 16,263.80 | 7,957.01 | 15,413.15 | 7,741.58 | 10,009.12 | 4,919.48 |
| gross loss | 7,279.63 | 5,841.33 | 7,670.55 | 6,900.95 | 6,963.52 | 4,053.38 |
| trades | 219 | 211 | 253 | 244 | 201 | 139 |
| win rate % | 52.5 | 42.2 | 51.0 | 45.5 | 46.3 | 46.0 |
| avg win | 141.42 | 89.40 | 119.48 | 69.74 | 107.62 | 76.87 |
| avg loss | -70.00 | -47.88 | -61.86 | -51.89 | -64.48 | -54.05 |
| avg result / trade | 41.02 | 10.03 | 30.60 | 3.45 | 15.15 | 6.23 |
| largest single loss | -570.19 | -191.05 | -275.79 | -197.37 | -213.19 | -123.31 |
| largest loss % of equity | -24.37 | -33.70 | -35.44 | -21.31 | -14.88 | -36.47 |
| max drawdown | -1,833.63 | -2,597.68 | -1,242.02 | -2,229.18 | -3,062.36 | -1,716.14 |
| max drawdown % | -9.62 | -19.48 | -8.15 | -18.23 | -20.83 | -14.77 |
| profit factor | 2.23 | 1.36 | 2.01 | 1.12 | 1.44 | 1.21 |
| unusually bad trades | 5 | 8 | 28 | 11 | 0 | 1 |
| … threshold (% of equity) | 25.6 | 22.7 | 18.6 | 23.4 | 33.5 | 30.3 |
| time in market % | 6.8 | 10.5 | 6.3 | 11.4 | 6.5 | 8.9 |
| buy & hold return % | 368.58 | 81.24 | 368.58 | 81.24 | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.56 |  | 0.26 |  | 0.59 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -0.4 | -0.3 | 0.0 |
| 2019 | -0.9 | 3.8 | 2.4 |
| 2020 | 12.1 | 12.7 | 10.1 |
| 2021 | 49.2 | 39.9 | 16.8 |
| 2022 | -0.5 | -2.6 | -8.2 |
| 2023 | 15.7 | 11.9 | 7.9 |
| 2024 (OOS) | 16.2 | 16.3 | 10.5 |
| 2025 (OOS) | -1.0 | -2.2 | -11.6 |
| 2026 (OOS) | 3.1 | -3.5 | 6.9 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 9.6% from a peak in-sample and 19.5% out-of-sample, and the worst single trade cost 33.7% of the account out-of-sample. About 53 of every 100 trades won in-sample. Out-of-sample it earned 6.9% a year against 12.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 51% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 8.2% from a peak in-sample and 18.2% out-of-sample, and the worst single trade cost 21.3% of the account out-of-sample. About 51 of every 100 trades won in-sample. Out-of-sample it earned 2.8% a year against 10.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 55% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 20.8% from a peak in-sample and 14.8% out-of-sample, and the worst single trade cost 36.5% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 2.9% a year against 4.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 48% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4324 | `{"max_candles": 144, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4349 | `{"max_candles": 108, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4352 | `{"max_candles": 180, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4363 | `{"max_candles": 168, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4366 | `{"max_candles": 132, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4369 | `{"max_candles": 120, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4382 | `{"max_candles": 96, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4390 | `{"max_candles": 192, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4391 | `{"max_candles": 84, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4395 | `{"max_candles": 156, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 4401 | `{"max_candles": 72, "n": 9, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,097.87 | 12.4 | -19.7 | 39.0 | 1,199.82 | 4.0 | -26.0 | 0.32 | 338/288 | not checked |
| 225 | `{"max_candles": 132, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | 1.00 |
| 236 | `{"max_candles": 120, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 237 | `{"max_candles": 144, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 567 | `{"max_candles": 108, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 588 | `{"max_candles": 96, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 869 | `{"max_candles": 156, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 871 | `{"max_candles": 168, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 940 | `{"max_candles": 180, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 980 | `{"max_candles": 192, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,984.17 | 12.2 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 719 | `{"max_candles": 72, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,886.84 | 12.1 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.56 | 219/211 | not checked |
| 666 | `{"max_candles": 84, "n": 13, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,869.09 | 12.1 | -9.6 | 52.5 | 2,115.68 | 6.9 | -19.5 | 0.57 | 219/211 | not checked |
| 233 | `{"max_candles": 132, "n": 13, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 8,816.31 | 12.1 | -9.4 | 51.6 | 1,615.06 | 5.3 | -18.3 | 0.44 | 219/211 | not checked |
| 525 | `{"max_candles": 120, "n": 13, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 8,816.31 | 12.1 | -9.4 | 51.6 | 1,615.06 | 5.3 | -18.3 | 0.44 | 219/211 | not checked |
| 618 | `{"max_candles": 144, "n": 13, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 8,816.31 | 12.1 | -9.4 | 51.6 | 1,615.06 | 5.3 | -18.3 | 0.44 | 219/211 | not checked |

(49 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 4,447 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
