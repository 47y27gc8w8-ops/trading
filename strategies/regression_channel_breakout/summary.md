# regression_channel_breakout: optimization summary

Updated 2026-11-25T11:48:55Z · backtest.py version `0e3504779a` · 982 parameter sets tested with this version (982 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [regression_channel_breakout__max-income__v002.md](regression_channel_breakout__max-income__v002.md) | 982 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [regression_channel_breakout__balanced__v001.md](regression_channel_breakout__balanced__v001.md) | 466 | `{"k": 1.8, "max_candles": 42, "n": 70, "stop_atr": 3.75, "take_profit_atr": 1.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [regression_channel_breakout__safe-starter__v002.md](regression_channel_breakout__safe-starter__v002.md) | 982 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |

Note: one parameter set wins max-income, safe-starter. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 12,302.60 | 2,987.85 | 5,686.23 | 1,366.84 | 12,302.60 | 2,987.85 |
| return % | 123.03 | 29.88 | 56.86 | 13.67 | 123.03 | 29.88 |
| return %/year | 5.0 | 2.4 | 2.8 | 1.2 | 5.0 | 2.4 |
| gross profit | 17,654.57 | 8,635.83 | 8,033.51 | 4,567.05 | 17,654.57 | 8,635.83 |
| gross loss | 5,351.97 | 5,647.97 | 2,347.28 | 3,200.22 | 5,351.97 | 5,647.97 |
| trades | 47 | 47 | 35 | 36 | 47 | 47 |
| win rate % | 70.2 | 70.2 | 80.0 | 75.0 | 70.2 | 70.2 |
| avg win | 534.99 | 261.69 | 286.91 | 169.15 | 534.99 | 261.69 |
| avg loss | -382.28 | -403.43 | -335.33 | -355.58 | -382.28 | -403.43 |
| avg result / trade | 261.76 | 63.57 | 162.46 | 37.97 | 261.76 | 63.57 |
| largest single loss | -619.20 | -819.23 | -557.21 | -655.91 | -619.20 | -819.23 |
| largest loss % of equity | -2.58 | -6.40 | -4.49 | -6.01 | -2.58 | -6.40 |
| max drawdown | -1,709.41 | -1,892.32 | -678.00 | -1,262.98 | -1,709.41 | -1,892.32 |
| max drawdown % | -7.12 | -13.06 | -6.33 | -11.58 | -7.12 | -13.06 |
| profit factor | 3.30 | 1.53 | 3.42 | 1.43 | 3.30 | 1.53 |
| unusually bad trades | 0 | 1 | 1 | 0 | 0 | 1 |
| … threshold (% of equity) | 4.1 | 6.1 | 4.1 | 7.1 | 4.1 | 6.1 |
| time in market % | 10.5 | 13.2 | 7.1 | 8.4 | 10.5 | 13.2 |
| buy & hold return % | 98.28 | 541.70 | 98.28 | 541.70 | 98.28 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.48 |  | 0.42 |  | 0.48 |
| period | 1999-09-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-09-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-09-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1999 | 23.6 | 15.1 | 23.6 |
| 2000 | 2.6 | 0.0 | 2.6 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 7.3 | 0.0 | 7.3 |
| 2003 | 6.4 | -1.9 | 6.4 |
| 2004 | 5.9 | 4.2 | 5.9 |
| 2005 | -0.2 | 3.3 | -0.2 |
| 2006 | 2.8 | 2.2 | 2.8 |
| 2007 | 7.5 | 3.6 | 7.5 |
| 2008 | 7.9 | 6.0 | 7.9 |
| 2009 | 4.3 | 6.2 | 4.3 |
| 2010 | 9.9 | 2.9 | 9.9 |
| 2011 | -2.8 | -3.4 | -2.8 |
| 2012 | 9.9 | 7.5 | 9.9 |
| 2013 | 1.5 | 0.3 | 1.5 |
| 2014 | 3.2 | 1.3 | 3.2 |
| 2015 | -4.6 | -0.2 | -4.6 |
| 2016 (OOS) | 5.9 | -0.0 | 5.9 |
| 2017 (OOS) | 5.5 | 4.4 | 5.5 |
| 2018 (OOS) | 1.5 | -4.1 | 1.5 |
| 2019 (OOS) | 6.7 | 1.7 | 6.7 |
| 2020 (OOS) | 5.5 | 0.6 | 5.5 |
| 2021 (OOS) | 0.6 | 0.6 | 0.6 |
| 2022 (OOS) | -4.8 | -4.5 | -4.8 |
| 2023 (OOS) | 13.2 | 5.1 | 13.2 |
| 2024 (OOS) | -2.0 | 4.9 | -2.0 |
| 2025 (OOS) | -7.1 | -3.7 | -7.1 |
| 2026 (OOS) | 3.1 | 8.6 | 3.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 7.1% from a peak in-sample and 13.1% out-of-sample, and the worst single trade cost 6.4% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 2.4% a year against 5.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 77% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 6.3% from a peak in-sample and 11.6% out-of-sample, and the worst single trade cost 6.0% of the account out-of-sample. About 80 of every 100 trades won in-sample. Out-of-sample it earned 1.2% a year against 2.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 86% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 7.1% from a peak in-sample and 13.1% out-of-sample, and the worst single trade cost 6.4% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 2.4% a year against 5.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 77% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 598 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 3.25, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,030.26 | 2.5 | -13.7 | 0.49 | 47/47 | not checked |
| 599 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,931.48 | 2.4 | -13.3 | 0.47 | 47/47 | not checked |
| 602 | `{"k": 1.5, "max_candles": 30, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,987.85 | 2.4 | -13.1 | 0.48 | 47/47 | not checked |
| 603 | `{"k": 1.5, "max_candles": 42, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,987.85 | 2.4 | -13.1 | 0.48 | 47/47 | not checked |
| 604 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,987.85 | 2.4 | -13.1 | 0.48 | 47/47 | 1.00 |
| 617 | `{"k": 1.5, "max_candles": 30, "n": 75, "stop_atr": 3.25, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,030.26 | 2.5 | -13.7 | 0.49 | 47/47 | not checked |
| 619 | `{"k": 1.5, "max_candles": 30, "n": 75, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,931.48 | 2.4 | -13.3 | 0.47 | 47/47 | not checked |
| 628 | `{"k": 1.5, "max_candles": 42, "n": 75, "stop_atr": 3.25, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,030.26 | 2.5 | -13.7 | 0.49 | 47/47 | not checked |
| 629 | `{"k": 1.5, "max_candles": 42, "n": 75, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,931.48 | 2.4 | -13.3 | 0.47 | 47/47 | not checked |
| 635 | `{"k": 1.5, "max_candles": 48, "n": 75, "stop_atr": 3.25, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,030.26 | 2.5 | -13.7 | 0.49 | 47/47 | not checked |
| 673 | `{"k": 1.5, "max_candles": 30, "n": 75, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,141.03 | 2.5 | -11.7 | 0.50 | 47/47 | not checked |
| 677 | `{"k": 1.5, "max_candles": 24, "n": 75, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,931.48 | 2.4 | -13.3 | 0.47 | 47/47 | not checked |
| 683 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,312.24 | 2.7 | -13.2 | 0.53 | 47/47 | not checked |
| 695 | `{"k": 1.5, "max_candles": 42, "n": 75, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,141.03 | 2.5 | -11.7 | 0.50 | 47/47 | not checked |
| 699 | `{"k": 1.5, "max_candles": 30, "n": 75, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,312.24 | 2.7 | -13.2 | 0.53 | 47/47 | not checked |
| 701 | `{"k": 1.5, "max_candles": 42, "n": 75, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,312.24 | 2.7 | -13.2 | 0.53 | 47/47 | not checked |
| 707 | `{"k": 1.5, "max_candles": 24, "n": 75, "stop_atr": 3.25, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,030.26 | 2.5 | -13.7 | 0.49 | 47/47 | not checked |
| 761 | `{"k": 1.5, "max_candles": 36, "n": 75, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,141.03 | 2.5 | -11.7 | 0.50 | 47/47 | not checked |
| 763 | `{"k": 1.5, "max_candles": 48, "n": 75, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,931.48 | 2.4 | -13.3 | 0.47 | 47/47 | not checked |
| 783 | `{"k": 1.5, "max_candles": 24, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,987.85 | 2.4 | -13.1 | 0.48 | 47/47 | not checked |
| 873 | `{"k": 1.5, "max_candles": 48, "n": 75, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 2,987.85 | 2.4 | -13.1 | 0.48 | 47/47 | not checked |
| 888 | `{"k": 1.5, "max_candles": 48, "n": 75, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,312.24 | 2.7 | -13.2 | 0.53 | 47/47 | not checked |
| 906 | `{"k": 1.5, "max_candles": 24, "n": 75, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,312.24 | 2.7 | -13.2 | 0.53 | 47/47 | not checked |
| 965 | `{"k": 1.5, "max_candles": 24, "n": 75, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 12,302.60 | 5.0 | -7.1 | 70.2 | 3,141.03 | 2.5 | -11.7 | 0.50 | 47/47 | not checked |
| 519 | `{"k": 1.6, "max_candles": 78, "n": 120, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 6,454.27 | 3.1 | -5.8 | 62.5 | 891.09 | 0.8 | -13.4 | 0.26 | 32/31 | not checked |

(2 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

48 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | GLD | 52% | 0.4 | 4.9 | 8.7 | 1.8 | 2.9 | 22 |
| 2 | XLK | 43% | 0.4 | 3.2 | 1.6 | 1.7 | 2.0 | 20 |
| 3 | SPY | 42% | 0.2 | 2.3 | 9.3 | 0.4 | 0.8 | 18 |
| 4 | TLT | 37% | 0.1 | 3.1 | 6.5 | 0.8 | 0.2 | 13 |
| 5 | QQQ | 35% | 0.6 | 5.0 | 4.3 | 1.9 | 0.1 | 13 |
| 6 | IEF | 35% | 0.1 | 1.4 | 5.2 | -0.3 | 0.2 | 4 |
| 7 | LQD | 32% | 0.0 | 0.8 | 5.3 | 0.1 | 0.0 | 16 |
| 8 | VWO | 32% | -0.1 | 4.0 | 4.3 | 1.3 | 1.0 | 12 |
| 9 | XLE | 31% | 0.3 | 1.9 | 6.7 | 1.4 | 0.1 | 12 |
| 10 | EFA | 29% | 0.1 | 2.0 | 5.4 | 0.5 | 0.8 | 11 |
| 11 | VTI | 26% | 0.1 | 2.0 | 7.0 | 0.3 | 0.6 | 11 |
| 12 | IVV | 25% | 0.2 | 1.4 | 4.8 | 0.4 | 0.8 | 13 |
| 13 | DIA | 25% | 0.0 | 0.9 | 6.2 | -0.3 | -0.5 | 2 |
| 14 | EEM | 25% | -0.6 | 4.6 | 7.4 | -0.1 | -0.1 | 11 |
| 15 | XLP | 23% | 0.0 | 1.2 | 6.6 | 0.3 | 0.3 | 7 |
| 16 | SLV | 22% | -0.5 | 4.9 | 0.6 | 1.1 | 2.1 | 13 |
| 17 | VUG | 20% | 0.0 | 1.8 | 9.1 | -0.1 | -0.1 | 11 |
| 18 | AGG | 20% | -0.2 | 1.5 | 4.1 | 0.3 | 0.1 | 10 |
| 19 | TQQQ | 18% | 0.5 | 13.0 | 55.2 | 4.4 | 1.0 | 1 |
| 20 | VTV | 18% | 0.0 | 2.0 | 7.6 | 0.1 | -0.2 | 5 |
| 21 | XLV | 17% | -0.4 | 0.8 | 7.1 | 0.8 | 0.8 | 11 |
| 22 | SMH | 15% | -0.4 | 1.2 | 1.0 | -1.2 | -1.9 | 9 |
| 23 | SOXX | 15% | -0.5 | 2.6 | 2.9 | 0.1 | -1.3 | 8 |
| 24 | RSP | 14% | 0.0 | 2.4 | 9.0 | 0.4 | 0.3 | 0 |
| 25 | XLF | 14% | -0.2 | 1.7 | 1.6 | 1.1 | -0.8 | 5 |
| 26 | HYG | 14% | -0.5 | 1.6 | 4.2 | -1.8 | -0.3 | 0 |
| 27 | VNQ | 14% | -0.8 | 1.4 | 8.9 | 0.3 | -1.3 | 0 |
| 28 | XLI | 11% | -0.1 | 0.5 | 5.5 | -0.1 | 0.2 | 5 |
| 29 | XLU | 11% | -0.7 | 0.8 | 6.0 | -1.0 | -0.1 | 3 |
| 30 | BND | 9% | -0.2 | 0.6 | 4.3 | -0.9 | 0.4 | 4 |
| 31 | XLY | 9% | -0.2 | 0.7 | 7.5 | -0.4 | 0.3 | 2 |
| 32 | USO | 9% | -0.8 | 1.3 | -15.8 | -0.7 | 1.0 | 4 |
| 33 | USMV | 8% | 0.5 | 2.4 | 13.2 | 1.8 | -0.2 | 3 |
| 34 | VOO | 8% | 0.0 | 2.1 | 12.5 | 0.1 | 0.8 | 3 |
| 35 | VT | 8% | 0.0 | 2.2 | 10.8 | -0.1 | -0.2 | 0 |
| 36 | VIG | 8% | -0.1 | 1.1 | 6.6 | -0.1 | 0.6 | 2 |
| 37 | ACWI | 6% | -0.2 | 1.9 | 6.4 | -1.1 | 0.2 | 0 |
| 38 | IWM | 6% | -0.3 | 0.4 | 7.7 | -0.3 | -1.3 | 0 |
| 39 | VEA | 5% | -0.3 | 1.1 | 0.9 | -0.9 | 0.1 | 0 |
| 40 | VXUS | 5% | -0.4 | 1.1 | 2.3 | 0.7 | -0.1 | 0 |

(8 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [regression_channel_breakout__broad__max-income__v001.md](symbols/broad/regression_channel_breakout__broad__max-income__v001.md) | 0.3 | 0.2 | 0.2 | -8.9 | 44.2 | 2043/2203 |
| broad | balanced | [regression_channel_breakout__broad__balanced__v001.md](symbols/broad/regression_channel_breakout__broad__balanced__v001.md) | 0.3 | 0.4 | 0.3 | -7.1 | 46.8 | 2006/2158 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 982 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
