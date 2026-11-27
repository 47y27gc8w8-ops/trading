# elder_impulse_onset: optimization summary

Updated 2026-11-26T00:38:05Z · backtest.py version `10a8dc4c3f` · 862 parameter sets tested with this version (862 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: MSFT (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [elder_impulse_onset__max-income__v001.md](elder_impulse_onset__max-income__v001.md) | 351 | `{"max_candles": 104, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [elder_impulse_onset__balanced__v002.md](elder_impulse_onset__balanced__v002.md) | 862 | `{"max_candles": 160, "n": 25, "stop_atr": 3.75, "take_profit_atr": 1.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 34,190.37 | 3,348.74 | 4,095.36 | 693.78 |
| return % | 341.90 | 33.49 | 40.95 | 6.94 |
| return %/year | 7.3 | 2.7 | 1.6 | 0.6 |
| gross profit | 138,490.33 | 25,665.10 | 59,437.21 | 26,120.37 |
| gross loss | 104,299.96 | 22,316.36 | 55,341.86 | 25,426.59 |
| trades | 246 | 153 | 266 | 183 |
| win rate % | 35.0 | 34.0 | 49.6 | 50.8 |
| avg win | 1,610.35 | 493.56 | 450.28 | 280.86 |
| avg loss | -651.87 | -220.95 | -413.00 | -282.52 |
| avg result / trade | 138.99 | 21.89 | 15.40 | 3.79 |
| largest single loss | -3,035.95 | -753.79 | -1,654.18 | -1,003.37 |
| largest loss % of equity | -8.29 | -5.20 | -10.02 | -8.18 |
| max drawdown | -22,039.91 | -3,068.71 | -11,101.03 | -4,113.24 |
| max drawdown % | -50.57 | -22.63 | -57.19 | -33.52 |
| profit factor | 1.33 | 1.15 | 1.07 | 1.03 |
| unusually bad trades | 22 | 2 | 25 | 9 |
| … threshold (% of equity) | 3.9 | 3.7 | 5.0 | 4.9 |
| time in market % | 35.4 | 47.2 | 26.9 | 35.5 |
| buy & hold return % | 1,968.97 | 944.05 | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.37 |  | 0.38 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 29.9 | 8.8 |
| 1996 | 25.0 | 18.1 |
| 1997 | 9.1 | -19.1 |
| 1998 | 73.7 | 29.6 |
| 1999 | 38.7 | 7.7 |
| 2000 | -30.5 | -29.7 |
| 2001 | -19.8 | -9.0 |
| 2002 | -3.2 | -4.1 |
| 2003 | 6.3 | 19.6 |
| 2004 | 4.1 | 2.6 |
| 2005 | 0.7 | -5.8 |
| 2006 | 15.4 | 11.0 |
| 2007 | 13.9 | -1.3 |
| 2008 | -3.7 | -7.8 |
| 2009 | 12.8 | 34.6 |
| 2010 | 12.5 | 6.7 |
| 2011 | -15.2 | 2.4 |
| 2012 | 9.9 | 1.6 |
| 2013 | 10.0 | 13.8 |
| 2014 | 17.6 | -6.1 |
| 2015 | -11.1 | -15.0 |
| 2016 (OOS) | -21.5 | -8.7 |
| 2017 (OOS) | 4.2 | 8.2 |
| 2018 (OOS) | 6.4 | -6.5 |
| 2019 (OOS) | 25.2 | 6.8 |
| 2020 (OOS) | 11.9 | 9.1 |
| 2021 (OOS) | 7.3 | -16.9 |
| 2022 (OOS) | -10.1 | -3.1 |
| 2023 (OOS) | 20.0 | 18.8 |
| 2024 (OOS) | -6.5 | -2.5 |
| 2025 (OOS) | 3.6 | 10.8 |
| 2026 (OOS) | -4.5 | -4.8 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 50.6% from a peak in-sample and 22.6% out-of-sample, and the worst single trade cost 5.2% of the account out-of-sample. About 35 of every 100 trades won in-sample. Out-of-sample it earned 2.7% a year against 7.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 20% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 57.2% from a peak in-sample and 33.5% out-of-sample, and the worst single trade cost 8.2% of the account out-of-sample. About 50 of every 100 trades won in-sample. Out-of-sample it earned 0.6% a year against 1.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 17% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 310 | `{"max_candles": 104, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | 1.00 |
| 322 | `{"max_candles": 96, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 323 | `{"max_candles": 112, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 365 | `{"max_candles": 128, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 405 | `{"max_candles": 120, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 468 | `{"max_candles": 136, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 491 | `{"max_candles": 88, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 499 | `{"max_candles": 80, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 500 | `{"max_candles": 144, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 521 | `{"max_candles": 72, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 3,348.74 | 2.7 | -22.6 | 0.37 | 246/153 | not checked |
| 770 | `{"max_candles": 64, "n": 18, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 34,190.37 | 7.3 | -50.6 | 35.0 | 4,123.02 | 3.2 | -22.6 | 0.44 | 246/153 | not checked |
| 313 | `{"max_candles": 96, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 314 | `{"max_candles": 112, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 315 | `{"max_candles": 104, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | 1.00 |
| 415 | `{"max_candles": 120, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 432 | `{"max_candles": 88, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 448 | `{"max_candles": 128, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 462 | `{"max_candles": 136, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 561 | `{"max_candles": 80, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 710 | `{"max_candles": 72, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 715 | `{"max_candles": 144, "n": 17, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 32,160.14 | 7.1 | -49.6 | 34.7 | 3,307.26 | 2.7 | -23.2 | 0.38 | 251/156 | not checked |
| 435 | `{"max_candles": 104, "n": 17, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 29,718.40 | 6.8 | -49.1 | 29.9 | 2,185.32 | 1.8 | -21.7 | 0.27 | 271/169 | not checked |
| 446 | `{"max_candles": 136, "n": 17, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 29,718.40 | 6.8 | -49.1 | 29.9 | 2,185.32 | 1.8 | -21.7 | 0.27 | 271/169 | not checked |
| 449 | `{"max_candles": 120, "n": 17, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 29,718.40 | 6.8 | -49.1 | 29.9 | 2,185.32 | 1.8 | -21.7 | 0.27 | 271/169 | not checked |
| 450 | `{"max_candles": 96, "n": 17, "stop_atr": 0.75, "take_profit_atr": 6.0}` | 29,718.40 | 6.8 | -49.1 | 29.9 | 2,185.32 | 1.8 | -21.7 | 0.27 | 271/169 | not checked |

(29 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

471 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SW | 100% | 15.1 | 21.6 | 50.6 | 14.7 | -16.1 | 0 |
| 2 | JBL | 100% | 15.1 | 20.1 | 20.7 | 14.3 | 12.7 | 59 |
| 3 | CF | 100% | 14.1 | 21.1 | 30.6 | 10.2 | -2.0 | 24 |
| 4 | RCL | 100% | 9.8 | 16.5 | 11.5 | 8.9 | 10.6 | 55 |
| 5 | GRMN | 100% | 9.6 | 15.3 | 14.2 | 13.2 | 1.8 | 40 |
| 6 | URI | 100% | 8.8 | 14.1 | 7.7 | 8.0 | 2.9 | 48 |
| 7 | ON | 98% | 15.4 | 23.4 | 2.3 | 15.2 | -9.1 | 0 |
| 8 | CMG | 98% | 14.1 | 19.7 | 26.1 | 13.7 | 0.9 | 13 |
| 9 | VRSN | 98% | 12.1 | 20.4 | 14.8 | 9.0 | 0.7 | 22 |
| 10 | EQIX | 98% | 10.9 | 16.1 | 14.4 | 7.6 | -3.2 | 0 |
| 11 | STX | 98% | 10.4 | 16.5 | 5.4 | 9.7 | 13.8 | 58 |
| 12 | LYV | 98% | 8.9 | 16.2 | 1.8 | 8.2 | 4.1 | 44 |
| 13 | TSCO | 98% | 7.4 | 11.0 | 22.3 | 6.9 | 8.7 | 57 |
| 14 | MO | 98% | 7.3 | 11.7 | 19.0 | 10.3 | -2.9 | 0 |
| 15 | GOOG | 98% | 6.1 | 11.8 | 17.3 | 10.5 | -1.4 | 28 |
| 16 | INTC | 98% | 5.6 | 10.3 | 12.6 | 4.8 | 0.3 | 39 |
| 17 | NRG | 98% | 5.5 | 10.2 | -0.3 | 4.1 | -0.8 | 23 |
| 18 | A | 98% | 4.2 | 8.2 | 0.3 | 6.6 | 5.3 | 59 |
| 19 | SKYD | 97% | 10.6 | 17.4 | 8.1 | 15.4 | -4.9 | 0 |
| 20 | ILMN | 97% | 6.0 | 16.4 | 29.1 | 8.4 | -10.1 | 0 |
| 21 | CMS | 97% | 5.9 | 9.9 | 5.5 | 8.2 | 0.1 | 3 |
| 22 | APTV | 97% | 4.8 | 15.4 | 38.8 | 4.1 | -6.6 | 0 |
| 23 | CCI | 97% | 3.7 | 8.5 | 10.6 | 7.0 | -7.5 | 0 |
| 24 | AXON | 95% | 19.7 | 28.0 | 19.4 | 11.2 | 17.3 | 61 |
| 25 | APO | 95% | 9.7 | 17.5 | 15.7 | 12.0 | 6.5 | 51 |
| 26 | LYB | 95% | 5.3 | 10.2 | 28.6 | 3.6 | 2.6 | 9 |
| 27 | CI | 95% | 3.9 | 8.5 | 16.7 | 4.3 | -6.2 | 0 |
| 28 | TRGP | 94% | 15.5 | 26.3 | 0.8 | 13.0 | -2.3 | 0 |
| 29 | MPWR | 94% | 7.1 | 22.9 | 22.6 | 13.1 | 1.6 | 5 |
| 30 | GOOGL | 94% | 6.2 | 12.2 | 17.5 | 10.0 | -1.6 | 28 |
| 31 | CBRE | 94% | 5.6 | 11.7 | 10.6 | 6.0 | -0.8 | 17 |
| 32 | OKE | 94% | 5.0 | 9.9 | 13.5 | 3.1 | 2.0 | 45 |
| 33 | NVDA | 92% | 11.4 | 19.9 | 17.8 | 8.5 | 10.9 | 53 |
| 34 | PM | 92% | 5.5 | 8.1 | 15.5 | 5.8 | 1.5 | 18 |
| 35 | KDP | 92% | 5.3 | 11.4 | 33.4 | 6.8 | -2.7 | 0 |
| 36 | SYK | 92% | 4.1 | 7.7 | 16.1 | 3.0 | -2.0 | 0 |
| 37 | AMD | 92% | 4.0 | 9.8 | -6.8 | 1.3 | 8.2 | 51 |
| 38 | PH | 92% | 3.3 | 8.8 | 11.7 | 1.2 | 1.1 | 48 |
| 39 | DLTR | 92% | 3.1 | 7.6 | 20.9 | 2.8 | 0.8 | 27 |
| 40 | EQT | 92% | 2.4 | 8.1 | 12.8 | 2.7 | -12.5 | 3 |

(431 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [elder_impulse_onset__broad__max-income__v001.md](symbols/broad/elder_impulse_onset__broad__max-income__v001.md) | 4.1 | 3.0 | 3.0 | -18.2 | 33.2 | 89564/51721 |
| broad | balanced | [elder_impulse_onset__broad__balanced__v001.md](symbols/broad/elder_impulse_onset__broad__balanced__v001.md) | 1.2 | 0.9 | 0.9 | -12.7 | 49.0 | 118318/68910 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 862 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
