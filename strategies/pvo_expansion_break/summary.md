# pvo_expansion_break: optimization summary

Updated 2026-11-25T10:33:15Z · backtest.py version `4a6c2ff343` · 43,963 parameter sets tested with this version (43,963 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: IWM (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [pvo_expansion_break__max-income__v001.md](pvo_expansion_break__max-income__v001.md) | 43962 | `{"level": 2, "max_candles": 42, "stop_atr": 2.75, "take_profit_atr": 2.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [pvo_expansion_break__balanced__v001.md](pvo_expansion_break__balanced__v001.md) | 43963 | `{"level": 2, "max_candles": 54, "stop_atr": 2.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,929.02 | 496.46 | 2,943.36 | 532.92 |
| return % | 29.29 | 4.96 | 29.43 | 5.33 |
| return %/year | 1.7 | 0.5 | 1.7 | 0.5 |
| gross profit | 5,691.12 | 3,252.51 | 5,706.69 | 3,240.58 |
| gross loss | 2,762.10 | 2,756.05 | 2,763.32 | 2,707.66 |
| trades | 22 | 19 | 22 | 19 |
| win rate % | 54.5 | 47.4 | 54.5 | 47.4 |
| avg win | 474.26 | 361.39 | 475.56 | 360.06 |
| avg loss | -276.21 | -275.60 | -276.33 | -270.77 |
| avg result / trade | 133.14 | 26.13 | 133.79 | 28.05 |
| largest single loss | -443.75 | -442.80 | -388.92 | -441.06 |
| largest loss % of equity | -3.51 | -4.38 | -2.85 | -4.37 |
| max drawdown | -1,492.65 | -1,149.84 | -1,419.12 | -1,145.62 |
| max drawdown % | -11.45 | -9.89 | -10.89 | -9.89 |
| profit factor | 2.06 | 1.18 | 2.06 | 1.20 |
| unusually bad trades | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 4.4 | 5.3 | 4.5 | 5.6 |
| time in market % | 6.8 | 7.2 | 6.8 | 6.9 |
| buy & hold return % | 177.00 | 175.35 | 177.00 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |  | 0.28 |
| period | 2000-12-29 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-12-29 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 0.0 | 0.0 |
| 2001 | 5.7 | 5.7 |
| 2002 | 0.0 | 0.0 |
| 2003 | 4.0 | 4.0 |
| 2004 | 7.9 | 7.9 |
| 2005 | 8.9 | 8.9 |
| 2006 | -2.2 | -2.2 |
| 2007 | -3.5 | -2.9 |
| 2008 | -2.7 | -2.7 |
| 2009 | 11.0 | 11.0 |
| 2010 | 5.1 | 5.1 |
| 2011 | 0.0 | 0.0 |
| 2012 | -3.4 | -3.4 |
| 2013 | 1.3 | 1.3 |
| 2014 | -2.5 | -2.5 |
| 2015 | -2.2 | -2.7 |
| 2016 (OOS) | 0.0 | 0.0 |
| 2017 (OOS) | -4.1 | -4.5 |
| 2018 (OOS) | 0.0 | 0.0 |
| 2019 (OOS) | 0.9 | 0.9 |
| 2020 (OOS) | 2.6 | 2.6 |
| 2021 (OOS) | 2.0 | 2.0 |
| 2022 (OOS) | 0.0 | 0.0 |
| 2023 (OOS) | 9.1 | 9.1 |
| 2024 (OOS) | -3.2 | -3.2 |
| 2025 (OOS) | 2.2 | 2.2 |
| 2026 (OOS) | -3.9 | -3.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 11.4% from a peak in-sample and 9.9% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 55 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 1.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 87% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 10.9% from a peak in-sample and 9.9% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 55 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 1.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 92% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4252 | `{"level": 2, "max_candles": 48, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 4253 | `{"level": 2, "max_candles": 60, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 4254 | `{"level": 2, "max_candles": 54, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | 1.00 |
| 15221 | `{"level": 2, "max_candles": 36, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 16327 | `{"level": 2, "max_candles": 24, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 16527 | `{"level": 2, "max_candles": 42, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 18649 | `{"level": 2, "max_candles": 84, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 20799 | `{"level": 2, "max_candles": 66, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 25179 | `{"level": 2, "max_candles": 72, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 27944 | `{"level": 2, "max_candles": 30, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 28312 | `{"level": 2, "max_candles": 96, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 30585 | `{"level": 2, "max_candles": 78, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 36877 | `{"level": 2, "max_candles": 90, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,943.36 | 1.7 | -10.9 | 54.5 | 532.92 | 0.5 | -9.9 | 0.28 | 22/19 | not checked |
| 1129 | `{"level": 0, "max_candles": 78, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 926.58 | 0.8 | -9.2 | 0.64 | 21/15 | not checked |
| 1395 | `{"level": 0, "max_candles": 72, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 926.58 | 0.8 | -9.2 | 0.64 | 21/15 | not checked |
| 1771 | `{"level": 0, "max_candles": 60, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 926.58 | 0.8 | -9.2 | 0.64 | 21/15 | not checked |
| 2026 | `{"level": 0, "max_candles": 36, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 915.06 | 0.8 | -9.2 | 0.63 | 21/15 | not checked |
| 3885 | `{"level": 0, "max_candles": 42, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 1,100.24 | 1.0 | -9.2 | 0.75 | 21/15 | not checked |
| 5519 | `{"level": 0, "max_candles": 78, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 1,100.24 | 1.0 | -9.2 | 0.75 | 21/15 | not checked |
| 5989 | `{"level": 0, "max_candles": 48, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 1,100.24 | 1.0 | -9.2 | 0.75 | 21/15 | not checked |
| 7213 | `{"level": 0, "max_candles": 96, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 1,100.24 | 1.0 | -9.2 | 0.75 | 21/15 | not checked |
| 7603 | `{"level": 0, "max_candles": 90, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 1,100.24 | 1.0 | -9.2 | 0.75 | 21/15 | not checked |
| 8115 | `{"level": 0, "max_candles": 48, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 926.58 | 0.8 | -9.2 | 0.64 | 21/15 | not checked |
| 8593 | `{"level": 0, "max_candles": 90, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 926.58 | 0.8 | -9.2 | 0.64 | 21/15 | not checked |
| 8739 | `{"level": 0, "max_candles": 54, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,097.50 | 1.3 | -10.1 | 47.6 | 1,100.24 | 1.0 | -9.2 | 0.75 | 21/15 | not checked |

(40 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

48 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | GLD | 40% | 0.2 | 3.5 | 8.3 | -1.8 | 2.0 | 20 |
| 2 | SOXX | 37% | 1.2 | 2.2 | 3.5 | 2.2 | -0.7 | 18 |
| 3 | LQD | 17% | -0.0 | 0.5 | 5.2 | -0.6 | 0.1 | 6 |
| 4 | TLT | 16% | -0.3 | 1.3 | 6.3 | -1.5 | -1.4 | 5 |
| 5 | SPY | 14% | 0.1 | 1.6 | 9.3 | -0.2 | 1.1 | 2 |
| 6 | XLK | 14% | -0.1 | 1.6 | 1.5 | 0.4 | -1.3 | 4 |
| 7 | IWM | 13% | 0.0 | 1.7 | 7.0 | 0.1 | 0.0 | 6 |
| 8 | XLY | 11% | -0.7 | 1.4 | 7.6 | -1.0 | 0.5 | 0 |
| 9 | SLV | 10% | -0.3 | 1.8 | -0.5 | -0.2 | 3.9 | 5 |
| 10 | VUG | 8% | -0.6 | 1.2 | 8.8 | -0.1 | -0.0 | 5 |
| 11 | EFA | 6% | 0.3 | 1.1 | 5.6 | 0.6 | 0.4 | 4 |
| 12 | EEM | 6% | 0.0 | 2.2 | 7.4 | 0.6 | 0.6 | 3 |
| 13 | XLB | 6% | -0.2 | 0.5 | 5.7 | -0.8 | 0.8 | 0 |
| 14 | QQQ | 5% | 0.0 | 0.9 | 4.1 | 0.1 | 0.0 | 1 |
| 15 | XLV | 5% | -0.1 | 0.8 | 7.2 | -0.2 | -0.7 | 2 |
| 16 | AGG | 3% | -0.1 | 0.3 | 4.3 | 0.3 | 0.1 | 2 |
| 17 | RSP | 3% | -0.2 | 0.6 | 8.8 | 0.1 | -0.4 | 0 |
| 18 | IEF | 3% | -0.3 | 0.1 | 5.0 | -0.9 | -0.1 | 0 |
| 19 | TIP | 3% | -0.4 | 0.2 | 4.2 | -0.8 | 0.1 | 0 |
| 20 | HYG | 2% | -0.1 | 0.2 | 4.4 | 0.1 | -0.2 | 0 |
| 21 | XLI | 2% | -0.3 | 0.2 | 5.5 | -0.5 | 0.5 | 1 |
| 22 | VNQ | 2% | -0.6 | 0.6 | 8.4 | -0.1 | -0.7 | 0 |
| 23 | USMV | 0% | 1.4 | n/a | 14.2 | 1.2 | -0.0 | 0 |
| 24 | VWO | 0% | 0.8 | n/a | 4.3 | -0.7 | 0.2 | 0 |
| 25 | SCHD | 0% | 0.7 | n/a | 13.7 | 1.4 | 0.1 | 0 |
| 26 | VIG | 0% | 0.4 | n/a | 6.5 | 1.1 | -0.2 | 0 |
| 27 | DIA | 0% | 0.2 | n/a | 6.5 | 0.6 | 0.5 | 0 |
| 28 | VXUS | 0% | 0.2 | n/a | 3.0 | 0.5 | -0.5 | 0 |
| 29 | DBC | 0% | 0.1 | n/a | -5.5 | 0.8 | -0.4 | 0 |
| 30 | XLE | 0% | 0.0 | n/a | 6.6 | 0.8 | 0.5 | 0 |
| 31 | TQQQ | 0% | 0.0 | n/a | 52.0 | -1.2 | 0.0 | 0 |
| 32 | MTUM | 0% | -0.0 | n/a | 13.6 | 1.0 | -0.3 | 0 |
| 33 | IVV | 0% | -0.1 | n/a | 5.3 | -0.1 | -0.5 | 0 |
| 34 | VTI | 0% | -0.1 | n/a | 7.1 | -0.4 | 0.6 | 0 |
| 35 | VOO | 0% | -0.1 | n/a | 11.9 | -0.2 | 0.5 | 0 |
| 36 | BND | 0% | -0.1 | n/a | 4.1 | 0.2 | -0.1 | 0 |
| 37 | SHY | 0% | -0.2 | n/a | 2.1 | -0.3 | -0.1 | 0 |
| 38 | XLF | 0% | -0.3 | n/a | 1.7 | 0.5 | 1.2 | 0 |
| 39 | XLU | 0% | -0.3 | n/a | 5.9 | -1.0 | 0.4 | 0 |
| 40 | ACWI | 0% | -0.4 | n/a | 10.5 | -0.8 | -0.0 | 0 |

(8 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [pvo_expansion_break__broad__max-income__v002.md](symbols/broad/pvo_expansion_break__broad__max-income__v002.md) | 0.1 | 0.0 | 0.0 | -2.4 | 49.2 | 932/916 |
| broad | balanced | [pvo_expansion_break__broad__balanced__v001.md](symbols/broad/pvo_expansion_break__broad__balanced__v001.md) | 0.0 | 0.1 | 0.0 | -0.6 | 56.7 | 150/76 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 43,963 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
