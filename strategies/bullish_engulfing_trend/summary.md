# bullish_engulfing_trend: optimization summary

Updated 2026-11-26T03:32:16Z · backtest.py version `d2ea6db0b5` · 52,474 parameter sets tested with this version (52,474 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [bullish_engulfing_trend__max-income__v002.md](bullish_engulfing_trend__max-income__v002.md) | 52474 | `{"max_candles": 52, "n": 110, "stop_atr": 0.5, "take_profit_atr": 6.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [bullish_engulfing_trend__balanced__v001.md](bullish_engulfing_trend__balanced__v001.md) | 51932 | `{"max_candles": 28, "n": 110, "stop_atr": 1.0, "take_profit_atr": 1.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 10,411.53 | 3,651.77 | 2,983.46 | 859.30 |
| return % | 104.12 | 36.52 | 29.83 | 8.59 |
| return %/year | 4.6 | 2.9 | 1.6 | 0.8 |
| gross profit | 20,075.79 | 9,948.73 | 13,981.84 | 7,755.44 |
| gross loss | 9,664.27 | 6,296.96 | 10,998.38 | 6,896.14 |
| trades | 77 | 63 | 83 | 68 |
| win rate % | 24.7 | 30.2 | 45.8 | 47.1 |
| avg win | 1,056.62 | 523.62 | 367.94 | 242.36 |
| avg loss | -166.63 | -143.11 | -244.41 | -191.56 |
| avg result / trade | 135.21 | 57.96 | 35.95 | 12.64 |
| largest single loss | -353.02 | -578.75 | -738.49 | -450.72 |
| largest loss % of equity | -3.53 | -4.19 | -7.33 | -4.19 |
| max drawdown | -4,203.17 | -1,824.04 | -4,619.88 | -1,028.93 |
| max drawdown % | -40.16 | -11.79 | -38.29 | -9.96 |
| profit factor | 2.08 | 1.58 | 1.27 | 1.12 |
| unusually bad trades | 2 | 1 | 2 | 2 |
| … threshold (% of equity) | 3.2 | 2.1 | 5.1 | 3.6 |
| time in market % | 8.2 | 10.3 | 5.2 | 7.1 |
| buy & hold return % | 2,918.19 | 1,414.11 | 2,918.19 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.64 |  | 0.46 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | -9.8 | -6.6 |
| 2001 | -0.4 | 19.5 |
| 2002 | -8.6 | -5.5 |
| 2003 | -15.3 | -17.0 |
| 2004 | 32.7 | -5.2 |
| 2005 | 25.4 | 8.0 |
| 2006 | -5.1 | -7.9 |
| 2007 | 6.1 | 12.6 |
| 2008 | -3.6 | -5.5 |
| 2009 | 30.2 | 28.9 |
| 2010 | 6.3 | 6.5 |
| 2011 | -2.2 | -1.2 |
| 2012 | -2.3 | -4.4 |
| 2013 | 20.0 | 6.1 |
| 2014 | 16.6 | 8.6 |
| 2015 | -1.6 | -1.0 |
| 2016 (OOS) | -1.4 | -3.1 |
| 2017 (OOS) | 2.1 | -1.7 |
| 2018 (OOS) | 2.2 | -0.3 |
| 2019 (OOS) | 8.9 | 8.9 |
| 2020 (OOS) | 14.4 | -2.5 |
| 2021 (OOS) | 6.6 | 7.5 |
| 2022 (OOS) | -1.9 | -3.6 |
| 2023 (OOS) | 4.5 | -3.7 |
| 2024 (OOS) | 7.4 | 4.5 |
| 2025 (OOS) | -0.1 | -1.0 |
| 2026 (OOS) | -9.2 | 4.3 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 40.2% from a peak in-sample and 11.8% out-of-sample, and the worst single trade cost 4.2% of the account out-of-sample. About 25 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 25% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 38.3% from a peak in-sample and 10.0% out-of-sample, and the worst single trade cost 4.2% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 0.8% a year against 1.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 52013 | `{"max_candles": 52, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52053 | `{"max_candles": 56, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52072 | `{"max_candles": 48, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52137 | `{"max_candles": 44, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52147 | `{"max_candles": 60, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52178 | `{"max_candles": 40, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52180 | `{"max_candles": 64, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52241 | `{"max_candles": 36, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52252 | `{"max_candles": 68, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52271 | `{"max_candles": 32, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52321 | `{"max_candles": 28, "n": 100, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,430.51 | 4.6 | -40.2 | 25.0 | 3,913.24 | 3.1 | -11.8 | 0.67 | 76/62 | not checked |
| 52014 | `{"max_candles": 52, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52035 | `{"max_candles": 48, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52100 | `{"max_candles": 44, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52125 | `{"max_candles": 40, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52129 | `{"max_candles": 56, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52143 | `{"max_candles": 36, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52327 | `{"max_candles": 32, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52381 | `{"max_candles": 60, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52398 | `{"max_candles": 68, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 52428 | `{"max_candles": 64, "n": 120, "stop_atr": 0.5, "take_profit_atr": 6.5}` | 10,239.95 | 4.5 | -39.4 | 24.7 | 3,797.19 | 3.0 | -11.8 | 0.67 | 77/62 | not checked |
| 145 | `{"max_candles": 28, "n": 110, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 5,650.16 | 2.8 | -37.3 | 43.2 | 3,201.13 | 2.6 | -7.7 | 0.91 | 81/64 | 1.00 |
| 177 | `{"max_candles": 24, "n": 110, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 5,650.16 | 2.8 | -37.3 | 43.2 | 3,201.13 | 2.6 | -7.7 | 0.91 | 81/64 | not checked |
| 178 | `{"max_candles": 32, "n": 110, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 5,650.16 | 2.8 | -37.3 | 43.2 | 3,201.13 | 2.6 | -7.7 | 0.91 | 81/64 | not checked |
| 1639 | `{"max_candles": 40, "n": 110, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 5,650.16 | 2.8 | -37.3 | 43.2 | 3,201.13 | 2.6 | -7.7 | 0.91 | 81/64 | not checked |

(73 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

468 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TDG | 100% | 5.6 | 8.0 | 32.2 | 5.8 | -1.9 | 0 |
| 2 | TPL | 100% | 4.2 | 6.3 | 20.4 | 4.2 | 2.2 | 36 |
| 3 | NRG | 100% | 3.6 | 5.7 | -3.2 | 5.6 | 0.5 | 45 |
| 4 | DPZ | 100% | 3.0 | 6.5 | 24.8 | 2.4 | -1.6 | 4 |
| 5 | ADM | 100% | 1.8 | 3.0 | 9.9 | 1.7 | -2.2 | 5 |
| 6 | LHX | 100% | 1.4 | 3.7 | 14.7 | 2.2 | 1.4 | 55 |
| 7 | EQIX | 98% | 4.2 | 8.0 | 22.4 | 5.1 | 1.6 | 22 |
| 8 | LUV | 98% | 2.6 | 5.8 | 9.3 | 4.1 | -0.5 | 1 |
| 9 | ACN | 98% | 2.2 | 5.0 | 17.7 | 3.8 | -1.5 | 9 |
| 10 | MS | 98% | 0.7 | 3.3 | -2.1 | 2.1 | 0.2 | 12 |
| 11 | HST | 95% | 3.0 | 5.3 | 7.1 | 3.8 | -1.8 | 3 |
| 12 | OKE | 95% | 2.5 | 4.6 | 14.0 | 2.9 | 2.7 | 12 |
| 13 | AMZN | 95% | 1.9 | 4.0 | 14.1 | 2.5 | 3.0 | 51 |
| 14 | MNST | 94% | 3.1 | 8.4 | 48.5 | 4.4 | -1.8 | 3 |
| 15 | CMG | 94% | 3.0 | 5.8 | 25.7 | 4.2 | 0.6 | 19 |
| 16 | TEL | 94% | 2.7 | 5.6 | 12.1 | 3.3 | -5.3 | 0 |
| 17 | HCA | 92% | 3.5 | 9.6 | 36.3 | 9.5 | -0.2 | 5 |
| 18 | AXON | 92% | 2.7 | 6.6 | 29.8 | 4.2 | 4.8 | 49 |
| 19 | ROK | 92% | 1.9 | 4.3 | 14.0 | 3.9 | 1.1 | 48 |
| 20 | AZO | 92% | 1.8 | 3.9 | 21.7 | 1.9 | 0.5 | 34 |
| 21 | SWKS | 91% | 4.1 | 11.6 | 6.4 | 1.7 | -3.7 | 0 |
| 22 | SYK | 91% | 2.1 | 4.0 | 11.9 | 3.6 | -0.8 | 0 |
| 23 | SOON.SW | 91% | 1.9 | 4.7 | 21.2 | 2.1 | 1.8 | 19 |
| 24 | MO | 91% | 1.9 | 3.2 | 22.4 | 2.6 | -0.6 | 6 |
| 25 | MGM | 91% | 1.0 | 2.8 | 3.8 | 1.4 | -0.6 | 3 |
| 26 | CI | 91% | 0.6 | 2.5 | 11.8 | 0.7 | -2.7 | 2 |
| 27 | NFLX | 89% | 6.0 | 9.6 | 39.4 | 5.0 | -0.1 | 14 |
| 28 | INCY | 89% | 4.8 | 9.0 | 7.8 | 4.0 | -1.1 | 1 |
| 29 | NVDA | 89% | 3.8 | 7.1 | 11.8 | 3.3 | 4.6 | 48 |
| 30 | VRSN | 89% | 2.6 | 5.9 | -4.2 | 2.5 | 1.4 | 23 |
| 31 | PM | 89% | 2.5 | 4.9 | 16.6 | 2.6 | -1.1 | 3 |
| 32 | MSCI | 89% | 2.5 | 5.6 | 23.4 | 2.5 | 1.0 | 39 |
| 33 | WYNN | 89% | 2.2 | 6.8 | 12.2 | 0.4 | -4.6 | 0 |
| 34 | BF-B | 89% | 1.6 | 3.6 | 14.8 | 3.2 | -0.9 | 5 |
| 35 | WY | 89% | 1.2 | 4.2 | 3.8 | 1.1 | 1.9 | 50 |
| 36 | BEN | 88% | 2.3 | 6.0 | 9.7 | 1.9 | 0.8 | 52 |
| 37 | UNP | 88% | 2.0 | 3.3 | 15.1 | 1.9 | -1.2 | 0 |
| 38 | SIKA.SW | 86% | 1.2 | 3.6 | 14.4 | 1.4 | 6.0 | 55 |
| 39 | GOOG | 86% | 0.9 | 4.3 | 15.7 | 4.3 | -2.6 | 0 |
| 40 | CMI | 86% | 0.9 | 2.6 | 15.6 | 0.9 | 0.1 | 26 |

(428 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 52,474 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
