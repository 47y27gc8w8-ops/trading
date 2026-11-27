# percent_b_money_flow__broad: optimization summary

Updated 2026-11-25T09:40:43Z · backtest.py version `0257c71e87` · 1,054 parameter sets tested with this version (1,054 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [percent_b_money_flow__broad__max-income__v002.md](percent_b_money_flow__broad__max-income__v002.md) | 1053 | `{"b": 0.65, "max_candles": 90, "mfi": 80, "stop_atr": 3.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [percent_b_money_flow__broad__balanced__v002.md](percent_b_money_flow__broad__balanced__v002.md) | 1054 | `{"b": 0.75, "max_candles": 90, "mfi": 90, "stop_atr": 4.25, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,084.01 | 1,810.57 | 580.30 | 135.10 |
| return % | 10.84 | 18.11 | 5.80 | 1.35 |
| return %/year | 0.5 | 1.5 | 0.3 | 0.1 |
| gross profit | 6,818.00 | 8,222.41 | 2,692.66 | 2,314.65 |
| gross loss | 5,733.99 | 6,411.84 | 2,112.36 | 2,179.55 |
| trades | 2,388 | 2,072 | 933 | 786 |
| win rate % | 41.4 | 44.0 | 45.4 | 45.7 |
| avg win | 6.90 | 9.02 | 6.35 | 6.45 |
| avg loss | -4.10 | -5.53 | -4.15 | -5.10 |
| avg result / trade | 0.45 | 0.87 | 0.62 | 0.17 |
| largest single loss | -33.25 | -101.82 | -30.71 | -37.34 |
| largest loss % of equity | -7.04 | -21.42 | -10.99 | -18.82 |
| max drawdown | -848.45 | -704.93 | -356.18 | -532.28 |
| max drawdown % | -8.39 | -5.99 | -3.55 | -5.11 |
| profit factor | 1.19 | 1.28 | 1.27 | 1.06 |
| unusually bad trades | 292 | 263 | 105 | 90 |
| … threshold (% of equity) | 3.1 | 3.1 | 3.1 | 3.6 |
| time in market % | 11.3 | 20.0 | 4.8 | 7.8 |
| buy & hold return % | 116.56 | 305.41 | 116.56 | 305.41 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 3.14 |  | 0.44 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.1 |
| 1996 | 0.2 | 0.1 |
| 1997 | 0.3 | 0.0 |
| 1998 | 0.4 | 0.1 |
| 1999 | -1.2 | -0.1 |
| 2000 | -1.9 | -0.9 |
| 2001 | -1.3 | -0.7 |
| 2002 | -2.2 | -0.8 |
| 2003 | -0.4 | 0.1 |
| 2004 | 0.7 | -0.0 |
| 2005 | 1.0 | 0.8 |
| 2006 | -1.3 | -0.0 |
| 2007 | 1.0 | 1.3 |
| 2008 | -0.6 | 0.1 |
| 2009 | 4.7 | 0.7 |
| 2010 | 3.7 | 2.5 |
| 2011 | -0.3 | 0.2 |
| 2012 | 4.5 | 1.1 |
| 2013 | 2.5 | 0.6 |
| 2014 | 2.4 | 2.0 |
| 2015 | -1.6 | -1.2 |
| 2016 (OOS) | 2.0 | 0.1 |
| 2017 (OOS) | 2.8 | 1.4 |
| 2018 (OOS) | -0.9 | -0.9 |
| 2019 (OOS) | 7.5 | 2.7 |
| 2020 (OOS) | 4.0 | -0.9 |
| 2021 (OOS) | -0.9 | -0.3 |
| 2022 (OOS) | -1.9 | -1.8 |
| 2023 (OOS) | 3.1 | 1.0 |
| 2024 (OOS) | -3.7 | -2.4 |
| 2025 (OOS) | 3.2 | 0.5 |
| 2026 (OOS) | 3.1 | 1.8 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 8.4% from a peak in-sample and 6.0% out-of-sample, and the worst single trade cost 21.4% of the account out-of-sample. About 41 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.5% from a peak in-sample and 5.1% out-of-sample, and the worst single trade cost 18.8% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 613 | `{"b": 0.6, "max_candles": 84, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 620 | `{"b": 0.6, "max_candles": 72, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 621 | `{"b": 0.6, "max_candles": 90, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 682 | `{"b": 0.6, "max_candles": 96, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 754 | `{"b": 0.6, "max_candles": 78, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 799 | `{"b": 0.6, "max_candles": 66, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 814 | `{"b": 0.6, "max_candles": 60, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 833 | `{"b": 0.6, "max_candles": 102, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 843 | `{"b": 0.6, "max_candles": 54, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,783.46 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 985 | `{"b": 0.6, "max_candles": 108, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 1,093.20 | 0.5 | -8.2 | 41.2 | 1,786.53 | 1.5 | -6.0 | 3.04 | 2415/2096 | not checked |
| 701 | `{"b": 0.6, "max_candles": 72, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 765 | `{"b": 0.6, "max_candles": 78, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 815 | `{"b": 0.6, "max_candles": 84, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 819 | `{"b": 0.6, "max_candles": 90, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 842 | `{"b": 0.6, "max_candles": 66, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 870 | `{"b": 0.6, "max_candles": 96, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 950 | `{"b": 0.6, "max_candles": 102, "mfi": 78, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 990.67 | 0.5 | -8.2 | 40.5 | 1,817.87 | 1.6 | -6.0 | 3.44 | 2717/2428 | not checked |
| 811 | `{"b": 0.6, "max_candles": 78, "mfi": 78, "stop_atr": 4.25, "take_profit_atr": 4.5}` | 986.96 | 0.5 | -8.2 | 40.5 | 1,838.28 | 1.6 | -5.9 | 3.47 | 2717/2425 | not checked |
| 812 | `{"b": 0.6, "max_candles": 66, "mfi": 78, "stop_atr": 4.25, "take_profit_atr": 4.5}` | 986.96 | 0.5 | -8.2 | 40.5 | 1,838.28 | 1.6 | -5.9 | 3.47 | 2717/2425 | not checked |
| 610 | `{"b": 0.6, "max_candles": 90, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 980.23 | 0.5 | -8.0 | 41.1 | 1,709.65 | 1.5 | -6.4 | 3.24 | 2453/2126 | not checked |
| 700 | `{"b": 0.6, "max_candles": 72, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 980.23 | 0.5 | -8.0 | 41.1 | 1,709.65 | 1.5 | -6.4 | 3.24 | 2453/2126 | not checked |
| 732 | `{"b": 0.6, "max_candles": 96, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 980.23 | 0.5 | -8.0 | 41.1 | 1,709.65 | 1.5 | -6.4 | 3.24 | 2453/2126 | not checked |
| 760 | `{"b": 0.6, "max_candles": 78, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 980.23 | 0.5 | -8.0 | 41.1 | 1,709.65 | 1.5 | -6.4 | 3.24 | 2453/2126 | not checked |
| 805 | `{"b": 0.6, "max_candles": 60, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 980.23 | 0.5 | -8.0 | 41.1 | 1,709.65 | 1.5 | -6.4 | 3.24 | 2453/2126 | not checked |
| 835 | `{"b": 0.6, "max_candles": 66, "mfi": 80, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 980.23 | 0.5 | -8.0 | 41.1 | 1,709.65 | 1.5 | -6.4 | 3.24 | 2453/2126 | not checked |

(24 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,054 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
