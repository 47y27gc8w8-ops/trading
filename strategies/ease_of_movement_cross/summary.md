# ease_of_movement_cross: optimization summary

Updated 2026-11-25T23:27:13Z · backtest.py version `cd6d51b443` · 808 parameter sets tested with this version (808 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: GLD (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [ease_of_movement_cross__max-income__v002.md](ease_of_movement_cross__max-income__v002.md) | 808 | `{"max_candles": 44, "n": 23, "stop_atr": 1.75, "take_profit_atr": 6.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [ease_of_movement_cross__balanced__v001.md](ease_of_movement_cross__balanced__v001.md) | 266 | `{"max_candles": 64, "n": 25, "stop_atr": 3.25, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 7,981.31 | 3,924.82 | 6,099.72 | 2,255.40 |
| return % | 79.81 | 39.25 | 61.00 | 22.55 |
| return %/year | 5.8 | 3.1 | 4.7 | 1.9 |
| gross profit | 16,685.65 | 10,757.52 | 14,393.83 | 9,262.81 |
| gross loss | 8,704.34 | 6,832.69 | 8,294.11 | 7,007.41 |
| trades | 62 | 82 | 59 | 85 |
| win rate % | 43.5 | 36.6 | 45.8 | 38.8 |
| avg win | 617.99 | 358.58 | 533.10 | 280.69 |
| avg loss | -248.70 | -131.40 | -259.19 | -134.76 |
| avg result / trade | 128.73 | 47.86 | 103.39 | 26.53 |
| largest single loss | -751.21 | -370.27 | -832.78 | -522.78 |
| largest loss % of equity | -4.82 | -3.96 | -4.89 | -4.84 |
| max drawdown | -3,010.44 | -1,549.10 | -2,539.03 | -2,179.59 |
| max drawdown % | -14.62 | -15.32 | -13.62 | -21.64 |
| profit factor | 1.92 | 1.57 | 1.74 | 1.32 |
| unusually bad trades | 1 | 3 | 2 | 5 |
| … threshold (% of equity) | 3.4 | 2.7 | 3.2 | 2.9 |
| time in market % | 23.1 | 23.7 | 22.6 | 23.6 |
| buy & hold return % | 128.41 | 222.91 | 128.41 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.53 |  | 0.40 |
| period | 2005-09-06 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2005-09-06 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2005 | 6.0 | 7.0 |
| 2006 | 10.9 | 7.4 |
| 2007 | 19.4 | 13.3 |
| 2008 | 5.5 | 5.1 |
| 2009 | 7.4 | 2.5 |
| 2010 | 11.1 | 11.8 |
| 2011 | 9.6 | 10.0 |
| 2012 | 2.3 | 4.6 |
| 2013 | -1.9 | 0.0 |
| 2014 | -6.4 | -6.3 |
| 2015 | -1.1 | -4.6 |
| 2016 (OOS) | -10.1 | -14.0 |
| 2017 (OOS) | -1.8 | -5.3 |
| 2018 (OOS) | 1.8 | 6.5 |
| 2019 (OOS) | 1.3 | -4.5 |
| 2020 (OOS) | -1.3 | 5.6 |
| 2021 (OOS) | -2.1 | -4.3 |
| 2022 (OOS) | 2.8 | 3.6 |
| 2023 (OOS) | 6.2 | -0.3 |
| 2024 (OOS) | 3.8 | 0.8 |
| 2025 (OOS) | 27.6 | 28.1 |
| 2026 (OOS) | 9.6 | 9.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 14.6% from a peak in-sample and 15.3% out-of-sample, and the worst single trade cost 4.0% of the account out-of-sample. About 44 of every 100 trades won in-sample. Out-of-sample it earned 3.1% a year against 5.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 65% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 13.6% from a peak in-sample and 21.6% out-of-sample, and the worst single trade cost 4.8% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 1.9% a year against 4.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 46% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 751 | `{"max_candles": 56, "n": 23, "stop_atr": 1.25, "take_profit_atr": 6.5}` | 7,991.05 | 5.9 | -13.4 | 41.9 | 2,785.78 | 2.3 | -14.9 | 0.39 | 62/82 | not checked |
| 768 | `{"max_candles": 52, "n": 23, "stop_atr": 1.25, "take_profit_atr": 6.5}` | 7,991.05 | 5.9 | -13.4 | 41.9 | 2,785.78 | 2.3 | -14.9 | 0.39 | 62/82 | not checked |
| 799 | `{"max_candles": 52, "n": 23, "stop_atr": 1.25, "take_profit_atr": 7.0}` | 7,346.94 | 5.5 | -13.1 | 41.9 | 3,128.97 | 2.5 | -14.4 | 0.46 | 62/82 | not checked |
| 61 | `{"max_candles": 36, "n": 25, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 5,029.72 | 4.0 | -12.7 | 44.1 | 1,350.64 | 1.2 | -21.7 | 0.29 | 59/85 | 1.00 |
| 75 | `{"max_candles": 40, "n": 25, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 5,029.72 | 4.0 | -12.7 | 44.1 | 1,313.82 | 1.1 | -21.7 | 0.28 | 59/85 | not checked |
| 275 | `{"max_candles": 68, "n": 25, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 5,029.72 | 4.0 | -12.7 | 44.1 | 1,306.57 | 1.1 | -23.8 | 0.28 | 59/85 | not checked |
| 779 | `{"max_candles": 60, "n": 25, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 5,029.72 | 4.0 | -12.7 | 44.1 | 1,306.57 | 1.1 | -23.8 | 0.28 | 59/85 | not checked |
| 436 | `{"max_candles": 68, "n": 14, "stop_atr": 1.25, "take_profit_atr": 4.0}` | 2,923.74 | 2.5 | -12.4 | 39.1 | 2,184.03 | 1.8 | -17.7 | 0.73 | 92/112 | not checked |
| 795 | `{"max_candles": 64, "n": 14, "stop_atr": 1.25, "take_profit_atr": 4.0}` | 2,923.74 | 2.5 | -12.4 | 39.1 | 2,184.03 | 1.8 | -17.7 | 0.73 | 92/112 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

63 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 100% | 3.0 | 5.1 | 5.0 | 3.0 | -0.1 | 4 |
| 2 | ^N225 | 97% | 1.6 | 2.8 | -0.2 | 1.0 | -3.0 | 6 |
| 3 | EEM | 95% | 4.2 | 9.2 | 6.4 | 3.2 | 0.3 | 24 |
| 4 | IWDA.AS | 94% | 1.8 | 6.8 | 13.5 | 1.7 | 1.7 | 49 |
| 5 | VNQ | 89% | 2.1 | 8.7 | 7.6 | 2.6 | -0.2 | 12 |
| 6 | CSNDX.SW | 86% | 1.9 | 5.2 | 16.8 | 1.1 | 1.7 | 48 |
| 7 | EFA | 83% | 1.1 | 4.0 | 6.0 | 0.2 | -0.3 | 22 |
| 8 | ^IXIC | 81% | 2.0 | 5.5 | 9.5 | 2.8 | 2.1 | 45 |
| 9 | RSP | 81% | 1.5 | 4.2 | 8.2 | 1.1 | 2.9 | 49 |
| 10 | TQQQ | 77% | 4.4 | 16.2 | 45.7 | 9.2 | 5.8 | 44 |
| 11 | VT | 77% | 1.9 | 7.2 | 11.9 | -0.7 | 2.8 | 43 |
| 12 | ACWI | 77% | 1.2 | 5.8 | 10.8 | 0.7 | -0.8 | 27 |
| 13 | VEA | 75% | 1.5 | 7.4 | 0.0 | 0.1 | 0.1 | 24 |
| 14 | VWO | 73% | 2.1 | 10.7 | 3.3 | -0.6 | 0.7 | 22 |
| 15 | XLE | 73% | 1.5 | 3.8 | 7.1 | 3.1 | -0.9 | 10 |
| 16 | ^RUT | 73% | 1.0 | 3.6 | 7.5 | 1.0 | -2.0 | 13 |
| 17 | TLT | 73% | 1.0 | 3.7 | 6.2 | -0.4 | -1.8 | 2 |
| 18 | VTV | 73% | 0.6 | 3.0 | 6.8 | -1.0 | 1.7 | 42 |
| 19 | XLU | 73% | 0.6 | 3.2 | 6.2 | 0.9 | 0.9 | 26 |
| 20 | GLD | 70% | 1.2 | 5.8 | 8.3 | -0.6 | 2.4 | 25 |
| 21 | CSSMI.SW | 70% | 1.0 | 4.6 | 7.7 | 0.3 | 0.1 | 14 |
| 22 | IEF | 70% | 0.5 | 2.7 | 5.0 | 0.3 | -0.1 | 2 |
| 23 | VIG | 66% | 1.0 | 4.4 | 6.2 | -1.0 | 0.7 | 35 |
| 24 | SOXX | 64% | 0.6 | 6.7 | 3.7 | -0.0 | 0.4 | 34 |
| 25 | VTI | 62% | 0.9 | 5.5 | 7.1 | -0.2 | 1.2 | 39 |
| 26 | DBC | 62% | 0.7 | 3.8 | -5.8 | 2.2 | -1.6 | 26 |
| 27 | QQQ | 62% | 0.7 | 5.9 | 2.0 | -0.3 | 3.7 | 36 |
| 28 | XLI | 62% | 0.6 | 4.1 | 5.7 | -0.5 | 0.3 | 24 |
| 29 | IWM | 61% | 0.7 | 3.6 | 7.8 | 1.2 | -0.1 | 34 |
| 30 | IVV | 61% | 0.5 | 3.2 | 5.3 | 0.8 | 3.0 | 39 |
| 31 | ^GSPC | 59% | 0.5 | 2.8 | 7.4 | -0.0 | 0.4 | 33 |
| 32 | XLB | 58% | 0.3 | 3.6 | 6.1 | -1.5 | 1.3 | 10 |
| 33 | BND | 53% | 0.1 | 1.4 | 3.8 | -0.3 | -0.1 | 9 |
| 34 | AGG | 53% | 0.0 | 0.9 | 4.2 | -0.1 | -0.4 | 4 |
| 35 | ^DJI | 52% | 0.1 | 1.7 | 7.5 | 0.6 | 1.2 | 18 |
| 36 | XLK | 52% | 0.1 | 3.8 | 1.2 | 0.7 | 2.8 | 32 |
| 37 | SPY | 48% | -0.1 | 3.0 | 9.3 | 0.4 | 2.1 | 30 |
| 38 | ^GDAXI | 47% | -0.1 | 1.7 | 8.1 | -0.9 | -1.3 | 0 |
| 39 | XLF | 47% | -0.7 | 2.9 | 2.4 | -2.4 | 3.8 | 28 |
| 40 | ^SSMI | 44% | -0.1 | 1.0 | 5.9 | -0.8 | -1.5 | 7 |

(23 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [ease_of_movement_cross__broad__max-income__v002.md](symbols/broad/ease_of_movement_cross__broad__max-income__v002.md) | 1.1 | 1.2 | 1.1 | -5.8 | 34.9 | 4674/4787 |
| broad | balanced | [ease_of_movement_cross__broad__balanced__v002.md](symbols/broad/ease_of_movement_cross__broad__balanced__v002.md) | 0.5 | 0.4 | 0.4 | -6.5 | 46.2 | 5039/5212 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 808 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
