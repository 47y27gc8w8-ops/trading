# macd_signal_cross: optimization summary

Updated 2026-11-26T06:54:08Z · backtest.py version `1299a2cc4b` · 27,799 parameter sets tested with this version (27,799 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [macd_signal_cross__max-income__v001.md](macd_signal_cross__max-income__v001.md) | 27271 | `{"max_candles": 48, "signal": 5, "stop_atr": 1.75, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [macd_signal_cross__balanced__v002.md](macd_signal_cross__balanced__v002.md) | 27799 | `{"max_candles": 112, "signal": 4, "stop_atr": 1.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 115,213.47 | 29,459.03 | 38,641.32 | 17,227.26 |
| return % | 1,152.13 | 294.59 | 386.41 | 172.27 |
| return %/year | 12.8 | 13.4 | 7.8 | 9.6 |
| gross profit | 229,468.30 | 57,632.99 | 92,879.74 | 38,290.29 |
| gross loss | 114,254.83 | 28,173.96 | 54,238.42 | 21,063.04 |
| trades | 177 | 104 | 195 | 117 |
| win rate % | 44.1 | 51.9 | 47.7 | 57.3 |
| avg win | 2,941.90 | 1,067.28 | 998.71 | 571.50 |
| avg loss | -1,154.09 | -563.48 | -531.75 | -421.26 |
| avg result / trade | 650.92 | 283.26 | 198.16 | 147.24 |
| largest single loss | -8,374.59 | -3,973.17 | -2,118.85 | -2,627.17 |
| largest loss % of equity | -7.80 | -9.03 | -5.51 | -9.03 |
| max drawdown | -15,168.32 | -6,775.58 | -5,019.25 | -4,787.43 |
| max drawdown % | -55.90 | -14.84 | -34.96 | -19.29 |
| profit factor | 2.01 | 2.05 | 1.71 | 1.82 |
| unusually bad trades | 10 | 7 | 9 | 6 |
| … threshold (% of equity) | 6.2 | 3.3 | 5.6 | 3.7 |
| time in market % | 26.0 | 33.3 | 16.4 | 17.1 |
| buy & hold return % | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.05 |  | 1.23 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | -24.2 | -16.1 |
| 1996 | -5.2 | -7.6 |
| 1997 | -11.4 | -0.4 |
| 1998 | 33.4 | -0.2 |
| 1999 | 133.6 | 38.7 |
| 2000 | -28.7 | 0.7 |
| 2001 | -12.8 | -10.2 |
| 2002 | -13.2 | 6.3 |
| 2003 | -1.2 | 1.4 |
| 2004 | 68.8 | 16.9 |
| 2005 | 48.6 | 16.8 |
| 2006 | 17.6 | 12.5 |
| 2007 | 57.5 | 60.9 |
| 2008 | 6.6 | 0.5 |
| 2009 | 19.1 | 14.0 |
| 2010 | 35.0 | 30.4 |
| 2011 | -6.8 | -3.9 |
| 2012 | 27.0 | 12.5 |
| 2013 | 10.8 | 2.8 |
| 2014 | 10.2 | 7.1 |
| 2015 | 3.0 | 6.4 |
| 2016 (OOS) | -2.6 | -3.1 |
| 2017 (OOS) | 24.3 | 19.4 |
| 2018 (OOS) | 16.4 | 10.2 |
| 2019 (OOS) | 19.5 | 20.5 |
| 2020 (OOS) | 74.2 | 42.9 |
| 2021 (OOS) | 21.4 | 5.7 |
| 2022 (OOS) | -1.3 | -8.2 |
| 2023 (OOS) | 4.1 | -0.4 |
| 2024 (OOS) | 5.9 | 8.4 |
| 2025 (OOS) | 2.9 | 17.0 |
| 2026 (OOS) | -0.9 | 1.3 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 55.9% from a peak in-sample and 14.8% out-of-sample, and the worst single trade cost 9.0% of the account out-of-sample. About 44 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 18% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 35.0% from a peak in-sample and 19.3% out-of-sample, and the worst single trade cost 9.0% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 29% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 27687 | `{"max_candles": 24, "signal": 4, "stop_atr": 1.5, "take_profit_atr": 5.5}` | 120,691.14 | 13.0 | -51.6 | 42.0 | 20,537.92 | 10.8 | -18.2 | 0.83 | 195/117 | not checked |
| 1368 | `{"max_candles": 192, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 1572 | `{"max_candles": 88, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 3650 | `{"max_candles": 168, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 4226 | `{"max_candles": 128, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 5642 | `{"max_candles": 160, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 6045 | `{"max_candles": 184, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 6452 | `{"max_candles": 144, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 7642 | `{"max_candles": 48, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 8665 | `{"max_candles": 96, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 12758 | `{"max_candles": 80, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 13771 | `{"max_candles": 112, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 15486 | `{"max_candles": 120, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 15750 | `{"max_candles": 104, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 16273 | `{"max_candles": 72, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 17590 | `{"max_candles": 64, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 20843 | `{"max_candles": 152, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 21621 | `{"max_candles": 136, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 21653 | `{"max_candles": 176, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 22857 | `{"max_candles": 56, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 30,476.03 | 13.7 | -14.7 | 1.13 | 170/97 | not checked |
| 27543 | `{"max_candles": 40, "signal": 6, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 101,092.95 | 12.2 | -50.2 | 42.9 | 31,418.34 | 13.9 | -14.7 | 1.15 | 170/97 | not checked |
| 988 | `{"max_candles": 112, "signal": 6, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 100,582.71 | 12.1 | -50.2 | 43.5 | 32,407.18 | 14.2 | -14.7 | 1.17 | 170/97 | not checked |
| 2239 | `{"max_candles": 168, "signal": 6, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 100,582.71 | 12.1 | -50.2 | 43.5 | 32,407.18 | 14.2 | -14.7 | 1.17 | 170/97 | not checked |
| 3856 | `{"max_candles": 176, "signal": 6, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 100,582.71 | 12.1 | -50.2 | 43.5 | 32,407.18 | 14.2 | -14.7 | 1.17 | 170/97 | not checked |
| 4415 | `{"max_candles": 160, "signal": 6, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 100,582.71 | 12.1 | -50.2 | 43.5 | 32,407.18 | 14.2 | -14.7 | 1.17 | 170/97 | not checked |

(242 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

469 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | AMZN | 100% | 10.7 | 14.2 | 29.1 | 12.7 | 5.2 | 27 |
| 2 | RMD | 100% | 7.2 | 11.4 | 22.9 | 7.3 | -0.9 | 5 |
| 3 | GOOG | 100% | 7.1 | 10.6 | 17.6 | 7.3 | 2.2 | 64 |
| 4 | GOOGL | 100% | 7.0 | 10.3 | 17.8 | 6.3 | 2.9 | 53 |
| 5 | ORLY | 100% | 6.1 | 8.3 | 23.4 | 5.6 | 5.1 | 38 |
| 6 | HAL | 100% | 4.9 | 8.6 | 8.8 | 7.1 | -2.2 | 10 |
| 7 | LONN.SW | 100% | 4.7 | 9.0 | 9.1 | 3.4 | -0.7 | 11 |
| 8 | SOON.SW | 100% | 3.6 | 9.2 | 16.4 | 3.5 | 2.3 | 35 |
| 9 | HCA | 98% | 10.9 | 24.5 | 34.4 | 14.4 | 1.0 | 28 |
| 10 | LVS | 98% | 9.8 | 16.8 | 2.8 | 9.9 | -1.2 | 5 |
| 11 | APTV | 98% | 6.2 | 11.3 | 39.1 | 6.0 | 1.4 | 17 |
| 12 | AAPL | 98% | 5.1 | 12.9 | 23.4 | 4.0 | 10.0 | 63 |
| 13 | COO | 98% | 4.7 | 10.5 | 19.3 | 3.8 | -0.6 | 21 |
| 14 | MOS | 98% | 4.0 | 7.5 | 2.2 | 4.8 | -2.0 | 1 |
| 15 | MO | 98% | 3.9 | 6.4 | 19.0 | 5.1 | 0.8 | 16 |
| 16 | UHS | 98% | 3.4 | 7.9 | 19.5 | 2.6 | -4.2 | 9 |
| 17 | EVRG | 98% | 2.5 | 4.3 | 7.7 | 2.5 | 3.1 | 63 |
| 18 | NFLX | 97% | 10.7 | 16.7 | 40.6 | 11.9 | 7.2 | 50 |
| 19 | AXON | 97% | 9.8 | 20.1 | 22.0 | 10.1 | 2.2 | 41 |
| 20 | MNST | 97% | 9.6 | 15.6 | 40.8 | 8.5 | 0.3 | 9 |
| 21 | NTAP | 97% | 9.5 | 14.2 | 13.5 | 9.5 | 1.4 | 39 |
| 22 | TDG | 97% | 6.3 | 12.9 | 32.9 | 5.7 | 2.0 | 17 |
| 23 | SBAC | 97% | 5.4 | 11.5 | 5.8 | 6.2 | -2.0 | 1 |
| 24 | TEL | 97% | 4.0 | 8.7 | 9.6 | 4.9 | -1.7 | 12 |
| 25 | CCI | 97% | 3.5 | 9.1 | 10.9 | 8.5 | -0.6 | 7 |
| 26 | KIM | 97% | 3.1 | 6.7 | 11.2 | 4.2 | 0.9 | 11 |
| 27 | CTSH | 97% | 2.7 | 7.5 | 33.4 | 3.6 | 3.4 | 48 |
| 28 | CPAY | 95% | 9.2 | 19.3 | 48.3 | 10.1 | 0.4 | 5 |
| 29 | ETN | 95% | 4.2 | 7.1 | 11.6 | 4.6 | 1.7 | 26 |
| 30 | ON | 95% | 3.9 | 10.0 | 4.3 | 1.9 | -5.2 | 1 |
| 31 | TSCO | 95% | 3.1 | 6.8 | 21.9 | 4.0 | 0.9 | 32 |
| 32 | CAT | 95% | 3.0 | 6.7 | 10.6 | 2.8 | 1.8 | 53 |
| 33 | STLD | 95% | 2.8 | 8.5 | 8.9 | 5.0 | 2.5 | 54 |
| 34 | HST | 95% | 2.3 | 4.9 | 6.7 | 3.0 | -2.6 | 8 |
| 35 | AEP | 95% | 0.8 | 2.8 | 8.1 | 0.3 | -1.4 | 40 |
| 36 | HII | 94% | 9.4 | 23.6 | 39.1 | 9.8 | 1.3 | 10 |
| 37 | CF | 94% | 9.3 | 15.5 | 33.1 | 9.5 | -3.0 | 14 |
| 38 | DAL | 94% | 7.5 | 13.8 | 27.1 | 9.8 | 0.6 | 14 |
| 39 | WYNN | 94% | 5.7 | 11.0 | 15.4 | 3.5 | -0.3 | 6 |
| 40 | KNIN.SW | 94% | 4.7 | 8.5 | 18.4 | 4.6 | -2.2 | 0 |

(429 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [macd_signal_cross__broad__max-income__v002.md](symbols/broad/macd_signal_cross__broad__max-income__v002.md) | 2.5 | 2.4 | 2.4 | -9.5 | 38.8 | 44467/25444 |
| broad | balanced | [macd_signal_cross__broad__balanced__v002.md](symbols/broad/macd_signal_cross__broad__balanced__v002.md) | 1.0 | 1.1 | 1.0 | -7.4 | 46.7 | 46070/26364 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 27,799 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
