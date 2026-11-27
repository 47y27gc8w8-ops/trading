# range_box_breakout: optimization summary

Updated 2026-11-25T11:40:31Z · backtest.py version `b039e0a41a` · 1,495 parameter sets tested with this version (1,495 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [range_box_breakout__max-income__v002.md](range_box_breakout__max-income__v002.md) | 1493 | `{"max_candles": 24, "n": 19, "stop_atr": 4.0, "take_profit_atr": 4.5, "width": 6.75}` | flat (data up to 2026-11-24 00:00) |
| balanced | [range_box_breakout__balanced__v002.md](range_box_breakout__balanced__v002.md) | 1494 | `{"max_candles": 48, "n": 19, "stop_atr": 4.0, "take_profit_atr": 4.5, "width": 5.25}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [range_box_breakout__safe-starter__v002.md](range_box_breakout__safe-starter__v002.md) | 1495 | `{"max_candles": 60, "n": 23, "stop_atr": 2.75, "take_profit_atr": 3.0, "width": 3.5}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 318,961.43 | 10,214.37 | 151,533.03 | 17,438.55 | 7,540.46 | 2,721.19 |
| return % | 3,189.61 | 102.14 | 1,515.33 | 174.39 | 75.40 | 27.21 |
| return %/year | 18.1 | 6.7 | 14.2 | 9.7 | 2.7 | 2.2 |
| gross profit | 588,207.66 | 40,172.55 | 258,967.57 | 43,403.48 | 14,251.35 | 4,637.49 |
| gross loss | 269,246.22 | 29,958.19 | 107,434.54 | 25,964.92 | 6,710.88 | 1,916.30 |
| trades | 129 | 81 | 116 | 64 | 25 | 12 |
| win rate % | 52.7 | 51.9 | 50.0 | 53.1 | 48.0 | 66.7 |
| avg win | 8,650.11 | 956.49 | 4,464.96 | 1,276.57 | 1,187.61 | 579.69 |
| avg loss | -4,413.87 | -768.16 | -1,852.32 | -865.50 | -516.22 | -479.07 |
| avg result / trade | 2,472.57 | 126.10 | 1,306.32 | 272.48 | 301.62 | 226.77 |
| largest single loss | -30,217.03 | -2,034.47 | -6,039.33 | -2,186.39 | -999.70 | -970.06 |
| largest loss % of equity | -8.32 | -10.11 | -5.06 | -7.70 | -6.42 | -6.89 |
| max drawdown | -59,594.65 | -5,945.15 | -16,971.15 | -8,069.82 | -2,058.34 | -1,538.66 |
| max drawdown % | -36.66 | -22.98 | -37.33 | -22.98 | -14.94 | -10.93 |
| profit factor | 2.19 | 1.34 | 2.41 | 1.67 | 2.12 | 2.42 |
| unusually bad trades | 11 | 5 | 10 | 7 | 1 | 1 |
| … threshold (% of equity) | 8.2 | 7.2 | 8.2 | 5.9 | 7.1 | 6.7 |
| time in market % | 27.0 | 37.7 | 23.9 | 32.5 | 3.6 | 4.9 |
| buy & hold return % | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.37 |  | 0.69 |  | 0.83 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 9.3 | 9.3 | 0.0 |
| 1996 | -5.3 | -15.7 | -4.3 |
| 1997 | 3.1 | -12.0 | -3.0 |
| 1998 | 56.5 | 25.0 | 11.2 |
| 1999 | 61.2 | 61.2 | 27.2 |
| 2000 | -11.8 | -11.8 | 0.0 |
| 2001 | 10.5 | 10.5 | -3.0 |
| 2002 | -7.4 | -7.4 | 5.4 |
| 2003 | 11.3 | 13.9 | -2.7 |
| 2004 | 60.5 | 46.3 | 19.3 |
| 2005 | 67.4 | 49.6 | -9.2 |
| 2006 | 31.9 | 31.9 | 6.8 |
| 2007 | 1.4 | -6.6 | 0.0 |
| 2008 | 21.4 | 21.4 | 13.1 |
| 2009 | 41.6 | 37.9 | 7.0 |
| 2010 | 23.4 | 23.2 | 0.0 |
| 2011 | 5.1 | 10.5 | 0.0 |
| 2012 | 30.1 | 15.9 | 0.0 |
| 2013 | 10.5 | 9.6 | 4.4 |
| 2014 | 5.9 | 13.3 | -3.5 |
| 2015 | -0.1 | 9.0 | -4.6 |
| 2016 (OOS) | 14.4 | 9.0 | 7.1 |
| 2017 (OOS) | 19.0 | 14.3 | 0.0 |
| 2018 (OOS) | -7.2 | -4.4 | 0.0 |
| 2019 (OOS) | 39.9 | 48.8 | 14.9 |
| 2020 (OOS) | 6.1 | 27.4 | 0.0 |
| 2021 (OOS) | 7.7 | 4.5 | 5.1 |
| 2022 (OOS) | -8.0 | 0.8 | 0.0 |
| 2023 (OOS) | 10.9 | 12.9 | 0.0 |
| 2024 (OOS) | 13.2 | 16.9 | 0.0 |
| 2025 (OOS) | -2.7 | 0.2 | 2.2 |
| 2026 (OOS) | -10.9 | -12.8 | -3.8 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 36.7% from a peak in-sample and 23.0% out-of-sample, and the worst single trade cost 10.1% of the account out-of-sample. About 53 of every 100 trades won in-sample. Out-of-sample it earned 6.7% a year against 18.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 27% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 37.3% from a peak in-sample and 23.0% out-of-sample, and the worst single trade cost 7.7% of the account out-of-sample. About 50 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 27% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 14.9% from a peak in-sample and 10.9% out-of-sample, and the worst single trade cost 6.9% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 67% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 992 | `{"max_candles": 24, "n": 19, "stop_atr": 4.0, "take_profit_atr": 4.5, "width": 6.75}` | 318,961.43 | 18.1 | -36.7 | 52.7 | 10,214.37 | 6.7 | -23.0 | 0.37 | 129/81 | 1.00 |
| 1060 | `{"max_candles": 85, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1103 | `{"max_candles": 79, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1104 | `{"max_candles": 85, "n": 30, "stop_atr": 3.5, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,295.30 | 8.5 | -20.8 | 0.59 | 83/49 | not checked |
| 1115 | `{"max_candles": 91, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1151 | `{"max_candles": 91, "n": 30, "stop_atr": 3.5, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,295.30 | 8.5 | -20.8 | 0.59 | 83/49 | not checked |
| 1158 | `{"max_candles": 73, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1214 | `{"max_candles": 67, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1216 | `{"max_candles": 97, "n": 30, "stop_atr": 3.75, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,101.63 | 8.4 | -20.8 | 0.58 | 83/49 | not checked |
| 1229 | `{"max_candles": 67, "n": 30, "stop_atr": 3.5, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,295.30 | 8.5 | -20.8 | 0.59 | 83/49 | not checked |
| 1248 | `{"max_candles": 79, "n": 30, "stop_atr": 3.5, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,295.30 | 8.5 | -20.8 | 0.59 | 83/49 | not checked |
| 1260 | `{"max_candles": 97, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1262 | `{"max_candles": 97, "n": 30, "stop_atr": 3.5, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,295.30 | 8.5 | -20.8 | 0.59 | 83/49 | not checked |
| 1270 | `{"max_candles": 85, "n": 30, "stop_atr": 3.75, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,101.63 | 8.4 | -20.8 | 0.58 | 83/49 | not checked |
| 1292 | `{"max_candles": 73, "n": 30, "stop_atr": 3.5, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,295.30 | 8.5 | -20.8 | 0.59 | 83/49 | not checked |
| 1293 | `{"max_candles": 61, "n": 30, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 13,117.28 | 8.0 | -23.0 | 0.55 | 83/49 | not checked |
| 1325 | `{"max_candles": 91, "n": 30, "stop_atr": 3.75, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,101.63 | 8.4 | -20.8 | 0.58 | 83/49 | not checked |
| 1348 | `{"max_candles": 79, "n": 30, "stop_atr": 3.75, "take_profit_atr": 4.5, "width": 6.75}` | 161,392.95 | 14.5 | -34.2 | 55.4 | 14,101.63 | 8.4 | -20.8 | 0.58 | 83/49 | not checked |
| 716 | `{"max_candles": 102, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |
| 829 | `{"max_candles": 108, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |
| 851 | `{"max_candles": 84, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |
| 974 | `{"max_candles": 90, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |
| 1064 | `{"max_candles": 79, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |
| 1098 | `{"max_candles": 85, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |
| 1141 | `{"max_candles": 109, "n": 30, "stop_atr": 2.0, "take_profit_atr": 4.5, "width": 6.5}` | 97,436.31 | 12.0 | -32.5 | 52.5 | 12,830.26 | 7.9 | -20.0 | 0.66 | 80/52 | not checked |

(8 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

455 of 516 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | MSTR | 81% | 3.9 | 22.2 | 2.1 | 5.8 | -0.8 | 23 |
| 2 | AAPL | 81% | 3.5 | 18.1 | 23.4 | 3.6 | 8.0 | 51 |
| 3 | TSCO | 81% | 3.0 | 14.4 | 22.3 | 4.7 | -0.4 | 23 |
| 4 | FICO | 81% | 3.0 | 10.7 | 12.9 | 7.3 | -1.9 | 18 |
| 5 | NDSN | 79% | 2.3 | 6.5 | 8.8 | 4.0 | -0.7 | 22 |
| 6 | COR | 78% | 3.3 | 9.2 | 20.2 | 2.3 | -1.2 | 8 |
| 7 | PM | 78% | 3.0 | 7.8 | 11.3 | 5.9 | 0.3 | 21 |
| 8 | MGM | 76% | 3.9 | 16.1 | 6.6 | 9.0 | 0.1 | 13 |
| 9 | VRSN | 76% | 2.8 | 14.9 | 14.3 | 10.3 | 5.8 | 33 |
| 10 | RMD | 76% | 2.8 | 13.2 | 22.6 | 3.5 | -2.2 | 8 |
| 11 | TPL | 75% | 3.8 | 17.5 | 19.6 | 6.5 | 9.4 | 50 |
| 12 | FDS | 75% | 3.6 | 10.5 | 20.7 | 6.7 | 1.4 | 13 |
| 13 | MO | 75% | 3.5 | 10.0 | 19.0 | 6.6 | -1.0 | 10 |
| 14 | CMS | 75% | 3.3 | 9.8 | 5.5 | 6.4 | 1.1 | 34 |
| 15 | IBM | 75% | 2.2 | 7.7 | 11.5 | 3.4 | -0.2 | 23 |
| 16 | INCY | 73% | 5.0 | 15.2 | 17.9 | 6.2 | -0.8 | 5 |
| 17 | EXPD | 73% | 2.3 | 7.0 | 19.0 | 5.9 | -6.6 | 0 |
| 18 | NOC | 72% | 1.4 | 7.7 | 14.2 | 3.5 | -0.9 | 16 |
| 19 | SYK | 72% | 1.2 | 6.0 | 16.1 | 2.1 | -4.4 | 2 |
| 20 | LYV | 70% | 3.2 | 13.3 | 1.3 | 6.8 | -0.5 | 18 |
| 21 | UHS | 70% | 2.1 | 10.2 | 19.5 | 4.0 | 3.1 | 32 |
| 22 | VMC | 70% | 2.1 | 5.7 | 10.7 | 5.0 | -2.5 | 7 |
| 23 | MOS | 70% | 2.1 | 10.4 | 2.2 | 8.7 | -9.2 | 4 |
| 24 | RCL | 69% | 2.3 | 13.6 | 11.5 | 5.6 | 7.1 | 27 |
| 25 | MNST | 69% | 2.1 | 13.7 | 40.8 | 5.6 | 4.0 | 31 |
| 26 | CME | 69% | 2.0 | 10.7 | 21.2 | 4.9 | 1.8 | 15 |
| 27 | ECL | 69% | 1.4 | 5.9 | 17.4 | 3.9 | 0.8 | 16 |
| 28 | L | 69% | 1.4 | 5.8 | 9.3 | 1.2 | -3.6 | 1 |
| 29 | BBY | 69% | 1.4 | 9.3 | 12.1 | 2.8 | -1.9 | 19 |
| 30 | HD | 69% | 1.4 | 5.0 | 14.7 | 3.7 | 2.8 | 39 |
| 31 | IDXX | 69% | 1.3 | 8.4 | 14.3 | 6.5 | 0.1 | 28 |
| 32 | MSFT | 69% | 1.2 | 7.5 | 15.5 | 0.7 | 4.5 | 36 |
| 33 | WEC | 69% | 0.7 | 4.1 | 10.9 | 0.3 | 2.6 | 24 |
| 34 | HII | 67% | 7.6 | 28.5 | 42.2 | 11.2 | 6.4 | 28 |
| 35 | NFLX | 67% | 3.3 | 20.8 | 49.9 | 12.1 | 2.5 | 18 |
| 36 | WYNN | 67% | 3.2 | 16.2 | 17.6 | 5.8 | -2.4 | 9 |
| 37 | AXON | 67% | 3.0 | 22.4 | 22.9 | 4.1 | 10.1 | 39 |
| 38 | GOOG | 67% | 2.0 | 12.1 | 20.6 | 4.9 | -1.8 | 17 |
| 39 | OKE | 67% | 2.0 | 7.9 | 13.5 | 3.1 | 9.8 | 25 |
| 40 | MCK | 67% | 1.7 | 9.0 | 12.6 | 6.3 | 2.1 | 12 |

(415 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [range_box_breakout__broad__max-income__v002.md](symbols/broad/range_box_breakout__broad__max-income__v002.md) | 4.3 | 4.1 | 4.1 | -33.0 | 32.4 | 112438/66461 |
| broad | balanced | [range_box_breakout__broad__balanced__v001.md](symbols/broad/range_box_breakout__broad__balanced__v001.md) | 0.5 | 0.4 | 0.4 | -6.3 | 48.0 | 21961/12761 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,495 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
