# rsi_dip_trend_filter: optimization summary

Updated 2026-11-24T22:14:38Z · backtest.py version `028e59b880` · 826 parameter sets tested with this version (826 rows in results.csv in total) · last run ended: converged: no profile improved in the last 540 iterations at the smallest step size

## Setup

- Data: BTCUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rsi_dip_trend_filter__max-income__v001.md](rsi_dip_trend_filter__max-income__v001.md) | 758 | `{"buy": 34, "exit": 65, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 3.5}` | flat (data up to 2026-11-24 16:00) |
| balanced | [rsi_dip_trend_filter__balanced__v001.md](rsi_dip_trend_filter__balanced__v001.md) | 758 | `{"buy": 34, "exit": 65, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 3.5}` | flat (data up to 2026-11-24 16:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 880.77 | 243.41 | 880.77 | 243.41 |
| return % | 8.81 | 2.43 | 8.81 | 2.43 |
| return %/year | 1.4 | 0.8 | 1.4 | 0.8 |
| gross profit | 4,632.84 | 1,201.92 | 4,632.84 | 1,201.92 |
| gross loss | 3,752.07 | 958.50 | 3,752.07 | 958.50 |
| trades | 20 | 8 | 20 | 8 |
| win rate % | 45.0 | 50.0 | 45.0 | 50.0 |
| avg win | 514.76 | 300.48 | 514.76 | 300.48 |
| avg loss | -341.10 | -239.63 | -341.10 | -239.63 |
| avg result / trade | 44.04 | 30.43 | 44.04 | 30.43 |
| largest single loss | -631.79 | -309.31 | -631.79 | -309.31 |
| largest loss % of equity | -6.32 | -3.06 | -6.32 | -3.06 |
| max drawdown | -2,253.33 | -1,371.00 | -2,253.33 | -1,371.00 |
| max drawdown % | -22.35 | -12.77 | -22.35 | -12.77 |
| profit factor | 1.24 | 1.25 | 1.24 | 1.25 |
| unusually bad trades | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 7.1 | 4.6 | 7.1 | 4.6 |
| time in market % | 1.3 | 0.9 | 1.3 | 0.9 |
| buy & hold return % | 313.33 | 44.90 | 313.33 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.58 |  | 0.58 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -19.2 | -19.2 |
| 2019 | -0.2 | -0.2 |
| 2020 | 8.4 | 8.4 |
| 2021 | 25.2 | 25.2 |
| 2022 | -3.4 | -3.4 |
| 2023 | 3.0 | 3.0 |
| 2024 (OOS) | -3.2 | -3.2 |
| 2025 (OOS) | 4.5 | 4.5 |
| 2026 (OOS) | 1.3 | 1.3 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 22.4% from a peak in-sample and 12.8% out-of-sample, and the worst single trade cost 3.1% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 0.8% a year against 1.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 45% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 22.4% from a peak in-sample and 12.8% out-of-sample, and the worst single trade cost 3.1% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 0.8% a year against 1.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 45% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 744 | `{"buy": 34, "exit": 65, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 3.5}` | 880.77 | 1.4 | -22.4 | 45.0 | 243.41 | 0.8 | -12.8 | 0.58 | 20/8 | 0.67 |
| 751 | `{"buy": 34, "exit": 60, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 3.5}` | 880.77 | 1.4 | -22.4 | 45.0 | 243.41 | 0.8 | -12.8 | 0.58 | 20/8 | not checked |
| 752 | `{"buy": 34, "exit": 70, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 3.5}` | 880.77 | 1.4 | -22.4 | 45.0 | 243.41 | 0.8 | -12.8 | 0.58 | 20/8 | not checked |
| 755 | `{"buy": 34, "exit": 65, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 862.32 | 1.4 | -21.9 | 45.0 | 293.73 | 1.0 | -12.8 | 0.72 | 20/8 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 826 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
