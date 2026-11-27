# aroon_trend_onset__broad: optimization summary

Updated 2026-11-25T18:52:04Z · backtest.py version `979cf22782` · 1,059 parameter sets tested with this version (1,059 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [aroon_trend_onset__broad__max-income__v002.md](aroon_trend_onset__broad__max-income__v002.md) | 1058 | `{"level": 65.0, "max_bars": 36, "n": 48, "stop_atr": 2.5, "take_profit_atr": 6.0}` | long XLV since 2026-10-16 00:00 @ 178.253457 |
| balanced | [aroon_trend_onset__broad__balanced__v002.md](aroon_trend_onset__broad__balanced__v002.md) | 1059 | `{"level": 65.0, "max_bars": 48, "n": 48, "stop_atr": 2.5, "take_profit_atr": 6.0}` | long XLV since 2026-10-16 00:00 @ 178.253457 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,420.54 | 1,848.73 | 1,433.67 | 2,464.09 |
| return % | 14.21 | 18.49 | 14.34 | 24.64 |
| return %/year | 0.6 | 1.6 | 0.6 | 2.0 |
| gross profit | 3,700.88 | 4,319.13 | 3,861.18 | 5,018.24 |
| gross loss | 2,280.34 | 2,470.40 | 2,427.50 | 2,554.15 |
| trades | 711 | 764 | 688 | 725 |
| win rate % | 49.9 | 51.8 | 47.7 | 50.2 |
| avg win | 10.43 | 10.91 | 11.77 | 13.79 |
| avg loss | -6.41 | -6.71 | -6.74 | -7.08 |
| avg result / trade | 2.00 | 2.42 | 2.08 | 3.40 |
| largest single loss | -27.85 | -58.23 | -28.20 | -93.22 |
| largest loss % of equity | -14.76 | -9.90 | -10.85 | -9.90 |
| max drawdown | -370.08 | -486.76 | -368.16 | -511.15 |
| max drawdown % | -3.15 | -4.14 | -3.13 | -4.14 |
| profit factor | 1.62 | 1.75 | 1.59 | 1.97 |
| unusually bad trades | 38 | 38 | 35 | 39 |
| … threshold (% of equity) | 5.6 | 5.4 | 6.0 | 5.5 |
| time in market % | 5.9 | 11.8 | 6.6 | 12.7 |
| buy & hold return % | 100.07 | 303.60 | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.49 |  | 3.19 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.2 |
| 1996 | 0.2 | 0.2 |
| 1997 | 0.1 | 0.1 |
| 1998 | 0.0 | 0.0 |
| 1999 | -0.1 | -0.1 |
| 2000 | -0.0 | -0.4 |
| 2001 | -0.3 | -0.5 |
| 2002 | 0.3 | -0.4 |
| 2003 | 3.0 | 2.9 |
| 2004 | 0.6 | 0.9 |
| 2005 | -0.3 | -0.6 |
| 2006 | 0.5 | 1.0 |
| 2007 | 0.3 | 0.3 |
| 2008 | 0.4 | 0.3 |
| 2009 | 2.7 | 3.7 |
| 2010 | 3.5 | 2.8 |
| 2011 | 0.1 | 0.0 |
| 2012 | 2.7 | 2.5 |
| 2013 | 2.0 | 2.5 |
| 2014 | -0.1 | 0.2 |
| 2015 | -2.1 | -1.9 |
| 2016 (OOS) | -0.7 | -1.3 |
| 2017 (OOS) | 2.9 | 2.8 |
| 2018 (OOS) | 1.1 | 1.5 |
| 2019 (OOS) | 6.4 | 7.4 |
| 2020 (OOS) | 10.2 | 9.3 |
| 2021 (OOS) | 1.3 | 2.1 |
| 2022 (OOS) | -2.2 | -2.5 |
| 2023 (OOS) | 0.3 | 2.0 |
| 2024 (OOS) | 0.5 | 2.2 |
| 2025 (OOS) | 2.2 | 2.8 |
| 2026 (OOS) | -2.8 | -3.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 3.1% from a peak in-sample and 4.1% out-of-sample, and the worst single trade cost 9.9% of the account out-of-sample. About 50 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.1% from a peak in-sample and 4.1% out-of-sample, and the worst single trade cost 9.9% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 551 | `{"level": 65.0, "max_bars": 48, "n": 48, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 1,433.67 | 0.6 | -3.1 | 47.7 | 2,464.09 | 2.0 | -4.1 | 3.19 | 688/725 | 1.00 |
| 1042 | `{"level": 65.0, "max_bars": 36, "n": 48, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 1,366.92 | 0.6 | -3.0 | 51.8 | 1,986.35 | 1.7 | -5.2 | 2.75 | 706/757 | not checked |
| 478 | `{"level": 60.0, "max_bars": 36, "n": 48, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 1,334.74 | 0.6 | -3.0 | 51.0 | 1,833.60 | 1.6 | -4.1 | 2.60 | 634/654 | not checked |
| 511 | `{"level": 60.0, "max_bars": 36, "n": 48, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 1,331.05 | 0.6 | -3.0 | 51.0 | 1,870.23 | 1.6 | -5.0 | 2.65 | 634/654 | not checked |
| 418 | `{"level": 60.0, "max_bars": 36, "n": 48, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 1,263.35 | 0.6 | -3.0 | 52.6 | 1,925.49 | 1.6 | -5.2 | 2.86 | 631/650 | not checked |
| 468 | `{"level": 60.0, "max_bars": 36, "n": 46, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 1,201.13 | 0.5 | -2.9 | 53.3 | 2,233.84 | 1.9 | -3.9 | 3.46 | 628/680 | not checked |
| 524 | `{"level": 60.0, "max_bars": 36, "n": 46, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 1,152.78 | 0.5 | -2.9 | 53.0 | 2,183.24 | 1.8 | -4.9 | 3.52 | 628/680 | not checked |
| 459 | `{"level": 60.0, "max_bars": 24, "n": 48, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 908.22 | 0.4 | -2.9 | 54.3 | 933.33 | 0.8 | -5.0 | 2.00 | 654/678 | not checked |
| 461 | `{"level": 60.0, "max_bars": 24, "n": 48, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 880.69 | 0.4 | -2.8 | 55.4 | 953.53 | 0.8 | -5.1 | 2.10 | 654/677 | not checked |
| 480 | `{"level": 60.0, "max_bars": 24, "n": 46, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 774.18 | 0.4 | -2.8 | 54.6 | 1,320.04 | 1.1 | -4.8 | 3.19 | 658/707 | not checked |
| 490 | `{"level": 60.0, "max_bars": 24, "n": 46, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 769.07 | 0.3 | -2.7 | 55.8 | 1,316.16 | 1.1 | -4.8 | 3.26 | 658/706 | not checked |
| 394 | `{"level": 67.5, "max_bars": 72, "n": 46, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 665.03 | 0.3 | -2.5 | 64.7 | 1,114.07 | 1.0 | -1.8 | 3.16 | 791/873 | not checked |
| 412 | `{"level": 67.5, "max_bars": 48, "n": 46, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 638.31 | 0.3 | -2.2 | 62.6 | 1,043.72 | 0.9 | -1.9 | 3.07 | 802/885 | not checked |
| 634 | `{"level": 60.0, "max_bars": 12, "n": 48, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 596.66 | 0.3 | -2.1 | 56.7 | 782.86 | 0.7 | -1.8 | 2.46 | 660/690 | not checked |
| 734 | `{"level": 60.0, "max_bars": 12, "n": 48, "stop_atr": 2.25, "take_profit_atr": 7.0}` | 526.34 | 0.2 | -2.1 | 55.5 | 771.00 | 0.7 | -2.1 | 2.83 | 660/690 | not checked |
| 1050 | `{"level": 60.0, "max_bars": 12, "n": 48, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 494.56 | 0.2 | -1.9 | 53.9 | 735.11 | 0.7 | -2.2 | 2.83 | 660/690 | not checked |
| 414 | `{"level": 65.0, "max_bars": 84, "n": 50, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 67.02 | 0.0 | -1.6 | 43.7 | 318.20 | 0.3 | -1.3 | 9.67 | 727/761 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,059 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
