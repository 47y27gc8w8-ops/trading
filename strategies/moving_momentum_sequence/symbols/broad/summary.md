# moving_momentum_sequence__broad: optimization summary

Updated 2026-11-25T23:54:42Z · backtest.py version `d97ae6e4c4` · 880 parameter sets tested with this version (880 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [moving_momentum_sequence__broad__max-income__v002.md](moving_momentum_sequence__broad__max-income__v002.md) | 879 | `{"max_candles": 24, "oversold": 15, "stop_atr": 3.75, "take_profit_atr": 4.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [moving_momentum_sequence__broad__balanced__v002.md](moving_momentum_sequence__broad__balanced__v002.md) | 880 | `{"max_candles": 168, "oversold": 6, "stop_atr": 1.0, "take_profit_atr": 4.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 231.98 | 517.82 | 35.92 | 68.21 |
| return % | 2.32 | 5.18 | 0.36 | 0.68 |
| return %/year | 0.1 | 0.5 | 0.0 | 0.1 |
| gross profit | 880.37 | 1,178.96 | 78.81 | 164.20 |
| gross loss | 648.40 | 661.14 | 42.89 | 95.99 |
| trades | 651 | 554 | 73 | 80 |
| win rate % | 61.9 | 63.0 | 63.0 | 48.8 |
| avg win | 2.18 | 3.38 | 1.71 | 4.21 |
| avg loss | -2.61 | -3.23 | -1.59 | -2.34 |
| avg result / trade | 0.36 | 0.93 | 0.49 | 0.85 |
| largest single loss | -29.79 | -70.65 | -3.94 | -14.29 |
| largest loss % of equity | -15.61 | -29.21 | -2.10 | -6.23 |
| max drawdown | -154.12 | -163.47 | -11.65 | -36.14 |
| max drawdown % | -1.51 | -1.58 | -0.12 | -0.36 |
| profit factor | 1.36 | 1.78 | 1.84 | 1.71 |
| unusually bad trades | 51 | 45 | 1 | 8 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 0.8 | 1.6 | 0.1 | 0.2 |
| buy & hold return % | 97.45 | 303.60 | 97.45 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 4.18 |  | 3.00 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.0 | 0.0 |
| 1996 | 0.0 | 0.0 |
| 1997 | 0.0 | 0.0 |
| 1998 | 0.0 | 0.0 |
| 1999 | -0.0 | 0.0 |
| 2000 | 0.1 | 0.0 |
| 2001 | -0.1 | 0.0 |
| 2002 | -0.1 | 0.0 |
| 2003 | 0.3 | 0.0 |
| 2004 | 0.0 | 0.1 |
| 2005 | 0.0 | 0.0 |
| 2006 | -0.2 | 0.0 |
| 2007 | 0.4 | 0.0 |
| 2008 | 0.1 | 0.0 |
| 2009 | 1.2 | -0.0 |
| 2010 | 0.4 | 0.0 |
| 2011 | -0.0 | 0.0 |
| 2012 | -0.7 | 0.1 |
| 2013 | 0.3 | 0.1 |
| 2014 | 0.3 | 0.1 |
| 2015 | 0.4 | -0.0 |
| 2016 (OOS) | 0.1 | 0.3 |
| 2017 (OOS) | 0.2 | -0.0 |
| 2018 (OOS) | 0.1 | -0.1 |
| 2019 (OOS) | 0.3 | -0.0 |
| 2020 (OOS) | 2.5 | 0.0 |
| 2021 (OOS) | 0.2 | -0.0 |
| 2022 (OOS) | -0.5 | 0.0 |
| 2023 (OOS) | 0.1 | -0.1 |
| 2024 (OOS) | 1.3 | 0.3 |
| 2025 (OOS) | -0.2 | 0.1 |
| 2026 (OOS) | 1.1 | 0.3 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 1.5% from a peak in-sample and 1.6% out-of-sample, and the worst single trade cost 29.2% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.1% from a peak in-sample and 0.4% out-of-sample, and the worst single trade cost 6.2% of the account out-of-sample. About 63 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 434 | `{"max_candles": 24, "oversold": 15, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 234.90 | 0.1 | -1.6 | 62.1 | 513.52 | 0.5 | -1.6 | 4.18 | 651/552 | not checked |
| 437 | `{"max_candles": 24, "oversold": 15, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 231.98 | 0.1 | -1.5 | 61.9 | 517.82 | 0.5 | -1.6 | 4.18 | 651/554 | 1.00 |
| 375 | `{"max_candles": 12, "oversold": 15, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 217.48 | 0.1 | -1.5 | 60.8 | 539.31 | 0.5 | -1.2 | 4.80 | 655/560 | not checked |
| 412 | `{"max_candles": 36, "oversold": 15, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 208.15 | 0.1 | -1.5 | 61.8 | 496.69 | 0.5 | -1.6 | 4.50 | 651/551 | not checked |
| 583 | `{"max_candles": 24, "oversold": 13, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 183.28 | 0.1 | -1.4 | 62.1 | 482.57 | 0.4 | -0.9 | 4.78 | 512/431 | not checked |
| 37 | `{"max_candles": 108, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 534.63 | 0.5 | -1.9 | 6.00 | 865/744 | not checked |
| 302 | `{"max_candles": 84, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 545.43 | 0.5 | -1.9 | 6.12 | 865/745 | not checked |
| 414 | `{"max_candles": 132, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 534.63 | 0.5 | -1.9 | 6.00 | 865/744 | not checked |
| 476 | `{"max_candles": 120, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 534.63 | 0.5 | -1.9 | 6.00 | 865/744 | not checked |
| 495 | `{"max_candles": 96, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 511.70 | 0.5 | -1.9 | 5.75 | 865/744 | not checked |
| 515 | `{"max_candles": 72, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 542.94 | 0.5 | -1.9 | 6.12 | 865/745 | not checked |
| 624 | `{"max_candles": 144, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 173.05 | 0.1 | -1.4 | 59.2 | 534.63 | 0.5 | -1.9 | 6.00 | 865/744 | not checked |
| 292 | `{"max_candles": 108, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 663.41 | 0.6 | -1.9 | 7.38 | 865/745 | not checked |
| 475 | `{"max_candles": 84, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 663.41 | 0.6 | -1.9 | 7.38 | 865/745 | not checked |
| 477 | `{"max_candles": 120, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 663.41 | 0.6 | -1.9 | 7.38 | 865/745 | not checked |
| 505 | `{"max_candles": 132, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 663.41 | 0.6 | -1.9 | 7.38 | 865/745 | not checked |
| 523 | `{"max_candles": 96, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 663.41 | 0.6 | -1.9 | 7.38 | 865/745 | not checked |
| 564 | `{"max_candles": 72, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 623.21 | 0.6 | -1.9 | 7.00 | 865/745 | not checked |
| 645 | `{"max_candles": 144, "oversold": 18, "stop_atr": 2.25, "take_profit_atr": 3.0}` | 170.07 | 0.1 | -1.4 | 59.2 | 663.41 | 0.6 | -1.9 | 7.38 | 865/745 | not checked |
| 790 | `{"max_candles": 24, "oversold": 13, "stop_atr": 3.25, "take_profit_atr": 4.0}` | 152.96 | 0.1 | -1.3 | 61.8 | 474.91 | 0.4 | -0.9 | 6.14 | 513/433 | not checked |
| 246 | `{"max_candles": 48, "oversold": 10, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 138.90 | 0.1 | -0.9 | 61.0 | 416.76 | 0.4 | -0.6 | 5.43 | 282/261 | not checked |
| 398 | `{"max_candles": 48, "oversold": 10, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 137.79 | 0.1 | -0.9 | 61.0 | 419.78 | 0.4 | -0.6 | 5.43 | 282/261 | not checked |
| 253 | `{"max_candles": 48, "oversold": 10, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 112.31 | 0.1 | -0.9 | 60.4 | 425.02 | 0.4 | -0.6 | 7.60 | 283/261 | not checked |
| 240 | `{"max_candles": 84, "oversold": 10, "stop_atr": 3.25, "take_profit_atr": 4.0}` | 108.94 | 0.1 | -0.9 | 60.4 | 537.08 | 0.5 | -0.5 | 9.60 | 283/262 | not checked |
| 191 | `{"max_candles": 168, "oversold": 10, "stop_atr": 1.75, "take_profit_atr": 3.5}` | 105.02 | 0.1 | -0.7 | 57.2 | 418.67 | 0.4 | -0.6 | 7.60 | 283/266 | not checked |

(29 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 880 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
