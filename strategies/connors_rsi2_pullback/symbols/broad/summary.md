# connors_rsi2_pullback__broad: optimization summary

Updated 2026-11-25T15:34:22Z · backtest.py version `e3108d629a` · 813 parameter sets tested with this version (813 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [connors_rsi2_pullback__broad__max-income__v002.md](connors_rsi2_pullback__broad__max-income__v002.md) | 813 | `{"buy": 9, "max_bars": 8, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-19 00:00 @ 180.454114; long XLP since 2026-11-20 00:00 @ 90.957279; long DBC since 2026-11-17 00:00 @ 30.399116; long VIG since 2026-11-18 00:00 @ 245.57365; long SCHD since 2026-11-19 00:00 @ 34.690404; long VNQ since 2026-11-18 00:00 @ 94.208254; long VTV since 2026-11-18 00:00 @ 222.906848; long CSSMI.SW since 2026-11-20 00:00 @ 152.385698 |
| balanced | [connors_rsi2_pullback__broad__balanced__v001.md](connors_rsi2_pullback__broad__balanced__v001.md) | 301 | `{"buy": 8, "max_bars": 12, "n": 2, "stop_atr": 2.5, "take_profit_atr": 3.0}` | long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-19 00:00 @ 180.454114; long XLP since 2026-11-20 00:00 @ 90.957279; long SCHD since 2026-11-19 00:00 @ 34.690404; long VNQ since 2026-11-18 00:00 @ 94.208254; long CSSMI.SW since 2026-11-20 00:00 @ 152.385698 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,097.08 | 572.51 | 1,822.97 | 642.00 |
| return % | 20.97 | 5.73 | 18.23 | 6.42 |
| return %/year | 0.9 | 0.5 | 0.8 | 0.6 |
| gross profit | 6,506.15 | 5,510.56 | 6,036.25 | 5,400.15 |
| gross loss | 4,409.07 | 4,938.05 | 4,213.28 | 4,758.15 |
| trades | 3,823 | 3,965 | 3,492 | 3,683 |
| win rate % | 63.7 | 62.8 | 63.5 | 62.5 |
| avg win | 2.67 | 2.21 | 2.72 | 2.35 |
| avg loss | -3.18 | -3.34 | -3.31 | -3.44 |
| avg result / trade | 0.55 | 0.14 | 0.52 | 0.17 |
| largest single loss | -45.72 | -39.35 | -35.41 | -40.31 |
| largest loss % of equity | -22.29 | -18.57 | -8.99 | -13.52 |
| max drawdown | -481.99 | -1,052.83 | -306.46 | -787.00 |
| max drawdown % | -4.16 | -10.20 | -2.73 | -7.68 |
| profit factor | 1.48 | 1.12 | 1.43 | 1.14 |
| unusually bad trades | 327 | 419 | 387 | 520 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.1 |
| time in market % | 4.6 | 8.9 | 3.8 | 7.3 |
| buy & hold return % | 100.07 | 303.60 | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.56 |  | 0.71 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.1 |
| 1996 | 0.0 | 0.0 |
| 1997 | 0.6 | 0.5 |
| 1998 | 0.3 | 0.3 |
| 1999 | 0.3 | 0.3 |
| 2000 | 0.3 | -0.3 |
| 2001 | 0.4 | 0.2 |
| 2002 | -0.3 | -0.2 |
| 2003 | 2.0 | 2.0 |
| 2004 | 0.4 | 0.3 |
| 2005 | -0.1 | -0.1 |
| 2006 | 0.8 | 0.9 |
| 2007 | 1.3 | 1.3 |
| 2008 | -0.9 | -0.4 |
| 2009 | 4.8 | 4.0 |
| 2010 | 2.0 | 0.7 |
| 2011 | -1.1 | -0.2 |
| 2012 | 2.9 | 3.2 |
| 2013 | 3.4 | 3.2 |
| 2014 | 1.1 | 1.5 |
| 2015 | 0.8 | -0.3 |
| 2016 (OOS) | 1.5 | 1.0 |
| 2017 (OOS) | 2.1 | 1.7 |
| 2018 (OOS) | -6.6 | -4.2 |
| 2019 (OOS) | -0.5 | -0.2 |
| 2020 (OOS) | -0.4 | -0.7 |
| 2021 (OOS) | 5.5 | 3.6 |
| 2022 (OOS) | -1.7 | -1.5 |
| 2023 (OOS) | -0.1 | 0.4 |
| 2024 (OOS) | 2.7 | 3.3 |
| 2025 (OOS) | 4.5 | 4.4 |
| 2026 (OOS) | 0.7 | -0.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.2% from a peak in-sample and 10.2% out-of-sample, and the worst single trade cost 18.6% of the account out-of-sample. About 64 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 0.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 98% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 2.7% from a peak in-sample and 7.7% out-of-sample, and the worst single trade cost 13.5% of the account out-of-sample. About 64 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 475 | `{"buy": 9, "max_bars": 24, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,191.77 | 0.9 | -4.5 | 63.8 | 657.78 | 0.6 | -10.2 | 0.62 | 3796/3950 | not checked |
| 521 | `{"buy": 9, "max_bars": 22, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,191.77 | 0.9 | -4.5 | 63.8 | 657.78 | 0.6 | -10.2 | 0.62 | 3796/3950 | not checked |
| 576 | `{"buy": 9, "max_bars": 20, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,191.77 | 0.9 | -4.5 | 63.8 | 657.78 | 0.6 | -10.2 | 0.62 | 3796/3950 | not checked |
| 622 | `{"buy": 9, "max_bars": 18, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,191.77 | 0.9 | -4.5 | 63.8 | 657.78 | 0.6 | -10.2 | 0.62 | 3796/3950 | not checked |
| 688 | `{"buy": 9, "max_bars": 16, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,191.77 | 0.9 | -4.5 | 63.8 | 657.78 | 0.6 | -10.2 | 0.62 | 3796/3950 | not checked |
| 716 | `{"buy": 9, "max_bars": 14, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,191.77 | 0.9 | -4.5 | 63.8 | 651.52 | 0.6 | -10.2 | 0.61 | 3796/3950 | not checked |
| 476 | `{"buy": 9, "max_bars": 24, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 2,180.52 | 0.9 | -4.2 | 63.8 | 645.28 | 0.6 | -9.9 | 0.62 | 3800/3955 | not checked |
| 496 | `{"buy": 9, "max_bars": 22, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 2,180.52 | 0.9 | -4.2 | 63.8 | 645.28 | 0.6 | -9.9 | 0.62 | 3800/3955 | not checked |
| 594 | `{"buy": 9, "max_bars": 20, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 2,180.52 | 0.9 | -4.2 | 63.8 | 645.28 | 0.6 | -9.9 | 0.62 | 3800/3955 | not checked |
| 641 | `{"buy": 9, "max_bars": 18, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 2,180.52 | 0.9 | -4.2 | 63.8 | 645.28 | 0.6 | -9.9 | 0.62 | 3800/3955 | not checked |
| 652 | `{"buy": 9, "max_bars": 16, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 2,180.52 | 0.9 | -4.2 | 63.8 | 645.28 | 0.6 | -9.9 | 0.62 | 3800/3955 | not checked |
| 311 | `{"buy": 9, "max_bars": 8, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 2,097.08 | 0.9 | -4.2 | 63.7 | 572.51 | 0.5 | -10.2 | 0.56 | 3823/3965 | 1.00 |
| 91 | `{"buy": 9, "max_bars": 8, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 2,079.00 | 0.9 | -4.0 | 63.7 | 567.18 | 0.5 | -9.9 | 0.57 | 3825/3970 | not checked |
| 378 | `{"buy": 9, "max_bars": 24, "n": 2, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 1,947.27 | 0.8 | -3.8 | 63.7 | 686.24 | 0.6 | -9.0 | 0.72 | 3823/3968 | not checked |
| 539 | `{"buy": 9, "max_bars": 24, "n": 2, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 1,886.61 | 0.8 | -3.4 | 63.6 | 633.41 | 0.6 | -9.1 | 0.69 | 3838/3989 | not checked |
| 391 | `{"buy": 8, "max_bars": 24, "n": 2, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 1,854.55 | 0.8 | -2.7 | 63.5 | 586.35 | 0.5 | -7.8 | 0.64 | 3491/3683 | not checked |
| 400 | `{"buy": 8, "max_bars": 22, "n": 2, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 1,854.55 | 0.8 | -2.7 | 63.5 | 586.35 | 0.5 | -7.8 | 0.64 | 3491/3683 | not checked |
| 451 | `{"buy": 8, "max_bars": 20, "n": 2, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 1,854.55 | 0.8 | -2.7 | 63.5 | 586.35 | 0.5 | -7.8 | 0.64 | 3491/3683 | not checked |
| 502 | `{"buy": 9, "max_bars": 24, "n": 2, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 1,798.42 | 0.8 | -2.7 | 63.3 | 559.22 | 0.5 | -8.6 | 0.63 | 3905/4069 | not checked |
| 421 | `{"buy": 7, "max_bars": 20, "n": 2, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 1,642.16 | 0.7 | -2.6 | 63.1 | 515.00 | 0.5 | -7.7 | 0.63 | 3014/3249 | not checked |
| 491 | `{"buy": 7, "max_bars": 24, "n": 2, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 1,642.16 | 0.7 | -2.6 | 63.1 | 515.00 | 0.5 | -7.7 | 0.63 | 3014/3249 | not checked |
| 32 | `{"buy": 8, "max_bars": 12, "n": 2, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 1,383.57 | 0.6 | -2.6 | 62.2 | 620.90 | 0.6 | -7.3 | 0.89 | 3550/3758 | not checked |
| 272 | `{"buy": 7, "max_bars": 10, "n": 2, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 1,332.89 | 0.6 | -2.6 | 62.0 | 525.76 | 0.5 | -6.7 | 0.78 | 3064/3305 | not checked |
| 623 | `{"buy": 8, "max_bars": 18, "n": 2, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 1,131.11 | 0.5 | -2.4 | 60.6 | 245.14 | 0.2 | -6.7 | 0.43 | 3607/3806 | not checked |
| 33 | `{"buy": 7, "max_bars": 12, "n": 2, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 1,092.35 | 0.5 | -2.4 | 60.4 | 281.90 | 0.3 | -6.6 | 0.52 | 3108/3351 | not checked |

(15 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 813 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
