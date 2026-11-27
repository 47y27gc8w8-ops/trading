# kst_cycle_confirmation: optimization summary

Updated 2026-11-26T04:01:40Z · backtest.py version `c6a1335e0b` · 40,146 parameter sets tested with this version (40,146 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [kst_cycle_confirmation__max-income__v002.md](kst_cycle_confirmation__max-income__v002.md) | 40145 | `{"max_candles": 80, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [kst_cycle_confirmation__balanced__v002.md](kst_cycle_confirmation__balanced__v002.md) | 40146 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 5,264.31 | 878.65 | 4,953.70 | 1,410.90 |
| return % | 52.64 | 8.79 | 49.54 | 14.11 |
| return %/year | 2.0 | 0.8 | 1.9 | 1.2 |
| gross profit | 9,886.83 | 5,123.42 | 9,474.98 | 5,787.25 |
| gross loss | 4,622.52 | 4,244.77 | 4,521.28 | 4,376.35 |
| trades | 48 | 36 | 48 | 36 |
| win rate % | 58.3 | 55.6 | 56.2 | 55.6 |
| avg win | 353.10 | 256.17 | 350.93 | 289.36 |
| avg loss | -231.13 | -265.30 | -215.30 | -273.52 |
| avg result / trade | 109.67 | 24.41 | 103.20 | 39.19 |
| largest single loss | -598.02 | -782.87 | -590.64 | -792.97 |
| largest loss % of equity | -4.26 | -6.88 | -4.26 | -6.88 |
| max drawdown | -1,125.21 | -1,009.88 | -1,000.18 | -1,059.56 |
| max drawdown % | -7.93 | -8.81 | -7.25 | -9.09 |
| profit factor | 2.14 | 1.21 | 2.10 | 1.32 |
| unusually bad trades | 3 | 6 | 3 | 6 |
| … threshold (% of equity) | 2.9 | 2.6 | 2.9 | 2.6 |
| time in market % | 13.3 | 17.7 | 14.9 | 20.0 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.38 |  | 0.63 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 9.9 | 7.7 |
| 1996 | 11.9 | 9.6 |
| 1997 | 4.2 | 2.0 |
| 1998 | 7.0 | 8.7 |
| 1999 | -0.6 | -0.6 |
| 2000 | -2.6 | -2.6 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 |
| 2003 | 4.3 | 4.9 |
| 2004 | 1.2 | 1.6 |
| 2005 | -0.4 | -0.4 |
| 2006 | 0.9 | 1.7 |
| 2007 | -6.5 | -6.5 |
| 2008 | 0.0 | 0.0 |
| 2009 | 1.3 | 2.9 |
| 2010 | 0.3 | 0.3 |
| 2011 | 2.0 | 1.5 |
| 2012 | 3.4 | 5.4 |
| 2013 | 5.8 | 2.6 |
| 2014 | 2.8 | 3.8 |
| 2015 | -0.6 | -0.6 |
| 2016 (OOS) | -1.7 | -1.7 |
| 2017 (OOS) | 7.7 | 8.4 |
| 2018 (OOS) | 0.9 | 1.7 |
| 2019 (OOS) | 3.3 | 4.3 |
| 2020 (OOS) | 0.4 | 0.9 |
| 2021 (OOS) | 0.2 | 2.1 |
| 2022 (OOS) | -3.8 | -3.8 |
| 2023 (OOS) | 3.9 | 3.1 |
| 2024 (OOS) | 2.1 | 3.0 |
| 2025 (OOS) | -2.2 | -2.2 |
| 2026 (OOS) | -1.9 | -1.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 7.9% from a peak in-sample and 8.8% out-of-sample, and the worst single trade cost 6.9% of the account out-of-sample. About 58 of every 100 trades won in-sample. Out-of-sample it earned 0.8% a year against 2.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 7.2% from a peak in-sample and 9.1% out-of-sample, and the worst single trade cost 6.9% of the account out-of-sample. About 56 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 39633 | `{"max_candles": 72, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39634 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39635 | `{"max_candles": 80, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | 1.00 |
| 39722 | `{"max_candles": 64, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39848 | `{"max_candles": 56, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39852 | `{"max_candles": 96, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39904 | `{"max_candles": 48, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39932 | `{"max_candles": 104, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39959 | `{"max_candles": 112, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 40077 | `{"max_candles": 120, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,264.31 | 2.0 | -7.9 | 58.3 | 878.65 | 0.8 | -8.8 | 0.38 | 48/36 | not checked |
| 39610 | `{"max_candles": 80, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39611 | `{"max_candles": 96, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39612 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | 1.00 |
| 39626 | `{"max_candles": 120, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39642 | `{"max_candles": 72, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39647 | `{"max_candles": 128, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39659 | `{"max_candles": 48, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39679 | `{"max_candles": 56, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39704 | `{"max_candles": 64, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39717 | `{"max_candles": 112, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39767 | `{"max_candles": 104, "signal": 21, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,953.70 | 1.9 | -7.2 | 56.2 | 1,410.90 | 1.2 | -9.1 | 0.63 | 48/36 | not checked |
| 39677 | `{"max_candles": 104, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 3,952.70 | 1.6 | -7.2 | 54.2 | 1,739.15 | 1.5 | -8.2 | 0.93 | 48/36 | not checked |
| 39699 | `{"max_candles": 64, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 3,952.70 | 1.6 | -7.2 | 54.2 | 1,739.15 | 1.5 | -8.2 | 0.93 | 48/36 | not checked |
| 40106 | `{"max_candles": 112, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 3,952.70 | 1.6 | -7.2 | 54.2 | 1,739.15 | 1.5 | -8.2 | 0.93 | 48/36 | not checked |
| 40129 | `{"max_candles": 88, "signal": 21, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 3,952.70 | 1.6 | -7.2 | 54.2 | 1,739.15 | 1.5 | -8.2 | 0.93 | 48/36 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

64 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ^GDAXI | 100% | 1.9 | 2.9 | 8.1 | 1.4 | -0.9 | 4 |
| 2 | ^SSMI | 98% | 1.1 | 2.2 | 5.9 | 0.7 | -0.6 | 3 |
| 3 | GLD | 97% | 2.7 | 4.6 | 8.3 | 0.3 | 2.3 | 44 |
| 4 | IEF | 91% | 0.6 | 1.4 | 5.0 | 0.0 | -0.3 | 9 |
| 5 | ^IXIC | 86% | 0.8 | 2.3 | 9.5 | 0.5 | -2.0 | 21 |
| 6 | XLP | 83% | 1.2 | 2.6 | 6.7 | 0.2 | -0.4 | 4 |
| 7 | LQD | 82% | 0.5 | 2.1 | 5.2 | -0.1 | -0.8 | 7 |
| 8 | TLT | 78% | 0.7 | 3.0 | 6.3 | 0.3 | -0.1 | 29 |
| 9 | BND | 69% | 0.2 | 0.8 | 4.1 | -0.1 | -0.2 | 27 |
| 10 | SPY | 68% | 0.5 | 2.0 | 9.3 | -0.6 | 0.3 | 39 |
| 11 | EFA | 66% | 1.1 | 2.7 | 5.6 | -1.3 | 0.1 | 7 |
| 12 | EEM | 65% | 0.9 | 3.9 | 7.4 | -0.4 | 0.7 | 13 |
| 13 | ^GSPC | 63% | 0.4 | 1.7 | 7.4 | -1.5 | -0.1 | 34 |
| 14 | ^DJI | 63% | 0.2 | 1.3 | 7.5 | -0.2 | 0.6 | 27 |
| 15 | AGG | 63% | 0.1 | 0.8 | 4.3 | -0.5 | -0.2 | 32 |
| 16 | VNQ | 57% | 0.4 | 2.9 | 8.4 | -1.9 | -1.2 | 3 |
| 17 | XLU | 52% | 0.1 | 1.7 | 5.9 | -0.6 | 0.8 | 33 |
| 18 | ^N225 | 45% | -0.2 | 1.2 | -0.2 | -1.3 | -1.8 | 5 |
| 19 | SHY | 43% | -0.0 | 0.3 | 2.1 | -0.4 | -0.2 | 0 |
| 20 | CSSMI.SW | 40% | 0.1 | 1.5 | 4.3 | -0.3 | -0.4 | 5 |
| 21 | RSP | 38% | -0.2 | 1.3 | 8.8 | -0.7 | -0.2 | 10 |
| 22 | TIP | 34% | -0.2 | 0.5 | 4.2 | -0.7 | -0.8 | 15 |
| 23 | IVV | 34% | -0.3 | 1.0 | 5.3 | -1.1 | 0.2 | 22 |
| 24 | HYG | 32% | 0.8 | 1.2 | 4.4 | 1.2 | 0.1 | 3 |
| 25 | DBC | 28% | 1.6 | 2.7 | -5.5 | 0.6 | 1.7 | 17 |
| 26 | VWO | 28% | -0.3 | 1.2 | 4.3 | -2.5 | -0.1 | 3 |
| 27 | VTV | 26% | -0.3 | 0.9 | 7.2 | -0.7 | 1.9 | 15 |
| 28 | XLV | 25% | -0.8 | 1.0 | 7.2 | -0.8 | 1.6 | 15 |
| 29 | TQQQ | 22% | -0.2 | 4.2 | 52.0 | 0.9 | -2.4 | 7 |
| 30 | DIA | 22% | -0.4 | 0.7 | 6.5 | -0.3 | -0.2 | 10 |
| 31 | VTI | 20% | -0.6 | 0.9 | 7.1 | -0.6 | -0.9 | 12 |
| 32 | XLI | 18% | -0.7 | 0.6 | 5.5 | -1.4 | -0.0 | 12 |
| 33 | ^RUT | 17% | -0.7 | 1.0 | 7.5 | -0.9 | 0.6 | 7 |
| 34 | XLY | 17% | -1.4 | 1.3 | 7.6 | -3.0 | 1.3 | 11 |
| 35 | ^VIX | 17% | -3.3 | 4.1 | 1.2 | -0.8 | -6.2 | 6 |
| 36 | VEA | 15% | -0.1 | 1.1 | 0.5 | -2.2 | -0.9 | 7 |
| 37 | XLK | 12% | -0.7 | 0.4 | 1.5 | -1.0 | 0.6 | 8 |
| 38 | XLF | 12% | -0.9 | 0.6 | 1.7 | -1.5 | 3.0 | 8 |
| 39 | IWM | 11% | -0.9 | 1.2 | 7.0 | -1.2 | 0.3 | 5 |
| 40 | SOXX | 11% | -1.6 | 1.1 | 3.5 | -2.6 | -0.3 | 7 |

(24 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [kst_cycle_confirmation__broad__max-income__v001.md](symbols/broad/kst_cycle_confirmation__broad__max-income__v001.md) | 0.3 | 0.5 | 0.3 | -5.1 | 46.8 | 1751/1833 |
| broad | balanced | [kst_cycle_confirmation__broad__balanced__v002.md](symbols/broad/kst_cycle_confirmation__broad__balanced__v002.md) | 0.3 | 0.4 | 0.3 | -4.2 | 45.6 | 1751/1833 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 40,146 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
