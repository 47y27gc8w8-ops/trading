# multi_horizon_rank_rotation: optimization summary

Updated 2026-11-27T12:00:30Z · backtest.py version `01c28d73a1` · 2,086 parameter sets tested with this version (2,086 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [multi_horizon_rank_rotation__max-income__v001.md](multi_horizon_rank_rotation__max-income__v001.md) | 2085 | `{"k": 3, "max_candles": 231, "stop_loss_pct": 15.0}` | long DBC since 2026-08-03 00:00 @ 29.358805; long EFA since 2026-11-02 00:00 @ 103.721109; long SPY since 2026-09-01 00:00 @ 760.350514 |
| balanced | [multi_horizon_rank_rotation__balanced__v001.md](multi_horizon_rank_rotation__balanced__v001.md) | 2086 | `{"k": 5, "max_candles": 441, "stop_loss_pct": 14}` | long DBC since 2025-08-01 00:00 @ 24.18179; long SPY since 2026-05-01 00:00 @ 727.115271; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 33,900.98 | 12,418.71 | 20,209.67 | 15,176.61 |
| return % | 339.01 | 124.19 | 202.10 | 151.77 |
| return %/year | 13.1 | 7.7 | 9.7 | 8.8 |
| gross profit | 48,371.14 | 25,172.17 | 33,705.10 | 22,223.07 |
| gross loss | 14,470.16 | 12,753.46 | 13,495.43 | 7,046.46 |
| trades | 115 | 122 | 109 | 111 |
| win rate % | 58.3 | 51.6 | 55.0 | 45.0 |
| avg win | 721.96 | 399.56 | 561.75 | 444.46 |
| avg loss | -301.46 | -216.16 | -275.42 | -115.52 |
| avg result / trade | 294.79 | 101.79 | 185.41 | 136.73 |
| largest single loss | -1,767.75 | -1,034.13 | -1,034.92 | -583.29 |
| largest loss % of equity | -3.69 | -5.44 | -3.49 | -4.78 |
| max drawdown | -8,888.94 | -5,379.45 | -3,580.02 | -4,672.24 |
| max drawdown % | -17.15 | -26.24 | -18.42 | -23.53 |
| profit factor | 3.34 | 1.97 | 2.50 | 3.15 |
| unusually bad trades | 5 | 10 | 9 | 4 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 36.0 | 34.9 | 53.8 | 53.5 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.59 |  | 0.92 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 10.1 | 8.4 |
| 2005 | 10.9 | 12.4 |
| 2006 | 25.7 | 21.9 |
| 2007 | 23.3 | 18.6 |
| 2008 | 19.8 | 8.9 |
| 2009 | 19.1 | 22.8 |
| 2010 | 11.5 | 10.3 |
| 2011 | 14.5 | 4.0 |
| 2012 | 9.6 | 4.4 |
| 2013 | 16.2 | 6.1 |
| 2014 | 11.5 | 5.7 |
| 2015 | -10.2 | -4.4 |
| 2016 (OOS) | 3.4 | 1.0 |
| 2017 (OOS) | 17.1 | 14.5 |
| 2018 (OOS) | -4.3 | -5.6 |
| 2019 (OOS) | 7.0 | 10.4 |
| 2020 (OOS) | 21.7 | 19.9 |
| 2021 (OOS) | 21.5 | 20.8 |
| 2022 (OOS) | -19.9 | -15.7 |
| 2023 (OOS) | 5.7 | 8.4 |
| 2024 (OOS) | 11.3 | 10.6 |
| 2025 (OOS) | 23.9 | 25.7 |
| 2026 (OOS) | 0.8 | 9.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.1% from a peak in-sample and 26.2% out-of-sample, and the worst single trade cost 5.4% of the account out-of-sample. About 58 of every 100 trades won in-sample. Out-of-sample it earned 7.7% a year against 13.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 18.4% from a peak in-sample and 23.5% out-of-sample, and the worst single trade cost 4.8% of the account out-of-sample. About 55 of every 100 trades won in-sample. With 100% of equity per trade; about 42% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 280 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 24}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 634 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 17}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 784 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 22}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 788 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 25}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 852 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 15}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 906 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 21}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 1079 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 18}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 1354 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 19}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 1388 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 23}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 1638 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 16}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 1736 | `{"k": 2, "max_candles": 168, "stop_loss_pct": 20}` | 33,945.19 | 13.1 | -21.1 | 56.5 | 17,143.02 | 9.6 | -24.4 | 0.73 | 108/99 | not checked |
| 5 | `{"k": 3, "max_candles": 231, "stop_loss_pct": 15.0}` | 33,900.98 | 13.1 | -17.1 | 58.3 | 12,418.71 | 7.7 | -26.2 | 0.59 | 115/122 | 1.00 |
| 210 | `{"k": 3, "max_candles": 231, "stop_loss_pct": 15}` | 33,900.98 | 13.1 | -17.1 | 58.3 | 12,418.71 | 7.7 | -26.2 | 0.59 | 115/122 | not checked |
| 876 | `{"k": 3, "max_candles": 231, "stop_loss_pct": 8}` | 26,597.48 | 11.4 | -16.9 | 55.8 | 9,356.42 | 6.2 | -28.4 | 0.55 | 120/126 | not checked |
| 1117 | `{"k": 4, "max_candles": 189, "stop_loss_pct": 14}` | 23,230.98 | 10.5 | -16.3 | 54.7 | 12,135.13 | 7.6 | -24.6 | 0.72 | 137/131 | not checked |
| 1291 | `{"k": 4, "max_candles": 231, "stop_loss_pct": 18}` | 22,168.06 | 10.2 | -15.7 | 53.4 | 12,478.18 | 7.7 | -26.2 | 0.76 | 131/128 | not checked |
| 10 | `{"k": 4, "max_candles": 231, "stop_loss_pct": 15.0}` | 21,524.89 | 10.1 | -15.5 | 53.0 | 12,218.94 | 7.6 | -26.2 | 0.76 | 132/128 | not checked |
| 1196 | `{"k": 4, "max_candles": 231, "stop_loss_pct": 15}` | 21,524.89 | 10.1 | -15.5 | 53.0 | 12,218.94 | 7.6 | -26.2 | 0.76 | 132/128 | not checked |
| 698 | `{"k": 4, "max_candles": 189, "stop_loss_pct": 13}` | 20,795.58 | 9.8 | -15.4 | 53.2 | 12,175.07 | 7.6 | -24.6 | 0.77 | 139/132 | not checked |
| 974 | `{"k": 5, "max_candles": 231, "stop_loss_pct": 13}` | 19,915.45 | 9.6 | -14.7 | 55.3 | 12,318.64 | 7.7 | -26.2 | 0.80 | 123/128 | not checked |
| 110 | `{"k": 5, "max_candles": 189, "stop_loss_pct": 10}` | 17,325.63 | 8.7 | -14.6 | 52.2 | 12,695.93 | 7.8 | -24.6 | 0.90 | 138/137 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 2,086 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
