# breakout_ws__VETUSDT: optimization summary

Updated 2026-11-23T22:09:03Z · backtest.py version `850733bcef` · 1,582 parameter sets tested with this version (1,582 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_ws__VETUSDT__max-income__v001.md](breakout_ws__VETUSDT__max-income__v001.md) | 1580 | `{"entry_n": 30, "exit_n": 9}` | flat (data up to 2026-11-22 00:00) |
| balanced | [breakout_ws__VETUSDT__balanced__v001.md](breakout_ws__VETUSDT__balanced__v001.md) | 1581 | `{"entry_n": 32, "exit_n": 4}` | flat (data up to 2026-11-22 00:00) |
| safe-starter | [breakout_ws__VETUSDT__safe-starter__v001.md](breakout_ws__VETUSDT__safe-starter__v001.md) | 1582 | `{"entry_n": 27, "exit_n": 4}` | flat (data up to 2026-11-22 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 402,189.90 | 10,307.58 | 137,207.29 | 9,721.46 | 110,768.79 | 6,038.74 |
| return % | 4,021.90 | 103.08 | 1,372.07 | 97.21 | 1,107.69 | 60.39 |
| return %/year | 107.2 | 27.8 | 69.3 | 26.5 | 62.9 | 17.8 |
| gross profit | 617,192.32 | 18,659.67 | 203,572.68 | 18,661.34 | 178,223.34 | 20,798.30 |
| gross loss | 215,002.43 | 8,352.09 | 66,365.39 | 8,939.88 | 67,454.55 | 14,759.57 |
| trades | 20 | 8 | 27 | 9 | 30 | 13 |
| win rate % | 55.0 | 37.5 | 55.6 | 44.4 | 53.3 | 38.5 |
| avg win | 56,108.39 | 6,219.89 | 13,571.51 | 4,665.34 | 11,138.96 | 4,159.66 |
| avg loss | -23,889.16 | -1,670.42 | -5,530.45 | -1,787.98 | -4,818.18 | -1,844.95 |
| avg result / trade | 20,109.49 | 1,288.45 | 5,081.75 | 1,080.16 | 3,692.29 | 464.52 |
| largest single loss | -89,631.88 | -2,136.49 | -27,847.07 | -3,131.35 | -23,779.15 | -4,268.17 |
| largest loss % of equity | -23.53 | -12.92 | -20.53 | -12.66 | -20.53 | -19.73 |
| max drawdown | -253,341.32 | -15,351.54 | -72,212.90 | -8,822.96 | -64,773.02 | -14,076.76 |
| max drawdown % | -50.33 | -54.03 | -43.77 | -37.90 | -45.98 | -46.97 |
| profit factor | 2.87 | 2.23 | 3.07 | 2.09 | 2.64 | 1.41 |
| unusually bad trades | 2 | 0 | 1 | 0 | 1 | 1 |
| … threshold (% of equity) | 18.4 | 23.2 | 18.6 | 22.1 | 18.6 | 17.5 |
| time in market % | 36.2 | 16.6 | 23.8 | 10.6 | 25.2 | 14.5 |
| buy & hold return % | 484.67 | -86.53 | 484.67 | -86.53 | 484.67 | -86.53 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |  | 0.38 |  | 0.28 |
| period | 2018-11-22 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-11-22 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-11-22 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | 0.0 | 0.0 | 0.0 |
| 2019 | 19.1 | 18.2 | 18.2 |
| 2020 | 175.5 | 63.1 | 39.3 |
| 2021 | 998.4 | 402.2 | 402.2 |
| 2022 | -19.2 | 4.0 | 4.0 |
| 2023 | 41.8 | 46.6 | 40.8 |
| 2024 (OOS) | 71.0 | 92.1 | 101.9 |
| 2025 (OOS) | -21.4 | -4.3 | -21.3 |
| 2026 (OOS) | 41.0 | 0.1 | -5.8 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 50.3% from a peak in-sample and 54.0% out-of-sample, and the worst single trade cost 12.9% of the account out-of-sample. About 55 of every 100 trades won in-sample. Out-of-sample it earned 27.8% a year against 107.2% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 19% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 43.8% from a peak in-sample and 37.9% out-of-sample, and the worst single trade cost 12.7% of the account out-of-sample. About 56 of every 100 trades won in-sample. Out-of-sample it earned 26.5% a year against 69.3% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 23% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 46.0% from a peak in-sample and 47.0% out-of-sample, and the worst single trade cost 19.7% of the account out-of-sample. About 53 of every 100 trades won in-sample. Out-of-sample it earned 17.8% a year against 62.9% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 21% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 548 | `{"entry_n": 30, "exit_n": 9}` | 402,189.90 | 107.2 | -50.3 | 55.0 | 10,307.58 | 27.8 | -54.0 | 0.26 | 20/8 | 1.00 |
| 547 | `{"entry_n": 31, "exit_n": 8}` | 287,536.44 | 94.3 | -50.0 | 60.0 | 14,026.62 | 35.4 | -51.0 | 0.38 | 20/8 | not checked |
| 454 | `{"entry_n": 42, "exit_n": 7}` | 174,953.59 | 77.1 | -49.0 | 60.0 | 9,332.45 | 25.6 | -46.0 | 0.33 | 20/7 | not checked |
| 266 | `{"entry_n": 36, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 9,307.48 | 25.6 | -46.0 | 0.34 | 21/8 | not checked |
| 490 | `{"entry_n": 40, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 11,707.01 | 30.7 | -46.0 | 0.41 | 21/7 | not checked |
| 672 | `{"entry_n": 41, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 9,332.45 | 25.6 | -46.0 | 0.34 | 21/7 | not checked |
| 1009 | `{"entry_n": 35, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 9,307.48 | 25.6 | -46.0 | 0.34 | 21/8 | not checked |
| 1138 | `{"entry_n": 39, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 11,707.01 | 30.7 | -46.0 | 0.41 | 21/7 | not checked |
| 1260 | `{"entry_n": 37, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 11,707.01 | 30.7 | -46.0 | 0.41 | 21/7 | not checked |
| 1348 | `{"entry_n": 38, "exit_n": 7}` | 165,440.05 | 75.2 | -47.4 | 57.1 | 11,707.01 | 30.7 | -46.0 | 0.41 | 21/7 | not checked |
| 763 | `{"entry_n": 23, "exit_n": 4}` | 150,629.96 | 72.2 | -45.1 | 54.8 | 6,851.01 | 19.8 | -51.1 | 0.27 | 31/14 | not checked |
| 84 | `{"entry_n": 32, "exit_n": 4}` | 137,207.29 | 69.3 | -43.8 | 55.6 | 9,721.46 | 26.5 | -37.9 | 0.38 | 27/9 | 1.00 |
| 87 | `{"entry_n": 33, "exit_n": 4}` | 137,207.29 | 69.3 | -43.8 | 55.6 | 9,721.46 | 26.5 | -37.9 | 0.38 | 27/9 | not checked |
| 489 | `{"entry_n": 34, "exit_n": 4}` | 137,207.29 | 69.3 | -43.8 | 55.6 | 9,721.46 | 26.5 | -37.9 | 0.38 | 27/9 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,582 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
