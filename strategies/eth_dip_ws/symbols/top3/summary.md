# eth_dip_ws__top3: optimization summary

Updated 2026-11-23T22:10:54Z · backtest.py version `2c91b9af57` · 334 parameter sets tested with this version (334 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: INJUSDT, LINKUSDT, TRXUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-06-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.05% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [eth_dip_ws__top3__max-income__v001.md](eth_dip_ws__top3__max-income__v001.md) | 332 | `{"entry": 25, "exit": 70, "rsi_n": 14, "stop_loss_pct": 5}` | long LINKUSDT since 2026-11-20 16:00 @ 8.347172; long TRXUSDT since 2026-11-01 00:00 @ 0.303852 |
| balanced | [eth_dip_ws__top3__balanced__v001.md](eth_dip_ws__top3__balanced__v001.md) | 333 | `{"entry": 24, "exit": 35, "rsi_n": 16, "stop_loss_pct": 10}` | flat (data up to 2026-11-23 16:00) |
| safe-starter | [eth_dip_ws__top3__safe-starter__v001.md](eth_dip_ws__top3__safe-starter__v001.md) | 334 | `{"entry": 18, "exit": 70, "rsi_n": 14, "stop_loss_pct": 3}` | flat (data up to 2026-11-23 16:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 14,745.74 | 2,594.55 | 5,323.73 | 2,517.09 | 7,481.38 | 1,493.33 |
| return % | 147.46 | 25.95 | 53.24 | 25.17 | 74.81 | 14.93 |
| return %/year | 18.0 | 8.3 | 8.1 | 8.1 | 10.8 | 4.9 |
| gross profit | 51,873.67 | 20,799.89 | 14,931.11 | 8,057.60 | 11,393.90 | 3,280.81 |
| gross loss | 37,127.94 | 18,205.34 | 9,607.38 | 5,540.51 | 3,912.52 | 1,787.48 |
| trades | 201 | 120 | 88 | 65 | 39 | 22 |
| win rate % | 24.4 | 30.8 | 67.0 | 69.2 | 25.6 | 31.8 |
| avg win | 1,058.65 | 562.16 | 253.07 | 179.06 | 1,139.39 | 468.69 |
| avg loss | -244.26 | -219.34 | -331.29 | -277.03 | -134.91 | -119.17 |
| avg result / trade | 73.36 | 21.62 | 60.50 | 38.72 | 191.83 | 67.88 |
| largest single loss | -798.92 | -583.39 | -619.94 | -533.26 | -231.66 | -134.71 |
| largest loss % of equity | -5.24 | -5.24 | -10.22 | -10.22 | -3.24 | -3.24 |
| max drawdown | -16,641.13 | -8,291.96 | -2,016.82 | -1,823.43 | -2,001.38 | -885.93 |
| max drawdown % | -54.36 | -41.79 | -17.68 | -17.72 | -15.27 | -7.58 |
| profit factor | 1.40 | 1.14 | 1.55 | 1.45 | 2.91 | 1.83 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 10.5 | 10.5 | 20.4 | 20.4 | 6.5 | 6.5 |
| time in market % | 16.0 | 24.2 | 1.5 | 1.9 | 2.5 | 3.7 |
| buy & hold return % | 1,842.98 | 20.16 | 1,842.98 | 20.16 | 1,842.98 | 20.16 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.46 |  | 0.99 |  | 0.46 |
| period | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -13.7 | 0.6 | 5.4 |
| 2019 | 18.3 | 6.7 | 15.2 |
| 2020 | 29.3 | 3.8 | 1.2 |
| 2021 | 56.2 | 24.6 | 0.0 |
| 2022 | -18.8 | 7.0 | 15.4 |
| 2023 | 47.7 | 3.2 | 23.3 |
| 2024 (OOS) | 2.2 | 0.6 | 2.8 |
| 2025 (OOS) | 27.1 | 33.0 | 13.1 |
| 2026 (OOS) | -10.9 | -5.9 | 5.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 54.4% from a peak in-sample and 41.8% out-of-sample, and the worst single trade cost 5.2% of the account out-of-sample. About 24 of every 100 trades won in-sample. Out-of-sample it earned 8.3% a year against 18.0% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 18% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 17.7% from a peak in-sample and 17.7% out-of-sample, and the worst single trade cost 10.2% of the account out-of-sample. About 67 of every 100 trades won in-sample. With 100% of equity per trade; about 56% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 15.3% from a peak in-sample and 7.6% out-of-sample, and the worst single trade cost 3.2% of the account out-of-sample. About 26 of every 100 trades won in-sample. Out-of-sample it earned 4.9% a year against 10.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 65% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 47 | `{"entry": 25, "exit": 70, "rsi_n": 14, "stop_loss_pct": 5}` | 14,745.74 | 18.0 | -54.4 | 24.4 | 2,594.55 | 8.3 | -41.8 | 0.46 | 201/120 | 1.00 |
| 53 | `{"entry": 26, "exit": 70, "rsi_n": 14, "stop_loss_pct": 5}` | 13,513.40 | 16.9 | -52.2 | 24.0 | 4,014.90 | 12.4 | -35.5 | 0.73 | 225/141 | not checked |
| 39 | `{"entry": 25, "exit": 65, "rsi_n": 14, "stop_loss_pct": 5}` | 13,512.29 | 16.9 | -48.7 | 27.1 | 2,825.30 | 9.0 | -36.1 | 0.53 | 203/124 | not checked |
| 51 | `{"entry": 25, "exit": 70, "rsi_n": 16, "stop_loss_pct": 5}` | 11,181.92 | 14.7 | -38.6 | 24.1 | 5,957.53 | 17.5 | -35.6 | 1.19 | 141/88 | not checked |
| 295 | `{"entry": 26, "exit": 60, "rsi_n": 18, "stop_loss_pct": 9}` | 10,904.58 | 14.4 | -36.0 | 42.4 | 3,619.51 | 11.3 | -37.9 | 0.78 | 99/67 | not checked |
| 72 | `{"entry": 20, "exit": 75, "rsi_n": 14, "stop_loss_pct": 5}` | 10,420.68 | 14.0 | -28.7 | 23.9 | 3,517.13 | 11.0 | -24.7 | 0.79 | 67/43 | not checked |
| 82 | `{"entry": 20, "exit": 70, "rsi_n": 14, "stop_loss_pct": 3}` | 9,846.59 | 13.4 | -19.7 | 21.8 | 2,293.29 | 7.4 | -15.9 | 0.55 | 78/48 | 0.88 |
| 93 | `{"entry": 18, "exit": 70, "rsi_n": 12, "stop_loss_pct": 3}` | 8,140.63 | 11.5 | -18.5 | 21.7 | 2,998.05 | 9.5 | -13.6 | 0.82 | 83/49 | not checked |
| 86 | `{"entry": 18, "exit": 70, "rsi_n": 14, "stop_loss_pct": 3}` | 7,481.38 | 10.8 | -15.3 | 25.6 | 1,493.33 | 4.9 | -7.6 | 0.46 | 39/22 | 1.00 |
| 85 | `{"entry": 20, "exit": 70, "rsi_n": 16, "stop_loss_pct": 3}` | 5,673.56 | 8.6 | -15.2 | 19.5 | 1,242.40 | 4.1 | -9.3 | 0.48 | 41/25 | not checked |
| 94 | `{"entry": 18, "exit": 70, "rsi_n": 16, "stop_loss_pct": 3}` | 1,671.79 | 2.9 | -15.2 | 14.3 | 1,247.90 | 4.2 | -7.0 | 1.45 | 21/11 | not checked |
| 305 | `{"entry": 18, "exit": 55, "rsi_n": 16, "stop_loss_pct": 4}` | 895.97 | 1.6 | -13.0 | 25.0 | 952.22 | 3.2 | -4.9 | 2.02 | 20/11 | not checked |
| 98 | `{"entry": 18, "exit": 70, "rsi_n": 14, "stop_loss_pct": 2}` | 259.00 | 0.5 | -12.7 | 13.6 | 691.84 | 2.3 | -9.1 | 4.98 | 44/22 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 334 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
