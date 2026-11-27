# EUR/USD London breakout: results

Data: HistData.com EURUSD 1-minute bid bars 2010-01 .. 2026-11-13, converted to UTC; days with <80 % minute coverage in the Asian or London window and US/EU DST-mismatch days excluded. Costs 1.0 pip per round trip unless stated. Sharpe: daily, annualised, 1 % risk per trade, flat days = 0.

## spec (as written)

`{"entry_mode": "touch", "entry_start": 7, "entry_end": 16, "buffer_pips": 0.0, "stop_frac": 1.0, "tp_mult": 2.0, "exit_hour": 16, "direction": "long", "min_range_pips": 0.0, "max_range_pips": 1000000000.0}`

| period | trades | win % | avg R | avg pips | PF | Sharpe | CAGR % | maxDD % | t |
|---|---|---|---|---|---|---|---|---|---|
| IS 2010-19 | 1740 | 41 | -0.073 | -1.99 | 0.88 | -0.91 | -13.39 | 76.1 | -2.8 |
| VAL 2020-23 | 625 | 43 | -0.021 | -0.38 | 0.97 | -0.25 | -4.72 | 33.1 | -0.47 |
| HOLDOUT 2024-26 | 475 | 44 | 0.021 | 0.68 | 1.07 | 0.25 | 2.69 | 18.2 | 0.42 |
| ALL | 2840 | 42 | -0.046 | -1.19 | 0.92 | -0.56 | -8.92 | 81.8 | -2.22 |

Cost sensitivity (ALL): 0.5 pip -> Sharpe -0.31, 2.0 pips -> Sharpe -1.07

Per year total R: 2010: -8.8, 2011: -17.9, 2012: -11.1, 2013: -7.8, 2014: -13.6, 2015: -24.7, 2016: -7.4, 2017: 19.0, 2018: -16.8, 2019: -38.0, 2020: 0.7, 2021: -13.7, 2022: 4.6, 2023: -4.5, 2024: -5.3, 2025: 22.1, 2026: -6.7

## best long-only (spec direction)

`{"entry_mode": "touch", "entry_start": 8, "entry_end": 9, "buffer_pips": 0.0, "stop_frac": 0.5, "tp_mult": 2.0, "exit_hour": 16, "direction": "long", "min_range_pips": 15.0, "max_range_pips": 50.0}`

| period | trades | win % | avg R | avg pips | PF | Sharpe | CAGR % | maxDD % | t |
|---|---|---|---|---|---|---|---|---|---|
| IS 2010-19 | 708 | 31 | 0.024 | -0.13 | 0.99 | 0.12 | 0.7 | 35.0 | 0.37 |
| VAL 2020-23 | 295 | 35 | 0.051 | 0.69 | 1.07 | 0.28 | 3.26 | 30.7 | 0.52 |
| HOLDOUT 2024-26 | 183 | 39 | 0.187 | 3.17 | 1.38 | 0.91 | 12.41 | 12.1 | 1.5 |
| ALL | 1186 | 33 | 0.056 | 0.58 | 1.05 | 0.28 | 3.19 | 35.0 | 1.13 |

Cost sensitivity (ALL): 0.5 pip -> Sharpe 0.46, 2.0 pips -> Sharpe -0.06

Per year total R: 2010: 20.3, 2011: -17.5, 2012: -11.2, 2013: 19.2, 2014: -20.5, 2015: -3.9, 2016: 6.5, 2017: 32.3, 2018: -16.6, 2019: 8.4, 2020: 31.1, 2021: -3.9, 2022: 2.5, 2023: -14.5, 2024: 18.1, 2025: 8.7, 2026: 7.5

## best long-only, close-confirmed

`{"entry_mode": "close15", "entry_start": 8, "entry_end": 11, "buffer_pips": 3.0, "stop_frac": 0.5, "tp_mult": 3.0, "exit_hour": 16, "direction": "long", "min_range_pips": 15.0, "max_range_pips": 50.0}`

| period | trades | win % | avg R | avg pips | PF | Sharpe | CAGR % | maxDD % | t |
|---|---|---|---|---|---|---|---|---|---|
| IS 2010-19 | 660 | 37 | -0.007 | -0.85 | 0.94 | -0.04 | -1.16 | 33.5 | -0.12 |
| VAL 2020-23 | 280 | 39 | -0.059 | -1.08 | 0.91 | -0.4 | -5.36 | 36.1 | -0.73 |
| HOLDOUT 2024-26 | 151 | 50 | 0.258 | 5.49 | 1.67 | 1.34 | 14.78 | 9.5 | 2.22 |
| ALL | 1091 | 39 | 0.016 | -0.03 | 1.0 | 0.1 | 0.46 | 47.6 | 0.39 |

