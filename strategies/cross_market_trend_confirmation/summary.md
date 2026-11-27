# cross_market_trend_confirmation: optimization summary

Updated 2026-11-25T14:02:48Z · backtest.py version `0d3481600b` · 54,031 parameter sets tested with this version (54,031 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cross_market_trend_confirmation__max-income__v001.md](cross_market_trend_confirmation__max-income__v001.md) | 43720 | `{"max_bars": 66, "n": 50, "stop_atr": 0.5, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 3,900.62 | 1,337.86 |
| return % | 39.01 | 13.38 |
| return %/year | 2.1 | 1.2 |
| gross profit | 8,064.49 | 4,568.40 |
| gross loss | 4,163.87 | 3,230.54 |
| trades | 48 | 39 |
| win rate % | 22.9 | 20.5 |
| avg win | 733.14 | 571.05 |
| avg loss | -112.54 | -104.21 |
| avg result / trade | 81.26 | 34.30 |
| largest single loss | -210.22 | -181.50 |
| largest loss % of equity | -2.10 | -1.91 |
| max drawdown | -1,354.93 | -2,223.04 |
| max drawdown % | -9.47 | -19.69 |
| profit factor | 1.94 | 1.41 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 5.1 | 8.9 |
| buy & hold return % | 10.97 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.55 |
| period | 2000-03-20 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2000 | 0.0 |
| 2001 | 0.0 |
| 2002 | -4.9 |
| 2003 | 9.1 |
| 2004 | -1.4 |
| 2005 | 9.0 |
| 2006 | -3.8 |
| 2007 | -2.2 |
| 2008 | 0.0 |
| 2009 | 15.3 |
| 2010 | 5.2 |
| 2011 | -1.2 |
| 2012 | 5.9 |
| 2013 | 9.2 |
| 2014 | 1.6 |
| 2015 | -5.9 |
| 2016 (OOS) | -5.2 |
| 2017 (OOS) | 9.2 |
| 2018 (OOS) | 0.0 |
| 2019 (OOS) | 3.5 |
| 2020 (OOS) | -4.3 |
| 2021 (OOS) | -3.4 |
| 2022 (OOS) | -7.3 |
| 2023 (OOS) | 18.0 |
| 2024 (OOS) | 0.0 |
| 2025 (OOS) | -1.4 |
| 2026 (OOS) | 6.1 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 9.5% from a peak in-sample and 19.7% out-of-sample, and the worst single trade cost 1.9% of the account out-of-sample. About 23 of every 100 trades won in-sample. Out-of-sample it earned 1.2% a year against 2.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 51% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 43726 | `{"max_bars": 90, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43764 | `{"max_bars": 66, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43766 | `{"max_bars": 78, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43793 | `{"max_bars": 84, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43837 | `{"max_bars": 96, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43857 | `{"max_bars": 72, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43893 | `{"max_bars": 60, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43895 | `{"max_bars": 54, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43928 | `{"max_bars": 48, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 44103 | `{"max_bars": 42, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 44133 | `{"max_bars": 36, "n": 52, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 4,055.80 | 2.2 | -9.5 | 21.7 | 996.36 | 0.9 | -20.8 | 0.40 | 46/42 | not checked |
| 43737 | `{"max_bars": 90, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 43773 | `{"max_bars": 66, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 43778 | `{"max_bars": 84, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 43826 | `{"max_bars": 78, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 43851 | `{"max_bars": 96, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 43869 | `{"max_bars": 72, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 43998 | `{"max_bars": 54, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 44079 | `{"max_bars": 60, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 44126 | `{"max_bars": 42, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 44176 | `{"max_bars": 48, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 47212 | `{"max_bars": 36, "n": 56, "stop_atr": 0.5, "take_profit_atr": 4.5}` | 3,349.21 | 1.9 | -9.1 | 19.6 | 890.20 | 0.8 | -20.8 | 0.43 | 46/43 | not checked |
| 36459 | `{"max_bars": 60, "n": 26, "stop_atr": 0.25, "take_profit_atr": 4.5}` | 1,560.46 | 0.9 | -8.7 | 16.2 | 264.05 | 0.2 | -9.6 | 0.26 | 74/64 | not checked |
| 37399 | `{"max_bars": 90, "n": 26, "stop_atr": 0.25, "take_profit_atr": 4.5}` | 1,560.46 | 0.9 | -8.7 | 16.2 | 264.05 | 0.2 | -9.6 | 0.26 | 74/64 | not checked |
| 38842 | `{"max_bars": 42, "n": 26, "stop_atr": 0.25, "take_profit_atr": 4.5}` | 1,560.46 | 0.9 | -8.7 | 16.2 | 264.05 | 0.2 | -9.6 | 0.26 | 74/64 | not checked |

(8 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLB | 98% | 2.4 | 4.4 | 5.8 | 2.8 | -0.5 | 23 |
| 2 | VTI | 87% | 1.2 | 2.8 | 8.6 | 0.6 | 0.9 | 41 |
| 3 | RSP | 85% | 1.3 | 4.3 | 9.0 | 0.6 | 2.4 | 46 |
| 4 | IWM | 84% | 1.4 | 3.8 | 7.0 | 0.1 | -0.5 | 20 |
| 5 | VT | 82% | 1.4 | 4.8 | 10.9 | 0.7 | 1.7 | 34 |
| 6 | HYG | 81% | 1.3 | 4.3 | 4.9 | 1.5 | -0.7 | 23 |
| 7 | VTV | 81% | 1.1 | 3.8 | 6.6 | 0.6 | 2.8 | 46 |
| 8 | VNQ | 79% | 1.5 | 5.4 | 8.0 | 1.1 | 0.7 | 34 |
| 9 | VEA | 79% | 0.8 | 3.6 | 1.6 | 1.6 | 1.7 | 44 |
| 10 | XLI | 79% | 0.7 | 2.8 | 5.8 | 1.1 | -1.6 | 30 |
| 11 | XLE | 79% | 0.6 | 2.5 | 7.2 | 1.4 | -3.2 | 20 |
| 12 | EFA | 77% | 0.6 | 2.4 | 7.1 | 0.3 | 1.4 | 29 |
| 13 | DIA | 76% | 0.5 | 1.8 | 6.0 | 0.3 | 0.6 | 45 |
| 14 | SPY | 76% | 0.5 | 1.8 | 9.3 | 0.1 | 0.3 | 41 |
| 15 | IVV | 73% | 0.3 | 2.8 | 5.4 | -0.1 | 0.2 | 39 |
| 16 | XLY | 71% | 0.2 | 2.1 | 7.5 | 0.2 | 1.4 | 9 |
| 17 | USMV | 61% | 0.3 | 1.8 | 13.8 | -1.8 | 1.0 | 32 |
| 18 | VUG | 53% | 0.2 | 1.8 | 8.5 | 1.2 | 0.8 | 14 |
| 19 | XLV | 52% | 0.0 | 1.7 | 7.1 | 0.4 | 2.0 | 25 |
| 20 | ACWI | 50% | 0.0 | 2.8 | 12.3 | -0.0 | 1.4 | 25 |
| 21 | VWO | 47% | -0.1 | 4.2 | 2.5 | -1.5 | -2.4 | 17 |
| 22 | QQQ | 45% | -0.1 | 2.1 | 0.7 | -0.9 | 0.7 | 15 |
| 23 | LQD | 44% | -0.2 | 1.1 | 5.3 | -0.9 | -1.5 | 0 |
| 24 | XLK | 39% | -0.2 | 1.3 | -0.3 | -0.4 | -0.3 | 14 |
| 25 | VIG | 39% | -0.5 | 1.7 | 6.0 | -1.2 | 1.6 | 24 |
| 26 | SMH | 29% | -0.3 | 1.9 | 1.7 | -1.9 | 0.7 | 16 |
| 27 | XLU | 27% | -0.2 | 0.9 | 6.7 | -0.2 | 2.4 | 15 |
| 28 | SCHD | 24% | 0.3 | 2.2 | 12.9 | 2.2 | 1.3 | 15 |
| 29 | EEM | 24% | -0.7 | 3.0 | 6.3 | -2.8 | -0.2 | 13 |
| 30 | XLF | 21% | -0.7 | 0.8 | 2.5 | -0.2 | 2.6 | 12 |
| 31 | USO | 16% | -1.6 | 3.1 | -16.2 | -1.6 | 2.9 | 4 |
| 32 | XLP | 11% | -0.6 | 0.8 | 7.6 | -0.7 | 1.2 | 7 |
| 33 | DBC | 10% | -1.2 | 1.3 | -6.0 | -0.6 | 1.5 | 2 |
| 34 | SLV | 10% | -1.9 | 1.3 | 0.1 | -2.8 | -1.3 | 0 |
| 35 | VOO | 6% | -0.4 | 0.8 | 15.3 | -1.7 | 0.5 | 4 |
| 36 | GDX | 6% | -2.6 | 2.8 | -11.0 | -5.2 | -6.1 | 0 |
| 37 | BND | 3% | -0.7 | 0.1 | 4.0 | -1.6 | -0.9 | 0 |
| 38 | TLT | 2% | -1.6 | 0.1 | 7.1 | -3.6 | -3.0 | 0 |
| 39 | TQQQ | 2% | -6.5 | 0.2 | 41.9 | -6.0 | 0.8 | 1 |
| 40 | SOXX | 0% | 0.0 | n/a | 6.5 | 0.0 | 0.0 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [cross_market_trend_confirmation__broad__max-income__v002.md](symbols/broad/cross_market_trend_confirmation__broad__max-income__v002.md) | 0.7 | 1.2 | 0.7 | -6.0 | 25.6 | 2194/2748 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 54,031 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
