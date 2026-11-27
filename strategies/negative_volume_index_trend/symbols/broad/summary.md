# negative_volume_index_trend__broad: optimization summary

Updated 2026-11-25T06:00:01Z · backtest.py version `c28f56dfaf` · 1,119 parameter sets tested with this version (1,119 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, VNQ, VUG, VTV (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [negative_volume_index_trend__broad__max-income__v002.md](negative_volume_index_trend__broad__max-income__v002.md) | 1118 | `{"max_candles": 138, "n": 50, "stop_atr": 3.75, "take_profit_atr": 10.5}` | long XLF since 2026-11-24 00:00 @ 55.526651; long XLV since 2026-11-24 00:00 @ 179.703889; long SHY since 2026-11-23 00:00 @ 81.514445; long VIG since 2026-09-28 00:00 @ 235.920761; long VTV since 2026-11-24 00:00 @ 217.875341 |
| balanced | [negative_volume_index_trend__broad__balanced__v001.md](negative_volume_index_trend__broad__balanced__v001.md) | 1119 | `{"max_candles": 168, "n": 50, "stop_atr": 4.5, "take_profit_atr": 2.5}` | long RSP since 2026-11-10 00:00 @ 219.655873; long XLF since 2026-11-24 00:00 @ 55.526651; long XLV since 2026-11-24 00:00 @ 179.703889; long SHY since 2026-11-23 00:00 @ 81.514445; long VTV since 2026-11-24 00:00 @ 217.875341 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,943.60 | 2,435.22 | 399.07 | 407.32 |
| return % | 19.44 | 24.35 | 3.99 | 4.07 |
| return %/year | 1.1 | 2.0 | 0.2 | 0.4 |
| gross profit | 5,001.68 | 7,288.29 | 2,807.50 | 4,002.74 |
| gross loss | 3,058.08 | 4,853.07 | 2,408.44 | 3,595.42 |
| trades | 911 | 1,249 | 911 | 1,249 |
| win rate % | 39.4 | 39.5 | 47.1 | 48.4 |
| avg win | 13.93 | 14.75 | 6.54 | 6.62 |
| avg loss | -5.54 | -6.43 | -5.00 | -5.58 |
| avg result / trade | 2.13 | 1.95 | 0.44 | 0.33 |
| largest single loss | -35.48 | -74.44 | -31.30 | -59.86 |
| largest loss % of equity | -8.11 | -13.49 | -11.84 | -22.23 |
| max drawdown | -525.82 | -696.15 | -281.91 | -396.36 |
| max drawdown % | -4.69 | -5.81 | -2.64 | -3.74 |
| profit factor | 1.64 | 1.50 | 1.17 | 1.11 |
| unusually bad trades | 167 | 227 | 142 | 190 |
| … threshold (% of equity) | 2.5 | 2.5 | 2.1 | 2.3 |
| time in market % | 13.3 | 26.9 | 5.4 | 11.4 |
| buy & hold return % | 64.23 | 277.57 | 64.23 | 277.57 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.92 |  | 1.61 |
| period | 1999-01-07 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-01-07 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1999 | 0.3 | 0.1 |
| 2000 | -0.2 | 0.1 |
| 2001 | 0.0 | 0.0 |
| 2002 | -0.1 | -0.1 |
| 2003 | 0.5 | 0.1 |
| 2004 | 0.3 | 0.2 |
| 2005 | -0.4 | -0.2 |
| 2006 | 0.7 | 0.6 |
| 2007 | 2.0 | 1.4 |
| 2008 | -1.2 | -0.5 |
| 2009 | 6.4 | 2.5 |
| 2010 | 1.3 | 1.0 |
| 2011 | -0.1 | -0.4 |
| 2012 | 0.7 | 0.0 |
| 2013 | 7.6 | 0.8 |
| 2014 | 3.1 | 0.6 |
| 2015 | -2.5 | -2.2 |
| 2016 (OOS) | 2.4 | 1.0 |
| 2017 (OOS) | 4.1 | 0.2 |
| 2018 (OOS) | -1.8 | 0.1 |
| 2019 (OOS) | 7.7 | 3.0 |
| 2020 (OOS) | 2.2 | 0.1 |
| 2021 (OOS) | 4.6 | 1.4 |
| 2022 (OOS) | -4.4 | -1.5 |
| 2023 (OOS) | 5.0 | -1.6 |
| 2024 (OOS) | 1.0 | 1.0 |
| 2025 (OOS) | 2.8 | 0.6 |
| 2026 (OOS) | -2.2 | -0.3 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.7% from a peak in-sample and 5.8% out-of-sample, and the worst single trade cost 13.5% of the account out-of-sample. About 39 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 2.6% from a peak in-sample and 3.7% out-of-sample, and the worst single trade cost 22.2% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.
- balanced: `max_candles` = 168 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 631 | `{"max_candles": 144, "n": 50, "stop_atr": 3.75, "take_profit_atr": 10.0}` | 2,013.87 | 1.1 | -3.9 | 39.5 | 2,296.98 | 1.9 | -5.8 | 1.76 | 911/1249 | not checked |
| 496 | `{"max_candles": 120, "n": 50, "stop_atr": 3.75, "take_profit_atr": 10.0}` | 1,883.00 | 1.0 | -3.8 | 39.5 | 2,293.89 | 1.9 | -5.8 | 1.88 | 911/1249 | not checked |
| 691 | `{"max_candles": 120, "n": 50, "stop_atr": 3.75, "take_profit_atr": 9.5}` | 1,766.62 | 1.0 | -3.8 | 39.6 | 2,195.51 | 1.8 | -5.9 | 1.92 | 911/1249 | not checked |
| 623 | `{"max_candles": 144, "n": 50, "stop_atr": 3.75, "take_profit_atr": 9.0}` | 1,761.15 | 1.0 | -3.6 | 39.6 | 2,157.25 | 1.8 | -5.3 | 1.89 | 911/1249 | not checked |
| 606 | `{"max_candles": 138, "n": 50, "stop_atr": 3.75, "take_profit_atr": 9.0}` | 1,752.52 | 1.0 | -3.6 | 39.6 | 2,185.09 | 1.8 | -5.3 | 1.91 | 911/1249 | not checked |
| 742 | `{"max_candles": 126, "n": 50, "stop_atr": 3.75, "take_profit_atr": 9.0}` | 1,738.28 | 0.9 | -3.5 | 39.6 | 2,246.38 | 1.9 | -5.3 | 1.98 | 911/1249 | not checked |
| 696 | `{"max_candles": 156, "n": 50, "stop_atr": 3.75, "take_profit_atr": 8.0}` | 1,566.06 | 0.9 | -3.5 | 39.9 | 1,979.03 | 1.7 | -5.5 | 1.94 | 911/1249 | not checked |
| 826 | `{"max_candles": 162, "n": 50, "stop_atr": 3.75, "take_profit_atr": 8.0}` | 1,563.77 | 0.9 | -3.5 | 39.9 | 1,988.36 | 1.7 | -5.5 | 1.95 | 911/1249 | not checked |
| 805 | `{"max_candles": 138, "n": 50, "stop_atr": 3.75, "take_profit_atr": 8.0}` | 1,560.36 | 0.9 | -3.5 | 39.9 | 1,985.99 | 1.7 | -5.5 | 1.95 | 911/1249 | not checked |
| 598 | `{"max_candles": 126, "n": 60, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 1,470.75 | 0.8 | -3.4 | 39.0 | 2,415.30 | 2.0 | -4.5 | 2.48 | 772/1092 | not checked |
| 880 | `{"max_candles": 126, "n": 60, "stop_atr": 3.75, "take_profit_atr": 10.0}` | 1,415.56 | 0.8 | -3.4 | 39.0 | 2,324.54 | 1.9 | -4.5 | 2.49 | 772/1092 | not checked |
| 379 | `{"max_candles": 84, "n": 50, "stop_atr": 3.75, "take_profit_atr": 8.0}` | 1,397.91 | 0.8 | -3.2 | 39.9 | 1,668.33 | 1.4 | -5.3 | 1.86 | 911/1249 | not checked |
| 667 | `{"max_candles": 132, "n": 80, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 1,380.30 | 0.8 | -2.9 | 38.0 | 1,438.95 | 1.2 | -4.5 | 1.63 | 579/788 | not checked |
| 608 | `{"max_candles": 138, "n": 100, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 1,328.72 | 0.7 | -2.4 | 37.8 | 855.40 | 0.8 | -2.8 | 1.03 | 473/621 | not checked |
| 593 | `{"max_candles": 120, "n": 100, "stop_atr": 3.75, "take_profit_atr": 10.0}` | 1,184.84 | 0.7 | -2.2 | 37.8 | 872.25 | 0.8 | -3.1 | 1.17 | 473/621 | not checked |
| 366 | `{"max_candles": 84, "n": 100, "stop_atr": 3.0, "take_profit_atr": 8.5}` | 1,005.60 | 0.6 | -1.7 | 38.0 | 260.90 | 0.2 | -3.2 | 0.42 | 473/621 | not checked |
| 423 | `{"max_candles": 102, "n": 100, "stop_atr": 2.25, "take_profit_atr": 8.5}` | 978.90 | 0.6 | -1.5 | 35.5 | 449.53 | 0.4 | -3.6 | 0.73 | 473/621 | not checked |
| 404 | `{"max_candles": 78, "n": 100, "stop_atr": 2.25, "take_profit_atr": 8.5}` | 949.00 | 0.5 | -1.4 | 36.4 | 310.11 | 0.3 | -3.5 | 0.52 | 473/621 | not checked |
| 359 | `{"max_candles": 72, "n": 100, "stop_atr": 1.75, "take_profit_atr": 5.5}` | 510.44 | 0.3 | -1.2 | 34.9 | 130.83 | 0.1 | -2.6 | 0.41 | 473/621 | not checked |
| 285 | `{"max_candles": 96, "n": 170, "stop_atr": 2.0, "take_profit_atr": 7.5}` | 327.71 | 0.2 | -1.1 | 32.4 | 407.86 | 0.4 | -1.8 | 1.95 | 247/360 | not checked |
| 316 | `{"max_candles": 96, "n": 170, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 317.24 | 0.2 | -1.1 | 32.8 | 428.70 | 0.4 | -1.8 | 2.17 | 247/360 | not checked |
| 219 | `{"max_candles": 42, "n": 190, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 196.77 | 0.1 | -0.9 | 29.3 | 68.68 | 0.1 | -0.9 | 0.55 | 208/339 | not checked |
| 84 | `{"max_candles": 90, "n": 170, "stop_atr": 1.25, "take_profit_atr": 5.5}` | 131.78 | 0.1 | -0.8 | 29.6 | 186.44 | 0.2 | -1.4 | 2.12 | 247/360 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,119 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
