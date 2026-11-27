# weekly_high_with_daily_trigger__broad: optimization summary

Updated 2026-11-26T00:53:31Z · backtest.py version `1d79bb9b82` · 1,955 parameter sets tested with this version (1,955 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [weekly_high_with_daily_trigger__broad__max-income__v002.md](weekly_high_with_daily_trigger__broad__max-income__v002.md) | 1953 | `{"max_candles": 42, "stop_atr": 5.75, "take_profit_atr": 6.5, "weeks": 4}` | flat (data up to 2026-11-24 00:00) |
| balanced | [weekly_high_with_daily_trigger__broad__balanced__v002.md](weekly_high_with_daily_trigger__broad__balanced__v002.md) | 1954 | `{"max_candles": 7, "stop_atr": 5.75, "take_profit_atr": 6.5, "weeks": 32}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [weekly_high_with_daily_trigger__broad__safe-starter__v002.md](weekly_high_with_daily_trigger__broad__safe-starter__v002.md) | 1955 | `{"max_candles": 24, "stop_atr": 0.5, "take_profit_atr": 7.5, "weeks": 18}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 52,486.81 | 6,188.82 | 8,182.11 | 1,953.75 | 1,641.79 | 1,017.12 |
| return % | 524.87 | 61.89 | 81.82 | 19.54 | 16.42 | 10.17 |
| return %/year | 39.1 | 18.1 | 11.4 | 6.4 | 2.8 | 3.4 |
| gross profit | 100,449.11 | 23,665.32 | 13,299.16 | 5,275.99 | 6,788.36 | 4,286.29 |
| gross loss | 47,962.31 | 17,476.50 | 5,117.05 | 3,322.24 | 5,146.57 | 3,269.16 |
| trades | 504 | 378 | 235 | 166 | 408 | 301 |
| win rate % | 52.4 | 41.5 | 56.6 | 50.6 | 11.0 | 11.6 |
| avg win | 380.49 | 150.73 | 99.99 | 62.81 | 150.85 | 122.47 |
| avg loss | -199.84 | -79.08 | -50.17 | -40.52 | -14.18 | -12.29 |
| avg result / trade | 104.14 | 16.37 | 34.82 | 11.77 | 4.02 | 3.38 |
| largest single loss | -3,726.86 | -2,161.43 | -270.44 | -298.60 | -54.58 | -34.49 |
| largest loss % of equity | -32.52 | -32.05 | -33.26 | -21.35 | -5.11 | -4.68 |
| max drawdown | -18,021.00 | -4,351.89 | -913.14 | -981.51 | -1,386.76 | -922.34 |
| max drawdown % | -30.81 | -33.89 | -5.70 | -8.34 | -11.38 | -7.93 |
| profit factor | 2.09 | 1.35 | 2.60 | 1.59 | 1.32 | 1.31 |
| unusually bad trades | 24 | 22 | 16 | 21 | 0 | 1 |
| … threshold (% of equity) | 31.5 | 28.1 | 18.0 | 15.6 | 7.7 | 6.7 |
| time in market % | 18.8 | 26.5 | 2.6 | 3.6 | 2.1 | 3.5 |
| buy & hold return % | 368.58 | 81.24 | 368.58 | 81.24 | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.46 |  | 0.56 |  | 1.22 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -1.0 | 0.0 | 0.0 |
| 2019 | 6.8 | 0.7 | -2.0 |
| 2020 | 47.2 | 9.5 | 6.4 |
| 2021 | 228.5 | 43.6 | 6.8 |
| 2022 | -20.8 | -0.0 | -1.4 |
| 2023 | 54.4 | 14.8 | 6.0 |
| 2024 (OOS) | 27.2 | 11.0 | 13.4 |
| 2025 (OOS) | -12.0 | 3.1 | -2.8 |
| 2026 (OOS) | -6.2 | 1.0 | -0.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 30.8% from a peak in-sample and 33.9% out-of-sample, and the worst single trade cost 32.0% of the account out-of-sample. About 52 of every 100 trades won in-sample. Out-of-sample it earned 18.1% a year against 39.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 5.7% from a peak in-sample and 8.3% out-of-sample, and the worst single trade cost 21.4% of the account out-of-sample. About 57 of every 100 trades won in-sample. Out-of-sample it earned 6.4% a year against 11.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 11.4% from a peak in-sample and 7.9% out-of-sample, and the worst single trade cost 4.7% of the account out-of-sample. About 11 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 88% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 773 | `{"max_candles": 48, "stop_atr": 5.0, "take_profit_atr": 6.0, "weeks": 4}` | 52,803.85 | 39.2 | -30.6 | 51.5 | 4,237.45 | 13.0 | -35.1 | 0.33 | 515/379 | not checked |
| 1019 | `{"max_candles": 42, "stop_atr": 6.5, "take_profit_atr": 6.5, "weeks": 4}` | 52,555.82 | 39.1 | -30.4 | 52.4 | 6,148.44 | 18.0 | -33.9 | 0.46 | 504/378 | not checked |
| 891 | `{"max_candles": 42, "stop_atr": 6.75, "take_profit_atr": 6.5, "weeks": 4}` | 52,431.59 | 39.1 | -30.4 | 52.4 | 6,115.42 | 17.9 | -33.9 | 0.46 | 504/378 | not checked |
| 580 | `{"max_candles": 42, "stop_atr": 7.0, "take_profit_atr": 6.5, "weeks": 4}` | 52,359.92 | 39.1 | -30.3 | 52.4 | 6,082.41 | 17.8 | -33.9 | 0.46 | 504/378 | not checked |
| 1482 | `{"max_candles": 49, "stop_atr": 5.0, "take_profit_atr": 6.0, "weeks": 4}` | 51,901.86 | 38.9 | -30.0 | 50.5 | 4,194.46 | 12.9 | -35.0 | 0.33 | 515/377 | not checked |
| 1519 | `{"max_candles": 37, "stop_atr": 5.5, "take_profit_atr": 6.5, "weeks": 4}` | 51,745.28 | 38.8 | -29.9 | 51.2 | 5,538.73 | 16.4 | -33.0 | 0.42 | 518/385 | not checked |
| 639 | `{"max_candles": 42, "stop_atr": 5.0, "take_profit_atr": 6.5, "weeks": 4}` | 51,667.16 | 38.8 | -28.8 | 52.1 | 6,219.78 | 18.2 | -34.1 | 0.47 | 505/378 | not checked |
| 1229 | `{"max_candles": 37, "stop_atr": 5.0, "take_profit_atr": 6.5, "weeks": 4}` | 51,088.63 | 38.6 | -28.1 | 50.9 | 5,641.99 | 16.7 | -33.2 | 0.43 | 519/385 | not checked |
| 1352 | `{"max_candles": 37, "stop_atr": 5.25, "take_profit_atr": 7.5, "weeks": 4}` | 49,783.68 | 38.0 | -26.5 | 50.1 | 3,951.49 | 12.2 | -30.0 | 0.32 | 509/377 | not checked |
| 1299 | `{"max_candles": 43, "stop_atr": 5.25, "take_profit_atr": 7.5, "weeks": 4}` | 49,362.68 | 37.8 | -25.4 | 50.7 | 4,667.85 | 14.2 | -31.3 | 0.37 | 489/368 | not checked |
| 1639 | `{"max_candles": 42, "stop_atr": 5.0, "take_profit_atr": 7.0, "weeks": 3}` | 42,598.64 | 34.9 | -25.2 | 50.4 | 3,062.83 | 9.7 | -35.7 | 0.28 | 540/429 | not checked |
| 1311 | `{"max_candles": 25, "stop_atr": 5.0, "take_profit_atr": 8.0, "weeks": 4}` | 41,383.00 | 34.3 | -21.8 | 49.6 | 6,318.89 | 18.4 | -29.0 | 0.54 | 568/404 | not checked |
| 1200 | `{"max_candles": 25, "stop_atr": 5.0, "take_profit_atr": 7.5, "weeks": 4}` | 40,803.08 | 34.0 | -21.0 | 49.9 | 5,013.85 | 15.1 | -29.1 | 0.44 | 569/406 | not checked |
| 588 | `{"max_candles": 18, "stop_atr": 3.5, "take_profit_atr": 6.0, "weeks": 4}` | 28,014.41 | 27.2 | -20.8 | 54.1 | 4,508.00 | 13.7 | -28.6 | 0.50 | 614/452 | not checked |
| 765 | `{"max_candles": 12, "stop_atr": 3.0, "take_profit_atr": 4.0, "weeks": 3}` | 16,270.66 | 19.0 | -19.8 | 52.1 | 2,293.28 | 7.4 | -22.2 | 0.39 | 774/587 | not checked |
| 692 | `{"max_candles": 54, "stop_atr": 3.0, "take_profit_atr": 5.5, "weeks": 18}` | 16,035.78 | 18.8 | -19.7 | 48.2 | 1,526.68 | 5.0 | -16.0 | 0.27 | 249/183 | not checked |
| 1787 | `{"max_candles": 37, "stop_atr": 3.5, "take_profit_atr": 8.5, "weeks": 38}` | 12,930.11 | 16.1 | -19.1 | 52.8 | 1,347.96 | 4.5 | -15.0 | 0.28 | 142/98 | not checked |
| 1707 | `{"max_candles": 25, "stop_atr": 4.75, "take_profit_atr": 7.5, "weeks": 27}` | 9,176.24 | 12.4 | -15.6 | 54.2 | 2,890.04 | 9.2 | -17.1 | 0.74 | 190/150 | not checked |
| 1946 | `{"max_candles": 7, "stop_atr": 5.25, "take_profit_atr": 6.5, "weeks": 32}` | 8,199.15 | 11.4 | -5.7 | 56.6 | 1,984.98 | 6.5 | -8.2 | 0.57 | 235/166 | not checked |
| 1425 | `{"max_candles": 7, "stop_atr": 5.5, "take_profit_atr": 6.5, "weeks": 32}` | 8,190.63 | 11.4 | -5.7 | 56.6 | 1,969.37 | 6.4 | -8.2 | 0.56 | 235/166 | not checked |
| 1431 | `{"max_candles": 7, "stop_atr": 5.75, "take_profit_atr": 6.5, "weeks": 32}` | 8,182.11 | 11.4 | -5.7 | 56.6 | 1,953.75 | 6.4 | -8.3 | 0.56 | 235/166 | 1.00 |
| 1426 | `{"max_candles": 7, "stop_atr": 6.0, "take_profit_atr": 6.5, "weeks": 32}` | 8,173.59 | 11.4 | -5.7 | 56.6 | 1,959.23 | 6.4 | -8.3 | 0.56 | 235/166 | not checked |
| 1895 | `{"max_candles": 7, "stop_atr": 6.25, "take_profit_atr": 6.5, "weeks": 32}` | 8,165.07 | 11.4 | -5.7 | 56.6 | 1,949.77 | 6.3 | -8.3 | 0.56 | 235/166 | not checked |
| 1598 | `{"max_candles": 7, "stop_atr": 5.5, "take_profit_atr": 6.5, "weeks": 33}` | 7,711.18 | 10.8 | -5.7 | 55.4 | 1,424.00 | 4.7 | -9.8 | 0.43 | 231/162 | not checked |
| 1521 | `{"max_candles": 7, "stop_atr": 5.75, "take_profit_atr": 6.5, "weeks": 33}` | 7,702.72 | 10.8 | -5.7 | 55.4 | 1,408.38 | 4.7 | -9.8 | 0.43 | 231/162 | not checked |

(11 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,955 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
