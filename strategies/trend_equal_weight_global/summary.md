# trend_equal_weight_global: optimization summary

Updated 2026-11-27T11:51:28Z · backtest.py version `edd6a64054` · 683 parameter sets tested with this version (683 rows in results.csv in total) · last run ended: converged: no profile improved in the last 510 iterations at the smallest step size

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [trend_equal_weight_global__max-income__v001.md](trend_equal_weight_global__max-income__v001.md) | 172 | `{"max_candles": 231, "n": 150, "stop_loss_pct": 24}` | long DBC since 2026-07-01 00:00 @ 30.206304; long SPY since 2026-05-01 00:00 @ 746.750135 |
| balanced | [trend_equal_weight_global__balanced__v001.md](trend_equal_weight_global__balanced__v001.md) | 173 | `{"max_candles": 294, "n": 180, "stop_loss_pct": 15.0}` | long DBC since 2026-10-01 00:00 @ 32.37971; long EFA since 2026-05-01 00:00 @ 101.598909; long SPY since 2026-05-01 00:00 @ 729.868211; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 18,478.81 | 12,684.32 | 17,283.36 | 10,699.84 |
| return % | 184.79 | 126.84 | 172.83 | 107.00 |
| return %/year | 9.1 | 7.8 | 8.7 | 6.9 |
| gross profit | 33,460.79 | 21,015.32 | 31,029.03 | 19,345.46 |
| gross loss | 14,981.97 | 8,331.00 | 13,745.67 | 8,645.62 |
| trades | 118 | 120 | 101 | 104 |
| win rate % | 48.3 | 45.0 | 45.5 | 46.1 |
| avg win | 587.03 | 389.17 | 674.54 | 403.03 |
| avg loss | -245.61 | -126.23 | -249.92 | -154.39 |
| avg result / trade | 156.60 | 105.70 | 171.12 | 102.88 |
| largest single loss | -1,206.86 | -605.82 | -945.17 | -631.00 |
| largest loss % of equity | -4.41 | -4.95 | -3.48 | -5.03 |
| max drawdown | -4,638.13 | -4,642.99 | -3,353.51 | -5,398.94 |
| max drawdown % | -15.72 | -22.07 | -17.08 | -26.25 |
| profit factor | 2.23 | 2.52 | 2.26 | 2.24 |
| unusually bad trades | 8 | 2 | 9 | 7 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 61.5 | 63.7 | 63.5 | 64.6 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.86 |  | 0.79 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 8.5 | 8.7 |
| 2005 | 13.2 | 14.3 |
| 2006 | 20.4 | 17.9 |
| 2007 | 12.2 | 15.2 |
| 2008 | 12.5 | 9.1 |
| 2009 | 19.4 | 18.5 |
| 2010 | 12.6 | 10.9 |
| 2011 | 9.8 | 3.3 |
| 2012 | 1.1 | 1.7 |
| 2013 | 11.2 | 7.4 |
| 2014 | 2.7 | 5.3 |
| 2015 | -10.4 | -5.1 |
| 2016 (OOS) | 12.4 | 9.0 |
| 2017 (OOS) | 14.7 | 14.3 |
| 2018 (OOS) | -7.3 | -5.8 |
| 2019 (OOS) | 10.6 | 11.1 |
| 2020 (OOS) | 19.6 | 19.1 |
| 2021 (OOS) | 19.0 | 21.0 |
| 2022 (OOS) | -11.6 | -18.0 |
| 2023 (OOS) | 6.3 | 6.7 |
| 2024 (OOS) | 3.7 | 6.1 |
| 2025 (OOS) | 21.9 | 20.4 |
| 2026 (OOS) | 2.0 | -0.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 15.7% from a peak in-sample and 22.1% out-of-sample, and the worst single trade cost 5.0% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 45% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 17.1% from a peak in-sample and 26.2% out-of-sample, and the worst single trade cost 5.0% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 563 | `{"max_candles": 378, "n": 150, "stop_loss_pct": 16}` | 19,043.00 | 9.3 | -14.8 | 49.5 | 12,910.48 | 7.9 | -22.1 | 0.85 | 103/105 | not checked |
| 351 | `{"max_candles": 336, "n": 150, "stop_loss_pct": 16}` | 18,736.67 | 9.2 | -14.1 | 50.0 | 13,375.29 | 8.1 | -22.1 | 0.88 | 106/106 | not checked |
| 278 | `{"max_candles": 168, "n": 150, "stop_loss_pct": 24}` | 17,391.97 | 8.8 | -13.9 | 49.6 | 11,297.77 | 7.2 | -21.9 | 0.82 | 139/136 | not checked |
| 285 | `{"max_candles": 168, "n": 150, "stop_loss_pct": 23}` | 17,391.97 | 8.8 | -13.9 | 49.6 | 11,297.77 | 7.2 | -21.9 | 0.82 | 139/136 | not checked |
| 325 | `{"max_candles": 168, "n": 150, "stop_loss_pct": 22}` | 17,391.97 | 8.8 | -13.9 | 49.6 | 11,297.77 | 7.2 | -21.9 | 0.82 | 139/136 | not checked |
| 332 | `{"max_candles": 168, "n": 150, "stop_loss_pct": 25}` | 17,391.97 | 8.8 | -13.9 | 49.6 | 11,297.77 | 7.2 | -21.9 | 0.82 | 139/136 | not checked |
| 367 | `{"max_candles": 168, "n": 150, "stop_loss_pct": 21}` | 17,391.97 | 8.8 | -13.9 | 49.6 | 11,297.77 | 7.2 | -21.9 | 0.82 | 139/136 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 683 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
