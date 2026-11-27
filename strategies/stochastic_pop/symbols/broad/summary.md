# stochastic_pop__broad: optimization summary

Updated 2026-11-25T07:46:05Z · backtest.py version `e9a1993ec3` · 790 parameter sets tested with this version (790 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [stochastic_pop__broad__max-income__v002.md](stochastic_pop__broad__max-income__v002.md) | 789 | `{"level": 72, "max_candles": 24, "stop_atr": 4.25, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [stochastic_pop__broad__balanced__v002.md](stochastic_pop__broad__balanced__v002.md) | 790 | `{"level": 72, "max_candles": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 129.07 | 604.23 | 82.56 | 400.67 |
| return % | 1.29 | 6.04 | 0.83 | 4.01 |
| return %/year | 0.1 | 0.5 | 0.1 | 0.4 |
| gross profit | 3,900.23 | 4,610.40 | 3,872.36 | 4,325.43 |
| gross loss | 3,771.16 | 4,006.17 | 3,789.80 | 3,924.77 |
| trades | 1,633 | 1,667 | 1,658 | 1,695 |
| win rate % | 44.0 | 46.0 | 46.3 | 48.0 |
| avg win | 5.42 | 6.02 | 5.05 | 5.31 |
| avg loss | -4.13 | -4.45 | -4.25 | -4.45 |
| avg result / trade | 0.08 | 0.36 | 0.05 | 0.24 |
| largest single loss | -31.39 | -45.17 | -34.45 | -43.90 |
| largest loss % of equity | -16.70 | -31.93 | -16.70 | -31.93 |
| max drawdown | -353.62 | -346.80 | -353.38 | -350.18 |
| max drawdown % | -3.37 | -3.42 | -3.39 | -3.43 |
| profit factor | 1.03 | 1.15 | 1.02 | 1.10 |
| unusually bad trades | 160 | 200 | 147 | 200 |
| … threshold (% of equity) | 3.5 | 3.2 | 3.6 | 3.2 |
| time in market % | 8.0 | 11.4 | 7.2 | 10.3 |
| buy & hold return % | 89.54 | 303.60 | 89.54 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 6.75 |  | 7.20 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 0.2 | -0.1 |
| 2001 | -0.4 | -0.3 |
| 2002 | -0.5 | -0.4 |
| 2003 | 1.1 | 0.9 |
| 2004 | 0.3 | 0.2 |
| 2005 | -2.2 | -1.6 |
| 2006 | 1.1 | 1.0 |
| 2007 | 0.5 | 0.1 |
| 2008 | -0.9 | -1.0 |
| 2009 | 0.6 | 1.2 |
| 2010 | 2.2 | 1.6 |
| 2011 | -0.8 | -0.6 |
| 2012 | -0.1 | -0.2 |
| 2013 | 1.7 | 1.3 |
| 2014 | 1.3 | 1.3 |
| 2015 | -2.6 | -2.6 |
| 2016 (OOS) | -0.0 | 0.0 |
| 2017 (OOS) | 0.7 | 0.8 |
| 2018 (OOS) | -2.7 | -2.8 |
| 2019 (OOS) | 2.5 | 2.3 |
| 2020 (OOS) | -0.2 | 0.1 |
| 2021 (OOS) | 2.4 | 2.2 |
| 2022 (OOS) | -1.4 | -1.6 |
| 2023 (OOS) | 0.9 | 0.5 |
| 2024 (OOS) | 1.6 | 1.1 |
| 2025 (OOS) | 0.4 | 0.4 |
| 2026 (OOS) | 2.0 | 1.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 3.4% from a peak in-sample and 3.4% out-of-sample, and the worst single trade cost 31.9% of the account out-of-sample. About 44 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.4% from a peak in-sample and 3.4% out-of-sample, and the worst single trade cost 31.9% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 754 | `{"level": 72, "max_candles": 24, "stop_atr": 4.25, "take_profit_atr": 3.0}` | 129.07 | 0.1 | -3.4 | 44.0 | 604.23 | 0.5 | -3.4 | 6.75 | 1633/1667 | 0.75 |
| 308 | `{"level": 72, "max_candles": 156, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 309 | `{"level": 72, "max_candles": 180, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 310 | `{"level": 72, "max_candles": 168, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | 0.88 |
| 340 | `{"level": 72, "max_candles": 144, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 401 | `{"level": 72, "max_candles": 192, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 403 | `{"level": 72, "max_candles": 132, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 476 | `{"level": 72, "max_candles": 120, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 521 | `{"level": 72, "max_candles": 108, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 578 | `{"level": 72, "max_candles": 96, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 648 | `{"level": 72, "max_candles": 84, "stop_atr": 1.75, "take_profit_atr": 3.0}` | 120.02 | 0.1 | -3.3 | 41.6 | 233.36 | 0.2 | -3.9 | 3.00 | 1669/1705 | not checked |
| 306 | `{"level": 72, "max_candles": 168, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 317 | `{"level": 72, "max_candles": 180, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 321 | `{"level": 72, "max_candles": 192, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 336 | `{"level": 72, "max_candles": 156, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 512 | `{"level": 72, "max_candles": 144, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 520 | `{"level": 72, "max_candles": 120, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 545 | `{"level": 72, "max_candles": 132, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 593 | `{"level": 72, "max_candles": 108, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 612 | `{"level": 72, "max_candles": 96, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 80.09 | 0.1 | -3.1 | 43.8 | 70.64 | 0.1 | -3.8 | 1.20 | 1697/1734 | not checked |
| 326 | `{"level": 70, "max_candles": 180, "stop_atr": 1.5, "take_profit_atr": 3.0}` | 58.17 | 0.0 | -3.0 | 39.1 | 36.64 | 0.0 | -4.6 | 0.75 | 1668/1692 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 790 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
