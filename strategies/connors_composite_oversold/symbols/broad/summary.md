# connors_composite_oversold__broad: optimization summary

Updated 2026-11-25T15:43:12Z · backtest.py version `0b5600ac10` · 996 parameter sets tested with this version (996 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [connors_composite_oversold__broad__max-income__v002.md](connors_composite_oversold__broad__max-income__v002.md) | 996 | `{"buy": 19, "exit": 77.5, "max_bars": 20, "stop_atr": 3.75, "take_profit_atr": 4.5}` | long XLF since 2026-11-18 00:00 @ 56.797033; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-18 00:00 @ 183.745109; long XLP since 2026-11-20 00:00 @ 90.957279; long USO since 2026-11-24 00:00 @ 135.160531; long DBC since 2026-11-17 00:00 @ 30.399116; long VIG since 2026-11-18 00:00 @ 245.57365; long SCHD since 2026-11-18 00:00 @ 35.090526; long VNQ since 2026-11-18 00:00 @ 94.208254; long VTV since 2026-11-18 00:00 @ 222.906848; long CSSMI.SW since 2026-11-20 00:00 @ 152.385698; long VWRL.SW since 2026-11-18 00:00 @ 149.184741 |
| balanced | [connors_composite_oversold__broad__balanced__v001.md](connors_composite_oversold__broad__balanced__v001.md) | 479 | `{"buy": 17, "exit": 75.0, "max_bars": 20, "stop_atr": 3.0, "take_profit_atr": 4.0}` | long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-18 00:00 @ 183.745109; long XLP since 2026-11-20 00:00 @ 90.957279; long SCHD since 2026-11-18 00:00 @ 35.090526; long VNQ since 2026-11-18 00:00 @ 94.208254; long CSSMI.SW since 2026-11-20 00:00 @ 152.385698 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 4,700.05 | 2,934.24 | 3,872.74 | 1,907.60 |
| return % | 47.00 | 29.34 | 38.73 | 19.08 |
| return %/year | 1.9 | 2.4 | 1.6 | 1.6 |
| gross profit | 13,063.28 | 13,203.16 | 10,101.89 | 9,748.76 |
| gross loss | 8,363.24 | 10,268.92 | 6,229.15 | 7,841.16 |
| trades | 4,373 | 4,506 | 3,812 | 3,959 |
| win rate % | 68.3 | 66.7 | 68.2 | 65.7 |
| avg win | 4.37 | 4.39 | 3.89 | 3.75 |
| avg loss | -6.04 | -6.84 | -5.14 | -5.77 |
| avg result / trade | 1.07 | 0.65 | 1.02 | 0.48 |
| largest single loss | -43.51 | -133.97 | -58.74 | -127.55 |
| largest loss % of equity | -17.31 | -24.23 | -10.50 | -12.50 |
| max drawdown | -606.35 | -756.48 | -399.18 | -595.20 |
| max drawdown % | -4.51 | -6.78 | -3.18 | -5.57 |
| profit factor | 1.56 | 1.29 | 1.62 | 1.24 |
| unusually bad trades | 444 | 385 | 353 | 213 |
| … threshold (% of equity) | 3.1 | 4.1 | 3.0 | 4.6 |
| time in market % | 10.2 | 20.2 | 6.7 | 13.4 |
| buy & hold return % | 100.07 | 303.60 | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.29 |  | 1.03 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.3 | 0.2 |
| 1996 | 0.2 | 0.1 |
| 1997 | 0.4 | 0.5 |
| 1998 | 0.4 | 0.4 |
| 1999 | 0.3 | 0.2 |
| 2000 | 0.8 | -0.0 |
| 2001 | -0.1 | -0.1 |
| 2002 | -0.6 | -0.1 |
| 2003 | 3.8 | 3.2 |
| 2004 | -0.1 | 0.5 |
| 2005 | -0.7 | -0.9 |
| 2006 | 2.9 | 2.2 |
| 2007 | 5.0 | 4.0 |
| 2008 | -2.2 | -1.4 |
| 2009 | 9.5 | 8.2 |
| 2010 | 2.0 | 1.5 |
| 2011 | 3.0 | 1.9 |
| 2012 | 3.5 | 4.5 |
| 2013 | 6.7 | 5.3 |
| 2014 | 1.5 | 1.0 |
| 2015 | 2.7 | 2.3 |
| 2016 (OOS) | 4.7 | 3.1 |
| 2017 (OOS) | 6.6 | 4.7 |
| 2018 (OOS) | -0.5 | -1.6 |
| 2019 (OOS) | 0.2 | -0.0 |
| 2020 (OOS) | 1.6 | 0.6 |
| 2021 (OOS) | 10.6 | 9.3 |
| 2022 (OOS) | -6.6 | -1.9 |
| 2023 (OOS) | 3.3 | 1.6 |
| 2024 (OOS) | 7.7 | 11.3 |
| 2025 (OOS) | 8.9 | 5.9 |
| 2026 (OOS) | 0.1 | -2.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.5% from a peak in-sample and 6.8% out-of-sample, and the worst single trade cost 24.2% of the account out-of-sample. About 68 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.2% from a peak in-sample and 5.6% out-of-sample, and the worst single trade cost 12.5% of the account out-of-sample. About 68 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 658 | `{"buy": 19, "exit": 77.5, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,854.02 | 1.9 | -4.3 | 68.5 | 2,903.20 | 2.4 | -7.3 | 1.25 | 4332/4466 | not checked |
| 819 | `{"buy": 19, "exit": 77.5, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 4,852.74 | 1.9 | -4.2 | 68.5 | 2,888.32 | 2.4 | -7.3 | 1.24 | 4330/4464 | not checked |
| 627 | `{"buy": 18, "exit": 77.5, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,703.98 | 1.9 | -4.0 | 68.8 | 2,692.03 | 2.2 | -6.2 | 1.20 | 3987/4077 | not checked |
| 621 | `{"buy": 18, "exit": 77.5, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,674.83 | 1.8 | -4.0 | 68.7 | 2,655.58 | 2.2 | -6.3 | 1.19 | 3994/4093 | not checked |
| 640 | `{"buy": 18, "exit": 77.5, "max_bars": 24, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 4,663.92 | 1.8 | -3.9 | 68.8 | 2,754.67 | 2.3 | -6.0 | 1.23 | 4016/4091 | not checked |
| 812 | `{"buy": 18, "exit": 77.5, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 4,662.73 | 1.8 | -3.7 | 68.7 | 2,583.16 | 2.1 | -6.5 | 1.16 | 4038/4126 | not checked |
| 751 | `{"buy": 18, "exit": 77.5, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 4,656.46 | 1.8 | -3.7 | 68.6 | 2,579.07 | 2.1 | -6.5 | 1.16 | 4036/4125 | not checked |
| 909 | `{"buy": 18, "exit": 77.5, "max_bars": 16, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 4,651.06 | 1.8 | -3.6 | 68.3 | 2,564.70 | 2.1 | -6.7 | 1.15 | 4063/4174 | not checked |
| 701 | `{"buy": 17, "exit": 77.5, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 4,471.84 | 1.8 | -3.5 | 68.8 | 2,767.40 | 2.3 | -6.3 | 1.27 | 3627/3758 | not checked |
| 754 | `{"buy": 17, "exit": 77.5, "max_bars": 20, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 4,427.01 | 1.8 | -3.5 | 68.7 | 2,780.99 | 2.3 | -6.3 | 1.29 | 3629/3771 | not checked |
| 908 | `{"buy": 17, "exit": 77.5, "max_bars": 24, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 4,315.46 | 1.7 | -3.3 | 68.7 | 3,122.00 | 2.5 | -5.8 | 1.47 | 3649/3785 | not checked |
| 594 | `{"buy": 17, "exit": 77.5, "max_bars": 20, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 4,265.01 | 1.7 | -3.3 | 68.6 | 3,145.37 | 2.5 | -5.7 | 1.49 | 3652/3798 | not checked |
| 625 | `{"buy": 17, "exit": 77.5, "max_bars": 16, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 4,226.68 | 1.7 | -3.3 | 68.1 | 2,999.42 | 2.4 | -5.9 | 1.44 | 3665/3822 | not checked |
| 497 | `{"buy": 17, "exit": 77.5, "max_bars": 18, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 4,165.89 | 1.7 | -3.3 | 68.4 | 2,757.46 | 2.3 | -5.6 | 1.35 | 3686/3845 | not checked |
| 563 | `{"buy": 17, "exit": 77.5, "max_bars": 16, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 4,138.18 | 1.7 | -3.3 | 68.0 | 2,727.59 | 2.2 | -5.7 | 1.35 | 3693/3860 | not checked |
| 637 | `{"buy": 18, "exit": 75.0, "max_bars": 22, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 4,067.84 | 1.6 | -3.2 | 68.2 | 1,495.75 | 1.3 | -6.4 | 0.79 | 4275/4367 | not checked |
| 484 | `{"buy": 18, "exit": 75.0, "max_bars": 16, "stop_atr": 3.0, "take_profit_atr": 3.5}` | 4,040.63 | 1.6 | -3.2 | 67.9 | 1,534.01 | 1.3 | -6.0 | 0.81 | 4284/4395 | not checked |
| 647 | `{"buy": 18, "exit": 75.0, "max_bars": 22, "stop_atr": 2.75, "take_profit_atr": 4.0}` | 3,930.10 | 1.6 | -3.0 | 67.8 | 1,502.85 | 1.3 | -5.4 | 0.81 | 4322/4434 | not checked |
| 236 | `{"buy": 17, "exit": 75.0, "max_bars": 20, "stop_atr": 2.75, "take_profit_atr": 4.0}` | 3,764.84 | 1.5 | -3.0 | 67.9 | 1,941.65 | 1.6 | -5.3 | 1.07 | 3854/4017 | not checked |
| 577 | `{"buy": 17, "exit": 75.0, "max_bars": 18, "stop_atr": 2.5, "take_profit_atr": 4.0}` | 3,574.11 | 1.5 | -2.9 | 67.2 | 1,852.28 | 1.6 | -5.3 | 1.07 | 3905/4072 | not checked |
| 171 | `{"buy": 14, "exit": 77.5, "max_bars": 20, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 2,836.35 | 1.2 | -2.9 | 68.9 | 2,750.95 | 2.3 | -5.8 | 1.88 | 2482/2634 | not checked |
| 158 | `{"buy": 15, "exit": 77.5, "max_bars": 20, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 2,778.75 | 1.2 | -2.8 | 67.2 | 1,957.08 | 1.7 | -6.1 | 1.42 | 2937/3087 | not checked |
| 465 | `{"buy": 15, "exit": 77.5, "max_bars": 20, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 2,175.62 | 0.9 | -2.7 | 63.1 | 2,315.05 | 1.9 | -5.5 | 2.05 | 2997/3164 | not checked |
| 416 | `{"buy": 11, "exit": 80.0, "max_bars": 12, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 1,390.00 | 0.6 | -2.4 | 65.8 | 1,504.80 | 1.3 | -6.2 | 2.10 | 1388/1543 | not checked |
| 115 | `{"buy": 11, "exit": 80.0, "max_bars": 14, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 1,353.59 | 0.6 | -2.2 | 61.7 | 1,347.73 | 1.2 | -4.5 | 1.92 | 1407/1572 | not checked |

(13 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 996 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
