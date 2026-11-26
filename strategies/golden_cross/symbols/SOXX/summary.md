# golden_cross__SOXX: optimization summary

Updated 2026-11-26T02:13:20Z · backtest.py version `d48a95163b` · 933 parameter sets tested with this version (933 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SOXX (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__SOXX__max-income__v001.md](golden_cross__SOXX__max-income__v001.md) | 420 | `{"fast": 30, "max_candles": 112, "slow": 200, "stop_atr": 2.0, "take_profit_atr": 10.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [golden_cross__SOXX__balanced__v001.md](golden_cross__SOXX__balanced__v001.md) | 421 | `{"fast": 35, "max_candles": 96, "slow": 200, "stop_atr": 1.0, "take_profit_atr": 10.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [golden_cross__SOXX__safe-starter__v002.md](golden_cross__SOXX__safe-starter__v002.md) | 933 | `{"fast": 40, "max_candles": 104, "slow": 200, "stop_atr": 0.75, "take_profit_atr": 10.0}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 13,525.26 | 10,897.69 | 12,442.15 | 4,817.40 | 12,530.85 | 4,207.98 |
| return % | 135.25 | 108.98 | 124.42 | 48.17 | 125.31 | 42.08 |
| return %/year | 6.9 | 7.0 | 6.5 | 3.7 | 6.5 | 3.3 |
| gross profit | 16,599.46 | 11,584.07 | 14,442.65 | 5,533.29 | 14,049.59 | 4,915.60 |
| gross loss | 3,074.20 | 686.38 | 2,000.50 | 715.89 | 1,518.74 | 707.62 |
| trades | 11 | 5 | 10 | 5 | 10 | 5 |
| win rate % | 45.5 | 60.0 | 40.0 | 40.0 | 40.0 | 40.0 |
| avg win | 3,319.89 | 3,861.36 | 3,610.66 | 2,766.65 | 3,512.40 | 2,457.80 |
| avg loss | -512.37 | -343.19 | -333.42 | -238.63 | -253.12 | -235.87 |
| avg result / trade | 1,229.57 | 2,179.54 | 1,244.21 | 963.48 | 1,253.09 | 841.60 |
| largest single loss | -890.65 | -364.79 | -414.71 | -363.49 | -317.18 | -316.81 |
| largest loss % of equity | -3.99 | -3.77 | -1.99 | -3.77 | -1.39 | -2.71 |
| max drawdown | -2,520.67 | -1,401.83 | -1,370.28 | -1,026.81 | -1,495.78 | -1,237.18 |
| max drawdown % | -10.86 | -9.82 | -9.21 | -9.82 | -9.21 | -9.82 |
| profit factor | 5.40 | 16.88 | 7.22 | 7.73 | 9.25 | 6.95 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 7.2 | 7.0 | 3.9 | 3.9 | 2.9 | 3.7 |
| time in market % | 15.8 | 9.8 | 10.2 | 6.5 | 9.9 | 4.4 |
| buy & hold return % | 179.81 | 1,491.27 | 179.81 | 1,491.27 | 179.81 | 1,491.27 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.02 |  | 0.57 |  | 0.50 |
| period | 2003-02-20 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2003-02-20 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2003-02-20 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2003 | 32.8 | 33.3 | 32.7 |
| 2004 | 0.0 | 0.0 | 0.0 |
| 2005 | 6.5 | -4.0 | -3.1 |
| 2006 | -4.5 | -2.0 | -1.5 |
| 2007 | 0.0 | 0.0 | 0.0 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 35.0 | 37.1 | 36.9 |
| 2010 | 14.4 | 11.0 | 9.4 |
| 2011 | 7.2 | 9.4 | 9.3 |
| 2012 | -7.2 | -3.9 | -2.9 |
| 2013 | 14.7 | 13.9 | 13.5 |
| 2014 | 0.0 | 0.0 | 0.0 |
| 2015 | -0.9 | -1.8 | -1.4 |
| 2016 (OOS) | -5.6 | -1.6 | -1.2 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 0.0 | 0.0 |
| 2019 (OOS) | -3.8 | -1.9 | 18.2 |
| 2020 (OOS) | 39.6 | -3.8 | -2.7 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 26.3 | 27.4 | 27.5 |
| 2024 (OOS) | 0.0 | 0.0 | 0.0 |
| 2025 (OOS) | 27.3 | 25.3 | -1.8 |
| 2026 (OOS) | 0.0 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 10.9% from a peak in-sample and 9.8% out-of-sample, and the worst single trade cost 3.8% of the account out-of-sample. About 45 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 92% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 9.2% from a peak in-sample and 9.8% out-of-sample, and the worst single trade cost 3.8% of the account out-of-sample. About 40 of every 100 trades won in-sample. Out-of-sample it earned 3.7% a year against 6.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 9.2% from a peak in-sample and 9.8% out-of-sample, and the worst single trade cost 2.7% of the account out-of-sample. About 40 of every 100 trades won in-sample. Out-of-sample it earned 3.3% a year against 6.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 137 | `{"fast": 35, "max_candles": 112, "slow": 200, "stop_atr": 1.5, "take_profit_atr": 10.0}` | 13,954.23 | 7.0 | -9.9 | 50.0 | 8,372.15 | 5.8 | -10.9 | 0.82 | 10/5 | 1.00 |
| 181 | `{"fast": 35, "max_candles": 104, "slow": 200, "stop_atr": 1.0, "take_profit_atr": 10.0}` | 12,908.84 | 6.7 | -9.2 | 40.0 | 4,817.40 | 3.7 | -9.8 | 0.55 | 10/5 | 1.00 |
| 747 | `{"fast": 50, "max_candles": 168, "slow": 180, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 11,639.24 | 6.2 | -9.1 | 77.8 | 3,429.60 | 2.8 | -9.8 | 0.44 | 9/5 | not checked |
| 799 | `{"fast": 50, "max_candles": 176, "slow": 180, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 11,639.24 | 6.2 | -9.1 | 77.8 | 3,429.60 | 2.8 | -9.8 | 0.44 | 9/5 | not checked |
| 851 | `{"fast": 50, "max_candles": 184, "slow": 180, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 11,639.24 | 6.2 | -9.1 | 77.8 | 3,429.60 | 2.8 | -9.8 | 0.44 | 9/5 | not checked |
| 866 | `{"fast": 50, "max_candles": 192, "slow": 180, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 11,639.24 | 6.2 | -9.1 | 77.8 | 3,429.60 | 2.8 | -9.8 | 0.44 | 9/5 | not checked |
| 888 | `{"fast": 50, "max_candles": 160, "slow": 180, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 11,639.24 | 6.2 | -9.1 | 77.8 | 3,429.60 | 2.8 | -9.8 | 0.44 | 9/5 | not checked |
| 769 | `{"fast": 65, "max_candles": 128, "slow": 260, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 7,302.76 | 4.4 | -7.8 | 75.0 | 4,939.24 | 3.8 | -9.8 | 0.86 | 8/4 | not checked |
| 791 | `{"fast": 65, "max_candles": 120, "slow": 260, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 7,302.76 | 4.4 | -7.8 | 75.0 | 4,939.24 | 3.8 | -9.8 | 0.86 | 8/4 | not checked |
| 871 | `{"fast": 65, "max_candles": 136, "slow": 260, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 7,302.76 | 4.4 | -7.8 | 75.0 | 4,939.24 | 3.8 | -9.8 | 0.86 | 8/4 | not checked |
| 523 | `{"fast": 80, "max_candles": 192, "slow": 260, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 4,732.86 | 3.1 | -7.1 | 75.0 | 1,780.81 | 1.5 | -9.8 | 0.50 | 8/4 | not checked |
| 608 | `{"fast": 80, "max_candles": 184, "slow": 260, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 4,732.86 | 3.1 | -7.1 | 75.0 | 1,780.81 | 1.5 | -9.8 | 0.50 | 8/4 | not checked |
| 651 | `{"fast": 80, "max_candles": 192, "slow": 260, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,736.20 | 2.5 | -5.8 | 75.0 | 1,464.60 | 1.3 | -9.8 | 0.50 | 8/4 | not checked |
| 753 | `{"fast": 50, "max_candles": 192, "slow": 150, "stop_atr": 1.75, "take_profit_atr": 1.5}` | 1,603.65 | 1.2 | -4.7 | 66.7 | 931.32 | 0.8 | -5.7 | 0.71 | 12/6 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 933 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
