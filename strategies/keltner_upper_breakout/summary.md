# keltner_upper_breakout: optimization summary

Updated 2026-11-26T02:48:14Z · backtest.py version `dcee56cb53` · 22,887 parameter sets tested with this version (22,887 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: GLD (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [keltner_upper_breakout__max-income__v002.md](keltner_upper_breakout__max-income__v002.md) | 22886 | `{"k": 0.75, "max_candles": 24, "stop_atr": 1.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [keltner_upper_breakout__balanced__v002.md](keltner_upper_breakout__balanced__v002.md) | 22887 | `{"k": 0.75, "max_candles": 8, "stop_atr": 1.0, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [keltner_upper_breakout__safe-starter__v001.md](keltner_upper_breakout__safe-starter__v001.md) | 22284 | `{"k": 2.75, "max_candles": 64, "stop_atr": 1.25, "take_profit_atr": 3.0}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 12,133.59 | 4,711.34 | 6,291.05 | 1,371.71 | 2,907.09 | 3,013.52 |
| return % | 121.34 | 47.11 | 62.91 | 13.72 | 29.07 | 30.14 |
| return %/year | 7.8 | 3.6 | 4.8 | 1.2 | 2.5 | 2.5 |
| gross profit | 27,135.24 | 14,968.41 | 18,070.02 | 10,917.01 | 7,358.45 | 7,893.28 |
| gross loss | 15,001.65 | 10,257.07 | 11,778.97 | 9,545.30 | 4,451.36 | 4,879.76 |
| trades | 86 | 106 | 99 | 118 | 39 | 50 |
| win rate % | 38.4 | 35.9 | 46.5 | 39.0 | 41.0 | 46.0 |
| avg win | 822.28 | 393.91 | 392.83 | 237.33 | 459.90 | 343.19 |
| avg loss | -283.05 | -150.84 | -222.24 | -132.57 | -193.54 | -180.73 |
| avg result / trade | 141.09 | 44.45 | 63.55 | 11.62 | 74.54 | 60.27 |
| largest single loss | -660.20 | -567.30 | -515.84 | -435.42 | -371.73 | -381.91 |
| largest loss % of equity | -4.26 | -3.60 | -4.26 | -3.60 | -3.01 | -3.33 |
| max drawdown | -3,170.97 | -2,009.89 | -1,830.80 | -2,215.51 | -1,332.70 | -1,554.05 |
| max drawdown % | -13.99 | -17.57 | -10.39 | -20.50 | -10.01 | -12.74 |
| profit factor | 1.81 | 1.46 | 1.53 | 1.14 | 1.65 | 1.62 |
| unusually bad trades | 3 | 5 | 3 | 5 | 0 | 1 |
| … threshold (% of equity) | 2.9 | 2.6 | 3.0 | 2.6 | 3.0 | 3.0 |
| time in market % | 28.0 | 28.7 | 18.6 | 20.1 | 9.5 | 11.0 |
| buy & hold return % | 130.80 | 222.91 | 130.80 | 222.91 | 130.80 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.46 |  | 0.25 |  | 1.00 |
| period | 2005-06-24 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2005-06-24 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2005-06-24 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2005 | 7.5 | 0.9 | 2.3 |
| 2006 | 9.6 | 2.7 | 15.7 |
| 2007 | 15.8 | 10.2 | 6.1 |
| 2008 | 15.3 | 3.1 | -1.7 |
| 2009 | 27.0 | 22.7 | 2.5 |
| 2010 | 4.1 | 3.5 | 0.2 |
| 2011 | 6.5 | 8.9 | 8.8 |
| 2012 | 4.2 | 2.7 | -0.4 |
| 2013 | -1.9 | -2.5 | -2.0 |
| 2014 | 3.1 | 1.5 | 0.7 |
| 2015 | -5.3 | -1.7 | -4.8 |
| 2016 (OOS) | -7.1 | -7.6 | 0.1 |
| 2017 (OOS) | 4.2 | 4.4 | -6.1 |
| 2018 (OOS) | 0.8 | -1.0 | 0.9 |
| 2019 (OOS) | 8.1 | 4.0 | 10.3 |
| 2020 (OOS) | -2.9 | -7.2 | 7.8 |
| 2021 (OOS) | -5.3 | -3.5 | -5.0 |
| 2022 (OOS) | 7.5 | 4.9 | 10.0 |
| 2023 (OOS) | 4.7 | 3.3 | -4.5 |
| 2024 (OOS) | 1.9 | 7.7 | -5.3 |
| 2025 (OOS) | 30.1 | 13.4 | 17.6 |
| 2026 (OOS) | 1.6 | -3.5 | 3.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 14.0% from a peak in-sample and 17.6% out-of-sample, and the worst single trade cost 3.6% of the account out-of-sample. About 38 of every 100 trades won in-sample. Out-of-sample it earned 3.6% a year against 7.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 57% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 10.4% from a peak in-sample and 20.5% out-of-sample, and the worst single trade cost 3.6% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 1.2% a year against 4.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 49% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 10.0% from a peak in-sample and 12.7% out-of-sample, and the worst single trade cost 3.3% of the account out-of-sample. About 41 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 78% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 22332 | `{"k": 0.75, "max_candles": 24, "stop_atr": 1.0, "take_profit_atr": 5.5}` | 12,133.59 | 7.8 | -14.0 | 38.4 | 4,711.34 | 3.6 | -17.6 | 0.46 | 86/106 | 1.00 |
| 22868 | `{"k": 0.75, "max_candles": 17, "stop_atr": 1.0, "take_profit_atr": 7.0}` | 10,467.80 | 7.0 | -12.5 | 38.5 | 4,699.94 | 3.6 | -22.3 | 0.51 | 91/108 | not checked |
| 22742 | `{"k": 0.75, "max_candles": 12, "stop_atr": 1.0, "take_profit_atr": 6.5}` | 9,556.90 | 6.6 | -11.5 | 43.8 | 5,096.45 | 3.9 | -18.6 | 0.59 | 96/115 | not checked |
| 22348 | `{"k": 0.75, "max_candles": 12, "stop_atr": 1.0, "take_profit_atr": 5.0}` | 9,063.32 | 6.3 | -10.4 | 43.8 | 3,616.45 | 2.9 | -18.4 | 0.46 | 96/115 | not checked |
| 489 | `{"k": 2.75, "max_candles": 40, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 699 | `{"k": 2.75, "max_candles": 28, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 914 | `{"k": 2.75, "max_candles": 64, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 5852 | `{"k": 2.75, "max_candles": 36, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 8870 | `{"k": 2.75, "max_candles": 76, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 12370 | `{"k": 2.75, "max_candles": 52, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 12699 | `{"k": 2.75, "max_candles": 56, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 13575 | `{"k": 2.75, "max_candles": 92, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 15118 | `{"k": 2.75, "max_candles": 24, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 15165 | `{"k": 2.75, "max_candles": 32, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 15716 | `{"k": 2.75, "max_candles": 88, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 17316 | `{"k": 2.75, "max_candles": 48, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 17688 | `{"k": 2.75, "max_candles": 84, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 18133 | `{"k": 2.75, "max_candles": 96, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 18259 | `{"k": 2.75, "max_candles": 72, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 19387 | `{"k": 2.75, "max_candles": 44, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 20523 | `{"k": 2.75, "max_candles": 68, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 20956 | `{"k": 2.75, "max_candles": 80, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 21314 | `{"k": 2.75, "max_candles": 60, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 22395 | `{"k": 2.75, "max_candles": 89, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |
| 22414 | `{"k": 2.75, "max_candles": 41, "stop_atr": 1.25, "take_profit_atr": 2.0}` | 3,279.83 | 2.7 | -10.0 | 54.2 | 2,469.24 | 2.0 | -11.5 | 0.75 | 48/51 | not checked |

(28 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

64 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ^IXIC | 92% | 2.4 | 5.0 | 9.5 | 2.5 | 2.9 | 40 |
| 2 | ^SSMI | 86% | 1.2 | 2.9 | 5.9 | 2.4 | -0.7 | 5 |
| 3 | GLD | 82% | 2.0 | 7.8 | 8.3 | 2.3 | 4.3 | 49 |
| 4 | ^RUT | 82% | 1.3 | 3.0 | 7.5 | 0.8 | 2.8 | 14 |
| 5 | HYG | 80% | 1.6 | 6.5 | 4.4 | 1.8 | -1.1 | 3 |
| 6 | SLV | 77% | 2.5 | 9.3 | -0.5 | 0.9 | -0.3 | 30 |
| 7 | TLT | 73% | 1.1 | 7.0 | 6.3 | -1.4 | -1.8 | 9 |
| 8 | CSNDX.SW | 68% | 0.9 | 4.4 | 20.5 | 1.0 | 6.9 | 39 |
| 9 | IWDA.AS | 65% | 1.1 | 3.8 | 12.0 | 0.5 | -0.9 | 21 |
| 10 | SPY | 65% | 0.4 | 2.8 | 9.3 | 1.1 | 1.7 | 40 |
| 11 | IEF | 65% | 0.2 | 2.1 | 5.0 | -0.1 | 0.2 | 9 |
| 12 | EEM | 62% | 0.4 | 4.7 | 7.4 | -0.7 | 2.8 | 28 |
| 13 | ^N225 | 61% | 0.8 | 3.3 | -0.2 | -0.8 | 1.5 | 17 |
| 14 | ^GDAXI | 59% | 0.3 | 2.8 | 8.1 | 0.4 | -0.3 | 21 |
| 15 | QQQ | 59% | 0.2 | 3.5 | 4.1 | 2.0 | 6.1 | 31 |
| 16 | LQD | 56% | 0.1 | 1.7 | 5.2 | 0.3 | 0.1 | 19 |
| 17 | TQQQ | 52% | 1.1 | 15.5 | 52.0 | -2.9 | 6.0 | 31 |
| 18 | VUG | 48% | -0.2 | 2.4 | 8.8 | 2.2 | 4.9 | 32 |
| 19 | RSP | 47% | 0.0 | 3.1 | 8.8 | -0.0 | 1.3 | 22 |
| 20 | ^GSPC | 47% | -0.1 | 1.1 | 7.4 | 0.5 | 1.0 | 27 |
| 21 | VWO | 47% | -0.1 | 4.8 | 4.3 | -0.5 | 0.3 | 13 |
| 22 | XLK | 44% | 0.1 | 2.8 | 1.5 | -0.5 | 4.3 | 29 |
| 23 | ^DJI | 42% | -0.1 | 1.1 | 7.5 | 0.8 | 2.6 | 16 |
| 24 | SCHD | 41% | 0.7 | 4.0 | 13.7 | 0.7 | 1.0 | 26 |
| 25 | VWRL.SW | 41% | 0.1 | 5.5 | 7.6 | 1.3 | -0.6 | 5 |
| 26 | EFA | 38% | -0.4 | 1.4 | 5.6 | 1.3 | -0.7 | 10 |
| 27 | DBC | 38% | -0.6 | 3.1 | -5.5 | -1.0 | 0.5 | 25 |
| 28 | AGG | 36% | -0.1 | 1.1 | 4.3 | -0.0 | -0.2 | 7 |
| 29 | CSSMI.SW | 35% | -0.2 | 2.1 | 4.3 | 1.6 | -0.2 | 11 |
| 30 | VNQ | 35% | -0.5 | 4.1 | 8.4 | 2.3 | -1.0 | 0 |
| 31 | VT | 33% | -0.8 | 3.8 | 12.1 | -0.9 | -0.3 | 17 |
| 32 | IWM | 32% | -0.3 | 3.5 | 7.0 | -3.0 | 1.7 | 3 |
| 33 | VOO | 32% | -0.7 | 3.8 | 11.9 | 0.8 | 1.9 | 21 |
| 34 | XLV | 30% | -0.6 | 1.5 | 7.2 | 1.0 | 0.4 | 10 |
| 35 | DIA | 29% | -0.4 | 1.0 | 6.5 | 0.4 | 2.8 | 11 |
| 36 | VTV | 26% | -0.4 | 2.4 | 7.2 | -0.7 | 1.1 | 10 |
| 37 | XLP | 23% | -1.0 | 0.5 | 6.7 | 0.3 | 1.6 | 3 |
| 38 | VTI | 20% | -0.3 | 1.0 | 7.1 | -1.2 | 1.0 | 11 |
| 39 | CSSPX.SW | 20% | -0.7 | 2.1 | 12.6 | 1.4 | 3.0 | 12 |
| 40 | USMV | 15% | 0.0 | 2.1 | 14.2 | 1.9 | 1.4 | 10 |

(24 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [keltner_upper_breakout__broad__max-income__v002.md](symbols/broad/keltner_upper_breakout__broad__max-income__v002.md) | 0.4 | 3.1 | 0.4 | -11.6 | 36.7 | 4806/4431 |
| broad | balanced | [keltner_upper_breakout__broad__balanced__v001.md](symbols/broad/keltner_upper_breakout__broad__balanced__v001.md) | 0.0 | 0.0 | 0.0 | -5.5 | 47.8 | 1316/1629 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 22,887 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
