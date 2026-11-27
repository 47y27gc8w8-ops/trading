# eth_dip_ws__INJUSDT: optimization summary

Updated 2026-11-23T22:08:58Z · backtest.py version `291e45ac04` · 837 parameter sets tested with this version (837 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: INJUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-06-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.05% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [eth_dip_ws__INJUSDT__max-income__v002.md](eth_dip_ws__INJUSDT__max-income__v002.md) | 836 | `{"entry": 30, "exit": 40, "rsi_n": 24, "stop_loss_pct": 6}` | flat (data up to 2026-11-23 16:00) |
| balanced | [eth_dip_ws__INJUSDT__balanced__v002.md](eth_dip_ws__INJUSDT__balanced__v002.md) | 836 | `{"entry": 30, "exit": 40, "rsi_n": 24, "stop_loss_pct": 6}` | flat (data up to 2026-11-23 16:00) |
| safe-starter | [eth_dip_ws__INJUSDT__safe-starter__v002.md](eth_dip_ws__INJUSDT__safe-starter__v002.md) | 837 | `{"entry": 30, "exit": 35, "rsi_n": 26, "stop_loss_pct": 3}` | flat (data up to 2026-11-23 16:00) |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 16,406.34 | 15,716.08 | 16,406.34 | 15,716.08 | 5,110.25 | 1,749.01 |
| return % | 164.06 | 157.16 | 164.06 | 157.16 | 51.10 | 17.49 |
| return %/year | 36.8 | 38.6 | 36.8 | 38.6 | 14.2 | 5.7 |
| gross profit | 26,746.56 | 25,142.72 | 26,746.56 | 25,142.72 | 9,891.41 | 7,437.53 |
| gross loss | 10,340.22 | 9,426.64 | 10,340.22 | 9,426.64 | 4,781.16 | 5,688.52 |
| trades | 23 | 26 | 23 | 26 | 21 | 28 |
| win rate % | 52.2 | 61.5 | 52.2 | 61.5 | 42.9 | 39.3 |
| avg win | 2,228.88 | 1,571.42 | 2,228.88 | 1,571.42 | 1,099.05 | 676.14 |
| avg loss | -940.02 | -942.66 | -940.02 | -942.66 | -398.43 | -334.62 |
| avg result / trade | 713.32 | 604.46 | 713.32 | 604.46 | 243.35 | 62.46 |
| largest single loss | -1,478.96 | -1,488.22 | -1,478.96 | -1,488.22 | -430.85 | -384.63 |
| largest loss % of equity | -6.23 | -6.23 | -6.23 | -6.23 | -3.24 | -3.24 |
| max drawdown | -3,755.70 | -2,854.18 | -3,755.70 | -2,854.18 | -2,073.04 | -1,619.85 |
| max drawdown % | -22.82 | -22.86 | -22.82 | -22.86 | -15.54 | -15.24 |
| profit factor | 2.59 | 2.67 | 2.59 | 2.67 | 2.07 | 1.31 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 12.5 | 12.5 | 12.5 | 12.5 | 6.5 | 6.5 |
| time in market % | 2.1 | 3.0 | 2.1 | 3.0 | 0.8 | 0.8 |
| buy & hold return % | 2,283.51 | -82.56 | 2,283.51 | -82.56 | 2,283.51 | -82.56 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.05 |  | 1.05 |  | 0.40 |
| period | 2020-11-23 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2020-11-23 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2020-11-23 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2020 | 0.0 | 0.0 | 0.0 |
| 2021 | 56.7 | 56.7 | 28.9 |
| 2022 | 44.7 | 44.7 | 11.7 |
| 2023 | 16.5 | 16.5 | 5.0 |
| 2024 (OOS) | 46.5 | 46.5 | 3.0 |
| 2025 (OOS) | 55.1 | 55.1 | 11.4 |
| 2026 (OOS) | 13.1 | 13.1 | 2.4 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 22.8% from a peak in-sample and 22.9% out-of-sample, and the worst single trade cost 6.2% of the account out-of-sample. About 52 of every 100 trades won in-sample. With 100% of equity per trade; about 44% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 22.8% from a peak in-sample and 22.9% out-of-sample, and the worst single trade cost 6.2% of the account out-of-sample. About 52 of every 100 trades won in-sample. With 100% of equity per trade; about 44% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 15.5% from a peak in-sample and 15.2% out-of-sample, and the worst single trade cost 3.2% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 5.7% a year against 14.2% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 64% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 362 | `{"entry": 30, "exit": 50, "rsi_n": 24, "stop_loss_pct": 3}` | 16,444.21 | 36.8 | -32.8 | 25.9 | 5,577.26 | 16.6 | -31.3 | 0.45 | 27/33 | not checked |
| 262 | `{"entry": 30, "exit": 40, "rsi_n": 24, "stop_loss_pct": 6}` | 16,406.34 | 36.8 | -22.8 | 52.2 | 15,716.08 | 38.6 | -22.9 | 1.05 | 23/26 | 1.00 |
| 303 | `{"entry": 30, "exit": 40, "rsi_n": 24, "stop_loss_pct": 3}` | 15,392.82 | 35.0 | -17.9 | 37.0 | 5,571.15 | 16.6 | -16.1 | 0.47 | 27/33 | not checked |
| 556 | `{"entry": 28, "exit": 40, "rsi_n": 22, "stop_loss_pct": 3}` | 11,642.24 | 28.3 | -15.3 | 38.1 | 5,309.45 | 15.9 | -15.2 | 0.56 | 21/30 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 837 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
