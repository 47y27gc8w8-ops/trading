# rsi_centerline_momentum: optimization summary

Updated 2026-11-25T10:12:21Z · backtest.py version `7e0177b6fd` · 1,028 parameter sets tested with this version (1,028 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: NVDA (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rsi_centerline_momentum__max-income__v002.md](rsi_centerline_momentum__max-income__v002.md) | 1026 | `{"level": 59, "max_candles": 180, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [rsi_centerline_momentum__balanced__v002.md](rsi_centerline_momentum__balanced__v002.md) | 1027 | `{"level": 59, "max_candles": 216, "n": 25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [rsi_centerline_momentum__safe-starter__v002.md](rsi_centerline_momentum__safe-starter__v002.md) | 1028 | `{"level": 63, "max_candles": 192, "n": 25, "stop_atr": 1.75, "take_profit_atr": 2.5}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 87,385.98 | 14,833.37 | 50,924.65 | 10,027.85 | 10,206.37 | 12,551.72 |
| return % | 873.86 | 148.33 | 509.25 | 100.28 | 102.06 | 125.52 |
| return %/year | 15.5 | 8.7 | 12.2 | 6.6 | 4.6 | 7.8 |
| gross profit | 170,794.24 | 62,556.69 | 101,518.10 | 43,856.32 | 35,361.49 | 36,301.89 |
| gross loss | 83,408.26 | 47,723.32 | 50,593.45 | 33,828.47 | 25,155.11 | 23,750.17 |
| trades | 51 | 49 | 53 | 50 | 49 | 48 |
| win rate % | 72.5 | 71.4 | 79.2 | 74.0 | 51.0 | 56.2 |
| avg win | 4,616.06 | 1,787.33 | 2,417.10 | 1,185.31 | 1,414.46 | 1,344.51 |
| avg loss | -5,957.73 | -3,408.81 | -4,599.40 | -2,602.19 | -1,048.13 | -1,130.96 |
| avg result / trade | 1,713.45 | 302.72 | 960.84 | 200.56 | 208.29 | 261.49 |
| largest single loss | -12,285.40 | -5,706.78 | -9,358.98 | -4,674.01 | -2,036.14 | -1,921.49 |
| largest loss % of equity | -16.39 | -17.94 | -19.29 | -18.86 | -9.03 | -7.07 |
| max drawdown | -37,909.10 | -15,276.67 | -12,926.22 | -11,023.15 | -5,034.97 | -6,396.69 |
| max drawdown % | -39.83 | -42.64 | -39.83 | -40.20 | -25.27 | -23.39 |
| profit factor | 2.05 | 1.31 | 2.01 | 1.30 | 1.41 | 1.53 |
| unusually bad trades | 3 | 0 | 2 | 0 | 1 | 0 |
| … threshold (% of equity) | 15.1 | 22.7 | 21.9 | 21.1 | 12.3 | 10.9 |
| time in market % | 20.9 | 26.8 | 18.4 | 23.9 | 11.4 | 14.1 |
| buy & hold return % | 476.60 | 20,904.13 | 476.60 | 20,904.13 | 476.60 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.56 |  | 0.54 |  | 1.70 |
| period | 2000-03-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-03-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-03-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | -6.3 | -9.9 | 3.3 |
| 2001 | 69.1 | 48.4 | 39.4 |
| 2002 | 0.0 | 0.0 | -8.6 |
| 2003 | 5.0 | -9.5 | -9.6 |
| 2004 | 13.4 | 6.9 | -3.0 |
| 2005 | 47.3 | 35.5 | 25.5 |
| 2006 | 113.1 | 97.7 | 24.8 |
| 2007 | 5.8 | 23.1 | -2.7 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 71.8 | 24.9 | 10.7 |
| 2010 | 0.0 | 0.0 | 12.1 |
| 2011 | 12.4 | 9.9 | -6.0 |
| 2012 | -12.5 | 12.7 | 0.0 |
| 2013 | -5.2 | -6.1 | 1.8 |
| 2014 | 4.0 | -0.3 | -7.0 |
| 2015 | -6.7 | -1.5 | 4.1 |
| 2016 (OOS) | 34.9 | 27.2 | 30.7 |
| 2017 (OOS) | 51.0 | 39.1 | 22.1 |
| 2018 (OOS) | -2.2 | -4.6 | 2.1 |
| 2019 (OOS) | 9.2 | 7.8 | 3.4 |
| 2020 (OOS) | 33.1 | 24.2 | 8.7 |
| 2021 (OOS) | -9.1 | -7.4 | -18.3 |
| 2022 (OOS) | -25.8 | -24.0 | 0.0 |
| 2023 (OOS) | 24.9 | 24.1 | 37.6 |
| 2024 (OOS) | -1.2 | -13.5 | 10.6 |
| 2025 (OOS) | 6.1 | 19.7 | -7.2 |
| 2026 (OOS) | -12.5 | -9.9 | 2.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 39.8% from a peak in-sample and 42.6% out-of-sample, and the worst single trade cost 17.9% of the account out-of-sample. About 73 of every 100 trades won in-sample. Out-of-sample it earned 8.7% a year against 15.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 23% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 39.8% from a peak in-sample and 40.2% out-of-sample, and the worst single trade cost 18.9% of the account out-of-sample. About 79 of every 100 trades won in-sample. Out-of-sample it earned 6.6% a year against 12.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 25% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 25.3% from a peak in-sample and 23.4% out-of-sample, and the worst single trade cost 7.1% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 40% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 648 | `{"level": 59, "max_candles": 168, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 649 | `{"level": 59, "max_candles": 192, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 650 | `{"level": 59, "max_candles": 180, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | 1.00 |
| 670 | `{"level": 59, "max_candles": 204, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 682 | `{"level": 59, "max_candles": 156, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 764 | `{"level": 59, "max_candles": 144, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 860 | `{"level": 59, "max_candles": 132, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 894 | `{"level": 59, "max_candles": 120, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 1020 | `{"level": 59, "max_candles": 108, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 1024 | `{"level": 59, "max_candles": 216, "n": 24, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 87,385.98 | 15.5 | -39.8 | 72.5 | 14,833.37 | 8.7 | -42.6 | 0.56 | 51/49 | not checked |
| 561 | `{"level": 59, "max_candles": 180, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 681 | `{"level": 59, "max_candles": 168, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 684 | `{"level": 59, "max_candles": 204, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 700 | `{"level": 59, "max_candles": 156, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 743 | `{"level": 59, "max_candles": 216, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 777 | `{"level": 59, "max_candles": 192, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 787 | `{"level": 59, "max_candles": 132, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 842 | `{"level": 59, "max_candles": 144, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 938 | `{"level": 59, "max_candles": 120, "n": 23, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 76,589.82 | 14.7 | -34.0 | 71.2 | 14,908.38 | 8.8 | -50.8 | 0.60 | 52/49 | not checked |
| 160 | `{"level": 60, "max_candles": 144, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 47,986.42 | 11.8 | -32.9 | 73.3 | 15,362.47 | 8.9 | -35.1 | 0.76 | 60/50 | not checked |
| 562 | `{"level": 60, "max_candles": 168, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 47,986.42 | 11.8 | -32.9 | 73.3 | 15,362.47 | 8.9 | -35.1 | 0.76 | 60/50 | not checked |
| 618 | `{"level": 60, "max_candles": 156, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 47,986.42 | 11.8 | -32.9 | 73.3 | 15,362.47 | 8.9 | -35.1 | 0.76 | 60/50 | not checked |
| 654 | `{"level": 60, "max_candles": 132, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 47,986.42 | 11.8 | -32.9 | 73.3 | 15,362.47 | 8.9 | -35.1 | 0.76 | 60/50 | not checked |
| 665 | `{"level": 60, "max_candles": 144, "n": 22, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 44,900.16 | 11.4 | -32.0 | 71.0 | 17,429.32 | 9.7 | -33.1 | 0.85 | 62/50 | not checked |
| 261 | `{"level": 63, "max_candles": 180, "n": 25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 21,240.18 | 7.5 | -30.3 | 47.5 | 52,759.13 | 18.4 | -24.5 | 2.45 | 40/44 | not checked |

(8 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

468 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TSCO | 99% | 7.6 | 15.2 | 32.5 | 6.9 | 0.5 | 36 |
| 2 | SKYD | 97% | 7.7 | 23.1 | 7.0 | 12.5 | -0.6 | 6 |
| 3 | MO | 97% | 5.8 | 12.9 | 22.4 | 3.9 | 0.2 | 19 |
| 4 | XEL | 96% | 2.3 | 7.4 | 8.8 | 3.4 | -3.2 | 24 |
| 5 | SBAC | 94% | 7.5 | 16.0 | 5.6 | 9.4 | -3.5 | 12 |
| 6 | STLD | 94% | 6.0 | 14.6 | 11.5 | 11.8 | 0.7 | 39 |
| 7 | DXCM | 94% | 6.0 | 17.5 | 21.5 | 6.0 | -1.2 | 12 |
| 8 | NOC | 94% | 4.0 | 9.7 | 16.3 | 5.0 | 2.5 | 36 |
| 9 | EFX | 94% | 3.4 | 8.6 | 15.0 | 4.8 | 0.2 | 14 |
| 10 | MNST | 93% | 8.2 | 19.7 | 48.5 | 6.7 | 4.2 | 42 |
| 11 | CI | 93% | 5.9 | 14.7 | 11.8 | 7.1 | 0.5 | 10 |
| 12 | OKE | 93% | 5.5 | 11.3 | 14.0 | 2.9 | 2.6 | 43 |
| 13 | AMP | 93% | 5.3 | 13.8 | 9.8 | 7.1 | 5.7 | 42 |
| 14 | REG | 93% | 5.1 | 12.4 | 13.7 | 8.5 | 1.0 | 19 |
| 15 | SBUX | 93% | 5.0 | 14.9 | 21.3 | 6.7 | 0.0 | 25 |
| 16 | COR | 93% | 4.5 | 12.1 | 23.9 | 4.2 | -2.6 | 15 |
| 17 | BXP | 93% | 4.3 | 9.5 | 14.8 | 5.6 | -3.5 | 2 |
| 18 | CNP | 93% | 3.4 | 7.4 | 5.6 | 6.2 | -0.3 | 31 |
| 19 | O | 93% | 3.3 | 9.3 | 17.5 | 2.9 | 2.3 | 28 |
| 20 | ALL | 93% | 2.9 | 8.7 | 8.9 | 6.8 | 2.2 | 30 |
| 21 | MAR | 93% | 2.7 | 8.1 | 10.9 | 5.6 | 1.6 | 40 |
| 22 | AEP | 93% | 2.3 | 5.3 | 8.9 | 0.7 | 3.3 | 41 |
| 23 | HAL | 91% | 5.6 | 13.1 | 4.8 | 10.6 | 11.0 | 48 |
| 24 | ON | 91% | 5.2 | 13.7 | 6.0 | 2.5 | 1.2 | 7 |
| 25 | CME | 91% | 4.2 | 17.9 | 18.2 | 6.5 | -0.3 | 32 |
| 26 | TEL | 91% | 3.5 | 11.5 | 12.1 | 3.8 | -5.5 | 9 |
| 27 | ROK | 91% | 2.8 | 10.8 | 14.0 | 2.8 | -2.5 | 21 |
| 28 | NFLX | 90% | 13.2 | 29.9 | 39.4 | 16.1 | 5.6 | 40 |
| 29 | ORLY | 90% | 7.3 | 17.0 | 21.6 | 8.8 | 2.0 | 28 |
| 30 | EQIX | 90% | 7.0 | 16.8 | 22.4 | 5.3 | -1.5 | 5 |
| 31 | GEBN.SW | 90% | 5.4 | 11.0 | 14.9 | 2.1 | -0.2 | 6 |
| 32 | KNIN.SW | 90% | 5.3 | 12.7 | 18.8 | 6.8 | 6.7 | 50 |
| 33 | SLHN.SW | 90% | 5.1 | 9.1 | -2.7 | 3.5 | 3.8 | 54 |
| 34 | SPG | 90% | 4.9 | 12.4 | 20.0 | 7.4 | 11.4 | 56 |
| 35 | COO | 90% | 4.2 | 11.7 | 14.8 | 9.3 | 3.1 | 22 |
| 36 | STZ | 90% | 4.1 | 9.6 | 21.5 | 4.3 | 1.3 | 3 |
| 37 | KIM | 90% | 3.7 | 10.7 | 10.8 | 5.9 | 1.7 | 49 |
| 38 | PM | 90% | 3.7 | 8.2 | 16.6 | 4.0 | -3.2 | 22 |
| 39 | ROST | 90% | 3.7 | 10.8 | 23.0 | 3.6 | 0.9 | 31 |
| 40 | SIKA.SW | 90% | 3.6 | 11.0 | 14.4 | 3.4 | 5.3 | 48 |

(428 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [rsi_centerline_momentum__broad__max-income__v001.md](symbols/broad/rsi_centerline_momentum__broad__max-income__v001.md) | 4.2 | 4.1 | 4.1 | -13.4 | 42.4 | 21706/16423 |
| broad | balanced | [rsi_centerline_momentum__broad__balanced__v001.md](symbols/broad/rsi_centerline_momentum__broad__balanced__v001.md) | 2.4 | 2.5 | 2.4 | -6.7 | 55.0 | 11830/9432 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,028 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
