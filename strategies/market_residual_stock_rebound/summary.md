# market_residual_stock_rebound: optimization summary

Updated 2026-11-26T07:57:49Z · backtest.py version `6f443a3d30` · 1,774 parameter sets tested with this version (1,774 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [market_residual_stock_rebound__max-income__v002.md](market_residual_stock_rebound__max-income__v002.md) | 1774 | `{"max_candles": 56, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | flat (data up to 2026-11-25 00:00) |
| balanced | [market_residual_stock_rebound__balanced__v002.md](market_residual_stock_rebound__balanced__v002.md) | 1774 | `{"max_candles": 56, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,798.05 | 1,219.45 | 3,798.05 | 1,219.45 |
| return % | 37.98 | 12.19 | 37.98 | 12.19 |
| return %/year | 1.6 | 1.1 | 1.6 | 1.1 |
| gross profit | 11,978.52 | 5,679.95 | 11,978.52 | 5,679.95 |
| gross loss | 8,180.46 | 4,460.50 | 8,180.46 | 4,460.50 |
| trades | 80 | 62 | 80 | 62 |
| win rate % | 76.2 | 80.7 | 76.2 | 80.7 |
| avg win | 196.37 | 113.60 | 196.37 | 113.60 |
| avg loss | -430.55 | -371.71 | -430.55 | -371.71 |
| avg result / trade | 47.48 | 19.67 | 47.48 | 19.67 |
| largest single loss | -1,149.18 | -575.62 | -1,149.18 | -575.62 |
| largest loss % of equity | -11.32 | -5.12 | -11.32 | -5.12 |
| max drawdown | -1,815.15 | -1,437.46 | -1,815.15 | -1,437.46 |
| max drawdown % | -17.88 | -13.55 | -17.88 | -13.55 |
| profit factor | 1.46 | 1.27 | 1.46 | 1.27 |
| unusually bad trades | 3 | 0 | 3 | 0 |
| … threshold (% of equity) | 5.7 | 7.8 | 5.7 | 7.8 |
| time in market % | 2.6 | 2.5 | 2.6 | 2.5 |
| buy & hold return % | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.68 |  | 0.68 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 1.3 | 1.3 |
| 1996 | 0.0 | 0.0 |
| 1997 | -1.7 | -1.7 |
| 1998 | -9.6 | -9.6 |
| 1999 | 2.2 | 2.2 |
| 2000 | 10.1 | 10.1 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 |
| 2003 | -0.4 | -0.4 |
| 2004 | 7.0 | 7.0 |
| 2005 | 14.8 | 14.8 |
| 2006 | -4.1 | -4.1 |
| 2007 | 9.2 | 9.2 |
| 2008 | 0.0 | 0.0 |
| 2009 | 0.1 | 0.1 |
| 2010 | -0.7 | -0.7 |
| 2011 | -6.0 | -6.0 |
| 2012 | 9.4 | 9.4 |
| 2013 | 1.9 | 1.9 |
| 2014 | 6.1 | 6.1 |
| 2015 | -3.7 | -3.7 |
| 2016 (OOS) | -1.4 | -1.4 |
| 2017 (OOS) | 0.5 | 0.5 |
| 2018 (OOS) | -6.6 | -6.6 |
| 2019 (OOS) | 3.6 | 3.6 |
| 2020 (OOS) | 12.1 | 12.1 |
| 2021 (OOS) | 3.5 | 3.5 |
| 2022 (OOS) | 0.0 | 0.0 |
| 2023 (OOS) | 1.7 | 1.7 |
| 2024 (OOS) | -1.4 | -1.4 |
| 2025 (OOS) | -1.3 | -1.3 |
| 2026 (OOS) | 1.8 | 1.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.9% from a peak in-sample and 13.6% out-of-sample, and the worst single trade cost 5.1% of the account out-of-sample. About 76 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 56% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 17.9% from a peak in-sample and 13.6% out-of-sample, and the worst single trade cost 5.1% of the account out-of-sample. About 76 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 56% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1274 | `{"max_candles": 56, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | 0.89 |
| 1287 | `{"max_candles": 52, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1288 | `{"max_candles": 60, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1293 | `{"max_candles": 64, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1331 | `{"max_candles": 44, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1385 | `{"max_candles": 48, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1422 | `{"max_candles": 68, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1500 | `{"max_candles": 40, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1533 | `{"max_candles": 36, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1617 | `{"max_candles": 72, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1719 | `{"max_candles": 76, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |
| 1743 | `{"max_candles": 32, "n": 63, "stop_atr": 2.25, "take_profit_atr": 0.5, "z": 1.75}` | 3,798.05 | 1.6 | -17.9 | 76.2 | 1,219.45 | 1.1 | -13.6 | 0.68 | 80/62 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

466 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | PAYX | 89% | 1.7 | 4.7 | 16.4 | 3.7 | -0.8 | 6 |
| 2 | TECH | 83% | 2.9 | 6.4 | 19.1 | 3.4 | 1.8 | 12 |
| 3 | AJG | 81% | 0.5 | 2.0 | 12.0 | 0.9 | 2.1 | 49 |
| 4 | TGT | 79% | 2.2 | 5.3 | 14.3 | 3.2 | 2.2 | 42 |
| 5 | MRSH | 79% | 1.0 | 2.4 | 10.0 | 1.1 | 0.8 | 32 |
| 6 | WRB | 79% | 0.9 | 2.7 | 13.7 | 1.6 | 1.0 | 44 |
| 7 | ECL | 79% | 0.6 | 1.9 | 17.4 | -0.3 | -0.1 | 17 |
| 8 | RTX | 78% | 1.0 | 4.2 | 14.8 | 1.8 | -1.4 | 10 |
| 9 | HD | 78% | 0.6 | 2.0 | 14.7 | 0.7 | -0.2 | 5 |
| 10 | PG | 78% | 0.4 | 1.7 | 10.7 | 0.2 | -0.5 | 10 |
| 11 | INTU | 76% | 1.7 | 4.0 | 14.9 | 3.3 | 1.9 | 47 |
| 12 | HAL | 76% | 1.6 | 5.3 | 8.8 | 1.3 | 1.7 | 32 |
| 13 | CSX | 76% | 0.8 | 3.5 | 9.7 | 1.2 | 0.6 | 27 |
| 14 | EXPD | 76% | 0.8 | 2.4 | 19.0 | 0.9 | 1.0 | 45 |
| 15 | SHW | 76% | 0.7 | 3.9 | 16.1 | 1.4 | 2.3 | 32 |
| 16 | MMM | 76% | 0.5 | 2.2 | 11.5 | 0.6 | 0.5 | 34 |
| 17 | IEX | 75% | 1.0 | 5.5 | 13.0 | 1.9 | 1.2 | 29 |
| 18 | NVO | 75% | 1.0 | 4.7 | 23.4 | 0.9 | 0.4 | 41 |
| 19 | CASY | 75% | 1.0 | 2.7 | 15.2 | 0.9 | 0.3 | 16 |
| 20 | XOM | 75% | 0.7 | 3.7 | 10.9 | 1.3 | -0.7 | 0 |
| 21 | IFF | 75% | 0.6 | 1.4 | 7.2 | 0.7 | -2.6 | 0 |
| 22 | CI | 75% | 0.4 | 2.7 | 16.7 | 1.7 | -0.6 | 5 |
| 23 | COHR | 73% | 2.2 | 7.9 | 19.2 | 3.0 | -0.2 | 32 |
| 24 | NVR | 73% | 1.7 | 4.1 | 31.2 | 2.1 | -0.1 | 16 |
| 25 | STE | 73% | 1.1 | 3.5 | 11.7 | 1.4 | -1.0 | 6 |
| 26 | GD | 73% | 0.8 | 3.2 | 15.2 | 1.5 | -1.3 | 3 |
| 27 | ADP | 73% | 0.8 | 2.0 | 12.0 | 0.2 | -0.8 | 2 |
| 28 | AZO | 73% | 0.6 | 2.6 | 17.7 | 1.9 | -2.2 | 0 |
| 29 | GL | 73% | 0.6 | 2.5 | 12.2 | 0.5 | -0.1 | 29 |
| 30 | BF-B | 73% | 0.4 | 2.8 | 15.1 | 1.3 | -0.7 | 14 |
| 31 | DRI | 71% | 1.9 | 3.8 | 16.5 | 2.2 | 2.3 | 30 |
| 32 | ACGL | 71% | 0.6 | 2.6 | 13.5 | 0.6 | 2.9 | 44 |
| 33 | CVX | 71% | 0.6 | 2.6 | 10.5 | 0.2 | -1.9 | 0 |
| 34 | HRL | 70% | 0.6 | 3.8 | 15.1 | 0.4 | -1.6 | 0 |
| 35 | CINF | 70% | 0.3 | 2.4 | 10.6 | 0.7 | 1.8 | 44 |
| 36 | ETN | 68% | 1.1 | 2.4 | 11.6 | 1.5 | 1.7 | 30 |
| 37 | FISV | 68% | 0.8 | 4.8 | 17.2 | 1.1 | 1.1 | 19 |
| 38 | HUBB | 68% | 0.7 | 1.9 | 10.2 | 0.9 | -2.0 | 9 |
| 39 | WST | 68% | 0.7 | 1.9 | 13.0 | 0.6 | -1.4 | 1 |
| 40 | STZ | 68% | 0.4 | 1.9 | 17.6 | 0.8 | 0.8 | 36 |

(426 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [market_residual_stock_rebound__broad__max-income__v002.md](symbols/broad/market_residual_stock_rebound__broad__max-income__v002.md) | 2.5 | 1.4 | 1.4 | -9.1 | 63.0 | 123228/78432 |
| broad | balanced | [market_residual_stock_rebound__broad__balanced__v002.md](symbols/broad/market_residual_stock_rebound__broad__balanced__v002.md) | 1.5 | 0.7 | 0.7 | -5.4 | 62.9 | 57999/38088 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,774 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
