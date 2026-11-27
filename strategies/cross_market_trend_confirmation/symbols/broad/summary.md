# cross_market_trend_confirmation__broad: optimization summary

Updated 2026-11-25T14:02:46Z · backtest.py version `951e834614` · 844 parameter sets tested with this version (844 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cross_market_trend_confirmation__broad__max-income__v002.md](cross_market_trend_confirmation__broad__max-income__v002.md) | 844 | `{"max_bars": 60, "n": 44, "stop_atr": 0.75, "take_profit_atr": 9.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 1,545.56 | 1,358.76 |
| return % | 15.46 | 13.59 |
| return %/year | 0.7 | 1.2 |
| gross profit | 5,244.05 | 5,793.93 |
| gross loss | 3,698.49 | 4,435.17 |
| trades | 2,194 | 2,748 |
| win rate % | 25.6 | 27.7 |
| avg win | 9.35 | 7.62 |
| avg loss | -2.26 | -2.23 |
| avg result / trade | 0.70 | 0.49 |
| largest single loss | -12.57 | -33.98 |
| largest loss % of equity | -5.60 | -8.28 |
| max drawdown | -730.48 | -470.55 |
| max drawdown % | -5.95 | -4.28 |
| profit factor | 1.42 | 1.31 |
| unusually bad trades | 165 | 199 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 6.8 | 16.9 |
| buy & hold return % | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.71 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 1995 | 0.0 |
| 1996 | 0.0 |
| 1997 | 0.0 |
| 1998 | 0.0 |
| 1999 | 0.0 |
| 2000 | 0.0 |
| 2001 | 0.1 |
| 2002 | -0.9 |
| 2003 | 1.2 |
| 2004 | 0.4 |
| 2005 | 0.8 |
| 2006 | -0.1 |
| 2007 | -0.3 |
| 2008 | -0.7 |
| 2009 | 12.2 |
| 2010 | 2.9 |
| 2011 | -1.0 |
| 2012 | 0.6 |
| 2013 | 4.7 |
| 2014 | -0.0 |
| 2015 | -4.5 |
| 2016 (OOS) | -0.8 |
| 2017 (OOS) | 4.1 |
| 2018 (OOS) | -2.1 |
| 2019 (OOS) | 2.2 |
| 2020 (OOS) | 4.6 |
| 2021 (OOS) | -0.8 |
| 2022 (OOS) | -2.1 |
| 2023 (OOS) | 2.5 |
| 2024 (OOS) | 0.2 |
| 2025 (OOS) | 0.0 |
| 2026 (OOS) | 4.7 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 6.0% from a peak in-sample and 4.3% out-of-sample, and the worst single trade cost 8.3% of the account out-of-sample. About 26 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 433 | `{"max_bars": 54, "n": 44, "stop_atr": 0.75, "take_profit_atr": 10.0}` | 1,601.55 | 0.7 | -6.0 | 25.6 | 1,318.04 | 1.1 | -4.1 | 1.61 | 2194/2748 | not checked |
| 362 | `{"max_bars": 60, "n": 44, "stop_atr": 0.75, "take_profit_atr": 9.5}` | 1,545.56 | 0.7 | -6.0 | 25.6 | 1,358.76 | 1.2 | -4.3 | 1.71 | 2194/2748 | 1.00 |
| 359 | `{"max_bars": 60, "n": 44, "stop_atr": 0.75, "take_profit_atr": 10.0}` | 1,535.25 | 0.7 | -5.9 | 25.6 | 1,455.02 | 1.3 | -4.3 | 1.85 | 2194/2748 | not checked |
| 515 | `{"max_bars": 54, "n": 44, "stop_atr": 0.75, "take_profit_atr": 8.5}` | 1,496.07 | 0.7 | -5.9 | 25.6 | 1,174.70 | 1.0 | -4.1 | 1.54 | 2194/2748 | not checked |
| 487 | `{"max_bars": 60, "n": 44, "stop_atr": 0.75, "take_profit_atr": 8.5}` | 1,431.85 | 0.6 | -5.8 | 25.6 | 1,208.66 | 1.1 | -4.2 | 1.64 | 2194/2748 | not checked |
| 436 | `{"max_bars": 72, "n": 44, "stop_atr": 0.75, "take_profit_atr": 8.5}` | 1,365.25 | 0.6 | -5.8 | 25.6 | 1,195.50 | 1.0 | -4.2 | 1.71 | 2194/2748 | not checked |
| 440 | `{"max_bars": 54, "n": 44, "stop_atr": 0.5, "take_profit_atr": 10.0}` | 1,362.02 | 0.6 | -5.0 | 20.0 | 1,183.66 | 1.0 | -4.0 | 1.69 | 2194/2748 | not checked |
| 564 | `{"max_bars": 54, "n": 46, "stop_atr": 0.5, "take_profit_atr": 9.5}` | 1,308.82 | 0.6 | -5.0 | 20.2 | 1,400.14 | 1.2 | -4.4 | 2.05 | 2112/2649 | not checked |
| 452 | `{"max_bars": 60, "n": 46, "stop_atr": 0.5, "take_profit_atr": 10.0}` | 1,278.86 | 0.6 | -4.9 | 20.2 | 1,663.48 | 1.4 | -4.8 | 2.49 | 2112/2649 | not checked |
| 539 | `{"max_bars": 54, "n": 46, "stop_atr": 0.5, "take_profit_atr": 8.5}` | 1,237.18 | 0.6 | -4.9 | 20.2 | 1,270.29 | 1.1 | -4.3 | 1.96 | 2112/2649 | not checked |
| 579 | `{"max_bars": 54, "n": 48, "stop_atr": 0.5, "take_profit_atr": 9.0}` | 1,218.55 | 0.6 | -4.8 | 19.9 | 1,355.41 | 1.2 | -4.2 | 2.13 | 2058/2586 | not checked |
| 692 | `{"max_bars": 60, "n": 48, "stop_atr": 0.5, "take_profit_atr": 9.0}` | 1,165.75 | 0.5 | -4.8 | 19.9 | 1,434.60 | 1.2 | -4.3 | 2.34 | 2058/2586 | not checked |
| 473 | `{"max_bars": 72, "n": 46, "stop_atr": 0.5, "take_profit_atr": 8.5}` | 1,133.13 | 0.5 | -4.7 | 20.2 | 1,257.81 | 1.1 | -4.4 | 2.14 | 2112/2649 | not checked |
| 612 | `{"max_bars": 78, "n": 46, "stop_atr": 0.5, "take_profit_atr": 8.5}` | 1,104.43 | 0.5 | -4.7 | 20.2 | 1,267.48 | 1.1 | -4.4 | 2.20 | 2112/2649 | not checked |
| 336 | `{"max_bars": 72, "n": 50, "stop_atr": 0.5, "take_profit_atr": 8.5}` | 1,021.71 | 0.5 | -4.6 | 19.3 | 1,589.44 | 1.4 | -3.9 | 2.96 | 1989/2524 | not checked |
| 337 | `{"max_bars": 36, "n": 50, "stop_atr": 0.5, "take_profit_atr": 8.0}` | 705.29 | 0.3 | -4.3 | 19.3 | 1,161.43 | 1.0 | -3.2 | 3.06 | 1989/2524 | not checked |
| 632 | `{"max_bars": 54, "n": 46, "stop_atr": 0.25, "take_profit_atr": 9.5}` | 552.01 | 0.3 | -3.4 | 11.2 | 584.26 | 0.5 | -3.0 | 2.00 | 2112/2649 | not checked |
| 709 | `{"max_bars": 54, "n": 46, "stop_atr": 0.25, "take_profit_atr": 8.5}` | 548.02 | 0.2 | -3.2 | 11.2 | 530.51 | 0.5 | -3.0 | 1.92 | 2112/2649 | not checked |
| 660 | `{"max_bars": 54, "n": 48, "stop_atr": 0.25, "take_profit_atr": 9.5}` | 547.31 | 0.2 | -3.1 | 10.8 | 659.68 | 0.6 | -2.9 | 2.36 | 2058/2586 | not checked |
| 732 | `{"max_bars": 54, "n": 48, "stop_atr": 0.25, "take_profit_atr": 8.5}` | 541.61 | 0.2 | -3.0 | 10.8 | 605.07 | 0.5 | -2.9 | 2.16 | 2058/2586 | not checked |
| 391 | `{"max_bars": 60, "n": 48, "stop_atr": 0.25, "take_profit_atr": 8.5}` | 499.26 | 0.2 | -3.0 | 10.8 | 645.51 | 0.6 | -3.0 | 2.52 | 2058/2586 | not checked |
| 739 | `{"max_bars": 60, "n": 50, "stop_atr": 0.25, "take_profit_atr": 8.5}` | 443.15 | 0.2 | -2.9 | 10.9 | 863.84 | 0.8 | -2.7 | 3.62 | 1989/2524 | not checked |
| 375 | `{"max_bars": 36, "n": 50, "stop_atr": 0.25, "take_profit_atr": 8.0}` | 238.05 | 0.1 | -2.9 | 10.9 | 567.64 | 0.5 | -2.4 | 4.64 | 1989/2524 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 844 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
