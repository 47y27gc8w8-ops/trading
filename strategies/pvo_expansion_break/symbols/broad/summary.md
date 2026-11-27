# pvo_expansion_break__broad: optimization summary

Updated 2026-11-25T10:33:13Z · backtest.py version `2318ebb74a` · 1,269 parameter sets tested with this version (1,269 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [pvo_expansion_break__broad__max-income__v002.md](pvo_expansion_break__broad__max-income__v002.md) | 1269 | `{"level": 1, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [pvo_expansion_break__broad__balanced__v001.md](pvo_expansion_break__broad__balanced__v001.md) | 228 | `{"level": 23, "max_candles": 84, "stop_atr": 2.75, "take_profit_atr": 1.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 146.55 | 23.56 | 60.74 | 50.54 |
| return % | 1.47 | 0.24 | 0.61 | 0.51 |
| return %/year | 0.1 | 0.0 | 0.0 | 0.1 |
| gross profit | 2,414.26 | 2,196.78 | 391.65 | 229.93 |
| gross loss | 2,267.71 | 2,173.22 | 330.91 | 179.39 |
| trades | 932 | 916 | 150 | 76 |
| win rate % | 49.2 | 54.4 | 56.7 | 71.0 |
| avg win | 5.26 | 4.41 | 4.61 | 4.26 |
| avg loss | -4.79 | -5.20 | -5.09 | -8.15 |
| avg result / trade | 0.16 | 0.03 | 0.40 | 0.67 |
| largest single loss | -30.41 | -38.37 | -16.03 | -20.37 |
| largest loss % of equity | -9.05 | -22.05 | -7.69 | -10.83 |
| max drawdown | -219.55 | -240.32 | -54.84 | -58.13 |
| max drawdown % | -2.18 | -2.36 | -0.55 | -0.58 |
| profit factor | 1.06 | 1.01 | 1.18 | 1.28 |
| unusually bad trades | 67 | 79 | 9 | 3 |
| … threshold (% of equity) | 3.8 | 3.8 | 4.4 | 7.0 |
| time in market % | 3.2 | 5.8 | 0.4 | 0.3 |
| buy & hold return % | 110.92 | 305.61 | 110.92 | 305.61 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |  | 1.67 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | -0.0 | 0.0 |
| 1996 | -0.0 | 0.0 |
| 1997 | 0.1 | 0.0 |
| 1998 | 0.1 | 0.0 |
| 1999 | 0.3 | 0.0 |
| 2000 | -0.8 | -0.3 |
| 2001 | -0.8 | 0.0 |
| 2002 | -0.3 | 0.2 |
| 2003 | 0.7 | 0.2 |
| 2004 | 0.1 | -0.0 |
| 2005 | 0.3 | 0.1 |
| 2006 | 0.5 | 0.1 |
| 2007 | 0.4 | 0.1 |
| 2008 | -0.1 | -0.1 |
| 2009 | 1.1 | -0.1 |
| 2010 | 0.6 | 0.1 |
| 2011 | -0.3 | 0.3 |
| 2012 | 0.6 | -0.3 |
| 2013 | 0.5 | 0.2 |
| 2014 | -0.4 | 0.0 |
| 2015 | -1.0 | 0.2 |
| 2016 (OOS) | -0.7 | 0.3 |
| 2017 (OOS) | 1.2 | 0.1 |
| 2018 (OOS) | 0.1 | -0.5 |
| 2019 (OOS) | 0.9 | 0.0 |
| 2020 (OOS) | -1.1 | 0.2 |
| 2021 (OOS) | -0.7 | 0.1 |
| 2022 (OOS) | 0.1 | -0.0 |
| 2023 (OOS) | 0.0 | 0.2 |
| 2024 (OOS) | -0.0 | -0.0 |
| 2025 (OOS) | 0.1 | 0.0 |
| 2026 (OOS) | -0.2 | 0.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 2.2% from a peak in-sample and 2.4% out-of-sample, and the worst single trade cost 22.1% of the account out-of-sample. About 49 of every 100 trades won in-sample. Out-of-sample it earned 0.0% a year against 0.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.6% from a peak in-sample and 0.6% out-of-sample, and the worst single trade cost 10.8% of the account out-of-sample. About 57 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 748 | `{"level": 1, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 146.55 | 0.1 | -2.2 | 49.2 | 23.56 | 0.0 | -2.4 | 0.29 | 932/916 | 0.83 |
| 1213 | `{"level": 1, "max_candles": 24, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 141.52 | 0.1 | -2.1 | 49.2 | 28.99 | 0.0 | -2.2 | 0.43 | 932/916 | not checked |
| 266 | `{"level": 1, "max_candles": 96, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 77.92 | 0.0 | -2.1 | 48.2 | 5.82 | 0.0 | -2.4 | 0.25 | 933/916 | not checked |
| 67 | `{"level": 23, "max_candles": 84, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 60.74 | 0.0 | -0.6 | 56.7 | 50.54 | 0.1 | -0.6 | 1.67 | 150/76 | 1.00 |
| 80 | `{"level": 23, "max_candles": 78, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 60.74 | 0.0 | -0.6 | 56.7 | 50.54 | 0.1 | -0.6 | 1.67 | 150/76 | not checked |
| 81 | `{"level": 23, "max_candles": 90, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 60.74 | 0.0 | -0.6 | 56.7 | 50.54 | 0.1 | -0.6 | 1.67 | 150/76 | not checked |
| 648 | `{"level": 23, "max_candles": 72, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 60.74 | 0.0 | -0.6 | 56.7 | 50.54 | 0.1 | -0.6 | 1.67 | 150/76 | not checked |
| 1199 | `{"level": 23, "max_candles": 96, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 60.74 | 0.0 | -0.6 | 56.7 | 50.54 | 0.1 | -0.6 | 1.67 | 150/76 | not checked |
| 1229 | `{"level": 23, "max_candles": 66, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 60.74 | 0.0 | -0.6 | 56.7 | 50.54 | 0.1 | -0.6 | 1.67 | 150/76 | not checked |
| 78 | `{"level": 23, "max_candles": 84, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 58.53 | 0.0 | -0.5 | 56.7 | 70.65 | 0.1 | -0.6 | 2.00 | 150/76 | not checked |
| 270 | `{"level": 23, "max_candles": 96, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 58.53 | 0.0 | -0.5 | 56.7 | 70.65 | 0.1 | -0.6 | 2.00 | 150/76 | not checked |
| 477 | `{"level": 23, "max_candles": 78, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 58.53 | 0.0 | -0.5 | 56.7 | 70.65 | 0.1 | -0.6 | 2.00 | 150/76 | not checked |
| 543 | `{"level": 23, "max_candles": 90, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 58.53 | 0.0 | -0.5 | 56.7 | 70.65 | 0.1 | -0.6 | 2.00 | 150/76 | not checked |
| 57 | `{"level": 23, "max_candles": 84, "stop_atr": 2.5, "take_profit_atr": 1.5}` | 46.21 | 0.0 | -0.5 | 55.3 | 55.93 | 0.1 | -0.6 | 2.50 | 150/77 | not checked |
| 518 | `{"level": 23, "max_candles": 78, "stop_atr": 2.5, "take_profit_atr": 1.5}` | 46.21 | 0.0 | -0.5 | 55.3 | 55.93 | 0.1 | -0.6 | 2.50 | 150/77 | not checked |
| 544 | `{"level": 23, "max_candles": 90, "stop_atr": 2.5, "take_profit_atr": 1.5}` | 46.21 | 0.0 | -0.5 | 55.3 | 55.93 | 0.1 | -0.6 | 2.50 | 150/77 | not checked |
| 60 | `{"level": 24, "max_candles": 84, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 45.82 | 0.0 | -0.5 | 56.4 | 38.40 | 0.0 | -0.6 | 2.00 | 140/72 | 1.00 |
| 71 | `{"level": 24, "max_candles": 78, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 45.82 | 0.0 | -0.5 | 56.4 | 38.40 | 0.0 | -0.6 | 2.00 | 140/72 | not checked |
| 72 | `{"level": 24, "max_candles": 90, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 45.82 | 0.0 | -0.5 | 56.4 | 38.40 | 0.0 | -0.6 | 2.00 | 140/72 | not checked |
| 698 | `{"level": 24, "max_candles": 72, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 45.82 | 0.0 | -0.5 | 56.4 | 38.40 | 0.0 | -0.6 | 2.00 | 140/72 | not checked |
| 1219 | `{"level": 24, "max_candles": 96, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 45.82 | 0.0 | -0.5 | 56.4 | 38.40 | 0.0 | -0.6 | 2.00 | 140/72 | not checked |
| 69 | `{"level": 24, "max_candles": 84, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 42.36 | 0.0 | -0.5 | 56.4 | 59.32 | 0.1 | -0.6 | 2.50 | 140/72 | not checked |
| 327 | `{"level": 24, "max_candles": 90, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 42.36 | 0.0 | -0.5 | 56.4 | 59.32 | 0.1 | -0.6 | 2.50 | 140/72 | not checked |
| 240 | `{"level": 23, "max_candles": 66, "stop_atr": 2.75, "take_profit_atr": 1.0}` | 38.25 | 0.0 | -0.5 | 66.2 | 29.41 | 0.0 | -0.3 | 1.50 | 151/79 | not checked |
| 258 | `{"level": 23, "max_candles": 72, "stop_atr": 2.75, "take_profit_atr": 1.0}` | 38.25 | 0.0 | -0.5 | 66.2 | 29.41 | 0.0 | -0.3 | 1.50 | 151/79 | not checked |

(14 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,269 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
