# low_correlation_momentum_selection: optimization summary

Updated 2026-11-27T12:05:10Z · backtest.py version `86f922c15c` · 1,077 parameter sets tested with this version (1,077 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [low_correlation_momentum_selection__max-income__v001.md](low_correlation_momentum_selection__max-income__v001.md) | 256 | `{"corr": 0.65, "k": 3, "max_candles": 273, "stop_loss_pct": 8}` | long DBC since 2026-07-01 00:00 @ 28.576484 |
| balanced | [low_correlation_momentum_selection__balanced__v001.md](low_correlation_momentum_selection__balanced__v001.md) | 257 | `{"corr": 0.65, "k": 3, "max_candles": 294, "stop_loss_pct": 8}` | long DBC since 2026-07-01 00:00 @ 28.576484 |
| safe-starter | [low_correlation_momentum_selection__safe-starter__v002.md](low_correlation_momentum_selection__safe-starter__v002.md) | 1077 | `{"corr": 0.9, "k": 3, "max_candles": 231, "stop_loss_pct": 5}` | long DBC since 2026-03-02 00:00 @ 26.016303 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 32,494.81 | 10,060.39 | 28,911.92 | 9,100.56 | 17,897.41 | 15,938.59 |
| return % | 324.95 | 100.60 | 289.12 | 91.01 | 178.97 | 159.39 |
| return %/year | 12.8 | 6.6 | 12.0 | 6.1 | 8.9 | 9.2 |
| gross profit | 50,733.87 | 24,661.13 | 44,841.59 | 22,962.29 | 35,940.26 | 29,849.32 |
| gross loss | 18,239.05 | 14,600.73 | 15,929.67 | 13,861.73 | 18,042.85 | 13,910.73 |
| trades | 85 | 90 | 84 | 89 | 116 | 102 |
| win rate % | 61.2 | 46.7 | 61.9 | 47.2 | 46.5 | 52.9 |
| avg win | 975.65 | 587.17 | 862.34 | 546.72 | 665.56 | 552.77 |
| avg loss | -552.70 | -304.18 | -497.80 | -294.93 | -291.01 | -289.81 |
| avg result / trade | 382.29 | 111.78 | 344.19 | 102.25 | 154.29 | 156.26 |
| largest single loss | -3,226.57 | -901.80 | -2,947.92 | -858.66 | -743.72 | -949.39 |
| largest loss % of equity | -6.91 | -4.06 | -7.03 | -4.06 | -2.56 | -5.12 |
| max drawdown | -7,606.73 | -4,549.90 | -6,067.23 | -4,411.25 | -4,982.95 | -6,097.75 |
| max drawdown % | -18.57 | -24.66 | -18.57 | -24.66 | -19.55 | -26.11 |
| profit factor | 2.78 | 1.69 | 2.81 | 1.66 | 1.99 | 2.15 |
| unusually bad trades | 1 | 1 | 3 | 1 | 0 | 1 |
| … threshold (% of equity) | 3.6 | 4.9 | 3.2 | 4.8 | 3.4 | 3.4 |
| time in market % | 30.6 | 32.4 | 30.9 | 32.6 | 31.9 | 32.2 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |  | 0.51 |  | 1.02 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2004 | 4.1 | 4.1 | 2.4 |
| 2005 | 24.2 | 24.4 | 16.1 |
| 2006 | 22.6 | 18.8 | 17.1 |
| 2007 | 28.3 | 28.3 | 19.4 |
| 2008 | 40.2 | 32.8 | 25.4 |
| 2009 | 1.0 | 1.0 | 1.2 |
| 2010 | 13.2 | 10.8 | 10.7 |
| 2011 | 12.5 | 12.0 | 8.5 |
| 2012 | 1.9 | 1.9 | 2.8 |
| 2013 | 12.4 | 12.4 | 12.9 |
| 2014 | 10.8 | 10.8 | 3.6 |
| 2015 | -8.5 | -6.6 | -8.4 |
| 2016 (OOS) | 6.8 | 6.8 | 10.1 |
| 2017 (OOS) | 10.1 | 10.1 | 22.6 |
| 2018 (OOS) | -5.4 | -5.4 | -1.2 |
| 2019 (OOS) | 9.0 | 9.0 | 3.7 |
| 2020 (OOS) | 2.2 | 1.9 | 23.0 |
| 2021 (OOS) | 33.2 | 29.7 | 25.4 |
| 2022 (OOS) | -16.2 | -16.3 | -17.8 |
| 2023 (OOS) | 6.1 | 6.1 | 6.0 |
| 2024 (OOS) | 9.8 | 9.8 | 5.5 |
| 2025 (OOS) | 17.5 | 19.9 | 27.4 |
| 2026 (OOS) | 3.8 | 0.0 | 3.5 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 18.6% from a peak in-sample and 24.7% out-of-sample, and the worst single trade cost 4.1% of the account out-of-sample. About 61 of every 100 trades won in-sample. Out-of-sample it earned 6.6% a year against 12.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 18.6% from a peak in-sample and 24.7% out-of-sample, and the worst single trade cost 4.1% of the account out-of-sample. About 62 of every 100 trades won in-sample. Out-of-sample it earned 6.1% a year against 12.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 19.6% from a peak in-sample and 26.1% out-of-sample, and the worst single trade cost 5.1% of the account out-of-sample. About 47 of every 100 trades won in-sample. With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 127 | `{"corr": 0.65, "k": 3, "max_candles": 273, "stop_loss_pct": 9}` | 32,892.06 | 12.9 | -18.6 | 62.6 | 11,181.90 | 7.1 | -24.7 | 0.55 | 83/86 | not checked |
| 516 | `{"corr": 0.8, "k": 3, "max_candles": 273, "stop_loss_pct": 7}` | 23,084.16 | 10.5 | -18.1 | 54.1 | 11,596.98 | 7.3 | -27.6 | 0.70 | 109/86 | not checked |
| 648 | `{"corr": 0.95, "k": 4, "max_candles": 252, "stop_loss_pct": 6}` | 20,235.77 | 9.7 | -17.3 | 50.8 | 16,342.98 | 9.3 | -27.1 | 0.96 | 122/108 | not checked |
| 668 | `{"corr": 0.95, "k": 5, "max_candles": 252, "stop_loss_pct": 6}` | 19,195.11 | 9.3 | -16.3 | 50.4 | 10,697.21 | 6.9 | -27.0 | 0.74 | 129/120 | not checked |
| 625 | `{"corr": 0.95, "k": 5, "max_candles": 252, "stop_loss_pct": 5}` | 19,076.95 | 9.3 | -16.1 | 46.3 | 10,037.13 | 6.6 | -28.9 | 0.71 | 136/126 | not checked |
| 674 | `{"corr": 0.95, "k": 5, "max_candles": 294, "stop_loss_pct": 6}` | 18,345.36 | 9.1 | -15.1 | 50.4 | 9,015.65 | 6.1 | -31.0 | 0.67 | 119/115 | not checked |
| 662 | `{"corr": 0.95, "k": 5, "max_candles": 294, "stop_loss_pct": 5}` | 17,473.81 | 8.8 | -14.4 | 46.1 | 9,542.65 | 6.3 | -28.5 | 0.72 | 128/119 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,077 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
