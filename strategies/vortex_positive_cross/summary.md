# vortex_positive_cross: optimization summary

Updated 2026-11-25T23:21:57Z · backtest.py version `0b2fd9cffe` · 53,754 parameter sets tested with this version (53,754 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: IWM (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [vortex_positive_cross__max-income__v001.md](vortex_positive_cross__max-income__v001.md) | 35545 | `{"max_candles": 120, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [vortex_positive_cross__balanced__v001.md](vortex_positive_cross__balanced__v001.md) | 35546 | `{"max_candles": 120, "n": 20, "stop_atr": 2.0, "take_profit_atr": 4.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [vortex_positive_cross__safe-starter__v001.md](vortex_positive_cross__safe-starter__v001.md) | 35547 | `{"max_candles": 192, "n": 20, "stop_atr": 1.0, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 11,810.94 | 4,677.00 | 11,606.35 | 4,331.67 | 3,551.14 | 3,289.38 |
| return % | 118.11 | 46.77 | 116.06 | 43.32 | 35.51 | 32.89 |
| return %/year | 5.4 | 3.6 | 5.3 | 3.4 | 2.1 | 2.6 |
| gross profit | 25,708.99 | 13,295.51 | 24,928.45 | 12,821.24 | 14,671.00 | 10,384.75 |
| gross loss | 13,898.05 | 8,618.52 | 13,322.10 | 8,489.56 | 11,119.86 | 7,095.37 |
| trades | 97 | 84 | 97 | 84 | 97 | 84 |
| win rate % | 49.5 | 45.2 | 49.5 | 45.2 | 41.2 | 41.7 |
| avg win | 535.60 | 349.88 | 519.34 | 337.40 | 366.78 | 296.71 |
| avg loss | -283.63 | -187.36 | -271.88 | -184.56 | -195.09 | -144.80 |
| avg result / trade | 121.76 | 55.68 | 119.65 | 51.57 | 36.61 | 39.16 |
| largest single loss | -996.45 | -677.28 | -925.92 | -654.37 | -492.47 | -309.54 |
| largest loss % of equity | -5.73 | -5.30 | -5.73 | -5.30 | -4.42 | -2.72 |
| max drawdown | -1,864.81 | -2,455.28 | -1,749.04 | -2,372.25 | -1,684.08 | -2,206.94 |
| max drawdown % | -12.58 | -19.04 | -12.58 | -19.04 | -11.41 | -18.27 |
| profit factor | 1.85 | 1.54 | 1.87 | 1.51 | 1.32 | 1.46 |
| unusually bad trades | 4 | 10 | 4 | 10 | 1 | 0 |
| … threshold (% of equity) | 3.5 | 2.7 | 3.5 | 2.7 | 3.1 | 3.0 |
| time in market % | 30.6 | 30.9 | 29.1 | 29.6 | 13.6 | 14.1 |
| buy & hold return % | 204.74 | 175.35 | 204.74 | 175.35 | 204.74 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.66 |  | 0.63 |  | 1.28 |
| period | 2001-03-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2001-03-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2001-03-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2001 | -0.4 | -0.4 | -0.4 |
| 2002 | 2.0 | 2.0 | 6.0 |
| 2003 | 12.2 | 11.4 | 4.2 |
| 2004 | 7.8 | 6.1 | -2.3 |
| 2005 | -5.6 | -5.6 | -3.2 |
| 2006 | 18.7 | 16.3 | 10.3 |
| 2007 | -6.3 | -6.3 | -5.8 |
| 2008 | -5.4 | -5.4 | -1.4 |
| 2009 | 31.4 | 28.6 | 15.1 |
| 2010 | 10.5 | 10.4 | 0.3 |
| 2011 | -2.2 | -3.7 | 2.7 |
| 2012 | 14.3 | 16.9 | 8.7 |
| 2013 | 14.4 | 16.8 | 4.8 |
| 2014 | -1.9 | 0.9 | -3.8 |
| 2015 | -1.8 | -1.8 | -2.1 |
| 2016 (OOS) | 3.8 | 3.0 | 2.7 |
| 2017 (OOS) | -1.5 | -2.0 | -1.9 |
| 2018 (OOS) | 0.1 | -0.6 | -4.3 |
| 2019 (OOS) | 2.3 | 2.3 | 8.4 |
| 2020 (OOS) | 22.0 | 20.2 | 9.1 |
| 2021 (OOS) | -16.0 | -16.0 | -11.4 |
| 2022 (OOS) | -2.7 | -2.7 | -2.3 |
| 2023 (OOS) | 3.3 | 8.0 | 4.0 |
| 2024 (OOS) | 10.1 | 8.7 | 7.3 |
| 2025 (OOS) | 10.0 | 8.4 | 6.7 |
| 2026 (OOS) | 12.3 | 11.6 | 13.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 12.6% from a peak in-sample and 19.0% out-of-sample, and the worst single trade cost 5.3% of the account out-of-sample. About 49 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 12.6% from a peak in-sample and 19.0% out-of-sample, and the worst single trade cost 5.3% of the account out-of-sample. About 49 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 11.4% from a peak in-sample and 18.3% out-of-sample, and the worst single trade cost 2.7% of the account out-of-sample. About 41 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 55% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 798 | `{"max_candles": 120, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | 1.00 |
| 809 | `{"max_candles": 108, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 810 | `{"max_candles": 132, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 864 | `{"max_candles": 192, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 1528 | `{"max_candles": 96, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 8461 | `{"max_candles": 168, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 9800 | `{"max_candles": 180, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 10479 | `{"max_candles": 48, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 21005 | `{"max_candles": 144, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 21058 | `{"max_candles": 156, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 21751 | `{"max_candles": 60, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 26088 | `{"max_candles": 84, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 35302 | `{"max_candles": 72, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 35550 | `{"max_candles": 204, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 35585 | `{"max_candles": 216, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 35586 | `{"max_candles": 228, "n": 20, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 11,810.94 | 5.4 | -12.6 | 49.5 | 4,677.00 | 3.6 | -19.0 | 0.66 | 97/84 | not checked |
| 806 | `{"max_candles": 120, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 5524 | `{"max_candles": 108, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 6927 | `{"max_candles": 168, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 18327 | `{"max_candles": 84, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 19855 | `{"max_candles": 144, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 20556 | `{"max_candles": 72, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 24490 | `{"max_candles": 96, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 26436 | `{"max_candles": 156, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |
| 26477 | `{"max_candles": 48, "n": 20, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 11,151.51 | 5.2 | -12.3 | 48.5 | 2,264.48 | 1.9 | -28.3 | 0.36 | 97/84 | not checked |

(71 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | VT | 94% | 2.4 | 8.3 | 11.9 | 1.8 | -0.7 | 29 |
| 2 | HYG | 92% | 2.3 | 6.1 | 5.0 | 2.3 | 0.2 | 8 |
| 3 | VNQ | 91% | 2.4 | 8.7 | 7.6 | 2.6 | 0.1 | 15 |
| 4 | SOXX | 91% | 2.1 | 6.7 | 3.7 | 3.9 | 3.9 | 48 |
| 5 | XLE | 91% | 1.8 | 6.0 | 6.9 | 0.8 | -2.9 | 14 |
| 6 | RSP | 89% | 1.8 | 5.3 | 8.2 | 1.3 | 4.8 | 49 |
| 7 | VTI | 89% | 1.3 | 3.8 | 7.1 | 0.3 | 2.6 | 41 |
| 8 | QQQ | 86% | 2.4 | 5.3 | 1.6 | 2.8 | 3.8 | 43 |
| 9 | ACWI | 86% | 1.7 | 9.3 | 10.8 | -0.2 | -0.6 | 26 |
| 10 | TQQQ | 84% | 4.6 | 16.4 | 45.7 | 8.7 | 4.0 | 30 |
| 11 | VWO | 83% | 3.8 | 9.5 | 3.3 | 0.8 | 0.1 | 13 |
| 12 | VUG | 83% | 2.0 | 5.3 | 8.3 | 2.7 | 2.7 | 27 |
| 13 | TLT | 81% | 1.4 | 4.0 | 6.2 | 2.3 | -3.4 | 1 |
| 14 | EEM | 80% | 3.2 | 7.1 | 6.4 | 1.9 | -0.4 | 27 |
| 15 | VTV | 77% | 1.1 | 4.7 | 6.8 | 0.6 | 1.0 | 36 |
| 16 | IVV | 75% | 0.9 | 3.3 | 5.3 | 1.2 | 2.0 | 39 |
| 17 | IWM | 72% | 1.4 | 5.4 | 7.8 | -0.3 | 0.6 | 22 |
| 18 | XLU | 69% | 0.8 | 3.8 | 6.4 | 0.5 | 2.1 | 28 |
| 19 | VIG | 69% | 0.8 | 4.2 | 6.2 | 1.4 | 1.7 | 31 |
| 20 | XLB | 69% | 0.7 | 3.1 | 5.6 | -1.1 | -0.0 | 2 |
| 21 | IWDA.AS | 67% | 0.5 | 4.9 | 13.5 | -3.2 | 1.3 | 36 |
| 22 | VOO | 66% | 1.6 | 5.2 | 13.1 | 1.8 | 2.2 | 34 |
| 23 | CSSPX.SW | 64% | 0.8 | 5.1 | 11.6 | -0.1 | 0.7 | 29 |
| 24 | XLI | 62% | 0.3 | 3.1 | 5.6 | 0.6 | -1.7 | 17 |
| 25 | VEA | 61% | 0.6 | 4.7 | 0.0 | -2.0 | -1.1 | 13 |
| 26 | GLD | 61% | 0.5 | 5.5 | 8.3 | -1.1 | -0.1 | 8 |
| 27 | CSNDX.SW | 58% | 0.8 | 5.3 | 16.8 | -0.1 | 2.9 | 36 |
| 28 | EFA | 58% | 0.5 | 4.8 | 6.0 | -0.2 | -0.3 | 13 |
| 29 | SPY | 58% | 0.2 | 2.4 | 3.9 | -0.9 | 0.6 | 32 |
| 30 | DBC | 58% | 0.2 | 4.5 | -5.8 | 2.6 | -0.5 | 13 |
| 31 | DIA | 52% | 0.1 | 2.6 | 4.9 | 1.2 | 1.1 | 26 |
| 32 | LQD | 52% | 0.0 | 1.6 | 4.9 | 0.2 | -1.0 | 6 |
| 33 | XLK | 50% | 0.0 | 2.5 | -0.5 | -1.4 | -0.7 | 24 |
| 34 | XLP | 50% | 0.0 | 3.0 | 7.4 | -0.4 | 1.2 | 14 |
| 35 | IEF | 50% | 0.0 | 1.4 | 5.0 | 0.4 | -0.7 | 0 |
| 36 | SMH | 42% | -0.6 | 1.9 | 2.1 | 0.4 | 3.5 | 23 |
| 37 | CSPX.L | 41% | -0.4 | 3.4 | 12.1 | -0.5 | 9.4 | 17 |
| 38 | USO | 41% | -0.5 | 6.5 | -14.7 | -3.5 | 0.1 | 19 |
| 39 | BND | 38% | -0.4 | 1.1 | 3.8 | -0.6 | -0.7 | 0 |
| 40 | CSSMI.SW | 38% | -0.5 | 2.1 | 7.7 | -0.9 | 1.8 | 11 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [vortex_positive_cross__broad__max-income__v002.md](symbols/broad/vortex_positive_cross__broad__max-income__v002.md) | 1.8 | 2.3 | 1.8 | -8.5 | 40.7 | 3848/3893 |
| broad | balanced | [vortex_positive_cross__broad__balanced__v001.md](symbols/broad/vortex_positive_cross__broad__balanced__v001.md) | 0.7 | 0.9 | 0.7 | -6.0 | 45.2 | 3848/3893 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 53,754 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
