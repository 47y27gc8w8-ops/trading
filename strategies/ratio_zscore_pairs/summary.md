# ratio_zscore_pairs: optimization summary

Updated 2026-11-27T12:06:36Z · backtest.py version `c920f7da44` · 6,189 parameter sets tested with this version (6,189 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: KO, PEP (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [ratio_zscore_pairs__max-income__v002.md](ratio_zscore_pairs__max-income__v002.md) | 6188 | `{"leg_stop_pct": 13, "max_candles": 40, "n": 100, "pair_stop_pct": 4.0, "z": 1.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [ratio_zscore_pairs__balanced__v002.md](ratio_zscore_pairs__balanced__v002.md) | 6189 | `{"leg_stop_pct": 12, "max_candles": 40, "n": 100, "pair_stop_pct": 4.0, "z": 1.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,156.83 | 200.49 | 1,214.38 | 200.49 |
| return % | 11.57 | 2.00 | 12.14 | 2.00 |
| return %/year | 0.7 | 0.2 | 0.7 | 0.2 |
| gross profit | 2,430.93 | 3,514.31 | 2,440.96 | 3,514.31 |
| gross loss | 1,274.10 | 3,313.82 | 1,226.57 | 3,313.82 |
| trades | 23 | 33 | 23 | 33 |
| win rate % | 69.6 | 57.6 | 69.6 | 57.6 |
| avg win | 151.93 | 184.96 | 152.56 | 184.96 |
| avg loss | -182.01 | -236.70 | -175.22 | -236.70 |
| avg result / trade | 50.30 | 6.08 | 52.80 | 6.08 |
| largest single loss | -346.39 | -475.96 | -346.39 | -475.96 |
| largest loss % of equity | -3.33 | -4.85 | -3.33 | -4.85 |
| max drawdown | -959.66 | -1,166.49 | -918.96 | -1,166.49 |
| max drawdown % | -9.19 | -11.07 | -8.80 | -11.07 |
| profit factor | 1.91 | 1.06 | 1.99 | 1.06 |
| unusually bad trades | 3 | 3 | 3 | 3 |
| … threshold (% of equity) | 2.5 | 4.2 | 2.5 | 4.2 |
| time in market % | 11.4 | 29.9 | 11.4 | 29.9 |
| buy & hold return % | 0.00 | 0.00 | 0.00 | 0.00 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |  | 0.25 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 0.0 | 0.0 |
| 2001 | 0.0 | 0.0 |
| 2002 | -1.2 | -1.2 |
| 2003 | 3.8 | 3.8 |
| 2004 | 0.0 | 0.0 |
| 2005 | 1.5 | 1.5 |
| 2006 | 0.0 | 0.0 |
| 2007 | 0.0 | 0.0 |
| 2008 | -1.5 | -1.0 |
| 2009 | 2.8 | 2.8 |
| 2010 | 0.0 | 0.0 |
| 2011 | 0.6 | 0.6 |
| 2012 | 1.7 | 1.7 |
| 2013 | 0.6 | 0.6 |
| 2014 | 0.9 | 0.9 |
| 2015 | 2.1 | 2.1 |
| 2016 (OOS) | -3.7 | -3.7 |
| 2017 (OOS) | -0.5 | -0.5 |
| 2018 (OOS) | 5.9 | 5.9 |
| 2019 (OOS) | -3.3 | -3.3 |
| 2020 (OOS) | 3.9 | 3.9 |
| 2021 (OOS) | -1.7 | -1.7 |
| 2022 (OOS) | -2.4 | -2.4 |
| 2023 (OOS) | 0.1 | 0.1 |
| 2024 (OOS) | 2.7 | 2.7 |
| 2025 (OOS) | 1.4 | 1.4 |
| 2026 (OOS) | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.2% from a peak in-sample and 11.1% out-of-sample, and the worst single trade cost 4.8% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.7% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 90% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 8.8% from a peak in-sample and 11.1% out-of-sample, and the worst single trade cost 4.8% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.7% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 90% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5672 | `{"leg_stop_pct": 12, "max_candles": 40, "n": 100, "pair_stop_pct": 4.0, "z": 1.0}` | 1,214.38 | 0.7 | -8.8 | 69.6 | 200.49 | 0.2 | -11.1 | 0.25 | 23/33 | 1.00 |
| 5681 | `{"leg_stop_pct": 12, "max_candles": 40, "n": 100, "pair_stop_pct": 4.5, "z": 1.0}` | 1,214.38 | 0.7 | -8.8 | 69.6 | 287.39 | 0.3 | -11.1 | 0.36 | 23/33 | not checked |
| 5874 | `{"leg_stop_pct": 14, "max_candles": 45, "n": 100, "pair_stop_pct": 4.0, "z": 0.75}` | 700.41 | 0.4 | -8.3 | 66.7 | 176.50 | 0.2 | -9.6 | 0.38 | 27/41 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 6,189 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
