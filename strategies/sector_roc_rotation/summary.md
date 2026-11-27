# sector_roc_rotation: optimization summary

Updated 2026-11-27T12:43:14Z · backtest.py version `0771a883af` · 12,688 parameter sets tested with this version (12,688 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d bars)
- In-sample (tuning): 2000-07-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [sector_roc_rotation__max-income__v002.md](sector_roc_rotation__max-income__v002.md) | 12686 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 21}` | long XLE since 2026-08-03 00:00 @ 58.360707 |
| balanced | [sector_roc_rotation__balanced__v002.md](sector_roc_rotation__balanced__v002.md) | 12687 | `{"k": 8, "max_candles": 210, "n": 252, "stop_loss_pct": 9}` | long XLB since 2026-05-01 00:00 @ 51.094857; long XLE since 2026-07-01 00:00 @ 52.869212; long XLF since 2026-08-03 00:00 @ 56.974733; long XLP since 2026-08-03 00:00 @ 85.305741; long XLRE since 2026-07-01 00:00 @ 43.597807; long XLV since 2026-06-01 00:00 @ 147.348317 |
| safe-starter | [sector_roc_rotation__safe-starter__v002.md](sector_roc_rotation__safe-starter__v002.md) | 12688 | `{"k": 8, "max_candles": 189, "n": 357, "stop_loss_pct": 2}` | long XLB since 2026-10-01 00:00 @ 48.354502; long XLE since 2026-07-01 00:00 @ 53.081374; long XLF since 2026-10-01 00:00 @ 53.265975; long XLP since 2026-11-02 00:00 @ 89.866948; long XLU since 2026-11-02 00:00 @ 43.322994; long XLV since 2026-07-01 00:00 @ 159.133946 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 43,704.04 | 6,167.91 | 27,927.00 | 11,006.81 | 12,204.72 | 8,216.42 |
| return % | 437.04 | 61.68 | 279.27 | 110.07 | 122.05 | 82.16 |
| return %/year | 11.5 | 4.5 | 9.0 | 7.1 | 5.3 | 5.7 |
| gross profit | 74,014.28 | 24,831.35 | 34,408.12 | 19,419.70 | 22,677.01 | 16,471.25 |
| gross loss | 30,310.24 | 18,663.44 | 6,481.12 | 8,412.89 | 10,472.30 | 8,254.83 |
| trades | 59 | 49 | 160 | 179 | 325 | 310 |
| win rate % | 62.7 | 49.0 | 68.1 | 54.2 | 28.6 | 26.8 |
| avg win | 2,000.39 | 1,034.64 | 315.67 | 200.20 | 243.84 | 198.45 |
| avg loss | -1,377.74 | -746.54 | -127.08 | -102.60 | -45.14 | -36.36 |
| avg result / trade | 740.75 | 125.88 | 174.54 | 61.49 | 37.55 | 26.50 |
| largest single loss | -5,200.40 | -2,525.82 | -482.63 | -253.67 | -150.25 | -76.35 |
| largest loss % of equity | -8.53 | -12.38 | -1.22 | -1.20 | -0.64 | -0.42 |
| max drawdown | -8,938.31 | -6,225.73 | -2,587.24 | -3,738.46 | -2,055.12 | -2,181.78 |
| max drawdown % | -19.88 | -29.17 | -11.10 | -20.32 | -8.50 | -16.56 |
| profit factor | 2.44 | 1.33 | 5.31 | 2.31 | 2.17 | 2.00 |
| unusually bad trades | 2 | 5 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 7.3 | 7.2 | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 6.1 | 7.5 | 46.9 | 58.2 | 39.8 | 47.7 |
| buy & hold return % | 139.85 | 244.45 | 139.85 | 244.45 | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.39 |  | 0.79 |  | 1.07 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 13.7 | 4.3 | 3.6 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | -4.1 | -3.1 | -1.7 |
| 2003 | 39.9 | 22.9 | 14.4 |
| 2004 | 7.8 | 12.6 | 11.1 |
| 2005 | 28.5 | 3.2 | 0.9 |
| 2006 | 3.0 | 14.5 | 15.1 |
| 2007 | 39.4 | 11.5 | 5.1 |
| 2008 | 0.7 | -0.0 | -0.1 |
| 2009 | 9.9 | 14.3 | 4.5 |
| 2010 | 13.5 | 9.0 | 7.2 |
| 2011 | 9.2 | 3.0 | 1.0 |
| 2012 | -10.4 | 11.2 | 6.3 |
| 2013 | 41.5 | 28.4 | 20.2 |
| 2014 | 2.1 | 14.1 | 3.2 |
| 2015 | -0.3 | -1.3 | -5.7 |
| 2016 (OOS) | 9.0 | 6.7 | 6.2 |
| 2017 (OOS) | 6.5 | 16.6 | 13.9 |
| 2018 (OOS) | -6.0 | -6.5 | -6.9 |
| 2019 (OOS) | 18.8 | 6.9 | 5.1 |
| 2020 (OOS) | 32.7 | 14.4 | 12.5 |
| 2021 (OOS) | 15.8 | 25.7 | 19.1 |
| 2022 (OOS) | -6.9 | -14.1 | -9.3 |
| 2023 (OOS) | -8.6 | 2.3 | 1.5 |
| 2024 (OOS) | 5.3 | 16.1 | 11.4 |
| 2025 (OOS) | 0.7 | 9.2 | 7.7 |
| 2026 (OOS) | -11.7 | 3.8 | 3.9 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 19.9% from a peak in-sample and 29.2% out-of-sample, and the worst single trade cost 12.4% of the account out-of-sample. About 63 of every 100 trades won in-sample. Out-of-sample it earned 4.5% a year against 11.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 34% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 11.1% from a peak in-sample and 20.3% out-of-sample, and the worst single trade cost 1.2% of the account out-of-sample. About 68 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 49% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 8.5% from a peak in-sample and 16.6% out-of-sample, and the worst single trade cost 0.4% of the account out-of-sample. About 29 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 60% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8822 | `{"k": 2, "max_candles": 189, "n": 294, "stop_loss_pct": 23}` | 45,300.73 | 11.7 | -22.0 | 68.5 | 14,190.50 | 8.4 | -23.8 | 0.72 | 73/67 | not checked |
| 8846 | `{"k": 2, "max_candles": 189, "n": 294, "stop_loss_pct": 25}` | 45,300.73 | 11.7 | -22.0 | 68.5 | 14,190.50 | 8.4 | -23.8 | 0.72 | 73/67 | not checked |
| 8901 | `{"k": 2, "max_candles": 189, "n": 294, "stop_loss_pct": 24}` | 45,300.73 | 11.7 | -22.0 | 68.5 | 14,190.50 | 8.4 | -23.8 | 0.72 | 73/67 | not checked |
| 558 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 20}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | not checked |
| 559 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 22}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | not checked |
| 562 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 21}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | 1.00 |
| 680 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 19}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | not checked |
| 701 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 23}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | not checked |
| 709 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 24}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | not checked |
| 718 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 25}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 6,167.91 | 4.5 | -29.2 | 0.39 | 59/49 | not checked |
| 726 | `{"k": 1, "max_candles": 147, "n": 189, "stop_loss_pct": 18}` | 43,704.04 | 11.5 | -19.9 | 62.7 | 5,113.08 | 3.9 | -33.4 | 0.34 | 59/49 | not checked |
| 9901 | `{"k": 2, "max_candles": 189, "n": 294, "stop_loss_pct": 11}` | 40,617.58 | 11.0 | -15.7 | 68.0 | 12,469.17 | 7.7 | -25.8 | 0.70 | 75/69 | not checked |
| 476 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 22}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 498 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 21}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 542 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 24}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 673 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 20}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 681 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 23}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 772 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 19}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 1029 | `{"k": 2, "max_candles": 147, "n": 210, "stop_loss_pct": 25}` | 38,552.38 | 10.7 | -15.6 | 64.7 | 7,629.40 | 5.3 | -24.6 | 0.50 | 85/74 | not checked |
| 9590 | `{"k": 4, "max_candles": 168, "n": 294, "stop_loss_pct": 21}` | 36,006.92 | 10.3 | -15.3 | 68.2 | 10,468.58 | 6.8 | -21.1 | 0.66 | 129/120 | not checked |
| 11117 | `{"k": 4, "max_candles": 168, "n": 294, "stop_loss_pct": 17}` | 35,522.75 | 10.3 | -15.1 | 68.2 | 10,235.88 | 6.7 | -21.1 | 0.65 | 129/120 | not checked |
| 793 | `{"k": 2, "max_candles": 168, "n": 168, "stop_loss_pct": 25}` | 34,298.24 | 10.1 | -14.1 | 66.7 | 11,269.16 | 7.2 | -23.9 | 0.71 | 99/91 | not checked |
| 6717 | `{"k": 5, "max_candles": 189, "n": 210, "stop_loss_pct": 9}` | 32,677.13 | 9.8 | -12.6 | 68.6 | 8,476.24 | 5.8 | -25.5 | 0.59 | 140/143 | not checked |
| 9738 | `{"k": 7, "max_candles": 210, "n": 231, "stop_loss_pct": 14}` | 31,082.16 | 9.6 | -12.0 | 69.5 | 11,109.00 | 7.1 | -19.9 | 0.74 | 154/167 | not checked |
| 4356 | `{"k": 6, "max_candles": 210, "n": 336, "stop_loss_pct": 13}` | 30,745.24 | 9.5 | -11.9 | 65.1 | 6,966.66 | 5.0 | -22.6 | 0.53 | 152/134 | not checked |

(14 more on the front, see results.csv)


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 12,688 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
