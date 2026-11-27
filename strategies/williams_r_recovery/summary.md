# williams_r_recovery: optimization summary

Updated 2026-11-25T23:37:51Z · backtest.py version `14edac6745` · 1,733 parameter sets tested with this version (1,733 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [williams_r_recovery__max-income__v004.md](williams_r_recovery__max-income__v004.md) | 1733 | `{"level": -89, "max_candles": 10, "n": 10, "stop_atr": 4.5, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [williams_r_recovery__balanced__v002.md](williams_r_recovery__balanced__v002.md) | 1039 | `{"level": -94, "max_candles": 24, "n": 26, "stop_atr": 2.0, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [williams_r_recovery__safe-starter__v002.md](williams_r_recovery__safe-starter__v002.md) | 1040 | `{"level": -94, "max_candles": 12, "n": 28, "stop_atr": 2.0, "take_profit_atr": 4.5}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 15,591.54 | 2,249.36 | 7,623.20 | 1,527.74 | 4,144.77 | 2,458.76 |
| return % | 155.92 | 22.49 | 76.23 | 15.28 | 41.45 | 24.59 |
| return %/year | 6.2 | 1.9 | 3.7 | 1.3 | 2.2 | 2.0 |
| gross profit | 24,484.83 | 11,787.08 | 11,863.20 | 7,246.54 | 7,140.35 | 7,325.64 |
| gross loss | 8,893.29 | 9,537.72 | 4,240.00 | 5,718.80 | 2,995.58 | 4,866.88 |
| trades | 84 | 65 | 33 | 27 | 28 | 26 |
| win rate % | 75.0 | 63.1 | 69.7 | 55.6 | 67.9 | 65.4 |
| avg win | 388.65 | 287.49 | 515.79 | 483.10 | 375.81 | 430.92 |
| avg loss | -423.49 | -397.41 | -424.00 | -476.57 | -332.84 | -540.76 |
| avg result / trade | 185.61 | 34.61 | 231.01 | 56.58 | 148.03 | 94.57 |
| largest single loss | -1,733.93 | -1,618.23 | -650.07 | -860.90 | -560.83 | -860.90 |
| largest loss % of equity | -8.68 | -12.96 | -4.80 | -8.80 | -4.80 | -8.80 |
| max drawdown | -2,805.39 | -3,128.40 | -939.33 | -2,824.82 | -835.47 | -2,824.82 |
| max drawdown % | -13.96 | -24.01 | -6.99 | -24.49 | -7.15 | -24.49 |
| profit factor | 2.75 | 1.24 | 2.80 | 1.27 | 2.38 | 1.50 |
| unusually bad trades | 2 | 7 | 0 | 2 | 0 | 1 |
| … threshold (% of equity) | 4.9 | 4.7 | 6.1 | 7.1 | 5.9 | 7.9 |
| time in market % | 13.8 | 15.7 | 8.7 | 7.7 | 5.9 | 6.4 |
| buy & hold return % | 36.87 | 541.70 | 36.87 | 541.70 | 36.87 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.30 |  | 0.35 |  | 0.91 |
| period | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | -0.5 | 0.0 | 0.0 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 | 0.0 |
| 2003 | 36.1 | 5.0 | 0.0 |
| 2004 | -1.2 | 5.9 | 2.5 |
| 2005 | 2.8 | 5.6 | 1.5 |
| 2006 | -0.8 | 1.7 | 1.7 |
| 2007 | 5.9 | 11.0 | 5.9 |
| 2008 | 3.4 | 0.0 | 0.0 |
| 2009 | 22.0 | 5.3 | 0.0 |
| 2010 | 7.2 | 5.0 | 3.1 |
| 2011 | -5.9 | -2.7 | -2.7 |
| 2012 | -6.1 | -2.7 | -2.7 |
| 2013 | 16.5 | 7.9 | 7.9 |
| 2014 | 10.1 | 12.5 | 14.7 |
| 2015 | 15.4 | 4.6 | 4.6 |
| 2016 (OOS) | -1.3 | 3.6 | 3.6 |
| 2017 (OOS) | 9.0 | 4.1 | 4.1 |
| 2018 (OOS) | 2.7 | 2.7 | 2.7 |
| 2019 (OOS) | 9.4 | 1.5 | 1.5 |
| 2020 (OOS) | -10.9 | -20.7 | -20.7 |
| 2021 (OOS) | 3.4 | 16.3 | 12.5 |
| 2022 (OOS) | -8.4 | 0.0 | 0.0 |
| 2023 (OOS) | 10.0 | 11.2 | 16.9 |
| 2024 (OOS) | 12.1 | -2.8 | -2.3 |
| 2025 (OOS) | -4.7 | 1.4 | 0.8 |
| 2026 (OOS) | 2.1 | 1.6 | 7.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 14.0% from a peak in-sample and 24.0% out-of-sample, and the worst single trade cost 13.0% of the account out-of-sample. About 75 of every 100 trades won in-sample. Out-of-sample it earned 1.9% a year against 6.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 42% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 7.0% from a peak in-sample and 24.5% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 1.3% a year against 3.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 7.2% from a peak in-sample and 24.5% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 68 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1456 | `{"level": -89, "max_candles": 10, "n": 10, "stop_atr": 4.5, "take_profit_atr": 5.0}` | 15,591.54 | 6.2 | -14.0 | 75.0 | 2,249.36 | 1.9 | -24.0 | 0.30 | 84/65 | 1.00 |
| 1349 | `{"level": -88, "max_candles": 12, "n": 10, "stop_atr": 4.5, "take_profit_atr": 5.0}` | 15,325.88 | 6.1 | -12.8 | 79.1 | 2,064.10 | 1.7 | -21.7 | 0.28 | 86/65 | not checked |
| 896 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 10,837.21 | 4.8 | -10.6 | 83.9 | 3,161.19 | 2.6 | -21.7 | 0.53 | 31/22 | not checked |
| 902 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 10,837.21 | 4.8 | -10.6 | 83.9 | 3,161.19 | 2.6 | -21.7 | 0.53 | 31/22 | not checked |
| 1015 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 10,837.21 | 4.8 | -10.6 | 83.9 | 3,161.19 | 2.6 | -21.7 | 0.53 | 31/22 | not checked |
| 1159 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 10,837.21 | 4.8 | -10.6 | 83.9 | 3,161.19 | 2.6 | -21.7 | 0.53 | 31/22 | not checked |
| 926 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 3.75, "take_profit_atr": 7.0}` | 10,691.38 | 4.8 | -10.3 | 83.9 | 3,280.03 | 2.6 | -21.7 | 0.56 | 31/22 | not checked |
| 1055 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 3.75, "take_profit_atr": 6.5}` | 10,691.38 | 4.8 | -10.3 | 83.9 | 3,280.03 | 2.6 | -21.7 | 0.56 | 31/22 | not checked |
| 1098 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 10,691.38 | 4.8 | -10.3 | 83.9 | 3,280.03 | 2.6 | -21.7 | 0.56 | 31/22 | not checked |
| 1134 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 10,691.38 | 4.8 | -10.3 | 83.9 | 3,280.03 | 2.6 | -21.7 | 0.56 | 31/22 | not checked |
| 1234 | `{"level": -92, "max_candles": 26, "n": 26, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 9,180.41 | 4.3 | -9.4 | 76.5 | 1,630.26 | 1.4 | -26.2 | 0.33 | 34/27 | not checked |
| 577 | `{"level": -94, "max_candles": 20, "n": 24, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 8,240.41 | 3.9 | -8.4 | 69.4 | 1,492.37 | 1.3 | -25.9 | 0.33 | 36/28 | not checked |
| 697 | `{"level": -94, "max_candles": 20, "n": 24, "stop_atr": 2.0, "take_profit_atr": 6.5}` | 8,240.41 | 3.9 | -8.4 | 69.4 | 1,492.37 | 1.3 | -25.9 | 0.33 | 36/28 | not checked |
| 730 | `{"level": -94, "max_candles": 20, "n": 24, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 8,240.41 | 3.9 | -8.4 | 69.4 | 1,492.37 | 1.3 | -25.9 | 0.33 | 36/28 | not checked |
| 876 | `{"level": -94, "max_candles": 20, "n": 24, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 8,240.41 | 3.9 | -8.4 | 69.4 | 1,492.37 | 1.3 | -25.9 | 0.33 | 36/28 | not checked |
| 720 | `{"level": -94, "max_candles": 18, "n": 24, "stop_atr": 2.0, "take_profit_atr": 6.5}` | 8,238.88 | 3.9 | -7.1 | 69.4 | 1,168.92 | 1.0 | -25.9 | 0.26 | 36/28 | not checked |
| 741 | `{"level": -94, "max_candles": 18, "n": 24, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 8,238.88 | 3.9 | -7.1 | 69.4 | 1,168.92 | 1.0 | -25.9 | 0.26 | 36/28 | not checked |
| 800 | `{"level": -94, "max_candles": 18, "n": 24, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 8,238.88 | 3.9 | -7.1 | 69.4 | 1,168.92 | 1.0 | -25.9 | 0.26 | 36/28 | not checked |
| 962 | `{"level": -94, "max_candles": 18, "n": 24, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 8,238.88 | 3.9 | -7.1 | 69.4 | 1,168.92 | 1.0 | -25.9 | 0.26 | 36/28 | not checked |
| 676 | `{"level": -94, "max_candles": 28, "n": 26, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 7,905.84 | 3.8 | -6.6 | 69.7 | 1,283.01 | 1.1 | -24.5 | 0.29 | 33/27 | not checked |
| 698 | `{"level": -94, "max_candles": 28, "n": 26, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 7,905.84 | 3.8 | -6.6 | 69.7 | 1,283.01 | 1.1 | -24.5 | 0.29 | 33/27 | not checked |
| 965 | `{"level": -94, "max_candles": 26, "n": 26, "stop_atr": 1.75, "take_profit_atr": 6.0}` | 6,981.60 | 3.5 | -6.0 | 64.7 | 1,933.61 | 1.6 | -23.8 | 0.47 | 34/27 | not checked |
| 1534 | `{"level": -94, "max_candles": 26, "n": 26, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 6,981.60 | 3.5 | -6.0 | 64.7 | 1,933.61 | 1.6 | -23.8 | 0.47 | 34/27 | not checked |
| 1359 | `{"level": -94, "max_candles": 12, "n": 27, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 4,968.71 | 2.6 | -5.7 | 63.6 | 2,390.08 | 2.0 | -23.8 | 0.76 | 33/27 | not checked |
| 977 | `{"level": -94, "max_candles": 10, "n": 28, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 4,162.77 | 2.2 | -5.6 | 65.5 | 2,109.46 | 1.8 | -25.0 | 0.79 | 29/27 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | QQQ | 97% | 1.9 | 6.2 | 2.0 | 0.9 | -0.2 | 30 |
| 2 | VTV | 94% | 1.5 | 4.1 | 6.7 | 0.1 | 2.1 | 55 |
| 3 | SOXX | 90% | 2.9 | 5.8 | 8.8 | 1.1 | 0.9 | 41 |
| 4 | SPY | 88% | 1.1 | 4.1 | 3.9 | 0.3 | 1.7 | 35 |
| 5 | SMH | 87% | 2.2 | 6.0 | 1.4 | 0.1 | 9.3 | 54 |
| 6 | VTI | 87% | 1.3 | 4.3 | 9.1 | 0.4 | 0.4 | 40 |
| 7 | XLK | 87% | 1.1 | 4.1 | -0.6 | 1.1 | -0.6 | 42 |
| 8 | RSP | 84% | 1.7 | 5.6 | 8.8 | 1.3 | 1.4 | 47 |
| 9 | XLB | 84% | 1.4 | 4.0 | 7.3 | 1.3 | 0.8 | 53 |
| 10 | XLU | 82% | 0.9 | 3.8 | 7.3 | 0.8 | 0.8 | 47 |
| 11 | IVV | 81% | 1.1 | 3.5 | 5.8 | -0.1 | 1.5 | 38 |
| 12 | ACWI | 78% | 1.6 | 5.2 | 9.4 | 1.4 | 3.5 | 51 |
| 13 | XLI | 78% | 1.3 | 5.6 | 6.6 | -0.1 | 1.1 | 51 |
| 14 | XLY | 78% | 1.1 | 5.3 | 8.6 | -1.1 | 0.8 | 18 |
| 15 | VEA | 76% | 2.1 | 6.0 | 4.3 | 4.6 | 1.2 | 44 |
| 16 | IWDA.AS | 74% | 2.3 | 5.7 | 13.0 | 1.6 | -0.2 | 28 |
| 17 | VIG | 72% | 0.9 | 3.7 | 6.0 | -0.1 | 2.7 | 38 |
| 18 | XLP | 72% | 0.7 | 2.9 | 8.4 | 1.4 | 2.5 | 34 |
| 19 | EFA | 71% | 0.9 | 5.3 | 7.2 | 3.5 | 3.0 | 45 |
| 20 | XLV | 71% | 0.8 | 3.0 | 7.6 | -0.4 | -2.7 | 5 |
| 21 | VUG | 71% | 0.7 | 4.2 | 8.7 | 1.3 | -1.9 | 9 |
| 22 | CSPX.L | 68% | 1.8 | 5.0 | 16.3 | 0.4 | 2.6 | 27 |
| 23 | CSSPX.SW | 65% | 2.3 | 6.2 | 12.0 | 3.2 | 0.1 | 22 |
| 24 | IWM | 63% | 0.8 | 6.4 | 7.4 | 3.0 | 3.3 | 34 |
| 25 | XLF | 63% | 0.4 | 2.9 | 3.0 | -1.2 | 3.7 | 40 |
| 26 | CSSMI.SW | 62% | 1.2 | 3.4 | 12.0 | -1.6 | -0.1 | 6 |
| 27 | XLE | 60% | 0.6 | 3.2 | 7.1 | -2.2 | 3.1 | 37 |
| 28 | GLD | 57% | 0.7 | 3.9 | 6.2 | 1.2 | 4.2 | 31 |
| 29 | CSNDX.SW | 56% | 1.7 | 10.2 | 16.5 | 2.9 | -1.8 | 18 |
| 30 | LQD | 54% | 0.1 | 1.0 | 5.1 | 0.2 | 0.1 | 15 |
| 31 | VOO | 51% | 2.7 | 6.6 | 14.9 | 1.5 | 1.2 | 23 |
| 32 | VT | 51% | 0.5 | 2.8 | 8.7 | -1.6 | 3.4 | 34 |
| 33 | DIA | 49% | -0.1 | 1.6 | 4.9 | -1.6 | 2.4 | 29 |
| 34 | VNQ | 47% | 0.2 | 3.1 | 7.4 | -3.3 | -0.9 | 6 |
| 35 | TLT | 44% | -0.1 | 2.2 | 6.9 | -0.5 | -1.0 | 9 |
| 36 | TIP | 44% | -0.1 | 1.1 | 3.7 | -0.4 | -0.1 | 7 |
| 37 | USMV | 40% | 6.1 | 8.5 | 14.8 | 6.2 | 1.8 | 6 |
| 38 | DBC | 40% | 0.4 | 3.5 | -6.5 | 2.4 | 3.0 | 23 |
| 39 | SCHD | 37% | 3.9 | 6.5 | 13.3 | 4.2 | 1.1 | 8 |
| 40 | TQQQ | 37% | 0.8 | 20.6 | 42.8 | -4.1 | 4.1 | 15 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [williams_r_recovery__broad__max-income__v002.md](symbols/broad/williams_r_recovery__broad__max-income__v002.md) | 2.0 | 1.7 | 1.7 | -4.3 | 71.0 | 3621/3769 |
| broad | balanced | [williams_r_recovery__broad__balanced__v002.md](symbols/broad/williams_r_recovery__broad__balanced__v002.md) | 1.9 | 1.2 | 1.2 | -4.4 | 70.6 | 3829/4002 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,733 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
