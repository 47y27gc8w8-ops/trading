# golden_cross__XLY: optimization summary

Updated 2026-11-26T02:13:50Z · backtest.py version `34798e406d` · 999 parameter sets tested with this version (999 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: XLY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__XLY__max-income__v001.md](golden_cross__XLY__max-income__v001.md) | 433 | `{"fast": 35, "max_candles": 104, "slow": 200, "stop_atr": 3.75, "take_profit_atr": 10.0}` | long XLY since 2026-11-18 00:00 @ 117.265172 |
| balanced | [golden_cross__XLY__balanced__v002.md](golden_cross__XLY__balanced__v002.md) | 998 | `{"fast": 70, "max_candles": 64, "slow": 250, "stop_atr": 2.5, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [golden_cross__XLY__safe-starter__v002.md](golden_cross__XLY__safe-starter__v002.md) | 999 | `{"fast": 75, "max_candles": 64, "slow": 250, "stop_atr": 2.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 15,495.77 | 1,843.34 | 8,161.95 | 1,705.44 | 7,322.86 | 2,619.57 |
| return % | 154.96 | 18.43 | 81.62 | 17.05 | 73.23 | 26.20 |
| return %/year | 6.2 | 1.6 | 3.9 | 1.5 | 3.6 | 2.2 |
| gross profit | 16,656.41 | 4,085.14 | 8,161.95 | 3,001.91 | 7,322.86 | 3,572.53 |
| gross loss | 1,160.63 | 2,241.80 | -0.00 | 1,296.47 | -0.00 | 952.96 |
| trades | 12 | 8 | 8 | 7 | 8 | 6 |
| win rate % | 75.0 | 37.5 | 100.0 | 57.1 | 100.0 | 66.7 |
| avg win | 1,850.71 | 1,361.71 | 1,020.24 | 750.48 | 915.36 | 893.13 |
| avg loss | -386.88 | -448.36 | 0.00 | -432.16 | 0.00 | -476.48 |
| avg result / trade | 1,291.31 | 230.42 | 1,020.24 | 243.63 | 915.36 | 436.60 |
| largest single loss | -910.06 | -833.49 | 0.00 | -731.87 | 0.00 | -659.88 |
| largest loss % of equity | -9.10 | -7.77 | 0.00 | -5.88 | 0.00 | -4.97 |
| max drawdown | -1,493.25 | -1,502.42 | -576.15 | -889.92 | -876.73 | -675.88 |
| max drawdown % | -11.16 | -12.19 | -4.71 | -8.80 | -6.39 | -5.77 |
| profit factor | 14.35 | 1.82 | 999.00 | 2.31 | 999.00 | 3.75 |
| unusually bad trades | 1 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 3.6 | 8.9 | 2.0 | 6.0 | 2.0 | 7.7 |
| time in market % | 21.7 | 11.3 | 8.0 | 6.0 | 8.9 | 5.3 |
| buy & hold return % | 248.26 | 241.30 | 248.26 | 241.30 | 248.26 | 241.30 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.25 |  | 0.37 |  | 0.60 |
| period | 2000-07-25 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-25 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-25 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 0.0 | 0.0 | 0.0 |
| 2001 | -4.5 | 13.5 | 13.0 |
| 2002 | 4.9 | 7.9 | 3.9 |
| 2003 | 10.9 | 6.6 | 6.2 |
| 2004 | 10.2 | 4.8 | 5.2 |
| 2005 | -4.6 | 0.5 | 0.0 |
| 2006 | 12.5 | 8.9 | 10.3 |
| 2007 | 1.2 | 0.0 | 0.0 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 26.5 | 13.0 | 12.3 |
| 2010 | 18.6 | 0.0 | 0.0 |
| 2011 | 8.9 | 0.0 | 0.0 |
| 2012 | 15.6 | 7.3 | 6.7 |
| 2013 | 0.0 | 0.0 | 0.0 |
| 2014 | 0.0 | 0.0 | 0.0 |
| 2015 | 1.4 | 0.0 | 0.0 |
| 2016 (OOS) | -11.7 | -3.0 | 6.0 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 0.0 | 0.0 |
| 2019 (OOS) | 12.3 | -2.7 | -2.8 |
| 2020 (OOS) | -7.8 | 10.1 | 10.8 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 14.6 | 10.9 | 8.6 |
| 2024 (OOS) | 0.0 | 0.0 | 0.0 |
| 2025 (OOS) | 11.8 | 8.0 | 7.1 |
| 2026 (OOS) | -6.6 | -5.9 | -5.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 11.2% from a peak in-sample and 12.2% out-of-sample, and the worst single trade cost 7.8% of the account out-of-sample. About 75 of every 100 trades won in-sample. Out-of-sample it earned 1.6% a year against 6.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 82% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 4.7% from a peak in-sample and 8.8% out-of-sample, and the worst single trade cost 5.9% of the account out-of-sample. About 100 of every 100 trades won in-sample. Out-of-sample it earned 1.5% a year against 3.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 6.4% from a peak in-sample and 5.8% out-of-sample, and the worst single trade cost 5.0% of the account out-of-sample. About 100 of every 100 trades won in-sample. Out-of-sample it earned 2.2% a year against 3.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 158 | `{"fast": 35, "max_candles": 104, "slow": 200, "stop_atr": 3.75, "take_profit_atr": 10.0}` | 15,495.77 | 6.2 | -11.2 | 75.0 | 1,843.34 | 1.6 | -12.2 | 0.25 | 12/8 | 1.00 |
| 975 | `{"fast": 35, "max_candles": 104, "slow": 190, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 13,576.52 | 5.7 | -10.5 | 63.6 | 1,849.69 | 1.6 | -14.8 | 0.28 | 11/9 | not checked |
| 994 | `{"fast": 35, "max_candles": 112, "slow": 190, "stop_atr": 2.75, "take_profit_atr": 10.0}` | 13,382.48 | 5.7 | -10.4 | 63.6 | 1,704.64 | 1.5 | -12.7 | 0.26 | 11/9 | not checked |
| 825 | `{"fast": 70, "max_candles": 64, "slow": 250, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 8,161.95 | 3.9 | -4.7 | 100.0 | 1,705.44 | 1.5 | -8.8 | 0.37 | 8/7 | 1.00 |
| 832 | `{"fast": 70, "max_candles": 64, "slow": 250, "stop_atr": 2.25, "take_profit_atr": 5.0}` | 8,161.95 | 3.9 | -4.7 | 100.0 | 1,766.08 | 1.5 | -8.3 | 0.38 | 8/7 | not checked |
| 833 | `{"fast": 70, "max_candles": 64, "slow": 250, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 8,161.95 | 3.9 | -4.7 | 100.0 | 1,570.44 | 1.4 | -9.8 | 0.34 | 8/7 | not checked |
| 607 | `{"fast": 70, "max_candles": 120, "slow": 250, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 5,654.13 | 3.0 | -4.6 | 100.0 | 920.77 | 0.8 | -8.8 | 0.28 | 8/7 | not checked |
| 647 | `{"fast": 70, "max_candles": 120, "slow": 250, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 5,654.13 | 3.0 | -4.6 | 100.0 | 977.35 | 0.9 | -8.3 | 0.29 | 8/7 | not checked |
| 736 | `{"fast": 70, "max_candles": 112, "slow": 250, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 5,654.13 | 3.0 | -4.6 | 100.0 | 920.77 | 0.8 | -8.8 | 0.28 | 8/7 | not checked |
| 914 | `{"fast": 70, "max_candles": 112, "slow": 250, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 5,654.13 | 3.0 | -4.6 | 100.0 | 977.35 | 0.9 | -8.3 | 0.29 | 8/7 | not checked |
| 937 | `{"fast": 70, "max_candles": 128, "slow": 250, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 5,654.13 | 3.0 | -4.6 | 100.0 | 920.77 | 0.8 | -8.8 | 0.28 | 8/7 | not checked |
| 958 | `{"fast": 70, "max_candles": 128, "slow": 250, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 5,654.13 | 3.0 | -4.6 | 100.0 | 977.35 | 0.9 | -8.3 | 0.29 | 8/7 | not checked |
| 790 | `{"fast": 75, "max_candles": 96, "slow": 260, "stop_atr": 3.5, "take_profit_atr": 1.5}` | 2,011.81 | 1.2 | -3.7 | 100.0 | 405.03 | 0.4 | -6.5 | 0.31 | 8/6 | not checked |
| 452 | `{"fast": 75, "max_candles": 64, "slow": 230, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 1,383.90 | 0.8 | -3.4 | 66.7 | 724.76 | 0.6 | -3.3 | 0.76 | 9/5 | not checked |
| 543 | `{"fast": 75, "max_candles": 56, "slow": 230, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 1,383.90 | 0.8 | -3.4 | 66.7 | 724.76 | 0.6 | -3.3 | 0.76 | 9/5 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 999 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
