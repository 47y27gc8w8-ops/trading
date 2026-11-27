# ppo_percentage_trend: optimization summary

Updated 2026-11-25T09:51:21Z · backtest.py version `56ab330998` · 30,468 parameter sets tested with this version (30,468 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: XLK (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [ppo_percentage_trend__max-income__v001.md](ppo_percentage_trend__max-income__v001.md) | 30466 | `{"max_candles": 84, "stop_atr": 3.0, "take_profit_atr": 6.0, "threshold": 0.75}` | flat (data up to 2026-11-24 00:00) |
| balanced | [ppo_percentage_trend__balanced__v001.md](ppo_percentage_trend__balanced__v001.md) | 30467 | `{"max_candles": 96, "stop_atr": 1.25, "take_profit_atr": 5.0, "threshold": 1.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [ppo_percentage_trend__safe-starter__v001.md](ppo_percentage_trend__safe-starter__v001.md) | 30468 | `{"max_candles": 120, "stop_atr": 0.5, "take_profit_atr": 5.5, "threshold": 1.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 9,189.76 | 8,778.63 | 7,857.37 | 6,868.67 | 3,891.10 | 2,545.40 |
| return % | 91.90 | 87.79 | 78.57 | 68.69 | 38.91 | 25.45 |
| return %/year | 4.4 | 6.0 | 3.9 | 4.9 | 2.2 | 2.1 |
| gross profit | 13,928.12 | 11,711.65 | 12,538.52 | 8,987.98 | 6,196.84 | 3,897.18 |
| gross loss | 4,738.36 | 2,933.02 | 4,681.15 | 2,119.31 | 2,305.74 | 1,351.78 |
| trades | 20 | 11 | 25 | 14 | 25 | 14 |
| win rate % | 65.0 | 72.7 | 48.0 | 57.1 | 32.0 | 28.6 |
| avg win | 1,071.39 | 1,463.96 | 1,044.88 | 1,123.50 | 774.60 | 974.29 |
| avg loss | -676.91 | -977.67 | -360.09 | -353.22 | -135.63 | -135.18 |
| avg result / trade | 459.49 | 798.06 | 314.29 | 490.62 | 155.64 | 181.81 |
| largest single loss | -955.21 | -1,202.52 | -493.01 | -552.49 | -220.60 | -189.64 |
| largest loss % of equity | -10.48 | -8.06 | -2.84 | -3.48 | -1.83 | -1.66 |
| max drawdown | -1,844.74 | -1,436.55 | -1,456.09 | -1,050.69 | -977.91 | -1,028.40 |
| max drawdown % | -18.45 | -9.58 | -9.42 | -6.48 | -7.74 | -8.70 |
| profit factor | 2.94 | 3.99 | 2.68 | 4.24 | 2.69 | 2.88 |
| unusually bad trades | 0 | 0 | 1 | 0 | 1 | 0 |
| … threshold (% of equity) | 11.3 | 14.1 | 4.3 | 4.9 | 2.0 | 2.5 |
| time in market % | 22.6 | 14.9 | 15.3 | 13.2 | 10.8 | 8.2 |
| buy & hold return % | 38.82 | 767.30 | 38.82 | 767.30 | 38.82 | 767.30 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.34 |  | 1.25 |  | 0.95 |
| period | 2000-12-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-12-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-12-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 0.0 | 0.0 | 0.0 |
| 2001 | -8.9 | -3.8 | -1.6 |
| 2002 | -9.9 | -4.4 | -2.1 |
| 2003 | 14.2 | 12.2 | -1.4 |
| 2004 | 3.1 | 7.0 | 7.7 |
| 2005 | 0.0 | -1.5 | -0.6 |
| 2006 | 14.0 | 12.6 | 13.9 |
| 2007 | 5.8 | 14.8 | 5.0 |
| 2008 | -9.9 | -3.7 | -1.2 |
| 2009 | 18.3 | 15.3 | -1.8 |
| 2010 | 17.9 | 13.7 | 15.1 |
| 2011 | -4.7 | -7.2 | -3.2 |
| 2012 | 22.8 | 5.9 | 7.9 |
| 2013 | 6.5 | 1.8 | -2.3 |
| 2014 | 2.8 | -1.8 | -0.8 |
| 2015 | 2.2 | 2.6 | 0.9 |
| 2016 (OOS) | 3.0 | 2.5 | 4.4 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 9.4 | 10.4 |
| 2019 (OOS) | 8.7 | 7.1 | -1.0 |
| 2020 (OOS) | 19.1 | 15.2 | -1.7 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | -7.1 | -2.8 | -1.2 |
| 2023 (OOS) | 16.7 | 15.9 | 6.1 |
| 2024 (OOS) | -4.0 | 1.2 | -2.7 |
| 2025 (OOS) | 17.0 | -2.7 | -1.3 |
| 2026 (OOS) | 12.0 | 9.9 | 10.9 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 18.4% from a peak in-sample and 9.6% out-of-sample, and the worst single trade cost 8.1% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 54% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 9.4% from a peak in-sample and 6.5% out-of-sample, and the worst single trade cost 3.5% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 7.7% from a peak in-sample and 8.7% out-of-sample, and the worst single trade cost 1.7% of the account out-of-sample. About 32 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10650 | `{"max_candles": 84, "stop_atr": 3.0, "take_profit_atr": 6.0, "threshold": 0.75}` | 9,189.76 | 4.4 | -18.4 | 65.0 | 8,778.63 | 6.0 | -9.6 | 1.34 | 20/11 | 1.00 |
| 17835 | `{"max_candles": 72, "stop_atr": 1.5, "take_profit_atr": 5.0, "threshold": 1.0}` | 8,722.74 | 4.3 | -10.5 | 52.0 | 8,884.46 | 6.0 | -7.3 | 1.41 | 25/14 | not checked |
| 23862 | `{"max_candles": 72, "stop_atr": 1.0, "take_profit_atr": 6.5, "threshold": 1.0}` | 8,218.19 | 4.1 | -9.1 | 40.0 | 5,582.72 | 4.2 | -8.2 | 1.02 | 25/14 | not checked |
| 29348 | `{"max_candles": 72, "stop_atr": 0.5, "take_profit_atr": 5.5, "threshold": 1.0}` | 4,519.99 | 2.5 | -7.7 | 32.0 | 2,204.74 | 1.9 | -8.7 | 0.74 | 25/14 | not checked |
| 26917 | `{"max_candles": 156, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 27250 | `{"max_candles": 48, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 27444 | `{"max_candles": 180, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 27597 | `{"max_candles": 72, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 28078 | `{"max_candles": 96, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 28812 | `{"max_candles": 144, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 29285 | `{"max_candles": 60, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 29547 | `{"max_candles": 132, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 29717 | `{"max_candles": 168, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 29731 | `{"max_candles": 84, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 29747 | `{"max_candles": 120, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 30083 | `{"max_candles": 192, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |
| 30224 | `{"max_candles": 108, "stop_atr": 0.5, "take_profit_atr": 2.0, "threshold": 1.0}` | 2,478.42 | 1.5 | -4.1 | 48.0 | 1,452.79 | 1.2 | -4.9 | 0.84 | 25/14 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

47 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SPY | 94% | 1.6 | 5.1 | 9.3 | 0.2 | 1.7 | 52 |
| 2 | XLY | 91% | 1.9 | 4.2 | 9.4 | 0.7 | 2.6 | 45 |
| 3 | XLB | 83% | 1.3 | 5.3 | 7.7 | 0.1 | -0.1 | 7 |
| 4 | QQQ | 83% | 1.2 | 4.0 | 6.7 | 0.2 | 1.7 | 53 |
| 5 | IVV | 75% | 1.9 | 3.9 | 6.8 | 0.4 | 1.7 | 39 |
| 6 | XLE | 75% | 0.9 | 5.9 | 6.3 | 2.0 | -0.8 | 26 |
| 7 | XLV | 73% | 0.8 | 3.2 | 8.0 | 0.2 | -0.7 | 26 |
| 8 | XLF | 69% | 0.6 | 3.7 | 1.0 | -0.4 | 1.4 | 13 |
| 9 | IWM | 59% | 2.1 | 4.7 | 7.8 | 1.4 | -0.6 | 10 |
| 10 | XLU | 59% | 0.5 | 3.5 | 5.5 | -0.6 | 1.4 | 20 |
| 11 | XLI | 59% | 0.2 | 2.9 | 5.5 | 0.1 | 1.3 | 34 |
| 12 | DIA | 58% | 0.2 | 2.2 | 4.9 | -0.3 | 0.1 | 22 |
| 13 | XLP | 56% | 0.2 | 2.3 | 6.5 | -0.8 | 1.8 | 32 |
| 14 | XLK | 56% | 0.2 | 4.4 | 2.2 | 1.4 | 3.0 | 36 |
| 15 | VTI | 39% | 1.5 | 4.3 | 8.5 | 1.0 | 2.6 | 14 |
| 16 | EFA | 36% | 0.8 | 2.0 | 6.5 | 1.1 | 1.1 | 18 |
| 17 | SOXX | 36% | 0.7 | 2.5 | 5.6 | 0.3 | -0.3 | 20 |
| 18 | SMH | 27% | 0.4 | 4.4 | 3.0 | -0.3 | -0.1 | 15 |
| 19 | IEF | 22% | 0.5 | 1.4 | 5.3 | 0.2 | -0.6 | 5 |
| 20 | TLT | 19% | 1.1 | 3.3 | 7.1 | -0.4 | -0.6 | 1 |
| 21 | VUG | 12% | 1.6 | 1.8 | 8.3 | 0.7 | 2.0 | 6 |
| 22 | LQD | 6% | -0.1 | 0.6 | 5.1 | 0.4 | 0.1 | 3 |
| 23 | RSP | 5% | 3.1 | 2.9 | 8.6 | 2.8 | 2.4 | 0 |
| 24 | VNQ | 5% | 1.0 | 2.7 | 5.8 | -0.7 | -0.6 | 0 |
| 25 | TQQQ | 0% | 7.7 | n/a | 50.9 | 10.3 | 5.7 | 0 |
| 26 | EEM | 0% | 2.6 | n/a | 5.0 | 1.8 | 0.4 | 0 |
| 27 | VTV | 0% | 2.1 | n/a | 6.2 | 0.4 | 1.0 | 0 |
| 28 | HYG | 0% | 1.9 | n/a | 9.5 | 1.7 | 0.5 | 0 |
| 29 | VIG | 0% | 1.8 | n/a | 7.1 | 0.1 | 1.0 | 0 |
| 30 | VWO | 0% | 1.6 | n/a | 1.3 | 0.5 | 1.4 | 0 |
| 31 | VT | 0% | 1.4 | n/a | 8.7 | 1.5 | 0.8 | 0 |
| 32 | USMV | 0% | 1.4 | n/a | 12.3 | 0.8 | 0.7 | 0 |
| 33 | ACWI | 0% | 1.2 | n/a | 6.9 | 1.4 | -0.0 | 0 |
| 34 | VOO | 0% | 0.4 | n/a | 14.0 | -0.3 | 1.7 | 0 |
| 35 | VEA | 0% | 0.4 | n/a | 6.3 | 0.8 | 0.7 | 0 |
| 36 | TIP | 0% | 0.1 | n/a | 3.9 | -0.1 | 0.3 | 0 |
| 37 | AGG | 0% | 0.0 | n/a | 4.2 | 0.4 | 0.3 | 0 |
| 38 | GLD | 0% | 0.0 | n/a | 5.6 | 2.5 | 0.9 | 0 |
| 39 | SHY | 0% | 0.0 | n/a | 2.2 | -0.0 | 0.0 | 0 |
| 40 | BND | 0% | 0.0 | n/a | 3.9 | 0.2 | 0.3 | 0 |

(7 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [ppo_percentage_trend__broad__max-income__v002.md](symbols/broad/ppo_percentage_trend__broad__max-income__v002.md) | 1.3 | 3.0 | 1.3 | -8.3 | 50.1 | 595/688 |
| broad | balanced | [ppo_percentage_trend__broad__balanced__v002.md](symbols/broad/ppo_percentage_trend__broad__balanced__v002.md) | 1.2 | 2.7 | 1.2 | -7.5 | 51.7 | 600/696 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 30,468 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
