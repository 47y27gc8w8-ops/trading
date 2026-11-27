# golden_cross_ws__XLY: optimization summary

Updated 2026-11-23T22:10:19Z · backtest.py version `30de6bbbac` · 879 parameter sets tested with this version (879 rows in results.csv in total) · last run ended: converged: no profile improved in the last 540 iterations at the smallest step size

## Setup

- Data: XLY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-20
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 5 in-sample and ≥ 2 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross_ws__XLY__max-income__v002.md](golden_cross_ws__XLY__max-income__v002.md) | 878 | `{"fast": 75, "slow": 290, "trailing_stop_pct": 21}` | flat (data up to 2026-11-23 00:00) |
| balanced | [golden_cross_ws__XLY__balanced__v001.md](golden_cross_ws__XLY__balanced__v001.md) | 224 | `{"fast": 20, "slow": 210, "trailing_stop_pct": 21}` | long XLY since 2026-11-10 00:00 @ 120.216054 |
| safe-starter | [golden_cross_ws__XLY__safe-starter__v002.md](golden_cross_ws__XLY__safe-starter__v002.md) | 879 | `{"fast": 100, "slow": 220, "trailing_stop_pct": 8}` | flat (data up to 2026-11-23 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 22,632.12 | 5,985.53 | 19,818.21 | 14,038.03 | 4,731.52 | 2,504.82 |
| return % | 226.32 | 59.86 | 198.18 | 140.38 | 47.32 | 25.05 |
| return %/year | 7.8 | 4.4 | 7.2 | 8.4 | 2.5 | 2.1 |
| gross profit | 25,817.29 | 7,175.80 | 23,250.61 | 20,912.92 | 6,373.94 | 3,505.26 |
| gross loss | 3,185.17 | 1,190.27 | 3,432.40 | 6,874.89 | 1,642.42 | 1,000.45 |
| trades | 8 | 4 | 17 | 9 | 11 | 6 |
| win rate % | 62.5 | 75.0 | 58.8 | 44.4 | 63.6 | 33.3 |
| avg win | 5,163.46 | 2,391.93 | 2,325.06 | 5,228.23 | 910.56 | 1,752.63 |
| avg loss | -1,061.72 | -1,190.27 | -490.34 | -1,374.98 | -410.61 | -250.11 |
| avg result / trade | 2,829.02 | 1,496.38 | 1,165.78 | 1,559.78 | 430.14 | 417.47 |
| largest single loss | -1,571.80 | -1,190.27 | -1,487.55 | -1,925.98 | -507.97 | -523.16 |
| largest loss % of equity | -14.37 | -9.71 | -16.41 | -9.18 | -4.50 | -3.92 |
| max drawdown | -4,401.79 | -4,964.52 | -3,456.91 | -7,361.42 | -2,103.28 | -2,020.16 |
| max drawdown % | -35.86 | -28.36 | -29.64 | -23.44 | -17.15 | -14.00 |
| profit factor | 8.11 | 6.03 | 6.77 | 3.04 | 3.88 | 3.50 |
| unusually bad trades | 0 | 0 | 2 | 0 | 0 | 1 |
| … threshold (% of equity) | 26.5 | 19.4 | 6.2 | 11.9 | 7.1 | 3.6 |
| time in market % | 70.4 | 63.8 | 71.1 | 77.1 | 22.3 | 22.1 |
| buy & hold return % | 268.77 | 228.26 | 268.77 | 228.26 | 268.77 | 228.26 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.57 |  | 1.18 |  | 0.84 |
| period | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 9.3 | -9.4 | 4.6 |
| 2001 | -14.4 | -11.9 | 4.8 |
| 2002 | -13.2 | -6.5 | -3.6 |
| 2003 | 14.0 | 27.8 | 12.2 |
| 2004 | 12.9 | 8.4 | -1.9 |
| 2005 | -7.3 | -13.5 | -9.5 |
| 2006 | 3.0 | 15.2 | 2.1 |
| 2007 | -0.7 | -3.5 | -3.6 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 15.5 | 26.9 | 24.5 |
| 2010 | 27.5 | 21.4 | 11.8 |
| 2011 | 7.3 | -5.9 | 0.0 |
| 2012 | 21.5 | 23.6 | 2.2 |
| 2013 | 42.7 | 42.7 | 0.0 |
| 2014 | 9.5 | 6.1 | 0.0 |
| 2015 | 9.9 | 10.7 | 0.0 |
| 2016 (OOS) | 2.8 | -1.9 | 5.1 |
| 2017 (OOS) | 22.8 | 22.8 | 22.8 |
| 2018 (OOS) | -4.8 | 10.8 | 1.2 |
| 2019 (OOS) | 8.1 | 15.0 | -0.1 |
| 2020 (OOS) | 0.7 | 8.6 | -1.3 |
| 2021 (OOS) | 27.9 | 27.9 | 0.0 |
| 2022 (OOS) | -17.1 | -9.1 | 0.0 |
| 2023 (OOS) | 8.3 | 10.6 | 3.4 |
| 2024 (OOS) | 26.5 | 26.5 | 0.0 |
| 2025 (OOS) | -17.5 | 2.6 | -3.9 |
| 2026 (OOS) | 0.0 | -20.2 | -2.4 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 35.9% from a peak in-sample and 28.4% out-of-sample, and the worst single trade cost 9.7% of the account out-of-sample. About 62 of every 100 trades won in-sample. Out-of-sample it earned 4.4% a year against 7.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 28% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 29.6% from a peak in-sample and 23.4% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 59 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 34% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 17.1% from a peak in-sample and 14.0% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 64 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 58% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 377 | `{"fast": 75, "slow": 290, "trailing_stop_pct": 21}` | 22,632.12 | 7.8 | -35.9 | 62.5 | 5,985.53 | 4.4 | -28.4 | 0.57 | 8/4 | 1.00 |
| 374 | `{"fast": 75, "slow": 300, "trailing_stop_pct": 21}` | 22,255.42 | 7.7 | -34.6 | 62.5 | 5,745.69 | 4.3 | -28.9 | 0.56 | 8/4 | not checked |
| 100 | `{"fast": 20, "slow": 210, "trailing_stop_pct": 21}` | 19,818.21 | 7.2 | -29.6 | 58.8 | 14,038.03 | 8.4 | -23.4 | 1.18 | 17/9 | 1.00 |
| 108 | `{"fast": 20, "slow": 210, "trailing_stop_pct": 22}` | 19,818.21 | 7.2 | -29.6 | 58.8 | 13,733.75 | 8.3 | -23.4 | 1.16 | 17/9 | not checked |
| 260 | `{"fast": 20, "slow": 210, "trailing_stop_pct": 24}` | 19,818.21 | 7.2 | -29.6 | 58.8 | 12,711.45 | 7.8 | -25.4 | 1.09 | 17/9 | not checked |
| 389 | `{"fast": 20, "slow": 210, "trailing_stop_pct": 23}` | 19,818.21 | 7.2 | -29.6 | 58.8 | 12,711.45 | 7.8 | -25.4 | 1.09 | 17/9 | not checked |
| 829 | `{"fast": 20, "slow": 160, "trailing_stop_pct": 24}` | 18,934.41 | 6.9 | -22.9 | 44.4 | 6,876.15 | 4.9 | -25.8 | 0.71 | 18/12 | not checked |
| 849 | `{"fast": 20, "slow": 160, "trailing_stop_pct": 22}` | 18,934.41 | 6.9 | -22.9 | 44.4 | 7,635.79 | 5.3 | -25.8 | 0.77 | 18/12 | not checked |
| 850 | `{"fast": 20, "slow": 160, "trailing_stop_pct": 25}` | 18,934.41 | 6.9 | -22.9 | 44.4 | 6,876.15 | 4.9 | -25.8 | 0.71 | 18/12 | not checked |
| 99 | `{"fast": 20, "slow": 190, "trailing_stop_pct": 21}` | 18,253.27 | 6.8 | -21.6 | 50.0 | 11,531.19 | 7.3 | -24.0 | 1.08 | 16/11 | not checked |
| 243 | `{"fast": 20, "slow": 190, "trailing_stop_pct": 24}` | 18,253.27 | 6.8 | -21.6 | 50.0 | 10,342.96 | 6.8 | -26.4 | 1.00 | 16/11 | not checked |
| 288 | `{"fast": 20, "slow": 190, "trailing_stop_pct": 23}` | 18,253.27 | 6.8 | -21.6 | 50.0 | 10,342.96 | 6.8 | -26.4 | 1.00 | 16/11 | not checked |
| 463 | `{"fast": 20, "slow": 190, "trailing_stop_pct": 25}` | 18,253.27 | 6.8 | -21.6 | 50.0 | 10,342.96 | 6.8 | -26.4 | 1.00 | 16/11 | not checked |
| 469 | `{"fast": 20, "slow": 190, "trailing_stop_pct": 22}` | 18,253.27 | 6.8 | -21.6 | 50.0 | 11,258.65 | 7.2 | -24.0 | 1.06 | 16/11 | not checked |
| 238 | `{"fast": 20, "slow": 160, "trailing_stop_pct": 16}` | 17,780.45 | 6.7 | -21.4 | 44.4 | 8,116.31 | 5.6 | -26.9 | 0.84 | 18/12 | not checked |
| 737 | `{"fast": 10, "slow": 200, "trailing_stop_pct": 13}` | 16,201.18 | 6.3 | -21.3 | 42.9 | 8,253.48 | 5.7 | -21.2 | 0.91 | 21/14 | not checked |
| 245 | `{"fast": 20, "slow": 160, "trailing_stop_pct": 11}` | 11,393.81 | 4.9 | -16.8 | 38.9 | 4,178.10 | 3.3 | -23.8 | 0.66 | 18/12 | not checked |
| 121 | `{"fast": 20, "slow": 250, "trailing_stop_pct": 9}` | 7,029.04 | 3.4 | -15.9 | 46.1 | 4,177.41 | 3.3 | -21.9 | 0.95 | 13/10 | not checked |
| 124 | `{"fast": 15, "slow": 250, "trailing_stop_pct": 8}` | 6,637.12 | 3.3 | -15.9 | 46.7 | 1,882.09 | 1.6 | -22.6 | 0.49 | 15/12 | not checked |
| 356 | `{"fast": 100, "slow": 210, "trailing_stop_pct": 8}` | 5,981.37 | 3.0 | -15.3 | 66.7 | 2,406.97 | 2.0 | -16.0 | 0.66 | 9/6 | not checked |
| 730 | `{"fast": 110, "slow": 200, "trailing_stop_pct": 8}` | 5,082.50 | 2.6 | -15.0 | 55.6 | 1,606.07 | 1.4 | -16.9 | 0.53 | 9/5 | not checked |
| 534 | `{"fast": 105, "slow": 210, "trailing_stop_pct": 8}` | 4,370.15 | 2.3 | -14.3 | 66.7 | 1,577.63 | 1.4 | -19.3 | 0.59 | 9/6 | not checked |
| 247 | `{"fast": 20, "slow": 250, "trailing_stop_pct": 4}` | 2,581.39 | 1.5 | -10.2 | 53.9 | 966.08 | 0.8 | -14.8 | 0.58 | 13/10 | not checked |
| 67 | `{"fast": 80, "slow": 280, "trailing_stop_pct": 4}` | 2,058.42 | 1.2 | -9.2 | 44.4 | 1,289.21 | 1.1 | -6.0 | 0.94 | 9/4 | not checked |
| 74 | `{"fast": 125, "slow": 180, "trailing_stop_pct": 3}` | 1,798.83 | 1.1 | -8.2 | 75.0 | 1,935.56 | 1.6 | -7.5 | 1.56 | 12/8 | not checked |

(2 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 879 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
