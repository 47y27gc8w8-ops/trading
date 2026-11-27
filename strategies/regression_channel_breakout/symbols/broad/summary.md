# regression_channel_breakout__broad: optimization summary

Updated 2026-11-25T11:48:53Z · backtest.py version `0096efbb35` · 914 parameter sets tested with this version (914 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [regression_channel_breakout__broad__max-income__v001.md](regression_channel_breakout__broad__max-income__v001.md) | 413 | `{"k": 1.3, "max_candles": 36, "n": 70, "stop_atr": 3.75, "take_profit_atr": 3.0}` | long SHY since 2026-11-23 00:00 @ 81.514445 |
| balanced | [regression_channel_breakout__broad__balanced__v001.md](regression_channel_breakout__broad__balanced__v001.md) | 414 | `{"k": 1.4, "max_candles": 36, "n": 70, "stop_atr": 3.75, "take_profit_atr": 2.5}` | long SHY since 2026-11-23 00:00 @ 81.514445 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 714.87 | 215.67 | 585.46 | 415.65 |
| return % | 7.15 | 2.16 | 5.85 | 4.16 |
| return %/year | 0.3 | 0.2 | 0.3 | 0.4 |
| gross profit | 6,075.80 | 6,411.51 | 5,789.60 | 6,323.47 |
| gross loss | 5,360.92 | 6,195.84 | 5,204.14 | 5,907.81 |
| trades | 2,043 | 2,203 | 2,006 | 2,158 |
| win rate % | 44.2 | 45.8 | 46.8 | 50.0 |
| avg win | 6.73 | 6.35 | 6.17 | 5.86 |
| avg loss | -4.70 | -5.19 | -4.87 | -5.48 |
| avg result / trade | 0.35 | 0.10 | 0.29 | 0.19 |
| largest single loss | -30.27 | -65.80 | -33.18 | -72.38 |
| largest loss % of equity | -7.29 | -18.95 | -7.29 | -18.95 |
| max drawdown | -615.32 | -948.07 | -586.35 | -761.01 |
| max drawdown % | -5.43 | -8.88 | -5.25 | -7.08 |
| profit factor | 1.13 | 1.03 | 1.11 | 1.07 |
| unusually bad trades | 232 | 217 | 189 | 186 |
| … threshold (% of equity) | 3.1 | 3.7 | 3.4 | 3.8 |
| time in market % | 9.1 | 18.3 | 8.0 | 16.2 |
| buy & hold return % | 114.15 | 305.61 | 114.15 | 305.61 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.61 |  | 1.37 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.0 | 0.1 |
| 1996 | 0.1 | 0.2 |
| 1997 | 0.1 | 0.1 |
| 1998 | 0.4 | 0.4 |
| 1999 | 1.1 | 0.9 |
| 2000 | -1.1 | -0.8 |
| 2001 | -1.2 | -1.4 |
| 2002 | -0.5 | -0.5 |
| 2003 | 1.2 | 1.2 |
| 2004 | 0.1 | 0.4 |
| 2005 | 0.3 | -0.1 |
| 2006 | 0.7 | 0.4 |
| 2007 | 0.7 | -0.1 |
| 2008 | 0.0 | 0.7 |
| 2009 | 1.4 | 1.4 |
| 2010 | 3.6 | 2.8 |
| 2011 | -1.4 | -1.5 |
| 2012 | 2.6 | 2.9 |
| 2013 | 3.1 | 2.0 |
| 2014 | -0.1 | 0.7 |
| 2015 | -3.9 | -4.0 |
| 2016 (OOS) | 0.3 | 0.4 |
| 2017 (OOS) | 3.4 | 4.2 |
| 2018 (OOS) | -1.0 | -1.4 |
| 2019 (OOS) | 0.9 | 1.2 |
| 2020 (OOS) | 0.7 | 2.9 |
| 2021 (OOS) | 0.6 | 1.1 |
| 2022 (OOS) | -4.4 | -3.7 |
| 2023 (OOS) | 4.1 | 2.9 |
| 2024 (OOS) | -3.0 | -2.6 |
| 2025 (OOS) | -1.7 | -2.4 |
| 2026 (OOS) | 5.3 | 4.5 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.4% from a peak in-sample and 8.9% out-of-sample, and the worst single trade cost 18.9% of the account out-of-sample. About 44 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 5.2% from a peak in-sample and 7.1% out-of-sample, and the worst single trade cost 18.9% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 418 | `{"k": 1.3, "max_candles": 36, "n": 70, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 735.61 | 0.3 | -5.6 | 42.3 | 378.86 | 0.3 | -8.3 | 1.00 | 1920/2077 | not checked |
| 196 | `{"k": 1.3, "max_candles": 36, "n": 70, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 718.78 | 0.3 | -5.4 | 44.2 | 260.05 | 0.2 | -8.7 | 0.73 | 2043/2202 | not checked |
| 547 | `{"k": 1.5, "max_candles": 30, "n": 70, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 635.37 | 0.3 | -4.7 | 40.8 | 607.74 | 0.5 | -7.8 | 1.86 | 1497/1606 | not checked |
| 820 | `{"k": 1.5, "max_candles": 30, "n": 70, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 631.56 | 0.3 | -4.6 | 40.6 | 688.99 | 0.6 | -7.3 | 2.10 | 1499/1607 | not checked |
| 848 | `{"k": 1.5, "max_candles": 30, "n": 70, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 619.65 | 0.3 | -4.6 | 40.6 | 656.72 | 0.6 | -7.4 | 2.03 | 1499/1606 | not checked |
| 572 | `{"k": 1.5, "max_candles": 36, "n": 70, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 591.70 | 0.3 | -4.6 | 41.9 | 465.77 | 0.4 | -7.2 | 1.56 | 1598/1731 | not checked |
| 436 | `{"k": 1.5, "max_candles": 36, "n": 70, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 586.23 | 0.3 | -4.6 | 41.9 | 495.37 | 0.5 | -7.4 | 1.67 | 1598/1730 | not checked |
| 94 | `{"k": 1.7, "max_candles": 42, "n": 60, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 584.44 | 0.3 | -3.3 | 41.9 | 451.94 | 0.4 | -4.5 | 1.52 | 1361/1503 | not checked |
| 83 | `{"k": 1.7, "max_candles": 42, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 553.28 | 0.3 | -3.2 | 41.7 | 418.85 | 0.4 | -4.6 | 1.46 | 1365/1509 | not checked |
| 66 | `{"k": 1.8, "max_candles": 48, "n": 60, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 532.74 | 0.2 | -2.6 | 42.4 | 215.32 | 0.2 | -5.1 | 0.80 | 1197/1344 | not checked |
| 482 | `{"k": 1.8, "max_candles": 36, "n": 60, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 532.74 | 0.2 | -2.6 | 42.4 | 214.55 | 0.2 | -5.1 | 0.80 | 1197/1344 | not checked |
| 533 | `{"k": 1.8, "max_candles": 42, "n": 60, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 532.74 | 0.2 | -2.6 | 42.4 | 219.45 | 0.2 | -5.0 | 0.80 | 1197/1344 | not checked |
| 804 | `{"k": 1.8, "max_candles": 48, "n": 60, "stop_atr": 2.75, "take_profit_atr": 4.0}` | 448.55 | 0.2 | -2.6 | 41.4 | 429.34 | 0.4 | -5.7 | 1.86 | 1158/1294 | not checked |
| 879 | `{"k": 1.8, "max_candles": 42, "n": 60, "stop_atr": 2.75, "take_profit_atr": 4.0}` | 448.55 | 0.2 | -2.6 | 41.4 | 436.57 | 0.4 | -5.6 | 1.86 | 1158/1294 | not checked |
| 39 | `{"k": 1.9, "max_candles": 48, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 378.60 | 0.2 | -2.5 | 42.4 | 205.40 | 0.2 | -4.7 | 1.06 | 1067/1195 | 1.00 |
| 56 | `{"k": 1.9, "max_candles": 42, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 378.60 | 0.2 | -2.5 | 42.4 | 210.00 | 0.2 | -4.7 | 1.06 | 1067/1195 | not checked |
| 57 | `{"k": 1.9, "max_candles": 54, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 378.60 | 0.2 | -2.5 | 42.4 | 202.19 | 0.2 | -4.8 | 1.00 | 1067/1195 | not checked |
| 434 | `{"k": 1.9, "max_candles": 36, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 378.60 | 0.2 | -2.5 | 42.4 | 205.48 | 0.2 | -4.8 | 1.06 | 1067/1195 | not checked |
| 28 | `{"k": 1.9, "max_candles": 48, "n": 60, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 337.54 | 0.2 | -2.5 | 41.7 | 159.62 | 0.1 | -4.9 | 0.94 | 1072/1207 | not checked |
| 30 | `{"k": 2.0, "max_candles": 48, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 287.79 | 0.1 | -2.3 | 41.4 | 229.04 | 0.2 | -4.2 | 1.50 | 932/1074 | 1.00 |
| 44 | `{"k": 2.0, "max_candles": 42, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 287.79 | 0.1 | -2.3 | 41.4 | 238.56 | 0.2 | -4.1 | 1.57 | 932/1074 | not checked |
| 45 | `{"k": 2.0, "max_candles": 54, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 287.79 | 0.1 | -2.3 | 41.4 | 228.00 | 0.2 | -4.2 | 1.50 | 932/1074 | not checked |
| 444 | `{"k": 2.0, "max_candles": 60, "n": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 287.79 | 0.1 | -2.3 | 41.4 | 228.00 | 0.2 | -4.2 | 1.50 | 932/1074 | not checked |
| 41 | `{"k": 2.0, "max_candles": 48, "n": 60, "stop_atr": 2.75, "take_profit_atr": 3.5}` | 264.95 | 0.1 | -2.3 | 41.7 | 313.59 | 0.3 | -4.2 | 2.33 | 929/1067 | not checked |
| 19 | `{"k": 2.0, "max_candles": 48, "n": 60, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 242.84 | 0.1 | -2.2 | 40.8 | 201.48 | 0.2 | -4.3 | 1.64 | 935/1087 | 1.00 |

(8 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 914 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
