# kst_cycle_confirmation__broad: optimization summary

Updated 2026-11-26T04:01:37Z · backtest.py version `b61a1cc422` · 6,854 parameter sets tested with this version (6,854 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [kst_cycle_confirmation__broad__max-income__v001.md](kst_cycle_confirmation__broad__max-income__v001.md) | 179 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [kst_cycle_confirmation__broad__balanced__v002.md](kst_cycle_confirmation__broad__balanced__v002.md) | 6854 | `{"max_candles": 96, "signal": 21, "stop_atr": 2.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 721.06 | 530.27 | 662.85 | 399.55 |
| return % | 7.21 | 5.30 | 6.63 | 4.00 |
| return %/year | 0.3 | 0.5 | 0.3 | 0.4 |
| gross profit | 4,380.21 | 4,627.28 | 4,324.74 | 4,497.68 |
| gross loss | 3,659.15 | 4,097.01 | 3,661.89 | 4,098.13 |
| trades | 1,751 | 1,833 | 1,751 | 1,833 |
| win rate % | 46.8 | 48.1 | 45.6 | 46.6 |
| avg win | 5.34 | 5.25 | 5.42 | 5.27 |
| avg loss | -3.93 | -4.30 | -3.84 | -4.19 |
| avg result / trade | 0.41 | 0.29 | 0.38 | 0.22 |
| largest single loss | -30.71 | -57.72 | -31.85 | -50.30 |
| largest loss % of equity | -23.74 | -26.68 | -21.76 | -27.42 |
| max drawdown | -535.67 | -510.76 | -434.31 | -444.40 |
| max drawdown % | -5.08 | -4.72 | -4.15 | -4.12 |
| profit factor | 1.20 | 1.13 | 1.18 | 1.10 |
| unusually bad trades | 200 | 249 | 144 | 170 |
| … threshold (% of equity) | 3.5 | 3.4 | 3.9 | 3.9 |
| time in market % | 7.3 | 14.7 | 7.0 | 14.0 |
| buy & hold return % | 127.68 | 280.36 | 127.68 | 280.36 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.46 |  | 1.16 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.2 | 0.1 |
| 1996 | 0.8 | 0.6 |
| 1997 | 0.7 | 0.7 |
| 1998 | 0.9 | 0.8 |
| 1999 | -0.1 | 0.0 |
| 2000 | -0.2 | -0.4 |
| 2001 | -0.2 | -0.2 |
| 2002 | 0.1 | -0.0 |
| 2003 | 0.7 | 0.4 |
| 2004 | 1.3 | 1.2 |
| 2005 | -0.3 | -0.2 |
| 2006 | 1.1 | 1.0 |
| 2007 | -1.3 | -0.8 |
| 2008 | -0.5 | -0.4 |
| 2009 | -1.5 | -1.4 |
| 2010 | 1.0 | 1.1 |
| 2011 | 1.4 | 1.3 |
| 2012 | 0.7 | 0.6 |
| 2013 | 2.0 | 1.7 |
| 2014 | 1.3 | 1.1 |
| 2015 | -0.9 | -0.9 |
| 2016 (OOS) | -0.5 | -0.5 |
| 2017 (OOS) | 3.0 | 2.6 |
| 2018 (OOS) | 1.0 | 0.5 |
| 2019 (OOS) | 2.5 | 2.3 |
| 2020 (OOS) | 0.3 | 1.2 |
| 2021 (OOS) | 0.9 | 0.0 |
| 2022 (OOS) | -2.1 | -1.9 |
| 2023 (OOS) | 0.6 | 0.5 |
| 2024 (OOS) | 1.0 | 0.9 |
| 2025 (OOS) | -0.5 | -0.5 |
| 2026 (OOS) | -0.6 | -1.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.1% from a peak in-sample and 4.7% out-of-sample, and the worst single trade cost 26.7% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.2% from a peak in-sample and 4.1% out-of-sample, and the worst single trade cost 27.4% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 188 | `{"max_candles": 64, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 231 | `{"max_candles": 96, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 237 | `{"max_candles": 104, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 242 | `{"max_candles": 48, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.10 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 302 | `{"max_candles": 56, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 341 | `{"max_candles": 72, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 346 | `{"max_candles": 80, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 363 | `{"max_candles": 112, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 797 | `{"max_candles": 120, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 812 | `{"max_candles": 144, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 814 | `{"max_candles": 128, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 843 | `{"max_candles": 136, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 1538 | `{"max_candles": 160, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 1818 | `{"max_candles": 168, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 1853 | `{"max_candles": 152, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 2304 | `{"max_candles": 184, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 2854 | `{"max_candles": 176, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 3705 | `{"max_candles": 192, "signal": 21, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 730.00 | 0.3 | -5.0 | 46.6 | 483.81 | 0.4 | -4.6 | 1.26 | 1751/1833 | not checked |
| 193 | `{"max_candles": 96, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 679.69 | 0.3 | -4.6 | 46.0 | 485.63 | 0.4 | -4.4 | 1.42 | 1751/1833 | not checked |
| 213 | `{"max_candles": 80, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 679.69 | 0.3 | -4.6 | 46.0 | 485.63 | 0.4 | -4.4 | 1.42 | 1751/1833 | not checked |
| 266 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 679.69 | 0.3 | -4.6 | 46.0 | 485.63 | 0.4 | -4.4 | 1.42 | 1751/1833 | not checked |
| 275 | `{"max_candles": 48, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 679.69 | 0.3 | -4.6 | 46.0 | 484.91 | 0.4 | -4.4 | 1.42 | 1751/1833 | not checked |
| 315 | `{"max_candles": 56, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 679.69 | 0.3 | -4.6 | 46.0 | 485.63 | 0.4 | -4.4 | 1.42 | 1751/1833 | not checked |
| 343 | `{"max_candles": 104, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 679.69 | 0.3 | -4.6 | 46.0 | 485.63 | 0.4 | -4.4 | 1.42 | 1751/1833 | not checked |

(89 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 6,854 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
