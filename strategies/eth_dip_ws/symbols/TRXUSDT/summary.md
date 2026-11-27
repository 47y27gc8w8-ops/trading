# eth_dip_ws__TRXUSDT: optimization summary

Updated 2026-11-23T22:10:07Z · backtest.py version `4087f933dc` · 605 parameter sets tested with this version (605 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: TRXUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-06-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.05% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [eth_dip_ws__TRXUSDT__max-income__v002.md](eth_dip_ws__TRXUSDT__max-income__v002.md) | 603 | `{"entry": 30, "exit": 75, "rsi_n": 28, "stop_loss_pct": 12}` | flat (data up to 2026-11-23 16:00) |
| balanced | [eth_dip_ws__TRXUSDT__balanced__v002.md](eth_dip_ws__TRXUSDT__balanced__v002.md) | 604 | `{"entry": 32, "exit": 65, "rsi_n": 32, "stop_loss_pct": 13}` | long TRXUSDT since 2026-11-01 00:00 @ 0.303852 |
| safe-starter | [eth_dip_ws__TRXUSDT__safe-starter__v002.md](eth_dip_ws__TRXUSDT__safe-starter__v002.md) | 605 | `{"entry": 16, "exit": 65, "rsi_n": 12, "stop_loss_pct": 3}` | flat (data up to 2026-11-23 16:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 220,552.87 | 8,671.40 | 30,124.50 | 2,486.95 | 6,274.15 | 4,035.15 |
| return % | 2,205.53 | 86.71 | 301.25 | 24.87 | 62.74 | 40.35 |
| return %/year | 77.6 | 24.1 | 29.0 | 8.0 | 9.3 | 12.4 |
| gross profit | 250,173.10 | 11,915.23 | 53,930.57 | 5,406.83 | 13,522.68 | 5,589.62 |
| gross loss | 29,620.24 | 3,243.82 | 23,806.07 | 2,919.88 | 7,248.53 | 1,554.47 |
| trades | 21 | 6 | 30 | 10 | 26 | 10 |
| win rate % | 42.9 | 66.7 | 46.7 | 80.0 | 26.9 | 60.0 |
| avg win | 27,797.01 | 2,978.81 | 3,852.18 | 675.85 | 1,931.81 | 931.60 |
| avg loss | -2,468.35 | -1,621.91 | -1,487.88 | -1,459.94 | -381.50 | -388.62 |
| avg result / trade | 10,502.52 | 1,445.23 | 1,004.15 | 248.70 | 241.31 | 403.51 |
| largest single loss | -11,289.06 | -2,021.85 | -3,398.51 | -1,598.15 | -468.65 | -452.62 |
| largest loss % of equity | -12.22 | -12.22 | -13.22 | -13.22 | -3.24 | -3.24 |
| max drawdown | -69,022.78 | -4,279.88 | -9,382.04 | -3,246.26 | -3,411.42 | -1,230.52 |
| max drawdown % | -70.83 | -23.06 | -49.10 | -23.94 | -23.64 | -8.63 |
| profit factor | 8.45 | 3.67 | 2.27 | 1.85 | 1.87 | 3.60 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 24.4 | 24.4 | 26.4 | 26.4 | 6.5 | 6.5 |
| time in market % | 59.1 | 60.7 | 33.8 | 40.8 | 2.4 | 5.3 |
| buy & hold return % | 222.95 | 184.00 | 222.95 | 184.00 | 222.95 | 184.00 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.31 |  | 0.28 |  | 1.33 |
| period | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -16.6 | -19.2 | -4.2 |
| 2019 | 29.8 | 17.4 | 27.9 |
| 2020 | 208.1 | 20.8 | -1.1 |
| 2021 | 176.7 | 83.5 | 0.0 |
| 2022 | -0.5 | 4.4 | 0.0 |
| 2023 | 150.9 | 82.8 | 34.2 |
| 2024 (OOS) | 25.0 | 5.7 | 1.4 |
| 2025 (OOS) | 16.2 | -0.7 | 28.9 |
| 2026 (OOS) | 28.6 | 19.0 | 7.4 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 70.8% from a peak in-sample and 23.1% out-of-sample, and the worst single trade cost 12.2% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 24.1% a year against 77.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 14% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 49.1% from a peak in-sample and 23.9% out-of-sample, and the worst single trade cost 13.2% of the account out-of-sample. About 47 of every 100 trades won in-sample. Out-of-sample it earned 8.0% a year against 29.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 20% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 23.6% from a peak in-sample and 8.6% out-of-sample, and the worst single trade cost 3.2% of the account out-of-sample. About 27 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 42% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 553 | `{"entry": 30, "exit": 75, "rsi_n": 28, "stop_loss_pct": 12}` | 220,552.87 | 77.6 | -70.8 | 42.9 | 8,671.40 | 24.1 | -23.1 | 0.31 | 21/6 | 1.00 |
| 549 | `{"entry": 30, "exit": 75, "rsi_n": 26, "stop_loss_pct": 12}` | 145,967.02 | 65.4 | -61.2 | 39.3 | 6,243.69 | 18.3 | -23.1 | 0.28 | 28/8 | not checked |
| 409 | `{"entry": 30, "exit": 75, "rsi_n": 26, "stop_loss_pct": 14}` | 106,241.53 | 56.7 | -56.1 | 40.7 | 7,536.26 | 21.4 | -24.8 | 0.38 | 27/7 | not checked |
| 475 | `{"entry": 32, "exit": 70, "rsi_n": 32, "stop_loss_pct": 13}` | 72,577.62 | 47.2 | -52.2 | 43.3 | 6,196.64 | 18.1 | -23.9 | 0.39 | 30/8 | not checked |
| 418 | `{"entry": 28, "exit": 75, "rsi_n": 24, "stop_loss_pct": 14}` | 52,295.88 | 39.8 | -52.0 | 45.5 | 7,643.15 | 21.7 | -24.8 | 0.55 | 22/6 | 0.88 |
| 563 | `{"entry": 32, "exit": 65, "rsi_n": 32, "stop_loss_pct": 13}` | 30,124.50 | 29.0 | -49.1 | 46.7 | 2,486.95 | 8.0 | -23.9 | 0.28 | 30/10 | 1.00 |
| 453 | `{"entry": 26, "exit": 60, "rsi_n": 18, "stop_loss_pct": 8}` | 29,755.85 | 28.8 | -40.8 | 43.4 | 3,710.79 | 11.5 | -16.1 | 0.40 | 53/17 | not checked |
| 50 | `{"entry": 22, "exit": 65, "rsi_n": 12, "stop_loss_pct": 6}` | 22,614.76 | 24.2 | -39.0 | 38.3 | 2,050.51 | 6.7 | -23.3 | 0.28 | 81/27 | 1.00 |
| 483 | `{"entry": 18, "exit": 70, "rsi_n": 12, "stop_loss_pct": 3}` | 20,500.20 | 22.6 | -35.2 | 23.9 | 2,101.95 | 6.8 | -14.6 | 0.30 | 46/16 | not checked |
| 431 | `{"entry": 14, "exit": 75, "rsi_n": 10, "stop_loss_pct": 4}` | 18,619.25 | 21.2 | -32.4 | 33.3 | 4,670.56 | 14.2 | -10.9 | 0.67 | 27/11 | not checked |
| 405 | `{"entry": 14, "exit": 70, "rsi_n": 10, "stop_loss_pct": 3}` | 14,807.69 | 18.1 | -25.9 | 31.0 | 4,316.50 | 13.2 | -8.6 | 0.73 | 29/11 | not checked |
| 455 | `{"entry": 18, "exit": 65, "rsi_n": 14, "stop_loss_pct": 3}` | 14,305.91 | 17.7 | -22.4 | 31.8 | 4,876.85 | 14.7 | -5.6 | 0.83 | 22/9 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 605 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
