# relative_volume_price_thrust: optimization summary

Updated 2026-11-25T12:14:49Z · backtest.py version `e55a16e3a2` · 27,089 parameter sets tested with this version (27,089 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: NVDA (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [relative_volume_price_thrust__max-income__v001.md](relative_volume_price_thrust__max-income__v001.md) | 27088 | `{"max_candles": 96, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [relative_volume_price_thrust__balanced__v001.md](relative_volume_price_thrust__balanced__v001.md) | 27089 | `{"max_candles": 48, "rvol": 1.5, "stop_atr": 1.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 29,510.70 | 19,497.54 | 22,839.18 | 10,899.45 |
| return % | 295.11 | 194.98 | 228.39 | 108.99 |
| return %/year | 9.0 | 10.4 | 7.7 | 7.0 |
| gross profit | 71,939.75 | 35,536.44 | 46,895.84 | 21,853.83 |
| gross loss | 42,429.05 | 16,038.91 | 24,056.66 | 10,954.38 |
| trades | 66 | 40 | 46 | 30 |
| win rate % | 45.5 | 42.5 | 52.2 | 36.7 |
| avg win | 2,397.99 | 2,090.38 | 1,953.99 | 1,986.71 |
| avg loss | -1,178.58 | -697.34 | -1,093.48 | -576.55 |
| avg result / trade | 447.13 | 487.44 | 496.50 | 363.31 |
| largest single loss | -3,150.77 | -1,574.14 | -2,673.43 | -1,164.87 |
| largest loss % of equity | -12.86 | -5.07 | -12.86 | -6.63 |
| max drawdown | -9,728.43 | -5,402.15 | -5,613.19 | -3,715.09 |
| max drawdown % | -45.07 | -24.82 | -43.28 | -24.93 |
| profit factor | 1.70 | 2.22 | 1.95 | 2.00 |
| unusually bad trades | 4 | 1 | 4 | 0 |
| … threshold (% of equity) | 8.8 | 8.7 | 10.6 | 8.6 |
| time in market % | 13.1 | 12.7 | 8.8 | 7.8 |
| buy & hold return % | 790.82 | 20,904.13 | 790.82 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.17 |  | 0.91 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 12.6 | 3.6 |
| 2001 | -17.5 | -21.9 |
| 2002 | 27.2 | 27.2 |
| 2003 | 36.3 | 40.1 |
| 2004 | 5.0 | 9.2 |
| 2005 | 24.5 | 24.5 |
| 2006 | 17.3 | -0.3 |
| 2007 | 6.5 | 6.5 |
| 2008 | -6.6 | 0.0 |
| 2009 | 4.7 | -4.1 |
| 2010 | 23.2 | 10.6 |
| 2011 | 10.9 | 16.6 |
| 2012 | -0.5 | 3.0 |
| 2013 | -8.0 | -3.8 |
| 2014 | 11.1 | 11.1 |
| 2015 | 10.9 | 16.0 |
| 2016 (OOS) | 41.1 | 26.0 |
| 2017 (OOS) | 3.3 | 3.3 |
| 2018 (OOS) | -1.3 | 0.6 |
| 2019 (OOS) | -12.9 | -14.6 |
| 2020 (OOS) | 13.0 | 20.9 |
| 2021 (OOS) | 17.9 | 17.9 |
| 2022 (OOS) | 11.0 | -4.3 |
| 2023 (OOS) | 5.5 | 7.6 |
| 2024 (OOS) | 27.7 | 34.2 |
| 2025 (OOS) | 18.2 | -5.1 |
| 2026 (OOS) | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 45.1% from a peak in-sample and 24.8% out-of-sample, and the worst single trade cost 5.1% of the account out-of-sample. About 45 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 22% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 43.3% from a peak in-sample and 24.9% out-of-sample, and the worst single trade cost 6.6% of the account out-of-sample. About 52 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 23% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 18668 | `{"max_candles": 96, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | 1.00 |
| 18679 | `{"max_candles": 90, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 18692 | `{"max_candles": 48, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 18700 | `{"max_candles": 60, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 19268 | `{"max_candles": 78, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 19273 | `{"max_candles": 66, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 19368 | `{"max_candles": 72, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 19445 | `{"max_candles": 30, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 18,571.82 | 10.1 | -24.8 | 1.13 | 66/40 | not checked |
| 19583 | `{"max_candles": 54, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 19646 | `{"max_candles": 42, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 21332 | `{"max_candles": 36, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,174.23 | 10.3 | -24.8 | 1.15 | 66/40 | not checked |
| 21334 | `{"max_candles": 84, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 23442 | `{"max_candles": 114, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 24639 | `{"max_candles": 102, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 26366 | `{"max_candles": 108, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 5.0}` | 29,510.70 | 9.0 | -45.1 | 45.5 | 19,497.54 | 10.4 | -24.8 | 1.17 | 66/40 | not checked |
| 18647 | `{"max_candles": 42, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 19727 | `{"max_candles": 36, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 19953 | `{"max_candles": 78, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 20014 | `{"max_candles": 24, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,453.43 | 7.7 | -30.8 | 0.99 | 67/43 | not checked |
| 20108 | `{"max_candles": 48, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 20181 | `{"max_candles": 90, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 20466 | `{"max_candles": 96, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 20545 | `{"max_candles": 84, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 20735 | `{"max_candles": 54, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |
| 21022 | `{"max_candles": 60, "rvol": 1.25, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 23,009.31 | 7.8 | -39.5 | 44.8 | 12,007.06 | 7.5 | -30.8 | 0.97 | 67/42 | not checked |

(54 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

475 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | AXON | 89% | 4.4 | 21.8 | 22.9 | 6.0 | 0.3 | 12 |
| 2 | NFLX | 60% | 5.5 | 13.8 | 49.9 | 5.5 | 1.9 | 20 |
| 3 | SOON.SW | 60% | 0.8 | 4.2 | 10.3 | 1.5 | -1.7 | 16 |
| 4 | SLHN.SW | 59% | 2.6 | 8.2 | -2.7 | 6.6 | -0.1 | 6 |
| 5 | LONN.SW | 54% | 2.7 | 6.6 | 9.3 | 4.0 | 1.2 | 16 |
| 6 | REGN | 52% | 2.8 | 12.8 | 26.2 | 4.6 | 0.2 | 5 |
| 7 | SBAC | 52% | 0.5 | 4.0 | 11.4 | 0.1 | 0.6 | 19 |
| 8 | CMG | 52% | 0.4 | 2.3 | 24.2 | 0.9 | -0.4 | 4 |
| 9 | TPL | 52% | 0.1 | 8.5 | 20.4 | 0.5 | 5.7 | 31 |
| 10 | ISRG | 51% | 1.9 | 5.3 | 22.0 | 2.9 | 0.3 | 0 |
| 11 | DECK | 51% | 0.3 | 4.0 | 28.3 | 0.6 | 1.1 | 16 |
| 12 | INCY | 48% | 3.4 | 12.5 | 7.8 | 4.2 | 1.1 | 4 |
| 13 | URI | 48% | 2.2 | 10.1 | 9.3 | 2.2 | 1.0 | 28 |
| 14 | BRO | 48% | 2.1 | 6.0 | 13.9 | 3.6 | 1.4 | 22 |
| 15 | ADSK | 48% | 2.0 | 9.3 | 13.4 | 5.2 | -1.9 | 1 |
| 16 | TMO | 48% | 1.1 | 3.6 | 16.4 | 1.9 | 1.1 | 8 |
| 17 | MNST | 48% | 0.5 | 6.7 | 48.5 | -3.2 | 0.4 | 6 |
| 18 | AKAM | 46% | 2.8 | 5.5 | -8.4 | 1.5 | -3.4 | 0 |
| 19 | JBHT | 44% | 0.8 | 4.4 | 21.9 | 1.0 | -0.2 | 13 |
| 20 | LHX | 44% | 0.4 | 3.4 | 14.7 | 0.7 | 2.2 | 26 |
| 21 | MGM | 43% | 1.8 | 7.3 | 3.8 | 1.9 | -1.2 | 11 |
| 22 | TSN | 43% | 1.4 | 5.2 | 8.9 | 1.1 | -0.9 | 1 |
| 23 | TKO | 43% | 0.8 | 3.4 | 6.6 | 0.7 | 3.0 | 27 |
| 24 | IT | 43% | 0.7 | 4.8 | 11.7 | -0.3 | 0.4 | 22 |
| 25 | TSCO | 43% | 0.6 | 4.2 | 32.5 | -0.3 | -0.3 | 15 |
| 26 | ACGL | 41% | 1.6 | 4.6 | 19.2 | 1.7 | -1.6 | 13 |
| 27 | UHS | 41% | 1.6 | 5.5 | 18.1 | 2.4 | 1.8 | 18 |
| 28 | KIM | 41% | 1.5 | 4.1 | 10.8 | 0.8 | 1.2 | 19 |
| 29 | WDC | 41% | 1.1 | 5.2 | 18.6 | 0.6 | -0.7 | 11 |
| 30 | TXT | 41% | 1.0 | 8.5 | 2.2 | 3.5 | -0.8 | 0 |
| 31 | CNP | 41% | 0.5 | 3.2 | 5.6 | 1.4 | -0.6 | 3 |
| 32 | VTRS | 41% | 0.5 | 3.0 | 10.8 | 0.5 | -2.1 | 7 |
| 33 | DPZ | 40% | 1.4 | 3.5 | 25.3 | 2.0 | 0.9 | 25 |
| 34 | GOOG | 40% | 1.3 | 6.8 | 20.6 | 2.1 | -0.6 | 3 |
| 35 | TYL | 40% | 1.2 | 7.2 | 23.4 | -1.0 | -0.6 | 1 |
| 36 | PGHN.SW | 40% | 1.2 | 7.6 | 19.2 | 0.7 | -0.6 | 17 |
| 37 | BG | 40% | 1.2 | 3.6 | 9.6 | 1.7 | -1.6 | 0 |
| 38 | GOOGL | 40% | 1.1 | 7.1 | 20.8 | 2.9 | 0.1 | 0 |
| 39 | CME | 40% | -0.3 | 10.8 | 21.2 | 0.8 | -1.8 | 3 |
| 40 | PHM | 38% | 1.1 | 3.5 | 8.1 | 3.3 | -1.4 | 5 |

(435 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [relative_volume_price_thrust__broad__max-income__v001.md](symbols/broad/relative_volume_price_thrust__broad__max-income__v001.md) | 0.3 | 0.2 | 0.2 | -3.2 | 39.5 | 12015/6675 |
| broad | balanced | [relative_volume_price_thrust__broad__balanced__v002.md](symbols/broad/relative_volume_price_thrust__broad__balanced__v002.md) | 0.2 | 0.1 | 0.1 | -0.3 | 46.2 | 1605/638 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 27,089 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
