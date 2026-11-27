# cmf_accumulation_cross: optimization summary

Updated 2026-11-25T15:59:57Z · backtest.py version `5ae30db648` · 957 parameter sets tested with this version (957 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: XLF (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cmf_accumulation_cross__max-income__v002.md](cmf_accumulation_cross__max-income__v002.md) | 956 | `{"level": 0.07, "max_bars": 48, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [cmf_accumulation_cross__balanced__v002.md](cmf_accumulation_cross__balanced__v002.md) | 957 | `{"level": 0.09, "max_bars": 96, "n": 26, "stop_atr": 2.25, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 7,055.15 | 2,399.80 | 6,675.90 | 2,201.01 |
| return % | 70.55 | 24.00 | 66.76 | 22.01 |
| return %/year | 3.3 | 2.0 | 3.2 | 1.8 |
| gross profit | 19,444.92 | 8,605.18 | 18,117.27 | 9,135.78 |
| gross loss | 12,389.78 | 6,205.39 | 11,441.37 | 6,934.77 |
| trades | 77 | 53 | 67 | 44 |
| win rate % | 40.3 | 37.7 | 50.8 | 40.9 |
| avg win | 627.26 | 430.26 | 532.86 | 507.54 |
| avg loss | -269.34 | -188.04 | -346.71 | -266.72 |
| avg result / trade | 91.63 | 45.28 | 99.64 | 50.02 |
| largest single loss | -1,060.81 | -337.97 | -817.11 | -556.86 |
| largest loss % of equity | -6.17 | -2.68 | -4.87 | -4.53 |
| max drawdown | -1,912.25 | -2,960.86 | -2,301.73 | -3,027.01 |
| max drawdown % | -10.08 | -20.39 | -17.12 | -24.42 |
| profit factor | 1.57 | 1.39 | 1.58 | 1.32 |
| unusually bad trades | 5 | 0 | 2 | 0 |
| … threshold (% of equity) | 2.7 | 3.4 | 4.5 | 4.9 |
| time in market % | 11.7 | 13.2 | 25.9 | 26.5 |
| buy & hold return % | 41.29 | 257.92 | 41.29 | 257.92 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.60 |  | 0.58 |
| period | 1999-08-12 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-08-12 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1999 | 0.0 | 0.0 |
| 2000 | 20.9 | -2.2 |
| 2001 | -2.0 | 0.2 |
| 2002 | 2.0 | 2.0 |
| 2003 | 12.4 | 16.3 |
| 2004 | 8.0 | 5.5 |
| 2005 | -2.3 | -1.8 |
| 2006 | 0.1 | -1.3 |
| 2007 | 4.9 | 0.2 |
| 2008 | 0.0 | 0.0 |
| 2009 | 11.1 | 22.0 |
| 2010 | 3.5 | 8.4 |
| 2011 | -1.2 | -3.3 |
| 2012 | 8.1 | 7.2 |
| 2013 | 0.2 | 7.1 |
| 2014 | 2.4 | 0.3 |
| 2015 | -10.1 | -4.9 |
| 2016 (OOS) | 2.8 | 4.4 |
| 2017 (OOS) | 5.9 | 17.3 |
| 2018 (OOS) | -5.8 | -11.9 |
| 2019 (OOS) | 3.8 | -8.8 |
| 2020 (OOS) | 16.8 | 4.9 |
| 2021 (OOS) | 15.1 | 25.2 |
| 2022 (OOS) | -11.8 | -9.2 |
| 2023 (OOS) | -1.7 | -0.2 |
| 2024 (OOS) | 3.2 | 11.4 |
| 2025 (OOS) | -7.4 | -3.7 |
| 2026 (OOS) | 4.7 | -3.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 10.1% from a peak in-sample and 20.4% out-of-sample, and the worst single trade cost 2.7% of the account out-of-sample. About 40 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 49% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 17.1% from a peak in-sample and 24.4% out-of-sample, and the worst single trade cost 4.5% of the account out-of-sample. About 51 of every 100 trades won in-sample. Out-of-sample it earned 1.8% a year against 3.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 441 | `{"level": 0.07, "max_bars": 42, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |
| 442 | `{"level": 0.07, "max_bars": 54, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |
| 443 | `{"level": 0.07, "max_bars": 48, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | 1.00 |
| 448 | `{"level": 0.07, "max_bars": 36, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |
| 507 | `{"level": 0.07, "max_bars": 60, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |
| 607 | `{"level": 0.07, "max_bars": 30, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,633.50 | 2.2 | -17.9 | 0.66 | 77/53 | not checked |
| 731 | `{"level": 0.07, "max_bars": 66, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |
| 899 | `{"level": 0.07, "max_bars": 72, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |
| 903 | `{"level": 0.07, "max_bars": 78, "n": 28, "stop_atr": 1.0, "take_profit_atr": 3.0}` | 7,055.15 | 3.3 | -10.1 | 40.3 | 2,399.80 | 2.0 | -20.4 | 0.60 | 77/53 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

54 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | VNQ | 84% | 1.6 | 6.0 | 8.2 | 3.5 | -3.9 | 12 |
| 2 | EEM | 75% | 1.5 | 8.6 | 7.3 | 5.8 | 3.4 | 22 |
| 3 | RSP | 75% | 1.3 | 5.5 | 8.9 | 1.6 | -1.4 | 21 |
| 4 | EFA | 75% | 1.2 | 5.7 | 5.5 | 4.3 | 1.3 | 20 |
| 5 | HYG | 73% | 1.2 | 4.6 | 4.8 | 1.8 | -0.6 | 18 |
| 6 | VT | 72% | 1.1 | 5.7 | 12.6 | 2.7 | -0.1 | 24 |
| 7 | TLT | 64% | 0.7 | 4.4 | 6.6 | 1.2 | -1.8 | 4 |
| 8 | VTI | 64% | 0.5 | 4.7 | 7.4 | 2.3 | 2.9 | 37 |
| 9 | VUG | 62% | 0.5 | 3.9 | 8.7 | 1.6 | 1.3 | 33 |
| 10 | VEA | 61% | 2.3 | 6.8 | 0.8 | 5.7 | 1.6 | 11 |
| 11 | IWDA.AS | 61% | 1.1 | 5.2 | 11.7 | 0.6 | 1.1 | 15 |
| 12 | CSSPX.SW | 61% | 1.0 | 3.7 | 12.3 | 3.6 | 1.4 | 33 |
| 13 | VWO | 59% | 1.2 | 8.0 | 4.7 | 8.0 | 3.2 | 15 |
| 14 | LQD | 59% | 0.3 | 2.0 | 5.3 | 1.1 | 0.7 | 12 |
| 15 | IWM | 58% | 0.7 | 4.8 | 7.2 | 4.8 | -0.7 | 14 |
| 16 | QQQ | 56% | 0.3 | 3.6 | 4.3 | -1.5 | 0.1 | 31 |
| 17 | SPY | 55% | 0.2 | 3.3 | 9.3 | 1.4 | 1.7 | 28 |
| 18 | XLI | 55% | 0.2 | 3.8 | 5.7 | 2.3 | 0.7 | 21 |
| 19 | IVV | 50% | -0.0 | 2.1 | 5.1 | -1.3 | 0.2 | 23 |
| 20 | XLY | 50% | -0.0 | 3.8 | 8.1 | 0.8 | -0.3 | 18 |
| 21 | AGG | 48% | 0.0 | 1.7 | 4.4 | 0.6 | -0.5 | 9 |
| 22 | XLK | 47% | -0.1 | 2.7 | 1.6 | 2.2 | 3.2 | 28 |
| 23 | XLF | 47% | -0.1 | 3.3 | 2.1 | 3.3 | -0.9 | 19 |
| 24 | TQQQ | 47% | -0.1 | 14.8 | 49.0 | 6.1 | -5.5 | 20 |
| 25 | IEF | 45% | -0.1 | 1.4 | 5.2 | 0.4 | -0.6 | 7 |
| 26 | ACWI | 44% | -0.1 | 5.4 | 11.1 | 2.8 | 0.8 | 16 |
| 27 | GLD | 42% | -0.2 | 3.6 | 8.7 | 1.8 | 0.6 | 16 |
| 28 | USO | 41% | -0.2 | 6.2 | -15.7 | 1.2 | 4.5 | 14 |
| 29 | VIG | 38% | -0.4 | 2.1 | 6.4 | 0.0 | -0.7 | 17 |
| 30 | VTV | 36% | -0.5 | 3.4 | 7.1 | -0.9 | -0.2 | 12 |
| 31 | XLU | 34% | -0.5 | 2.4 | 6.1 | -0.9 | -2.4 | 19 |
| 32 | CSPX.L | 33% | -0.1 | 6.2 | 11.5 | 2.6 | -1.0 | 7 |
| 33 | SLV | 33% | -0.4 | 4.9 | -0.5 | -1.2 | -2.3 | 3 |
| 34 | SOXX | 33% | -0.5 | 3.7 | 2.0 | -0.2 | -4.3 | 13 |
| 35 | DIA | 33% | -0.7 | 1.9 | 7.0 | -1.4 | -1.1 | 13 |
| 36 | VOO | 31% | -0.3 | 2.5 | 11.4 | 1.4 | -0.3 | 15 |
| 37 | XLB | 25% | -0.8 | 2.4 | 5.5 | -0.1 | -3.7 | 0 |
| 38 | CSNDX.SW | 23% | -0.6 | 5.2 | 19.2 | -0.7 | 3.5 | 14 |
| 39 | CSSMI.SW | 22% | -0.6 | 3.3 | 4.6 | -4.7 | -0.4 | 5 |
| 40 | USMV | 20% | 0.3 | 3.5 | 14.0 | 0.9 | 0.2 | 1 |

(14 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [cmf_accumulation_cross__broad__max-income__v002.md](symbols/broad/cmf_accumulation_cross__broad__max-income__v002.md) | 1.3 | 2.7 | 1.3 | -9.7 | 50.2 | 1603/1636 |
| broad | balanced | [cmf_accumulation_cross__broad__balanced__v002.md](symbols/broad/cmf_accumulation_cross__broad__balanced__v002.md) | 1.4 | 2.7 | 1.4 | -9.5 | 50.7 | 1585/1623 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 957 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
