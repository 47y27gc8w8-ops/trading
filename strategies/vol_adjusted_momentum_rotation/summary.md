# vol_adjusted_momentum_rotation: optimization summary

Updated 2026-11-27T11:46:49Z · backtest.py version `f0b0a8922e` · 786 parameter sets tested with this version (786 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [vol_adjusted_momentum_rotation__max-income__v001.md](vol_adjusted_momentum_rotation__max-income__v001.md) | 285 | `{"k": 3, "max_candles": 378, "n": 63, "stop_loss_pct": 22}` | long DBC since 2026-09-01 00:00 @ 31.95853; long TLT since 2026-11-02 00:00 @ 81.854551 |
| balanced | [vol_adjusted_momentum_rotation__balanced__v001.md](vol_adjusted_momentum_rotation__balanced__v001.md) | 286 | `{"k": 4, "max_candles": 168, "n": 252, "stop_loss_pct": 24}` | long DBC since 2026-04-01 00:00 @ 28.623851; long EFA since 2026-10-01 00:00 @ 103.411011; long SPY since 2026-05-01 00:00 @ 719.344233; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 25,648.87 | 13,754.89 | 21,891.22 | 7,413.83 |
| return % | 256.49 | 137.55 | 218.91 | 74.14 |
| return %/year | 11.2 | 8.3 | 10.2 | 5.2 |
| gross profit | 49,424.35 | 26,280.30 | 31,680.01 | 15,310.53 |
| gross loss | 23,775.49 | 12,525.40 | 9,788.79 | 7,896.70 |
| trades | 129 | 127 | 103 | 90 |
| win rate % | 58.9 | 53.5 | 64.1 | 53.3 |
| avg win | 650.32 | 386.47 | 480.00 | 318.97 |
| avg loss | -448.59 | -212.29 | -264.56 | -188.02 |
| avg result / trade | 198.83 | 108.31 | 212.54 | 82.38 |
| largest single loss | -3,293.62 | -1,100.90 | -1,184.66 | -813.89 |
| largest loss % of equity | -7.99 | -4.18 | -6.42 | -6.11 |
| max drawdown | -9,531.64 | -5,195.72 | -2,602.56 | -3,334.11 |
| max drawdown % | -25.81 | -23.71 | -16.36 | -26.97 |
| profit factor | 2.08 | 2.10 | 3.24 | 1.94 |
| unusually bad trades | 11 | 11 | 5 | 8 |
| … threshold (% of equity) | 2.5 | 2.0 | 2.0 | 2.2 |
| time in market % | 35.2 | 33.8 | 45.2 | 43.1 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.74 |  | 0.52 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 4.3 | 8.7 |
| 2005 | 10.0 | 11.0 |
| 2006 | 25.1 | 20.6 |
| 2007 | 6.7 | 14.0 |
| 2008 | 4.8 | 19.6 |
| 2009 | 34.5 | 2.8 |
| 2010 | 26.3 | 8.4 |
| 2011 | 26.2 | 4.7 |
| 2012 | -0.9 | 10.5 |
| 2013 | 17.2 | 12.9 |
| 2014 | 5.0 | 11.2 |
| 2015 | -15.0 | -0.6 |
| 2016 (OOS) | -5.4 | -6.5 |
| 2017 (OOS) | 18.3 | 16.4 |
| 2018 (OOS) | 1.2 | -17.8 |
| 2019 (OOS) | 9.3 | 11.8 |
| 2020 (OOS) | 23.5 | 12.4 |
| 2021 (OOS) | 19.0 | 13.4 |
| 2022 (OOS) | -11.5 | -12.9 |
| 2023 (OOS) | 6.3 | 1.6 |
| 2024 (OOS) | 5.2 | 7.8 |
| 2025 (OOS) | 21.0 | 26.5 |
| 2026 (OOS) | 4.0 | 10.5 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 25.8% from a peak in-sample and 23.7% out-of-sample, and the worst single trade cost 4.2% of the account out-of-sample. About 59 of every 100 trades won in-sample. With 100% of equity per trade; about 39% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 16.4% from a peak in-sample and 27.0% out-of-sample, and the worst single trade cost 6.1% of the account out-of-sample. About 64 of every 100 trades won in-sample. Out-of-sample it earned 5.2% a year against 10.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 37% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 394 | `{"k": 3, "max_candles": 420, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 436 | `{"k": 3, "max_candles": 399, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 513 | `{"k": 3, "max_candles": 441, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 516 | `{"k": 3, "max_candles": 462, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 575 | `{"k": 3, "max_candles": 378, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 609 | `{"k": 3, "max_candles": 483, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 633 | `{"k": 3, "max_candles": 357, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 664 | `{"k": 3, "max_candles": 504, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 668 | `{"k": 3, "max_candles": 336, "n": 63, "stop_loss_pct": 14}` | 26,898.85 | 11.5 | -23.2 | 58.9 | 13,754.89 | 8.3 | -23.7 | 0.72 | 129/127 | not checked |
| 556 | `{"k": 4, "max_candles": 126, "n": 252, "stop_loss_pct": 22}` | 24,474.25 | 10.9 | -13.8 | 66.4 | 4,565.50 | 3.5 | -28.3 | 0.32 | 119/102 | not checked |
| 534 | `{"k": 4, "max_candles": 189, "n": 252, "stop_loss_pct": 20}` | 22,423.44 | 10.3 | -13.0 | 66.7 | 7,722.98 | 5.4 | -24.8 | 0.52 | 99/85 | not checked |
| 465 | `{"k": 5, "max_candles": 189, "n": 252, "stop_loss_pct": 21}` | 19,879.72 | 9.6 | -12.8 | 69.4 | 7,671.70 | 5.4 | -23.9 | 0.56 | 108/94 | not checked |
| 353 | `{"k": 5, "max_candles": 168, "n": 273, "stop_loss_pct": 22}` | 18,528.61 | 9.1 | -12.0 | 62.5 | 7,730.24 | 5.4 | -25.1 | 0.59 | 112/97 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 786 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
