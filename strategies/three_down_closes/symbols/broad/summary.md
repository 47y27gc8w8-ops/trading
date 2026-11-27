# three_down_closes__broad: optimization summary

Updated 2026-11-25T07:31:05Z · backtest.py version `aece766218` · 804 parameter sets tested with this version (804 rows in results.csv in total) · last run ended: converged: no profile improved in the last 560 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [three_down_closes__broad__max-income__v001.md](three_down_closes__broad__max-income__v001.md) | 243 | `{"max_candles": 10, "n": 3, "stop_atr": 4.25, "take_profit_atr": 5.0}` | long RSP since 2026-11-19 00:00 @ 215.974777; long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-19 00:00 @ 180.454114; long XLB since 2026-11-17 00:00 @ 51.335396; long DBC since 2026-11-18 00:00 @ 29.858955; long VIG since 2026-11-19 00:00 @ 244.893453; long SCHD since 2026-11-19 00:00 @ 34.690404; long USMV since 2026-11-19 00:00 @ 101.370398; long VNQ since 2026-11-13 00:00 @ 96.849046; long VTV since 2026-11-19 00:00 @ 221.756509 |
| balanced | [three_down_closes__broad__balanced__v001.md](three_down_closes__broad__balanced__v001.md) | 244 | `{"max_candles": 12, "n": 3, "stop_atr": 3.0, "take_profit_atr": 3.5}` | long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-19 00:00 @ 180.454114; long DBC since 2026-11-18 00:00 @ 29.858955; long SCHD since 2026-11-19 00:00 @ 34.690404 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,790.38 | 312.56 | 1,675.58 | 579.76 |
| return % | 17.90 | 3.13 | 16.76 | 5.80 |
| return %/year | 1.0 | 0.3 | 1.0 | 0.5 |
| gross profit | 6,253.30 | 6,108.91 | 6,283.82 | 6,497.70 |
| gross loss | 4,462.92 | 5,796.35 | 4,608.24 | 5,917.94 |
| trades | 4,060 | 4,518 | 4,106 | 4,592 |
| win rate % | 62.0 | 60.9 | 61.9 | 60.7 |
| avg win | 2.48 | 2.22 | 2.47 | 2.33 |
| avg loss | -2.89 | -3.28 | -2.95 | -3.28 |
| avg result / trade | 0.44 | 0.07 | 0.41 | 0.13 |
| largest single loss | -35.30 | -74.08 | -33.37 | -51.42 |
| largest loss % of equity | -14.01 | -25.62 | -9.27 | -17.78 |
| max drawdown | -477.70 | -905.17 | -381.65 | -808.37 |
| max drawdown % | -4.19 | -8.74 | -3.18 | -7.76 |
| profit factor | 1.40 | 1.05 | 1.36 | 1.10 |
| unusually bad trades | 315 | 475 | 379 | 559 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 6.1 | 9.4 | 5.8 | 9.0 |
| buy & hold return % | 95.12 | 303.60 | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |  | 0.54 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 0.7 | 0.3 |
| 2001 | 0.4 | 0.2 |
| 2002 | -0.7 | -0.7 |
| 2003 | 1.4 | 1.4 |
| 2004 | 1.1 | 1.0 |
| 2005 | 0.3 | -0.2 |
| 2006 | 1.3 | 1.3 |
| 2007 | 1.4 | 1.6 |
| 2008 | -0.1 | -0.0 |
| 2009 | 2.1 | 1.9 |
| 2010 | 2.4 | 2.2 |
| 2011 | 0.0 | 0.7 |
| 2012 | 1.2 | 1.7 |
| 2013 | 2.6 | 2.5 |
| 2014 | 2.2 | 2.3 |
| 2015 | 0.4 | -0.4 |
| 2016 (OOS) | 0.1 | -0.1 |
| 2017 (OOS) | 2.1 | 2.1 |
| 2018 (OOS) | -1.9 | -0.4 |
| 2019 (OOS) | -0.8 | -0.4 |
| 2020 (OOS) | -1.4 | -0.8 |
| 2021 (OOS) | 2.6 | 3.0 |
| 2022 (OOS) | 0.4 | 0.7 |
| 2023 (OOS) | -0.8 | -0.6 |
| 2024 (OOS) | 4.7 | 5.3 |
| 2025 (OOS) | 2.4 | 2.2 |
| 2026 (OOS) | -1.7 | -1.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.2% from a peak in-sample and 8.7% out-of-sample, and the worst single trade cost 25.6% of the account out-of-sample. About 62 of every 100 trades won in-sample. Out-of-sample it earned 0.3% a year against 1.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.2% from a peak in-sample and 7.8% out-of-sample, and the worst single trade cost 17.8% of the account out-of-sample. About 62 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 1.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 397 | `{"max_candles": 14, "n": 3, "stop_atr": 4.25, "take_profit_atr": 4.5}` | 1,826.28 | 1.1 | -4.2 | 62.1 | 382.19 | 0.3 | -8.7 | 0.33 | 4052/4509 | not checked |
| 747 | `{"max_candles": 14, "n": 3, "stop_atr": 4.25, "take_profit_atr": 3.5}` | 1,814.81 | 1.1 | -4.2 | 62.1 | 468.30 | 0.4 | -8.7 | 0.40 | 4052/4510 | not checked |
| 286 | `{"max_candles": 14, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 1,800.33 | 1.0 | -4.0 | 62.1 | 377.26 | 0.3 | -8.5 | 0.33 | 4058/4525 | not checked |
| 416 | `{"max_candles": 14, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 1,795.64 | 1.0 | -3.9 | 62.1 | 430.54 | 0.4 | -8.5 | 0.38 | 4058/4526 | not checked |
| 379 | `{"max_candles": 14, "n": 3, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 1,721.96 | 1.0 | -3.7 | 62.0 | 378.41 | 0.3 | -8.1 | 0.34 | 4070/4536 | not checked |
| 657 | `{"max_candles": 8, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 1,691.56 | 1.0 | -3.7 | 61.7 | 324.17 | 0.3 | -8.4 | 0.30 | 4085/4553 | not checked |
| 559 | `{"max_candles": 12, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 1,687.73 | 1.0 | -3.2 | 61.9 | 491.14 | 0.4 | -7.7 | 0.45 | 4106/4591 | not checked |
| 413 | `{"max_candles": 18, "n": 3, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 1,684.31 | 1.0 | -3.1 | 62.0 | 465.48 | 0.4 | -8.0 | 0.43 | 4088/4569 | not checked |
| 483 | `{"max_candles": 12, "n": 3, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 1,679.47 | 1.0 | -3.1 | 61.9 | 422.76 | 0.4 | -8.1 | 0.39 | 4091/4570 | not checked |
| 482 | `{"max_candles": 12, "n": 3, "stop_atr": 3.25, "take_profit_atr": 3.0}` | 1,658.30 | 1.0 | -3.1 | 61.9 | 514.11 | 0.5 | -8.2 | 0.48 | 4091/4571 | not checked |
| 781 | `{"max_candles": 12, "n": 3, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 1,466.15 | 0.9 | -3.1 | 61.6 | 334.75 | 0.3 | -7.1 | 0.35 | 4149/4649 | not checked |
| 111 | `{"max_candles": 14, "n": 3, "stop_atr": 1.75, "take_profit_atr": 5.5}` | 797.64 | 0.5 | -2.9 | 59.5 | 129.88 | 0.1 | -5.8 | 0.25 | 4277/4781 | not checked |
| 139 | `{"max_candles": 18, "n": 3, "stop_atr": 1.5, "take_profit_atr": 2.5}` | 775.58 | 0.5 | -2.6 | 58.1 | 243.05 | 0.2 | -6.2 | 0.47 | 4354/4841 | not checked |
| 216 | `{"max_candles": 18, "n": 5, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 262.57 | 0.2 | -2.5 | 65.0 | 48.84 | 0.0 | -2.0 | 0.25 | 608/738 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 804 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
