# price_zscore_reversion: optimization summary

Updated 2026-11-25T10:15:38Z · backtest.py version `6bd65abf1d` · 3,618 parameter sets tested with this version (3,618 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: GLD (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [price_zscore_reversion__max-income__v002.md](price_zscore_reversion__max-income__v002.md) | 3618 | `{"max_candles": 22, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.5, "z": 1.9}` | flat (data up to 2026-11-24 00:00) |
| balanced | [price_zscore_reversion__balanced__v002.md](price_zscore_reversion__balanced__v002.md) | 3618 | `{"max_candles": 22, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.5, "z": 1.9}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,276.75 | 1,176.98 | 2,276.75 | 1,176.98 |
| return % | 22.77 | 11.77 | 22.77 | 11.77 |
| return %/year | 2.0 | 1.0 | 2.0 | 1.0 |
| gross profit | 5,606.29 | 5,510.42 | 5,606.29 | 5,510.42 |
| gross loss | 3,329.54 | 4,333.44 | 3,329.54 | 4,333.44 |
| trades | 30 | 37 | 30 | 37 |
| win rate % | 73.3 | 67.6 | 73.3 | 67.6 |
| avg win | 254.83 | 220.42 | 254.83 | 220.42 |
| avg loss | -416.19 | -361.12 | -416.19 | -361.12 |
| avg result / trade | 75.89 | 31.81 | 75.89 | 31.81 |
| largest single loss | -704.47 | -1,020.70 | -704.47 | -1,020.70 |
| largest loss % of equity | -5.38 | -8.37 | -5.38 | -8.37 |
| max drawdown | -1,123.09 | -1,929.08 | -1,123.09 | -1,929.08 |
| max drawdown % | -8.50 | -15.31 | -8.50 | -15.31 |
| profit factor | 1.68 | 1.27 | 1.68 | 1.27 |
| unusually bad trades | 1 | 1 | 1 | 1 |
| … threshold (% of equity) | 5.7 | 5.7 | 5.7 | 5.7 |
| time in market % | 9.5 | 12.5 | 9.5 | 12.5 |
| buy & hold return % | 130.80 | 222.91 | 130.80 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |  | 0.52 |
| period | 2005-06-24 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2005-06-24 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2005 | 2.3 | 2.3 |
| 2006 | 1.9 | 1.9 |
| 2007 | 5.6 | 5.6 |
| 2008 | -4.8 | -4.8 |
| 2009 | 10.7 | 10.7 |
| 2010 | 7.0 | 7.0 |
| 2011 | 1.4 | 1.4 |
| 2012 | 4.7 | 4.7 |
| 2013 | -6.0 | -6.0 |
| 2014 | 0.7 | 0.7 |
| 2015 | -1.5 | -1.5 |
| 2016 (OOS) | 4.5 | 4.5 |
| 2017 (OOS) | 9.9 | 9.9 |
| 2018 (OOS) | -1.7 | -1.7 |
| 2019 (OOS) | 0.9 | 0.9 |
| 2020 (OOS) | 8.4 | 8.4 |
| 2021 (OOS) | 0.6 | 0.6 |
| 2022 (OOS) | -9.5 | -9.5 |
| 2023 (OOS) | -2.7 | -2.7 |
| 2024 (OOS) | 6.4 | 6.4 |
| 2025 (OOS) | 4.2 | 4.2 |
| 2026 (OOS) | -7.7 | -7.7 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 8.5% from a peak in-sample and 15.3% out-of-sample, and the worst single trade cost 8.4% of the account out-of-sample. About 73 of every 100 trades won in-sample. Out-of-sample it earned 1.0% a year against 2.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 65% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 8.5% from a peak in-sample and 15.3% out-of-sample, and the worst single trade cost 8.4% of the account out-of-sample. About 73 of every 100 trades won in-sample. Out-of-sample it earned 1.0% a year against 2.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 65% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3453 | `{"max_candles": 22, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.5, "z": 1.8}` | 2,296.19 | 2.0 | -10.7 | 71.4 | 691.46 | 0.6 | -17.5 | 0.31 | 35/38 | not checked |
| 3460 | `{"max_candles": 22, "n": 22, "stop_atr": 3.0, "take_profit_atr": 2.5, "z": 1.9}` | 2,276.75 | 2.0 | -8.5 | 73.3 | 1,176.98 | 1.0 | -15.3 | 0.52 | 30/37 | 1.00 |

## Screening: where does the strategy work? (in-sample ranking)

48 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SMH | 29% | -0.2 | 2.7 | 0.8 | -0.1 | -1.0 | 13 |
| 2 | TLT | 24% | 0.1 | 2.7 | 6.3 | 0.0 | -1.5 | 1 |
| 3 | VTV | 24% | -0.1 | 3.9 | 7.2 | -0.2 | -0.3 | 2 |
| 4 | TIP | 22% | -0.2 | 0.9 | 4.2 | -0.6 | -0.6 | 0 |
| 5 | XLP | 19% | -0.2 | 1.7 | 6.7 | -0.7 | 2.5 | 12 |
| 6 | SOXX | 19% | -0.4 | 2.8 | 3.5 | 2.5 | 1.0 | 7 |
| 7 | XLE | 19% | -0.7 | 1.7 | 6.6 | -0.9 | 1.0 | 10 |
| 8 | VIG | 17% | -1.7 | 3.3 | 6.5 | 2.5 | 0.1 | 7 |
| 9 | XLI | 16% | -0.2 | 1.0 | 5.5 | 0.6 | 1.9 | 9 |
| 10 | RSP | 16% | -0.7 | 1.2 | 8.8 | -1.3 | -0.0 | 4 |
| 11 | VNQ | 16% | -1.8 | 3.3 | 8.4 | 1.0 | 0.3 | 3 |
| 12 | TQQQ | 13% | 1.7 | 5.5 | 52.0 | -0.4 | -2.7 | 2 |
| 13 | XLV | 13% | -1.0 | 1.6 | 7.2 | -0.3 | 0.9 | 3 |
| 14 | XLF | 13% | -1.1 | 2.0 | 1.7 | -2.5 | 1.6 | 3 |
| 15 | EEM | 11% | -1.2 | 1.9 | 7.4 | -3.3 | 0.2 | 1 |
| 16 | LQD | 10% | -0.0 | 0.4 | 5.2 | -0.0 | -0.1 | 0 |
| 17 | GLD | 10% | -0.6 | 2.0 | 8.3 | -0.2 | 1.8 | 5 |
| 18 | XLK | 10% | -0.8 | 0.9 | 1.5 | -1.2 | 1.4 | 6 |
| 19 | IEF | 8% | -0.1 | 0.2 | 5.0 | -0.4 | -1.2 | 0 |
| 20 | XLY | 8% | -1.1 | 1.2 | 7.6 | -0.9 | -1.9 | 4 |
| 21 | GDX | 8% | -1.1 | 2.9 | -10.3 | -2.3 | 4.0 | 5 |
| 22 | USO | 8% | -3.0 | 3.1 | -16.0 | -4.1 | 0.4 | 1 |
| 23 | USMV | 6% | 0.6 | 3.2 | 14.2 | 2.0 | 0.2 | 2 |
| 24 | XLU | 6% | -0.9 | 0.6 | 5.9 | -0.9 | -0.1 | 1 |
| 25 | VT | 5% | -0.9 | 1.0 | 12.1 | -1.1 | 0.6 | 0 |
| 26 | DIA | 5% | -0.9 | 0.2 | 6.5 | -0.5 | -0.2 | 0 |
| 27 | XLB | 5% | -1.0 | 0.3 | 5.7 | -1.0 | 1.0 | 1 |
| 28 | VOO | 5% | -1.2 | 0.6 | 11.9 | -0.1 | 0.1 | 1 |
| 29 | QQQ | 5% | -1.4 | 0.6 | 4.1 | -1.6 | -2.0 | 0 |
| 30 | DBC | 3% | -0.5 | 0.2 | -5.5 | -1.1 | -0.5 | 1 |
| 31 | SPY | 3% | -0.7 | 0.1 | 9.3 | -1.1 | -0.4 | 1 |
| 32 | VUG | 3% | -1.5 | 0.4 | 8.8 | -1.5 | 0.5 | 1 |
| 33 | ACWI | 3% | -1.5 | 2.0 | 10.5 | -2.4 | -0.2 | 0 |
| 34 | BND | 2% | -0.1 | 0.1 | 4.1 | -0.4 | -0.7 | 0 |
| 35 | VWO | 2% | -1.8 | 0.0 | 4.3 | -3.8 | 1.9 | 1 |
| 36 | VEA | 2% | -1.8 | 0.1 | 0.5 | -3.1 | -0.1 | 1 |
| 37 | IWM | 2% | -2.2 | 0.8 | 7.0 | -3.2 | -1.1 | 0 |
| 38 | SQQQ | 2% | -2.7 | 2.4 | -50.7 | -2.7 | -6.7 | 0 |
| 39 | SHY | 0% | -0.1 | n/a | 2.1 | -0.3 | -0.5 | 0 |
| 40 | AGG | 0% | -0.1 | n/a | 4.3 | -0.1 | -0.7 | 0 |

(8 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 3,618 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
