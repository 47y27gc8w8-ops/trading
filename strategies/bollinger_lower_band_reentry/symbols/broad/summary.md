# bollinger_lower_band_reentry__broad: optimization summary

Updated 2026-11-25T18:45:57Z · backtest.py version `1ca8bee48e` · 13,453 parameter sets tested with this version (13,453 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [bollinger_lower_band_reentry__broad__max-income__v002.md](bollinger_lower_band_reentry__broad__max-income__v002.md) | 13452 | `{"k": 3.4, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 3.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [bollinger_lower_band_reentry__broad__balanced__v002.md](bollinger_lower_band_reentry__broad__balanced__v002.md) | 13453 | `{"k": 3.5, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 1.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 187.74 | 131.20 | 131.91 | 77.41 |
| return % | 1.88 | 1.31 | 1.32 | 0.77 |
| return %/year | 0.1 | 0.1 | 0.1 | 0.1 |
| gross profit | 272.75 | 259.23 | 159.62 | 173.57 |
| gross loss | 85.01 | 128.04 | 27.71 | 96.17 |
| trades | 71 | 82 | 49 | 64 |
| win rate % | 81.7 | 76.8 | 81.6 | 79.7 |
| avg win | 4.70 | 4.11 | 3.99 | 3.40 |
| avg loss | -6.54 | -6.74 | -3.08 | -7.40 |
| avg result / trade | 2.64 | 1.60 | 2.69 | 1.21 |
| largest single loss | -28.35 | -13.31 | -6.53 | -13.31 |
| largest loss % of equity | -15.31 | -7.19 | -3.53 | -7.19 |
| max drawdown | -104.87 | -152.61 | -41.45 | -131.62 |
| max drawdown % | -1.04 | -1.52 | -0.41 | -1.31 |
| profit factor | 3.21 | 2.02 | 5.76 | 1.80 |
| unusually bad trades | 2 | 0 | 4 | 0 |
| … threshold (% of equity) | 5.4 | 8.6 | 2.0 | 9.2 |
| time in market % | 0.3 | 0.5 | 0.1 | 0.3 |
| buy & hold return % | 108.03 | 303.57 | 108.03 | 303.57 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.33 |  | 1.17 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.0 | 0.0 |
| 1996 | 0.0 | 0.0 |
| 1997 | 0.0 | 0.0 |
| 1998 | 0.0 | 0.0 |
| 1999 | 0.0 | 0.0 |
| 2000 | 0.3 | 0.2 |
| 2001 | 0.2 | 0.1 |
| 2002 | -0.2 | -0.0 |
| 2003 | 0.0 | 0.0 |
| 2004 | 0.0 | -0.0 |
| 2005 | 0.0 | 0.0 |
| 2006 | 0.0 | 0.0 |
| 2007 | 0.2 | 0.1 |
| 2008 | 0.1 | 0.0 |
| 2009 | 0.0 | 0.0 |
| 2010 | -0.0 | -0.1 |
| 2011 | 0.2 | 0.0 |
| 2012 | 0.0 | 0.0 |
| 2013 | -0.3 | 0.0 |
| 2014 | 0.4 | 0.2 |
| 2015 | 0.9 | 0.6 |
| 2016 (OOS) | 0.3 | 0.3 |
| 2017 (OOS) | 0.0 | 0.0 |
| 2018 (OOS) | -0.8 | -0.6 |
| 2019 (OOS) | 0.2 | 0.2 |
| 2020 (OOS) | 0.1 | 0.1 |
| 2021 (OOS) | 0.7 | 0.4 |
| 2022 (OOS) | -0.1 | -0.1 |
| 2023 (OOS) | -0.1 | -0.1 |
| 2024 (OOS) | 0.0 | 0.0 |
| 2025 (OOS) | 0.8 | 0.5 |
| 2026 (OOS) | 0.1 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 1.0% from a peak in-sample and 1.5% out-of-sample, and the worst single trade cost 7.2% of the account out-of-sample. About 82 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.4% from a peak in-sample and 1.3% out-of-sample, and the worst single trade cost 7.2% of the account out-of-sample. About 82 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 789 | `{"k": 3.1, "max_bars": 16, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 194.78 | 0.1 | -1.6 | 76.6 | 341.14 | 0.3 | -2.5 | 3.44 | 175/245 | not checked |
| 344 | `{"k": 3.4, "max_bars": 18, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 189.05 | 0.1 | -1.1 | 83.1 | 130.46 | 0.1 | -1.5 | 1.33 | 71/82 | not checked |
| 366 | `{"k": 3.4, "max_bars": 20, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 189.05 | 0.1 | -1.1 | 83.1 | 127.00 | 0.1 | -1.6 | 1.33 | 71/82 | not checked |
| 395 | `{"k": 3.4, "max_bars": 22, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 189.05 | 0.1 | -1.1 | 83.1 | 131.29 | 0.1 | -1.5 | 1.33 | 71/82 | not checked |
| 465 | `{"k": 3.4, "max_bars": 24, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 189.05 | 0.1 | -1.1 | 83.1 | 141.91 | 0.1 | -1.4 | 1.44 | 71/82 | not checked |
| 300 | `{"k": 3.4, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 187.74 | 0.1 | -1.0 | 81.7 | 131.20 | 0.1 | -1.5 | 1.33 | 71/82 | 1.00 |
| 307 | `{"k": 3.4, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 187.74 | 0.1 | -1.0 | 81.7 | 127.74 | 0.1 | -1.6 | 1.33 | 71/82 | not checked |
| 410 | `{"k": 3.4, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 187.74 | 0.1 | -1.0 | 81.7 | 132.03 | 0.1 | -1.5 | 1.33 | 71/82 | not checked |
| 533 | `{"k": 3.4, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 187.74 | 0.1 | -1.0 | 81.7 | 142.65 | 0.1 | -1.4 | 1.44 | 71/82 | not checked |
| 305 | `{"k": 3.4, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 182.69 | 0.1 | -1.0 | 81.7 | 120.63 | 0.1 | -1.5 | 1.22 | 71/82 | not checked |
| 355 | `{"k": 3.4, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 182.69 | 0.1 | -1.0 | 81.7 | 117.11 | 0.1 | -1.6 | 1.22 | 71/82 | not checked |
| 407 | `{"k": 3.4, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 182.69 | 0.1 | -1.0 | 81.7 | 121.40 | 0.1 | -1.5 | 1.22 | 71/82 | not checked |
| 550 | `{"k": 3.4, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 182.69 | 0.1 | -1.0 | 81.7 | 132.02 | 0.1 | -1.4 | 1.33 | 71/82 | not checked |
| 303 | `{"k": 3.5, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 178.43 | 0.1 | -0.8 | 79.6 | 96.60 | 0.1 | -1.5 | 1.12 | 49/64 | 1.00 |
| 315 | `{"k": 3.5, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 178.43 | 0.1 | -0.8 | 79.6 | 92.96 | 0.1 | -1.5 | 1.12 | 49/64 | not checked |
| 506 | `{"k": 3.5, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 178.43 | 0.1 | -0.8 | 79.6 | 107.88 | 0.1 | -1.4 | 1.25 | 49/64 | not checked |
| 507 | `{"k": 3.5, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 178.43 | 0.1 | -0.8 | 79.6 | 97.25 | 0.1 | -1.5 | 1.12 | 49/64 | not checked |
| 313 | `{"k": 3.5, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 173.62 | 0.1 | -0.7 | 79.6 | 89.78 | 0.1 | -1.5 | 1.00 | 49/64 | 1.00 |
| 324 | `{"k": 3.5, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 173.62 | 0.1 | -0.7 | 79.6 | 86.11 | 0.1 | -1.5 | 1.00 | 49/64 | not checked |
| 398 | `{"k": 3.5, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 173.62 | 0.1 | -0.7 | 79.6 | 90.40 | 0.1 | -1.5 | 1.00 | 49/64 | not checked |
| 499 | `{"k": 3.5, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 173.62 | 0.1 | -0.7 | 79.6 | 101.03 | 0.1 | -1.4 | 1.12 | 49/64 | not checked |
| 322 | `{"k": 3.5, "max_bars": 18, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 162.20 | 0.1 | -0.6 | 79.6 | 103.27 | 0.1 | -1.3 | 1.12 | 49/64 | not checked |
| 351 | `{"k": 3.5, "max_bars": 24, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 162.20 | 0.1 | -0.6 | 79.6 | 114.49 | 0.1 | -1.2 | 1.25 | 49/64 | not checked |
| 481 | `{"k": 3.5, "max_bars": 20, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 162.20 | 0.1 | -0.6 | 79.6 | 99.58 | 0.1 | -1.3 | 1.12 | 49/64 | not checked |
| 1383 | `{"k": 3.5, "max_bars": 22, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 162.20 | 0.1 | -0.6 | 79.6 | 103.87 | 0.1 | -1.3 | 1.12 | 49/64 | not checked |

(16 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 13,453 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
