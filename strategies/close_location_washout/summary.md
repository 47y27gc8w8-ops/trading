# close_location_washout: optimization summary

Updated 2026-11-25T16:22:15Z · backtest.py version `58d6d19b6c` · 33,814 parameter sets tested with this version (33,814 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: IWM (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [close_location_washout__max-income__v001.md](close_location_washout__max-income__v001.md) | 27352 | `{"clv": 0.05, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [close_location_washout__balanced__v001.md](close_location_washout__balanced__v001.md) | 27352 | `{"clv": 0.05, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,730.56 | 591.93 | 2,730.56 | 591.93 |
| return % | 27.31 | 5.92 | 27.31 | 5.92 |
| return %/year | 1.7 | 0.5 | 1.7 | 0.5 |
| gross profit | 7,460.12 | 3,598.95 | 7,460.12 | 3,598.95 |
| gross loss | 4,729.57 | 3,007.02 | 4,729.57 | 3,007.02 |
| trades | 92 | 41 | 92 | 41 |
| win rate % | 68.5 | 63.4 | 68.5 | 63.4 |
| avg win | 118.41 | 138.42 | 118.41 | 138.42 |
| avg loss | -163.09 | -200.47 | -163.09 | -200.47 |
| avg result / trade | 29.68 | 14.44 | 29.68 | 14.44 |
| largest single loss | -436.21 | -546.28 | -436.21 | -546.28 |
| largest loss % of equity | -3.64 | -5.04 | -3.64 | -5.04 |
| max drawdown | -845.63 | -1,230.68 | -845.63 | -1,230.68 |
| max drawdown % | -7.47 | -10.85 | -7.47 | -10.85 |
| profit factor | 1.58 | 1.20 | 1.58 | 1.20 |
| unusually bad trades | 10 | 5 | 10 | 5 |
| … threshold (% of equity) | 2.0 | 2.1 | 2.0 | 2.1 |
| time in market % | 5.2 | 3.1 | 5.2 | 3.1 |
| buy & hold return % | 166.10 | 175.35 | 166.10 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.32 |  | 0.32 |
| period | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2001 | -0.5 | -0.5 |
| 2002 | 0.2 | 0.2 |
| 2003 | 2.3 | 2.3 |
| 2004 | -2.4 | -2.4 |
| 2005 | -1.0 | -1.0 |
| 2006 | 8.5 | 8.5 |
| 2007 | -1.1 | -1.1 |
| 2008 | 0.0 | 0.0 |
| 2009 | 1.2 | 1.2 |
| 2010 | 6.9 | 6.9 |
| 2011 | 0.9 | 0.9 |
| 2012 | -0.3 | -0.3 |
| 2013 | 4.9 | 4.9 |
| 2014 | 3.3 | 3.3 |
| 2015 | 2.1 | 2.1 |
| 2016 (OOS) | 1.0 | 1.0 |
| 2017 (OOS) | 1.8 | 1.8 |
| 2018 (OOS) | 2.3 | 2.3 |
| 2019 (OOS) | 0.9 | 0.9 |
| 2020 (OOS) | 2.1 | 2.1 |
| 2021 (OOS) | 0.8 | 0.8 |
| 2022 (OOS) | 0.0 | 0.0 |
| 2023 (OOS) | -1.7 | -1.7 |
| 2024 (OOS) | -2.2 | -2.2 |
| 2025 (OOS) | -1.3 | -1.3 |
| 2026 (OOS) | 2.2 | 2.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 7.5% from a peak in-sample and 10.8% out-of-sample, and the worst single trade cost 5.0% of the account out-of-sample. About 68 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 1.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 92% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 7.5% from a peak in-sample and 10.8% out-of-sample, and the worst single trade cost 5.0% of the account out-of-sample. About 68 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 1.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 92% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 113 | `{"clv": 0.05, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | 1.00 |
| 128 | `{"clv": 0.05, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 129 | `{"clv": 0.05, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 130 | `{"clv": 0.05, "max_bars": 20, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 131 | `{"clv": 0.05, "max_bars": 24, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 1027 | `{"clv": 0.05, "max_bars": 24, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 1151 | `{"clv": 0.05, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 1234 | `{"clv": 0.05, "max_bars": 18, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 1791 | `{"clv": 0.05, "max_bars": 10, "stop_atr": 2.0, "take_profit_atr": 4.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 1794 | `{"clv": 0.05, "max_bars": 20, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 2243 | `{"clv": 0.05, "max_bars": 18, "stop_atr": 2.0, "take_profit_atr": 2.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 603.21 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 3177 | `{"clv": 0.05, "max_bars": 20, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 3469 | `{"clv": 0.05, "max_bars": 10, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 3506 | `{"clv": 0.05, "max_bars": 24, "stop_atr": 2.0, "take_profit_atr": 4.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 3508 | `{"clv": 0.05, "max_bars": 24, "stop_atr": 2.0, "take_profit_atr": 4.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 3956 | `{"clv": 0.05, "max_bars": 14, "stop_atr": 2.0, "take_profit_atr": 4.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 4210 | `{"clv": 0.05, "max_bars": 14, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 4826 | `{"clv": 0.05, "max_bars": 18, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 4940 | `{"clv": 0.05, "max_bars": 10, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 6147 | `{"clv": 0.05, "max_bars": 12, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 6171 | `{"clv": 0.05, "max_bars": 14, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 6260 | `{"clv": 0.05, "max_bars": 18, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 6530 | `{"clv": 0.05, "max_bars": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 6750 | `{"clv": 0.05, "max_bars": 20, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |
| 6770 | `{"clv": 0.05, "max_bars": 8, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 2,730.56 | 1.7 | -7.5 | 68.5 | 591.93 | 0.5 | -10.8 | 0.32 | 92/41 | not checked |

(155 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLF | 97% | 2.8 | 4.6 | 2.5 | 3.0 | -0.7 | 10 |
| 2 | VUG | 97% | 1.6 | 2.5 | 8.5 | 1.7 | 3.5 | 57 |
| 3 | SPY | 97% | 1.3 | 2.4 | 9.3 | 0.9 | 1.9 | 53 |
| 4 | XLP | 95% | 1.3 | 2.4 | 7.6 | 1.6 | -0.9 | 3 |
| 5 | XLE | 92% | 2.0 | 3.4 | 7.2 | 0.8 | 1.0 | 6 |
| 6 | VTI | 90% | 1.5 | 3.0 | 8.6 | 1.6 | 2.1 | 46 |
| 7 | XLI | 89% | 1.2 | 3.5 | 5.8 | 1.0 | 1.5 | 54 |
| 8 | VIG | 89% | 1.2 | 2.5 | 6.0 | 1.0 | 1.8 | 50 |
| 9 | VNQ | 87% | 1.8 | 3.9 | 8.0 | 1.9 | -1.5 | 0 |
| 10 | VOO | 87% | 1.6 | 3.5 | 15.3 | 2.5 | 2.2 | 43 |
| 11 | RSP | 87% | 1.5 | 3.4 | 9.0 | 2.6 | 2.5 | 51 |
| 12 | IVV | 82% | 0.6 | 1.9 | 5.4 | 0.7 | 1.9 | 49 |
| 13 | ACWI | 79% | 0.8 | 1.9 | 12.3 | 1.9 | 1.2 | 43 |
| 14 | SCHD | 73% | 1.6 | 3.2 | 12.9 | 2.3 | 1.1 | 13 |
| 15 | GDX | 71% | 1.8 | 6.1 | -11.0 | 1.3 | 2.3 | 32 |
| 16 | VTV | 69% | 0.3 | 1.4 | 6.6 | 0.7 | 1.7 | 41 |
| 17 | XLY | 68% | 0.4 | 1.6 | 7.5 | 1.1 | -0.4 | 12 |
| 18 | USO | 66% | 0.6 | 2.1 | -16.2 | 1.8 | 0.3 | 20 |
| 19 | VT | 66% | 0.4 | 1.4 | 10.9 | 1.4 | 1.6 | 34 |
| 20 | IWM | 63% | 0.3 | 1.7 | 7.0 | 0.1 | 0.2 | 22 |
| 21 | SMH | 61% | 0.3 | 1.4 | 1.7 | 1.4 | 1.0 | 36 |
| 22 | XLV | 55% | 0.7 | 2.7 | 7.1 | 0.8 | -0.1 | 1 |
| 23 | DBC | 53% | 0.2 | 2.0 | -6.0 | -0.2 | -0.1 | 1 |
| 24 | XLB | 50% | 0.0 | 2.0 | 5.8 | 0.4 | 1.9 | 31 |
| 25 | EFA | 45% | -0.0 | 1.4 | 7.1 | 0.9 | 1.0 | 28 |
| 26 | VWO | 42% | 0.5 | 3.4 | 2.5 | 1.6 | 1.2 | 21 |
| 27 | SOXX | 40% | -0.1 | 1.2 | 6.5 | 1.2 | 4.7 | 25 |
| 28 | EEM | 40% | -0.1 | 1.6 | 6.3 | -0.8 | 1.1 | 22 |
| 29 | TLT | 34% | -0.1 | 0.8 | 7.1 | -0.4 | -1.2 | 8 |
| 30 | XLU | 32% | -0.2 | 0.7 | 6.7 | -0.2 | -2.4 | 0 |
| 31 | CSNDX.SW | 24% | -0.6 | 1.4 | 16.1 | 0.8 | 1.3 | 15 |
| 32 | VEA | 23% | -0.2 | 0.4 | 1.6 | 0.4 | 0.9 | 11 |
| 33 | USMV | 16% | -0.4 | 1.0 | 13.8 | -0.9 | 0.8 | 7 |
| 34 | TQQQ | 16% | -2.2 | 6.8 | 41.9 | -0.4 | 15.3 | 10 |
| 35 | DIA | 11% | -0.6 | 0.4 | 6.0 | -0.7 | 0.7 | 6 |
| 36 | CSSMI.SW | 11% | -0.8 | 0.2 | 8.4 | -0.9 | -1.0 | 0 |
| 37 | IEF | 8% | -0.1 | 0.2 | 5.3 | -0.2 | 0.1 | 5 |
| 38 | QQQ | 6% | -1.0 | 0.6 | 0.7 | 0.2 | 2.8 | 4 |
| 39 | IWDA.AS | 3% | -1.8 | 0.0 | 13.8 | -2.6 | -0.5 | 0 |
| 40 | CSPX.L | 2% | -1.0 | 0.3 | 16.9 | -1.7 | 1.6 | 1 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [close_location_washout__broad__max-income__v001.md](symbols/broad/close_location_washout__broad__max-income__v001.md) | 0.4 | 1.4 | 0.4 | -5.5 | 63.3 | 3326/2897 |
| broad | balanced | [close_location_washout__broad__balanced__v001.md](symbols/broad/close_location_washout__broad__balanced__v001.md) | 0.4 | 1.3 | 0.4 | -4.5 | 63.5 | 2926/2525 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 33,814 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
