# vortex_positive_cross__broad: optimization summary

Updated 2026-11-25T23:21:52Z · backtest.py version `95f0c9b9b2` · 932 parameter sets tested with this version (932 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [vortex_positive_cross__broad__max-income__v002.md](vortex_positive_cross__broad__max-income__v002.md) | 932 | `{"max_candles": 132, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.5}` | long XLV since 2026-11-25 00:00 @ 184.315273 |
| balanced | [vortex_positive_cross__broad__balanced__v001.md](vortex_positive_cross__broad__balanced__v001.md) | 391 | `{"max_candles": 132, "n": 21, "stop_atr": 3.0, "take_profit_atr": 2.5}` | long XLV since 2026-11-25 00:00 @ 184.315273 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,194.20 | 2,764.44 | 1,093.06 | 981.82 |
| return % | 31.94 | 27.64 | 10.93 | 9.82 |
| return %/year | 1.8 | 2.3 | 0.7 | 0.9 |
| gross profit | 11,475.82 | 11,907.74 | 8,062.94 | 8,404.72 |
| gross loss | 8,281.62 | 9,143.30 | 6,969.89 | 7,422.91 |
| trades | 3,848 | 3,893 | 3,848 | 3,893 |
| win rate % | 40.7 | 40.5 | 45.2 | 45.3 |
| avg win | 7.33 | 7.56 | 4.63 | 4.77 |
| avg loss | -3.63 | -3.95 | -3.31 | -3.48 |
| avg result / trade | 0.83 | 0.71 | 0.28 | 0.25 |
| largest single loss | -55.09 | -71.41 | -35.18 | -116.89 |
| largest loss % of equity | -9.19 | -25.46 | -14.34 | -25.46 |
| max drawdown | -1,222.77 | -781.09 | -692.49 | -528.45 |
| max drawdown % | -8.51 | -6.00 | -5.97 | -4.72 |
| profit factor | 1.39 | 1.30 | 1.16 | 1.13 |
| unusually bad trades | 566 | 630 | 517 | 583 |
| … threshold (% of equity) | 2.3 | 2.1 | 2.3 | 2.2 |
| time in market % | 22.4 | 33.6 | 12.2 | 18.7 |
| buy & hold return % | 89.54 | 303.60 | 89.54 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.30 |  | 1.32 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | -2.2 | -1.3 |
| 2001 | -2.3 | -1.9 |
| 2002 | -0.7 | -0.6 |
| 2003 | 3.4 | 1.7 |
| 2004 | 0.4 | -0.1 |
| 2005 | 0.3 | 0.9 |
| 2006 | 1.7 | -0.1 |
| 2007 | 2.7 | 0.7 |
| 2008 | 0.2 | -0.0 |
| 2009 | 13.1 | 6.4 |
| 2010 | 5.4 | 2.6 |
| 2011 | -1.9 | -2.3 |
| 2012 | 4.6 | 1.9 |
| 2013 | 7.4 | 4.3 |
| 2014 | 3.7 | 3.2 |
| 2015 | -6.3 | -4.4 |
| 2016 (OOS) | -1.7 | -1.8 |
| 2017 (OOS) | 6.6 | 2.6 |
| 2018 (OOS) | 1.2 | 0.3 |
| 2019 (OOS) | 5.2 | 3.5 |
| 2020 (OOS) | 3.4 | 0.6 |
| 2021 (OOS) | 6.6 | 1.9 |
| 2022 (OOS) | -3.2 | -1.8 |
| 2023 (OOS) | 5.2 | 2.0 |
| 2024 (OOS) | 3.4 | 2.7 |
| 2025 (OOS) | -3.5 | -2.6 |
| 2026 (OOS) | 2.2 | 0.6 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 8.5% from a peak in-sample and 6.0% out-of-sample, and the worst single trade cost 25.5% of the account out-of-sample. About 41 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 6.0% from a peak in-sample and 4.7% out-of-sample, and the worst single trade cost 25.5% of the account out-of-sample. About 45 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 931 | `{"max_candles": 72, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.5}` | 3,201.21 | 1.8 | -8.5 | 40.7 | 2,750.86 | 2.3 | -6.1 | 1.29 | 3848/3893 | not checked |
| 468 | `{"max_candles": 120, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.80 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 477 | `{"max_candles": 144, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.80 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 488 | `{"max_candles": 132, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.80 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 528 | `{"max_candles": 156, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.80 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 539 | `{"max_candles": 168, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.80 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 867 | `{"max_candles": 180, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.80 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 880 | `{"max_candles": 84, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,636.35 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 926 | `{"max_candles": 96, "n": 21, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 3,149.48 | 1.7 | -8.4 | 40.4 | 2,638.04 | 2.2 | -5.9 | 1.25 | 3848/3893 | not checked |
| 517 | `{"max_candles": 108, "n": 21, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 3,065.17 | 1.7 | -8.3 | 40.3 | 2,807.10 | 2.3 | -6.4 | 1.36 | 3848/3893 | not checked |
| 519 | `{"max_candles": 120, "n": 21, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 3,065.17 | 1.7 | -8.3 | 40.3 | 2,805.59 | 2.3 | -6.4 | 1.36 | 3848/3893 | not checked |
| 568 | `{"max_candles": 156, "n": 21, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 3,065.17 | 1.7 | -8.3 | 40.3 | 2,805.59 | 2.3 | -6.4 | 1.36 | 3848/3893 | not checked |
| 611 | `{"max_candles": 144, "n": 21, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 3,065.17 | 1.7 | -8.3 | 40.3 | 2,805.59 | 2.3 | -6.4 | 1.36 | 3848/3893 | not checked |
| 636 | `{"max_candles": 132, "n": 21, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 3,065.17 | 1.7 | -8.3 | 40.3 | 2,805.59 | 2.3 | -6.4 | 1.36 | 3848/3893 | not checked |
| 879 | `{"max_candles": 84, "n": 21, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 3,065.17 | 1.7 | -8.3 | 40.3 | 2,805.15 | 2.3 | -6.4 | 1.36 | 3848/3893 | not checked |
| 420 | `{"max_candles": 120, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 421 | `{"max_candles": 144, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 422 | `{"max_candles": 132, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | 1.00 |
| 525 | `{"max_candles": 108, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 645 | `{"max_candles": 156, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 666 | `{"max_candles": 168, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 719 | `{"max_candles": 180, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 741 | `{"max_candles": 96, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,594.82 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 809 | `{"max_candles": 192, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,595.26 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |
| 826 | `{"max_candles": 84, "n": 21, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 3,003.06 | 1.7 | -8.2 | 40.7 | 2,593.12 | 2.1 | -5.7 | 1.29 | 3848/3893 | not checked |

(27 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 932 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
