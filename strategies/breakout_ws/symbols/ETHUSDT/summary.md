# breakout_ws__ETHUSDT: optimization summary

Updated 2026-11-23T22:07:57Z · backtest.py version `330d161090` · 1,641 parameter sets tested with this version (1,641 rows in results.csv in total) · last run ended: no untested valid parameter sets left to try

## Setup

- Data: ETHUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_ws__ETHUSDT__max-income__v001.md](breakout_ws__ETHUSDT__max-income__v001.md) | 1582 | `{"entry_n": 9, "exit_n": 5}` | flat (data up to 2026-11-22 00:00) |
| balanced | [breakout_ws__ETHUSDT__balanced__v002.md](breakout_ws__ETHUSDT__balanced__v002.md) | 1641 | `{"entry_n": 23, "exit_n": 2}` | flat (data up to 2026-11-22 00:00) |
| safe-starter | [breakout_ws__ETHUSDT__safe-starter__v001.md](breakout_ws__ETHUSDT__safe-starter__v001.md) | 1583 | `{"entry_n": 59, "exit_n": 3}` | flat (data up to 2026-11-22 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 127,723.56 | 5,026.74 | 19,972.32 | 2,325.01 | 23,514.75 | 2,789.43 |
| return % | 1,277.24 | 50.27 | 199.72 | 23.25 | 235.15 | 27.89 |
| return %/year | 54.9 | 15.1 | 20.1 | 7.5 | 22.4 | 8.9 |
| gross profit | 274,610.54 | 25,174.84 | 53,477.77 | 11,795.48 | 46,101.64 | 9,023.68 |
| gross loss | 146,886.98 | 20,148.11 | 33,505.45 | 9,470.47 | 22,586.89 | 6,234.25 |
| trades | 52 | 26 | 48 | 20 | 29 | 13 |
| win rate % | 48.1 | 46.1 | 47.9 | 40.0 | 44.8 | 53.9 |
| avg win | 10,984.42 | 2,097.90 | 2,325.12 | 1,474.43 | 3,546.28 | 1,289.10 |
| avg loss | -5,440.26 | -1,439.15 | -1,340.22 | -789.21 | -1,411.68 | -1,039.04 |
| avg result / trade | 2,456.22 | 193.34 | 416.09 | 116.25 | 810.85 | 214.57 |
| largest single loss | -22,990.19 | -3,284.80 | -3,897.73 | -1,829.98 | -4,077.07 | -2,141.62 |
| largest loss % of equity | -16.14 | -13.45 | -18.88 | -9.80 | -20.10 | -13.45 |
| max drawdown | -62,240.62 | -11,927.10 | -7,643.75 | -7,698.82 | -14,379.50 | -4,783.95 |
| max drawdown % | -66.61 | -44.25 | -49.81 | -38.45 | -35.11 | -27.22 |
| profit factor | 1.87 | 1.25 | 1.60 | 1.25 | 2.04 | 1.45 |
| unusually bad trades | 2 | 0 | 6 | 1 | 1 | 0 |
| … threshold (% of equity) | 19.1 | 17.0 | 10.2 | 9.7 | 10.9 | 14.5 |
| time in market % | 47.0 | 41.4 | 19.1 | 17.8 | 16.4 | 18.0 |
| buy & hold return % | 211.30 | -24.43 | 211.30 | -24.43 | 211.30 | -24.43 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |  | 0.37 |  | 0.40 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -28.0 | -21.3 | 6.6 |
| 2019 | 29.4 | 41.4 | 10.9 |
| 2020 | 196.3 | 26.0 | 46.8 |
| 2021 | 332.4 | 95.6 | 77.0 |
| 2022 | -15.1 | -2.6 | -5.6 |
| 2023 | 36.1 | 12.3 | 15.6 |
| 2024 (OOS) | 55.8 | 29.3 | 24.0 |
| 2025 (OOS) | 7.4 | 20.6 | 11.2 |
| 2026 (OOS) | -13.2 | -21.0 | -7.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 66.6% from a peak in-sample and 44.2% out-of-sample, and the worst single trade cost 13.4% of the account out-of-sample. About 48 of every 100 trades won in-sample. Out-of-sample it earned 15.1% a year against 54.9% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 15% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 49.8% from a peak in-sample and 38.5% out-of-sample, and the worst single trade cost 9.8% of the account out-of-sample. About 48 of every 100 trades won in-sample. Out-of-sample it earned 7.5% a year against 20.1% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 20% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 35.1% from a peak in-sample and 27.2% out-of-sample, and the worst single trade cost 13.4% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 8.9% a year against 22.4% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 28% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 38 | `{"entry_n": 9, "exit_n": 5}` | 127,723.56 | 54.9 | -66.6 | 48.1 | 5,026.74 | 15.1 | -44.2 | 0.28 | 52/26 | 1.00 |
| 61 | `{"entry_n": 16, "exit_n": 22}` | 127,436.63 | 54.8 | -64.3 | 52.4 | 8,702.86 | 24.2 | -52.7 | 0.44 | 21/9 | not checked |
| 452 | `{"entry_n": 16, "exit_n": 18}` | 109,902.65 | 51.3 | -61.9 | 50.0 | 7,577.24 | 21.5 | -50.6 | 0.42 | 24/11 | not checked |
| 453 | `{"entry_n": 16, "exit_n": 17}` | 102,807.35 | 49.8 | -60.3 | 52.0 | 7,577.24 | 21.5 | -50.6 | 0.43 | 25/11 | 1.00 |
| 665 | `{"entry_n": 32, "exit_n": 17}` | 67,946.08 | 40.8 | -56.2 | 55.0 | 12,303.01 | 32.0 | -35.7 | 0.78 | 20/8 | not checked |
| 1563 | `{"entry_n": 9, "exit_n": 3}` | 47,639.56 | 33.9 | -55.1 | 42.6 | 4,227.03 | 13.0 | -53.0 | 0.38 | 68/29 | not checked |
| 544 | `{"entry_n": 13, "exit_n": 3}` | 29,277.22 | 25.6 | -45.7 | 38.3 | 3,273.03 | 10.3 | -41.4 | 0.40 | 60/25 | not checked |
| 689 | `{"entry_n": 52, "exit_n": 3}` | 24,339.10 | 22.9 | -43.8 | 43.3 | 2,162.88 | 7.0 | -27.2 | 0.31 | 30/14 | not checked |
| 1387 | `{"entry_n": 53, "exit_n": 3}` | 24,339.10 | 22.9 | -43.8 | 43.3 | 2,162.88 | 7.0 | -27.2 | 0.31 | 30/14 | not checked |
| 613 | `{"entry_n": 60, "exit_n": 3}` | 23,514.75 | 22.4 | -35.1 | 44.8 | 2,038.71 | 6.6 | -27.2 | 0.30 | 29/13 | not checked |
| 615 | `{"entry_n": 59, "exit_n": 3}` | 23,514.75 | 22.4 | -35.1 | 44.8 | 2,789.43 | 8.9 | -27.2 | 0.40 | 29/13 | 1.00 |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,641 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
