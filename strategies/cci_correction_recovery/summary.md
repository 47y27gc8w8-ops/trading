# cci_correction_recovery: optimization summary

Updated 2026-11-25T17:40:26Z · backtest.py version `c98e2deff1` · 14,310 parameter sets tested with this version (14,310 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: XLF (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cci_correction_recovery__max-income__v001.md](cci_correction_recovery__max-income__v001.md) | 14310 | `{"max_bars": 8, "n": 14, "stop_atr": 1.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [cci_correction_recovery__balanced__v001.md](cci_correction_recovery__balanced__v001.md) | 14310 | `{"max_bars": 8, "n": 14, "stop_atr": 1.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,435.30 | 2,288.83 | 2,435.30 | 2,288.83 |
| return % | 24.35 | 22.89 | 24.35 | 22.89 |
| return %/year | 1.4 | 1.9 | 1.4 | 1.9 |
| gross profit | 10,186.22 | 6,883.51 | 10,186.22 | 6,883.51 |
| gross loss | 7,750.92 | 4,594.69 | 7,750.92 | 4,594.69 |
| trades | 86 | 57 | 86 | 57 |
| win rate % | 60.5 | 52.6 | 60.5 | 52.6 |
| avg win | 195.89 | 229.45 | 195.89 | 229.45 |
| avg loss | -227.97 | -170.17 | -227.97 | -170.17 |
| avg result / trade | 28.32 | 40.15 | 28.32 | 40.15 |
| largest single loss | -435.34 | -433.15 | -435.34 | -433.15 |
| largest loss % of equity | -3.45 | -3.89 | -3.45 | -3.89 |
| max drawdown | -1,058.01 | -746.46 | -1,058.01 | -746.46 |
| max drawdown % | -8.98 | -6.44 | -8.98 | -6.44 |
| profit factor | 1.31 | 1.50 | 1.31 | 1.50 |
| unusually bad trades | 0 | 1 | 0 | 1 |
| … threshold (% of equity) | 3.9 | 3.5 | 3.9 | 3.5 |
| time in market % | 7.6 | 7.2 | 7.6 | 7.2 |
| buy & hold return % | 46.47 | 257.92 | 46.47 | 257.92 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.42 |  | 1.42 |
| period | 1999-10-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-10-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1999 | -7.4 | -7.4 |
| 2000 | 14.7 | 14.7 |
| 2001 | 0.9 | 0.9 |
| 2002 | 1.9 | 1.9 |
| 2003 | 10.8 | 10.8 |
| 2004 | 0.6 | 0.6 |
| 2005 | -3.3 | -3.3 |
| 2006 | 3.7 | 3.7 |
| 2007 | 3.3 | 3.3 |
| 2008 | 0.0 | 0.0 |
| 2009 | 2.2 | 2.2 |
| 2010 | -3.0 | -3.0 |
| 2011 | -1.9 | -1.9 |
| 2012 | 1.0 | 1.0 |
| 2013 | 4.8 | 4.8 |
| 2014 | 3.4 | 3.4 |
| 2015 | -7.3 | -7.3 |
| 2016 (OOS) | 2.6 | 2.6 |
| 2017 (OOS) | 2.4 | 2.4 |
| 2018 (OOS) | 2.1 | 2.1 |
| 2019 (OOS) | 1.1 | 1.1 |
| 2020 (OOS) | -1.4 | -1.4 |
| 2021 (OOS) | 2.9 | 2.9 |
| 2022 (OOS) | 2.0 | 2.0 |
| 2023 (OOS) | 2.8 | 2.8 |
| 2024 (OOS) | 4.0 | 4.0 |
| 2025 (OOS) | 4.3 | 4.3 |
| 2026 (OOS) | -2.0 | -2.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.0% from a peak in-sample and 6.4% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 60 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 9.0% from a peak in-sample and 6.4% out-of-sample, and the worst single trade cost 3.9% of the account out-of-sample. About 60 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 360 | `{"max_bars": 8, "n": 14, "stop_atr": 1.75, "take_profit_atr": 2.0}` | 2,516.25 | 1.4 | -10.2 | 61.5 | 1,968.87 | 1.7 | -8.1 | 1.19 | 83/55 | not checked |
| 365 | `{"max_bars": 8, "n": 14, "stop_atr": 1.5, "take_profit_atr": 2.0}` | 2,435.30 | 1.4 | -9.0 | 60.5 | 2,288.83 | 1.9 | -6.4 | 1.42 | 86/57 | 0.88 |

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SMH | 100% | 2.9 | 5.5 | 2.1 | 2.0 | 1.8 | 24 |
| 2 | VTI | 97% | 0.9 | 2.5 | 7.1 | 0.5 | 1.7 | 31 |
| 3 | SOXX | 95% | 1.6 | 4.1 | 3.7 | 0.1 | -2.0 | 35 |
| 4 | XLB | 95% | 1.1 | 3.0 | 6.1 | 2.7 | 1.7 | 30 |
| 5 | RSP | 94% | 1.1 | 2.3 | 8.2 | 0.9 | 1.6 | 43 |
| 6 | VTV | 92% | 0.6 | 2.6 | 6.8 | 0.4 | 0.5 | 39 |
| 7 | XLU | 68% | 0.4 | 1.9 | 6.2 | -1.4 | -0.7 | 13 |
| 8 | ACWI | 65% | 1.2 | 3.3 | 10.8 | 2.3 | 0.9 | 39 |
| 9 | VT | 65% | 0.9 | 3.4 | 11.9 | 1.2 | 1.4 | 38 |
| 10 | TIP | 61% | 0.1 | 0.5 | 3.8 | 0.1 | 0.1 | 13 |
| 11 | IVV | 56% | 0.2 | 2.2 | 5.3 | -0.3 | 0.0 | 10 |
| 12 | XLI | 50% | 0.0 | 2.8 | 5.7 | -1.0 | 1.5 | 30 |
| 13 | IWM | 47% | -0.2 | 3.5 | 7.8 | -1.8 | -1.3 | 6 |
| 14 | SPY | 45% | -0.0 | 2.0 | 9.3 | -0.6 | -0.2 | 10 |
| 15 | CSSPX.SW | 42% | -0.2 | 2.7 | 11.6 | -1.8 | -0.7 | 3 |
| 16 | VIG | 42% | -0.3 | 2.4 | 6.2 | -0.1 | 1.1 | 18 |
| 17 | USMV | 40% | 0.9 | 2.6 | 13.3 | 0.5 | -0.6 | 4 |
| 18 | VOO | 40% | 0.3 | 3.3 | 13.1 | -1.7 | 0.1 | 0 |
| 19 | CSPX.L | 40% | -0.3 | 3.2 | 12.1 | -3.0 | 1.7 | 10 |
| 20 | XLP | 39% | -0.1 | 1.0 | 7.0 | -1.9 | 1.4 | 9 |
| 21 | TLT | 37% | -0.2 | 1.5 | 6.2 | -0.2 | 1.1 | 16 |
| 22 | EEM | 37% | -0.5 | 2.4 | 6.4 | -1.6 | -2.1 | 12 |
| 23 | VEA | 37% | -0.6 | 3.0 | 0.0 | 1.2 | 0.5 | 16 |
| 24 | HYG | 35% | 0.3 | 1.3 | 5.0 | -0.4 | 0.5 | 5 |
| 25 | XLY | 35% | -0.3 | 2.0 | 7.8 | -0.7 | -0.1 | 13 |
| 26 | IWDA.AS | 35% | -0.4 | 2.5 | 13.5 | -0.5 | 0.8 | 12 |
| 27 | EFA | 35% | -0.5 | 2.8 | 6.0 | 1.3 | -0.2 | 20 |
| 28 | XLK | 34% | -0.5 | 1.6 | 1.2 | -2.1 | 1.2 | 13 |
| 29 | VUG | 34% | -0.7 | 1.8 | 8.3 | -1.1 | 0.7 | 5 |
| 30 | GDX | 32% | -0.3 | 5.9 | -10.5 | 1.5 | 1.9 | 7 |
| 31 | QQQ | 32% | -0.9 | 3.3 | 2.0 | -2.9 | 0.8 | 1 |
| 32 | GLD | 29% | -0.5 | 1.6 | 8.3 | -0.4 | 1.1 | 16 |
| 33 | LQD | 27% | -0.2 | 0.5 | 4.9 | 0.1 | 0.9 | 12 |
| 34 | BND | 24% | -0.6 | 0.7 | 3.8 | 0.1 | 0.3 | 1 |
| 35 | CSSMI.SW | 24% | -1.4 | 1.6 | 7.7 | -1.6 | -0.1 | 3 |
| 36 | VNQ | 23% | -1.4 | 1.9 | 7.6 | -2.2 | 0.4 | 8 |
| 37 | DBC | 19% | 0.1 | 1.7 | -5.8 | -0.7 | 0.3 | 6 |
| 38 | SLV | 18% | -2.0 | 3.3 | -0.7 | -1.8 | 5.8 | 4 |
| 39 | VXUS | 16% | -0.3 | 1.0 | 4.5 | 0.5 | -0.6 | 8 |
| 40 | DIA | 16% | -0.5 | 1.2 | 6.4 | -0.3 | 1.7 | 8 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [cci_correction_recovery__broad__max-income__v002.md](symbols/broad/cci_correction_recovery__broad__max-income__v002.md) | 0.6 | 0.2 | 0.2 | -9.4 | 59.4 | 4260/4239 |
| broad | balanced | [cci_correction_recovery__broad__balanced__v002.md](symbols/broad/cci_correction_recovery__broad__balanced__v002.md) | 0.5 | 0.3 | 0.3 | -11.6 | 57.8 | 3633/3685 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 14,310 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
