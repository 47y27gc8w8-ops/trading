# stochastic_pop: optimization summary

Updated 2026-11-25T07:46:08Z · backtest.py version `c20fb5f59d` · 35,538 parameter sets tested with this version (35,538 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [stochastic_pop__max-income__v001.md](stochastic_pop__max-income__v001.md) | 35537 | `{"level": 78, "max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [stochastic_pop__balanced__v001.md](stochastic_pop__balanced__v001.md) | 35538 | `{"level": 76, "max_candles": 120, "stop_atr": 2.5, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,143.00 | 3,701.11 | 3,217.50 | 1,327.68 |
| return % | 31.43 | 37.01 | 32.18 | 13.28 |
| return %/year | 1.7 | 2.9 | 1.8 | 1.1 |
| gross profit | 10,823.22 | 8,055.15 | 10,858.74 | 5,534.51 |
| gross loss | 7,680.22 | 4,354.04 | 7,641.24 | 4,206.82 |
| trades | 47 | 43 | 48 | 40 |
| win rate % | 46.8 | 48.8 | 45.8 | 45.0 |
| avg win | 491.96 | 383.58 | 493.58 | 307.47 |
| avg loss | -307.21 | -197.91 | -293.89 | -191.22 |
| avg result / trade | 66.87 | 86.07 | 67.03 | 33.19 |
| largest single loss | -829.42 | -458.77 | -829.42 | -454.79 |
| largest loss % of equity | -8.29 | -4.58 | -8.29 | -4.58 |
| max drawdown | -1,736.82 | -1,320.57 | -1,561.32 | -1,240.80 |
| max drawdown % | -13.01 | -12.49 | -12.45 | -11.84 |
| profit factor | 1.41 | 1.85 | 1.42 | 1.32 |
| unusually bad trades | 2 | 1 | 1 | 1 |
| … threshold (% of equity) | 4.1 | 3.5 | 4.7 | 3.5 |
| time in market % | 12.4 | 14.6 | 12.3 | 13.7 |
| buy & hold return % | 28.06 | 541.70 | 28.06 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.70 |  | 0.65 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 1.7 | 1.7 |
| 2001 | -0.0 | -0.2 |
| 2002 | 11.3 | 11.3 |
| 2003 | 1.2 | 1.4 |
| 2004 | 2.9 | 2.5 |
| 2005 | -3.4 | -5.8 |
| 2006 | 5.0 | 5.0 |
| 2007 | -0.3 | 4.1 |
| 2008 | -2.1 | -2.1 |
| 2009 | 3.2 | 2.7 |
| 2010 | 14.4 | 14.4 |
| 2011 | -7.6 | -6.0 |
| 2012 | 2.3 | 1.8 |
| 2013 | 3.1 | 3.1 |
| 2014 | 4.5 | 2.2 |
| 2015 | -6.3 | -5.8 |
| 2016 (OOS) | -0.1 | -0.1 |
| 2017 (OOS) | 1.1 | 0.2 |
| 2018 (OOS) | -5.5 | -5.5 |
| 2019 (OOS) | 5.6 | 5.6 |
| 2020 (OOS) | 6.3 | 0.3 |
| 2021 (OOS) | 1.2 | 1.0 |
| 2022 (OOS) | -3.0 | -3.0 |
| 2023 (OOS) | 15.0 | 15.0 |
| 2024 (OOS) | 2.2 | 2.3 |
| 2025 (OOS) | 4.8 | -0.9 |
| 2026 (OOS) | 5.7 | -1.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 13.0% from a peak in-sample and 12.5% out-of-sample, and the worst single trade cost 4.6% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 77% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 12.4% from a peak in-sample and 11.8% out-of-sample, and the worst single trade cost 4.6% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 80% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2285 | `{"level": 76, "max_candles": 120, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | 1.00 |
| 2296 | `{"level": 76, "max_candles": 108, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 2297 | `{"level": 76, "max_candles": 132, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 8200 | `{"level": 76, "max_candles": 72, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 12260 | `{"level": 76, "max_candles": 168, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 14333 | `{"level": 76, "max_candles": 192, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 15737 | `{"level": 76, "max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 21564 | `{"level": 76, "max_candles": 156, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 25578 | `{"level": 76, "max_candles": 48, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 27266 | `{"level": 76, "max_candles": 144, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 27641 | `{"level": 76, "max_candles": 84, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 30027 | `{"level": 76, "max_candles": 60, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 30904 | `{"level": 76, "max_candles": 180, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,217.50 | 1.8 | -12.4 | 45.8 | 1,327.68 | 1.1 | -11.8 | 0.65 | 48/40 | not checked |
| 2291 | `{"level": 75, "max_candles": 120, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 4605 | `{"level": 75, "max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 8262 | `{"level": 75, "max_candles": 108, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 9638 | `{"level": 75, "max_candles": 60, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 13963 | `{"level": 75, "max_candles": 156, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 14459 | `{"level": 75, "max_candles": 180, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 15925 | `{"level": 75, "max_candles": 144, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 19503 | `{"level": 75, "max_candles": 48, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 20721 | `{"level": 75, "max_candles": 72, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 21948 | `{"level": 75, "max_candles": 192, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 24936 | `{"level": 75, "max_candles": 168, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |
| 25198 | `{"level": 75, "max_candles": 132, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 3,136.67 | 1.7 | -12.0 | 43.8 | 2,306.23 | 1.9 | -11.8 | 1.12 | 48/41 | not checked |

(79 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 98% | 1.6 | 3.1 | 5.0 | 2.6 | -0.2 | 18 |
| 2 | EFA | 90% | 1.3 | 2.4 | 6.0 | 1.3 | 1.2 | 47 |
| 3 | AGG | 90% | 0.7 | 1.5 | 4.2 | 0.5 | 0.1 | 20 |
| 4 | IWDA.AS | 89% | 1.8 | 5.0 | 13.5 | 2.8 | 1.0 | 35 |
| 5 | SPY | 71% | 0.4 | 1.6 | 3.9 | 0.2 | -0.3 | 31 |
| 6 | TIP | 63% | 0.2 | 0.9 | 3.8 | 0.6 | -0.7 | 0 |
| 7 | EEM | 56% | 0.4 | 3.5 | 6.4 | 0.7 | 0.9 | 9 |
| 8 | VUG | 56% | 0.1 | 1.9 | 8.3 | 1.6 | 2.1 | 32 |
| 9 | IEF | 56% | 0.0 | 0.7 | 5.0 | 0.0 | -0.1 | 0 |
| 10 | VTI | 52% | 0.1 | 1.0 | 7.1 | 0.5 | 0.1 | 27 |
| 11 | LQD | 52% | 0.0 | 1.1 | 4.9 | -0.0 | 0.1 | 26 |
| 12 | VIG | 51% | 0.0 | 1.3 | 6.2 | -0.3 | -0.5 | 6 |
| 13 | XLP | 49% | -0.0 | 1.2 | 7.4 | -0.7 | 0.6 | 15 |
| 14 | IVV | 44% | -0.1 | 0.9 | 5.3 | 0.1 | -0.4 | 21 |
| 15 | GLD | 35% | -0.3 | 1.4 | 8.3 | 0.1 | 0.2 | 16 |
| 16 | XLK | 35% | -0.4 | 1.2 | -0.5 | -0.7 | 2.1 | 21 |
| 17 | XLU | 35% | -0.5 | 2.4 | 6.4 | -0.1 | -1.9 | 9 |
| 18 | CSSMI.SW | 33% | 0.6 | 2.4 | 7.7 | 0.7 | 0.3 | 13 |
| 19 | XLE | 33% | -0.4 | 1.7 | 6.9 | 0.2 | -0.3 | 4 |
| 20 | ACWI | 32% | 0.6 | 2.3 | 10.8 | 1.7 | -0.3 | 8 |
| 21 | BND | 32% | -0.2 | 0.7 | 3.8 | -0.7 | 0.5 | 7 |
| 22 | XLI | 27% | -0.8 | 1.2 | 5.6 | -1.1 | -1.3 | 8 |
| 23 | DBC | 25% | 2.8 | 4.0 | -5.8 | 2.7 | 2.7 | 13 |
| 24 | SLV | 25% | 0.8 | 4.0 | -0.7 | 0.7 | 2.5 | 16 |
| 25 | VWO | 25% | 0.0 | 1.7 | 3.3 | 0.6 | 0.5 | 6 |
| 26 | TLT | 25% | -0.4 | 0.6 | 6.2 | -0.4 | -1.2 | 2 |
| 27 | VEA | 24% | 0.3 | 1.5 | 0.0 | 0.5 | 0.7 | 7 |
| 28 | XLF | 24% | -0.8 | 1.4 | 2.1 | -1.4 | 1.9 | 13 |
| 29 | QQQ | 24% | -1.1 | 1.8 | 1.6 | 0.5 | 4.4 | 15 |
| 30 | IWM | 22% | -0.3 | 1.0 | 7.8 | 0.2 | -1.0 | 0 |
| 31 | XLV | 22% | -0.6 | 0.9 | 6.9 | -0.0 | -0.9 | 2 |
| 32 | SHY | 21% | -0.2 | 0.2 | 2.1 | -0.3 | 0.1 | 10 |
| 33 | XLY | 17% | -0.7 | 0.6 | 7.2 | -1.4 | -1.5 | 8 |
| 34 | DIA | 13% | -0.8 | 0.4 | 4.9 | 0.3 | -1.1 | 1 |
| 35 | CSNDX.SW | 11% | 0.9 | 2.4 | 16.8 | 1.2 | 3.0 | 7 |
| 36 | VT | 11% | -1.2 | 2.3 | 11.9 | -0.6 | -0.0 | 0 |
| 37 | XLB | 8% | -0.9 | 0.4 | 5.6 | -1.2 | -0.5 | 0 |
| 38 | USO | 6% | -2.4 | 0.8 | -14.7 | -2.4 | 2.0 | 2 |
| 39 | VTV | 5% | -0.8 | 0.3 | 6.8 | -1.7 | 1.0 | 3 |
| 40 | RSP | 2% | -1.7 | 0.0 | 8.2 | -2.2 | -0.6 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [stochastic_pop__broad__max-income__v002.md](symbols/broad/stochastic_pop__broad__max-income__v002.md) | 0.1 | 0.5 | 0.1 | -3.4 | 44.0 | 1633/1667 |
| broad | balanced | [stochastic_pop__broad__balanced__v002.md](symbols/broad/stochastic_pop__broad__balanced__v002.md) | 0.1 | 0.4 | 0.1 | -3.4 | 46.3 | 1658/1695 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 35,538 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
