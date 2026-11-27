# eth_dip_ws__LINKUSDT: optimization summary

Updated 2026-11-23T22:09:30Z · backtest.py version `e7a0a06a3f` · 980 parameter sets tested with this version (980 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: LINKUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-06-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.05% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [eth_dip_ws__LINKUSDT__max-income__v002.md](eth_dip_ws__LINKUSDT__max-income__v002.md) | 978 | `{"entry": 26, "exit": 55, "rsi_n": 16, "stop_loss_pct": 15}` | flat (data up to 2026-11-23 16:00) |
| balanced | [eth_dip_ws__LINKUSDT__balanced__v002.md](eth_dip_ws__LINKUSDT__balanced__v002.md) | 979 | `{"entry": 26, "exit": 55, "rsi_n": 16, "stop_loss_pct": 14}` | flat (data up to 2026-11-23 16:00) |
| safe-starter | [eth_dip_ws__LINKUSDT__safe-starter__v002.md](eth_dip_ws__LINKUSDT__safe-starter__v002.md) | 980 | `{"entry": 28, "exit": 35, "rsi_n": 26, "stop_loss_pct": 5}` | flat (data up to 2026-11-23 16:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 34,428.19 | 9,099.64 | 33,345.71 | 7,782.57 | 2,162.43 | 3,666.70 |
| return % | 344.28 | 91.00 | 333.46 | 77.83 | 21.62 | 36.67 |
| return %/year | 35.9 | 25.1 | 35.2 | 22.0 | 4.1 | 11.4 |
| gross profit | 82,133.34 | 29,320.96 | 79,069.41 | 29,972.03 | 7,826.06 | 7,829.27 |
| gross loss | 47,705.15 | 20,221.32 | 45,723.70 | 22,189.46 | 5,663.63 | 4,162.57 |
| trades | 36 | 27 | 37 | 28 | 21 | 17 |
| win rate % | 69.4 | 70.4 | 67.6 | 67.9 | 47.6 | 58.8 |
| avg win | 3,285.33 | 1,543.21 | 3,162.78 | 1,577.48 | 782.61 | 782.93 |
| avg loss | -4,336.83 | -2,527.67 | -3,810.31 | -2,465.50 | -514.88 | -594.65 |
| avg result / trade | 956.34 | 337.02 | 901.24 | 277.95 | 102.97 | 215.69 |
| largest single loss | -7,340.10 | -4,824.47 | -6,613.87 | -4,669.11 | -613.60 | -722.61 |
| largest loss % of equity | -15.21 | -15.21 | -14.21 | -14.21 | -5.24 | -5.24 |
| max drawdown | -10,883.28 | -14,744.77 | -9,522.73 | -17,128.91 | -1,776.55 | -1,614.58 |
| max drawdown % | -47.79 | -45.38 | -45.93 | -50.90 | -15.12 | -15.44 |
| profit factor | 1.72 | 1.45 | 1.73 | 1.35 | 1.38 | 1.88 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 30.4 | 30.4 | 28.4 | 28.4 | 10.5 | 10.5 |
| time in market % | 8.8 | 13.1 | 8.6 | 13.0 | 0.9 | 0.9 |
| buy & hold return % | 3,022.47 | -40.95 | 3,022.47 | -40.95 | 3,022.47 | -40.95 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.70 |  | 0.63 |  | 2.78 |
| period | 2019-02-18 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2019-02-18 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2019-02-18 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2019 | 42.4 | 42.4 | 0.0 |
| 2020 | 40.2 | 48.6 | 5.9 |
| 2021 | 82.6 | 58.5 | 9.0 |
| 2022 | 20.6 | 26.4 | 3.6 |
| 2023 | 1.1 | 2.3 | 1.6 |
| 2024 (OOS) | 31.5 | 36.2 | 8.2 |
| 2025 (OOS) | 141.1 | 141.1 | 23.4 |
| 2026 (OOS) | -39.8 | -45.9 | 2.4 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 47.8% from a peak in-sample and 45.4% out-of-sample, and the worst single trade cost 15.2% of the account out-of-sample. About 69 of every 100 trades won in-sample. With 100% of equity per trade; about 21% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 45.9% from a peak in-sample and 50.9% out-of-sample, and the worst single trade cost 14.2% of the account out-of-sample. About 68 of every 100 trades won in-sample. With 100% of equity per trade; about 20% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 15.1% from a peak in-sample and 15.4% out-of-sample, and the worst single trade cost 5.2% of the account out-of-sample. About 48 of every 100 trades won in-sample. With 100% of equity per trade; about 65% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 468 | `{"entry": 26, "exit": 55, "rsi_n": 16, "stop_loss_pct": 15}` | 34,428.19 | 35.9 | -47.8 | 69.4 | 9,099.64 | 25.1 | -45.4 | 0.70 | 36/27 | 1.00 |
| 460 | `{"entry": 26, "exit": 55, "rsi_n": 16, "stop_loss_pct": 14}` | 33,345.71 | 35.2 | -45.9 | 67.6 | 7,782.57 | 22.0 | -50.9 | 0.63 | 37/28 | 1.00 |
| 461 | `{"entry": 26, "exit": 55, "rsi_n": 16, "stop_loss_pct": 13}` | 32,436.32 | 34.6 | -44.0 | 65.8 | 9,186.46 | 25.3 | -47.8 | 0.73 | 38/30 | 1.00 |
| 123 | `{"entry": 26, "exit": 55, "rsi_n": 16, "stop_loss_pct": 11}` | 28,219.23 | 31.7 | -40.8 | 60.5 | 8,566.87 | 23.9 | -41.4 | 0.75 | 38/31 | 1.00 |
| 942 | `{"entry": 22, "exit": 55, "rsi_n": 12, "stop_loss_pct": 14}` | 21,549.45 | 26.6 | -40.0 | 70.3 | 9,245.08 | 25.4 | -35.7 | 0.95 | 37/24 | not checked |
| 822 | `{"entry": 24, "exit": 65, "rsi_n": 16, "stop_loss_pct": 14}` | 12,666.44 | 18.3 | -39.7 | 63.0 | 11,466.14 | 30.2 | -37.8 | 1.65 | 27/18 | not checked |
| 654 | `{"entry": 24, "exit": 60, "rsi_n": 16, "stop_loss_pct": 15}` | 10,864.26 | 16.3 | -34.5 | 55.6 | 9,322.35 | 25.6 | -38.5 | 1.57 | 27/18 | not checked |
| 560 | `{"entry": 30, "exit": 35, "rsi_n": 26, "stop_loss_pct": 4}` | 2,352.63 | 4.4 | -16.8 | 44.4 | 589.25 | 2.0 | -24.8 | 0.45 | 36/31 | not checked |
| 408 | `{"entry": 28, "exit": 35, "rsi_n": 26, "stop_loss_pct": 5}` | 2,162.43 | 4.1 | -15.1 | 47.6 | 3,666.70 | 11.4 | -15.4 | 2.78 | 21/17 | 0.86 |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 980 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
