# half_life_filtered_pairs: optimization summary

Updated 2026-11-27T12:07:41Z · backtest.py version `31c5e452a7` · 790 parameter sets tested with this version (790 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: EWA, EWC (etf, 1d bars)
- In-sample (tuning): 1998-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [half_life_filtered_pairs__max-income__v002.md](half_life_filtered_pairs__max-income__v002.md) | 790 | `{"half": 70, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 3.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [half_life_filtered_pairs__balanced__v001.md](half_life_filtered_pairs__balanced__v001.md) | 255 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 5.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,509.94 | 246.36 | 1,320.59 | 246.36 |
| return % | 15.10 | 2.46 | 13.21 | 2.46 |
| return %/year | 0.8 | 0.2 | 0.7 | 0.2 |
| gross profit | 6,046.67 | 2,325.70 | 5,122.79 | 2,325.70 |
| gross loss | 4,536.72 | 2,079.35 | 3,802.19 | 2,079.35 |
| trades | 57 | 36 | 55 | 36 |
| win rate % | 61.4 | 58.3 | 63.6 | 58.3 |
| avg win | 172.76 | 110.75 | 146.37 | 110.75 |
| avg loss | -206.21 | -138.62 | -190.11 | -138.62 |
| avg result / trade | 26.49 | 6.84 | 24.01 | 6.84 |
| largest single loss | -556.91 | -227.59 | -547.75 | -227.59 |
| largest loss % of equity | -4.85 | -2.20 | -4.85 | -2.20 |
| max drawdown | -1,463.30 | -1,100.77 | -1,233.84 | -1,100.77 |
| max drawdown % | -14.09 | -9.92 | -11.96 | -9.92 |
| profit factor | 1.33 | 1.12 | 1.35 | 1.12 |
| unusually bad trades | 5 | 0 | 4 | 0 |
| … threshold (% of equity) | 3.0 | 2.4 | 3.0 | 2.4 |
| time in market % | 21.4 | 21.6 | 21.2 | 21.6 |
| buy & hold return % | 0.00 | 0.00 | 0.00 | 0.00 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |  | 0.32 |
| period | 1998-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1998-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1998 | 0.9 | 0.3 |
| 1999 | -0.4 | -0.4 |
| 2000 | -5.9 | -6.8 |
| 2001 | 2.0 | 2.0 |
| 2002 | -0.2 | -0.2 |
| 2003 | 4.5 | 4.5 |
| 2004 | 2.0 | 2.0 |
| 2005 | 0.6 | 0.6 |
| 2006 | 1.5 | 1.5 |
| 2007 | -1.2 | -1.2 |
| 2008 | 1.8 | 1.8 |
| 2009 | 8.0 | 8.0 |
| 2010 | -3.3 | -3.3 |
| 2011 | 2.4 | 2.4 |
| 2012 | 0.0 | 0.0 |
| 2013 | -1.9 | -1.9 |
| 2014 | 0.8 | 0.8 |
| 2015 | 3.2 | 3.2 |
| 2016 (OOS) | 2.8 | 2.8 |
| 2017 (OOS) | 3.7 | 3.7 |
| 2018 (OOS) | 2.1 | 2.1 |
| 2019 (OOS) | 1.2 | 1.2 |
| 2020 (OOS) | -2.3 | -2.3 |
| 2021 (OOS) | -2.4 | -2.4 |
| 2022 (OOS) | 4.8 | 4.8 |
| 2023 (OOS) | -0.3 | -0.3 |
| 2024 (OOS) | -1.7 | -1.7 |
| 2025 (OOS) | -6.1 | -6.1 |
| 2026 (OOS) | 1.2 | 1.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 14.1% from a peak in-sample and 9.9% out-of-sample, and the worst single trade cost 2.2% of the account out-of-sample. About 61 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.8% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 71% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 12.0% from a peak in-sample and 9.9% out-of-sample, and the worst single trade cost 2.2% of the account out-of-sample. About 64 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.7% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 84% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 282 | `{"half": 65, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 3.5}` | 1,509.94 | 0.8 | -14.1 | 61.4 | 246.36 | 0.2 | -9.9 | 0.28 | 57/36 | not checked |
| 289 | `{"half": 70, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 3.5}` | 1,509.94 | 0.8 | -14.1 | 61.4 | 246.36 | 0.2 | -9.9 | 0.28 | 57/36 | 0.78 |
| 548 | `{"half": 75, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 3.5}` | 1,509.94 | 0.8 | -14.1 | 61.4 | 246.36 | 0.2 | -9.9 | 0.28 | 57/36 | not checked |
| 555 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 3.5}` | 1,509.94 | 0.8 | -14.1 | 61.4 | 246.36 | 0.2 | -9.9 | 0.28 | 57/36 | not checked |
| 719 | `{"half": 80, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 3.5}` | 1,509.94 | 0.8 | -14.1 | 61.4 | 246.36 | 0.2 | -9.9 | 0.28 | 57/36 | not checked |
| 208 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 5.0}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | 0.78 |
| 219 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 4.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 220 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 5.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 275 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 321 | `{"half": 80, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 330 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.0}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 331 | `{"half": 65, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 4.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 333 | `{"half": 75, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 344 | `{"half": 60, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 7.0}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 413 | `{"half": 80, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.0}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 421 | `{"half": 65, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 5.0}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 431 | `{"half": 65, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 5.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 514 | `{"half": 80, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 7.0}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 523 | `{"half": 65, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |
| 528 | `{"half": 85, "leg_stop_pct": 13, "max_candles": 25, "n": 70, "pair_stop_pct": 6.5}` | 1,320.59 | 0.7 | -12.0 | 63.6 | 246.36 | 0.2 | -9.9 | 0.32 | 55/36 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 790 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
