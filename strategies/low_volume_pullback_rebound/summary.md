# low_volume_pullback_rebound: optimization summary

Updated 2026-11-26T05:33:39Z · backtest.py version `834d5c61c2` · 48,213 parameter sets tested with this version (48,213 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: AAPL (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [low_volume_pullback_rebound__max-income__v001.md](low_volume_pullback_rebound__max-income__v001.md) | 48212 | `{"fraction": 0.85, "max_candles": 32, "stop_atr": 2.5, "take_profit_atr": 7.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [low_volume_pullback_rebound__balanced__v001.md](low_volume_pullback_rebound__balanced__v001.md) | 48213 | `{"fraction": 0.85, "max_candles": 48, "stop_atr": 2.5, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 67,149.73 | 6,219.50 | 20,572.71 | 1,790.26 |
| return % | 671.50 | 62.19 | 205.73 | 17.90 |
| return %/year | 10.2 | 4.5 | 5.5 | 1.5 |
| gross profit | 140,297.89 | 18,678.55 | 62,258.29 | 13,881.87 |
| gross loss | 73,148.16 | 12,459.06 | 41,685.58 | 12,091.61 |
| trades | 113 | 55 | 129 | 63 |
| win rate % | 38.0 | 41.8 | 45.7 | 46.0 |
| avg win | 3,262.74 | 812.11 | 1,055.23 | 478.69 |
| avg loss | -1,044.97 | -389.35 | -595.51 | -355.64 |
| avg result / trade | 594.25 | 113.08 | 159.48 | 28.42 |
| largest single loss | -3,942.66 | -1,133.95 | -1,519.58 | -1,222.51 |
| largest loss % of equity | -4.56 | -8.45 | -7.48 | -9.03 |
| max drawdown | -18,628.08 | -2,841.35 | -4,369.53 | -2,671.61 |
| max drawdown % | -42.23 | -17.62 | -36.01 | -22.80 |
| profit factor | 1.92 | 1.50 | 1.49 | 1.15 |
| unusually bad trades | 8 | 7 | 8 | 3 |
| … threshold (% of equity) | 6.3 | 4.3 | 6.7 | 5.8 |
| time in market % | 21.7 | 26.6 | 13.3 | 18.0 |
| buy & hold return % | 8,135.28 | 1,414.11 | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.44 |  | 0.28 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 27.7 | 8.8 |
| 1996 | -17.1 | -2.9 |
| 1997 | -5.1 | -5.1 |
| 1998 | 9.3 | -15.8 |
| 1999 | 50.0 | 32.1 |
| 2000 | -21.5 | -21.5 |
| 2001 | 0.2 | 19.5 |
| 2002 | -15.6 | -15.6 |
| 2003 | 22.9 | 18.5 |
| 2004 | 34.6 | 14.8 |
| 2005 | 46.5 | 30.8 |
| 2006 | 1.2 | 3.9 |
| 2007 | 26.8 | 15.1 |
| 2008 | 19.9 | -0.5 |
| 2009 | 52.7 | 29.7 |
| 2010 | 6.7 | 3.8 |
| 2011 | -1.1 | 9.8 |
| 2012 | 23.8 | 17.8 |
| 2013 | 3.5 | 2.5 |
| 2014 | 1.9 | -4.4 |
| 2015 | -10.1 | -4.1 |
| 2016 (OOS) | -1.9 | 1.9 |
| 2017 (OOS) | 20.7 | 6.9 |
| 2018 (OOS) | -9.4 | -9.4 |
| 2019 (OOS) | 25.2 | 12.2 |
| 2020 (OOS) | 16.7 | 2.7 |
| 2021 (OOS) | 0.5 | -2.9 |
| 2022 (OOS) | -11.9 | -14.5 |
| 2023 (OOS) | 5.3 | 18.5 |
| 2024 (OOS) | 17.1 | 6.3 |
| 2025 (OOS) | -1.2 | 7.7 |
| 2026 (OOS) | -4.0 | -7.9 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 42.2% from a peak in-sample and 17.6% out-of-sample, and the worst single trade cost 8.4% of the account out-of-sample. About 38 of every 100 trades won in-sample. Out-of-sample it earned 4.5% a year against 10.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 24% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 36.0% from a peak in-sample and 22.8% out-of-sample, and the worst single trade cost 9.0% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 1.5% a year against 5.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 28% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 37109 | `{"fraction": 0.85, "max_candles": 32, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 67,149.73 | 10.2 | -42.2 | 38.0 | 6,219.50 | 4.5 | -17.6 | 0.44 | 113/55 | 1.00 |
| 33562 | `{"fraction": 0.85, "max_candles": 32, "stop_atr": 1.0, "take_profit_atr": 6.5}` | 54,962.41 | 9.3 | -41.6 | 33.3 | 5,991.40 | 4.4 | -16.2 | 0.47 | 120/58 | not checked |
| 1699 | `{"fraction": 0.85, "max_candles": 44, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 1857 | `{"fraction": 0.85, "max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 5896 | `{"fraction": 0.85, "max_candles": 60, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 6306 | `{"fraction": 0.85, "max_candles": 40, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 7294 | `{"fraction": 0.85, "max_candles": 68, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 9846 | `{"fraction": 0.85, "max_candles": 88, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 10142 | `{"fraction": 0.85, "max_candles": 84, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 12611 | `{"fraction": 0.85, "max_candles": 92, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 15866 | `{"fraction": 0.85, "max_candles": 56, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 16305 | `{"fraction": 0.85, "max_candles": 48, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 16961 | `{"fraction": 0.85, "max_candles": 52, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 18388 | `{"fraction": 0.85, "max_candles": 72, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 22795 | `{"fraction": 0.85, "max_candles": 76, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 23589 | `{"fraction": 0.85, "max_candles": 64, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 27154 | `{"fraction": 0.85, "max_candles": 80, "stop_atr": 2.5, "take_profit_atr": 3.5}` | 38,536.00 | 7.8 | -36.0 | 41.9 | 6,800.31 | 4.9 | -17.4 | 0.62 | 124/60 | not checked |
| 3663 | `{"fraction": 0.85, "max_candles": 80, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |
| 5773 | `{"fraction": 0.85, "max_candles": 48, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |
| 9195 | `{"fraction": 0.85, "max_candles": 28, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 5,677.47 | 4.2 | -17.7 | 0.54 | 129/62 | not checked |
| 9667 | `{"fraction": 0.85, "max_candles": 56, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |
| 9772 | `{"fraction": 0.85, "max_candles": 60, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |
| 10321 | `{"fraction": 0.85, "max_candles": 84, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |
| 11751 | `{"fraction": 0.85, "max_candles": 96, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |
| 11832 | `{"fraction": 0.85, "max_candles": 36, "stop_atr": 1.0, "take_profit_atr": 3.5}` | 38,022.82 | 7.8 | -34.8 | 37.2 | 6,276.11 | 4.6 | -17.7 | 0.59 | 129/62 | not checked |

(84 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

472 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TPL | 98% | 3.7 | 6.4 | 19.6 | 2.5 | 2.3 | 45 |
| 2 | ASML | 95% | 3.0 | 6.5 | 16.9 | 5.9 | 4.7 | 53 |
| 3 | NVR | 95% | 2.8 | 7.5 | 31.2 | 2.3 | -0.6 | 1 |
| 4 | BRO | 95% | 2.0 | 4.1 | 16.1 | 2.0 | -0.7 | 36 |
| 5 | ESS | 95% | 1.3 | 3.8 | 18.9 | 1.5 | -0.7 | 4 |
| 6 | FICO | 94% | 1.9 | 4.7 | 12.9 | 1.0 | 0.2 | 18 |
| 7 | RMD | 94% | 1.6 | 4.6 | 23.7 | 1.8 | 0.3 | 36 |
| 8 | WST | 92% | 1.0 | 2.4 | 13.0 | 0.8 | 3.6 | 45 |
| 9 | TSCO | 90% | 2.7 | 6.3 | 22.3 | 4.0 | 1.6 | 33 |
| 10 | WRB | 90% | 1.8 | 3.8 | 13.7 | 1.4 | 1.4 | 45 |
| 11 | ROP | 90% | 1.0 | 3.3 | 18.5 | 0.3 | 0.3 | 11 |
| 12 | WSM | 89% | 2.4 | 5.0 | 11.4 | 3.5 | -2.4 | 0 |
| 13 | EQIX | 87% | 5.9 | 17.2 | 12.5 | 5.0 | -0.5 | 16 |
| 14 | CSGP | 87% | 3.3 | 6.0 | 13.8 | 3.9 | -2.5 | 5 |
| 15 | KNIN.SW | 87% | 2.8 | 5.5 | 17.7 | 2.9 | 1.5 | 25 |
| 16 | COR | 87% | 2.2 | 5.6 | 18.8 | 2.5 | 1.3 | 8 |
| 17 | DHI | 87% | 1.5 | 5.6 | 16.9 | 2.8 | 0.8 | 39 |
| 18 | SWKS | 86% | 4.1 | 8.9 | 18.7 | 4.9 | -1.2 | 0 |
| 19 | WAT | 86% | 3.8 | 7.9 | 16.2 | 6.0 | 0.8 | 27 |
| 20 | FDS | 86% | 3.1 | 9.1 | 21.8 | 4.1 | 0.4 | 24 |
| 21 | BKNG | 83% | 4.8 | 11.3 | 8.2 | 3.7 | 0.4 | 1 |
| 22 | MGM | 83% | 2.9 | 7.5 | 6.6 | 5.2 | -2.0 | 0 |
| 23 | SYK | 83% | 2.1 | 4.5 | 16.1 | 1.7 | -1.2 | 5 |
| 24 | ODFL | 83% | 1.6 | 4.2 | 17.2 | 1.2 | 0.9 | 31 |
| 25 | AXON | 81% | 12.7 | 24.9 | 20.2 | 12.7 | -0.3 | 1 |
| 26 | MSTR | 81% | 8.3 | 17.9 | 0.9 | 7.8 | -5.1 | 0 |
| 27 | URI | 81% | 5.7 | 8.9 | 3.0 | 5.2 | 1.2 | 1 |
| 28 | JBL | 81% | 3.4 | 8.7 | 20.7 | 7.0 | 1.6 | 7 |
| 29 | IT | 81% | 2.7 | 6.0 | 11.5 | 3.3 | 0.5 | 19 |
| 30 | VLO | 81% | 2.2 | 7.1 | 18.7 | 3.2 | -1.9 | 16 |
| 31 | PGR | 81% | 2.0 | 5.0 | 14.1 | 2.3 | -0.4 | 14 |
| 32 | PSA | 81% | 1.2 | 3.1 | 19.1 | 1.7 | -0.6 | 6 |
| 33 | OKE | 81% | 1.1 | 4.8 | 13.5 | 0.0 | -0.8 | 10 |
| 34 | PWR | 79% | 2.9 | 7.2 | 5.1 | 2.4 | -3.0 | 2 |
| 35 | MCK | 79% | 2.7 | 6.4 | 11.9 | 2.9 | -1.3 | 0 |
| 36 | MOS | 79% | 2.0 | 5.2 | 2.2 | 1.6 | -2.3 | 1 |
| 37 | RJF | 78% | 1.8 | 5.0 | 17.2 | -0.1 | -1.2 | 11 |
| 38 | J | 78% | 1.5 | 3.1 | 11.0 | 2.8 | 0.6 | 10 |
| 39 | BLK | 76% | 3.8 | 8.9 | 20.6 | 1.4 | -0.2 | 16 |
| 40 | SGSN.SW | 76% | 1.9 | 4.2 | 10.8 | 2.4 | -0.9 | 0 |

(432 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [low_volume_pullback_rebound__broad__max-income__v002.md](symbols/broad/low_volume_pullback_rebound__broad__max-income__v002.md) | 2.0 | 1.6 | 1.6 | -9.7 | 34.0 | 48114/27706 |
| broad | balanced | [low_volume_pullback_rebound__broad__balanced__v001.md](symbols/broad/low_volume_pullback_rebound__broad__balanced__v001.md) | 0.3 | 0.1 | 0.1 | -0.7 | 49.5 | 11661/2946 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 48,213 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
