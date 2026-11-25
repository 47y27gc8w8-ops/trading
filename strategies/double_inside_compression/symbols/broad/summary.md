# double_inside_compression__broad: optimization summary

Updated 2026-11-25T23:07:40Z · backtest.py version `4b76847a81` · 3,074 parameter sets tested with this version (3,074 rows in results.csv in total) · last run ended: no untested valid parameter sets left to try

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [double_inside_compression__broad__max-income__v001.md](double_inside_compression__broad__max-income__v001.md) | 2484 | `{"max_candles": 72, "stop_atr": 4.0, "take_profit_atr": 4.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 53.24 | 6.28 |
| return % | 0.53 | 0.06 |
| return %/year | 0.0 | 0.0 |
| gross profit | 300.49 | 180.82 |
| gross loss | 247.25 | 174.54 |
| trades | 146 | 133 |
| win rate % | 37.0 | 42.1 |
| avg win | 5.56 | 3.23 |
| avg loss | -2.69 | -2.27 |
| avg result / trade | 0.36 | 0.05 |
| largest single loss | -14.33 | -8.33 |
| largest loss % of equity | -9.31 | -5.67 |
| max drawdown | -52.50 | -61.16 |
| max drawdown % | -0.52 | -0.61 |
| profit factor | 1.22 | 1.04 |
| unusually bad trades | 21 | 16 |
| … threshold (% of equity) | 2.7 | 2.3 |
| time in market % | 0.3 | 0.5 |
| buy & hold return % | 131.76 | 280.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.33 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 1995 | 0.1 |
| 1996 | 0.1 |
| 1997 | -0.0 |
| 1998 | -0.0 |
| 1999 | 0.1 |
| 2000 | -0.1 |
| 2001 | -0.1 |
| 2002 | -0.0 |
| 2003 | 0.3 |
| 2004 | -0.1 |
| 2005 | -0.1 |
| 2006 | -0.1 |
| 2007 | -0.0 |
| 2008 | -0.1 |
| 2009 | 0.2 |
| 2010 | -0.1 |
| 2011 | 0.3 |
| 2012 | 0.5 |
| 2013 | -0.3 |
| 2014 | 0.1 |
| 2015 | -0.2 |
| 2016 (OOS) | -0.0 |
| 2017 (OOS) | 0.1 |
| 2018 (OOS) | -0.0 |
| 2019 (OOS) | 0.1 |
| 2020 (OOS) | -0.1 |
| 2021 (OOS) | -0.1 |
| 2022 (OOS) | 0.1 |
| 2023 (OOS) | -0.1 |
| 2024 (OOS) | -0.0 |
| 2025 (OOS) | 0.1 |
| 2026 (OOS) | 0.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 0.5% from a peak in-sample and 0.6% out-of-sample, and the worst single trade cost 5.7% of the account out-of-sample. About 37 of every 100 trades won in-sample. Out-of-sample it earned 0.0% a year against 0.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 117 | `{"max_candles": 68, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 118 | `{"max_candles": 76, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 119 | `{"max_candles": 72, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | 1.00 |
| 391 | `{"max_candles": 40, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 554 | `{"max_candles": 84, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 666 | `{"max_candles": 28, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 805 | `{"max_candles": 60, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1051 | `{"max_candles": 48, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1087 | `{"max_candles": 64, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1093 | `{"max_candles": 80, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1145 | `{"max_candles": 92, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1246 | `{"max_candles": 88, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1322 | `{"max_candles": 52, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1347 | `{"max_candles": 96, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1733 | `{"max_candles": 44, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 1969 | `{"max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2325 | `{"max_candles": 36, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2331 | `{"max_candles": 56, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2485 | `{"max_candles": 28, "stop_atr": 4.75, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2487 | `{"max_candles": 36, "stop_atr": 4.75, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2491 | `{"max_candles": 68, "stop_atr": 4.25, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2492 | `{"max_candles": 72, "stop_atr": 4.5, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2496 | `{"max_candles": 44, "stop_atr": 4.75, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2500 | `{"max_candles": 48, "stop_atr": 4.75, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |
| 2501 | `{"max_candles": 48, "stop_atr": 4.5, "take_profit_atr": 4.0}` | 53.24 | 0.0 | -0.5 | 37.0 | 6.28 | 0.0 | -0.6 | 0.33 | 146/133 | not checked |

(66 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 3,074 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
