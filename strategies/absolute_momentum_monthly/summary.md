# absolute_momentum_monthly: optimization summary

Updated 2026-11-24T23:06:46Z · backtest.py version `a4a2e56694` · 94,821 parameter sets tested with this version (94,821 rows in results.csv in total) · last run ended: screen

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 12 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [absolute_momentum_monthly__max-income__v001.md](absolute_momentum_monthly__max-income__v001.md) | 94319 | `{"hurdle": 2.75, "max_candles": 9, "n": 15, "stop_atr": 3.0, "take_profit_atr": 5.0}` | long SPY since 2026-06-01 00:00 @ 751.778176 |
| balanced | [absolute_momentum_monthly__balanced__v001.md](absolute_momentum_monthly__balanced__v001.md) | 94320 | `{"hurdle": 0.25, "max_candles": 10, "n": 7, "stop_atr": 3.5, "take_profit_atr": 4.0}` | long SPY since 2026-05-01 00:00 @ 717.829936 |
| safe-starter | [absolute_momentum_monthly__safe-starter__v001.md](absolute_momentum_monthly__safe-starter__v001.md) | 94321 | `{"hurdle": 3.0, "max_candles": 17, "n": 15, "stop_atr": 3.25, "take_profit_atr": 4.5}` | long SPY since 2026-05-01 00:00 @ 717.829936 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 118,713.21 | 16,325.61 | 77,135.51 | 14,168.73 | 90,748.60 | 15,767.48 |
| return % | 1,187.13 | 163.26 | 771.36 | 141.69 | 907.49 | 157.67 |
| return %/year | 13.0 | 9.3 | 10.9 | 8.4 | 11.7 | 9.1 |
| gross profit | 125,457.49 | 25,410.30 | 89,917.72 | 15,673.93 | 90,748.60 | 31,264.03 |
| gross loss | 6,744.28 | 9,084.69 | 12,782.21 | 1,505.20 | -0.00 | 15,496.55 |
| trades | 22 | 14 | 26 | 13 | 15 | 13 |
| win rate % | 90.9 | 64.3 | 73.1 | 76.9 | 100.0 | 61.5 |
| avg win | 6,272.87 | 2,823.37 | 4,732.51 | 1,567.39 | 6,049.91 | 3,908.00 |
| avg loss | -3,372.14 | -1,816.94 | -1,826.03 | -501.73 | 0.00 | -3,099.31 |
| avg result / trade | 5,396.06 | 1,166.12 | 2,966.75 | 1,089.90 | 6,049.91 | 1,212.88 |
| largest single loss | -3,799.53 | -2,640.16 | -3,542.88 | -554.70 | 0.00 | -4,519.82 |
| largest loss % of equity | -6.01 | -18.35 | -13.90 | -3.13 | 0.00 | -18.48 |
| max drawdown | -15,932.18 | -6,842.46 | -5,914.17 | -3,332.78 | -10,394.72 | -7,708.22 |
| max drawdown % | -17.31 | -28.38 | -21.15 | -16.76 | -17.96 | -29.60 |
| profit factor | 18.60 | 2.80 | 7.04 | 10.41 | 999.00 | 2.02 |
| unusually bad trades | 0 | 1 | 1 | 0 | 0 | 0 |
| … threshold (% of equity) | 8.2 | 18.1 | 9.0 | 5.2 | 2.0 | 34.4 |
| time in market % | 68.6 | 78.5 | 68.6 | 77.7 | 71.2 | 80.8 |
| buy & hold return % | 529.96 | 328.39 | 529.96 | 328.39 | 529.96 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.72 |  | 0.77 |  | 0.78 |
| period | 1995-01-27 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-27 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-27 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 26.3 | 33.1 | 24.2 |
| 1996 | 24.4 | 22.4 | 22.6 |
| 1997 | 40.2 | 33.7 | 30.8 |
| 1998 | 49.5 | 7.2 | 32.5 |
| 1999 | 21.0 | 12.7 | 25.6 |
| 2000 | 4.7 | -7.5 | -1.1 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 0.0 | -8.0 | 0.0 |
| 2003 | 5.6 | 22.4 | 5.6 |
| 2004 | 9.8 | 3.9 | 10.7 |
| 2005 | 4.3 | 6.7 | 3.9 |
| 2006 | 14.4 | 13.1 | 13.8 |
| 2007 | 9.4 | 5.7 | 5.1 |
| 2008 | -6.0 | 0.0 | -5.7 |
| 2009 | 0.0 | 21.8 | 0.0 |
| 2010 | 17.2 | 12.7 | 18.5 |
| 2011 | 10.0 | 4.9 | 2.7 |
| 2012 | 14.0 | 9.4 | 16.0 |
| 2013 | 28.5 | 30.0 | 27.2 |
| 2014 | 11.0 | 15.2 | 13.7 |
| 2015 | 3.5 | 1.6 | 10.1 |
| 2016 (OOS) | 3.5 | 9.1 | 3.5 |
| 2017 (OOS) | 14.4 | 16.0 | 18.4 |
| 2018 (OOS) | 2.0 | 1.2 | -4.2 |
| 2019 (OOS) | 15.4 | 10.7 | 21.3 |
| 2020 (OOS) | 20.6 | 8.6 | 33.6 |
| 2021 (OOS) | 34.5 | 26.2 | 28.3 |
| 2022 (OOS) | -20.2 | -13.0 | -21.6 |
| 2023 (OOS) | -3.7 | 5.1 | -3.7 |
| 2024 (OOS) | 21.5 | 24.3 | 21.8 |
| 2025 (OOS) | 15.7 | 11.5 | 2.6 |
| 2026 (OOS) | 1.7 | -3.5 | 5.4 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.3% from a peak in-sample and 28.4% out-of-sample, and the worst single trade cost 18.4% of the account out-of-sample. About 91 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 21.1% from a peak in-sample and 16.8% out-of-sample, and the worst single trade cost 3.1% of the account out-of-sample. About 73 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 47% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 18.0% from a peak in-sample and 29.6% out-of-sample, and the worst single trade cost 18.5% of the account out-of-sample. About 100 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 34% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20129 | `{"hurdle": 2.5, "max_candles": 9, "n": 15, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 20130 | `{"hurdle": 3.0, "max_candles": 9, "n": 15, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 20131 | `{"hurdle": 2.75, "max_candles": 9, "n": 15, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 14,598.36 | 8.6 | -28.4 | 0.66 | 22/14 | not checked |
| 20132 | `{"hurdle": 2.75, "max_candles": 9, "n": 15, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 20137 | `{"hurdle": 2.75, "max_candles": 9, "n": 15, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | 1.00 |
| 21775 | `{"hurdle": 2.25, "max_candles": 9, "n": 15, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 14,199.91 | 8.5 | -28.4 | 0.65 | 22/14 | not checked |
| 50760 | `{"hurdle": 2.5, "max_candles": 9, "n": 15, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 14,598.36 | 8.6 | -28.4 | 0.66 | 22/14 | not checked |
| 88040 | `{"hurdle": 2.25, "max_candles": 9, "n": 15, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 14,630.81 | 8.6 | -28.4 | 0.66 | 22/14 | not checked |
| 94327 | `{"hurdle": 2.75, "max_candles": 9, "n": 15, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 15,640.83 | 9.0 | -28.4 | 0.70 | 22/14 | not checked |
| 94338 | `{"hurdle": 2.75, "max_candles": 9, "n": 15, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 94383 | `{"hurdle": 3.0, "max_candles": 9, "n": 15, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 94391 | `{"hurdle": 3.0, "max_candles": 9, "n": 15, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 14,598.36 | 8.6 | -28.4 | 0.66 | 22/14 | not checked |
| 94425 | `{"hurdle": 3.0, "max_candles": 9, "n": 15, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 94460 | `{"hurdle": 2.25, "max_candles": 9, "n": 15, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,057.51 | 9.2 | -28.4 | 0.71 | 22/14 | not checked |
| 94504 | `{"hurdle": 2.25, "max_candles": 9, "n": 15, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 14,886.61 | 8.7 | -28.4 | 0.67 | 22/14 | not checked |
| 94537 | `{"hurdle": 2.5, "max_candles": 9, "n": 15, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 94594 | `{"hurdle": 2.5, "max_candles": 9, "n": 15, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 15,640.83 | 9.0 | -28.4 | 0.70 | 22/14 | not checked |
| 94687 | `{"hurdle": 3.25, "max_candles": 9, "n": 15, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 94781 | `{"hurdle": 3.25, "max_candles": 9, "n": 15, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 118,713.21 | 13.0 | -17.3 | 90.9 | 16,325.61 | 9.3 | -28.4 | 0.72 | 22/14 | not checked |
| 14202 | `{"hurdle": 2.5, "max_candles": 9, "n": 14, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 101,437.71 | 12.2 | -16.5 | 90.9 | 10,059.99 | 6.6 | -32.0 | 0.54 | 22/15 | not checked |
| 20127 | `{"hurdle": 2.75, "max_candles": 9, "n": 14, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 101,437.71 | 12.2 | -16.5 | 90.9 | 12,904.75 | 7.9 | -29.8 | 0.65 | 22/15 | not checked |
| 94361 | `{"hurdle": 2.75, "max_candles": 9, "n": 14, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 101,437.71 | 12.2 | -16.5 | 90.9 | 11,970.19 | 7.5 | -30.9 | 0.61 | 22/15 | not checked |
| 94483 | `{"hurdle": 2.5, "max_candles": 9, "n": 14, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 101,437.71 | 12.2 | -16.5 | 90.9 | 12,904.75 | 7.9 | -29.8 | 0.65 | 22/15 | not checked |
| 94591 | `{"hurdle": 2.75, "max_candles": 9, "n": 14, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 101,437.71 | 12.2 | -16.5 | 90.9 | 10,059.99 | 6.6 | -32.0 | 0.54 | 22/15 | not checked |
| 94674 | `{"hurdle": 2.5, "max_candles": 9, "n": 14, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 101,437.71 | 12.2 | -16.5 | 90.9 | 11,970.19 | 7.5 | -30.9 | 0.61 | 22/15 | not checked |

(12 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

52 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SPY | 100% | 8.9 | 13.0 | 9.2 | 9.2 | 8.1 | 64 |
| 2 | XLV | 100% | 4.6 | 6.8 | 8.4 | 6.8 | 2.6 | 59 |
| 3 | XLP | 97% | 3.9 | 7.2 | 6.5 | 5.2 | 2.3 | 36 |
| 4 | XLY | 95% | 5.6 | 7.5 | 9.8 | 6.5 | 5.8 | 59 |
| 5 | QQQ | 94% | 5.5 | 8.6 | 6.4 | 5.4 | 13.7 | 60 |
| 6 | XLB | 94% | 3.5 | 7.5 | 7.8 | 4.2 | 1.9 | 51 |
| 7 | XLE | 91% | 5.2 | 9.4 | 6.2 | 8.5 | 6.6 | 51 |
| 8 | XLK | 91% | 3.2 | 6.9 | 3.4 | 5.6 | 14.5 | 58 |
| 9 | XLI | 88% | 5.1 | 8.9 | 5.9 | 5.0 | 5.5 | 50 |
| 10 | IWM | 86% | 5.4 | 9.7 | 8.1 | 7.6 | 2.9 | 35 |
| 11 | DIA | 84% | 4.1 | 5.5 | 4.9 | 4.0 | 3.7 | 54 |
| 12 | EFA | 84% | 4.0 | 8.0 | 6.3 | 4.6 | 3.1 | 50 |
| 13 | XLU | 81% | 6.7 | 9.5 | 5.8 | 6.7 | 3.6 | 51 |
| 14 | TLT | 80% | 2.3 | 4.3 | 7.2 | 2.5 | -2.3 | 15 |
| 15 | XLF | 80% | 2.0 | 5.3 | 1.0 | 1.3 | 2.5 | 48 |
| 16 | IVV | 72% | 6.1 | 9.9 | 6.9 | 6.5 | 8.1 | 46 |
| 17 | VTI | 72% | 4.9 | 8.7 | 8.7 | 4.5 | 5.7 | 46 |
| 18 | EEM | 66% | 2.6 | 9.4 | 5.3 | 2.8 | 6.4 | 42 |
| 19 | IEF | 64% | 2.8 | 4.3 | 5.3 | 3.0 | 0.2 | 17 |
| 20 | SMH | 64% | 1.7 | 8.2 | 3.8 | 0.4 | 18.8 | 41 |
| 21 | GLD | 59% | 5.6 | 11.2 | 5.7 | 7.2 | 7.3 | 36 |
| 22 | VUG | 55% | 3.2 | 7.1 | 8.2 | 2.0 | 9.7 | 35 |
| 23 | RSP | 52% | 3.6 | 8.6 | 8.7 | 3.0 | 4.0 | 32 |
| 24 | VTV | 47% | 2.5 | 8.2 | 6.1 | 2.2 | 4.1 | 30 |
| 25 | SOXX | 45% | 0.5 | 6.3 | 6.1 | -3.8 | 19.8 | 29 |
| 26 | LQD | 44% | 2.9 | 3.8 | 5.1 | 2.3 | 1.9 | 22 |
| 27 | VNQ | 39% | 5.5 | 10.5 | 5.7 | 7.4 | -1.7 | 5 |
| 28 | AGG | 38% | 1.9 | 3.0 | 4.2 | 1.9 | 0.9 | 17 |
| 29 | TIP | 25% | 1.9 | 3.7 | 3.9 | 1.4 | 1.3 | 14 |
| 30 | SHY | 19% | 0.8 | 1.1 | 2.2 | 1.1 | 0.7 | 12 |
| 31 | VIG | 14% | 5.5 | 6.1 | 6.8 | 6.4 | 5.3 | 9 |
| 32 | VWO | 14% | -1.7 | 3.6 | 1.0 | -1.2 | 5.0 | 9 |
| 33 | IWDA.AS | 9% | 12.7 | 13.9 | 18.2 | 9.1 | 3.2 | 6 |
| 34 | HYG | 9% | 5.3 | 6.0 | 9.2 | 4.3 | 2.1 | 6 |
| 35 | TQQQ | 6% | 31.2 | 22.6 | 49.9 | 35.6 | 8.5 | 4 |
| 36 | CSNDX.SW | 3% | 15.9 | 14.1 | 19.0 | 17.7 | 13.9 | 2 |
| 37 | CSSMI.SW | 3% | 3.9 | 2.4 | 6.8 | 0.8 | 1.5 | 2 |
| 38 | BND | 3% | 3.0 | 2.9 | 3.9 | 3.1 | 1.1 | 1 |
| 39 | SLV | 3% | -1.0 | 3.8 | -2.9 | -1.8 | 0.2 | 2 |
| 40 | CSSPX.SW | 0% | 11.3 | n/a | 14.3 | 10.2 | 8.6 | 0 |

(12 more in screen.csv)


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 94,821 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
