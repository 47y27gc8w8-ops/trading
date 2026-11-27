# three_down_closes: optimization summary

Updated 2026-11-25T07:31:08Z · backtest.py version `1d9e1ab953` · 6,428 parameter sets tested with this version (6,428 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [three_down_closes__max-income__v001.md](three_down_closes__max-income__v001.md) | 6427 | `{"max_candles": 10, "n": 3, "stop_atr": 4.25, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [three_down_closes__balanced__v001.md](three_down_closes__balanced__v001.md) | 6428 | `{"max_candles": 8, "n": 3, "stop_atr": 4.0, "take_profit_atr": 3.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 4,524.61 | 731.29 | 4,304.63 | 788.48 |
| return % | 45.25 | 7.31 | 43.05 | 7.88 |
| return %/year | 2.4 | 0.7 | 2.3 | 0.7 |
| gross profit | 9,567.57 | 6,660.04 | 9,442.69 | 6,839.11 |
| gross loss | 5,042.96 | 5,928.74 | 5,138.07 | 6,050.63 |
| trades | 116 | 103 | 119 | 104 |
| win rate % | 69.8 | 68.9 | 69.8 | 67.3 |
| avg win | 118.12 | 93.80 | 113.77 | 97.70 |
| avg loss | -144.08 | -185.27 | -142.72 | -177.96 |
| avg result / trade | 39.01 | 7.10 | 36.17 | 7.58 |
| largest single loss | -781.94 | -768.91 | -712.74 | -725.43 |
| largest loss % of equity | -5.57 | -6.69 | -5.25 | -6.30 |
| max drawdown | -1,306.71 | -1,547.11 | -1,007.39 | -1,817.79 |
| max drawdown % | -9.31 | -14.58 | -8.03 | -16.57 |
| profit factor | 1.90 | 1.12 | 1.84 | 1.13 |
| unusually bad trades | 5 | 12 | 6 | 11 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 9.7 | 11.7 | 9.7 | 11.4 |
| buy & hold return % | 85.02 | 328.39 | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |  | 0.31 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 7.5 | 7.5 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.8 | 0.8 |
| 2003 | 3.9 | 2.4 |
| 2004 | -0.4 | -0.4 |
| 2005 | 1.1 | -0.1 |
| 2006 | 2.5 | 1.6 |
| 2007 | 2.9 | 3.0 |
| 2008 | 0.0 | 0.0 |
| 2009 | 5.0 | 5.0 |
| 2010 | 4.1 | 4.1 |
| 2011 | 1.4 | 1.7 |
| 2012 | 0.2 | 3.0 |
| 2013 | 1.5 | 1.5 |
| 2014 | 6.6 | 5.3 |
| 2015 | 1.1 | 1.1 |
| 2016 (OOS) | 2.0 | 2.0 |
| 2017 (OOS) | -0.0 | 0.6 |
| 2018 (OOS) | 1.5 | 1.4 |
| 2019 (OOS) | -5.7 | -5.2 |
| 2020 (OOS) | -0.2 | -0.2 |
| 2021 (OOS) | 10.7 | 10.7 |
| 2022 (OOS) | -0.5 | -0.5 |
| 2023 (OOS) | 1.9 | 1.9 |
| 2024 (OOS) | 8.5 | 5.1 |
| 2025 (OOS) | -3.7 | -3.2 |
| 2026 (OOS) | -6.1 | -4.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.3% from a peak in-sample and 14.6% out-of-sample, and the worst single trade cost 6.7% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 0.7% a year against 2.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 69% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 8.0% from a peak in-sample and 16.6% out-of-sample, and the worst single trade cost 6.3% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 0.7% a year against 2.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 60% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5555 | `{"max_candles": 10, "n": 3, "stop_atr": 4.25, "take_profit_atr": 5.0}` | 4,524.61 | 2.4 | -9.3 | 69.8 | 731.29 | 0.7 | -14.6 | 0.28 | 116/103 | 1.00 |
| 5470 | `{"max_candles": 12, "n": 3, "stop_atr": 4.75, "take_profit_atr": 5.0}` | 4,515.26 | 2.4 | -9.2 | 69.0 | 1,377.31 | 1.2 | -15.4 | 0.50 | 116/103 | not checked |
| 373 | `{"max_candles": 10, "n": 3, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 4,461.93 | 2.3 | -8.7 | 69.8 | 933.45 | 0.8 | -16.6 | 0.35 | 116/104 | 1.00 |
| 5784 | `{"max_candles": 8, "n": 3, "stop_atr": 4.5, "take_profit_atr": 5.0}` | 4,334.70 | 2.3 | -8.1 | 69.8 | 856.06 | 0.8 | -15.0 | 0.33 | 119/103 | not checked |
| 371 | `{"max_candles": 8, "n": 3, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 4,304.63 | 2.3 | -8.0 | 69.8 | 788.48 | 0.7 | -16.6 | 0.31 | 119/104 | 0.86 |
| 378 | `{"max_candles": 8, "n": 3, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 4,282.44 | 2.2 | -7.8 | 69.8 | 725.77 | 0.7 | -16.6 | 0.29 | 119/104 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLE | 90% | 1.9 | 5.0 | 7.1 | 2.8 | 3.0 | 46 |
| 2 | TLT | 79% | 1.4 | 2.6 | 6.9 | 2.4 | -0.4 | 20 |
| 3 | CSSMI.SW | 73% | 1.0 | 4.5 | 12.0 | 2.7 | -0.1 | 0 |
| 4 | XLF | 73% | 0.5 | 2.6 | 3.0 | 1.9 | 0.4 | 35 |
| 5 | CSSPX.SW | 71% | 1.2 | 2.6 | 12.0 | 0.6 | 1.4 | 21 |
| 6 | VIG | 71% | 0.6 | 3.3 | 6.0 | 2.4 | 1.2 | 16 |
| 7 | EFA | 71% | 0.5 | 1.7 | 7.2 | 1.7 | 0.0 | 9 |
| 8 | XLU | 71% | 0.5 | 1.4 | 7.3 | 0.2 | -2.8 | 0 |
| 9 | XLV | 70% | 0.6 | 2.7 | 7.6 | 0.6 | -1.2 | 0 |
| 10 | XLI | 70% | 0.4 | 2.0 | 6.6 | 1.1 | 0.4 | 25 |
| 11 | SMH | 65% | 0.8 | 3.3 | 1.4 | 2.1 | 3.8 | 39 |
| 12 | VOO | 63% | 1.5 | 2.6 | 14.9 | 0.6 | 1.3 | 23 |
| 13 | SOXX | 63% | 0.4 | 3.1 | 8.8 | 1.2 | 3.7 | 38 |
| 14 | XLP | 62% | 0.3 | 1.4 | 8.4 | -0.1 | 0.0 | 29 |
| 15 | TQQQ | 59% | 8.0 | 23.2 | 42.8 | 13.7 | 6.5 | 17 |
| 16 | QQQ | 59% | 0.8 | 2.6 | 2.0 | 2.5 | 0.2 | 6 |
| 17 | VTI | 59% | 0.5 | 2.4 | 9.1 | 1.2 | 1.5 | 21 |
| 18 | VNQ | 59% | 0.3 | 5.9 | 7.4 | 5.9 | -1.2 | 0 |
| 19 | IVV | 54% | 0.5 | 1.9 | 5.8 | 0.7 | 1.1 | 14 |
| 20 | GLD | 51% | 0.2 | 3.6 | 6.2 | 0.7 | -2.1 | 0 |
| 21 | CSNDX.SW | 49% | 1.3 | 6.2 | 16.5 | 5.5 | 0.7 | 0 |
| 22 | CSPX.L | 49% | 0.9 | 4.8 | 16.3 | 0.2 | 2.2 | 20 |
| 23 | XLK | 49% | 0.7 | 1.1 | -0.6 | -0.1 | 1.3 | 14 |
| 24 | VUG | 49% | 0.4 | 3.5 | 8.7 | 1.8 | 1.6 | 13 |
| 25 | VTV | 49% | 0.2 | 1.4 | 6.7 | 1.2 | -1.0 | 0 |
| 26 | SLV | 48% | 2.5 | 3.8 | 0.4 | 0.4 | -3.4 | 0 |
| 27 | SPY | 48% | 0.3 | 2.4 | 3.9 | 0.9 | 0.6 | 13 |
| 28 | XLY | 46% | 0.0 | 2.5 | 8.6 | 1.4 | 1.4 | 16 |
| 29 | EEM | 46% | -0.0 | 1.3 | 7.6 | 0.7 | -0.1 | 12 |
| 30 | IEF | 40% | -0.1 | 0.8 | 5.1 | 0.1 | -0.8 | 0 |
| 31 | RSP | 37% | 0.0 | 3.7 | 8.8 | 1.8 | -0.4 | 2 |
| 32 | XLB | 35% | 0.1 | 0.8 | 7.3 | 0.6 | -1.4 | 0 |
| 33 | IWM | 32% | 0.3 | 2.0 | 7.4 | 0.8 | 2.0 | 12 |
| 34 | VT | 32% | 0.2 | 1.8 | 8.7 | 1.4 | 0.3 | 7 |
| 35 | GDX | 30% | 0.2 | 3.1 | -11.2 | -0.5 | -2.3 | 14 |
| 36 | IWDA.AS | 27% | 0.3 | 1.9 | 13.0 | -1.4 | 0.9 | 3 |
| 37 | VWO | 25% | -0.3 | 1.8 | 2.2 | -1.6 | -0.5 | 0 |
| 38 | USMV | 24% | 0.3 | 4.8 | 14.8 | -0.8 | 0.2 | 10 |
| 39 | USO | 21% | -0.5 | 2.8 | -16.6 | -1.1 | -2.3 | 0 |
| 40 | AGG | 21% | -0.8 | 0.1 | 4.1 | -0.9 | -0.7 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [three_down_closes__broad__max-income__v001.md](symbols/broad/three_down_closes__broad__max-income__v001.md) | 1.0 | 0.3 | 0.3 | -8.7 | 62.0 | 4060/4518 |
| broad | balanced | [three_down_closes__broad__balanced__v001.md](symbols/broad/three_down_closes__broad__balanced__v001.md) | 1.0 | 0.5 | 0.5 | -7.8 | 61.9 | 4106/4592 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 6,428 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
