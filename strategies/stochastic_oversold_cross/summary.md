# stochastic_oversold_cross: optimization summary

Updated 2026-11-25T09:04:52Z · backtest.py version `1fce26ee1e` · 50,395 parameter sets tested with this version (50,395 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [stochastic_oversold_cross__max-income__v001.md](stochastic_oversold_cross__max-income__v001.md) | 40377 | `{"level": 26, "max_candles": 20, "stop_atr": 4.25, "take_profit_atr": 7.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [stochastic_oversold_cross__balanced__v001.md](stochastic_oversold_cross__balanced__v001.md) | 40378 | `{"level": 18, "max_candles": 18, "stop_atr": 4.5, "take_profit_atr": 6.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [stochastic_oversold_cross__safe-starter__v001.md](stochastic_oversold_cross__safe-starter__v001.md) | 40379 | `{"level": 17, "max_candles": 18, "stop_atr": 4.25, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 29,080.35 | 2,985.00 | 19,698.09 | 2,539.67 | 11,764.92 | 2,448.31 |
| return % | 290.80 | 29.85 | 196.98 | 25.40 | 117.65 | 24.48 |
| return %/year | 8.9 | 2.4 | 7.0 | 2.1 | 5.0 | 2.0 |
| gross profit | 51,147.04 | 11,273.37 | 29,358.26 | 7,873.85 | 19,286.66 | 7,146.47 |
| gross loss | 22,066.69 | 8,288.37 | 9,660.17 | 5,334.18 | 7,521.74 | 4,698.16 |
| trades | 48 | 35 | 33 | 25 | 30 | 22 |
| win rate % | 79.2 | 74.3 | 75.8 | 80.0 | 73.3 | 81.8 |
| avg win | 1,345.97 | 433.59 | 1,174.33 | 393.69 | 876.67 | 397.03 |
| avg loss | -2,206.67 | -920.93 | -1,207.52 | -1,066.84 | -940.22 | -1,174.54 |
| avg result / trade | 605.84 | 85.29 | 596.91 | 101.59 | 392.16 | 111.29 |
| largest single loss | -7,132.59 | -2,063.25 | -2,570.39 | -2,000.96 | -1,770.70 | -1,814.70 |
| largest loss % of equity | -22.74 | -15.96 | -9.24 | -16.89 | -8.74 | -15.96 |
| max drawdown | -8,772.70 | -3,788.23 | -3,077.59 | -3,793.39 | -2,227.00 | -3,331.87 |
| max drawdown % | -27.56 | -27.35 | -22.60 | -29.88 | -21.95 | -27.35 |
| profit factor | 2.32 | 1.36 | 3.04 | 1.48 | 2.56 | 1.52 |
| unusually bad trades | 1 | 1 | 0 | 1 | 0 | 0 |
| … threshold (% of equity) | 14.0 | 15.2 | 14.7 | 16.1 | 15.5 | 17.8 |
| time in market % | 14.6 | 15.4 | 10.2 | 11.1 | 9.0 | 8.9 |
| buy & hold return % | 2,918.19 | 1,414.11 | 2,918.19 | 1,414.11 | 2,918.19 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |  | 0.30 |  | 0.41 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 4.0 | 8.9 | -8.0 |
| 2001 | 2.3 | 0.0 | 0.0 |
| 2002 | 18.1 | 12.6 | 0.0 |
| 2003 | 37.7 | 17.2 | 17.2 |
| 2004 | 7.5 | 1.2 | 1.2 |
| 2005 | 24.2 | 16.4 | 16.4 |
| 2006 | -3.9 | -0.2 | -0.2 |
| 2007 | 41.2 | 39.2 | 30.1 |
| 2008 | -22.7 | -7.6 | -7.6 |
| 2009 | 14.1 | 5.1 | 5.1 |
| 2010 | 7.5 | 6.0 | 6.0 |
| 2011 | 14.6 | 8.0 | 12.3 |
| 2012 | -8.2 | -3.5 | -3.0 |
| 2013 | 2.6 | 2.6 | 2.6 |
| 2014 | 15.1 | 13.0 | 13.0 |
| 2015 | 5.9 | 1.5 | 1.5 |
| 2016 (OOS) | 6.9 | 7.3 | 5.5 |
| 2017 (OOS) | 4.7 | 4.7 | 4.7 |
| 2018 (OOS) | 7.6 | -1.7 | -1.7 |
| 2019 (OOS) | 7.4 | 7.4 | 4.8 |
| 2020 (OOS) | -12.3 | -16.7 | -15.8 |
| 2021 (OOS) | 1.3 | -4.8 | 3.5 |
| 2022 (OOS) | 0.7 | 9.7 | 9.7 |
| 2023 (OOS) | 3.9 | 3.2 | 3.2 |
| 2024 (OOS) | -2.5 | -2.7 | -2.5 |
| 2025 (OOS) | 0.1 | 0.1 | 0.5 |
| 2026 (OOS) | 10.7 | 20.9 | 13.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 27.6% from a peak in-sample and 27.4% out-of-sample, and the worst single trade cost 16.0% of the account out-of-sample. About 79 of every 100 trades won in-sample. Out-of-sample it earned 2.4% a year against 8.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 22.6% from a peak in-sample and 29.9% out-of-sample, and the worst single trade cost 16.9% of the account out-of-sample. About 76 of every 100 trades won in-sample. Out-of-sample it earned 2.1% a year against 7.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 33% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 21.9% from a peak in-sample and 27.4% out-of-sample, and the worst single trade cost 16.0% of the account out-of-sample. About 73 of every 100 trades won in-sample. Out-of-sample it earned 2.0% a year against 5.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 37% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 40434 | `{"level": 26, "max_candles": 20, "stop_atr": 4.25, "take_profit_atr": 8.5}` | 29,839.86 | 9.0 | -27.6 | 79.2 | 2,985.00 | 2.4 | -27.4 | 0.27 | 48/35 | not checked |
| 40643 | `{"level": 21, "max_candles": 20, "stop_atr": 4.25, "take_profit_atr": 8.5}` | 26,421.53 | 8.4 | -22.8 | 76.9 | 2,552.64 | 2.1 | -27.4 | 0.25 | 39/30 | not checked |
| 34052 | `{"level": 18, "max_candles": 18, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 20,524.70 | 7.2 | -22.6 | 75.8 | 2,723.38 | 2.2 | -29.1 | 0.31 | 33/25 | not checked |
| 36132 | `{"level": 21, "max_candles": 18, "stop_atr": 4.25, "take_profit_atr": 2.0}` | 18,066.44 | 6.7 | -21.9 | 77.5 | 2,657.73 | 2.2 | -22.1 | 0.33 | 40/30 | not checked |
| 36589 | `{"level": 16, "max_candles": 20, "stop_atr": 1.5, "take_profit_atr": 6.5}` | 9,751.94 | 4.3 | -19.2 | 59.4 | 1,993.98 | 1.7 | -23.9 | 0.39 | 32/23 | not checked |
| 33161 | `{"level": 16, "max_candles": 14, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 8,257.66 | 3.8 | -19.1 | 65.6 | 2,051.06 | 1.7 | -21.7 | 0.45 | 32/19 | not checked |
| 31899 | `{"level": 16, "max_candles": 14, "stop_atr": 2.25, "take_profit_atr": 6.5}` | 7,762.26 | 3.7 | -17.4 | 62.5 | 1,661.35 | 1.4 | -24.9 | 0.39 | 32/19 | not checked |
| 16164 | `{"level": 16, "max_candles": 22, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 1,709.28 | 1.0 | -17.2 | 48.5 | 290.37 | 0.3 | -13.7 | 0.26 | 33/23 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

468 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | 100% | 9.3 | 18.7 | 39.4 | 7.2 | 5.6 | 59 |
| 2 | SBAC | 100% | 7.8 | 12.3 | 5.6 | 7.9 | -1.7 | 0 |
| 3 | DECK | 100% | 6.9 | 13.0 | 28.3 | 8.0 | -4.2 | 13 |
| 4 | NVO | 100% | 6.2 | 10.0 | 23.0 | 5.9 | 1.7 | 57 |
| 5 | CMI | 100% | 6.0 | 10.4 | 15.6 | 6.6 | 0.4 | 19 |
| 6 | TSN | 100% | 5.6 | 11.2 | 8.9 | 5.6 | -0.4 | 4 |
| 7 | SRE | 100% | 4.6 | 7.0 | 15.2 | 4.3 | -2.5 | 0 |
| 8 | ITW | 100% | 4.3 | 7.4 | 9.4 | 5.1 | -0.3 | 2 |
| 9 | UDR | 100% | 3.6 | 8.6 | 15.5 | 3.6 | -1.1 | 7 |
| 10 | SPG | 100% | 3.4 | 6.0 | 20.0 | 4.6 | -1.1 | 4 |
| 11 | BXP | 100% | 3.2 | 5.4 | 14.8 | 2.2 | -3.9 | 2 |
| 12 | ROP | 100% | 3.2 | 8.8 | 16.3 | 2.0 | 1.1 | 39 |
| 13 | CPT | 100% | 2.9 | 6.6 | 12.4 | 4.6 | 3.3 | 38 |
| 14 | VMRK | 100% | 2.9 | 7.2 | 13.9 | 3.2 | -0.5 | 14 |
| 15 | PGR | 100% | 2.4 | 4.5 | 13.5 | 3.1 | 0.8 | 59 |
| 16 | ECL | 100% | 2.1 | 3.9 | 13.1 | 1.7 | -0.3 | 9 |
| 17 | GRMN | 98% | 4.0 | 9.0 | 12.9 | 6.3 | 4.2 | 60 |
| 18 | ARE | 98% | 3.8 | 7.7 | 10.8 | 3.8 | 1.6 | 53 |
| 19 | FRT | 98% | 3.5 | 6.0 | 18.9 | 4.6 | 1.1 | 36 |
| 20 | AKAM | 98% | 3.5 | 7.6 | 7.0 | 3.7 | 0.5 | 45 |
| 21 | GPC | 98% | 3.1 | 7.6 | 11.8 | 2.1 | -2.1 | 9 |
| 22 | CSX | 98% | 3.0 | 9.2 | 12.7 | 4.3 | -0.2 | 30 |
| 23 | KLAC | 98% | 2.3 | 4.9 | 4.3 | 3.9 | 7.6 | 63 |
| 24 | BAX | 98% | 2.3 | 4.7 | 7.7 | 2.2 | -1.0 | 1 |
| 25 | IVZ | 98% | 2.2 | 5.4 | 4.9 | 1.2 | -3.7 | 10 |
| 26 | LNT | 98% | 2.1 | 4.3 | 10.4 | 3.5 | -1.8 | 6 |
| 27 | DHI | 97% | 7.4 | 11.3 | 15.8 | 6.5 | -1.9 | 12 |
| 28 | MTB | 97% | 4.1 | 8.8 | 9.6 | 3.9 | -0.3 | 3 |
| 29 | SLB | 97% | 3.6 | 6.2 | 7.4 | 4.5 | -3.7 | 4 |
| 30 | ESS | 97% | 3.6 | 8.8 | 17.7 | 2.5 | -3.1 | 0 |
| 31 | MAR | 97% | 3.6 | 6.2 | 10.9 | 4.1 | 1.2 | 28 |
| 32 | COO | 97% | 3.5 | 8.1 | 14.8 | 4.5 | 0.5 | 17 |
| 33 | ADBE | 97% | 3.3 | 6.2 | 11.4 | 0.9 | 3.7 | 55 |
| 34 | NUE | 97% | 3.2 | 7.5 | 10.0 | 2.4 | 1.3 | 37 |
| 35 | TPL | 97% | 2.2 | 4.8 | 20.4 | 2.5 | -0.6 | 35 |
| 36 | PEP | 97% | 1.5 | 3.0 | 9.2 | 1.5 | -1.1 | 7 |
| 37 | CCI | 95% | 5.0 | 15.1 | 7.1 | 5.3 | -1.1 | 4 |
| 38 | APH | 95% | 4.5 | 9.4 | 17.4 | 4.8 | 5.1 | 59 |
| 39 | PSA | 95% | 2.8 | 7.2 | 20.5 | 1.6 | -2.2 | 0 |
| 40 | CHD | 95% | 2.6 | 6.0 | 16.4 | 1.2 | -0.6 | 20 |

(428 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [stochastic_oversold_cross__broad__max-income__v002.md](symbols/broad/stochastic_oversold_cross__broad__max-income__v002.md) | 2.4 | 2.3 | 2.3 | -7.8 | 68.2 | 22612/16648 |
| broad | balanced | [stochastic_oversold_cross__broad__balanced__v001.md](symbols/broad/stochastic_oversold_cross__broad__balanced__v001.md) | 1.7 | 1.1 | 1.1 | -4.3 | 61.4 | 13330/10117 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 50,395 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
