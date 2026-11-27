# cci_correction_recovery__broad: optimization summary

Updated 2026-11-25T17:40:23Z · backtest.py version `a123d82c08` · 828 parameter sets tested with this version (828 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cci_correction_recovery__broad__max-income__v002.md](cci_correction_recovery__broad__max-income__v002.md) | 827 | `{"max_bars": 14, "n": 7, "stop_atr": 5.75, "take_profit_atr": 3.0}` | long XLV since 2026-11-24 00:00 @ 179.703889; long XLP since 2026-11-23 00:00 @ 89.516845; long XLU since 2026-11-24 00:00 @ 43.122934; long VNQ since 2026-11-24 00:00 @ 93.207954; long CSSMI.SW since 2026-11-24 00:00 @ 152.985884 |
| balanced | [cci_correction_recovery__broad__balanced__v002.md](cci_correction_recovery__broad__balanced__v002.md) | 828 | `{"max_bars": 8, "n": 9, "stop_atr": 4.5, "take_profit_atr": 3.5}` | long XLF since 2026-11-24 00:00 @ 55.526651; long XLV since 2026-11-24 00:00 @ 179.703889; long XLY since 2026-11-19 00:00 @ 119.625873; long XLP since 2026-11-23 00:00 @ 89.516845; long XLU since 2026-11-24 00:00 @ 43.122934; long SCHD since 2026-11-24 00:00 @ 34.38031; long VNQ since 2026-11-24 00:00 @ 93.207954 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,328.39 | 230.76 | 1,173.18 | 307.42 |
| return % | 13.28 | 2.31 | 11.73 | 3.07 |
| return %/year | 0.6 | 0.2 | 0.5 | 0.3 |
| gross profit | 8,535.04 | 7,033.81 | 6,994.78 | 6,459.36 |
| gross loss | 7,206.65 | 6,803.06 | 5,821.60 | 6,151.94 |
| trades | 4,260 | 4,239 | 3,633 | 3,685 |
| win rate % | 59.4 | 57.6 | 57.8 | 58.0 |
| avg win | 3.37 | 2.88 | 3.33 | 3.02 |
| avg loss | -4.17 | -3.78 | -3.79 | -3.98 |
| avg result / trade | 0.31 | 0.05 | 0.32 | 0.08 |
| largest single loss | -55.83 | -42.81 | -38.68 | -69.05 |
| largest loss % of equity | -25.95 | -14.39 | -14.16 | -15.93 |
| max drawdown | -792.97 | -976.26 | -482.07 | -1,249.18 |
| max drawdown % | -6.69 | -9.44 | -4.21 | -11.64 |
| profit factor | 1.18 | 1.03 | 1.20 | 1.05 |
| unusually bad trades | 452 | 428 | 448 | 398 |
| … threshold (% of equity) | 2.5 | 2.8 | 2.1 | 2.8 |
| time in market % | 6.5 | 12.1 | 5.7 | 10.6 |
| buy & hold return % | 102.62 | 303.60 | 102.62 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.35 |  | 0.53 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.1 |
| 1996 | 0.1 | 0.2 |
| 1997 | -0.1 | -0.1 |
| 1998 | -0.1 | -0.1 |
| 1999 | 0.3 | 0.1 |
| 2000 | 0.4 | 0.2 |
| 2001 | 0.6 | -0.6 |
| 2002 | -0.3 | 0.5 |
| 2003 | 3.5 | 3.3 |
| 2004 | 1.3 | 1.5 |
| 2005 | -0.8 | -0.5 |
| 2006 | 2.3 | 2.4 |
| 2007 | 1.6 | 1.5 |
| 2008 | 0.6 | -0.2 |
| 2009 | 6.4 | 4.4 |
| 2010 | -2.8 | -2.9 |
| 2011 | -2.1 | -0.4 |
| 2012 | 6.7 | 3.4 |
| 2013 | 0.5 | 1.8 |
| 2014 | -0.5 | 0.7 |
| 2015 | -4.6 | -3.7 |
| 2016 (OOS) | 2.1 | 2.6 |
| 2017 (OOS) | -0.1 | 1.9 |
| 2018 (OOS) | -4.1 | -1.9 |
| 2019 (OOS) | 1.1 | 1.1 |
| 2020 (OOS) | 2.9 | 1.0 |
| 2021 (OOS) | -0.8 | 1.2 |
| 2022 (OOS) | -4.8 | -8.3 |
| 2023 (OOS) | -2.1 | -1.3 |
| 2024 (OOS) | 0.6 | 0.9 |
| 2025 (OOS) | 4.2 | 3.8 |
| 2026 (OOS) | 3.8 | 3.4 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 6.7% from a peak in-sample and 9.4% out-of-sample, and the worst single trade cost 14.4% of the account out-of-sample. About 59 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.2% from a peak in-sample and 11.6% out-of-sample, and the worst single trade cost 15.9% of the account out-of-sample. About 58 of every 100 trades won in-sample. Out-of-sample it earned 0.3% a year against 0.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 86% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 354 | `{"max_bars": 10, "n": 7, "stop_atr": 5.75, "take_profit_atr": 3.5}` | 1,370.50 | 0.6 | -6.0 | 59.0 | 182.43 | 0.2 | -9.1 | 0.28 | 4293/4278 | 0.88 |
| 443 | `{"max_bars": 10, "n": 7, "stop_atr": 5.25, "take_profit_atr": 2.5}` | 1,362.30 | 0.6 | -5.7 | 59.0 | 185.21 | 0.2 | -8.8 | 0.28 | 4297/4283 | not checked |
| 589 | `{"max_bars": 10, "n": 9, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 1,255.90 | 0.6 | -5.2 | 59.4 | 378.94 | 0.3 | -12.2 | 0.60 | 3563/3594 | not checked |
| 818 | `{"max_bars": 10, "n": 9, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 1,250.87 | 0.6 | -5.2 | 59.3 | 198.94 | 0.2 | -12.0 | 0.32 | 3572/3632 | not checked |
| 587 | `{"max_bars": 8, "n": 9, "stop_atr": 4.5, "take_profit_atr": 3.5}` | 1,173.18 | 0.5 | -4.2 | 57.8 | 307.42 | 0.3 | -11.6 | 0.53 | 3633/3685 | 1.00 |
| 583 | `{"max_bars": 8, "n": 9, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 1,170.14 | 0.5 | -4.1 | 57.8 | 392.24 | 0.3 | -11.7 | 0.66 | 3630/3677 | not checked |
| 801 | `{"max_bars": 8, "n": 9, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 1,145.86 | 0.5 | -4.1 | 57.6 | 245.82 | 0.2 | -11.5 | 0.42 | 3639/3711 | not checked |
| 808 | `{"max_bars": 8, "n": 9, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 1,096.39 | 0.5 | -4.1 | 57.6 | 173.24 | 0.2 | -12.0 | 0.32 | 3646/3729 | not checked |
| 813 | `{"max_bars": 8, "n": 9, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 1,064.20 | 0.5 | -4.1 | 57.6 | 188.46 | 0.2 | -12.0 | 0.35 | 3646/3729 | not checked |
| 554 | `{"max_bars": 6, "n": 29, "stop_atr": 1.0, "take_profit_atr": 4.0}` | 294.06 | 0.1 | -3.9 | 43.0 | 272.66 | 0.2 | -4.4 | 1.79 | 1992/2057 | not checked |
| 611 | `{"max_bars": 6, "n": 29, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 259.85 | 0.1 | -3.9 | 43.0 | 217.97 | 0.2 | -4.5 | 1.67 | 1992/2057 | not checked |
| 612 | `{"max_bars": 6, "n": 29, "stop_atr": 1.25, "take_profit_atr": 4.0}` | 211.25 | 0.1 | -3.7 | 46.7 | 360.86 | 0.3 | -4.2 | 3.30 | 1936/2002 | not checked |
| 607 | `{"max_bars": 6, "n": 29, "stop_atr": 1.25, "take_profit_atr": 3.0}` | 181.13 | 0.1 | -3.6 | 46.8 | 306.57 | 0.3 | -4.3 | 3.11 | 1936/2002 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 828 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
