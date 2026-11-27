# ease_of_movement_cross__broad: optimization summary

Updated 2026-11-25T23:27:08Z · backtest.py version `66df47bf4f` · 1,019 parameter sets tested with this version (1,019 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [ease_of_movement_cross__broad__max-income__v002.md](ease_of_movement_cross__broad__max-income__v002.md) | 1018 | `{"max_candles": 88, "n": 23, "stop_atr": 1.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [ease_of_movement_cross__broad__balanced__v002.md](ease_of_movement_cross__broad__balanced__v002.md) | 1019 | `{"max_candles": 12, "n": 19, "stop_atr": 1.75, "take_profit_atr": 2.5}` | long XLU since 2026-11-25 00:00 @ 43.312989; long TLT since 2026-11-25 00:00 @ 82.392707; long IEF since 2026-11-23 00:00 @ 91.317388; long AGG since 2026-11-24 00:00 @ 96.298878; long BND since 2026-11-23 00:00 @ 71.201354 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,721.66 | 1,364.83 | 1,057.64 | 395.44 |
| return % | 27.22 | 13.65 | 10.58 | 3.95 |
| return %/year | 1.1 | 1.2 | 0.5 | 0.4 |
| gross profit | 9,769.82 | 8,932.00 | 7,943.51 | 7,826.28 |
| gross loss | 7,048.15 | 7,567.17 | 6,885.87 | 7,430.84 |
| trades | 4,674 | 4,787 | 5,039 | 5,212 |
| win rate % | 34.9 | 33.0 | 46.2 | 44.4 |
| avg win | 5.99 | 5.65 | 3.41 | 3.39 |
| avg loss | -2.32 | -2.36 | -2.54 | -2.56 |
| avg result / trade | 0.58 | 0.29 | 0.21 | 0.08 |
| largest single loss | -15.81 | -31.72 | -20.68 | -32.68 |
| largest loss % of equity | -4.28 | -5.85 | -13.03 | -9.81 |
| max drawdown | -633.03 | -554.02 | -581.44 | -714.31 |
| max drawdown % | -5.76 | -4.79 | -5.65 | -6.51 |
| profit factor | 1.39 | 1.18 | 1.15 | 1.05 |
| unusually bad trades | 289 | 297 | 505 | 558 |
| … threshold (% of equity) | 2.3 | 2.3 | 2.5 | 2.3 |
| time in market % | 11.4 | 21.6 | 7.6 | 14.8 |
| buy & hold return % | 124.13 | 280.02 | 124.13 | 280.02 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.03 |  | 0.75 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.5 | 0.4 |
| 1996 | 0.5 | 0.2 |
| 1997 | 0.3 | 0.5 |
| 1998 | 1.3 | 0.2 |
| 1999 | 1.1 | 0.8 |
| 2000 | -1.6 | -0.2 |
| 2001 | -1.5 | -2.4 |
| 2002 | -1.6 | -0.8 |
| 2003 | 2.3 | 0.8 |
| 2004 | 0.7 | 0.5 |
| 2005 | 0.9 | 0.5 |
| 2006 | -0.3 | -0.2 |
| 2007 | 2.0 | 1.1 |
| 2008 | -0.0 | -0.2 |
| 2009 | 9.6 | 3.8 |
| 2010 | 7.2 | 2.0 |
| 2011 | -2.0 | -2.7 |
| 2012 | 3.9 | 1.1 |
| 2013 | 4.2 | 4.4 |
| 2014 | 0.2 | 1.9 |
| 2015 | -2.9 | -1.4 |
| 2016 (OOS) | 0.0 | -0.7 |
| 2017 (OOS) | 2.7 | 1.9 |
| 2018 (OOS) | 0.1 | -1.0 |
| 2019 (OOS) | 3.1 | 3.8 |
| 2020 (OOS) | 4.0 | 3.2 |
| 2021 (OOS) | 3.4 | 2.3 |
| 2022 (OOS) | -2.8 | -3.5 |
| 2023 (OOS) | 3.7 | 2.3 |
| 2024 (OOS) | -2.1 | -2.0 |
| 2025 (OOS) | -1.0 | -1.3 |
| 2026 (OOS) | 3.0 | -1.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.8% from a peak in-sample and 4.8% out-of-sample, and the worst single trade cost 5.8% of the account out-of-sample. About 35 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 5.7% from a peak in-sample and 6.5% out-of-sample, and the worst single trade cost 9.8% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1015 | `{"max_candles": 60, "n": 23, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 2,840.53 | 1.2 | -5.8 | 34.8 | 1,613.45 | 1.4 | -4.8 | 1.15 | 4674/4787 | not checked |
| 616 | `{"max_candles": 76, "n": 23, "stop_atr": 1.0, "take_profit_atr": 5.5}` | 2,728.28 | 1.2 | -5.8 | 34.9 | 1,365.77 | 1.2 | -4.8 | 1.02 | 4674/4787 | not checked |
| 610 | `{"max_candles": 76, "n": 23, "stop_atr": 1.0, "take_profit_atr": 5.0}` | 2,639.89 | 1.1 | -5.6 | 35.0 | 1,146.31 | 1.0 | -4.7 | 0.89 | 4674/4787 | not checked |
| 510 | `{"max_candles": 92, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 849.97 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 547 | `{"max_candles": 88, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 847.40 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 567 | `{"max_candles": 96, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 849.19 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 582 | `{"max_candles": 84, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 848.42 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 667 | `{"max_candles": 76, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 848.35 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 681 | `{"max_candles": 80, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 848.67 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 692 | `{"max_candles": 72, "n": 23, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 2,412.57 | 1.0 | -5.5 | 35.1 | 847.85 | 0.8 | -4.6 | 0.73 | 4674/4787 | not checked |
| 702 | `{"max_candles": 72, "n": 23, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 2,394.54 | 1.0 | -5.3 | 30.3 | 1,323.16 | 1.1 | -3.9 | 1.12 | 4674/4787 | not checked |
| 714 | `{"max_candles": 76, "n": 23, "stop_atr": 0.75, "take_profit_atr": 5.5}` | 2,322.34 | 1.0 | -5.2 | 30.4 | 1,154.29 | 1.0 | -3.8 | 1.01 | 4674/4787 | not checked |
| 695 | `{"max_candles": 76, "n": 23, "stop_atr": 0.75, "take_profit_atr": 5.0}` | 2,233.65 | 1.0 | -5.1 | 30.6 | 965.15 | 0.8 | -3.6 | 0.89 | 4674/4787 | not checked |
| 599 | `{"max_candles": 92, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 726.54 | 0.7 | -3.5 | 0.73 | 4674/4787 | not checked |
| 621 | `{"max_candles": 88, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 723.64 | 0.6 | -3.5 | 0.72 | 4674/4787 | not checked |
| 637 | `{"max_candles": 80, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 725.08 | 0.7 | -3.5 | 0.73 | 4674/4787 | not checked |
| 691 | `{"max_candles": 76, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 724.71 | 0.6 | -3.5 | 0.72 | 4674/4787 | not checked |
| 738 | `{"max_candles": 84, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 724.79 | 0.6 | -3.5 | 0.72 | 4674/4787 | not checked |
| 808 | `{"max_candles": 96, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 725.66 | 0.7 | -3.5 | 0.73 | 4674/4787 | not checked |
| 854 | `{"max_candles": 72, "n": 23, "stop_atr": 0.75, "take_profit_atr": 4.5}` | 2,034.93 | 0.9 | -4.9 | 30.7 | 724.16 | 0.6 | -3.5 | 0.72 | 4674/4787 | not checked |
| 755 | `{"max_candles": 68, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 1,766.32 | 0.8 | -4.6 | 29.8 | 872.71 | 0.8 | -6.9 | 0.99 | 4566/4744 | not checked |
| 607 | `{"max_candles": 76, "n": 24, "stop_atr": 0.75, "take_profit_atr": 5.5}` | 1,657.29 | 0.7 | -4.4 | 29.9 | 768.42 | 0.7 | -7.0 | 0.93 | 4566/4744 | not checked |
| 734 | `{"max_candles": 80, "n": 24, "stop_atr": 0.75, "take_profit_atr": 5.5}` | 1,657.29 | 0.7 | -4.4 | 29.9 | 768.33 | 0.7 | -7.0 | 0.93 | 4566/4744 | not checked |
| 760 | `{"max_candles": 88, "n": 24, "stop_atr": 0.75, "take_profit_atr": 5.5}` | 1,657.29 | 0.7 | -4.4 | 29.9 | 768.51 | 0.7 | -7.0 | 0.93 | 4566/4744 | not checked |
| 852 | `{"max_candles": 92, "n": 24, "stop_atr": 0.75, "take_profit_atr": 5.5}` | 1,657.29 | 0.7 | -4.4 | 29.9 | 769.53 | 0.7 | -7.0 | 0.93 | 4566/4744 | not checked |

(24 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,019 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
