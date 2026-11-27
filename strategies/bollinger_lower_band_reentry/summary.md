# bollinger_lower_band_reentry: optimization summary

Updated 2026-11-25T18:45:58Z · backtest.py version `dafc0e1042` · 20,814 parameter sets tested with this version (20,814 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [bollinger_lower_band_reentry__max-income__v001.md](bollinger_lower_band_reentry__max-income__v001.md) | 20814 | `{"k": 2.5, "max_bars": 8, "stop_atr": 2.5, "take_profit_atr": 2.5}` | long SPY since 2026-11-24 00:00 @ 715.362555 |
| balanced | [bollinger_lower_band_reentry__balanced__v001.md](bollinger_lower_band_reentry__balanced__v001.md) | 20814 | `{"k": 2.5, "max_bars": 8, "stop_atr": 2.5, "take_profit_atr": 2.5}` | long SPY since 2026-11-24 00:00 @ 715.362555 |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,062.13 | 138.70 | 1,062.13 | 138.70 |
| return % | 10.62 | 1.39 | 10.62 | 1.39 |
| return %/year | 0.5 | 0.1 | 0.5 | 0.1 |
| gross profit | 4,719.68 | 2,123.12 | 4,719.68 | 2,123.12 |
| gross loss | 3,657.55 | 1,984.42 | 3,657.55 | 1,984.42 |
| trades | 35 | 18 | 35 | 18 |
| win rate % | 62.9 | 61.1 | 62.9 | 61.1 |
| avg win | 214.53 | 193.01 | 214.53 | 193.01 |
| avg loss | -281.35 | -283.49 | -281.35 | -283.49 |
| avg result / trade | 30.35 | 7.71 | 30.35 | 7.71 |
| largest single loss | -1,096.04 | -423.16 | -1,096.04 | -423.16 |
| largest loss % of equity | -9.53 | -4.19 | -9.53 | -4.19 |
| max drawdown | -1,866.72 | -786.66 | -1,866.72 | -786.66 |
| max drawdown % | -16.13 | -7.26 | -16.13 | -7.26 |
| profit factor | 1.29 | 1.07 | 1.29 | 1.07 |
| unusually bad trades | 3 | 0 | 3 | 0 |
| … threshold (% of equity) | 3.5 | 6.0 | 3.5 | 6.0 |
| time in market % | 3.9 | 3.1 | 3.9 | 3.1 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |  | 0.27 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.0 | 0.0 |
| 1996 | 0.1 | 0.1 |
| 1997 | 0.2 | 0.2 |
| 1998 | 0.0 | 0.0 |
| 1999 | 3.0 | 3.0 |
| 2000 | 3.9 | 3.9 |
| 2001 | 1.3 | 1.3 |
| 2002 | 0.0 | 0.0 |
| 2003 | 2.6 | 2.6 |
| 2004 | -2.4 | -2.4 |
| 2005 | 0.0 | 0.0 |
| 2006 | 3.7 | 3.7 |
| 2007 | -0.4 | -0.4 |
| 2008 | -7.6 | -7.6 |
| 2009 | 0.0 | 0.0 |
| 2010 | -2.7 | -2.7 |
| 2011 | -3.9 | -3.9 |
| 2012 | 0.0 | 0.0 |
| 2013 | 3.0 | 3.0 |
| 2014 | 7.2 | 7.2 |
| 2015 | 3.0 | 3.0 |
| 2016 (OOS) | -0.7 | -0.7 |
| 2017 (OOS) | 1.6 | 1.6 |
| 2018 (OOS) | -4.2 | -4.2 |
| 2019 (OOS) | 1.5 | 1.5 |
| 2020 (OOS) | 4.4 | 4.4 |
| 2021 (OOS) | -0.9 | -0.9 |
| 2022 (OOS) | 4.5 | 4.5 |
| 2023 (OOS) | -1.3 | -1.3 |
| 2024 (OOS) | 3.4 | 3.4 |
| 2025 (OOS) | -3.2 | -3.2 |
| 2026 (OOS) | -3.3 | -3.3 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 16.1% from a peak in-sample and 7.3% out-of-sample, and the worst single trade cost 4.2% of the account out-of-sample. About 63 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 62% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 16.1% from a peak in-sample and 7.3% out-of-sample, and the worst single trade cost 4.2% of the account out-of-sample. About 63 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 62% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 12184 | `{"k": 2.5, "max_bars": 8, "stop_atr": 2.5, "take_profit_atr": 2.5}` | 1,062.13 | 0.5 | -16.1 | 62.9 | 138.70 | 0.1 | -7.3 | 0.27 | 35/18 | 1.00 |
| 3173 | `{"k": 2.5, "max_bars": 20, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 695.90 | 0.3 | -15.7 | 65.7 | 85.05 | 0.1 | -8.1 | 0.25 | 35/18 | not checked |
| 4839 | `{"k": 2.5, "max_bars": 22, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 695.90 | 0.3 | -15.7 | 65.7 | 85.05 | 0.1 | -8.1 | 0.25 | 35/18 | not checked |
| 12876 | `{"k": 2.5, "max_bars": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 695.90 | 0.3 | -15.7 | 65.7 | 85.05 | 0.1 | -8.1 | 0.25 | 35/18 | not checked |
| 18528 | `{"k": 2.5, "max_bars": 18, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 695.90 | 0.3 | -15.7 | 65.7 | 85.05 | 0.1 | -8.1 | 0.25 | 35/18 | not checked |
| 19705 | `{"k": 2.5, "max_bars": 14, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 695.90 | 0.3 | -15.7 | 65.7 | 85.05 | 0.1 | -8.1 | 0.25 | 35/18 | not checked |
| 19723 | `{"k": 2.5, "max_bars": 24, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 695.90 | 0.3 | -15.7 | 65.7 | 85.05 | 0.1 | -8.1 | 0.25 | 35/18 | not checked |
| 12182 | `{"k": 2.5, "max_bars": 6, "stop_atr": 2.5, "take_profit_atr": 2.5}` | 331.11 | 0.2 | -14.9 | 57.1 | 50.01 | 0.1 | -6.9 | 0.31 | 35/18 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

54 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | CSSPX.SW | 58% | 2.5 | 5.6 | 13.0 | 3.1 | -0.4 | 0 |
| 2 | IWDA.AS | 55% | 3.2 | 6.2 | 12.6 | 3.9 | -0.5 | 17 |
| 3 | TQQQ | 48% | 7.7 | 17.6 | 52.0 | 11.2 | -1.9 | 2 |
| 4 | XLB | 47% | -0.2 | 2.7 | 5.4 | 1.9 | 4.5 | 29 |
| 5 | SMH | 47% | -0.2 | 7.9 | 0.1 | 0.5 | 1.9 | 19 |
| 6 | SOXX | 45% | -0.0 | 5.0 | 2.1 | 1.5 | -1.4 | 10 |
| 7 | VXUS | 44% | 0.7 | 4.7 | 0.6 | 0.8 | 1.1 | 26 |
| 8 | VOO | 39% | 0.6 | 5.2 | 11.9 | -1.1 | 0.3 | 12 |
| 9 | USO | 37% | -0.8 | 4.8 | -16.2 | -2.7 | -1.0 | 14 |
| 10 | DBC | 32% | 0.2 | 2.5 | -6.1 | 0.7 | 0.7 | 15 |
| 11 | RSP | 31% | -0.3 | 2.9 | 9.2 | -0.4 | 0.6 | 17 |
| 12 | VNQ | 27% | -0.8 | 3.8 | 8.7 | 0.3 | 1.6 | 12 |
| 13 | BND | 26% | 0.0 | 0.3 | 4.2 | 0.3 | -0.9 | 0 |
| 14 | LQD | 26% | -0.1 | 0.6 | 5.4 | 0.0 | -0.5 | 0 |
| 15 | IEF | 26% | -0.1 | 0.6 | 5.2 | -0.2 | -1.3 | 0 |
| 16 | GLD | 24% | -0.4 | 2.4 | 8.5 | 0.2 | 0.8 | 14 |
| 17 | GDX | 24% | -1.3 | 4.1 | -10.1 | 1.3 | 6.0 | 15 |
| 18 | VT | 23% | 0.2 | 4.6 | 10.8 | -4.2 | 1.2 | 9 |
| 19 | VWO | 23% | -0.2 | 2.1 | 4.9 | -1.7 | -0.1 | 10 |
| 20 | ACWI | 18% | -0.4 | 2.2 | 5.9 | -3.2 | 1.0 | 9 |
| 21 | DIA | 18% | -0.5 | 0.9 | 6.0 | -0.5 | -0.9 | 2 |
| 22 | VEA | 16% | -1.0 | 2.6 | 0.4 | -2.1 | 1.6 | 10 |
| 23 | CSNDX.SW | 15% | 1.8 | 5.1 | 19.8 | -100.0 | 0.9 | 2 |
| 24 | CSPX.L | 13% | 0.1 | 1.4 | 11.4 | -0.9 | -0.8 | 0 |
| 25 | TLT | 13% | -0.1 | 0.6 | 6.7 | 0.0 | -0.5 | 1 |
| 26 | EFA | 13% | -1.1 | 1.4 | 6.0 | -2.1 | 1.9 | 8 |
| 27 | EEM | 10% | -0.7 | 0.5 | 7.8 | -3.2 | -1.4 | 1 |
| 28 | XLF | 10% | -0.8 | 1.9 | 1.7 | -2.4 | 0.7 | 6 |
| 29 | SCHD | 8% | 0.7 | 1.1 | 12.8 | 0.1 | 0.9 | 5 |
| 30 | SPY | 6% | -0.8 | 0.5 | 9.3 | -1.6 | -0.1 | 1 |
| 31 | VTI | 6% | -1.2 | 0.4 | 7.0 | -1.8 | 0.8 | 4 |
| 32 | VTV | 6% | -1.3 | 1.8 | 7.5 | -2.4 | -0.2 | 3 |
| 33 | XLU | 5% | -1.1 | 0.3 | 5.9 | -1.2 | 2.1 | 3 |
| 34 | CSSMI.SW | 5% | -1.5 | 0.5 | 4.1 | -1.3 | -0.8 | 2 |
| 35 | XLE | 5% | -1.6 | 0.2 | 6.3 | -5.5 | 4.0 | 3 |
| 36 | SQQQ | 3% | 0.1 | 3.0 | -50.7 | -5.8 | -9.2 | 0 |
| 37 | AGG | 3% | -0.1 | 0.1 | 4.0 | -0.1 | -0.8 | 0 |
| 38 | IVV | 3% | -0.9 | 0.3 | 4.3 | -1.8 | 0.4 | 0 |
| 39 | QQQ | 3% | -1.4 | 0.1 | 4.5 | -2.5 | -1.7 | 0 |
| 40 | USMV | 2% | 1.4 | 0.7 | 13.8 | 3.6 | 0.3 | 0 |

(14 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [bollinger_lower_band_reentry__broad__max-income__v002.md](symbols/broad/bollinger_lower_band_reentry__broad__max-income__v002.md) | 0.1 | 0.1 | 0.1 | -1.5 | 81.7 | 71/82 |
| broad | balanced | [bollinger_lower_band_reentry__broad__balanced__v002.md](symbols/broad/bollinger_lower_band_reentry__broad__balanced__v002.md) | 0.1 | 0.1 | 0.1 | -1.3 | 81.6 | 49/64 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 20,814 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
