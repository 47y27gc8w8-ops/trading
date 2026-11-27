# return_percentile_shock: optimization summary

Updated 2026-11-25T11:07:15Z · backtest.py version `d5c1e2fac8` · 958 parameter sets tested with this version (958 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [return_percentile_shock__max-income__v002.md](return_percentile_shock__max-income__v002.md) | 957 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [return_percentile_shock__balanced__v002.md](return_percentile_shock__balanced__v002.md) | 958 | `{"max_candles": 8, "n": 40, "rank": 2, "stop_atr": 4.75, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,216.66 | 4,369.63 | 2,413.32 | 781.28 |
| return % | 32.17 | 43.70 | 24.13 | 7.81 |
| return %/year | 1.8 | 3.4 | 1.4 | 0.7 |
| gross profit | 12,516.65 | 11,481.59 | 5,640.05 | 4,260.19 |
| gross loss | 9,300.00 | 7,111.95 | 3,226.73 | 3,478.91 |
| trades | 193 | 159 | 63 | 51 |
| win rate % | 64.8 | 66.7 | 68.2 | 66.7 |
| avg win | 100.13 | 108.32 | 131.16 | 125.30 |
| avg loss | -136.76 | -134.19 | -161.34 | -204.64 |
| avg result / trade | 16.67 | 27.48 | 38.31 | 15.32 |
| largest single loss | -803.25 | -574.21 | -377.54 | -590.71 |
| largest loss % of equity | -6.53 | -4.22 | -3.70 | -5.86 |
| max drawdown | -1,409.83 | -1,520.59 | -941.23 | -1,490.41 |
| max drawdown % | -11.16 | -12.15 | -9.02 | -13.82 |
| profit factor | 1.35 | 1.61 | 1.75 | 1.23 |
| unusually bad trades | 13 | 10 | 4 | 5 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.4 | 3.2 |
| time in market % | 15.9 | 16.9 | 5.8 | 6.2 |
| buy & hold return % | 85.02 | 328.39 | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.93 |  | 0.51 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | -1.8 | -1.7 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.6 | 0.0 |
| 2003 | 9.3 | 1.5 |
| 2004 | -2.5 | -1.7 |
| 2005 | -4.9 | -1.1 |
| 2006 | 2.6 | 1.0 |
| 2007 | -2.1 | -0.1 |
| 2008 | 0.0 | 0.0 |
| 2009 | 14.7 | 6.9 |
| 2010 | 4.4 | 4.5 |
| 2011 | -4.0 | 0.3 |
| 2012 | 1.1 | 4.5 |
| 2013 | 11.4 | 4.2 |
| 2014 | 3.5 | 1.9 |
| 2015 | -1.8 | 2.0 |
| 2016 (OOS) | 8.9 | 3.2 |
| 2017 (OOS) | 5.2 | 4.1 |
| 2018 (OOS) | -8.0 | -7.8 |
| 2019 (OOS) | -0.3 | -1.8 |
| 2020 (OOS) | 12.6 | -2.3 |
| 2021 (OOS) | 12.1 | 6.8 |
| 2022 (OOS) | 3.8 | 1.8 |
| 2023 (OOS) | -8.6 | -2.1 |
| 2024 (OOS) | 6.5 | 5.7 |
| 2025 (OOS) | 1.0 | -3.8 |
| 2026 (OOS) | 6.0 | 4.7 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 11.2% from a peak in-sample and 12.2% out-of-sample, and the worst single trade cost 4.2% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 82% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 9.0% from a peak in-sample and 13.8% out-of-sample, and the worst single trade cost 5.9% of the account out-of-sample. About 68 of every 100 trades won in-sample. Out-of-sample it earned 0.7% a year against 1.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 72% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 670 | `{"max_candles": 8, "n": 20, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,227.87 | 1.8 | -12.2 | 67.0 | 2,324.06 | 1.9 | -13.3 | 1.10 | 203/157 | not checked |
| 728 | `{"max_candles": 8, "n": 20, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,227.87 | 1.8 | -12.2 | 67.0 | 2,324.06 | 1.9 | -13.3 | 1.10 | 203/157 | not checked |
| 739 | `{"max_candles": 8, "n": 20, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,227.87 | 1.8 | -12.2 | 67.0 | 2,324.06 | 1.9 | -13.3 | 1.10 | 203/157 | not checked |
| 822 | `{"max_candles": 8, "n": 20, "rank": 6, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,227.87 | 1.8 | -12.2 | 67.0 | 2,324.06 | 1.9 | -13.3 | 1.10 | 203/157 | not checked |
| 824 | `{"max_candles": 8, "n": 20, "rank": 7, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,227.87 | 1.8 | -12.2 | 67.0 | 2,324.06 | 1.9 | -13.3 | 1.10 | 203/157 | not checked |
| 671 | `{"max_candles": 8, "n": 10, "rank": 7, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,216.66 | 1.8 | -11.2 | 64.8 | 4,369.63 | 3.4 | -12.2 | 1.93 | 193/159 | not checked |
| 672 | `{"max_candles": 8, "n": 10, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,216.66 | 1.8 | -11.2 | 64.8 | 4,369.63 | 3.4 | -12.2 | 1.93 | 193/159 | not checked |
| 679 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,216.66 | 1.8 | -11.2 | 64.8 | 4,369.63 | 3.4 | -12.2 | 1.93 | 193/159 | 1.00 |
| 698 | `{"max_candles": 8, "n": 10, "rank": 6, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,216.66 | 1.8 | -11.2 | 64.8 | 4,369.63 | 3.4 | -12.2 | 1.93 | 193/159 | not checked |
| 760 | `{"max_candles": 8, "n": 10, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,216.66 | 1.8 | -11.2 | 64.8 | 4,369.63 | 3.4 | -12.2 | 1.93 | 193/159 | not checked |
| 891 | `{"max_candles": 8, "n": 10, "rank": 5, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 3,216.66 | 1.8 | -11.2 | 64.8 | 4,369.63 | 3.4 | -12.2 | 1.93 | 193/159 | not checked |
| 429 | `{"max_candles": 8, "n": 10, "rank": 2, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 4,639.46 | 3.6 | -12.3 | 2.47 | 193/160 | not checked |
| 557 | `{"max_candles": 8, "n": 10, "rank": 3, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 3,516.98 | 2.8 | -12.3 | 1.95 | 193/160 | not checked |
| 568 | `{"max_candles": 8, "n": 10, "rank": 1, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 4,639.46 | 3.6 | -12.3 | 2.47 | 193/160 | not checked |
| 618 | `{"max_candles": 8, "n": 10, "rank": 2, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 4,721.91 | 3.6 | -12.3 | 2.51 | 193/160 | not checked |
| 628 | `{"max_candles": 8, "n": 10, "rank": 1, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 3,516.98 | 2.8 | -12.3 | 1.95 | 193/160 | not checked |
| 641 | `{"max_candles": 8, "n": 10, "rank": 3, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 3,160.11 | 2.5 | -12.3 | 1.77 | 193/160 | not checked |
| 692 | `{"max_candles": 8, "n": 10, "rank": 4, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 4,639.46 | 3.6 | -12.3 | 2.47 | 193/160 | not checked |
| 694 | `{"max_candles": 8, "n": 10, "rank": 3, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 4,721.91 | 3.6 | -12.3 | 2.51 | 193/160 | not checked |
| 725 | `{"max_candles": 8, "n": 10, "rank": 2, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 2,571.22 | 1.4 | -11.1 | 64.8 | 3,516.98 | 2.8 | -12.3 | 1.95 | 193/160 | not checked |
| 392 | `{"max_candles": 8, "n": 40, "rank": 2, "stop_atr": 4.75, "take_profit_atr": 3.0}` | 2,413.32 | 1.4 | -9.0 | 68.2 | 781.28 | 0.7 | -13.8 | 0.51 | 63/51 | 0.90 |
| 397 | `{"max_candles": 8, "n": 40, "rank": 1, "stop_atr": 4.75, "take_profit_atr": 3.0}` | 2,413.32 | 1.4 | -9.0 | 68.2 | 781.28 | 0.7 | -13.8 | 0.51 | 63/51 | not checked |
| 400 | `{"max_candles": 8, "n": 40, "rank": 2, "stop_atr": 5.0, "take_profit_atr": 3.0}` | 2,413.32 | 1.4 | -9.0 | 68.2 | 704.56 | 0.6 | -14.4 | 0.46 | 63/51 | not checked |
| 402 | `{"max_candles": 8, "n": 40, "rank": 2, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 2,413.32 | 1.4 | -9.0 | 68.2 | 781.28 | 0.7 | -13.8 | 0.51 | 63/51 | not checked |
| 414 | `{"max_candles": 8, "n": 40, "rank": 2, "stop_atr": 5.25, "take_profit_atr": 3.5}` | 2,413.32 | 1.4 | -9.0 | 68.2 | 609.35 | 0.5 | -15.2 | 0.40 | 63/51 | not checked |

(20 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

52 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLP | 83% | 0.9 | 2.3 | 7.3 | 0.4 | -0.8 | 2 |
| 2 | XLF | 71% | 0.7 | 5.0 | 1.5 | 0.3 | -0.7 | 0 |
| 3 | TQQQ | 68% | 11.4 | 25.6 | 57.4 | 9.0 | 7.8 | 28 |
| 4 | CSNDX.SW | 55% | 1.0 | 5.6 | 20.9 | -0.4 | -0.2 | 19 |
| 5 | SOXX | 55% | 0.3 | 3.2 | 8.3 | 0.3 | 3.5 | 30 |
| 6 | XLI | 54% | 0.1 | 2.3 | 5.7 | 0.2 | 0.8 | 32 |
| 7 | VOO | 52% | 0.8 | 4.8 | 13.5 | -1.7 | 0.7 | 28 |
| 8 | XLY | 49% | 0.2 | 2.7 | 8.4 | -0.1 | -2.7 | 21 |
| 9 | VUG | 49% | 0.0 | 2.8 | 8.6 | -1.4 | 4.2 | 24 |
| 10 | IWM | 48% | 0.0 | 3.1 | 7.6 | 1.0 | 1.2 | 5 |
| 11 | VWO | 45% | 0.4 | 4.5 | 2.3 | 1.8 | -0.4 | 2 |
| 12 | XLU | 43% | 0.0 | 1.4 | 6.7 | -1.1 | -0.6 | 0 |
| 13 | TLT | 42% | 0.0 | 1.3 | 6.6 | 0.1 | -1.8 | 0 |
| 14 | EEM | 40% | 0.0 | 3.2 | 6.0 | -1.8 | -0.3 | 1 |
| 15 | VIG | 40% | 0.0 | 2.0 | 6.4 | -1.7 | 1.2 | 22 |
| 16 | VEA | 37% | 0.0 | 3.4 | 11.2 | -0.8 | 0.9 | 10 |
| 17 | CSPX.L | 37% | 0.0 | 3.9 | 13.5 | -1.8 | 5.6 | 24 |
| 18 | RSP | 35% | 0.0 | 1.9 | 8.1 | 0.4 | 1.9 | 22 |
| 19 | XLV | 35% | 0.0 | 1.6 | 7.5 | -1.1 | -2.2 | 1 |
| 20 | USMV | 35% | 0.0 | 4.7 | 10.8 | -0.4 | 1.4 | 1 |
| 21 | QQQ | 34% | -0.0 | 1.4 | 2.4 | 0.4 | 3.4 | 22 |
| 22 | VTI | 34% | -0.1 | 1.7 | 9.4 | -0.6 | 0.9 | 19 |
| 23 | SLV | 32% | 0.0 | 3.4 | -0.8 | 2.5 | -0.6 | 1 |
| 24 | TIP | 29% | -0.0 | 0.5 | 3.8 | -0.4 | -0.6 | 0 |
| 25 | CSSMI.SW | 29% | -0.1 | 2.1 | 8.0 | 0.8 | -1.6 | 0 |
| 26 | XLK | 29% | -0.1 | 1.4 | -0.4 | -0.4 | 2.9 | 19 |
| 27 | XLE | 29% | -0.2 | 2.7 | 6.8 | -2.9 | -0.9 | 3 |
| 28 | SMH | 28% | -0.1 | 2.8 | 1.5 | -1.8 | 2.9 | 13 |
| 29 | IVV | 28% | -0.2 | 2.0 | 6.3 | -0.9 | 0.8 | 16 |
| 30 | VNQ | 23% | -0.3 | 3.4 | 6.8 | -1.9 | -1.1 | 0 |
| 31 | IWDA.AS | 20% | -0.3 | 1.9 | 13.8 | -0.3 | 1.8 | 10 |
| 32 | SPY | 20% | -0.3 | 1.8 | 3.9 | -1.1 | 1.1 | 12 |
| 33 | VTV | 20% | -0.9 | 3.0 | 6.7 | -1.2 | 1.1 | 5 |
| 34 | VT | 18% | -0.3 | 1.9 | 7.9 | -2.3 | -0.2 | 9 |
| 35 | ACWI | 15% | -0.6 | 2.2 | 7.3 | -0.9 | -0.3 | 3 |
| 36 | SCHD | 14% | -0.8 | 2.1 | 8.0 | -2.8 | 2.1 | 7 |
| 37 | XLB | 12% | -1.0 | 0.9 | 7.7 | -1.0 | 2.7 | 5 |
| 38 | DIA | 11% | -0.6 | 1.4 | 4.9 | -0.6 | 0.8 | 5 |
| 39 | GDX | 9% | -0.8 | 1.5 | -12.8 | -2.7 | 0.6 | 1 |
| 40 | CSSPX.SW | 8% | -1.0 | 1.1 | 15.1 | -3.7 | 2.2 | 5 |

(12 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [return_percentile_shock__broad__max-income__v001.md](symbols/broad/return_percentile_shock__broad__max-income__v001.md) | 0.7 | 1.0 | 0.7 | -10.1 | 60.6 | 6328/6950 |
| broad | balanced | [return_percentile_shock__broad__balanced__v001.md](symbols/broad/return_percentile_shock__broad__balanced__v001.md) | 0.7 | 1.0 | 0.7 | -10.1 | 60.6 | 6328/6950 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 958 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
