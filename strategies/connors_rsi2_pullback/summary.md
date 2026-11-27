# connors_rsi2_pullback: optimization summary

Updated 2026-11-25T15:34:26Z · backtest.py version `3aa6e0898d` · 76,088 parameter sets tested with this version (76,088 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [connors_rsi2_pullback__max-income__v001.md](connors_rsi2_pullback__max-income__v001.md) | 76086 | `{"buy": 11, "max_bars": 8, "n": 2, "stop_atr": 4.0, "take_profit_atr": 6.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [connors_rsi2_pullback__balanced__v001.md](connors_rsi2_pullback__balanced__v001.md) | 76087 | `{"buy": 10, "max_bars": 8, "n": 2, "stop_atr": 4.0, "take_profit_atr": 3.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [connors_rsi2_pullback__safe-starter__v001.md](connors_rsi2_pullback__safe-starter__v001.md) | 76088 | `{"buy": 7, "max_bars": 6, "n": 2, "stop_atr": 2.0, "take_profit_atr": 2.5}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 16,656.79 | 1,978.47 | 14,317.00 | 1,481.64 | 8,889.29 | 2,408.86 |
| return % | 166.57 | 19.78 | 143.17 | 14.82 | 88.89 | 24.09 |
| return %/year | 4.8 | 1.7 | 4.3 | 1.3 | 3.1 | 2.0 |
| gross profit | 28,551.24 | 7,805.39 | 24,749.92 | 6,961.52 | 17,353.22 | 6,371.93 |
| gross loss | 11,894.44 | 5,826.92 | 10,432.92 | 5,479.89 | 8,463.93 | 3,963.08 |
| trades | 182 | 107 | 166 | 95 | 117 | 73 |
| win rate % | 74.7 | 68.2 | 74.7 | 68.4 | 73.5 | 69.9 |
| avg win | 209.94 | 106.92 | 199.60 | 107.10 | 201.78 | 124.94 |
| avg loss | -258.57 | -171.38 | -248.40 | -182.66 | -273.03 | -180.14 |
| avg result / trade | 91.52 | 18.49 | 86.25 | 15.60 | 75.98 | 33.00 |
| largest single loss | -1,190.99 | -805.44 | -1,092.01 | -772.03 | -830.83 | -548.41 |
| largest loss % of equity | -5.25 | -6.30 | -5.25 | -6.30 | -5.13 | -5.64 |
| max drawdown | -1,915.33 | -1,181.79 | -1,535.02 | -1,333.56 | -1,348.29 | -1,307.56 |
| max drawdown % | -8.25 | -11.11 | -7.85 | -12.63 | -7.38 | -12.62 |
| profit factor | 2.40 | 1.34 | 2.37 | 1.27 | 2.05 | 1.61 |
| unusually bad trades | 10 | 10 | 9 | 10 | 1 | 1 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 | 3.7 | 3.6 |
| time in market % | 11.1 | 11.9 | 9.9 | 10.6 | 5.7 | 6.3 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.35 |  | 0.30 |  | 0.65 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 7.2 | 5.8 | 5.7 |
| 1996 | -0.8 | -0.2 | 1.3 |
| 1997 | 26.8 | 26.1 | 23.0 |
| 1998 | 14.2 | 12.6 | 5.9 |
| 1999 | 9.4 | 9.4 | 11.4 |
| 2000 | 5.0 | 7.2 | -1.6 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 | 0.0 |
| 2003 | 7.3 | 5.4 | 5.0 |
| 2004 | 2.1 | 0.6 | 0.3 |
| 2005 | -2.2 | -2.2 | -1.1 |
| 2006 | 5.1 | 4.3 | 1.8 |
| 2007 | -1.6 | -3.0 | 0.1 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 13.9 | 9.6 | 9.6 |
| 2010 | 1.0 | 1.0 | 1.4 |
| 2011 | -4.6 | -3.6 | -3.4 |
| 2012 | 12.4 | 13.2 | 8.1 |
| 2013 | 6.0 | 6.0 | 2.2 |
| 2014 | 1.0 | -0.2 | 2.6 |
| 2015 | 3.1 | 3.1 | -4.3 |
| 2016 (OOS) | 2.0 | 2.3 | 1.9 |
| 2017 (OOS) | 3.8 | 3.0 | 1.4 |
| 2018 (OOS) | -6.3 | -6.2 | -4.8 |
| 2019 (OOS) | 1.4 | 0.1 | 1.0 |
| 2020 (OOS) | 5.2 | 4.3 | 1.1 |
| 2021 (OOS) | 7.9 | 8.8 | 7.1 |
| 2022 (OOS) | -5.3 | -5.3 | -1.2 |
| 2023 (OOS) | -1.4 | -2.0 | -1.5 |
| 2024 (OOS) | 9.3 | 9.5 | 8.7 |
| 2025 (OOS) | 8.1 | 5.3 | 6.2 |
| 2026 (OOS) | -4.9 | -4.5 | 2.6 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 8.2% from a peak in-sample and 11.1% out-of-sample, and the worst single trade cost 6.3% of the account out-of-sample. About 75 of every 100 trades won in-sample. Out-of-sample it earned 1.7% a year against 4.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 90% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 7.8% from a peak in-sample and 12.6% out-of-sample, and the worst single trade cost 6.3% of the account out-of-sample. About 75 of every 100 trades won in-sample. Out-of-sample it earned 1.3% a year against 4.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 79% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 7.4% from a peak in-sample and 12.6% out-of-sample, and the worst single trade cost 5.6% of the account out-of-sample. About 74 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 79% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 53255 | `{"buy": 11, "max_bars": 8, "n": 2, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 16,740.83 | 4.8 | -8.2 | 74.7 | 1,978.47 | 1.7 | -11.1 | 0.35 | 182/107 | not checked |
| 6875 | `{"buy": 10, "max_bars": 8, "n": 2, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 14,853.51 | 4.4 | -7.8 | 74.7 | 1,481.64 | 1.3 | -12.6 | 0.29 | 166/95 | not checked |
| 18182 | `{"buy": 8, "max_bars": 6, "n": 2, "stop_atr": 2.0, "take_profit_atr": 4.5}` | 12,338.05 | 3.9 | -7.5 | 74.5 | 2,192.09 | 1.8 | -10.7 | 0.47 | 137/87 | not checked |
| 6991 | `{"buy": 7, "max_bars": 6, "n": 2, "stop_atr": 2.0, "take_profit_atr": 4.5}` | 9,896.08 | 3.3 | -7.4 | 73.5 | 2,173.07 | 1.8 | -12.6 | 0.55 | 117/73 | not checked |
| 45883 | `{"buy": 12, "max_bars": 20, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 49450 | `{"buy": 12, "max_bars": 16, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 49922 | `{"buy": 12, "max_bars": 8, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 58965 | `{"buy": 12, "max_bars": 12, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 60376 | `{"buy": 12, "max_bars": 24, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 61119 | `{"buy": 12, "max_bars": 10, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 63388 | `{"buy": 12, "max_bars": 18, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 72754 | `{"buy": 12, "max_bars": 14, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 75634 | `{"buy": 12, "max_bars": 22, "n": 3, "stop_atr": 2.5, "take_profit_atr": 4.5}` | 9,863.03 | 3.3 | -6.3 | 73.7 | 1,547.37 | 1.3 | -12.4 | 0.40 | 76/48 | not checked |
| 66790 | `{"buy": 12, "max_bars": 4, "n": 3, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 4,917.22 | 1.9 | -5.8 | 58.5 | 742.66 | 0.7 | -5.5 | 0.34 | 82/51 | not checked |
| 54252 | `{"buy": 11, "max_bars": 4, "n": 3, "stop_atr": 1.0, "take_profit_atr": 4.5}` | 3,713.62 | 1.5 | -5.7 | 56.1 | 760.83 | 0.7 | -5.0 | 0.45 | 66/43 | not checked |
| 4239 | `{"buy": 7, "max_bars": 10, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 6961 | `{"buy": 7, "max_bars": 18, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 8726 | `{"buy": 7, "max_bars": 10, "n": 3, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 9435 | `{"buy": 7, "max_bars": 18, "n": 3, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 10264 | `{"buy": 7, "max_bars": 6, "n": 3, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 509.23 | 0.5 | -6.4 | 0.40 | 24/15 | not checked |
| 12815 | `{"buy": 7, "max_bars": 14, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 13548 | `{"buy": 7, "max_bars": 8, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 14595 | `{"buy": 7, "max_bars": 12, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 14608 | `{"buy": 7, "max_bars": 24, "n": 3, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |
| 17002 | `{"buy": 7, "max_bars": 16, "n": 3, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 2,676.39 | 1.1 | -3.5 | 75.0 | 470.80 | 0.4 | -6.4 | 0.37 | 24/15 | not checked |

(40 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SPY | 58% | 0.8 | 4.8 | 9.3 | 2.2 | 1.0 | 21 |
| 2 | XLI | 50% | 0.6 | 2.1 | 5.8 | 0.4 | 1.1 | 28 |
| 3 | XLK | 48% | 0.8 | 2.1 | -0.3 | 1.3 | 0.3 | 11 |
| 4 | XLE | 47% | 1.0 | 4.7 | 7.2 | 2.7 | -1.9 | 9 |
| 5 | SOXX | 47% | 0.4 | 3.5 | 6.5 | 2.3 | 1.1 | 26 |
| 6 | IVV | 47% | 0.2 | 2.8 | 5.4 | 1.7 | 1.1 | 25 |
| 7 | XLF | 45% | 0.6 | 2.9 | 2.5 | 1.7 | 0.4 | 10 |
| 8 | IWM | 45% | 0.2 | 3.4 | 7.0 | 0.9 | 2.2 | 23 |
| 9 | VTV | 45% | 0.2 | 2.7 | 6.6 | 1.0 | 1.3 | 25 |
| 10 | XLV | 45% | 0.1 | 3.2 | 7.1 | 2.2 | -1.6 | 5 |
| 11 | VUG | 45% | 0.1 | 3.8 | 8.5 | 1.6 | 0.1 | 12 |
| 12 | QQQ | 42% | 0.3 | 1.6 | 0.7 | 0.7 | 2.0 | 14 |
| 13 | RSP | 41% | 0.1 | 2.4 | 9.0 | 1.4 | 1.2 | 17 |
| 14 | SMH | 38% | 0.6 | 3.5 | 1.7 | 1.1 | 1.1 | 21 |
| 15 | EFA | 38% | 0.3 | 1.3 | 7.1 | 0.4 | 0.1 | 14 |
| 16 | VTI | 38% | 0.1 | 2.9 | 8.6 | 0.5 | 1.8 | 19 |
| 17 | CSSMI.SW | 34% | 0.5 | 3.9 | 8.4 | 2.7 | -1.1 | 0 |
| 18 | VIG | 34% | 0.3 | 3.7 | 6.0 | 0.7 | -0.1 | 7 |
| 19 | IWDA.AS | 33% | 0.7 | 4.1 | 13.8 | 1.9 | 0.3 | 16 |
| 20 | XLY | 33% | 0.0 | 2.8 | 7.5 | 0.4 | 1.2 | 18 |
| 21 | VWO | 33% | 0.0 | 4.3 | 2.5 | 0.3 | -1.2 | 3 |
| 22 | DIA | 33% | -0.0 | 1.4 | 6.0 | 0.6 | 0.5 | 10 |
| 23 | CSPX.L | 31% | 1.3 | 5.8 | 16.9 | 2.2 | 3.5 | 18 |
| 24 | CSNDX.SW | 31% | 0.9 | 3.6 | 16.1 | 2.9 | -0.9 | 3 |
| 25 | ACWI | 31% | 0.2 | 2.4 | 12.3 | 1.0 | -0.2 | 7 |
| 26 | VNQ | 31% | 0.0 | 3.9 | 8.0 | 0.9 | -0.9 | 0 |
| 27 | CSSPX.SW | 30% | 0.6 | 4.9 | 12.3 | 2.4 | 1.2 | 16 |
| 28 | TQQQ | 27% | 5.1 | 17.5 | 41.9 | 10.2 | 8.9 | 10 |
| 29 | VOO | 27% | 0.6 | 5.4 | 15.3 | 3.2 | 1.3 | 13 |
| 30 | VEA | 23% | 0.3 | 1.5 | 1.6 | 1.0 | -0.8 | 3 |
| 31 | SLV | 22% | 2.3 | 2.6 | 0.1 | 2.2 | 0.1 | 5 |
| 32 | GLD | 22% | 0.0 | 1.3 | 7.4 | 0.6 | 1.6 | 10 |
| 33 | XLB | 22% | 0.0 | 0.9 | 5.8 | 0.6 | 1.6 | 9 |
| 34 | XLP | 19% | -0.1 | 0.8 | 7.6 | -0.4 | 0.6 | 3 |
| 35 | VT | 17% | 0.1 | 1.0 | 10.9 | -0.6 | -0.7 | 6 |
| 36 | HYG | 17% | 0.1 | 0.7 | 4.9 | -0.7 | -0.3 | 0 |
| 37 | EEM | 17% | -0.1 | 1.5 | 6.3 | -0.2 | -0.8 | 4 |
| 38 | GDX | 16% | 0.7 | 3.4 | -11.0 | 3.2 | -0.2 | 5 |
| 39 | TLT | 14% | 0.0 | 0.6 | 7.1 | -0.4 | 0.8 | 9 |
| 40 | TIP | 14% | 0.0 | 0.2 | 3.8 | 0.2 | -0.2 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [connors_rsi2_pullback__broad__max-income__v002.md](symbols/broad/connors_rsi2_pullback__broad__max-income__v002.md) | 0.9 | 0.5 | 0.5 | -10.2 | 63.7 | 3823/3965 |
| broad | balanced | [connors_rsi2_pullback__broad__balanced__v001.md](symbols/broad/connors_rsi2_pullback__broad__balanced__v001.md) | 0.8 | 0.6 | 0.6 | -7.7 | 63.5 | 3492/3683 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 76,088 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
