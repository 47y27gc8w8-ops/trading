# close_location_washout__broad: optimization summary

Updated 2026-11-25T16:22:12Z · backtest.py version `d508f8c47c` · 798 parameter sets tested with this version (798 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [close_location_washout__broad__max-income__v001.md](close_location_washout__broad__max-income__v001.md) | 277 | `{"clv": 0.1, "max_bars": 16, "stop_atr": 4.0, "take_profit_atr": 3.5}` | long XLF since 2026-11-18 00:00 @ 56.797033; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-19 00:00 @ 180.454114; long XLP since 2026-11-18 00:00 @ 90.847246; long VIG since 2026-11-20 00:00 @ 240.732202 |
| balanced | [close_location_washout__broad__balanced__v001.md](close_location_washout__broad__balanced__v001.md) | 278 | `{"clv": 0.08, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 6.0}` | long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-19 00:00 @ 61.728512; long XLP since 2026-11-18 00:00 @ 90.847246 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 955.02 | 1,646.27 | 884.42 | 1,482.63 |
| return % | 9.55 | 16.46 | 8.84 | 14.83 |
| return %/year | 0.4 | 1.4 | 0.4 | 1.3 |
| gross profit | 5,102.91 | 6,083.22 | 4,440.94 | 5,063.59 |
| gross loss | 4,147.88 | 4,436.94 | 3,556.52 | 3,580.96 |
| trades | 3,326 | 2,897 | 2,926 | 2,525 |
| win rate % | 63.3 | 63.6 | 63.5 | 64.1 |
| avg win | 2.42 | 3.30 | 2.39 | 3.13 |
| avg loss | -3.40 | -4.21 | -3.33 | -3.95 |
| avg result / trade | 0.29 | 0.57 | 0.30 | 0.59 |
| largest single loss | -36.95 | -108.81 | -36.25 | -84.80 |
| largest loss % of equity | -17.22 | -9.77 | -17.22 | -9.77 |
| max drawdown | -504.38 | -568.55 | -361.83 | -465.90 |
| max drawdown % | -4.56 | -5.51 | -3.26 | -4.54 |
| profit factor | 1.23 | 1.37 | 1.25 | 1.41 |
| unusually bad trades | 319 | 324 | 272 | 270 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 2.9 | 4.7 | 2.5 | 4.0 |
| buy & hold return % | 100.07 | 303.60 | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 3.21 |  | 3.20 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.0 | 0.0 |
| 1996 | 0.0 | 0.0 |
| 1997 | 0.5 | 0.5 |
| 1998 | 0.2 | 0.2 |
| 1999 | -0.2 | -0.2 |
| 2000 | -1.2 | -1.1 |
| 2001 | -0.2 | -0.2 |
| 2002 | 0.3 | 0.3 |
| 2003 | 1.2 | 0.9 |
| 2004 | -0.2 | -0.3 |
| 2005 | -0.1 | 0.0 |
| 2006 | 1.3 | 1.6 |
| 2007 | 2.5 | 2.2 |
| 2008 | -1.6 | -1.3 |
| 2009 | 5.6 | 4.3 |
| 2010 | 0.5 | 0.3 |
| 2011 | -1.8 | -0.4 |
| 2012 | 0.4 | 0.2 |
| 2013 | 2.9 | 2.7 |
| 2014 | -0.6 | -0.8 |
| 2015 | -0.1 | -0.3 |
| 2016 (OOS) | 0.8 | 0.4 |
| 2017 (OOS) | 2.3 | 2.2 |
| 2018 (OOS) | -3.4 | -3.2 |
| 2019 (OOS) | 2.6 | 2.2 |
| 2020 (OOS) | 2.7 | 2.8 |
| 2021 (OOS) | 4.9 | 4.5 |
| 2022 (OOS) | -2.1 | -2.8 |
| 2023 (OOS) | 0.5 | 0.2 |
| 2024 (OOS) | 4.7 | 4.7 |
| 2025 (OOS) | 0.9 | 1.3 |
| 2026 (OOS) | 2.0 | 2.3 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.6% from a peak in-sample and 5.5% out-of-sample, and the worst single trade cost 9.8% of the account out-of-sample. About 63 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.3% from a peak in-sample and 4.5% out-of-sample, and the worst single trade cost 9.8% of the account out-of-sample. About 64 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 313 | `{"clv": 0.1, "max_bars": 16, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,621.29 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 361 | `{"clv": 0.1, "max_bars": 14, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,621.29 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 427 | `{"clv": 0.1, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,621.29 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 431 | `{"clv": 0.1, "max_bars": 12, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,615.58 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 513 | `{"clv": 0.1, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,621.29 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 633 | `{"clv": 0.1, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,621.29 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 668 | `{"clv": 0.1, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 972.51 | 0.4 | -4.6 | 63.4 | 1,621.29 | 1.4 | -5.6 | 3.16 | 3326/2897 | not checked |
| 227 | `{"clv": 0.1, "max_bars": 16, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 950.92 | 0.4 | -4.5 | 63.3 | 1,666.54 | 1.4 | -5.5 | 3.33 | 3326/2897 | not checked |
| 302 | `{"clv": 0.1, "max_bars": 14, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 950.92 | 0.4 | -4.5 | 63.3 | 1,666.54 | 1.4 | -5.5 | 3.33 | 3326/2897 | not checked |
| 403 | `{"clv": 0.1, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 950.92 | 0.4 | -4.5 | 63.3 | 1,666.54 | 1.4 | -5.5 | 3.33 | 3326/2897 | not checked |
| 447 | `{"clv": 0.1, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 950.92 | 0.4 | -4.5 | 63.3 | 1,666.54 | 1.4 | -5.5 | 3.33 | 3326/2897 | not checked |
| 456 | `{"clv": 0.1, "max_bars": 12, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 950.92 | 0.4 | -4.5 | 63.3 | 1,660.69 | 1.4 | -5.5 | 3.30 | 3326/2897 | not checked |
| 756 | `{"clv": 0.1, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 950.92 | 0.4 | -4.5 | 63.3 | 1,666.54 | 1.4 | -5.5 | 3.33 | 3326/2897 | not checked |
| 307 | `{"clv": 0.1, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 938.45 | 0.4 | -4.5 | 63.3 | 1,627.97 | 1.4 | -5.5 | 3.26 | 3327/2898 | not checked |
| 757 | `{"clv": 0.08, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 919.70 | 0.4 | -3.4 | 63.7 | 1,500.61 | 1.3 | -4.5 | 3.07 | 2925/2524 | not checked |
| 783 | `{"clv": 0.08, "max_bars": 12, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 919.70 | 0.4 | -3.4 | 63.7 | 1,494.54 | 1.3 | -4.5 | 3.07 | 2925/2524 | not checked |
| 100 | `{"clv": 0.08, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 884.42 | 0.4 | -3.3 | 63.5 | 1,482.63 | 1.3 | -4.5 | 3.20 | 2926/2525 | not checked |
| 103 | `{"clv": 0.08, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 884.42 | 0.4 | -3.3 | 63.5 | 1,482.63 | 1.3 | -4.5 | 3.20 | 2926/2525 | 1.00 |
| 284 | `{"clv": 0.08, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 884.42 | 0.4 | -3.3 | 63.5 | 1,482.63 | 1.3 | -4.5 | 3.20 | 2926/2525 | not checked |
| 380 | `{"clv": 0.08, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 884.42 | 0.4 | -3.3 | 63.5 | 1,482.63 | 1.3 | -4.5 | 3.20 | 2926/2525 | not checked |
| 780 | `{"clv": 0.08, "max_bars": 8, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 884.42 | 0.4 | -3.3 | 63.5 | 1,482.63 | 1.3 | -4.5 | 3.20 | 2926/2525 | not checked |
| 358 | `{"clv": 0.08, "max_bars": 6, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 823.76 | 0.4 | -3.2 | 63.4 | 1,469.68 | 1.3 | -4.5 | 3.34 | 2930/2526 | not checked |
| 321 | `{"clv": 0.07, "max_bars": 16, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 798.14 | 0.4 | -3.0 | 63.2 | 1,490.31 | 1.3 | -4.5 | 3.46 | 2704/2325 | not checked |
| 774 | `{"clv": 0.07, "max_bars": 12, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 798.14 | 0.4 | -3.0 | 63.2 | 1,484.83 | 1.3 | -4.5 | 3.46 | 2704/2325 | not checked |
| 108 | `{"clv": 0.07, "max_bars": 12, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 685.73 | 0.3 | -3.0 | 63.0 | 1,398.43 | 1.2 | -4.6 | 3.78 | 2706/2329 | not checked |

(11 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 798 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
