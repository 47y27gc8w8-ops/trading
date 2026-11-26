# linear_regression_residual_reversion: optimization summary

Updated 2026-11-26T04:18:23Z · backtest.py version `b3a0f0afae` · 1,476 parameter sets tested with this version (1,476 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [linear_regression_residual_reversion__max-income__v002.md](linear_regression_residual_reversion__max-income__v002.md) | 1474 | `{"max_candles": 16, "n": 140, "stop_atr": 3.0, "take_profit_atr": 4.5, "z": 1.0}` | long SPY since 2026-11-24 00:00 @ 715.364569 |
| balanced | [linear_regression_residual_reversion__balanced__v002.md](linear_regression_residual_reversion__balanced__v002.md) | 1475 | `{"max_candles": 16, "n": 140, "stop_atr": 2.75, "take_profit_atr": 4.0, "z": 1.0}` | long SPY since 2026-11-24 00:00 @ 715.364569 |
| safe-starter | [linear_regression_residual_reversion__safe-starter__v002.md](linear_regression_residual_reversion__safe-starter__v002.md) | 1476 | `{"max_candles": 24, "n": 170, "stop_atr": 2.25, "take_profit_atr": 4.0, "z": 3.0}` | long SPY since 2026-11-20 00:00 @ 713.774066 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 41,540.24 | 5,638.75 | 36,920.13 | 8,066.18 | 13,763.15 | 3,010.12 |
| return % | 415.40 | 56.39 | 369.20 | 80.66 | 137.63 | 30.10 |
| return %/year | 8.1 | 4.2 | 7.6 | 5.6 | 4.2 | 2.5 |
| gross profit | 78,815.99 | 20,732.55 | 72,956.94 | 22,207.94 | 19,073.83 | 8,383.79 |
| gross loss | 37,275.75 | 15,093.79 | 36,036.81 | 14,141.76 | 5,310.68 | 5,373.67 |
| trades | 137 | 78 | 138 | 80 | 37 | 22 |
| win rate % | 68.6 | 65.4 | 66.7 | 65.0 | 73.0 | 50.0 |
| avg win | 838.47 | 406.52 | 793.01 | 427.08 | 706.44 | 762.16 |
| avg loss | -866.88 | -559.03 | -783.41 | -505.06 | -531.07 | -488.52 |
| avg result / trade | 303.21 | 72.29 | 267.54 | 100.83 | 371.98 | 136.82 |
| largest single loss | -2,148.32 | -1,297.90 | -1,955.45 | -1,133.30 | -869.97 | -961.73 |
| largest loss % of equity | -6.49 | -11.19 | -6.13 | -7.41 | -4.40 | -8.95 |
| max drawdown | -3,938.18 | -4,228.51 | -3,482.21 | -3,670.05 | -1,371.21 | -2,530.46 |
| max drawdown % | -15.82 | -33.07 | -14.97 | -28.55 | -7.77 | -21.77 |
| profit factor | 2.11 | 1.37 | 2.02 | 1.57 | 3.59 | 1.56 |
| unusually bad trades | 1 | 3 | 1 | 2 | 0 | 1 |
| … threshold (% of equity) | 6.7 | 7.3 | 6.2 | 6.6 | 6.7 | 7.0 |
| time in market % | 28.0 | 28.3 | 27.6 | 28.1 | 10.3 | 7.0 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |  | 0.73 |  | 0.58 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 7.0 | 6.6 | 6.5 |
| 1996 | 13.3 | 13.9 | 10.7 |
| 1997 | 18.0 | 18.9 | 12.9 |
| 1998 | -2.2 | -1.2 | 0.4 |
| 1999 | 28.1 | 28.0 | 6.5 |
| 2000 | 33.7 | 27.2 | 8.1 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | -3.5 | -2.2 | 0.0 |
| 2003 | 14.7 | 14.7 | 0.0 |
| 2004 | -4.5 | -5.2 | 5.7 |
| 2005 | 3.2 | 3.9 | 4.4 |
| 2006 | 1.0 | 3.4 | -2.1 |
| 2007 | 2.8 | 3.4 | 4.2 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 19.4 | 19.3 | 0.0 |
| 2010 | 1.4 | -1.5 | 4.7 |
| 2011 | 1.2 | 2.3 | 6.7 |
| 2012 | 7.4 | -0.8 | -3.0 |
| 2013 | 7.4 | 8.3 | 9.4 |
| 2014 | 15.2 | 13.6 | 7.2 |
| 2015 | 16.5 | 16.8 | 7.9 |
| 2016 (OOS) | 7.3 | 6.2 | 0.0 |
| 2017 (OOS) | 7.0 | 6.7 | 0.0 |
| 2018 (OOS) | 0.3 | 3.0 | 1.7 |
| 2019 (OOS) | 10.7 | 9.8 | 5.1 |
| 2020 (OOS) | -6.5 | -3.6 | 7.7 |
| 2021 (OOS) | 25.7 | 25.8 | -2.4 |
| 2022 (OOS) | -6.2 | -5.9 | -2.3 |
| 2023 (OOS) | 7.9 | 7.6 | 5.3 |
| 2024 (OOS) | 9.7 | 9.9 | 6.7 |
| 2025 (OOS) | -6.7 | 3.4 | 1.8 |
| 2026 (OOS) | 0.7 | 1.0 | 3.5 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 15.8% from a peak in-sample and 33.1% out-of-sample, and the worst single trade cost 11.2% of the account out-of-sample. About 69 of every 100 trades won in-sample. Out-of-sample it earned 4.2% a year against 8.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 15.0% from a peak in-sample and 28.6% out-of-sample, and the worst single trade cost 7.4% of the account out-of-sample. About 67 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 7.8% from a peak in-sample and 21.8% out-of-sample, and the worst single trade cost 8.9% of the account out-of-sample. About 73 of every 100 trades won in-sample. Out-of-sample it earned 2.5% a year against 4.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 46% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 947 | `{"max_candles": 17, "n": 135, "stop_atr": 3.0, "take_profit_atr": 6.0, "z": 1.25}` | 42,489.58 | 8.2 | -10.3 | 69.8 | 3,470.74 | 2.8 | -33.9 | 0.34 | 116/74 | not checked |
| 775 | `{"max_candles": 17, "n": 140, "stop_atr": 3.0, "take_profit_atr": 6.0, "z": 1.5}` | 27,282.81 | 6.5 | -10.2 | 66.3 | 2,518.00 | 2.1 | -33.1 | 0.32 | 98/64 | not checked |
| 1293 | `{"max_candles": 25, "n": 175, "stop_atr": 2.25, "take_profit_atr": 6.0, "z": 3.0}` | 17,673.47 | 5.0 | -8.1 | 72.2 | 3,603.57 | 2.9 | -25.6 | 0.58 | 36/21 | not checked |
| 1299 | `{"max_candles": 20, "n": 170, "stop_atr": 2.25, "take_profit_atr": 6.0, "z": 3.0}` | 15,622.22 | 4.6 | -7.6 | 72.2 | 3,979.37 | 3.1 | -25.6 | 0.68 | 36/21 | not checked |
| 1277 | `{"max_candles": 21, "n": 170, "stop_atr": 2.25, "take_profit_atr": 6.0, "z": 3.0}` | 14,860.42 | 4.4 | -7.4 | 72.2 | 2,977.07 | 2.4 | -25.6 | 0.55 | 36/21 | not checked |
| 1391 | `{"max_candles": 21, "n": 175, "stop_atr": 2.25, "take_profit_atr": 6.0, "z": 3.0}` | 14,448.49 | 4.3 | -7.3 | 72.2 | 3,244.69 | 2.6 | -25.6 | 0.60 | 36/21 | not checked |
| 1369 | `{"max_candles": 19, "n": 170, "stop_atr": 2.25, "take_profit_atr": 6.0, "z": 3.25}` | 11,648.48 | 3.8 | -7.1 | 69.0 | 1,282.25 | 1.1 | -27.8 | 0.30 | 29/19 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

63 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ^GSPC | 100% | 2.5 | 6.2 | 7.4 | 2.4 | 1.7 | 28 |
| 2 | SPY | 99% | 2.6 | 8.1 | 9.3 | 2.6 | 1.6 | 31 |
| 3 | ^DJI | 91% | 0.9 | 3.5 | 7.5 | 0.6 | 1.2 | 26 |
| 4 | VTI | 87% | 1.6 | 5.3 | 7.1 | 1.6 | 0.8 | 31 |
| 5 | IVV | 87% | 1.1 | 5.0 | 5.3 | 0.9 | 1.5 | 38 |
| 6 | RSP | 84% | 1.9 | 6.3 | 8.2 | 1.9 | 1.0 | 30 |
| 7 | VTV | 84% | 1.5 | 6.1 | 6.8 | 1.4 | 1.8 | 39 |
| 8 | XLI | 84% | 1.5 | 5.3 | 5.7 | -0.2 | 0.3 | 44 |
| 9 | XLB | 84% | 1.5 | 6.3 | 6.1 | 0.7 | 0.4 | 31 |
| 10 | VIG | 79% | 2.0 | 5.0 | 6.2 | 2.5 | 2.7 | 40 |
| 11 | ^FTSE | 79% | 0.9 | 4.3 | 3.5 | -0.6 | 1.2 | 50 |
| 12 | XLP | 76% | 1.2 | 4.0 | 7.0 | 1.0 | 0.5 | 44 |
| 13 | VUG | 75% | 0.8 | 5.3 | 8.3 | -1.0 | -2.4 | 20 |
| 14 | SOXX | 72% | 2.0 | 7.4 | 3.7 | 1.6 | -3.1 | 39 |
| 15 | DIA | 72% | 0.8 | 3.5 | 6.4 | 0.2 | 1.1 | 24 |
| 16 | CSSMI.SW | 70% | 2.8 | 6.6 | 7.7 | 0.0 | 0.7 | 27 |
| 17 | XLE | 70% | 1.3 | 5.1 | 7.1 | -2.5 | -3.2 | 26 |
| 18 | XLY | 67% | 0.8 | 3.9 | 7.8 | 3.2 | -0.3 | 20 |
| 19 | SMH | 66% | 2.5 | 12.1 | 2.1 | 2.4 | -0.1 | 34 |
| 20 | VT | 66% | 2.4 | 8.1 | 11.9 | 2.1 | 1.3 | 33 |
| 21 | CSSPX.SW | 66% | 2.4 | 9.4 | 11.6 | 3.0 | -0.1 | 19 |
| 22 | VNQ | 64% | 2.3 | 7.3 | 7.6 | -3.6 | -1.3 | 4 |
| 23 | IWM | 64% | 1.2 | 5.7 | 7.8 | 1.9 | 1.2 | 13 |
| 24 | ^SSMI | 64% | 0.6 | 3.4 | 5.9 | -0.2 | -0.1 | 18 |
| 25 | QQQ | 64% | 0.5 | 3.5 | 2.0 | -1.4 | -0.8 | 25 |
| 26 | ^VIX | 63% | 6.9 | 20.9 | 1.2 | 9.0 | -9.3 | 18 |
| 27 | ^GDAXI | 63% | 0.5 | 3.3 | 8.1 | 0.3 | 2.6 | 32 |
| 28 | CSNDX.SW | 61% | 3.4 | 10.7 | 16.8 | 0.3 | -2.6 | 16 |
| 29 | ACWI | 60% | 1.1 | 5.5 | 10.8 | 4.4 | 2.5 | 34 |
| 30 | XLU | 57% | 1.0 | 5.6 | 6.2 | -0.6 | -3.0 | 34 |
| 31 | TQQQ | 54% | 6.2 | 36.5 | 45.7 | 2.8 | -6.5 | 13 |
| 32 | GLD | 54% | 1.5 | 5.5 | 8.3 | 1.1 | 3.7 | 29 |
| 33 | EFA | 54% | 0.4 | 3.2 | 6.0 | 3.1 | 2.3 | 34 |
| 34 | HYG | 54% | 0.4 | 3.2 | 5.0 | -1.0 | 0.0 | 9 |
| 35 | GDX | 52% | 2.6 | 11.9 | -10.5 | 0.6 | 0.4 | 27 |
| 36 | VOO | 52% | 2.3 | 10.4 | 13.1 | 3.3 | 1.6 | 21 |
| 37 | IWDA.AS | 52% | 2.3 | 6.5 | 13.5 | 2.3 | 1.5 | 30 |
| 38 | XLK | 52% | 0.3 | 4.7 | 1.2 | 0.3 | 0.8 | 24 |
| 39 | TIP | 52% | 0.1 | 2.5 | 3.8 | 0.6 | 0.2 | 2 |
| 40 | CSPX.L | 51% | 2.0 | 7.6 | 12.1 | 2.3 | 4.5 | 19 |

(23 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [linear_regression_residual_reversion__broad__max-income__v002.md](symbols/broad/linear_regression_residual_reversion__broad__max-income__v002.md) | 13.0 | 3.3 | 3.3 | -47.3 | 66.6 | 7424/6776 |
| broad | balanced | [linear_regression_residual_reversion__broad__balanced__v002.md](symbols/broad/linear_regression_residual_reversion__broad__balanced__v002.md) | 1.6 | 0.8 | 0.8 | -6.9 | 63.5 | 3780/3500 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,476 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
