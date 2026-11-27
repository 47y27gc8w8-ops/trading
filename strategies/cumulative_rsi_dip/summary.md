# cumulative_rsi_dip: optimization summary

Updated 2026-11-25T13:38:05Z · backtest.py version `7a3fd74311` · 857 parameter sets tested with this version (857 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: DIA (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cumulative_rsi_dip__max-income__v001.md](cumulative_rsi_dip__max-income__v001.md) | 357 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 48}` | flat (data up to 2026-11-24 00:00) |
| balanced | [cumulative_rsi_dip__balanced__v001.md](cumulative_rsi_dip__balanced__v001.md) | 357 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 48}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,983.41 | 1,234.73 | 1,983.41 | 1,234.73 |
| return % | 19.83 | 12.35 | 19.83 | 12.35 |
| return %/year | 1.1 | 1.1 | 1.1 | 1.1 |
| gross profit | 5,350.65 | 5,113.67 | 5,350.65 | 5,113.67 |
| gross loss | 3,367.24 | 3,878.94 | 3,367.24 | 3,878.94 |
| trades | 83 | 62 | 83 | 62 |
| win rate % | 66.3 | 67.7 | 66.3 | 67.7 |
| avg win | 97.28 | 121.75 | 97.28 | 121.75 |
| avg loss | -120.26 | -193.95 | -120.26 | -193.95 |
| avg result / trade | 23.90 | 19.92 | 23.90 | 19.92 |
| largest single loss | -488.70 | -533.77 | -488.70 | -533.77 |
| largest loss % of equity | -4.77 | -4.73 | -4.77 | -4.73 |
| max drawdown | -999.26 | -936.21 | -999.26 | -936.21 |
| max drawdown % | -9.69 | -7.80 | -9.69 | -7.80 |
| profit factor | 1.59 | 1.32 | 1.59 | 1.32 |
| unusually bad trades | 6 | 8 | 6 | 8 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 6.9 | 7.5 | 6.9 | 7.5 |
| buy & hold return % | 168.24 | 258.53 | 168.24 | 258.53 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.00 |  | 1.00 |
| period | 1999-02-01 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-02-01 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1999 | -3.6 | -3.6 |
| 2000 | -1.3 | -1.3 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.9 | 0.9 |
| 2003 | 3.2 | 3.2 |
| 2004 | 2.5 | 2.5 |
| 2005 | -1.0 | -1.0 |
| 2006 | 2.1 | 2.1 |
| 2007 | 4.1 | 4.1 |
| 2008 | 0.0 | 0.0 |
| 2009 | 4.1 | 4.1 |
| 2010 | -0.9 | -0.9 |
| 2011 | -1.8 | -1.8 |
| 2012 | 4.5 | 4.5 |
| 2013 | 1.5 | 1.5 |
| 2014 | 0.3 | 0.3 |
| 2015 | 4.1 | 4.1 |
| 2016 (OOS) | 2.7 | 2.7 |
| 2017 (OOS) | -0.2 | -0.2 |
| 2018 (OOS) | 11.5 | 11.5 |
| 2019 (OOS) | -0.8 | -0.8 |
| 2020 (OOS) | 0.0 | 0.0 |
| 2021 (OOS) | -1.1 | -1.1 |
| 2022 (OOS) | -0.1 | -0.1 |
| 2023 (OOS) | 0.0 | 0.0 |
| 2024 (OOS) | 3.8 | 3.8 |
| 2025 (OOS) | 3.1 | 3.1 |
| 2026 (OOS) | -6.2 | -6.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.7% from a peak in-sample and 7.8% out-of-sample, and the worst single trade cost 4.7% of the account out-of-sample. About 66 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 9.7% from a peak in-sample and 7.8% out-of-sample, and the worst single trade cost 4.7% of the account out-of-sample. About 66 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 141 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,234.73 | 1.1 | -7.8 | 1.00 | 83/62 | 0.90 |
| 158 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 3.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,157.47 | 1.0 | -7.8 | 0.94 | 83/62 | not checked |
| 159 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 160 | `{"max_bars": 20, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,234.73 | 1.1 | -7.8 | 1.00 | 83/62 | not checked |
| 161 | `{"max_bars": 24, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,234.73 | 1.1 | -7.8 | 1.00 | 83/62 | not checked |
| 402 | `{"max_bars": 24, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 410 | `{"max_bars": 20, "n": 3, "stop_atr": 3.0, "take_profit_atr": 3.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,157.47 | 1.0 | -7.8 | 0.94 | 83/62 | not checked |
| 422 | `{"max_bars": 20, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 433 | `{"max_bars": 24, "n": 3, "stop_atr": 3.0, "take_profit_atr": 3.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,157.47 | 1.0 | -7.8 | 0.94 | 83/62 | not checked |
| 487 | `{"max_bars": 24, "n": 3, "stop_atr": 3.0, "take_profit_atr": 5.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 493 | `{"max_bars": 18, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 502 | `{"max_bars": 20, "n": 3, "stop_atr": 3.0, "take_profit_atr": 5.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 552 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 5.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 583 | `{"max_bars": 18, "n": 3, "stop_atr": 3.0, "take_profit_atr": 3.5, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,157.47 | 1.0 | -7.8 | 0.94 | 83/62 | not checked |
| 595 | `{"max_bars": 18, "n": 3, "stop_atr": 3.0, "take_profit_atr": 5.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 898.45 | 0.8 | -7.8 | 0.73 | 83/62 | not checked |
| 623 | `{"max_bars": 18, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 48}` | 1,983.41 | 1.1 | -9.7 | 66.3 | 1,234.73 | 1.1 | -7.8 | 1.00 | 83/62 | not checked |
| 362 | `{"max_bars": 22, "n": 3, "stop_atr": 3.5, "take_profit_atr": 4.5, "threshold": 48}` | 1,736.42 | 0.9 | -9.4 | 66.3 | 739.08 | 0.7 | -9.0 | 0.69 | 83/60 | not checked |
| 372 | `{"max_bars": 24, "n": 3, "stop_atr": 3.5, "take_profit_atr": 4.5, "threshold": 48}` | 1,736.42 | 0.9 | -9.4 | 66.3 | 739.08 | 0.7 | -9.0 | 0.69 | 83/60 | not checked |
| 406 | `{"max_bars": 20, "n": 3, "stop_atr": 3.5, "take_profit_atr": 3.5, "threshold": 48}` | 1,736.42 | 0.9 | -9.4 | 66.3 | 994.31 | 0.9 | -9.0 | 0.92 | 83/60 | not checked |
| 417 | `{"max_bars": 20, "n": 3, "stop_atr": 3.5, "take_profit_atr": 4.5, "threshold": 48}` | 1,736.42 | 0.9 | -9.4 | 66.3 | 739.08 | 0.7 | -9.0 | 0.69 | 83/60 | not checked |
| 127 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 46}` | 1,699.31 | 0.9 | -9.3 | 68.0 | 778.83 | 0.7 | -8.0 | 0.74 | 78/57 | 0.90 |
| 143 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 3.5, "threshold": 46}` | 1,699.31 | 0.9 | -9.3 | 68.0 | 778.83 | 0.7 | -8.0 | 0.74 | 78/57 | not checked |
| 144 | `{"max_bars": 22, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.5, "threshold": 46}` | 1,699.31 | 0.9 | -9.3 | 68.0 | 778.83 | 0.7 | -8.0 | 0.74 | 78/57 | not checked |
| 145 | `{"max_bars": 20, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 46}` | 1,699.31 | 0.9 | -9.3 | 68.0 | 778.83 | 0.7 | -8.0 | 0.74 | 78/57 | not checked |
| 146 | `{"max_bars": 24, "n": 3, "stop_atr": 3.0, "take_profit_atr": 4.0, "threshold": 46}` | 1,699.31 | 0.9 | -9.3 | 68.0 | 778.83 | 0.7 | -8.0 | 0.74 | 78/57 | not checked |

(26 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SPY | 60% | 1.0 | 5.1 | 9.3 | 1.9 | -0.5 | 3 |
| 2 | XLE | 58% | 1.3 | 4.5 | 7.2 | 1.6 | 3.9 | 19 |
| 3 | QQQ | 58% | 1.3 | 3.6 | 0.7 | 2.3 | 0.5 | 2 |
| 4 | XLV | 56% | 1.2 | 3.9 | 7.1 | 1.8 | -0.2 | 1 |
| 5 | XLF | 56% | 0.8 | 3.5 | 2.5 | 1.2 | -1.1 | 12 |
| 6 | SOXX | 56% | 0.6 | 3.5 | 6.5 | 0.6 | 1.4 | 31 |
| 7 | VUG | 55% | 1.0 | 4.2 | 8.5 | 1.4 | 0.2 | 16 |
| 8 | IWM | 55% | 0.5 | 4.5 | 7.0 | 0.9 | -0.0 | 15 |
| 9 | IVV | 55% | 0.4 | 2.7 | 5.4 | 1.4 | -0.3 | 16 |
| 10 | XLU | 55% | 0.2 | 0.9 | 6.7 | 0.0 | -2.7 | 3 |
| 11 | TLT | 53% | 0.2 | 1.2 | 7.1 | 0.7 | 0.6 | 30 |
| 12 | VIG | 52% | 0.2 | 3.0 | 6.0 | 1.0 | -0.6 | 13 |
| 13 | XLK | 50% | 0.9 | 3.1 | -0.3 | 1.2 | -1.0 | 6 |
| 14 | VTI | 50% | 0.1 | 2.5 | 8.6 | 0.8 | 0.5 | 17 |
| 15 | XLI | 48% | 0.5 | 3.2 | 5.8 | 0.5 | 0.5 | 25 |
| 16 | VTV | 47% | 0.4 | 2.1 | 6.6 | 1.0 | -0.2 | 20 |
| 17 | XLY | 47% | 0.2 | 4.2 | 7.5 | 0.2 | -0.3 | 18 |
| 18 | EFA | 45% | 0.3 | 1.5 | 7.1 | 0.8 | 0.2 | 21 |
| 19 | RSP | 45% | 0.0 | 1.9 | 9.0 | 1.1 | -0.7 | 12 |
| 20 | TQQQ | 42% | 4.0 | 29.5 | 41.9 | 8.0 | 2.0 | 6 |
| 21 | CSSMI.SW | 42% | 0.7 | 3.1 | 8.4 | 1.2 | -0.8 | 1 |
| 22 | CSSPX.SW | 42% | 0.4 | 2.9 | 12.3 | 0.5 | 0.7 | 13 |
| 23 | XLB | 39% | 0.0 | 1.2 | 5.8 | 0.7 | 0.5 | 17 |
| 24 | SMH | 37% | 0.5 | 2.8 | 1.7 | -0.3 | 1.1 | 23 |
| 25 | VOO | 35% | 1.0 | 4.6 | 15.3 | 3.0 | -0.4 | 8 |
| 26 | CSPX.L | 35% | 0.6 | 4.1 | 16.9 | 1.2 | 0.3 | 18 |
| 27 | CSNDX.SW | 35% | 0.5 | 6.6 | 16.1 | 0.3 | 0.0 | 2 |
| 28 | USO | 32% | 0.1 | 2.8 | -16.2 | -0.6 | -0.9 | 14 |
| 29 | SLV | 31% | 2.1 | 7.0 | 0.1 | 2.2 | -0.2 | 0 |
| 30 | TIP | 31% | -0.0 | 0.4 | 3.8 | 0.0 | -0.1 | 3 |
| 31 | DIA | 31% | -0.1 | 1.1 | 6.0 | -0.1 | -0.6 | 11 |
| 32 | IWDA.AS | 29% | 0.5 | 1.9 | 13.8 | 1.0 | 1.2 | 15 |
| 33 | GLD | 29% | 0.1 | 2.0 | 7.4 | -0.9 | 1.2 | 14 |
| 34 | EEM | 27% | -0.1 | 2.4 | 6.3 | -0.4 | -0.4 | 5 |
| 35 | VT | 26% | 0.0 | 2.4 | 10.9 | 0.7 | 0.2 | 8 |
| 36 | VNQ | 26% | -0.1 | 3.1 | 8.0 | -0.5 | -0.7 | 3 |
| 37 | VWO | 24% | -0.0 | 5.3 | 2.5 | 0.2 | -0.2 | 4 |
| 38 | VEA | 23% | 0.4 | 1.6 | 1.6 | 1.6 | 0.4 | 8 |
| 39 | ACWI | 23% | 0.0 | 1.8 | 12.3 | 1.0 | 0.8 | 5 |
| 40 | USMV | 16% | 0.7 | 3.7 | 13.8 | 0.6 | -0.4 | 5 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [cumulative_rsi_dip__broad__max-income__v001.md](symbols/broad/cumulative_rsi_dip__broad__max-income__v001.md) | 1.2 | 1.1 | 1.1 | -8.7 | 64.6 | 4562/4825 |
| broad | balanced | [cumulative_rsi_dip__broad__balanced__v001.md](symbols/broad/cumulative_rsi_dip__broad__balanced__v001.md) | 0.9 | 0.5 | 0.5 | -6.4 | 64.6 | 3788/3991 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 857 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
