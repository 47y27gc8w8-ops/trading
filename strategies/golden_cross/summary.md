# golden_cross: optimization summary

Updated 2026-11-26T02:14:24Z · backtest.py version `913e5c44e1` · 1,000 parameter sets tested with this version (1,000 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__max-income__v002.md](golden_cross__max-income__v002.md) | 998 | `{"fast": 30, "max_candles": 104, "slow": 210, "stop_atr": 3.5, "take_profit_atr": 10.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [golden_cross__balanced__v002.md](golden_cross__balanced__v002.md) | 999 | `{"fast": 40, "max_candles": 104, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 7.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [golden_cross__safe-starter__v002.md](golden_cross__safe-starter__v002.md) | 1000 | `{"fast": 40, "max_candles": 104, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 7.0}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 14,600.45 | 4,719.27 | 7,856.29 | 2,693.41 | 7,177.50 | 2,570.82 |
| return % | 146.00 | 47.19 | 78.56 | 26.93 | 71.78 | 25.71 |
| return %/year | 4.4 | 3.6 | 2.8 | 2.2 | 2.6 | 2.1 |
| gross profit | 15,262.52 | 5,469.54 | 8,502.67 | 3,444.97 | 7,803.03 | 3,320.28 |
| gross loss | 662.07 | 750.27 | 646.38 | 751.56 | 625.53 | 749.46 |
| trades | 10 | 5 | 8 | 5 | 8 | 5 |
| win rate % | 90.0 | 80.0 | 75.0 | 60.0 | 75.0 | 60.0 |
| avg win | 1,695.84 | 1,367.39 | 1,417.11 | 1,148.32 | 1,300.51 | 1,106.76 |
| avg loss | -662.07 | -750.27 | -323.19 | -375.78 | -312.77 | -374.73 |
| avg result / trade | 1,460.05 | 943.85 | 982.04 | 538.68 | 897.19 | 514.16 |
| largest single loss | -662.07 | -750.27 | -478.61 | -469.23 | -460.42 | -467.13 |
| largest loss % of equity | -5.08 | -5.49 | -2.61 | -3.88 | -2.61 | -3.88 |
| max drawdown | -2,536.27 | -1,301.72 | -601.04 | -1,117.50 | -595.28 | -1,112.48 |
| max drawdown % | -9.69 | -9.44 | -5.11 | -9.44 | -5.11 | -9.44 |
| profit factor | 23.05 | 7.29 | 13.15 | 4.58 | 12.47 | 4.43 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 10.2 | 11.0 | 3.9 | 6.7 | 3.9 | 6.7 |
| time in market % | 14.9 | 15.8 | 6.8 | 11.1 | 6.4 | 10.8 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.83 |  | 0.79 |  | 0.81 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 0.0 | 0.0 | 0.0 |
| 1996 | 0.0 | 0.0 | 0.0 |
| 1997 | 0.0 | 0.0 | 0.0 |
| 1998 | 8.1 | 8.1 | 8.1 |
| 1999 | 16.6 | 5.4 | 4.5 |
| 2000 | 3.4 | 0.0 | 0.0 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | -5.1 | 0.0 | 0.0 |
| 2003 | 14.7 | 12.8 | 11.9 |
| 2004 | 8.4 | 4.9 | 4.4 |
| 2005 | 0.0 | 0.0 | 0.0 |
| 2006 | 12.0 | 0.0 | 0.0 |
| 2007 | 0.0 | 0.0 | 0.0 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 21.6 | 14.2 | 13.2 |
| 2010 | 8.9 | 8.2 | 8.2 |
| 2011 | 4.4 | 1.2 | 0.7 |
| 2012 | 2.0 | 8.8 | 8.2 |
| 2013 | 0.0 | 0.0 | 0.0 |
| 2014 | 0.0 | 0.0 | 0.0 |
| 2015 | 1.3 | -2.6 | -2.6 |
| 2016 (OOS) | 1.2 | -2.8 | -2.8 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 0.0 | 0.0 |
| 2019 (OOS) | 7.3 | 7.1 | 6.6 |
| 2020 (OOS) | 19.4 | 16.1 | 16.1 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | -5.5 | -3.9 | -3.9 |
| 2024 (OOS) | 0.0 | 0.0 | 0.0 |
| 2025 (OOS) | 13.9 | 9.3 | 8.7 |
| 2026 (OOS) | 0.0 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.7% from a peak in-sample and 9.4% out-of-sample, and the worst single trade cost 5.5% of the account out-of-sample. About 90 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 5.1% from a peak in-sample and 9.4% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 75 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 5.1% from a peak in-sample and 9.4% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 75 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 748 | `{"fast": 30, "max_candles": 104, "slow": 210, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 15,128.14 | 4.5 | -9.7 | 90.0 | 4,760.45 | 3.6 | -9.4 | 0.81 | 10/5 | not checked |
| 925 | `{"fast": 30, "max_candles": 104, "slow": 210, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 15,128.14 | 4.5 | -9.7 | 90.0 | 4,619.90 | 3.5 | -9.4 | 0.79 | 10/5 | not checked |
| 939 | `{"fast": 30, "max_candles": 96, "slow": 210, "stop_atr": 2.5, "take_profit_atr": 9.5}` | 13,702.95 | 4.2 | -9.3 | 90.0 | 2,500.95 | 2.1 | -12.8 | 0.49 | 10/5 | not checked |
| 763 | `{"fast": 30, "max_candles": 160, "slow": 120, "stop_atr": 1.0, "take_profit_atr": 10.5}` | 8,776.43 | 3.0 | -8.9 | 29.2 | 2,766.48 | 2.3 | -9.4 | 0.74 | 24/10 | not checked |
| 873 | `{"fast": 30, "max_candles": 168, "slow": 120, "stop_atr": 1.0, "take_profit_atr": 10.5}` | 8,776.43 | 3.0 | -8.9 | 29.2 | 2,766.48 | 2.3 | -9.4 | 0.74 | 24/10 | not checked |
| 875 | `{"fast": 30, "max_candles": 176, "slow": 120, "stop_atr": 1.0, "take_profit_atr": 10.5}` | 8,776.43 | 3.0 | -8.9 | 29.2 | 2,766.48 | 2.3 | -9.4 | 0.74 | 24/10 | not checked |
| 997 | `{"fast": 30, "max_candles": 184, "slow": 120, "stop_atr": 1.0, "take_profit_atr": 10.5}` | 8,776.43 | 3.0 | -8.9 | 29.2 | 2,766.48 | 2.3 | -9.4 | 0.74 | 24/10 | not checked |
| 609 | `{"fast": 40, "max_candles": 104, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 7.5}` | 7,856.29 | 2.8 | -5.1 | 75.0 | 2,693.41 | 2.2 | -9.4 | 0.79 | 8/5 | 1.00 |
| 622 | `{"fast": 40, "max_candles": 96, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 7.5}` | 7,856.29 | 2.8 | -5.1 | 75.0 | 1,887.45 | 1.6 | -9.4 | 0.57 | 8/5 | not checked |
| 623 | `{"fast": 40, "max_candles": 112, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 7.5}` | 7,856.29 | 2.8 | -5.1 | 75.0 | 2,693.41 | 2.2 | -9.4 | 0.79 | 8/5 | not checked |
| 890 | `{"fast": 40, "max_candles": 120, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 7.5}` | 7,856.29 | 2.8 | -5.1 | 75.0 | 2,693.41 | 2.2 | -9.4 | 0.79 | 8/5 | not checked |
| 608 | `{"fast": 40, "max_candles": 104, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 6,553.45 | 2.4 | -4.8 | 75.0 | 2,193.74 | 1.8 | -6.6 | 0.76 | 8/5 | not checked |
| 632 | `{"fast": 40, "max_candles": 96, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 6,553.45 | 2.4 | -4.8 | 75.0 | 2,193.74 | 1.8 | -6.6 | 0.76 | 8/5 | not checked |
| 789 | `{"fast": 40, "max_candles": 112, "slow": 230, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 6,553.45 | 2.4 | -4.8 | 75.0 | 2,193.74 | 1.8 | -6.6 | 0.76 | 8/5 | not checked |
| 670 | `{"fast": 55, "max_candles": 120, "slow": 230, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 4,122.49 | 1.7 | -3.7 | 62.5 | 1,386.89 | 1.2 | -6.5 | 0.72 | 8/5 | not checked |
| 713 | `{"fast": 55, "max_candles": 128, "slow": 230, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 4,122.49 | 1.7 | -3.7 | 62.5 | 1,386.89 | 1.2 | -6.5 | 0.72 | 8/5 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

62 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ^IXIC | 88% | 1.8 | 4.6 | 9.5 | 0.7 | 2.0 | 56 |
| 2 | SOXX | 85% | 2.7 | 7.6 | 8.3 | 0.3 | -0.0 | 45 |
| 3 | SMH | 84% | 1.8 | 7.6 | 1.5 | -0.3 | 2.2 | 52 |
| 4 | XLY | 81% | 1.5 | 5.6 | 8.4 | 0.6 | 0.3 | 35 |
| 5 | ^RUT | 76% | 0.6 | 4.0 | 7.5 | -0.5 | 0.2 | 13 |
| 6 | ^DJI | 76% | 0.2 | 3.1 | 7.5 | 0.1 | 0.7 | 23 |
| 7 | ^FTSE | 73% | 0.6 | 1.8 | 3.5 | -0.9 | -0.1 | 18 |
| 8 | ^SSMI | 70% | 0.5 | 2.2 | 5.9 | 0.5 | -0.9 | 18 |
| 9 | XLB | 67% | 0.8 | 3.2 | 7.7 | -0.0 | 0.3 | 18 |
| 10 | XLV | 64% | 0.4 | 2.9 | 7.5 | 0.7 | -1.3 | 27 |
| 11 | QQQ | 61% | 1.4 | 6.9 | 2.4 | 0.3 | 2.3 | 39 |
| 12 | ^GSPC | 61% | 1.2 | 3.8 | 7.4 | 1.1 | 0.1 | 30 |
| 13 | XLK | 61% | 1.0 | 5.2 | -0.4 | 0.8 | 1.7 | 41 |
| 14 | ^N225 | 57% | 0.2 | 2.4 | -0.2 | -0.5 | -0.4 | 27 |
| 15 | DIA | 57% | 0.1 | 1.8 | 5.2 | -0.2 | -0.0 | 22 |
| 16 | SPY | 55% | 1.3 | 4.4 | 9.3 | 0.6 | 0.6 | 29 |
| 17 | TLT | 55% | 1.1 | 4.1 | 6.6 | 0.1 | -0.5 | 10 |
| 18 | XLF | 55% | 0.6 | 4.0 | 1.5 | 0.2 | 0.3 | 20 |
| 19 | IWM | 54% | 1.1 | 4.8 | 7.6 | 1.6 | 0.4 | 12 |
| 20 | ^GDAXI | 54% | 0.4 | 5.9 | 8.1 | 0.0 | -0.8 | 14 |
| 21 | EEM | 52% | 0.9 | 5.0 | 6.0 | 0.8 | -0.1 | 15 |
| 22 | IEF | 51% | 0.3 | 1.8 | 5.0 | 0.5 | 0.0 | 8 |
| 23 | XLU | 46% | 0.5 | 3.2 | 6.7 | 1.1 | 0.5 | 20 |
| 24 | VWO | 43% | 0.8 | 5.7 | 2.3 | -0.7 | -0.3 | 18 |
| 25 | XLP | 42% | 0.3 | 2.5 | 7.3 | -0.1 | 1.5 | 21 |
| 26 | XLI | 42% | 0.3 | 4.5 | 5.7 | -0.9 | 1.7 | 23 |
| 27 | IVV | 40% | 1.2 | 4.6 | 6.3 | -0.1 | 0.6 | 21 |
| 28 | EFA | 37% | 1.2 | 6.1 | 7.9 | 0.8 | -0.3 | 13 |
| 29 | VTI | 28% | 1.3 | 3.6 | 9.4 | 0.8 | 0.6 | 12 |
| 30 | LQD | 25% | 0.1 | 1.0 | 4.7 | 0.3 | -0.0 | 13 |
| 31 | XLE | 24% | 0.2 | 3.3 | 6.8 | -0.4 | 2.0 | 8 |
| 32 | AGG | 21% | 0.2 | 1.1 | 4.2 | -0.2 | -0.2 | 4 |
| 33 | VNQ | 19% | 1.7 | 6.1 | 6.8 | 0.5 | -1.9 | 6 |
| 34 | VUG | 18% | 1.3 | 3.4 | 8.6 | -0.0 | 2.5 | 9 |
| 35 | TIP | 18% | 0.2 | 1.0 | 3.8 | -0.3 | 0.0 | 7 |
| 36 | RSP | 15% | 1.0 | 4.6 | 8.1 | 0.4 | 0.5 | 8 |
| 37 | ^STOXX50E | 12% | 0.3 | 3.2 | 2.9 | -0.1 | -1.2 | 6 |
| 38 | VTV | 6% | 0.8 | 3.9 | 6.7 | -0.1 | 0.7 | 3 |
| 39 | GLD | 6% | -0.6 | 2.3 | 6.0 | -0.8 | 0.8 | 4 |
| 40 | DBC | 6% | -0.7 | 1.1 | -7.3 | 1.1 | 1.2 | 3 |

(22 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| SMH | max-income | [golden_cross__SMH__max-income__v001.md](symbols/SMH/golden_cross__SMH__max-income__v001.md) | 6.1 | 2.0 | 2.0 | -22.4 | 66.7 | 15/6 |
| SMH | balanced | [golden_cross__SMH__balanced__v001.md](symbols/SMH/golden_cross__SMH__balanced__v001.md) | 5.3 | 5.2 | 5.2 | -10.9 | 60.0 | 10/5 |
| SMH | safe-starter | [golden_cross__SMH__safe-starter__v001.md](symbols/SMH/golden_cross__SMH__safe-starter__v001.md) | 4.8 | 4.9 | 4.8 | -9.1 | 60.0 | 10/5 |
| SOXX | max-income | [golden_cross__SOXX__max-income__v001.md](symbols/SOXX/golden_cross__SOXX__max-income__v001.md) | 6.9 | 7.0 | 6.9 | -10.9 | 45.5 | 11/5 |
| SOXX | balanced | [golden_cross__SOXX__balanced__v001.md](symbols/SOXX/golden_cross__SOXX__balanced__v001.md) | 6.5 | 3.7 | 3.7 | -9.8 | 40.0 | 10/5 |
| SOXX | safe-starter | [golden_cross__SOXX__safe-starter__v002.md](symbols/SOXX/golden_cross__SOXX__safe-starter__v002.md) | 6.5 | 3.3 | 3.3 | -9.8 | 40.0 | 10/5 |
| XLY | max-income | [golden_cross__XLY__max-income__v001.md](symbols/XLY/golden_cross__XLY__max-income__v001.md) | 6.2 | 1.6 | 1.6 | -12.2 | 75.0 | 12/8 |
| XLY | balanced | [golden_cross__XLY__balanced__v002.md](symbols/XLY/golden_cross__XLY__balanced__v002.md) | 3.9 | 1.5 | 1.5 | -8.8 | 100.0 | 8/7 |
| XLY | safe-starter | [golden_cross__XLY__safe-starter__v002.md](symbols/XLY/golden_cross__XLY__safe-starter__v002.md) | 3.6 | 2.2 | 2.2 | -6.4 | 100.0 | 8/6 |
| ^IXIC | max-income | [golden_cross__^IXIC__max-income__v002.md](symbols/^IXIC/golden_cross__^IXIC__max-income__v002.md) | 7.5 | 4.8 | 4.8 | -14.4 | 85.0 | 20/9 |
| ^IXIC | balanced | [golden_cross__^IXIC__balanced__v002.md](symbols/^IXIC/golden_cross__^IXIC__balanced__v002.md) | 4.9 | 5.1 | 4.9 | -10.2 | 90.9 | 11/6 |
| ^IXIC | safe-starter | [golden_cross__^IXIC__safe-starter__v001.md](symbols/^IXIC/golden_cross__^IXIC__safe-starter__v001.md) | 2.8 | 3.7 | 2.8 | -5.3 | 90.0 | 10/6 |
| broad | max-income | [golden_cross__broad__max-income__v002.md](symbols/broad/golden_cross__broad__max-income__v002.md) | 1.7 | 3.8 | 1.7 | -7.3 | 46.5 | 652/615 |
| broad | balanced | [golden_cross__broad__balanced__v002.md](symbols/broad/golden_cross__broad__balanced__v002.md) | 0.7 | 0.2 | 0.2 | -4.1 | 54.2 | 391/386 |
| top3 | max-income | [golden_cross__top3__max-income__v001.md](symbols/top3/golden_cross__top3__max-income__v001.md) | 4.9 | 7.9 | 4.9 | -15.5 | 61.5 | 39/16 |
| top3 | balanced | [golden_cross__top3__balanced__v002.md](symbols/top3/golden_cross__top3__balanced__v002.md) | 2.5 | 4.7 | 2.5 | -7.7 | 64.3 | 28/15 |
| top3 | safe-starter | [golden_cross__top3__safe-starter__v002.md](symbols/top3/golden_cross__top3__safe-starter__v002.md) | 2.1 | 2.1 | 2.1 | -10.3 | 44.7 | 47/26 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,000 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