Cost sensitivity (ALL): 0.5 pip -> Sharpe 0.24, 2.0 pips -> Sharpe -0.19

Per year total R: 2010: 12.9, 2011: -4.4, 2012: 14.5, 2013: 2.9, 2014: -14.4, 2015: -7.3, 2016: -0.7, 2017: 16.5, 2018: -16.9, 2019: -7.5, 2020: 10.7, 2021: -9.6, 2022: -5.3, 2023: -12.3, 2024: 11.0, 2025: 16.7, 2026: 11.2

## best both directions

`{"entry_mode": "touch", "entry_start": 8, "entry_end": 13, "buffer_pips": 0.0, "stop_frac": 0.5, "tp_mult": 0.0, "exit_hour": 16, "direction": "both", "min_range_pips": 15.0, "max_range_pips": 1000000000.0}`

| period | trades | win % | avg R | avg pips | PF | Sharpe | CAGR % | maxDD % | t |
|---|---|---|---|---|---|---|---|---|---|
| IS 2010-19 | 2121 | 34 | 0.061 | 0.58 | 1.04 | 0.46 | 9.73 | 46.4 | 1.41 |
| VAL 2020-23 | 759 | 34 | -0.009 | -0.33 | 0.97 | -0.07 | -4.94 | 42.9 | -0.14 |
| HOLDOUT 2024-26 | 515 | 36 | 0.024 | -0.02 | 1.0 | 0.21 | 2.26 | 29.4 | 0.35 |
| ALL | 3395 | 34 | 0.04 | 0.29 | 1.02 | 0.31 | 5.05 | 59.5 | 1.24 |

Cost sensitivity (ALL): 0.5 pip -> Sharpe 0.55, 2.0 pips -> Sharpe -0.17

Per year total R: 2010: 59.0, 2011: -18.1, 2012: 10.0, 2013: 8.9, 2014: 43.6, 2015: 13.9, 2016: 2.5, 2017: 50.3, 2018: -10.5, 2019: -30.8, 2020: -5.1, 2021: 11.3, 2022: -8.9, 2023: -3.9, 2024: 7.3, 2025: -4.7, 2026: 9.9

## best overall (short-only)

`{"entry_mode": "touch", "entry_start": 8, "entry_end": 13, "buffer_pips": 0.0, "stop_frac": 1.0, "tp_mult": 3.0, "exit_hour": 13, "direction": "short", "min_range_pips": 0.0, "max_range_pips": 50.0}`

| period | trades | win % | avg R | avg pips | PF | Sharpe | CAGR % | maxDD % | t |
|---|---|---|---|---|---|---|---|---|---|
| IS 2010-19 | 1198 | 51 | 0.097 | 2.93 | 1.33 | 1.14 | 12.33 | 12.0 | 3.53 |
| VAL 2020-23 | 494 | 50 | 0.009 | 0.91 | 1.11 | 0.13 | 0.81 | 24.2 | 0.24 |
| HOLDOUT 2024-26 | 384 | 49 | 0.015 | 0.15 | 1.02 | 0.2 | 1.58 | 15.0 | 0.34 |
| ALL | 2076 | 50 | 0.061 | 1.94 | 1.23 | 0.77 | 7.81 | 27.1 | 3.04 |

Cost sensitivity (ALL): 0.5 pip -> Sharpe 1.03, 2.0 pips -> Sharpe 0.23

Per year total R: 2010: 8.2, 2011: 12.2, 2012: 17.4, 2013: -0.8, 2014: 34.0, 2015: 25.5, 2016: 10.5, 2017: 2.6, 2018: 12.2, 2019: -5.2, 2020: -17.1, 2021: -3.5, 2022: 10.0, 2023: 15.1, 2024: -4.2, 2025: -2.3, 2026: 12.2

## Drift benchmarks (no breakout logic, trade every valid day)

| benchmark | IS Sharpe | VAL Sharpe | HOLDOUT Sharpe |
|---|---|---|---|
| short 08:00 -> 13:00 UTC | 0.67 | -0.14 | -0.46 |
| long 08:00 -> 13:00 UTC | -1.62 | -1.06 | -0.81 |
| short 07:00 -> 16:00 UTC | 0.51 | -0.36 | 0.02 |

## Grid summary (in-sample Sharpe, combos with >= 300 IS trades)

6912 combos. Median IS Sharpe by direction: both: -0.41, long: -0.92, short: 0.31. Max IS Sharpe overall 1.14; max long-only 0.12.
With ~7k correlated trials over 10 years, a best-of-grid IS Sharpe around 1 is roughly what noise alone can produce.
