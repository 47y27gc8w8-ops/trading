# golden_cross_ws__QQQ: optimization summary

Updated 2026-11-23T22:09:42Z · backtest.py version `7fe33695ff` · 1,739 parameter sets tested with this version (1,739 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-20
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 5 in-sample and ≥ 2 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross_ws__QQQ__max-income__v002.md](golden_cross_ws__QQQ__max-income__v002.md) | 1737 | `{"fast": 70, "slow": 240, "trailing_stop_pct": 0}` | long QQQ since 2025-07-01 00:00 @ 546.689551 |
| balanced | [golden_cross_ws__QQQ__balanced__v002.md](golden_cross_ws__QQQ__balanced__v002.md) | 1738 | `{"fast": 55, "slow": 210, "trailing_stop_pct": 9}` | flat (data up to 2026-11-23 00:00) |
| safe-starter | [golden_cross_ws__QQQ__safe-starter__v002.md](golden_cross_ws__QQQ__safe-starter__v002.md) | 1739 | `{"fast": 55, "slow": 230, "trailing_stop_pct": 6}` | flat (data up to 2026-11-23 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 30,505.14 | 37,002.55 | 17,999.77 | 7,206.03 | 4,115.52 | 2,423.51 |
| return % | 305.05 | 370.03 | 180.00 | 72.06 | 41.16 | 24.24 |
| return %/year | 9.4 | 15.3 | 6.8 | 5.1 | 2.2 | 2.0 |
| gross profit | 30,701.14 | 37,002.55 | 18,580.41 | 8,050.45 | 4,987.32 | 2,849.12 |
| gross loss | 196.00 | -0.00 | 580.65 | 844.42 | 871.79 | 425.61 |
| trades | 5 | 4 | 9 | 4 | 9 | 4 |
| win rate % | 80.0 | 100.0 | 88.9 | 75.0 | 44.4 | 50.0 |
| avg win | 7,675.28 | 9,250.64 | 2,322.55 | 2,683.48 | 1,246.83 | 1,424.56 |
| avg loss | -196.00 | 0.00 | -580.65 | -844.42 | -174.36 | -212.80 |
| avg result / trade | 6,101.03 | 9,250.64 | 1,999.97 | 1,801.51 | 457.28 | 605.88 |
| largest single loss | -196.00 | 0.00 | -580.65 | -844.42 | -364.79 | -228.05 |
| largest loss % of equity | -1.56 | 0.00 | -4.40 | -5.65 | -3.39 | -2.33 |
| max drawdown | -5,726.99 | -11,727.89 | -2,581.29 | -2,406.38 | -1,277.22 | -1,004.66 |
| max drawdown % | -24.12 | -28.56 | -15.16 | -14.65 | -10.61 | -9.62 |
| profit factor | 156.64 | 999.00 | 32.00 | 9.53 | 5.72 | 6.69 |
| unusually bad trades | 0 | 0 | 0 | 0 | 1 | 0 |
| … threshold (% of equity) | 3.1 | 2.0 | 8.8 | 11.3 | 2.8 | 4.3 |
| time in market % | 66.3 | 82.7 | 41.2 | 28.9 | 15.4 | 9.1 |
| buy & hold return % | 36.87 | 499.73 | 36.87 | 499.73 | 36.87 | 499.73 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.63 |  | 0.75 |  | 0.91 |
| period | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 0.0 | 0.0 | 0.0 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 | 0.0 |
| 2003 | 39.3 | 35.7 | 10.8 |
| 2004 | -7.6 | 1.3 | 3.7 |
| 2005 | 1.6 | -4.2 | -6.2 |
| 2006 | -5.9 | -0.2 | 1.5 |
| 2007 | 19.0 | 6.9 | -1.5 |
| 2008 | -14.9 | 0.0 | 0.0 |
| 2009 | 29.5 | 24.6 | -3.4 |
| 2010 | 20.1 | 2.7 | 11.6 |
| 2011 | 3.7 | -2.1 | 1.1 |
| 2012 | 13.2 | 11.8 | 15.3 |
| 2013 | 36.6 | 32.6 | 5.8 |
| 2014 | 19.2 | 5.2 | 0.0 |
| 2015 | 9.4 | 2.2 | -1.3 |
| 2016 (OOS) | -3.0 | 5.8 | -5.0 |
| 2017 (OOS) | 32.7 | 32.7 | 0.0 |
| 2018 (OOS) | -2.7 | -0.2 | 0.0 |
| 2019 (OOS) | 14.6 | -5.7 | -2.3 |
| 2020 (OOS) | 48.4 | 0.0 | 0.0 |
| 2021 (OOS) | 27.4 | 0.0 | 0.0 |
| 2022 (OOS) | -9.6 | 0.0 | 0.0 |
| 2023 (OOS) | 28.3 | 15.3 | 17.5 |
| 2024 (OOS) | 25.6 | 0.0 | 0.0 |
| 2025 (OOS) | 7.4 | 12.4 | 10.4 |
| 2026 (OOS) | -0.7 | -5.8 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 24.1% from a peak in-sample and 28.6% out-of-sample, and the worst single trade cost 0.0% of the account out-of-sample. About 80 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 15.2% from a peak in-sample and 14.7% out-of-sample, and the worst single trade cost 5.7% of the account out-of-sample. About 89 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 66% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 10.6% from a peak in-sample and 9.6% out-of-sample, and the worst single trade cost 2.3% of the account out-of-sample. About 44 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 94% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 906 | `{"fast": 70, "slow": 240, "trailing_stop_pct": 0}` | 30,505.14 | 9.4 | -24.1 | 80.0 | 37,002.55 | 15.3 | -28.6 | 1.63 | 5/4 | 1.00 |
| 894 | `{"fast": 65, "slow": 240, "trailing_stop_pct": 0}` | 28,632.91 | 9.0 | -23.9 | 83.3 | 35,014.22 | 14.8 | -28.6 | 1.64 | 6/4 | not checked |
| 643 | `{"fast": 60, "slow": 270, "trailing_stop_pct": 0}` | 28,628.82 | 9.0 | -22.1 | 80.0 | 39,642.59 | 15.9 | -28.6 | 1.76 | 5/4 | 1.00 |
| 9 | `{"fast": 55, "slow": 190, "trailing_stop_pct": 0.0}` | 24,469.59 | 8.2 | -20.0 | 72.7 | 38,687.10 | 15.7 | -28.6 | 1.90 | 11/6 | 0.80 |
| 352 | `{"fast": 55, "slow": 190, "trailing_stop_pct": 0}` | 24,469.59 | 8.2 | -20.0 | 72.7 | 38,687.10 | 15.7 | -28.6 | 1.90 | 11/6 | not checked |
| 100 | `{"fast": 10, "slow": 240, "trailing_stop_pct": 9}` | 21,863.96 | 7.7 | -17.6 | 64.3 | 10,869.03 | 7.0 | -21.7 | 0.91 | 14/12 | not checked |
| 161 | `{"fast": 55, "slow": 220, "trailing_stop_pct": 10}` | 19,784.34 | 7.2 | -16.4 | 77.8 | 6,558.06 | 4.8 | -15.9 | 0.66 | 9/4 | not checked |
| 276 | `{"fast": 55, "slow": 220, "trailing_stop_pct": 9}` | 19,684.64 | 7.2 | -14.5 | 77.8 | 7,349.03 | 5.2 | -14.0 | 0.72 | 9/4 | not checked |
| 326 | `{"fast": 55, "slow": 220, "trailing_stop_pct": 8}` | 14,367.36 | 5.9 | -12.3 | 77.8 | 7,859.49 | 5.5 | -12.9 | 0.93 | 9/4 | not checked |
| 494 | `{"fast": 55, "slow": 240, "trailing_stop_pct": 7}` | 4,862.93 | 2.6 | -11.7 | 50.0 | 2,070.52 | 1.8 | -10.0 | 0.68 | 8/4 | not checked |
| 462 | `{"fast": 55, "slow": 230, "trailing_stop_pct": 6}` | 4,115.52 | 2.2 | -10.6 | 44.4 | 2,423.51 | 2.0 | -9.6 | 0.91 | 9/4 | 1.00 |
| 331 | `{"fast": 65, "slow": 250, "trailing_stop_pct": 6}` | 3,716.24 | 2.0 | -9.9 | 50.0 | 1,383.69 | 1.2 | -11.8 | 0.59 | 6/4 | not checked |
| 1676 | `{"fast": 10, "slow": 240, "trailing_stop_pct": 5}` | 3,468.27 | 1.9 | -9.9 | 42.9 | 3,859.33 | 3.0 | -19.7 | 1.59 | 14/12 | not checked |
| 348 | `{"fast": 65, "slow": 260, "trailing_stop_pct": 6}` | 2,964.77 | 1.7 | -8.8 | 50.0 | 1,705.43 | 1.5 | -10.1 | 0.87 | 6/4 | not checked |
| 239 | `{"fast": 55, "slow": 230, "trailing_stop_pct": 5}` | 2,831.22 | 1.6 | -8.3 | 55.6 | 2,985.16 | 2.4 | -7.5 | 1.51 | 9/4 | not checked |
| 480 | `{"fast": 70, "slow": 240, "trailing_stop_pct": 4}` | 2,804.42 | 1.6 | -8.2 | 60.0 | 1,032.99 | 0.9 | -9.6 | 0.57 | 5/4 | not checked |
| 475 | `{"fast": 60, "slow": 230, "trailing_stop_pct": 4}` | 2,791.50 | 1.6 | -7.2 | 63.6 | 1,937.83 | 1.6 | -7.0 | 1.03 | 11/4 | not checked |
| 192 | `{"fast": 25, "slow": 290, "trailing_stop_pct": 4}` | 2,592.77 | 1.5 | -7.2 | 50.0 | 1,723.14 | 1.5 | -14.5 | 0.99 | 10/7 | not checked |
| 924 | `{"fast": 60, "slow": 230, "trailing_stop_pct": 2}` | 1,614.61 | 1.0 | -5.5 | 45.5 | 304.94 | 0.3 | -3.8 | 0.29 | 11/4 | not checked |
| 966 | `{"fast": 60, "slow": 240, "trailing_stop_pct": 3}` | 1,476.61 | 0.9 | -5.1 | 42.9 | 352.40 | 0.3 | -3.0 | 0.36 | 7/4 | not checked |
| 656 | `{"fast": 60, "slow": 260, "trailing_stop_pct": 2}` | 1,330.12 | 0.8 | -3.9 | 28.6 | 223.70 | 0.2 | -4.0 | 0.25 | 7/4 | not checked |
| 933 | `{"fast": 60, "slow": 240, "trailing_stop_pct": 2}` | 1,292.64 | 0.8 | -3.4 | 28.6 | 682.25 | 0.6 | -2.1 | 0.78 | 7/4 | not checked |
| 698 | `{"fast": 65, "slow": 260, "trailing_stop_pct": 1}` | 783.07 | 0.5 | -3.0 | 50.0 | 218.55 | 0.2 | -1.1 | 0.42 | 6/4 | not checked |
| 510 | `{"fast": 45, "slow": 200, "trailing_stop_pct": 1}` | 433.22 | 0.3 | -2.9 | 23.1 | 97.41 | 0.1 | -2.9 | 0.33 | 13/5 | not checked |
| 1377 | `{"fast": 70, "slow": 290, "trailing_stop_pct": 1}` | 314.38 | 0.2 | -1.8 | 60.0 | 107.35 | 0.1 | -1.2 | 0.50 | 5/3 | not checked |

(1 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,739 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
