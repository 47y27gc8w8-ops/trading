# opening_gap_daily_continuation: optimization summary

Updated 2026-11-25T09:32:57Z · backtest.py version `2da54abf60` · 31,769 parameter sets tested with this version (31,769 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: NVDA (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [opening_gap_daily_continuation__max-income__v001.md](opening_gap_daily_continuation__max-income__v001.md) | 31767 | `{"gap": 0.75, "max_candles": 24, "stop_atr": 2.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [opening_gap_daily_continuation__balanced__v001.md](opening_gap_daily_continuation__balanced__v001.md) | 31768 | `{"gap": 2.25, "max_candles": 36, "stop_atr": 3.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [opening_gap_daily_continuation__safe-starter__v001.md](opening_gap_daily_continuation__safe-starter__v001.md) | 31769 | `{"gap": 2.5, "max_candles": 72, "stop_atr": 0.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 48,623.00 | 16,898.80 | 38,804.72 | 10,236.06 | 7,705.23 | 5,137.23 |
| return % | 486.23 | 168.99 | 388.05 | 102.36 | 77.05 | 51.37 |
| return %/year | 11.3 | 9.5 | 10.1 | 6.7 | 3.5 | 3.9 |
| gross profit | 97,388.99 | 27,911.94 | 60,606.17 | 13,687.15 | 17,029.23 | 8,102.08 |
| gross loss | 48,765.99 | 11,013.15 | 21,801.44 | 3,451.09 | 9,324.00 | 2,964.86 |
| trades | 43 | 26 | 23 | 16 | 23 | 14 |
| win rate % | 46.5 | 50.0 | 52.2 | 50.0 | 30.4 | 42.9 |
| avg win | 4,869.45 | 2,147.07 | 5,050.51 | 1,710.89 | 2,432.75 | 1,350.35 |
| avg loss | -2,120.26 | -847.17 | -1,981.95 | -431.39 | -582.75 | -370.61 |
| avg result / trade | 1,130.77 | 649.95 | 1,687.16 | 639.75 | 335.01 | 366.94 |
| largest single loss | -6,340.08 | -3,766.29 | -5,950.50 | -826.32 | -1,317.05 | -716.60 |
| largest loss % of equity | -11.15 | -11.86 | -21.28 | -3.92 | -8.07 | -5.56 |
| max drawdown | -19,474.06 | -5,009.24 | -12,477.47 | -2,102.13 | -4,747.49 | -2,037.59 |
| max drawdown % | -52.72 | -15.77 | -38.35 | -13.16 | -28.16 | -14.36 |
| profit factor | 2.00 | 2.53 | 2.78 | 3.97 | 1.83 | 2.73 |
| unusually bad trades | 5 | 3 | 2 | 0 | 1 | 1 |
| … threshold (% of equity) | 7.8 | 5.8 | 7.0 | 5.1 | 7.2 | 4.8 |
| time in market % | 8.8 | 8.3 | 6.1 | 5.8 | 3.6 | 2.5 |
| buy & hold return % | 2,340.06 | 20,904.13 | 2,340.06 | 20,904.13 | 2,340.06 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.84 |  | 0.67 |  | 1.10 |
| period | 1999-06-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-06-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-06-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1999 | 29.2 | 32.4 | 21.5 |
| 2000 | 129.5 | 118.7 | 23.5 |
| 2001 | -3.4 | -3.4 | -3.4 |
| 2002 | -33.1 | -21.3 | -5.4 |
| 2003 | 13.4 | 15.7 | -11.6 |
| 2004 | 17.6 | 0.0 | 0.0 |
| 2005 | 25.9 | 27.9 | 27.0 |
| 2006 | 4.6 | 0.0 | 0.0 |
| 2007 | 3.1 | 0.0 | 0.0 |
| 2008 | 5.4 | 5.4 | 5.4 |
| 2009 | 37.5 | 40.2 | 15.4 |
| 2010 | 8.3 | -3.6 | 0.0 |
| 2011 | -7.3 | 17.0 | 0.0 |
| 2012 | -5.5 | -5.5 | -2.8 |
| 2013 | -1.1 | 0.0 | 0.0 |
| 2014 | 11.0 | 0.0 | 0.0 |
| 2015 | 11.9 | -4.9 | -2.7 |
| 2016 (OOS) | 31.3 | 18.9 | 16.6 |
| 2017 (OOS) | -0.1 | 6.9 | 9.7 |
| 2018 (OOS) | 4.0 | 14.7 | 0.0 |
| 2019 (OOS) | -0.4 | -0.5 | 0.7 |
| 2020 (OOS) | 30.5 | -3.4 | -5.6 |
| 2021 (OOS) | 14.2 | 15.6 | 14.2 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 12.3 | -2.2 | -2.2 |
| 2024 (OOS) | 23.2 | 32.9 | 14.3 |
| 2025 (OOS) | 0.0 | 0.0 | 0.0 |
| 2026 (OOS) | -3.9 | -3.9 | -2.5 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 52.7% from a peak in-sample and 15.8% out-of-sample, and the worst single trade cost 11.9% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 19% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 38.4% from a peak in-sample and 13.2% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 52 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 28.2% from a peak in-sample and 14.4% out-of-sample, and the worst single trade cost 5.6% of the account out-of-sample. About 30 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 16395 | `{"gap": 0.75, "max_candles": 24, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 48,623.00 | 11.3 | -52.7 | 46.5 | 16,898.80 | 9.5 | -15.8 | 0.84 | 43/26 | 1.00 |
| 3222 | `{"gap": 2.25, "max_candles": 24, "stop_atr": 2.75, "take_profit_atr": 5.5}` | 40,464.59 | 10.3 | -38.4 | 52.2 | 9,600.89 | 6.4 | -13.2 | 0.62 | 23/16 | not checked |
| 11900 | `{"gap": 2.25, "max_candles": 24, "stop_atr": 3.0, "take_profit_atr": 5.5}` | 40,464.59 | 10.3 | -38.4 | 52.2 | 10,236.06 | 6.7 | -13.2 | 0.65 | 23/16 | not checked |
| 31321 | `{"gap": 2.25, "max_candles": 24, "stop_atr": 0.75, "take_profit_atr": 7.0}` | 15,954.97 | 5.9 | -28.2 | 34.8 | 7,540.19 | 5.3 | -14.4 | 0.89 | 23/16 | not checked |
| 28969 | `{"gap": 2.25, "max_candles": 6, "stop_atr": 0.75, "take_profit_atr": 7.0}` | 2,655.74 | 1.4 | -25.4 | 40.0 | 3,383.34 | 2.7 | -14.4 | 1.90 | 25/16 | not checked |
| 24449 | `{"gap": 2.25, "max_candles": 6, "stop_atr": 0.75, "take_profit_atr": 1.5}` | 471.82 | 0.3 | -23.0 | 40.0 | 2,057.53 | 1.7 | -8.1 | 6.18 | 25/16 | not checked |
| 25039 | `{"gap": 1.5, "max_candles": 6, "stop_atr": 0.75, "take_profit_atr": 1.5}` | 174.57 | 0.1 | -23.0 | 37.5 | 1,362.25 | 1.2 | -12.5 | 11.80 | 40/21 | not checked |
| 25684 | `{"gap": 1.25, "max_candles": 6, "stop_atr": 0.75, "take_profit_atr": 1.5}` | 174.57 | 0.1 | -23.0 | 37.5 | 99.96 | 0.1 | -15.5 | 0.90 | 40/26 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

455 of 516 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | WDC | 100% | 5.4 | 8.5 | 10.2 | 4.8 | 2.0 | 49 |
| 2 | SAP | 100% | 1.8 | 4.1 | 10.9 | 3.2 | 0.4 | 27 |
| 3 | BBY | 98% | 3.9 | 6.5 | 12.1 | 5.0 | -0.2 | 19 |
| 4 | ISRG | 98% | 2.1 | 4.6 | 22.0 | 1.6 | -2.2 | 0 |
| 5 | ADSK | 98% | 1.9 | 4.4 | 9.5 | 2.9 | 1.6 | 14 |
| 6 | NFLX | 95% | 2.7 | 9.7 | 49.9 | 0.5 | 2.0 | 27 |
| 7 | ADBE | 88% | 1.7 | 3.6 | 16.8 | -0.2 | -0.8 | 13 |
| 8 | AKAM | 83% | 2.1 | 5.9 | -8.4 | 0.5 | 0.1 | 20 |
| 9 | IVZ | 81% | 2.8 | 4.8 | 10.2 | 3.1 | -2.6 | 0 |
| 10 | NVDA | 78% | 3.0 | 11.3 | 21.3 | 1.6 | 6.9 | 50 |
| 11 | ORCL | 78% | 2.0 | 5.1 | 14.8 | 1.4 | -0.9 | 29 |
| 12 | TSM | 78% | 1.7 | 3.4 | 11.2 | 1.6 | 1.5 | 39 |
| 13 | QCOM | 70% | 1.5 | 3.1 | 19.6 | 0.8 | 2.3 | 34 |
| 14 | GLW | 67% | 1.6 | 7.8 | 5.0 | 3.2 | 2.7 | 32 |
| 15 | INCY | 64% | 7.3 | 11.6 | 17.9 | 8.2 | 0.1 | 0 |
| 16 | ILMN | 61% | 2.6 | 5.6 | 20.4 | 3.7 | -0.5 | 14 |
| 17 | TXN | 61% | 1.1 | 3.0 | 13.8 | 1.3 | -1.8 | 3 |
| 18 | WYNN | 59% | 0.5 | 5.5 | 17.6 | 2.1 | -0.4 | 10 |
| 19 | AXON | 56% | 0.8 | 9.6 | 22.9 | -1.5 | 4.5 | 35 |
| 20 | FLEX | 56% | 0.5 | 3.4 | 8.8 | -0.4 | 2.2 | 33 |
| 21 | VTRS | 55% | 1.8 | 3.3 | 10.0 | 2.1 | -2.7 | 0 |
| 22 | RCL | 53% | 0.1 | 4.9 | 11.5 | 4.4 | -0.8 | 12 |
| 23 | TER | 50% | 0.1 | 4.3 | 4.5 | -0.4 | 3.8 | 31 |
| 24 | APH | 48% | 0.8 | 5.3 | 18.7 | 1.5 | 0.4 | 5 |
| 25 | MNST | 48% | -0.1 | 2.5 | 40.8 | 1.5 | 0.8 | 29 |
| 26 | BIIB | 47% | 0.6 | 3.8 | 37.8 | 0.6 | 0.5 | 13 |
| 27 | NTAP | 47% | 0.3 | 5.7 | 15.1 | 1.5 | 0.7 | 26 |
| 28 | INTC | 45% | 2.0 | 2.8 | 12.6 | 0.9 | 1.7 | 25 |
| 29 | TPR | 45% | 1.6 | 3.7 | 17.3 | 3.0 | 6.3 | 27 |
| 30 | LEN | 44% | 1.3 | 4.3 | 15.6 | 2.4 | -4.5 | 0 |
| 31 | CDNS | 44% | 0.4 | 2.9 | 7.5 | 1.6 | 0.1 | 4 |
| 32 | CIEN | 44% | -0.4 | 2.8 | -10.4 | 1.4 | -6.1 | 1 |
| 33 | WAT | 42% | 1.5 | 4.6 | 16.1 | 2.4 | -0.2 | 1 |
| 34 | PWR | 42% | 0.8 | 4.8 | 4.3 | 0.6 | -0.9 | 10 |
| 35 | COO | 41% | 2.3 | 3.7 | 19.3 | 2.9 | -0.7 | 0 |
| 36 | HPQ | 41% | 2.0 | 4.1 | 6.2 | 3.6 | 1.0 | 4 |
| 37 | CPRT | 41% | 1.9 | 3.0 | 16.8 | 0.8 | 1.6 | 26 |
| 38 | IBM | 41% | 1.7 | 4.5 | 11.5 | 1.5 | 1.8 | 24 |
| 39 | MDT | 41% | 1.6 | 2.0 | 13.5 | 1.0 | 0.6 | 22 |
| 40 | MGM | 39% | -0.1 | 3.1 | 6.6 | 0.3 | -5.0 | 0 |

(415 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [opening_gap_daily_continuation__broad__max-income__v002.md](symbols/broad/opening_gap_daily_continuation__broad__max-income__v002.md) | 0.9 | 0.7 | 0.7 | -5.8 | 39.2 | 22781/12254 |
| broad | balanced | [opening_gap_daily_continuation__broad__balanced__v002.md](symbols/broad/opening_gap_daily_continuation__broad__balanced__v002.md) | 0.5 | 0.2 | 0.2 | -5.3 | 45.5 | 23684/12676 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 31,769 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
