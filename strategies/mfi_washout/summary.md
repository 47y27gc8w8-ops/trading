# mfi_washout: optimization summary

Updated 2026-11-26T02:08:52Z · backtest.py version `9fc21f0042` · 1,680 parameter sets tested with this version (1,680 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: MSFT (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [mfi_washout__max-income__v002.md](mfi_washout__max-income__v002.md) | 1179 | `{"level": 34, "max_candles": 36, "n": 15, "stop_atr": 3.0, "take_profit_atr": 4.0}` | long MSFT since 2026-11-24 00:00 @ 490.277044 |
| balanced | [mfi_washout__balanced__v002.md](mfi_washout__balanced__v002.md) | 1180 | `{"level": 34, "max_candles": 32, "n": 15, "stop_atr": 2.75, "take_profit_atr": 3.5}` | long MSFT since 2026-11-24 00:00 @ 490.277044 |
| safe-starter | [mfi_washout__safe-starter__v001.md](mfi_washout__safe-starter__v001.md) | 1181 | `{"level": 34, "max_candles": 30, "n": 15, "stop_atr": 2.25, "take_profit_atr": 3.5}` | long MSFT since 2026-11-24 00:00 @ 490.277044 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 20,288.64 | 7,206.53 | 16,918.12 | 5,845.20 | 14,439.71 | 4,410.48 |
| return % | 202.89 | 72.07 | 169.18 | 58.45 | 144.40 | 44.10 |
| return %/year | 5.4 | 5.1 | 4.8 | 4.3 | 4.3 | 3.4 |
| gross profit | 43,235.37 | 15,025.31 | 34,729.76 | 14,555.12 | 32,036.47 | 13,133.76 |
| gross loss | 22,946.74 | 7,818.78 | 17,811.64 | 8,709.92 | 17,596.76 | 8,723.28 |
| trades | 50 | 30 | 50 | 30 | 52 | 32 |
| win rate % | 72.0 | 70.0 | 68.0 | 70.0 | 61.5 | 62.5 |
| avg win | 1,200.98 | 715.49 | 1,021.46 | 693.10 | 1,001.14 | 656.69 |
| avg loss | -1,639.05 | -868.75 | -1,113.23 | -967.77 | -879.84 | -726.94 |
| avg result / trade | 405.77 | 240.22 | 338.36 | 194.84 | 277.69 | 137.83 |
| largest single loss | -3,449.36 | -1,904.41 | -2,603.53 | -1,741.24 | -1,993.73 | -1,500.64 |
| largest loss % of equity | -12.56 | -9.16 | -11.53 | -9.16 | -9.45 | -9.19 |
| max drawdown | -6,340.30 | -3,977.92 | -4,379.85 | -3,631.69 | -4,682.80 | -3,680.44 |
| max drawdown % | -19.80 | -19.09 | -18.85 | -18.96 | -17.94 | -21.33 |
| profit factor | 1.88 | 1.92 | 1.95 | 1.67 | 1.82 | 1.51 |
| unusually bad trades | 1 | 0 | 1 | 0 | 1 | 0 |
| … threshold (% of equity) | 10.8 | 11.6 | 9.9 | 10.7 | 8.5 | 9.7 |
| time in market % | 13.9 | 16.7 | 12.8 | 16.1 | 11.8 | 14.8 |
| buy & hold return % | 1,968.97 | 944.05 | 1,968.97 | 944.05 | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.94 |  | 0.89 |  | 0.78 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 17.8 | 14.4 | 15.1 |
| 1996 | 20.6 | 8.3 | -2.9 |
| 1997 | 7.1 | 4.0 | 6.5 |
| 1998 | 40.7 | 39.1 | 39.1 |
| 1999 | 28.2 | 26.0 | 27.4 |
| 2000 | -12.0 | -11.0 | -8.9 |
| 2001 | 1.7 | 1.1 | 2.8 |
| 2002 | -3.0 | -3.0 | -3.0 |
| 2003 | 14.9 | 14.9 | 7.8 |
| 2004 | -3.7 | -3.3 | -2.5 |
| 2005 | -7.3 | -7.1 | -6.1 |
| 2006 | 8.2 | 7.6 | 4.5 |
| 2007 | 5.2 | 3.3 | 3.5 |
| 2008 | 10.7 | 9.4 | 9.4 |
| 2009 | 0.0 | 0.0 | 0.0 |
| 2010 | 6.4 | 6.4 | 6.4 |
| 2011 | -3.9 | -3.5 | -2.6 |
| 2012 | -0.1 | 10.6 | 11.4 |
| 2013 | -4.0 | -3.6 | -2.7 |
| 2014 | 8.4 | 6.6 | 8.2 |
| 2015 | -7.3 | -6.9 | -10.0 |
| 2016 (OOS) | 13.1 | 12.4 | 3.4 |
| 2017 (OOS) | 5.0 | 5.9 | 6.8 |
| 2018 (OOS) | -0.3 | 1.5 | 3.1 |
| 2019 (OOS) | 0.0 | 0.0 | 0.0 |
| 2020 (OOS) | 28.8 | 28.8 | 28.8 |
| 2021 (OOS) | 25.2 | 23.1 | 17.8 |
| 2022 (OOS) | -7.2 | -15.5 | -20.5 |
| 2023 (OOS) | 12.6 | 12.6 | 12.6 |
| 2024 (OOS) | -4.2 | -4.5 | 0.5 |
| 2025 (OOS) | -9.9 | -9.0 | -7.2 |
| 2026 (OOS) | 0.0 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 19.8% from a peak in-sample and 19.1% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 72 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 51% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 18.9% from a peak in-sample and 19.0% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 68 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 17.9% from a peak in-sample and 21.3% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 47% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 678 | `{"level": 34, "max_candles": 36, "n": 15, "stop_atr": 3.0, "take_profit_atr": 4.0}` | 20,288.64 | 5.4 | -19.8 | 72.0 | 7,206.53 | 5.1 | -19.1 | 0.94 | 50/30 | 1.00 |
| 535 | `{"level": 34, "max_candles": 36, "n": 15, "stop_atr": 2.75, "take_profit_atr": 4.0}` | 18,751.77 | 5.2 | -18.9 | 70.0 | 6,051.76 | 4.4 | -18.7 | 0.86 | 50/30 | not checked |
| 511 | `{"level": 34, "max_candles": 30, "n": 15, "stop_atr": 2.25, "take_profit_atr": 4.0}` | 15,053.48 | 4.5 | -17.4 | 59.6 | 4,761.52 | 3.6 | -21.3 | 0.81 | 52/32 | not checked |
| 1278 | `{"level": 34, "max_candles": 22, "n": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 2,256.25 | 1.0 | -17.4 | 43.8 | 4,705.65 | 3.6 | -13.7 | 3.72 | 73/58 | not checked |
| 1288 | `{"level": 34, "max_candles": 24, "n": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 2,256.25 | 1.0 | -17.4 | 43.8 | 4,705.65 | 3.6 | -13.7 | 3.72 | 73/58 | not checked |
| 1320 | `{"level": 34, "max_candles": 26, "n": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 2,256.25 | 1.0 | -17.4 | 43.8 | 4,705.65 | 3.6 | -13.7 | 3.72 | 73/58 | not checked |
| 1365 | `{"level": 34, "max_candles": 28, "n": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 2,256.25 | 1.0 | -17.4 | 43.8 | 4,705.65 | 3.6 | -13.7 | 3.72 | 73/58 | not checked |
| 1408 | `{"level": 34, "max_candles": 30, "n": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 2,256.25 | 1.0 | -17.4 | 43.8 | 4,705.65 | 3.6 | -13.7 | 3.72 | 73/58 | not checked |
| 1530 | `{"level": 34, "max_candles": 32, "n": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 2,256.25 | 1.0 | -17.4 | 43.8 | 4,705.65 | 3.6 | -13.7 | 3.72 | 73/58 | not checked |
| 1328 | `{"level": 34, "max_candles": 26, "n": 13, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 1,721.82 | 0.8 | -17.3 | 49.3 | 1,772.13 | 1.5 | -15.8 | 1.99 | 73/58 | not checked |
| 1336 | `{"level": 34, "max_candles": 24, "n": 13, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 1,721.82 | 0.8 | -17.3 | 49.3 | 1,772.13 | 1.5 | -15.8 | 1.99 | 73/58 | not checked |
| 1416 | `{"level": 34, "max_candles": 22, "n": 13, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 1,721.82 | 0.8 | -17.3 | 49.3 | 1,772.13 | 1.5 | -15.8 | 1.99 | 73/58 | not checked |
| 1427 | `{"level": 34, "max_candles": 28, "n": 13, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 1,721.82 | 0.8 | -17.3 | 49.3 | 1,772.13 | 1.5 | -15.8 | 1.99 | 73/58 | not checked |
| 1430 | `{"level": 34, "max_candles": 30, "n": 13, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 1,721.82 | 0.8 | -17.3 | 49.3 | 1,772.13 | 1.5 | -15.8 | 1.99 | 73/58 | not checked |
| 1493 | `{"level": 34, "max_candles": 32, "n": 13, "stop_atr": 1.0, "take_profit_atr": 1.5}` | 1,721.82 | 0.8 | -17.3 | 49.3 | 1,772.13 | 1.5 | -15.8 | 1.99 | 73/58 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

469 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | BRO | 60% | 1.3 | 3.8 | 16.1 | 1.3 | 0.9 | 26 |
| 2 | MTB | 58% | 0.9 | 6.2 | 13.4 | 0.9 | -0.8 | 13 |
| 3 | PSA | 57% | 1.1 | 5.2 | 19.1 | 1.2 | -0.7 | 15 |
| 4 | REG | 57% | 0.8 | 8.5 | 13.3 | 1.3 | 0.5 | 15 |
| 5 | ROP | 55% | 1.7 | 5.3 | 18.5 | 1.3 | 0.4 | 6 |
| 6 | IRM | 55% | 1.6 | 4.3 | 11.0 | 1.4 | 0.6 | 21 |
| 7 | AJG | 55% | 0.5 | 3.5 | 12.0 | 0.1 | -1.6 | 18 |
| 8 | CRH | 55% | 0.3 | 4.3 | 11.2 | 1.6 | 0.2 | 9 |
| 9 | ESS | 54% | 1.2 | 5.8 | 18.9 | 1.0 | -0.1 | 9 |
| 10 | KIM | 54% | 0.8 | 3.8 | 11.2 | 1.3 | 0.2 | 5 |
| 11 | CB | 54% | 0.7 | 6.0 | 16.0 | -0.5 | -0.4 | 20 |
| 12 | NVO | 52% | 0.9 | 6.5 | 23.4 | 1.5 | 2.1 | 20 |
| 13 | FRT | 52% | 0.8 | 4.1 | 15.5 | 0.3 | -0.3 | 7 |
| 14 | STZ | 51% | 1.7 | 7.1 | 17.6 | 0.7 | 0.7 | 5 |
| 15 | SPG | 51% | 0.7 | 4.4 | 16.6 | 0.7 | -0.4 | 5 |
| 16 | NVR | 49% | 1.1 | 5.1 | 31.2 | 0.3 | -0.0 | 20 |
| 17 | JKHY | 49% | 0.9 | 4.9 | 21.6 | 0.1 | 0.4 | 12 |
| 18 | ORLY | 49% | 0.8 | 5.0 | 23.4 | 1.6 | 0.7 | 15 |
| 19 | SIKA.SW | 49% | 0.5 | 5.5 | 15.0 | -0.3 | -0.3 | 11 |
| 20 | ILMN | 48% | 2.5 | 15.2 | 27.5 | 0.7 | 1.6 | 14 |
| 21 | NI | 48% | 0.8 | 4.3 | 10.9 | 0.6 | -0.3 | 12 |
| 22 | CPRT | 48% | 0.8 | 6.0 | 16.6 | -0.1 | -0.0 | 24 |
| 23 | UNH | 46% | 1.4 | 5.6 | 16.1 | 0.4 | 0.6 | 25 |
| 24 | EG | 46% | 1.2 | 6.3 | 12.6 | 0.1 | 0.3 | 23 |
| 25 | CPT | 46% | 0.8 | 4.7 | 11.8 | 1.2 | 0.6 | 19 |
| 26 | UHS | 46% | 0.7 | 4.9 | 19.5 | 0.7 | 0.7 | 15 |
| 27 | CHD | 46% | 0.7 | 6.0 | 18.8 | 1.2 | -0.1 | 12 |
| 28 | LNT | 46% | 0.5 | 5.2 | 9.6 | 1.2 | -0.4 | 18 |
| 29 | EVRG | 46% | 0.5 | 3.7 | 7.7 | -0.1 | 0.3 | 14 |
| 30 | CCI | 45% | 2.3 | 12.9 | 10.9 | 2.7 | -0.8 | 1 |
| 31 | TJX | 45% | 1.8 | 7.7 | 24.1 | 1.8 | 0.1 | 20 |
| 32 | DHI | 45% | 1.0 | 9.6 | 16.9 | 0.7 | -1.7 | 6 |
| 33 | MNST | 45% | 0.7 | 11.8 | 40.8 | -0.7 | 0.1 | 11 |
| 34 | BMY | 45% | 0.7 | 3.5 | 11.9 | -1.2 | -0.3 | 11 |
| 35 | AEP | 45% | 0.3 | 4.5 | 8.1 | 0.3 | 0.1 | 9 |
| 36 | WEC | 45% | 0.2 | 3.8 | 10.9 | -0.1 | 0.2 | 10 |
| 37 | WST | 45% | 0.2 | 3.5 | 13.0 | -1.5 | 0.9 | 12 |
| 38 | EQT | 45% | 0.0 | 5.3 | 12.8 | -0.9 | 2.3 | 27 |
| 39 | OKE | 43% | 1.1 | 6.6 | 13.5 | 1.1 | 2.7 | 19 |
| 40 | SPGI | 43% | 0.7 | 5.6 | 15.1 | 1.0 | -0.7 | 1 |

(429 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [mfi_washout__broad__max-income__v002.md](symbols/broad/mfi_washout__broad__max-income__v002.md) | 2.6 | 2.5 | 2.5 | -9.9 | 63.6 | 33340/19588 |
| broad | balanced | [mfi_washout__broad__balanced__v001.md](symbols/broad/mfi_washout__broad__balanced__v001.md) | 0.7 | 0.5 | 0.5 | -1.9 | 61.9 | 8433/4342 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,680 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
