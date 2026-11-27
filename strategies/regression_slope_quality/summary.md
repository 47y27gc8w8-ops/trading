# regression_slope_quality: optimization summary

Updated 2026-11-25T11:57:05Z · backtest.py version `18de83232f` · 1,280 parameter sets tested with this version (1,280 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [regression_slope_quality__max-income__v002.md](regression_slope_quality__max-income__v002.md) | 1279 | `{"max_candles": 168, "n": 110, "r2": 0.34, "stop_atr": 2.75, "take_profit_atr": 10.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [regression_slope_quality__balanced__v002.md](regression_slope_quality__balanced__v002.md) | 1280 | `{"max_candles": 156, "n": 110, "r2": 0.48, "stop_atr": 3.5, "take_profit_atr": 7.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [regression_slope_quality__safe-starter__v001.md](regression_slope_quality__safe-starter__v001.md) | 335 | `{"max_candles": 144, "n": 110, "r2": 0.62, "stop_atr": 3.5, "take_profit_atr": 4.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 18,421.18 | 4,428.60 | 12,039.57 | 1,437.25 | 6,350.10 | 2,498.44 |
| return % | 184.21 | 44.29 | 120.40 | 14.37 | 63.50 | 24.98 |
| return %/year | 5.1 | 3.4 | 3.8 | 1.2 | 2.4 | 2.1 |
| gross profit | 22,397.48 | 6,440.22 | 15,175.31 | 3,385.75 | 8,099.88 | 3,723.12 |
| gross loss | 3,976.30 | 2,011.62 | 3,135.74 | 1,948.50 | 1,749.77 | 1,224.68 |
| trades | 20 | 11 | 20 | 11 | 20 | 13 |
| win rate % | 70.0 | 45.5 | 60.0 | 45.5 | 80.0 | 69.2 |
| avg win | 1,599.82 | 1,288.04 | 1,264.61 | 677.15 | 506.24 | 413.68 |
| avg loss | -662.72 | -335.27 | -391.97 | -324.75 | -437.44 | -306.17 |
| avg result / trade | 921.06 | 402.60 | 601.98 | 130.66 | 317.51 | 192.19 |
| largest single loss | -1,157.78 | -567.43 | -650.28 | -593.84 | -502.22 | -464.79 |
| largest loss % of equity | -4.02 | -4.38 | -4.38 | -5.38 | -3.25 | -4.34 |
| max drawdown | -3,692.53 | -1,170.46 | -1,399.02 | -963.54 | -935.65 | -882.16 |
| max drawdown % | -16.07 | -9.44 | -9.42 | -9.18 | -7.61 | -8.21 |
| profit factor | 5.63 | 3.20 | 4.84 | 1.74 | 4.63 | 3.04 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 6.3 | 4.8 | 6.0 | 5.6 | 6.3 | 6.0 |
| time in market % | 25.1 | 18.2 | 22.1 | 11.9 | 13.6 | 12.5 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.67 |  | 0.32 |  | 0.87 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 6.1 | 4.7 | 2.5 |
| 1996 | 5.4 | 6.5 | -0.7 |
| 1997 | 22.5 | 10.6 | 5.8 |
| 1998 | 13.6 | 8.2 | 4.4 |
| 1999 | 7.4 | 11.3 | 6.7 |
| 2000 | -7.4 | -4.4 | 0.4 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 4.5 | 0.0 | 0.0 |
| 2003 | 13.5 | 10.3 | 6.0 |
| 2004 | 4.7 | 2.3 | 2.7 |
| 2005 | -4.3 | -5.2 | -2.3 |
| 2006 | 3.0 | 3.5 | 5.8 |
| 2007 | 2.1 | -3.1 | -3.1 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 22.7 | 14.3 | 7.6 |
| 2010 | 8.0 | 2.1 | 3.2 |
| 2011 | 5.0 | 2.4 | 1.2 |
| 2012 | -1.2 | 6.3 | 1.1 |
| 2013 | 8.2 | 13.4 | 6.6 |
| 2014 | -0.7 | 0.4 | 2.6 |
| 2015 | -0.7 | -0.2 | 0.0 |
| 2016 (OOS) | -2.8 | -3.3 | -3.4 |
| 2017 (OOS) | 7.0 | 4.4 | 2.4 |
| 2018 (OOS) | -2.2 | -2.9 | 2.7 |
| 2019 (OOS) | 5.8 | 0.2 | -1.6 |
| 2020 (OOS) | 20.4 | 12.2 | 7.1 |
| 2021 (OOS) | 0.0 | 0.0 | -0.2 |
| 2022 (OOS) | 0.0 | 0.0 | -4.1 |
| 2023 (OOS) | 7.3 | 1.7 | 9.7 |
| 2024 (OOS) | 8.7 | 6.1 | 8.8 |
| 2025 (OOS) | -2.2 | -2.7 | 3.6 |
| 2026 (OOS) | -2.5 | -1.3 | -1.2 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 16.1% from a peak in-sample and 9.4% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 70 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 62% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 9.4% from a peak in-sample and 9.2% out-of-sample, and the worst single trade cost 5.4% of the account out-of-sample. About 60 of every 100 trades won in-sample. Out-of-sample it earned 1.2% a year against 3.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 7.6% from a peak in-sample and 8.2% out-of-sample, and the worst single trade cost 4.3% of the account out-of-sample. About 80 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 946 | `{"max_candles": 144, "n": 110, "r2": 0.34, "stop_atr": 2.75, "take_profit_atr": 10.5}` | 18,965.89 | 5.2 | -13.1 | 70.0 | 4,428.60 | 3.4 | -9.4 | 0.66 | 20/11 | not checked |
| 968 | `{"max_candles": 132, "n": 110, "r2": 0.34, "stop_atr": 2.75, "take_profit_atr": 10.5}` | 18,731.41 | 5.2 | -12.3 | 70.0 | 4,428.60 | 3.4 | -9.4 | 0.67 | 20/11 | not checked |
| 1256 | `{"max_candles": 144, "n": 110, "r2": 0.34, "stop_atr": 2.25, "take_profit_atr": 10.5}` | 17,867.17 | 5.0 | -11.9 | 65.0 | 4,832.73 | 3.7 | -9.4 | 0.74 | 20/11 | not checked |
| 1268 | `{"max_candles": 132, "n": 110, "r2": 0.34, "stop_atr": 2.25, "take_profit_atr": 10.5}` | 17,641.58 | 5.0 | -11.7 | 65.0 | 4,832.73 | 3.7 | -9.4 | 0.74 | 20/11 | not checked |
| 761 | `{"max_candles": 156, "n": 110, "r2": 0.4, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 16,162.87 | 4.7 | -11.1 | 63.6 | 2,354.02 | 2.0 | -10.8 | 0.42 | 22/11 | not checked |
| 762 | `{"max_candles": 180, "n": 110, "r2": 0.4, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 16,162.87 | 4.7 | -11.1 | 63.6 | 2,354.02 | 2.0 | -10.8 | 0.42 | 22/11 | not checked |
| 763 | `{"max_candles": 168, "n": 110, "r2": 0.4, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 16,162.87 | 4.7 | -11.1 | 63.6 | 2,354.02 | 2.0 | -10.8 | 0.42 | 22/11 | 1.00 |
| 853 | `{"max_candles": 192, "n": 110, "r2": 0.4, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 16,162.87 | 4.7 | -11.1 | 63.6 | 2,354.02 | 2.0 | -10.8 | 0.42 | 22/11 | not checked |
| 560 | `{"max_candles": 156, "n": 110, "r2": 0.46, "stop_atr": 3.0, "take_profit_atr": 8.5}` | 14,570.24 | 4.4 | -10.8 | 66.7 | 2,199.87 | 1.8 | -9.4 | 0.42 | 21/11 | not checked |
| 670 | `{"max_candles": 168, "n": 110, "r2": 0.46, "stop_atr": 3.0, "take_profit_atr": 8.5}` | 14,570.24 | 4.4 | -10.8 | 66.7 | 2,199.87 | 1.8 | -9.4 | 0.42 | 21/11 | not checked |
| 695 | `{"max_candles": 144, "n": 110, "r2": 0.46, "stop_atr": 3.0, "take_profit_atr": 8.5}` | 14,570.24 | 4.4 | -10.8 | 66.7 | 2,199.87 | 1.8 | -9.4 | 0.42 | 21/11 | not checked |
| 838 | `{"max_candles": 180, "n": 110, "r2": 0.46, "stop_atr": 3.0, "take_profit_atr": 8.5}` | 14,570.24 | 4.4 | -10.8 | 66.7 | 2,199.87 | 1.8 | -9.4 | 0.42 | 21/11 | not checked |
| 785 | `{"max_candles": 144, "n": 110, "r2": 0.46, "stop_atr": 2.5, "take_profit_atr": 8.5}` | 13,679.55 | 4.2 | -10.7 | 63.6 | 2,565.11 | 2.1 | -9.4 | 0.51 | 22/11 | not checked |
| 818 | `{"max_candles": 144, "n": 110, "r2": 0.46, "stop_atr": 2.25, "take_profit_atr": 8.5}` | 13,499.94 | 4.2 | -10.2 | 60.9 | 2,735.87 | 2.2 | -9.4 | 0.54 | 23/11 | not checked |
| 815 | `{"max_candles": 156, "n": 110, "r2": 0.46, "stop_atr": 3.0, "take_profit_atr": 7.0}` | 12,297.06 | 3.9 | -9.6 | 66.7 | 1,402.19 | 1.2 | -8.7 | 0.31 | 21/11 | not checked |
| 406 | `{"max_candles": 156, "n": 110, "r2": 0.48, "stop_atr": 3.5, "take_profit_atr": 7.0}` | 12,039.57 | 3.8 | -9.4 | 60.0 | 1,437.25 | 1.2 | -9.2 | 0.32 | 20/11 | 1.00 |
| 418 | `{"max_candles": 144, "n": 110, "r2": 0.48, "stop_atr": 3.5, "take_profit_atr": 7.0}` | 12,039.57 | 3.8 | -9.4 | 60.0 | 1,437.25 | 1.2 | -9.2 | 0.32 | 20/11 | not checked |
| 419 | `{"max_candles": 168, "n": 110, "r2": 0.48, "stop_atr": 3.5, "take_profit_atr": 7.0}` | 12,039.57 | 3.8 | -9.4 | 60.0 | 1,437.25 | 1.2 | -9.2 | 0.32 | 20/11 | not checked |
| 661 | `{"max_candles": 180, "n": 110, "r2": 0.48, "stop_atr": 3.5, "take_profit_atr": 7.0}` | 12,039.57 | 3.8 | -9.4 | 60.0 | 1,437.25 | 1.2 | -9.2 | 0.32 | 20/11 | not checked |
| 677 | `{"max_candles": 192, "n": 110, "r2": 0.48, "stop_atr": 3.5, "take_profit_atr": 7.0}` | 12,039.57 | 3.8 | -9.4 | 60.0 | 1,437.25 | 1.2 | -9.2 | 0.32 | 20/11 | not checked |
| 773 | `{"max_candles": 144, "n": 110, "r2": 0.44, "stop_atr": 2.25, "take_profit_atr": 6.5}` | 10,670.19 | 3.5 | -9.0 | 63.6 | 2,444.41 | 2.0 | -4.7 | 0.58 | 22/11 | not checked |
| 68 | `{"max_candles": 144, "n": 110, "r2": 0.62, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 6,350.10 | 2.4 | -7.6 | 80.0 | 2,498.44 | 2.1 | -8.2 | 0.87 | 20/13 | 1.00 |
| 82 | `{"max_candles": 132, "n": 110, "r2": 0.62, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 6,350.10 | 2.4 | -7.6 | 80.0 | 2,498.44 | 2.1 | -8.2 | 0.87 | 20/13 | not checked |
| 83 | `{"max_candles": 156, "n": 110, "r2": 0.62, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 6,350.10 | 2.4 | -7.6 | 80.0 | 2,498.44 | 2.1 | -8.2 | 0.87 | 20/13 | not checked |
| 361 | `{"max_candles": 168, "n": 110, "r2": 0.62, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 6,350.10 | 2.4 | -7.6 | 80.0 | 2,498.44 | 2.1 | -8.2 | 0.87 | 20/13 | not checked |

(6 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

48 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SPY | 75% | 1.5 | 5.1 | 9.3 | 0.5 | 0.0 | 45 |
| 2 | XLP | 48% | 1.2 | 3.1 | 6.6 | 2.2 | 1.4 | 21 |
| 3 | XLY | 46% | 1.3 | 3.8 | 7.5 | 0.0 | -0.8 | 20 |
| 4 | DIA | 45% | 1.4 | 2.8 | 6.2 | 0.3 | 0.8 | 25 |
| 5 | QQQ | 43% | 1.4 | 5.6 | 4.3 | -1.2 | 1.9 | 28 |
| 6 | XLV | 43% | 0.8 | 3.5 | 7.1 | 0.3 | -1.5 | 18 |
| 7 | IVV | 40% | 1.2 | 3.0 | 4.8 | 0.4 | 0.0 | 24 |
| 8 | XLU | 40% | 0.6 | 4.2 | 6.0 | 1.2 | -2.0 | 8 |
| 9 | VTI | 37% | 1.9 | 3.9 | 7.0 | 1.6 | -0.8 | 23 |
| 10 | EFA | 37% | 1.5 | 4.5 | 5.4 | 1.2 | 0.4 | 21 |
| 11 | XLI | 34% | 1.0 | 2.6 | 5.5 | 0.5 | -1.5 | 17 |
| 12 | XLK | 34% | 0.4 | 2.5 | 1.6 | -1.7 | 3.2 | 22 |
| 13 | VUG | 32% | 1.4 | 3.5 | 9.1 | 2.2 | 0.8 | 19 |
| 14 | XLF | 32% | 0.4 | 3.8 | 1.6 | -1.1 | 0.4 | 12 |
| 15 | IEF | 31% | 0.5 | 1.5 | 5.2 | 0.4 | 0.4 | 16 |
| 16 | AGG | 31% | 0.5 | 1.2 | 4.1 | -0.3 | 0.2 | 17 |
| 17 | IWM | 29% | 1.0 | 3.8 | 7.7 | -1.9 | -1.0 | 9 |
| 18 | LQD | 29% | 0.4 | 2.2 | 5.3 | 0.2 | -0.1 | 15 |
| 19 | EEM | 28% | 1.7 | 6.7 | 7.4 | -0.5 | -0.6 | 9 |
| 20 | RSP | 28% | 1.7 | 4.3 | 9.0 | 0.3 | -1.4 | 11 |
| 21 | VTV | 28% | 1.6 | 3.7 | 7.6 | -0.2 | 0.9 | 17 |
| 22 | TLT | 28% | 1.5 | 3.1 | 6.5 | 2.4 | 0.8 | 3 |
| 23 | SMH | 20% | 0.6 | 2.8 | 1.0 | -1.0 | 3.5 | 12 |
| 24 | SOXX | 20% | 0.2 | 3.5 | 2.9 | 0.2 | 3.2 | 13 |
| 25 | SHY | 20% | 0.0 | 0.4 | 2.1 | -0.1 | -0.1 | 1 |
| 26 | VWO | 18% | 1.7 | 4.9 | 4.3 | -1.2 | 0.2 | 10 |
| 27 | TIP | 18% | 0.8 | 1.3 | 4.2 | 0.4 | -0.1 | 6 |
| 28 | GLD | 17% | 1.4 | 4.8 | 8.7 | 2.1 | 2.8 | 11 |
| 29 | VNQ | 14% | 1.9 | 4.5 | 8.9 | -1.7 | 0.5 | 0 |
| 30 | HYG | 14% | 1.2 | 3.1 | 4.2 | -1.5 | 0.2 | 4 |
| 31 | XLB | 12% | 0.1 | 2.3 | 5.6 | -0.5 | -1.2 | 6 |
| 32 | XLE | 12% | -0.8 | 2.8 | 6.7 | 1.2 | 0.8 | 4 |
| 33 | BND | 9% | 0.4 | 0.8 | 4.3 | 0.4 | 0.1 | 5 |
| 34 | VEA | 8% | 0.8 | 2.9 | 0.9 | 0.8 | -0.4 | 5 |
| 35 | SLV | 8% | 0.2 | 6.8 | 0.6 | -1.1 | -1.4 | 3 |
| 36 | VT | 6% | 1.3 | 3.4 | 10.8 | 2.4 | 0.1 | 4 |
| 37 | ACWI | 6% | 1.2 | 3.3 | 6.4 | 1.6 | 0.0 | 4 |
| 38 | VIG | 6% | 1.1 | 2.0 | 6.6 | 1.8 | 1.1 | 4 |
| 39 | DBC | 6% | -0.1 | 2.4 | -6.2 | 0.7 | 2.0 | 2 |
| 40 | TQQQ | 3% | 3.7 | 7.8 | 55.2 | 6.7 | 8.4 | 2 |

(8 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [regression_slope_quality__broad__max-income__v002.md](symbols/broad/regression_slope_quality__broad__max-income__v002.md) | 1.6 | 2.3 | 1.6 | -8.0 | 50.3 | 545/556 |
| broad | balanced | [regression_slope_quality__broad__balanced__v002.md](symbols/broad/regression_slope_quality__broad__balanced__v002.md) | 1.0 | 1.4 | 1.0 | -4.5 | 51.0 | 539/539 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,280 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
