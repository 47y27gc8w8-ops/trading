# volatility_percentile_turnup: optimization summary

Updated 2026-11-25T06:02:48Z · backtest.py version `27cc240f83` · 35,572 parameter sets tested with this version (35,572 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [volatility_percentile_turnup__max-income__v001.md](volatility_percentile_turnup__max-income__v001.md) | 35571 | `{"max_candles": 90, "n": 120, "stop_atr": 3.5, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [volatility_percentile_turnup__balanced__v001.md](volatility_percentile_turnup__balanced__v001.md) | 35572 | `{"max_candles": 36, "n": 190, "stop_atr": 2.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 733.06 | 149.72 | 267.07 | 118.25 |
| return % | 7.33 | 1.50 | 2.67 | 1.18 |
| return %/year | 0.4 | 0.1 | 0.2 | 0.1 |
| gross profit | 4,712.26 | 3,299.28 | 3,195.03 | 2,901.94 |
| gross loss | 3,979.20 | 3,149.56 | 2,927.95 | 2,783.69 |
| trades | 41 | 36 | 33 | 30 |
| win rate % | 43.9 | 41.7 | 48.5 | 36.7 |
| avg win | 261.79 | 219.95 | 199.69 | 263.81 |
| avg loss | -173.01 | -149.98 | -172.23 | -146.51 |
| avg result / trade | 17.88 | 4.16 | 8.09 | 3.94 |
| largest single loss | -500.83 | -398.72 | -370.10 | -405.20 |
| largest loss % of equity | -5.09 | -4.03 | -3.65 | -4.03 |
| max drawdown | -1,549.39 | -1,503.19 | -1,560.23 | -1,364.20 |
| max drawdown % | -14.63 | -13.66 | -14.53 | -12.67 |
| profit factor | 1.18 | 1.05 | 1.09 | 1.04 |
| unusually bad trades | 3 | 1 | 2 | 1 |
| … threshold (% of equity) | 2.9 | 3.1 | 2.9 | 3.2 |
| time in market % | 12.3 | 13.6 | 11.9 | 15.2 |
| buy & hold return % | 85.02 | 328.39 | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.32 |  | 0.69 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 0.5 | 0.4 |
| 2001 | -2.0 | 0.0 |
| 2002 | -5.1 | 0.0 |
| 2003 | 2.1 | 3.4 |
| 2004 | 2.7 | -0.0 |
| 2005 | -4.2 | -4.2 |
| 2006 | 1.9 | 0.5 |
| 2007 | -2.6 | -2.1 |
| 2008 | -2.2 | -2.2 |
| 2009 | 4.0 | -2.2 |
| 2010 | -0.2 | 3.9 |
| 2011 | 2.2 | 0.6 |
| 2012 | 6.8 | -0.3 |
| 2013 | 3.4 | 5.5 |
| 2014 | 0.6 | -0.3 |
| 2015 | 0.0 | 0.0 |
| 2016 (OOS) | -0.7 | -2.0 |
| 2017 (OOS) | 2.7 | 2.6 |
| 2018 (OOS) | 0.9 | -1.9 |
| 2019 (OOS) | 3.8 | 1.5 |
| 2020 (OOS) | 1.9 | 3.4 |
| 2021 (OOS) | -6.7 | -2.7 |
| 2022 (OOS) | -6.5 | -4.0 |
| 2023 (OOS) | 9.9 | 6.1 |
| 2024 (OOS) | -1.1 | 1.7 |
| 2025 (OOS) | -0.6 | -1.8 |
| 2026 (OOS) | -1.1 | -1.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 14.6% from a peak in-sample and 13.7% out-of-sample, and the worst single trade cost 4.0% of the account out-of-sample. About 44 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 68% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 14.5% from a peak in-sample and 12.7% out-of-sample, and the worst single trade cost 4.0% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 69% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 23845 | `{"max_candles": 24, "n": 120, "stop_atr": 2.5, "take_profit_atr": 3.0}` | 757.79 | 0.5 | -14.6 | 43.9 | 182.39 | 0.2 | -13.0 | 0.37 | 41/36 | not checked |
| 3546 | `{"max_candles": 36, "n": 190, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 267.07 | 0.2 | -14.5 | 48.5 | 118.25 | 0.1 | -12.7 | 0.69 | 33/30 | 0.62 |
| 19393 | `{"max_candles": 36, "n": 200, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 6.54 | 0.0 | -13.0 | 42.4 | 104.73 | 0.1 | -13.8 | n/a | 33/31 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

52 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 89% | 0.9 | 2.4 | 9.1 | 1.4 | -1.0 | 0 |
| 2 | EEM | 83% | 1.4 | 5.5 | 6.0 | 4.7 | -2.6 | 0 |
| 3 | XLE | 79% | 1.3 | 3.6 | 6.8 | 3.2 | 0.5 | 10 |
| 4 | VWO | 79% | 1.2 | 5.5 | 2.3 | 2.0 | -1.6 | 0 |
| 5 | DBC | 79% | 0.9 | 2.8 | -7.3 | 1.6 | 1.3 | 35 |
| 6 | VTV | 79% | 0.5 | 1.6 | 6.7 | 1.3 | 0.0 | 33 |
| 7 | DIA | 78% | 0.5 | 1.3 | 4.9 | 0.5 | -0.4 | 0 |
| 8 | SOXX | 76% | 0.9 | 3.2 | 8.3 | 1.8 | -1.4 | 15 |
| 9 | EFA | 73% | 0.7 | 2.1 | 7.9 | 0.1 | -2.9 | 0 |
| 10 | BND | 67% | 0.1 | 0.7 | 4.4 | -0.1 | 0.1 | 15 |
| 11 | XLI | 63% | 0.2 | 1.1 | 5.7 | -0.1 | 1.2 | 18 |
| 12 | RSP | 62% | 0.3 | 2.0 | 8.1 | 1.8 | -0.8 | 8 |
| 13 | LQD | 62% | 0.1 | 1.0 | 4.7 | -0.3 | -0.1 | 16 |
| 14 | SLV | 60% | 3.2 | 7.7 | -0.8 | 4.7 | 0.1 | 4 |
| 15 | XLB | 56% | 0.1 | 3.7 | 7.7 | 2.2 | -2.0 | 3 |
| 16 | AGG | 52% | 0.0 | 0.5 | 4.2 | -0.1 | 0.4 | 14 |
| 17 | TLT | 51% | 0.0 | 1.6 | 6.6 | -0.2 | 0.1 | 7 |
| 18 | GLD | 49% | -0.0 | 1.4 | 6.0 | -1.2 | 2.4 | 26 |
| 19 | VUG | 41% | 0.0 | 1.8 | 8.6 | 1.8 | -0.4 | 12 |
| 20 | SMH | 40% | -0.1 | 1.5 | 1.5 | -1.7 | 2.3 | 24 |
| 21 | XLF | 37% | -0.3 | 1.1 | 1.5 | 0.1 | -1.3 | 8 |
| 22 | VNQ | 35% | -0.9 | 3.2 | 6.8 | -1.7 | -3.1 | 0 |
| 23 | GDX | 30% | 0.4 | 3.4 | -12.8 | 0.1 | 0.3 | 2 |
| 24 | IVV | 29% | -0.2 | 0.8 | 6.3 | 0.4 | -0.1 | 3 |
| 25 | XLU | 27% | -0.3 | 1.2 | 6.7 | -0.2 | 0.0 | 16 |
| 26 | IWM | 24% | -0.5 | 1.0 | 7.6 | -1.6 | 1.2 | 10 |
| 27 | IEF | 19% | -0.2 | 0.6 | 5.0 | -0.1 | -0.6 | 2 |
| 28 | TIP | 19% | -0.3 | 0.5 | 3.8 | -0.8 | -0.9 | 0 |
| 29 | SPY | 19% | -0.4 | 0.4 | 3.9 | 0.2 | -0.5 | 3 |
| 30 | VTI | 19% | -0.7 | 0.4 | 9.4 | -0.3 | -1.8 | 5 |
| 31 | QQQ | 17% | -0.7 | 1.8 | 2.4 | 1.8 | 0.5 | 10 |
| 32 | XLV | 16% | -0.4 | 0.6 | 7.5 | -1.0 | 0.3 | 3 |
| 33 | VIG | 10% | -0.1 | 0.9 | 6.4 | 0.0 | 0.2 | 3 |
| 34 | SHY | 3% | -0.4 | 0.0 | 2.1 | -0.3 | -0.3 | 0 |
| 35 | USO | 3% | -1.4 | 0.6 | -20.9 | -3.5 | 0.7 | 2 |
| 36 | CSNDX.SW | 2% | 0.2 | 0.9 | 20.9 | 2.7 | 1.4 | 1 |
| 37 | XLY | 2% | -1.2 | 0.4 | 8.4 | -1.5 | -0.9 | 1 |
| 38 | TQQQ | 0% | 4.8 | n/a | 57.4 | 9.0 | 1.3 | 0 |
| 39 | VOO | 0% | 1.0 | n/a | 13.5 | 1.7 | -0.6 | 0 |
| 40 | CSSPX.SW | 0% | 0.8 | n/a | 15.1 | 3.0 | 0.2 | 0 |

(12 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [volatility_percentile_turnup__broad__max-income__v001.md](symbols/broad/volatility_percentile_turnup__broad__max-income__v001.md) | 0.4 | 0.5 | 0.4 | -6.6 | 38.4 | 1455/1650 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 35,572 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
