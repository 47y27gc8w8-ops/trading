# breakout_ws__BNBUSDT: optimization summary

Updated 2026-11-23T22:09:33Z · backtest.py version `777b99fc80` · 1,590 parameter sets tested with this version (1,590 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: BNBUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_ws__BNBUSDT__max-income__v001.md](breakout_ws__BNBUSDT__max-income__v001.md) | 1588 | `{"entry_n": 23, "exit_n": 17}` | flat (data up to 2026-11-22 00:00) |
| balanced | [breakout_ws__BNBUSDT__balanced__v001.md](breakout_ws__BNBUSDT__balanced__v001.md) | 1589 | `{"entry_n": 21, "exit_n": 11}` | flat (data up to 2026-11-22 00:00) |
| safe-starter | [breakout_ws__BNBUSDT__safe-starter__v001.md](breakout_ws__BNBUSDT__safe-starter__v001.md) | 1590 | `{"entry_n": 36, "exit_n": 13}` | flat (data up to 2026-11-22 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 687,376.68 | 11,417.13 | 524,234.60 | 9,621.49 | 401,479.48 | 9,035.52 |
| return % | 6,873.77 | 114.17 | 5,242.35 | 96.21 | 4,014.79 | 90.36 |
| return %/year | 107.3 | 30.1 | 98.1 | 26.3 | 89.4 | 24.9 |
| gross profit | 886,160.52 | 19,915.73 | 638,943.84 | 15,845.52 | 546,761.89 | 18,131.69 |
| gross loss | 198,783.84 | 8,498.60 | 114,709.24 | 6,224.03 | 145,282.42 | 9,096.17 |
| trades | 20 | 10 | 24 | 12 | 20 | 9 |
| win rate % | 60.0 | 40.0 | 54.2 | 50.0 | 50.0 | 44.4 |
| avg win | 73,846.71 | 4,978.93 | 49,149.53 | 2,640.92 | 54,676.19 | 4,532.92 |
| avg loss | -24,847.98 | -1,416.43 | -10,428.11 | -1,037.34 | -14,528.24 | -1,819.23 |
| avg result / trade | 34,368.83 | 1,141.71 | 21,843.11 | 801.79 | 20,073.97 | 1,003.95 |
| largest single loss | -85,056.82 | -3,424.94 | -51,308.53 | -2,057.35 | -57,661.08 | -4,104.76 |
| largest loss % of equity | -12.63 | -14.50 | -10.70 | -12.48 | -12.63 | -17.53 |
| max drawdown | -396,162.89 | -14,366.31 | -141,462.17 | -8,488.07 | -207,184.75 | -15,245.51 |
| max drawdown % | -56.76 | -46.14 | -64.94 | -38.75 | -37.30 | -49.39 |
| profit factor | 4.46 | 2.34 | 5.57 | 2.55 | 3.76 | 1.99 |
| unusually bad trades | 2 | 0 | 1 | 2 | 0 | 1 |
| … threshold (% of equity) | 13.8 | 14.9 | 17.5 | 8.4 | 15.8 | 16.2 |
| time in market % | 49.1 | 53.1 | 42.5 | 49.0 | 38.3 | 48.0 |
| buy & hold return % | 2,992.03 | 79.41 | 2,992.03 | 79.41 | 2,992.03 | 79.41 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |  | 0.27 |  | 0.28 |
| period | 2018-03-06 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-03-06 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-03-06 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -24.0 | -38.4 | -3.9 |
| 2019 | 228.5 | 122.6 | 148.3 |
| 2020 | 64.9 | 102.1 | 36.0 |
| 2021 | 1,749.4 | 1,391.0 | 1,294.2 |
| 2022 | -22.8 | 3.7 | -11.9 |
| 2023 | 18.8 | 25.0 | 3.4 |
| 2024 (OOS) | 88.7 | 62.1 | 94.2 |
| 2025 (OOS) | 30.3 | 14.6 | 27.0 |
| 2026 (OOS) | -9.3 | 9.9 | -18.7 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 56.8% from a peak in-sample and 46.1% out-of-sample, and the worst single trade cost 14.5% of the account out-of-sample. About 60 of every 100 trades won in-sample. Out-of-sample it earned 30.1% a year against 107.3% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 18% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 64.9% from a peak in-sample and 38.8% out-of-sample, and the worst single trade cost 12.5% of the account out-of-sample. About 54 of every 100 trades won in-sample. Out-of-sample it earned 26.3% a year against 98.1% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 15% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 37.3% from a peak in-sample and 49.4% out-of-sample, and the worst single trade cost 17.5% of the account out-of-sample. About 50 of every 100 trades won in-sample. Out-of-sample it earned 24.9% a year against 89.4% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 20% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 411 | `{"entry_n": 23, "exit_n": 17}` | 687,376.68 | 107.3 | -56.8 | 60.0 | 11,417.13 | 30.1 | -46.1 | 0.28 | 20/10 | 1.00 |
| 43 | `{"entry_n": 23, "exit_n": 12}` | 599,602.87 | 102.6 | -55.1 | 56.5 | 11,333.63 | 30.0 | -37.9 | 0.29 | 23/11 | not checked |
| 257 | `{"entry_n": 32, "exit_n": 12}` | 561,436.95 | 100.4 | -45.6 | 52.4 | 9,189.55 | 25.3 | -41.6 | 0.25 | 21/10 | not checked |
| 1202 | `{"entry_n": 31, "exit_n": 12}` | 561,436.95 | 100.4 | -45.6 | 52.4 | 9,189.55 | 25.3 | -41.6 | 0.25 | 21/10 | not checked |
| 199 | `{"entry_n": 34, "exit_n": 12}` | 467,522.15 | 94.3 | -37.3 | 50.0 | 9,189.55 | 25.3 | -41.6 | 0.27 | 20/10 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,590 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
