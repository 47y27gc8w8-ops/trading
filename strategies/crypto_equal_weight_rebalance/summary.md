# crypto_equal_weight_rebalance: optimization summary

Updated 2026-11-27T12:07:44Z · backtest.py version `7d4096a16d` · 436 parameter sets tested with this version (436 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: BTCUSDT, ETHUSDT, LTCUSDT, SOLUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [crypto_equal_weight_rebalance__max-income__v001.md](crypto_equal_weight_rebalance__max-income__v001.md) | 435 | `{"max_candles": 84, "stop_loss_pct": 13}` | flat (data up to 2026-11-26 00:00) |
| balanced | none | | | |
| safe-starter | [crypto_equal_weight_rebalance__safe-starter__v001.md](crypto_equal_weight_rebalance__safe-starter__v001.md) | 436 | `{"max_candles": 42, "stop_loss_pct": 11}` | flat (data up to 2026-11-26 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|
| net profit | 87,619.78 | 4,693.99 | 59,176.73 | 3,036.62 |
| return % | 876.20 | 46.94 | 591.77 | 30.37 |
| return %/year | 46.2 | 14.2 | 38.1 | 9.6 |
| gross profit | 216,450.17 | 29,491.80 | 176,256.82 | 26,099.71 |
| gross loss | 128,830.38 | 24,797.81 | 117,080.08 | 23,063.08 |
| trades | 139 | 70 | 180 | 90 |
| win rate % | 32.4 | 34.3 | 30.0 | 41.1 |
| avg win | 4,810.00 | 1,228.83 | 3,264.02 | 705.40 |
| avg loss | -1,370.54 | -539.08 | -929.21 | -435.15 |
| avg result / trade | 630.36 | 67.06 | 328.76 | 33.74 |
| largest single loss | -3,756.43 | -731.26 | -2,369.07 | -601.38 |
| largest loss % of equity | -3.31 | -3.31 | -2.82 | -2.84 |
| max drawdown | -94,613.00 | -12,622.63 | -51,081.10 | -11,053.51 |
| max drawdown % | -70.90 | -51.54 | -58.23 | -47.05 |
| profit factor | 1.68 | 1.19 | 1.50 | 1.13 |
| unusually bad trades | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 6.6 | 6.6 | 5.6 | 5.6 |
| time in market % | 63.0 | 71.0 | 46.2 | 51.4 |
| buy & hold return % | 955.32 | -13.09 | 955.32 | -13.09 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.31 |  | 0.25 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | safe-starter |
|---|---|---|
| 2018 | -45.6 | -31.1 |
| 2019 | 43.2 | 19.3 |
| 2020 | 134.8 | 95.5 |
| 2021 | 414.2 | 361.3 |
| 2022 | -56.9 | -50.5 |
| 2023 | 141.3 | 88.6 |
| 2024 (OOS) | 47.8 | 49.5 |
| 2025 (OOS) | -12.5 | -8.5 |
| 2026 (OOS) | -11.0 | -17.8 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 70.9% from a peak in-sample and 51.5% out-of-sample, and the worst single trade cost 3.3% of the account out-of-sample. About 32 of every 100 trades won in-sample. Out-of-sample it earned 14.2% a year against 46.2% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 14% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 58.2% from a peak in-sample and 47.0% out-of-sample, and the worst single trade cost 2.8% of the account out-of-sample. About 30 of every 100 trades won in-sample. Out-of-sample it earned 9.6% a year against 38.1% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 17% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 379 | `{"max_candles": 84, "stop_loss_pct": 13}` | 87,619.78 | 46.2 | -70.9 | 32.4 | 4,693.99 | 14.2 | -51.5 | 0.31 | 139/70 | 1.00 |
| 381 | `{"max_candles": 84, "stop_loss_pct": 9}` | 76,485.72 | 43.3 | -68.8 | 24.7 | 3,500.44 | 10.9 | -49.4 | 0.25 | 154/82 | not checked |
| 315 | `{"max_candles": 126, "stop_loss_pct": 12}` | 75,829.44 | 43.1 | -66.0 | 23.3 | 4,248.11 | 13.0 | -52.3 | 0.30 | 120/53 | 1.00 |
| 352 | `{"max_candles": 42, "stop_loss_pct": 11}` | 59,176.73 | 38.1 | -58.2 | 30.0 | 3,036.62 | 9.6 | -47.0 | 0.25 | 180/90 | 1.00 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 436 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
