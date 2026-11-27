# aroon_trend_onset: optimization summary

Updated 2026-11-25T18:52:05Z · backtest.py version `0f1046be1b` · 941 parameter sets tested with this version (941 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: GLD (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [aroon_trend_onset__max-income__v002.md](aroon_trend_onset__max-income__v002.md) | 939 | `{"level": 90.0, "max_bars": 72, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [aroon_trend_onset__balanced__v002.md](aroon_trend_onset__balanced__v002.md) | 940 | `{"level": 65.0, "max_bars": 72, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [aroon_trend_onset__safe-starter__v002.md](aroon_trend_onset__safe-starter__v002.md) | 941 | `{"level": 50.0, "max_bars": 48, "n": 20, "stop_atr": 0.75, "take_profit_atr": 4.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 10,653.29 | 2,513.82 | 5,216.05 | 2,905.61 | 2,220.11 | 3,039.26 |
| return % | 106.53 | 25.14 | 52.16 | 29.06 | 22.20 | 30.39 |
| return %/year | 7.5 | 2.1 | 4.2 | 2.4 | 2.0 | 2.5 |
| gross profit | 17,055.67 | 6,684.83 | 7,905.42 | 6,682.53 | 4,266.32 | 5,655.58 |
| gross loss | 6,402.38 | 4,171.01 | 2,689.37 | 3,776.91 | 2,046.20 | 2,616.32 |
| trades | 26 | 29 | 27 | 45 | 21 | 34 |
| win rate % | 50.0 | 37.9 | 48.1 | 31.1 | 33.3 | 41.2 |
| avg win | 1,311.97 | 607.71 | 608.11 | 477.32 | 609.47 | 403.97 |
| avg loss | -492.49 | -231.72 | -192.10 | -121.84 | -146.16 | -130.82 |
| avg result / trade | 409.74 | 86.68 | 193.19 | 64.57 | 105.72 | 89.39 |
| largest single loss | -884.76 | -442.19 | -385.99 | -306.51 | -194.40 | -316.48 |
| largest loss % of equity | -4.21 | -3.41 | -2.59 | -2.45 | -1.94 | -2.33 |
| max drawdown | -2,340.32 | -1,222.16 | -979.17 | -1,145.58 | -882.73 | -684.12 |
| max drawdown % | -10.64 | -10.85 | -8.81 | -9.89 | -7.95 | -5.85 |
| profit factor | 2.66 | 1.60 | 2.94 | 1.77 | 2.08 | 2.16 |
| unusually bad trades | 0 | 0 | 0 | 1 | 0 | 1 |
| … threshold (% of equity) | 5.4 | 4.3 | 2.9 | 2.0 | 2.3 | 2.0 |
| time in market % | 17.1 | 15.2 | 8.0 | 9.8 | 5.7 | 7.2 |
| buy & hold return % | 105.55 | 222.91 | 105.55 | 222.91 | 105.55 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |  | 0.56 |  | 1.23 |
| period | 2005-11-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2005-11-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2005-11-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2005 | 0.0 | 0.0 | 0.0 |
| 2006 | 11.0 | 8.4 | 2.9 |
| 2007 | 5.1 | 5.8 | -0.6 |
| 2008 | 15.2 | 10.0 | 10.2 |
| 2009 | 32.6 | 0.0 | -2.6 |
| 2010 | 5.5 | 2.4 | 4.8 |
| 2011 | 7.1 | 11.5 | 7.2 |
| 2012 | 1.3 | 0.8 | 1.3 |
| 2013 | -3.1 | -0.9 | -4.0 |
| 2014 | 7.2 | 2.7 | -1.1 |
| 2015 | -2.5 | 3.0 | 2.9 |
| 2016 (OOS) | -2.9 | 1.9 | 1.6 |
| 2017 (OOS) | 1.7 | 5.4 | 0.0 |
| 2018 (OOS) | -3.5 | -1.9 | -2.4 |
| 2019 (OOS) | 2.4 | 6.3 | 10.2 |
| 2020 (OOS) | 2.3 | -0.1 | 2.3 |
| 2021 (OOS) | 4.5 | -4.4 | 2.9 |
| 2022 (OOS) | 0.9 | -1.4 | -3.1 |
| 2023 (OOS) | -3.0 | 2.7 | 0.0 |
| 2024 (OOS) | 8.9 | 5.9 | 6.7 |
| 2025 (OOS) | 6.6 | 10.6 | 14.3 |
| 2026 (OOS) | 5.6 | 1.6 | -4.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 10.6% from a peak in-sample and 10.8% out-of-sample, and the worst single trade cost 3.4% of the account out-of-sample. About 50 of every 100 trades won in-sample. Out-of-sample it earned 2.1% a year against 7.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 92% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 8.8% from a peak in-sample and 9.9% out-of-sample, and the worst single trade cost 2.5% of the account out-of-sample. About 48 of every 100 trades won in-sample. Out-of-sample it earned 2.4% a year against 4.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 8.0% from a peak in-sample and 5.8% out-of-sample, and the worst single trade cost 2.3% of the account out-of-sample. About 33 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 376 | `{"level": 90.0, "max_bars": 60, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 377 | `{"level": 90.0, "max_bars": 84, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 378 | `{"level": 90.0, "max_bars": 72, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | 1.00 |
| 473 | `{"level": 90.0, "max_bars": 120, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 476 | `{"level": 90.0, "max_bars": 108, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 516 | `{"level": 90.0, "max_bars": 48, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 622 | `{"level": 90.0, "max_bars": 132, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 753 | `{"level": 90.0, "max_bars": 96, "n": 38, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 10,653.29 | 7.5 | -10.6 | 50.0 | 2,513.82 | 2.1 | -10.8 | 0.28 | 26/29 | not checked |
| 549 | `{"level": 62.5, "max_bars": 72, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 555 | `{"level": 65.0, "max_bars": 60, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 556 | `{"level": 65.0, "max_bars": 84, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 557 | `{"level": 65.0, "max_bars": 72, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | 1.00 |
| 561 | `{"level": 65.0, "max_bars": 48, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 572 | `{"level": 62.5, "max_bars": 48, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 626 | `{"level": 62.5, "max_bars": 60, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 638 | `{"level": 62.5, "max_bars": 84, "n": 18, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 5,216.05 | 4.2 | -8.8 | 48.1 | 2,905.61 | 2.4 | -9.9 | 0.56 | 27/45 | not checked |
| 760 | `{"level": 65.0, "max_bars": 72, "n": 20, "stop_atr": 1.0, "take_profit_atr": 4.0}` | 4,862.46 | 4.0 | -7.9 | 50.0 | 2,833.12 | 2.3 | -10.0 | 0.58 | 24/43 | not checked |
| 548 | `{"level": 65.0, "max_bars": 72, "n": 20, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 3,480.51 | 3.0 | -7.8 | 37.5 | 2,875.05 | 2.4 | -8.7 | 0.78 | 24/43 | not checked |
| 761 | `{"level": 67.5, "max_bars": 84, "n": 20, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 3,480.51 | 3.0 | -7.8 | 37.5 | 2,875.05 | 2.4 | -8.7 | 0.78 | 24/43 | not checked |
| 815 | `{"level": 67.5, "max_bars": 72, "n": 20, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 3,480.51 | 3.0 | -7.8 | 37.5 | 2,875.05 | 2.4 | -8.7 | 0.78 | 24/43 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | EEM | 75% | 1.8 | 5.3 | 6.3 | 1.3 | -0.8 | 13 |
| 2 | LQD | 75% | 1.2 | 3.2 | 5.3 | 1.0 | -0.1 | 10 |
| 3 | TLT | 71% | 1.2 | 3.4 | 7.1 | 1.3 | -2.2 | 6 |
| 4 | AGG | 55% | 0.3 | 1.4 | 4.1 | 0.3 | -0.1 | 13 |
| 5 | IEF | 54% | 0.1 | 1.2 | 5.3 | 0.2 | -0.3 | 12 |
| 6 | XLK | 52% | 0.5 | 3.2 | -0.3 | -1.0 | 2.6 | 33 |
| 7 | XLU | 51% | 0.1 | 3.5 | 6.7 | -0.6 | -1.0 | 15 |
| 8 | GLD | 49% | 0.8 | 7.5 | 7.4 | -0.9 | -0.6 | 23 |
| 9 | VWO | 48% | 1.3 | 5.4 | 2.5 | 1.6 | -1.5 | 12 |
| 10 | VNQ | 42% | -0.0 | 5.1 | 8.0 | 4.6 | -1.3 | 2 |
| 11 | EFA | 38% | 0.4 | 3.1 | 7.1 | -0.1 | 0.6 | 8 |
| 12 | XLB | 38% | 0.0 | 2.0 | 5.8 | -1.8 | 0.2 | 14 |
| 13 | XLV | 38% | -0.0 | 2.8 | 7.1 | 0.9 | -2.2 | 9 |
| 14 | VUG | 37% | 0.3 | 4.2 | 8.5 | -0.1 | 4.2 | 24 |
| 15 | HYG | 34% | 1.6 | 3.9 | 4.9 | 1.7 | 0.2 | 1 |
| 16 | SMH | 34% | -0.1 | 5.9 | 1.7 | -0.6 | 4.2 | 18 |
| 17 | XLP | 34% | -0.4 | 2.0 | 7.6 | 0.8 | 3.4 | 19 |
| 18 | IWM | 31% | -0.1 | 4.4 | 7.0 | -1.2 | 0.6 | 6 |
| 19 | SPY | 31% | -0.4 | 2.2 | 9.3 | -1.7 | 3.8 | 18 |
| 20 | SLV | 28% | 1.0 | 4.4 | 0.1 | 1.4 | 2.0 | 13 |
| 21 | BND | 26% | 0.0 | 0.7 | 4.0 | -0.5 | -0.2 | 7 |
| 22 | XLY | 26% | -0.7 | 2.1 | 7.5 | -2.6 | 2.6 | 17 |
| 23 | VTI | 25% | -0.4 | 4.1 | 8.6 | -1.4 | 1.6 | 16 |
| 24 | RSP | 23% | -0.5 | 2.0 | 9.0 | -1.4 | 1.4 | 12 |
| 25 | IVV | 23% | -0.6 | 1.8 | 5.4 | -2.5 | 3.5 | 15 |
| 26 | QQQ | 23% | -0.7 | 1.6 | 0.7 | -2.0 | 2.7 | 14 |
| 27 | DIA | 22% | -0.5 | 2.0 | 6.0 | -1.1 | 1.8 | 14 |
| 28 | SOXX | 20% | -0.6 | 3.6 | 6.5 | -1.1 | 1.1 | 5 |
| 29 | VTV | 18% | -0.7 | 1.3 | 6.6 | -1.9 | -0.4 | 8 |
| 30 | DBC | 18% | -0.9 | 2.5 | -6.0 | 1.0 | 0.8 | 4 |
| 31 | XLF | 18% | -1.7 | 2.6 | 2.5 | 0.3 | -1.8 | 1 |
| 32 | SHY | 14% | -0.2 | 0.4 | 2.1 | -0.3 | -0.2 | 1 |
| 33 | TIP | 14% | -0.3 | 0.8 | 3.8 | -0.5 | 0.2 | 6 |
| 34 | XLE | 14% | -1.3 | 2.8 | 7.2 | -5.1 | -1.9 | 4 |
| 35 | IWDA.AS | 12% | 0.5 | 3.1 | 13.8 | 0.6 | -0.2 | 2 |
| 36 | VT | 12% | 0.1 | 3.1 | 10.9 | -0.3 | 1.2 | 7 |
| 37 | VEA | 11% | -0.5 | 1.4 | 1.6 | 1.2 | -0.1 | 3 |
| 38 | ACWI | 9% | -0.3 | 1.7 | 12.3 | -1.0 | 1.5 | 6 |
| 39 | CSSPX.SW | 8% | 0.2 | 0.9 | 12.3 | 0.8 | 2.5 | 4 |
| 40 | CSNDX.SW | 8% | -0.7 | 2.9 | 16.1 | -1.3 | 2.9 | 4 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [aroon_trend_onset__broad__max-income__v002.md](symbols/broad/aroon_trend_onset__broad__max-income__v002.md) | 0.6 | 1.6 | 0.6 | -4.1 | 49.9 | 711/764 |
| broad | balanced | [aroon_trend_onset__broad__balanced__v002.md](symbols/broad/aroon_trend_onset__broad__balanced__v002.md) | 0.6 | 2.0 | 0.6 | -4.1 | 47.7 | 688/725 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 941 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
