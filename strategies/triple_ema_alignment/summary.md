# triple_ema_alignment: optimization summary

Updated 2026-11-25T07:19:30Z · backtest.py version `861ff684f9` · 928 parameter sets tested with this version (928 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [triple_ema_alignment__max-income__v002.md](triple_ema_alignment__max-income__v002.md) | 928 | `{"fast": 3, "max_candles": 120, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 5,107.98 | 4,046.14 |
| return % | 51.08 | 40.46 |
| return %/year | 2.6 | 3.2 |
| gross profit | 21,334.77 | 12,867.34 |
| gross loss | 16,226.79 | 8,821.20 |
| trades | 106 | 63 |
| win rate % | 34.0 | 42.9 |
| avg win | 592.63 | 476.57 |
| avg loss | -231.81 | -245.03 |
| avg result / trade | 48.19 | 64.22 |
| largest single loss | -613.18 | -612.14 |
| largest loss % of equity | -5.66 | -4.65 |
| max drawdown | -2,471.47 | -2,556.32 |
| max drawdown % | -15.25 | -15.56 |
| profit factor | 1.31 | 1.46 |
| unusually bad trades | 9 | 5 |
| … threshold (% of equity) | 3.1 | 3.6 |
| time in market % | 23.6 | 21.4 |
| buy & hold return % | 28.06 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.22 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2000 | 0.7 |
| 2001 | 14.5 |
| 2002 | -0.3 |
| 2003 | -3.2 |
| 2004 | 7.9 |
| 2005 | 3.8 |
| 2006 | 4.3 |
| 2007 | 13.5 |
| 2008 | 8.3 |
| 2009 | -2.0 |
| 2010 | -2.4 |
| 2011 | -3.2 |
| 2012 | 3.3 |
| 2013 | 9.6 |
| 2014 | -2.6 |
| 2015 | -7.4 |
| 2016 (OOS) | -3.7 |
| 2017 (OOS) | 8.6 |
| 2018 (OOS) | 0.6 |
| 2019 (OOS) | 8.9 |
| 2020 (OOS) | 11.6 |
| 2021 (OOS) | -8.0 |
| 2022 (OOS) | 2.1 |
| 2023 (OOS) | 15.1 |
| 2024 (OOS) | 3.8 |
| 2025 (OOS) | 6.1 |
| 2026 (OOS) | -7.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 15.2% from a peak in-sample and 15.6% out-of-sample, and the worst single trade cost 4.7% of the account out-of-sample. About 34 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 64% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 365 | `{"fast": 3, "max_candles": 120, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | 1.00 |
| 417 | `{"fast": 3, "max_candles": 120, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 420 | `{"fast": 3, "max_candles": 108, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | not checked |
| 421 | `{"fast": 3, "max_candles": 132, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | not checked |
| 439 | `{"fast": 3, "max_candles": 84, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | not checked |
| 460 | `{"fast": 3, "max_candles": 144, "mid": 10, "slow": 13, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,905.46 | 3.1 | -15.6 | 1.18 | 106/63 | not checked |
| 461 | `{"fast": 3, "max_candles": 156, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 476 | `{"fast": 3, "max_candles": 156, "mid": 10, "slow": 13, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,993.81 | 3.1 | -15.6 | 1.20 | 106/63 | not checked |
| 490 | `{"fast": 3, "max_candles": 108, "mid": 10, "slow": 13, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,993.81 | 3.1 | -15.6 | 1.20 | 106/63 | not checked |
| 492 | `{"fast": 3, "max_candles": 96, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | not checked |
| 495 | `{"fast": 3, "max_candles": 132, "mid": 10, "slow": 13, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,993.81 | 3.1 | -15.6 | 1.20 | 106/63 | not checked |
| 512 | `{"fast": 3, "max_candles": 156, "mid": 10, "slow": 13, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,905.46 | 3.1 | -15.6 | 1.18 | 106/63 | not checked |
| 516 | `{"fast": 3, "max_candles": 144, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 519 | `{"fast": 3, "max_candles": 72, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | not checked |
| 522 | `{"fast": 3, "max_candles": 156, "mid": 10, "slow": 13, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,905.46 | 3.1 | -15.6 | 1.18 | 106/63 | not checked |
| 532 | `{"fast": 3, "max_candles": 132, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 533 | `{"fast": 3, "max_candles": 120, "mid": 10, "slow": 13, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,905.46 | 3.1 | -15.6 | 1.18 | 106/63 | not checked |
| 556 | `{"fast": 3, "max_candles": 144, "mid": 10, "slow": 13, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,993.81 | 3.1 | -15.6 | 1.20 | 106/63 | not checked |
| 575 | `{"fast": 3, "max_candles": 168, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 588 | `{"fast": 3, "max_candles": 108, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 599 | `{"fast": 3, "max_candles": 144, "mid": 10, "slow": 13, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,046.14 | 3.2 | -15.6 | 1.22 | 106/63 | not checked |
| 695 | `{"fast": 3, "max_candles": 96, "mid": 10, "slow": 13, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 4,019.97 | 3.1 | -15.6 | 1.21 | 106/63 | not checked |
| 702 | `{"fast": 3, "max_candles": 168, "mid": 10, "slow": 13, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,993.81 | 3.1 | -15.6 | 1.20 | 106/63 | not checked |
| 704 | `{"fast": 3, "max_candles": 120, "mid": 10, "slow": 13, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,993.81 | 3.1 | -15.6 | 1.20 | 106/63 | not checked |
| 718 | `{"fast": 3, "max_candles": 132, "mid": 10, "slow": 13, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 5,107.98 | 2.6 | -15.2 | 34.0 | 3,905.46 | 3.1 | -15.6 | 1.18 | 106/63 | not checked |

(5 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 98% | 2.5 | 4.0 | 5.0 | 2.2 | -0.4 | 9 |
| 2 | GLD | 92% | 1.4 | 5.9 | 8.3 | 0.5 | -0.1 | 27 |
| 3 | VNQ | 84% | 2.7 | 6.8 | 7.6 | 4.3 | 0.1 | 2 |
| 4 | TLT | 83% | 0.8 | 2.8 | 6.2 | 1.4 | -1.4 | 4 |
| 5 | EFA | 83% | 0.7 | 3.1 | 6.0 | 0.9 | -2.3 | 4 |
| 6 | LQD | 79% | 0.6 | 1.8 | 4.9 | 0.5 | -1.2 | 0 |
| 7 | XLU | 78% | 1.0 | 2.8 | 6.4 | 0.8 | -2.2 | 3 |
| 8 | SLV | 75% | 4.3 | 9.8 | -0.7 | 2.5 | -1.6 | 0 |
| 9 | DBC | 63% | 0.4 | 2.3 | -5.8 | -0.9 | 0.9 | 39 |
| 10 | BND | 56% | 0.1 | 0.8 | 3.8 | 0.1 | -0.4 | 4 |
| 11 | SOXX | 51% | 0.1 | 4.3 | 3.7 | 0.2 | 3.8 | 24 |
| 12 | EEM | 40% | -0.3 | 2.0 | 6.4 | -2.0 | 0.4 | 14 |
| 13 | GDX | 35% | -0.9 | 5.0 | -10.5 | -2.2 | 6.3 | 17 |
| 14 | IWDA.AS | 33% | -0.2 | 3.2 | 13.5 | 0.2 | -0.9 | 4 |
| 15 | VOO | 33% | -0.8 | 3.4 | 13.1 | -1.9 | 2.5 | 19 |
| 16 | IWM | 32% | -0.6 | 1.1 | 7.8 | 0.8 | -0.9 | 0 |
| 17 | DIA | 27% | -0.5 | 2.0 | 4.9 | -1.1 | 0.4 | 13 |
| 18 | VWO | 27% | -0.7 | 2.6 | 3.3 | 1.2 | -0.9 | 1 |
| 19 | VEA | 24% | -1.1 | 2.4 | 0.0 | -1.2 | -2.3 | 5 |
| 20 | QQQ | 22% | -1.4 | 2.6 | 1.6 | 0.1 | 2.5 | 12 |
| 21 | IEF | 21% | -0.6 | 0.9 | 5.0 | -0.1 | -1.3 | 2 |
| 22 | AGG | 17% | -0.3 | 1.0 | 4.2 | 0.3 | -0.4 | 2 |
| 23 | CSSPX.SW | 17% | -1.1 | 1.5 | 11.6 | 1.2 | 1.6 | 10 |
| 24 | VUG | 16% | -0.9 | 1.1 | 8.3 | -0.8 | 1.0 | 10 |
| 25 | SCHD | 14% | -0.2 | 1.6 | 12.4 | 1.7 | -1.4 | 0 |
| 26 | VTI | 11% | -0.6 | 0.5 | 7.1 | -0.7 | 2.3 | 6 |
| 27 | SPY | 10% | -1.1 | 1.2 | 3.9 | -0.8 | 2.8 | 6 |
| 28 | CSPX.L | 10% | -1.5 | 0.8 | 12.1 | -1.1 | 3.1 | 1 |
| 29 | XLK | 10% | -1.5 | 0.5 | -0.5 | -0.9 | 2.2 | 5 |
| 30 | IVV | 8% | -1.1 | 1.9 | 5.3 | -0.6 | 2.2 | 5 |
| 31 | VIG | 8% | -2.4 | 2.0 | 6.2 | -2.7 | 0.3 | 3 |
| 32 | ACWI | 8% | -2.4 | 1.9 | 10.8 | -3.1 | 1.2 | 2 |
| 33 | TQQQ | 8% | -6.7 | 4.4 | 45.7 | -7.8 | 5.2 | 5 |
| 34 | XLV | 6% | -1.3 | 2.5 | 6.9 | -0.9 | 0.5 | 4 |
| 35 | VTV | 6% | -1.3 | 0.5 | 6.8 | -1.9 | -0.8 | 4 |
| 36 | XLY | 6% | -1.4 | 2.0 | 7.2 | -0.8 | -0.1 | 1 |
| 37 | CSNDX.SW | 6% | -3.0 | 0.6 | 16.8 | -0.7 | 4.7 | 4 |
| 38 | VT | 5% | -2.5 | 1.2 | 11.9 | -0.7 | 0.8 | 2 |
| 39 | RSP | 3% | -1.7 | 0.7 | 8.2 | -2.1 | 0.5 | 2 |
| 40 | XLP | 3% | -1.7 | 0.4 | 7.4 | -1.6 | -1.5 | 1 |

(13 more in screen.csv)

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

Searching 928 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
