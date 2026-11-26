# golden_cross__SMH: optimization summary

Updated 2026-11-26T02:13:35Z · backtest.py version `39e790a3ae` · 967 parameter sets tested with this version (967 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SMH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__SMH__max-income__v001.md](golden_cross__SMH__max-income__v001.md) | 465 | `{"fast": 80, "max_candles": 152, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [golden_cross__SMH__balanced__v001.md](golden_cross__SMH__balanced__v001.md) | 466 | `{"fast": 40, "max_candles": 96, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [golden_cross__SMH__safe-starter__v001.md](golden_cross__SMH__safe-starter__v001.md) | 467 | `{"fast": 40, "max_candles": 96, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 12,774.92 | 2,377.27 | 10,511.36 | 7,458.10 | 9,175.77 | 6,890.28 |
| return % | 127.75 | 23.77 | 105.11 | 74.58 | 91.76 | 68.90 |
| return %/year | 6.1 | 2.0 | 5.3 | 5.2 | 4.8 | 4.9 |
| gross profit | 17,324.81 | 4,283.11 | 12,163.93 | 7,650.72 | 10,745.45 | 7,082.91 |
| gross loss | 4,549.89 | 1,905.84 | 1,652.57 | 192.63 | 1,569.68 | 192.63 |
| trades | 15 | 6 | 10 | 5 | 10 | 5 |
| win rate % | 66.7 | 50.0 | 60.0 | 80.0 | 60.0 | 80.0 |
| avg win | 1,732.48 | 1,427.70 | 2,027.32 | 1,912.68 | 1,790.91 | 1,770.73 |
| avg loss | -909.98 | -635.28 | -413.14 | -192.63 | -392.42 | -192.63 |
| avg result / trade | 851.66 | 396.21 | 1,051.14 | 1,491.62 | 917.58 | 1,378.06 |
| largest single loss | -1,230.47 | -913.84 | -428.57 | -192.63 | -403.63 | -192.63 |
| largest loss % of equity | -7.45 | -7.58 | -2.19 | -1.93 | -2.19 | -1.93 |
| max drawdown | -2,596.65 | -2,343.08 | -1,263.53 | -1,333.43 | -1,172.59 | -1,303.57 |
| max drawdown % | -22.39 | -17.55 | -10.87 | -9.12 | -6.76 | -9.12 |
| profit factor | 3.81 | 2.25 | 7.36 | 39.72 | 6.85 | 36.77 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 11.3 | 10.6 | 4.3 | 3.9 | 4.3 | 3.9 |
| time in market % | 16.6 | 8.3 | 10.4 | 7.3 | 8.2 | 7.1 |
| buy & hold return % | 23.67 | 1,830.25 | 23.67 | 1,830.25 | 23.67 | 1,830.25 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.33 |  | 0.99 |  | 1.03 |
| period | 2002-01-10 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2002-01-10 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2002-01-10 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2002 | -10.7 | 0.0 | 0.0 |
| 2003 | 39.9 | 22.4 | 20.5 |
| 2004 | 0.0 | 0.0 | 0.0 |
| 2005 | 26.9 | 7.6 | 6.7 |
| 2006 | -5.6 | -0.3 | -0.3 |
| 2007 | 10.4 | 11.7 | 10.8 |
| 2008 | -7.4 | 0.0 | 0.0 |
| 2009 | 25.4 | 22.3 | 20.0 |
| 2010 | 4.0 | 11.3 | 10.3 |
| 2011 | 5.9 | 0.0 | 0.0 |
| 2012 | 0.2 | -4.3 | -4.3 |
| 2013 | 9.1 | 9.5 | 8.7 |
| 2014 | 0.0 | 0.0 | 0.0 |
| 2015 | -1.3 | -2.0 | -2.0 |
| 2016 (OOS) | -8.5 | -1.9 | -1.9 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 0.0 | 0.0 |
| 2019 (OOS) | -5.3 | 10.3 | 9.4 |
| 2020 (OOS) | 15.1 | 21.2 | 19.4 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 16.3 | 16.8 | 16.8 |
| 2024 (OOS) | 0.0 | 0.0 | 0.0 |
| 2025 (OOS) | 2.7 | 14.0 | 12.9 |
| 2026 (OOS) | 0.0 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 22.4% from a peak in-sample and 17.6% out-of-sample, and the worst single trade cost 7.6% of the account out-of-sample. About 67 of every 100 trades won in-sample. Out-of-sample it earned 2.0% a year against 6.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 45% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 10.9% from a peak in-sample and 9.1% out-of-sample, and the worst single trade cost 1.9% of the account out-of-sample. About 60 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 92% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 6.8% from a peak in-sample and 9.1% out-of-sample, and the worst single trade cost 1.9% of the account out-of-sample. About 60 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 319 | `{"fast": 80, "max_candles": 152, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | 1.00 |
| 330 | `{"fast": 80, "max_candles": 144, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 331 | `{"fast": 80, "max_candles": 160, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 712 | `{"fast": 80, "max_candles": 136, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 736 | `{"fast": 80, "max_candles": 168, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 790 | `{"fast": 80, "max_candles": 128, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 913 | `{"fast": 80, "max_candles": 120, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 961 | `{"fast": 80, "max_candles": 112, "slow": 150, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 12,774.92 | 6.1 | -22.4 | 66.7 | 2,377.27 | 2.0 | -17.6 | 0.33 | 15/6 | not checked |
| 594 | `{"fast": 80, "max_candles": 112, "slow": 150, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 12,178.01 | 5.9 | -17.9 | 60.0 | 3,844.61 | 3.0 | -15.7 | 0.52 | 15/6 | not checked |
| 639 | `{"fast": 80, "max_candles": 120, "slow": 150, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 12,178.01 | 5.9 | -17.9 | 60.0 | 3,844.61 | 3.0 | -15.7 | 0.52 | 15/6 | not checked |
| 691 | `{"fast": 80, "max_candles": 96, "slow": 150, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 12,178.01 | 5.9 | -17.9 | 60.0 | 3,844.61 | 3.0 | -15.7 | 0.52 | 15/6 | not checked |
| 696 | `{"fast": 80, "max_candles": 104, "slow": 150, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 12,178.01 | 5.9 | -17.9 | 60.0 | 3,844.61 | 3.0 | -15.7 | 0.52 | 15/6 | not checked |
| 795 | `{"fast": 80, "max_candles": 128, "slow": 150, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 12,178.01 | 5.9 | -17.9 | 60.0 | 3,844.61 | 3.0 | -15.7 | 0.52 | 15/6 | not checked |
| 663 | `{"fast": 80, "max_candles": 96, "slow": 160, "stop_atr": 2.25, "take_profit_atr": 7.0}` | 11,804.38 | 5.7 | -15.1 | 58.3 | 1,687.47 | 1.4 | -13.1 | 0.25 | 12/7 | not checked |
| 574 | `{"fast": 75, "max_candles": 96, "slow": 160, "stop_atr": 2.25, "take_profit_atr": 7.0}` | 11,435.00 | 5.6 | -14.0 | 63.6 | 2,185.72 | 1.8 | -14.8 | 0.33 | 11/6 | not checked |
| 184 | `{"fast": 40, "max_candles": 96, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 10,511.36 | 5.3 | -10.9 | 60.0 | 7,458.10 | 5.2 | -9.1 | 0.99 | 10/5 | 0.89 |
| 196 | `{"fast": 40, "max_candles": 88, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 10,511.36 | 5.3 | -10.9 | 60.0 | 7,458.10 | 5.2 | -9.1 | 0.99 | 10/5 | not checked |
| 197 | `{"fast": 40, "max_candles": 104, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 10,511.36 | 5.3 | -10.9 | 60.0 | 7,458.10 | 5.2 | -9.1 | 0.99 | 10/5 | not checked |
| 195 | `{"fast": 40, "max_candles": 96, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 5.5}` | 9,175.77 | 4.8 | -6.8 | 60.0 | 6,890.28 | 4.9 | -9.1 | 1.03 | 10/5 | 0.80 |
| 207 | `{"fast": 40, "max_candles": 88, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 5.5}` | 9,175.77 | 4.8 | -6.8 | 60.0 | 6,890.28 | 4.9 | -9.1 | 1.03 | 10/5 | not checked |
| 208 | `{"fast": 40, "max_candles": 104, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 5.5}` | 9,175.77 | 4.8 | -6.8 | 60.0 | 6,890.28 | 4.9 | -9.1 | 1.03 | 10/5 | not checked |
| 470 | `{"fast": 40, "max_candles": 112, "slow": 210, "stop_atr": 1.25, "take_profit_atr": 5.5}` | 9,175.77 | 4.8 | -6.8 | 60.0 | 6,890.28 | 4.9 | -9.1 | 1.03 | 10/5 | not checked |
| 356 | `{"fast": 75, "max_candles": 176, "slow": 230, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 4,608.15 | 2.8 | -5.8 | 100.0 | 1,725.47 | 1.5 | -4.2 | 0.54 | 9/4 | not checked |
| 460 | `{"fast": 75, "max_candles": 72, "slow": 250, "stop_atr": 2.0, "take_profit_atr": 2.0}` | 1,978.72 | 1.3 | -4.7 | 62.5 | 854.15 | 0.8 | -5.8 | 0.58 | 8/4 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 967 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
