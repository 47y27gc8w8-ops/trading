# obv_leading_breakout: optimization summary

Updated 2026-11-25T08:22:19Z · backtest.py version `685cc94aa3` · 1,079 parameter sets tested with this version (1,079 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [obv_leading_breakout__max-income__v002.md](obv_leading_breakout__max-income__v002.md) | 1077 | `{"max_candles": 36, "n": 54, "stop_atr": 1.25, "take_profit_atr": 6.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [obv_leading_breakout__balanced__v002.md](obv_leading_breakout__balanced__v002.md) | 1078 | `{"max_candles": 36, "n": 58, "stop_atr": 1.25, "take_profit_atr": 1.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [obv_leading_breakout__safe-starter__v001.md](obv_leading_breakout__safe-starter__v001.md) | 1079 | `{"max_candles": 78, "n": 50, "stop_atr": 1.0, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 24,531.79 | 4,120.65 | 13,320.44 | 2,488.17 | 13,084.59 | 2,766.13 |
| return % | 245.32 | 41.21 | 133.20 | 24.88 | 130.85 | 27.66 |
| return %/year | 6.1 | 3.2 | 4.1 | 2.1 | 4.1 | 2.3 |
| gross profit | 61,180.42 | 12,280.82 | 46,889.43 | 10,819.22 | 48,768.93 | 11,341.41 |
| gross loss | 36,648.63 | 8,160.17 | 33,568.99 | 8,331.05 | 35,684.34 | 8,575.29 |
| trades | 103 | 56 | 134 | 74 | 141 | 71 |
| win rate % | 42.7 | 42.9 | 53.7 | 51.4 | 45.4 | 42.2 |
| avg win | 1,390.46 | 511.70 | 651.24 | 284.72 | 762.01 | 378.05 |
| avg loss | -621.16 | -255.01 | -541.44 | -231.42 | -463.43 | -209.15 |
| avg result / trade | 238.17 | 73.58 | 99.41 | 33.62 | 92.80 | 38.96 |
| largest single loss | -1,789.20 | -597.23 | -1,045.27 | -514.42 | -1,219.34 | -445.19 |
| largest loss % of equity | -5.23 | -4.38 | -8.27 | -4.38 | -5.23 | -3.53 |
| max drawdown | -7,335.84 | -2,402.87 | -2,781.73 | -1,261.64 | -4,222.91 | -1,488.56 |
| max drawdown % | -35.83 | -14.73 | -21.97 | -10.68 | -28.83 | -11.81 |
| profit factor | 1.67 | 1.50 | 1.40 | 1.30 | 1.37 | 1.32 |
| unusually bad trades | 3 | 1 | 3 | 1 | 1 | 0 |
| … threshold (% of equity) | 6.1 | 4.1 | 6.7 | 4.3 | 6.3 | 3.8 |
| time in market % | 12.7 | 12.7 | 6.5 | 8.4 | 7.7 | 8.3 |
| buy & hold return % | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.53 |  | 0.50 |  | 0.56 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | -9.0 | -2.2 | -2.8 |
| 1996 | -13.5 | -8.2 | -7.5 |
| 1997 | 15.9 | -1.2 | -2.4 |
| 1998 | 49.5 | 28.5 | 42.4 |
| 1999 | 18.1 | 10.9 | 11.3 |
| 2000 | 14.8 | 19.1 | 5.2 |
| 2001 | -2.8 | -2.8 | -7.7 |
| 2002 | -12.3 | 4.9 | -2.0 |
| 2003 | -4.8 | 4.2 | -8.0 |
| 2004 | 12.2 | 4.3 | 10.4 |
| 2005 | 22.1 | 5.3 | 14.0 |
| 2006 | 19.5 | 4.1 | 11.2 |
| 2007 | -0.0 | -4.8 | -1.1 |
| 2008 | 17.6 | 8.4 | 3.2 |
| 2009 | -4.7 | 10.4 | 5.6 |
| 2010 | 6.8 | 7.2 | 15.4 |
| 2011 | 2.3 | 2.9 | 3.9 |
| 2012 | 16.8 | 0.8 | 8.2 |
| 2013 | -3.3 | 0.5 | -5.6 |
| 2014 | 8.9 | 5.0 | 5.1 |
| 2015 | -6.6 | -4.6 | -2.2 |
| 2016 (OOS) | -6.2 | -3.6 | -5.1 |
| 2017 (OOS) | 2.0 | -2.2 | -4.1 |
| 2018 (OOS) | 8.2 | 2.9 | 4.9 |
| 2019 (OOS) | 15.9 | 13.1 | 18.0 |
| 2020 (OOS) | 8.6 | 2.3 | 7.9 |
| 2021 (OOS) | 3.4 | -3.2 | -2.9 |
| 2022 (OOS) | -2.0 | 1.3 | -2.8 |
| 2023 (OOS) | 8.7 | 10.8 | 3.3 |
| 2024 (OOS) | 9.7 | 8.1 | 7.8 |
| 2025 (OOS) | -8.1 | -4.1 | -3.8 |
| 2026 (OOS) | -2.6 | -1.2 | 3.9 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 35.8% from a peak in-sample and 14.7% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 3.2% a year against 6.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 28% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 22.0% from a peak in-sample and 10.7% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 54 of every 100 trades won in-sample. Out-of-sample it earned 2.1% a year against 4.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 46% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 28.8% from a peak in-sample and 11.8% out-of-sample, and the worst single trade cost 3.5% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 2.3% a year against 4.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1024 | `{"max_candles": 30, "n": 54, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 24,531.79 | 6.1 | -35.8 | 42.7 | 4,120.65 | 3.2 | -14.7 | 0.53 | 103/56 | not checked |
| 1025 | `{"max_candles": 42, "n": 54, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 24,531.79 | 6.1 | -35.8 | 42.7 | 4,120.65 | 3.2 | -14.7 | 0.53 | 103/56 | not checked |
| 1026 | `{"max_candles": 36, "n": 54, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 24,531.79 | 6.1 | -35.8 | 42.7 | 4,120.65 | 3.2 | -14.7 | 0.53 | 103/56 | 1.00 |
| 356 | `{"max_candles": 54, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 357 | `{"max_candles": 66, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 358 | `{"max_candles": 60, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | 1.00 |
| 522 | `{"max_candles": 48, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 530 | `{"max_candles": 42, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 560 | `{"max_candles": 36, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 601 | `{"max_candles": 72, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 621 | `{"max_candles": 78, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 655 | `{"max_candles": 84, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 691 | `{"max_candles": 30, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 852 | `{"max_candles": 24, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 985 | `{"max_candles": 90, "n": 24, "stop_atr": 0.5, "take_profit_atr": 6.0}` | 23,010.74 | 5.8 | -32.8 | 24.8 | 4,944.81 | 3.8 | -14.4 | 0.64 | 153/89 | not checked |
| 353 | `{"max_candles": 60, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 420 | `{"max_candles": 54, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 454 | `{"max_candles": 66, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 487 | `{"max_candles": 48, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 501 | `{"max_candles": 42, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 511 | `{"max_candles": 72, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 532 | `{"max_candles": 36, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 634 | `{"max_candles": 78, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 699 | `{"max_candles": 84, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |
| 709 | `{"max_candles": 30, "n": 24, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 21,960.12 | 5.7 | -32.0 | 34.1 | 6,264.89 | 4.6 | -16.6 | 0.80 | 135/82 | not checked |

(8 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

452 of 516 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | APTV | 100% | 6.8 | 14.7 | 39.6 | 7.1 | -3.5 | 0 |
| 2 | WYNN | 100% | 6.7 | 11.6 | 15.3 | 5.5 | 0.5 | 21 |
| 3 | VRSN | 100% | 6.3 | 17.0 | 16.7 | 8.9 | 0.3 | 5 |
| 4 | A | 100% | 4.9 | 6.6 | -0.9 | 5.6 | -0.7 | 4 |
| 5 | GLW | 100% | 4.9 | 7.6 | 5.0 | 4.5 | 1.1 | 6 |
| 6 | NDAQ | 100% | 4.5 | 11.2 | 16.0 | 5.2 | 4.1 | 59 |
| 7 | WAT | 100% | 2.9 | 6.1 | 16.2 | 4.0 | -1.9 | 0 |
| 8 | EFX | 100% | 2.7 | 6.0 | 15.2 | 2.0 | -2.2 | 13 |
| 9 | NRG | 100% | 2.3 | 5.3 | -0.3 | 2.6 | 0.3 | 60 |
| 10 | BXP | 100% | 2.0 | 4.8 | 13.2 | 4.3 | 0.4 | 2 |
| 11 | DXCM | 97% | 7.7 | 13.2 | 18.9 | 6.4 | 0.7 | 11 |
| 12 | FTNT | 97% | 6.9 | 19.4 | 26.4 | 6.8 | -4.5 | 5 |
| 13 | OKE | 97% | 6.3 | 9.5 | 13.5 | 7.1 | 1.7 | 46 |
| 14 | GILD | 97% | 4.5 | 6.7 | 32.1 | 1.7 | -8.8 | 0 |
| 15 | GOOG | 97% | 3.0 | 5.3 | 21.9 | 3.4 | 3.2 | 14 |
| 16 | MPC | 95% | 7.6 | 19.1 | 33.0 | 7.6 | 11.1 | 61 |
| 17 | FDS | 95% | 6.0 | 8.3 | 21.8 | 6.4 | 2.4 | 51 |
| 18 | HII | 95% | 5.5 | 18.6 | 45.0 | 8.7 | 3.7 | 54 |
| 19 | RVTY | 95% | 3.1 | 6.8 | 12.0 | 3.0 | -0.8 | 4 |
| 20 | GE | 95% | 2.8 | 4.1 | 9.4 | 1.3 | 0.1 | 18 |
| 21 | ROK | 95% | 2.7 | 5.0 | 14.6 | 2.5 | -2.2 | 0 |
| 22 | ED | 95% | 2.4 | 3.4 | 10.1 | 1.5 | -0.2 | 8 |
| 23 | MU | 95% | 2.3 | 7.2 | 1.3 | 5.0 | -0.2 | 24 |
| 24 | ICE | 95% | 2.3 | 6.7 | 18.5 | 1.3 | 1.1 | 19 |
| 25 | KO | 95% | 1.4 | 3.7 | 8.3 | 2.8 | -1.9 | 0 |
| 26 | INCY | 94% | 9.5 | 21.0 | 17.9 | 11.6 | -1.0 | 0 |
| 27 | TPL | 94% | 4.8 | 8.6 | 19.6 | 5.0 | 7.3 | 60 |
| 28 | TDG | 94% | 4.0 | 11.7 | 35.2 | 8.1 | 2.7 | 54 |
| 29 | LII | 94% | 2.7 | 5.2 | 20.2 | 2.7 | -2.1 | 23 |
| 30 | KIM | 94% | 2.6 | 4.5 | 11.2 | 1.0 | -1.5 | 13 |
| 31 | ROP | 94% | 2.5 | 4.5 | 18.5 | 3.3 | -1.4 | 2 |
| 32 | SPGI | 94% | 2.2 | 4.0 | 15.1 | -1.4 | 1.3 | 57 |
| 33 | RCL | 94% | 2.2 | 6.8 | 11.5 | 4.3 | -3.4 | 26 |
| 34 | TXT | 94% | 1.8 | 5.4 | 7.7 | 3.2 | 0.1 | 36 |
| 35 | ORLY | 94% | 1.7 | 4.5 | 23.4 | 2.4 | -2.8 | 0 |
| 36 | NVDA | 92% | 8.1 | 17.4 | 18.9 | 6.9 | 17.6 | 61 |
| 37 | BA | 92% | 3.2 | 6.7 | 11.1 | 6.2 | -0.1 | 24 |
| 38 | STX | 92% | 3.1 | 8.1 | 7.3 | 6.4 | -2.4 | 18 |
| 39 | MCK | 92% | 2.9 | 4.5 | 11.9 | 3.7 | -1.8 | 1 |
| 40 | FICO | 92% | 2.9 | 6.6 | 12.9 | 3.6 | -1.6 | 31 |

(412 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [obv_leading_breakout__broad__max-income__v002.md](symbols/broad/obv_leading_breakout__broad__max-income__v002.md) | 2.5 | 1.0 | 1.0 | -14.5 | 38.5 | 80294/50196 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,079 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
