# cmf_accumulation_cross__broad: optimization summary

Updated 2026-11-25T15:59:55Z · backtest.py version `80c2a1fcaa` · 1,430 parameter sets tested with this version (1,430 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cmf_accumulation_cross__broad__max-income__v002.md](cmf_accumulation_cross__broad__max-income__v002.md) | 1429 | `{"level": 0.07, "max_bars": 48, "n": 42, "stop_atr": 4.5, "take_profit_atr": 7.0}` | long XLU since 2026-11-12 00:00 @ 43.943179; long TLT since 2026-11-24 00:00 @ 81.719508; long AGG since 2026-11-10 00:00 @ 96.018795; long BND since 2026-11-02 00:00 @ 71.411416; long SCHD since 2026-11-24 00:00 @ 34.38031; long USMV since 2026-11-24 00:00 @ 99.879953; long SQQQ since 2026-11-20 00:00 @ 50.945279 |
| balanced | [cmf_accumulation_cross__broad__balanced__v002.md](cmf_accumulation_cross__broad__balanced__v002.md) | 1430 | `{"level": 0.07, "max_bars": 48, "n": 42, "stop_atr": 4.75, "take_profit_atr": 7.5}` | long XLU since 2026-11-12 00:00 @ 43.943179; long TLT since 2026-11-24 00:00 @ 81.719508; long AGG since 2026-11-10 00:00 @ 96.018795; long BND since 2026-11-02 00:00 @ 71.411416; long SCHD since 2026-11-24 00:00 @ 34.38031; long USMV since 2026-11-24 00:00 @ 99.879953; long SQQQ since 2026-11-20 00:00 @ 50.945279 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,107.93 | 3,359.42 | 3,238.22 | 3,312.85 |
| return % | 31.08 | 33.59 | 32.38 | 33.13 |
| return %/year | 1.3 | 2.7 | 1.4 | 2.7 |
| gross profit | 8,699.84 | 10,464.38 | 8,687.52 | 10,303.21 |
| gross loss | 5,591.91 | 7,104.96 | 5,449.30 | 6,990.36 |
| trades | 1,603 | 1,636 | 1,585 | 1,623 |
| win rate % | 50.2 | 52.1 | 50.7 | 52.6 |
| avg win | 10.81 | 12.27 | 10.81 | 12.08 |
| avg loss | -7.01 | -9.07 | -6.98 | -9.08 |
| avg result / trade | 1.94 | 2.05 | 2.04 | 2.04 |
| largest single loss | -41.16 | -194.62 | -40.30 | -151.15 |
| largest loss % of equity | -17.16 | -18.31 | -18.11 | -21.04 |
| max drawdown | -662.91 | -1,246.82 | -642.28 | -1,227.50 |
| max drawdown % | -5.34 | -9.67 | -5.16 | -9.50 |
| profit factor | 1.56 | 1.47 | 1.59 | 1.47 |
| unusually bad trades | 180 | 139 | 180 | 154 |
| … threshold (% of equity) | 5.1 | 6.0 | 5.0 | 6.0 |
| time in market % | 14.9 | 29.0 | 15.2 | 29.9 |
| buy & hold return % | 106.57 | 303.57 | 106.57 | 303.57 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.08 |  | 1.97 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.1 | 0.1 |
| 1996 | 0.3 | 0.3 |
| 1997 | 0.3 | 0.4 |
| 1998 | 0.0 | 0.0 |
| 1999 | 0.6 | 0.6 |
| 2000 | -0.1 | -0.1 |
| 2001 | -1.9 | -1.9 |
| 2002 | -1.3 | -1.3 |
| 2003 | 2.8 | 2.8 |
| 2004 | 0.8 | 0.8 |
| 2005 | 1.2 | 1.2 |
| 2006 | 2.3 | 2.5 |
| 2007 | 0.7 | 0.6 |
| 2008 | -0.6 | -0.7 |
| 2009 | 10.4 | 10.1 |
| 2010 | 3.8 | 4.7 |
| 2011 | -2.0 | -2.0 |
| 2012 | 3.6 | 3.7 |
| 2013 | 6.2 | 6.6 |
| 2014 | 2.2 | 2.3 |
| 2015 | -1.4 | -1.5 |
| 2016 (OOS) | 2.5 | 2.3 |
| 2017 (OOS) | 7.6 | 7.6 |
| 2018 (OOS) | -0.1 | -0.2 |
| 2019 (OOS) | 5.0 | 4.8 |
| 2020 (OOS) | 5.3 | 5.4 |
| 2021 (OOS) | 5.6 | 6.3 |
| 2022 (OOS) | -8.2 | -8.2 |
| 2023 (OOS) | 8.4 | 8.7 |
| 2024 (OOS) | 6.8 | 4.2 |
| 2025 (OOS) | 1.0 | 1.1 |
| 2026 (OOS) | 0.6 | 1.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.3% from a peak in-sample and 9.7% out-of-sample, and the worst single trade cost 18.3% of the account out-of-sample. About 50 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 5.2% from a peak in-sample and 9.5% out-of-sample, and the worst single trade cost 21.0% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 978 | `{"level": 0.07, "max_bars": 48, "n": 42, "stop_atr": 5.5, "take_profit_atr": 7.5}` | 3,255.84 | 1.4 | -5.3 | 51.5 | 3,316.26 | 2.7 | -9.9 | 1.98 | 1580/1608 | not checked |
| 1244 | `{"level": 0.07, "max_bars": 48, "n": 42, "stop_atr": 5.25, "take_profit_atr": 7.5}` | 3,243.63 | 1.4 | -5.3 | 51.3 | 3,225.12 | 2.6 | -9.9 | 1.93 | 1581/1613 | not checked |
| 915 | `{"level": 0.07, "max_bars": 48, "n": 42, "stop_atr": 4.75, "take_profit_atr": 7.5}` | 3,238.22 | 1.4 | -5.2 | 50.7 | 3,312.85 | 2.7 | -9.5 | 1.97 | 1585/1623 | 1.00 |
| 925 | `{"level": 0.07, "max_bars": 48, "n": 42, "stop_atr": 4.75, "take_profit_atr": 8.0}` | 3,216.77 | 1.3 | -5.1 | 50.7 | 3,528.65 | 2.8 | -9.4 | 2.10 | 1580/1619 | not checked |
| 1009 | `{"level": 0.04, "max_bars": 48, "n": 42, "stop_atr": 5.0, "take_profit_atr": 7.5}` | 3,082.98 | 1.3 | -5.1 | 49.0 | 3,158.35 | 2.5 | -7.3 | 1.98 | 1749/1742 | not checked |
| 1329 | `{"level": 0.07, "max_bars": 42, "n": 42, "stop_atr": 5.25, "take_profit_atr": 8.0}` | 3,035.38 | 1.3 | -4.9 | 51.0 | 2,949.89 | 2.4 | -9.7 | 1.89 | 1613/1659 | not checked |
| 1030 | `{"level": 0.07, "max_bars": 42, "n": 42, "stop_atr": 4.75, "take_profit_atr": 8.0}` | 3,027.09 | 1.3 | -4.9 | 50.5 | 2,988.35 | 2.4 | -9.3 | 1.91 | 1617/1667 | not checked |
| 1189 | `{"level": 0.07, "max_bars": 42, "n": 42, "stop_atr": 5.0, "take_profit_atr": 8.0}` | 3,012.99 | 1.3 | -4.9 | 50.7 | 2,954.77 | 2.4 | -9.5 | 1.91 | 1616/1662 | not checked |
| 1163 | `{"level": 0.04, "max_bars": 48, "n": 42, "stop_atr": 4.0, "take_profit_atr": 7.5}` | 2,766.51 | 1.2 | -4.7 | 47.7 | 2,985.14 | 2.4 | -7.9 | 2.08 | 1762/1759 | not checked |
| 582 | `{"level": 0.04, "max_bars": 48, "n": 42, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 2,618.14 | 1.1 | -4.7 | 47.8 | 2,839.04 | 2.3 | -8.0 | 2.09 | 1763/1764 | not checked |
| 676 | `{"level": 0.04, "max_bars": 48, "n": 42, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 2,488.79 | 1.1 | -4.7 | 47.8 | 2,691.25 | 2.2 | -8.0 | 2.08 | 1770/1765 | not checked |
| 561 | `{"level": 0.04, "max_bars": 48, "n": 44, "stop_atr": 4.5, "take_profit_atr": 7.0}` | 2,427.20 | 1.0 | -4.6 | 48.9 | 3,059.32 | 2.5 | -6.8 | 2.38 | 1727/1719 | not checked |
| 593 | `{"level": 0.04, "max_bars": 54, "n": 42, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 2,259.37 | 1.0 | -4.6 | 47.1 | 3,229.02 | 2.6 | -8.1 | 2.65 | 1741/1738 | not checked |
| 646 | `{"level": 0.04, "max_bars": 54, "n": 42, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 2,216.51 | 1.0 | -4.5 | 47.1 | 2,958.43 | 2.4 | -8.2 | 2.51 | 1748/1740 | not checked |
| 504 | `{"level": 0.04, "max_bars": 30, "n": 42, "stop_atr": 4.5, "take_profit_atr": 7.0}` | 1,746.88 | 0.8 | -4.3 | 48.4 | 1,818.99 | 1.6 | -5.9 | 2.01 | 1833/1833 | not checked |
| 955 | `{"level": 0.04, "max_bars": 30, "n": 44, "stop_atr": 5.5, "take_profit_atr": 7.0}` | 1,622.16 | 0.7 | -4.2 | 50.6 | 1,733.63 | 1.5 | -6.4 | 2.06 | 1777/1780 | not checked |
| 578 | `{"level": 0.04, "max_bars": 24, "n": 42, "stop_atr": 4.5, "take_profit_atr": 7.0}` | 1,225.16 | 0.6 | -4.2 | 48.7 | 1,447.17 | 1.2 | -5.5 | 2.27 | 1874/1877 | not checked |
| 529 | `{"level": 0.06, "max_bars": 60, "n": 46, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 688.40 | 0.3 | -4.1 | 56.8 | 842.58 | 0.8 | -8.0 | 2.34 | 1755/1844 | not checked |
| 996 | `{"level": 0.25, "max_bars": 48, "n": 48, "stop_atr": 4.25, "take_profit_atr": 5.0}` | 491.79 | 0.2 | -3.5 | 57.5 | 897.61 | 0.8 | -3.0 | 3.44 | 551/468 | not checked |
| 1276 | `{"level": 0.01, "max_bars": 66, "n": 40, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 360.29 | 0.2 | -3.0 | 47.3 | 422.53 | 0.4 | -3.3 | 2.23 | 2414/2440 | not checked |
| 199 | `{"level": 0.25, "max_bars": 54, "n": 38, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 228.95 | 0.1 | -2.7 | 61.3 | 143.98 | 0.1 | -4.7 | 1.18 | 982/934 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,430 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
