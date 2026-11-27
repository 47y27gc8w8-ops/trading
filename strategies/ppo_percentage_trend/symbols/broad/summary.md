# ppo_percentage_trend__broad: optimization summary

Updated 2026-11-25T09:51:19Z · backtest.py version `e01275ffba` · 935 parameter sets tested with this version (935 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [ppo_percentage_trend__broad__max-income__v002.md](ppo_percentage_trend__broad__max-income__v002.md) | 934 | `{"max_candles": 168, "stop_atr": 3.75, "take_profit_atr": 6.5, "threshold": 2.25}` | long XLP since 2026-10-29 00:00 @ 87.856351; long USMV since 2026-08-10 00:00 @ 100.390506; long SQQQ since 2026-11-18 00:00 @ 46.043808 |
| balanced | [ppo_percentage_trend__broad__balanced__v002.md](ppo_percentage_trend__broad__balanced__v002.md) | 935 | `{"max_candles": 168, "stop_atr": 3.75, "take_profit_atr": 6.0, "threshold": 2.25}` | long XLP since 2026-10-29 00:00 @ 87.856351; long USMV since 2026-08-10 00:00 @ 100.390506; long SQQQ since 2026-11-18 00:00 @ 46.043808 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,174.94 | 3,807.93 | 2,929.17 | 3,382.42 |
| return % | 31.75 | 38.08 | 29.29 | 33.82 |
| return %/year | 1.3 | 3.0 | 1.2 | 2.7 |
| gross profit | 6,913.23 | 8,430.74 | 6,559.32 | 7,871.28 |
| gross loss | 3,738.29 | 4,622.81 | 3,630.16 | 4,488.85 |
| trades | 595 | 688 | 600 | 696 |
| win rate % | 50.1 | 51.5 | 51.7 | 53.0 |
| avg win | 23.20 | 23.82 | 21.16 | 21.33 |
| avg loss | -12.59 | -13.84 | -12.52 | -13.73 |
| avg result / trade | 5.34 | 5.53 | 4.88 | 4.86 |
| largest single loss | -47.57 | -146.74 | -45.54 | -125.79 |
| largest loss % of equity | -12.71 | -16.78 | -12.71 | -16.78 |
| max drawdown | -559.66 | -1,033.12 | -532.81 | -918.82 |
| max drawdown % | -4.79 | -8.32 | -4.76 | -7.51 |
| profit factor | 1.85 | 1.82 | 1.81 | 1.75 |
| unusually bad trades | 20 | 29 | 20 | 28 |
| … threshold (% of equity) | 9.0 | 9.3 | 9.1 | 9.4 |
| time in market % | 12.3 | 25.5 | 11.5 | 24.2 |
| buy & hold return % | 93.18 | 305.70 | 93.18 | 305.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.26 |  | 2.20 |
| period | 1995-01-23 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-23 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.1 |
| 1996 | 0.0 | 0.0 |
| 1997 | 0.2 | 0.2 |
| 1998 | 0.5 | 0.5 |
| 1999 | 0.1 | 0.1 |
| 2000 | -0.7 | -0.7 |
| 2001 | -1.1 | -1.1 |
| 2002 | -1.3 | -1.3 |
| 2003 | 3.9 | 3.9 |
| 2004 | 1.3 | 1.2 |
| 2005 | -1.1 | -0.9 |
| 2006 | 3.6 | 3.3 |
| 2007 | 1.6 | 1.6 |
| 2008 | -2.5 | -2.5 |
| 2009 | 10.5 | 9.6 |
| 2010 | 7.8 | 8.0 |
| 2011 | -2.3 | -2.2 |
| 2012 | 1.2 | 1.0 |
| 2013 | 5.3 | 5.0 |
| 2014 | 3.3 | 2.8 |
| 2015 | -1.7 | -1.6 |
| 2016 (OOS) | 0.1 | 0.3 |
| 2017 (OOS) | 5.6 | 5.0 |
| 2018 (OOS) | -0.0 | 0.6 |
| 2019 (OOS) | 3.9 | 3.6 |
| 2020 (OOS) | 9.5 | 8.8 |
| 2021 (OOS) | 3.2 | 2.8 |
| 2022 (OOS) | -5.6 | -5.2 |
| 2023 (OOS) | 3.1 | 2.3 |
| 2024 (OOS) | 5.7 | 5.1 |
| 2025 (OOS) | 5.5 | 4.7 |
| 2026 (OOS) | 2.9 | 2.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.8% from a peak in-sample and 8.3% out-of-sample, and the worst single trade cost 16.8% of the account out-of-sample. About 50 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.8% from a peak in-sample and 7.5% out-of-sample, and the worst single trade cost 16.8% of the account out-of-sample. About 52 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 403 | `{"max_candles": 168, "stop_atr": 4.0, "take_profit_atr": 6.5, "threshold": 2.25}` | 3,193.71 | 1.3 | -4.8 | 51.0 | 4,301.63 | 3.3 | -8.8 | 2.51 | 588/674 | not checked |
| 397 | `{"max_candles": 168, "stop_atr": 3.75, "take_profit_atr": 6.5, "threshold": 2.25}` | 3,174.94 | 1.3 | -4.8 | 50.1 | 3,807.93 | 3.0 | -8.3 | 2.26 | 595/688 | 1.00 |
| 473 | `{"max_candles": 168, "stop_atr": 4.0, "take_profit_atr": 7.0, "threshold": 2.25}` | 3,115.96 | 1.3 | -4.8 | 49.2 | 4,361.66 | 3.4 | -9.4 | 2.60 | 583/657 | not checked |
| 404 | `{"max_candles": 168, "stop_atr": 3.75, "take_profit_atr": 7.0, "threshold": 2.25}` | 3,108.81 | 1.3 | -4.7 | 48.3 | 3,859.00 | 3.0 | -8.8 | 2.34 | 590/671 | not checked |
| 777 | `{"max_candles": 168, "stop_atr": 3.25, "take_profit_atr": 7.0, "threshold": 2.25}` | 2,946.89 | 1.2 | -4.7 | 45.2 | 3,470.22 | 2.8 | -8.2 | 2.23 | 613/694 | not checked |
| 834 | `{"max_candles": 168, "stop_atr": 3.0, "take_profit_atr": 7.0, "threshold": 2.25}` | 2,788.40 | 1.2 | -4.7 | 42.6 | 3,507.86 | 2.8 | -7.8 | 2.37 | 631/703 | not checked |
| 827 | `{"max_candles": 168, "stop_atr": 3.0, "take_profit_atr": 6.0, "threshold": 1.75}` | 2,584.32 | 1.1 | -4.6 | 46.9 | 3,514.91 | 2.8 | -6.8 | 2.56 | 689/738 | not checked |
| 330 | `{"max_candles": 192, "stop_atr": 2.0, "take_profit_atr": 6.0, "threshold": 2.5}` | 2,579.70 | 1.1 | -4.4 | 38.9 | 3,120.20 | 2.5 | -6.3 | 2.30 | 674/803 | not checked |
| 491 | `{"max_candles": 168, "stop_atr": 3.75, "take_profit_atr": 5.0, "threshold": 2.25}` | 2,504.84 | 1.1 | -4.2 | 55.2 | 2,813.92 | 2.3 | -5.9 | 2.15 | 619/724 | not checked |
| 581 | `{"max_candles": 180, "stop_atr": 2.0, "take_profit_atr": 5.5, "threshold": 2.5}` | 2,298.22 | 1.0 | -4.0 | 39.7 | 2,654.21 | 2.2 | -5.7 | 2.21 | 682/815 | not checked |
| 685 | `{"max_candles": 168, "stop_atr": 2.0, "take_profit_atr": 5.0, "threshold": 2.5}` | 2,236.99 | 1.0 | -3.8 | 42.8 | 2,212.29 | 1.9 | -5.4 | 1.91 | 691/825 | not checked |
| 479 | `{"max_candles": 72, "stop_atr": 3.75, "take_profit_atr": 4.0, "threshold": 2.25}` | 1,916.18 | 0.8 | -3.7 | 60.9 | 1,991.11 | 1.7 | -4.5 | 2.00 | 649/763 | not checked |
| 789 | `{"max_candles": 180, "stop_atr": 1.5, "take_profit_atr": 6.5, "threshold": 2.25}` | 1,863.86 | 0.8 | -3.5 | 30.1 | 2,812.47 | 2.3 | -4.8 | 2.81 | 724/816 | not checked |
| 553 | `{"max_candles": 192, "stop_atr": 1.75, "take_profit_atr": 5.5, "threshold": 2.75}` | 1,634.53 | 0.7 | -3.5 | 35.2 | 2,997.15 | 2.4 | -4.2 | 3.34 | 696/815 | not checked |
| 681 | `{"max_candles": 180, "stop_atr": 1.75, "take_profit_atr": 5.5, "threshold": 2.75}` | 1,634.53 | 0.7 | -3.5 | 35.2 | 2,997.15 | 2.4 | -4.2 | 3.34 | 696/815 | not checked |
| 716 | `{"max_candles": 156, "stop_atr": 1.75, "take_profit_atr": 5.0, "threshold": 2.75}` | 1,620.43 | 0.7 | -3.4 | 37.7 | 2,319.63 | 1.9 | -4.3 | 2.68 | 703/828 | not checked |
| 314 | `{"max_candles": 108, "stop_atr": 1.5, "take_profit_atr": 5.0, "threshold": 2.5}` | 1,506.37 | 0.7 | -3.2 | 35.5 | 1,953.24 | 1.6 | -4.5 | 2.46 | 723/859 | not checked |
| 360 | `{"max_candles": 96, "stop_atr": 1.25, "take_profit_atr": 5.5, "threshold": 2.25}` | 1,499.23 | 0.7 | -3.0 | 29.5 | 1,765.52 | 1.5 | -3.7 | 2.24 | 750/855 | not checked |
| 294 | `{"max_candles": 156, "stop_atr": 1.25, "take_profit_atr": 4.5, "threshold": 2.5}` | 1,422.23 | 0.6 | -2.9 | 33.7 | 1,534.64 | 1.3 | -3.7 | 2.06 | 748/877 | not checked |
| 357 | `{"max_candles": 180, "stop_atr": 1.5, "take_profit_atr": 5.0, "threshold": 3.0}` | 1,294.63 | 0.6 | -2.4 | 32.9 | 1,754.33 | 1.5 | -3.3 | 2.59 | 700/826 | not checked |
| 630 | `{"max_candles": 84, "stop_atr": 1.75, "take_profit_atr": 2.5, "threshold": 3.0}` | 638.90 | 0.3 | -2.2 | 50.3 | 361.50 | 0.3 | -2.0 | 1.10 | 714/838 | not checked |
| 302 | `{"max_candles": 192, "stop_atr": 3.0, "take_profit_atr": 1.5, "threshold": 2.25}` | 625.71 | 0.3 | -2.1 | 75.7 | 366.73 | 0.3 | -2.2 | 1.14 | 728/832 | not checked |
| 231 | `{"max_candles": 156, "stop_atr": 1.5, "take_profit_atr": 2.0, "threshold": 3.0}` | 323.36 | 0.1 | -1.6 | 50.4 | 260.74 | 0.2 | -1.9 | 1.60 | 723/851 | not checked |
| 234 | `{"max_candles": 108, "stop_atr": 1.0, "take_profit_atr": 2.0, "threshold": 3.0}` | 272.03 | 0.1 | -1.1 | 41.5 | 237.46 | 0.2 | -1.4 | 1.69 | 734/859 | not checked |
| 377 | `{"max_candles": 60, "stop_atr": 1.0, "take_profit_atr": 2.0, "threshold": 3.0}` | 272.03 | 0.1 | -1.1 | 41.5 | 237.46 | 0.2 | -1.4 | 1.69 | 734/859 | not checked |

(1 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 935 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
