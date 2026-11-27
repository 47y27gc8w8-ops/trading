# golden_cross_ws__XLI: optimization summary

Updated 2026-11-23T22:11:03Z · backtest.py version `0a1eb1d80a` · 1,128 parameter sets tested with this version (1,128 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: XLI (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-20
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 5 in-sample and ≥ 2 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross_ws__XLI__max-income__v001.md](golden_cross_ws__XLI__max-income__v001.md) | 189 | `{"fast": 50, "slow": 210, "trailing_stop_pct": 0.0}` | flat (data up to 2026-11-23 00:00) |
| balanced | [golden_cross_ws__XLI__balanced__v002.md](golden_cross_ws__XLI__balanced__v002.md) | 1127 | `{"fast": 21, "slow": 300, "trailing_stop_pct": 1}` | flat (data up to 2026-11-23 00:00) |
| safe-starter | [golden_cross_ws__XLI__safe-starter__v002.md](golden_cross_ws__XLI__safe-starter__v002.md) | 1128 | `{"fast": 6, "slow": 260, "trailing_stop_pct": 7}` | flat (data up to 2026-11-23 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 22,549.41 | 5,821.25 | 1,189.82 | 211.11 | 9,021.21 | 3,274.07 |
| return % | 225.49 | 58.21 | 11.90 | 2.11 | 90.21 | 32.74 |
| return %/year | 7.7 | 4.3 | 0.7 | 0.2 | 4.2 | 2.6 |
| gross profit | 24,340.07 | 11,227.93 | 1,451.04 | 369.25 | 12,727.15 | 5,248.94 |
| gross loss | 1,790.66 | 5,406.68 | 261.22 | 158.14 | 3,705.94 | 1,974.87 |
| trades | 12 | 7 | 9 | 6 | 20 | 12 |
| win rate % | 50.0 | 71.4 | 66.7 | 50.0 | 55.0 | 33.3 |
| avg win | 4,056.68 | 2,245.59 | 241.84 | 123.08 | 1,157.01 | 1,312.24 |
| avg loss | -298.44 | -2,703.34 | -87.07 | -52.71 | -411.77 | -246.86 |
| avg result / trade | 1,879.12 | 831.61 | 132.20 | 35.18 | 451.06 | 272.84 |
| largest single loss | -788.34 | -3,932.37 | -124.82 | -79.51 | -818.01 | -682.67 |
| largest loss % of equity | -7.88 | -30.08 | -1.13 | -0.80 | -4.12 | -4.89 |
| max drawdown | -6,225.29 | -6,502.86 | -231.37 | -158.07 | -3,371.04 | -1,843.30 |
| max drawdown % | -26.19 | -42.67 | -2.07 | -1.57 | -15.05 | -16.53 |
| profit factor | 13.59 | 2.08 | 5.55 | 2.33 | 3.43 | 2.66 |
| unusually bad trades | 2 | 0 | 0 | 0 | 0 | 1 |
| … threshold (% of equity) | 3.1 | 40.2 | 2.0 | 2.0 | 6.2 | 4.4 |
| time in market % | 69.5 | 80.4 | 0.8 | 0.4 | 33.6 | 26.7 |
| buy & hold return % | 174.01 | 261.19 | 174.01 | 261.19 | 174.01 | 261.19 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.56 |  | 0.27 |  | 0.64 |
| period | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 8.4 | 1.5 | 0.4 |
| 2001 | -16.7 | 5.4 | 2.2 |
| 2002 | -4.6 | -0.8 | -4.9 |
| 2003 | 27.8 | 0.6 | 2.6 |
| 2004 | 17.8 | 0.0 | 0.0 |
| 2005 | -4.0 | 4.1 | 4.3 |
| 2006 | 3.6 | 0.0 | 15.7 |
| 2007 | 13.5 | 0.0 | -1.9 |
| 2008 | -12.1 | -0.5 | -7.3 |
| 2009 | 36.4 | -1.1 | 4.3 |
| 2010 | 28.3 | 0.0 | 19.0 |
| 2011 | -8.6 | 0.0 | 1.4 |
| 2012 | 6.2 | 1.1 | 13.5 |
| 2013 | 40.5 | 0.0 | 40.5 |
| 2014 | 10.4 | 0.0 | -1.2 |
| 2015 | -4.0 | 1.2 | -12.7 |
| 2016 (OOS) | 10.4 | -0.4 | -0.2 |
| 2017 (OOS) | 24.0 | 0.0 | 0.0 |
| 2018 (OOS) | -8.6 | 0.0 | 2.2 |
| 2019 (OOS) | 11.3 | -0.3 | 1.9 |
| 2020 (OOS) | -28.7 | 0.2 | -1.1 |
| 2021 (OOS) | 21.1 | 0.0 | 0.0 |
| 2022 (OOS) | -12.5 | -0.4 | -8.1 |
| 2023 (OOS) | 10.9 | 0.0 | 11.1 |
| 2024 (OOS) | 17.3 | 0.0 | 5.9 |
| 2025 (OOS) | 1.4 | 3.1 | 17.0 |
| 2026 (OOS) | 9.0 | 0.0 | 2.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 26.2% from a peak in-sample and 42.7% out-of-sample, and the worst single trade cost 30.1% of the account out-of-sample. About 50 of every 100 trades won in-sample. Out-of-sample it earned 4.3% a year against 7.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 23% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 2.1% from a peak in-sample and 1.6% out-of-sample, and the worst single trade cost 0.8% of the account out-of-sample. About 67 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks moderate: the account fell up to 15.1% from a peak in-sample and 16.5% out-of-sample, and the worst single trade cost 4.9% of the account out-of-sample. About 55 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 60% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 353 | `{"fast": 6, "slow": 270, "trailing_stop_pct": 10}` | 23,259.08 | 7.9 | -17.6 | 52.6 | 18,193.57 | 10.0 | -15.8 | 1.27 | 19/12 | not checked |
| 381 | `{"fast": 6, "slow": 270, "trailing_stop_pct": 9}` | 12,448.57 | 5.2 | -16.7 | 57.9 | 12,898.64 | 7.9 | -16.0 | 1.51 | 19/12 | not checked |
| 294 | `{"fast": 6, "slow": 270, "trailing_stop_pct": 8}` | 12,204.37 | 5.2 | -16.0 | 57.9 | 11,326.38 | 7.2 | -16.1 | 1.40 | 19/12 | not checked |
| 301 | `{"fast": 6, "slow": 270, "trailing_stop_pct": 7}` | 9,628.47 | 4.3 | -14.8 | 57.9 | 3,617.65 | 2.9 | -15.1 | 0.66 | 19/12 | not checked |
| 378 | `{"fast": 11, "slow": 270, "trailing_stop_pct": 7}` | 6,077.63 | 3.0 | -14.3 | 64.3 | 2,279.20 | 1.9 | -17.8 | 0.63 | 14/11 | not checked |
| 391 | `{"fast": 11, "slow": 280, "trailing_stop_pct": 7}` | 5,389.88 | 2.8 | -14.0 | 66.7 | 3,406.11 | 2.7 | -17.6 | 0.99 | 12/9 | not checked |
| 497 | `{"fast": 1, "slow": 270, "trailing_stop_pct": 4}` | 4,382.33 | 2.3 | -12.7 | 34.1 | 2,422.46 | 2.0 | -17.9 | 0.87 | 41/28 | not checked |
| 674 | `{"fast": 11, "slow": 240, "trailing_stop_pct": 6}` | 4,198.71 | 2.2 | -11.3 | 62.5 | 1,347.58 | 1.2 | -17.9 | 0.52 | 16/9 | not checked |
| 691 | `{"fast": 11, "slow": 240, "trailing_stop_pct": 5}` | 3,104.34 | 1.7 | -9.4 | 62.5 | 1,954.09 | 1.6 | -14.5 | 0.96 | 16/9 | not checked |
| 421 | `{"fast": 11, "slow": 270, "trailing_stop_pct": 4}` | 1,665.54 | 1.0 | -9.3 | 42.9 | 2,636.18 | 2.2 | -10.0 | 2.21 | 14/11 | not checked |
| 255 | `{"fast": 55, "slow": 220, "trailing_stop_pct": 4}` | 1,635.34 | 1.0 | -7.7 | 50.0 | 1,400.70 | 1.2 | -7.8 | 1.26 | 8/6 | not checked |
| 655 | `{"fast": 16, "slow": 290, "trailing_stop_pct": 4}` | 1,214.93 | 0.7 | -6.8 | 50.0 | 2,514.45 | 2.1 | -7.9 | 2.85 | 10/7 | not checked |
| 1037 | `{"fast": 21, "slow": 300, "trailing_stop_pct": 1}` | 1,189.82 | 0.7 | -2.1 | 66.7 | 211.11 | 0.2 | -1.6 | 0.27 | 9/6 | 0.80 |
| 1003 | `{"fast": 11, "slow": 270, "trailing_stop_pct": 1}` | 1,059.53 | 0.6 | -2.1 | 64.3 | 385.71 | 0.3 | -3.2 | 0.55 | 14/11 | not checked |
| 1107 | `{"fast": 16, "slow": 290, "trailing_stop_pct": 1}` | 256.60 | 0.2 | -1.6 | 40.0 | 345.05 | 0.3 | -1.8 | 1.94 | 10/7 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,128 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
