# regression_slope_quality__broad: optimization summary

Updated 2026-11-25T11:57:04Z · backtest.py version `67a06b638d` · 1,255 parameter sets tested with this version (1,255 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [regression_slope_quality__broad__max-income__v002.md](regression_slope_quality__broad__max-income__v002.md) | 1254 | `{"max_candles": 156, "n": 110, "r2": 0.44, "stop_atr": 4.25, "take_profit_atr": 10.5}` | long XLE since 2026-09-18 00:00 @ 63.839792; long XLV since 2026-08-06 00:00 @ 165.55624; long VIG since 2026-07-08 00:00 @ 237.239119; long USMV since 2026-08-06 00:00 @ 99.483216 |
| balanced | [regression_slope_quality__broad__balanced__v002.md](regression_slope_quality__broad__balanced__v002.md) | 1255 | `{"max_candles": 144, "n": 115, "r2": 0.34, "stop_atr": 3.25, "take_profit_atr": 6.0}` | long XLP since 2026-11-24 00:00 @ 90.797228; long USMV since 2026-08-05 00:00 @ 99.901965 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,968.41 | 2,849.38 | 2,339.14 | 1,596.40 |
| return % | 39.68 | 28.49 | 23.39 | 15.96 |
| return %/year | 1.6 | 2.3 | 1.0 | 1.4 |
| gross profit | 7,061.71 | 6,346.00 | 4,789.49 | 4,101.66 |
| gross loss | 3,093.30 | 3,496.62 | 2,450.35 | 2,505.25 |
| trades | 545 | 556 | 539 | 539 |
| win rate % | 50.3 | 46.0 | 51.0 | 48.0 |
| avg win | 25.77 | 24.79 | 17.42 | 15.84 |
| avg loss | -11.41 | -11.66 | -9.28 | -8.95 |
| avg result / trade | 7.28 | 5.12 | 4.34 | 2.96 |
| largest single loss | -39.45 | -210.42 | -40.41 | -62.52 |
| largest loss % of equity | -11.57 | -24.53 | -11.16 | -16.37 |
| max drawdown | -1,131.70 | -748.94 | -574.20 | -413.96 |
| max drawdown % | -7.96 | -6.89 | -4.53 | -3.76 |
| profit factor | 2.28 | 1.81 | 1.96 | 1.64 |
| unusually bad trades | 34 | 26 | 21 | 20 |
| … threshold (% of equity) | 8.2 | 8.2 | 7.3 | 7.2 |
| time in market % | 15.1 | 24.0 | 8.8 | 13.6 |
| buy & hold return % | 114.15 | 305.61 | 114.15 | 305.61 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.46 |  | 1.36 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.1 |
| 1996 | 0.1 | 0.1 |
| 1997 | 0.3 | 0.2 |
| 1998 | 0.3 | 0.2 |
| 1999 | 0.9 | 0.3 |
| 2000 | 0.1 | 0.6 |
| 2001 | -0.3 | -0.3 |
| 2002 | -0.6 | 0.2 |
| 2003 | 5.2 | 2.3 |
| 2004 | 2.1 | 1.1 |
| 2005 | -2.7 | -2.2 |
| 2006 | 2.4 | 1.5 |
| 2007 | 1.4 | 1.6 |
| 2008 | -1.8 | -1.7 |
| 2009 | 15.6 | 10.5 |
| 2010 | 4.2 | 4.8 |
| 2011 | 4.5 | 1.2 |
| 2012 | -1.9 | 0.1 |
| 2013 | 7.5 | 2.0 |
| 2014 | -0.2 | 0.9 |
| 2015 | -2.2 | -1.6 |
| 2016 (OOS) | -0.2 | 0.9 |
| 2017 (OOS) | 4.3 | 1.9 |
| 2018 (OOS) | -2.1 | -0.5 |
| 2019 (OOS) | 0.5 | 1.4 |
| 2020 (OOS) | 10.1 | 5.1 |
| 2021 (OOS) | 3.6 | -0.0 |
| 2022 (OOS) | -1.9 | -0.4 |
| 2023 (OOS) | 0.1 | -1.1 |
| 2024 (OOS) | 6.6 | 4.1 |
| 2025 (OOS) | 8.8 | 3.7 |
| 2026 (OOS) | -2.9 | -0.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 8.0% from a peak in-sample and 6.9% out-of-sample, and the worst single trade cost 24.5% of the account out-of-sample. About 50 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.5% from a peak in-sample and 3.8% out-of-sample, and the worst single trade cost 16.4% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 753 | `{"max_candles": 156, "n": 110, "r2": 0.44, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 3,968.41 | 1.6 | -8.0 | 50.3 | 2,849.38 | 2.3 | -6.9 | 1.46 | 545/556 | 1.00 |
| 511 | `{"max_candles": 180, "n": 110, "r2": 0.44, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 3,828.13 | 1.6 | -7.8 | 49.0 | 2,647.89 | 2.2 | -6.9 | 1.40 | 545/557 | not checked |
| 598 | `{"max_candles": 156, "n": 110, "r2": 0.44, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 3,813.47 | 1.6 | -7.7 | 48.9 | 2,629.55 | 2.2 | -6.9 | 1.40 | 548/558 | not checked |
| 502 | `{"max_candles": 180, "n": 110, "r2": 0.44, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 3,612.59 | 1.5 | -7.5 | 48.2 | 2,669.03 | 2.2 | -6.9 | 1.49 | 548/559 | not checked |
| 484 | `{"max_candles": 192, "n": 110, "r2": 0.44, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 3,558.52 | 1.5 | -7.5 | 48.2 | 2,670.56 | 2.2 | -6.9 | 1.51 | 548/559 | 1.00 |
| 689 | `{"max_candles": 156, "n": 110, "r2": 0.44, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 3,555.52 | 1.5 | -7.4 | 48.1 | 2,654.13 | 2.2 | -6.9 | 1.50 | 551/560 | not checked |
| 497 | `{"max_candles": 192, "n": 110, "r2": 0.42, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 3,372.99 | 1.4 | -7.3 | 46.5 | 3,245.27 | 2.6 | -7.2 | 1.89 | 555/554 | not checked |
| 812 | `{"max_candles": 156, "n": 105, "r2": 0.44, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 3,354.29 | 1.4 | -7.3 | 48.3 | 2,550.70 | 2.1 | -7.2 | 1.52 | 569/572 | not checked |
| 697 | `{"max_candles": 180, "n": 115, "r2": 0.46, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 3,314.39 | 1.4 | -7.3 | 46.9 | 3,040.05 | 2.5 | -6.9 | 1.80 | 512/532 | not checked |
| 798 | `{"max_candles": 192, "n": 115, "r2": 0.46, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 3,297.62 | 1.4 | -7.2 | 47.0 | 3,034.83 | 2.5 | -6.9 | 1.80 | 511/532 | not checked |
| 679 | `{"max_candles": 156, "n": 115, "r2": 0.46, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 3,243.08 | 1.4 | -7.2 | 46.8 | 3,020.04 | 2.5 | -6.9 | 1.81 | 515/532 | not checked |
| 895 | `{"max_candles": 180, "n": 110, "r2": 0.42, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 3,225.30 | 1.3 | -7.1 | 44.6 | 2,923.94 | 2.4 | -7.0 | 1.78 | 558/560 | not checked |
| 640 | `{"max_candles": 192, "n": 110, "r2": 0.42, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 3,173.46 | 1.3 | -7.1 | 44.4 | 2,927.58 | 2.4 | -7.0 | 1.81 | 558/560 | not checked |
| 1136 | `{"max_candles": 156, "n": 110, "r2": 0.42, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 3,139.37 | 1.3 | -7.1 | 44.6 | 2,889.35 | 2.4 | -7.0 | 1.80 | 561/561 | not checked |
| 1252 | `{"max_candles": 192, "n": 115, "r2": 0.46, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 3,098.17 | 1.3 | -7.1 | 46.0 | 2,752.60 | 2.3 | -6.9 | 1.75 | 513/535 | not checked |
| 741 | `{"max_candles": 156, "n": 105, "r2": 0.44, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 3,054.36 | 1.3 | -7.0 | 47.1 | 2,523.50 | 2.1 | -7.0 | 1.63 | 571/579 | not checked |
| 1172 | `{"max_candles": 180, "n": 105, "r2": 0.46, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 3,032.97 | 1.3 | -7.0 | 46.3 | 2,355.25 | 2.0 | -7.1 | 1.54 | 570/574 | not checked |
| 1152 | `{"max_candles": 204, "n": 115, "r2": 0.46, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 3,006.11 | 1.3 | -7.0 | 44.5 | 2,828.87 | 2.3 | -6.9 | 1.83 | 519/536 | not checked |
| 581 | `{"max_candles": 204, "n": 110, "r2": 0.44, "stop_atr": 3.25, "take_profit_atr": 10.5}` | 3,001.64 | 1.3 | -6.9 | 44.3 | 2,871.68 | 2.4 | -7.0 | 1.86 | 553/564 | not checked |
| 984 | `{"max_candles": 180, "n": 115, "r2": 0.42, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 2,990.48 | 1.2 | -6.9 | 42.9 | 2,779.45 | 2.3 | -7.2 | 1.82 | 527/534 | not checked |
| 461 | `{"max_candles": 192, "n": 115, "r2": 0.42, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 2,966.83 | 1.2 | -6.9 | 42.7 | 2,775.08 | 2.3 | -7.2 | 1.82 | 527/534 | not checked |
| 482 | `{"max_candles": 192, "n": 115, "r2": 0.42, "stop_atr": 3.25, "take_profit_atr": 10.5}` | 2,934.87 | 1.2 | -6.5 | 41.0 | 2,599.46 | 2.1 | -7.2 | 1.75 | 531/535 | not checked |
| 566 | `{"max_candles": 204, "n": 110, "r2": 0.44, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 2,821.08 | 1.2 | -6.5 | 53.4 | 1,695.01 | 1.4 | -5.9 | 1.22 | 554/564 | not checked |
| 597 | `{"max_candles": 228, "n": 110, "r2": 0.44, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 2,821.08 | 1.2 | -6.5 | 53.4 | 1,695.01 | 1.4 | -5.9 | 1.22 | 554/564 | not checked |
| 647 | `{"max_candles": 156, "n": 110, "r2": 0.44, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 2,821.08 | 1.2 | -6.5 | 53.4 | 1,695.01 | 1.4 | -5.9 | 1.22 | 554/564 | not checked |

(19 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,255 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
