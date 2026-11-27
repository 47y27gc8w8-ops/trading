# chaikin_oscillator_cross: optimization summary

Updated 2026-11-25T17:28:04Z · backtest.py version `7f972f2d22` · 756 parameter sets tested with this version (756 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: MSFT (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [chaikin_oscillator_cross__max-income__v002.md](chaikin_oscillator_cross__max-income__v002.md) | 756 | `{"max_bars": 66, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 5,505.54 | 1,375.74 |
| return % | 55.06 | 13.76 |
| return %/year | 2.1 | 1.2 |
| gross profit | 86,205.57 | 22,992.39 |
| gross loss | 80,700.03 | 21,616.65 |
| trades | 224 | 128 |
| win rate % | 34.4 | 43.0 |
| avg win | 1,119.55 | 418.04 |
| avg loss | -548.98 | -296.12 |
| avg result / trade | 24.58 | 10.75 |
| largest single loss | -4,130.97 | -826.03 |
| largest loss % of equity | -12.25 | -6.85 |
| max drawdown | -26,836.14 | -6,071.99 |
| max drawdown % | -73.27 | -48.51 |
| profit factor | 1.07 | 1.06 |
| unusually bad trades | 25 | 19 |
| … threshold (% of equity) | 4.8 | 4.5 |
| time in market % | 34.5 | 45.8 |
| buy & hold return % | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.56 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 1995 | 22.0 |
| 1996 | 18.6 |
| 1997 | -11.5 |
| 1998 | 42.7 |
| 1999 | 48.3 |
| 2000 | 6.7 |
| 2001 | -19.9 |
| 2002 | -24.3 |
| 2003 | 4.4 |
| 2004 | 1.0 |
| 2005 | 5.6 |
| 2006 | 4.6 |
| 2007 | -4.3 |
| 2008 | -38.1 |
| 2009 | 5.1 |
| 2010 | 14.3 |
| 2011 | 3.2 |
| 2012 | 0.7 |
| 2013 | -0.4 |
| 2014 | 10.4 |
| 2015 | -6.4 |
| 2016 (OOS) | -17.6 |
| 2017 (OOS) | 23.5 |
| 2018 (OOS) | 2.6 |
| 2019 (OOS) | 7.0 |
| 2020 (OOS) | -5.0 |
| 2021 (OOS) | -1.0 |
| 2022 (OOS) | -32.7 |
| 2023 (OOS) | 21.8 |
| 2024 (OOS) | 25.2 |
| 2025 (OOS) | 4.9 |
| 2026 (OOS) | -1.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 73.3% from a peak in-sample and 48.5% out-of-sample, and the worst single trade cost 6.8% of the account out-of-sample. About 34 of every 100 trades won in-sample. Out-of-sample it earned 1.2% a year against 2.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 14% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 288 | `{"max_bars": 60, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 289 | `{"max_bars": 72, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 290 | `{"max_bars": 66, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | 1.00 |
| 363 | `{"max_bars": 78, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 369 | `{"max_bars": 54, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 385 | `{"max_bars": 48, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 453 | `{"max_bars": 84, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 467 | `{"max_bars": 90, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 513 | `{"max_bars": 96, "n": 20, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 5,505.54 | 2.1 | -73.3 | 34.4 | 1,375.74 | 1.2 | -48.5 | 0.56 | 224/128 | not checked |
| 233 | `{"max_bars": 48, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,619.11 | 1.4 | -47.7 | 0.72 | 224/128 | not checked |
| 237 | `{"max_bars": 66, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 255 | `{"max_bars": 60, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 362 | `{"max_bars": 72, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 387 | `{"max_bars": 54, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 463 | `{"max_bars": 84, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 493 | `{"max_bars": 96, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 504 | `{"max_bars": 78, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 540 | `{"max_bars": 90, "n": 20, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 4,949.26 | 1.9 | -72.0 | 34.4 | 1,753.49 | 1.5 | -47.7 | 0.78 | 224/128 | not checked |
| 279 | `{"max_bars": 48, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,473.43 | 2.0 | -46.1 | 1.34 | 224/128 | not checked |
| 297 | `{"max_bars": 60, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,617.69 | 2.2 | -46.1 | 1.41 | 224/128 | not checked |
| 342 | `{"max_bars": 66, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,617.69 | 2.2 | -46.1 | 1.41 | 224/128 | not checked |
| 587 | `{"max_bars": 78, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,617.69 | 2.2 | -46.1 | 1.41 | 224/128 | not checked |
| 658 | `{"max_bars": 72, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,617.69 | 2.2 | -46.1 | 1.41 | 224/128 | not checked |
| 673 | `{"max_bars": 54, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,617.69 | 2.2 | -46.1 | 1.41 | 224/128 | not checked |
| 725 | `{"max_bars": 84, "n": 20, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 3,743.24 | 1.5 | -71.3 | 33.9 | 2,617.69 | 2.2 | -46.1 | 1.41 | 224/128 | not checked |

(11 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

475 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | DAL | 100% | 13.1 | 28.6 | 12.2 | 14.1 | 1.3 | 1 |
| 2 | MPWR | 100% | 13.0 | 20.2 | 25.9 | 10.3 | -0.7 | 18 |
| 3 | CSGP | 100% | 12.1 | 23.5 | 17.3 | 17.1 | -2.6 | 2 |
| 4 | ULTA | 100% | 10.8 | 21.1 | 39.8 | 20.0 | -1.5 | 0 |
| 5 | TSCO | 100% | 9.9 | 17.2 | 22.3 | 9.9 | 0.6 | 38 |
| 6 | CPT | 100% | 8.3 | 10.4 | 11.8 | 10.4 | -3.8 | 0 |
| 7 | SBUX | 100% | 8.3 | 14.6 | 23.0 | 6.6 | 1.6 | 27 |
| 8 | DLR | 100% | 7.9 | 10.8 | 22.2 | 6.4 | -4.1 | 1 |
| 9 | STZ | 100% | 7.9 | 14.2 | 17.6 | 8.3 | 2.0 | 18 |
| 10 | PSX | 100% | 7.7 | 17.2 | 21.8 | 7.8 | 3.0 | 28 |
| 11 | APTV | 100% | 7.7 | 17.8 | 37.0 | 4.2 | -8.9 | 0 |
| 12 | ORLY | 100% | 7.5 | 14.1 | 23.4 | 11.1 | -1.1 | 0 |
| 13 | MNST | 100% | 7.3 | 13.5 | 40.8 | 4.2 | 4.9 | 41 |
| 14 | ROST | 100% | 7.0 | 14.0 | 28.2 | 5.0 | -4.8 | 0 |
| 15 | HSIC | 100% | 6.3 | 8.9 | 12.0 | 4.3 | -4.4 | 0 |
| 16 | FICO | 100% | 6.2 | 13.6 | 12.9 | 11.5 | 6.6 | 57 |
| 17 | CMS | 100% | 6.2 | 11.5 | 5.5 | 7.6 | 3.0 | 62 |
| 18 | PGHN.SW | 100% | 5.3 | 17.1 | 18.8 | 7.4 | -3.4 | 8 |
| 19 | AMZN | 100% | 5.0 | 11.5 | 31.0 | 2.5 | 6.4 | 54 |
| 20 | COR | 100% | 4.8 | 10.0 | 19.3 | 4.1 | 2.5 | 24 |
| 21 | AME | 100% | 4.2 | 7.5 | 16.7 | 5.0 | 4.4 | 53 |
| 22 | CHRW | 100% | 3.9 | 6.8 | 15.7 | 0.5 | -5.9 | 1 |
| 23 | MRSH | 100% | 3.9 | 7.0 | 10.0 | 2.6 | 3.4 | 36 |
| 24 | AEE | 100% | 3.5 | 7.1 | 6.1 | 5.4 | 2.8 | 57 |
| 25 | OMC | 100% | 2.8 | 6.4 | 14.2 | 1.3 | -7.8 | 0 |
| 26 | CHD | 100% | 2.7 | 5.7 | 18.8 | 2.9 | -4.1 | 4 |
| 27 | HUBB | 100% | 2.5 | 8.2 | 10.2 | 3.1 | -4.9 | 2 |
| 28 | PEG | 100% | 2.5 | 4.7 | 10.7 | 2.5 | 2.8 | 50 |
| 29 | HII | 98% | 15.3 | 31.5 | 45.2 | 11.2 | -2.9 | 0 |
| 30 | SBAC | 98% | 10.9 | 16.1 | 13.6 | 9.4 | 3.4 | 6 |
| 31 | NFLX | 98% | 10.3 | 22.0 | 49.2 | 3.8 | -4.7 | 2 |
| 32 | NTAP | 98% | 10.3 | 18.3 | 13.3 | 18.3 | 4.2 | 34 |
| 33 | TDG | 98% | 8.0 | 15.2 | 36.2 | 7.9 | 5.2 | 62 |
| 34 | LYB | 98% | 5.4 | 13.4 | 33.8 | 5.0 | -5.5 | 0 |
| 35 | FIS | 98% | 5.2 | 10.1 | 10.8 | 4.2 | -4.5 | 1 |
| 36 | EME | 98% | 4.9 | 13.2 | 17.0 | 7.8 | -0.2 | 21 |
| 37 | CPAY | 98% | 4.4 | 12.0 | 40.2 | 7.3 | -2.9 | 2 |
| 38 | SYK | 98% | 4.1 | 10.2 | 16.1 | 1.7 | -5.4 | 5 |
| 39 | MO | 98% | 3.8 | 6.0 | 19.0 | 4.7 | 2.0 | 51 |
| 40 | IDXX | 98% | 3.4 | 6.7 | 14.3 | 3.9 | 6.9 | 62 |

(435 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [chaikin_oscillator_cross__broad__max-income__v002.md](symbols/broad/chaikin_oscillator_cross__broad__max-income__v002.md) | 3.6 | 3.0 | 3.0 | -33.8 | 38.0 | 105613/68775 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 756 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
