# percent_b_money_flow: optimization summary

Updated 2026-11-25T09:40:45Z · backtest.py version `87997ef64b` · 1,296 parameter sets tested with this version (1,296 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [percent_b_money_flow__max-income__v002.md](percent_b_money_flow__max-income__v002.md) | 1295 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 3.0, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [percent_b_money_flow__balanced__v002.md](percent_b_money_flow__balanced__v002.md) | 1296 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 3.0, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 5,747.28 | 4,788.66 | 5,389.49 | 5,481.86 |
| return % | 57.47 | 47.89 | 53.89 | 54.82 |
| return %/year | 2.8 | 3.7 | 2.7 | 4.1 |
| gross profit | 29,328.22 | 16,140.99 | 28,710.97 | 16,079.08 |
| gross loss | 23,580.94 | 11,352.33 | 23,321.48 | 10,597.23 |
| trades | 181 | 134 | 177 | 125 |
| win rate % | 53.0 | 60.5 | 54.2 | 61.6 |
| avg win | 305.50 | 199.27 | 299.07 | 208.82 |
| avg loss | -277.42 | -214.19 | -287.92 | -220.78 |
| avg result / trade | 31.75 | 35.74 | 30.45 | 43.85 |
| largest single loss | -868.45 | -768.80 | -925.92 | -831.85 |
| largest loss % of equity | -7.87 | -5.70 | -8.47 | -5.70 |
| max drawdown | -2,307.42 | -1,946.14 | -2,199.96 | -1,665.07 |
| max drawdown % | -19.04 | -13.96 | -19.04 | -11.15 |
| profit factor | 1.24 | 1.42 | 1.23 | 1.52 |
| unusually bad trades | 14 | 6 | 11 | 8 |
| … threshold (% of equity) | 3.4 | 3.1 | 3.9 | 2.8 |
| time in market % | 20.4 | 24.0 | 19.7 | 23.1 |
| buy & hold return % | 117.30 | 541.70 | 117.30 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.30 |  | 1.54 |
| period | 1999-08-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1999-08-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1999 | 12.4 | 12.4 |
| 2000 | -5.2 | -8.5 |
| 2001 | 1.0 | 1.0 |
| 2002 | 14.1 | 16.1 |
| 2003 | -0.2 | -2.1 |
| 2004 | 3.5 | 6.7 |
| 2005 | -0.4 | -0.4 |
| 2006 | 2.6 | 4.7 |
| 2007 | 3.5 | -1.5 |
| 2008 | 6.8 | 8.8 |
| 2009 | 7.5 | -0.1 |
| 2010 | 8.6 | 11.9 |
| 2011 | -1.7 | 0.7 |
| 2012 | -0.4 | -0.2 |
| 2013 | 2.1 | 7.7 |
| 2014 | -2.1 | -6.0 |
| 2015 | -3.8 | -3.8 |
| 2016 (OOS) | -5.9 | -1.2 |
| 2017 (OOS) | 5.8 | 5.8 |
| 2018 (OOS) | -9.3 | -8.7 |
| 2019 (OOS) | 17.6 | 16.0 |
| 2020 (OOS) | 22.0 | 21.4 |
| 2021 (OOS) | 1.9 | 2.9 |
| 2022 (OOS) | -10.7 | -4.9 |
| 2023 (OOS) | 9.6 | 10.7 |
| 2024 (OOS) | 5.2 | 1.8 |
| 2025 (OOS) | 5.1 | -1.4 |
| 2026 (OOS) | 1.2 | 3.6 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 19.0% from a peak in-sample and 14.0% out-of-sample, and the worst single trade cost 5.7% of the account out-of-sample. About 53 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 19.0% from a peak in-sample and 11.2% out-of-sample, and the worst single trade cost 5.7% of the account out-of-sample. About 54 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 770 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 5,747.28 | 2.8 | -19.0 | 53.0 | 4,788.66 | 3.7 | -14.0 | 1.30 | 181/134 | 1.00 |
| 786 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 5,747.28 | 2.8 | -19.0 | 53.0 | 4,899.90 | 3.7 | -13.5 | 1.33 | 181/134 | not checked |
| 787 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 3.25, "take_profit_atr": 2.0}` | 5,747.28 | 2.8 | -19.0 | 53.0 | 4,743.16 | 3.6 | -14.0 | 1.29 | 181/134 | not checked |
| 846 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 5,747.28 | 2.8 | -19.0 | 53.0 | 4,684.49 | 3.6 | -14.0 | 1.28 | 181/134 | not checked |
| 909 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 5,747.28 | 2.8 | -19.0 | 53.0 | 4,871.90 | 3.7 | -14.0 | 1.32 | 181/134 | not checked |
| 1000 | `{"b": 0.7, "max_candles": 6, "mfi": 58, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 5,747.28 | 2.8 | -19.0 | 53.0 | 4,844.74 | 3.7 | -14.0 | 1.32 | 181/134 | not checked |
| 774 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 5,091.01 | 2.5 | -18.4 | 56.7 | 5,940.92 | 4.4 | -11.5 | 1.72 | 178/126 | not checked |
| 890 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 5,091.01 | 2.5 | -18.4 | 56.7 | 5,756.24 | 4.3 | -11.5 | 1.68 | 178/126 | not checked |
| 1012 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 5,091.01 | 2.5 | -18.4 | 56.7 | 5,881.31 | 4.3 | -11.5 | 1.71 | 178/126 | not checked |
| 1079 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 5,091.01 | 2.5 | -18.4 | 56.7 | 5,998.53 | 4.4 | -11.5 | 1.74 | 178/126 | not checked |
| 1201 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 5,091.01 | 2.5 | -18.4 | 56.7 | 6,275.21 | 4.6 | -11.5 | 1.80 | 178/126 | not checked |
| 1206 | `{"b": 0.7, "max_candles": 6, "mfi": 60, "stop_atr": 3.5, "take_profit_atr": 1.5}` | 5,091.01 | 2.5 | -18.4 | 56.7 | 5,807.54 | 4.3 | -11.5 | 1.69 | 178/126 | not checked |
| 902 | `{"b": 0.7, "max_candles": 13, "mfi": 60, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 3,805.49 | 2.0 | -17.2 | 51.8 | 5,000.63 | 3.8 | -12.3 | 1.92 | 164/115 | not checked |
| 970 | `{"b": 0.7, "max_candles": 13, "mfi": 60, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 3,805.49 | 2.0 | -17.2 | 51.8 | 5,231.30 | 3.9 | -12.3 | 1.99 | 164/115 | not checked |
| 971 | `{"b": 0.7, "max_candles": 13, "mfi": 60, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 3,805.49 | 2.0 | -17.2 | 51.8 | 5,176.46 | 3.9 | -12.3 | 1.98 | 164/115 | not checked |
| 1129 | `{"b": 0.7, "max_candles": 13, "mfi": 60, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 3,805.49 | 2.0 | -17.2 | 51.8 | 5,119.70 | 3.9 | -12.3 | 1.96 | 164/115 | not checked |
| 1211 | `{"b": 0.7, "max_candles": 13, "mfi": 60, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 3,805.49 | 2.0 | -17.2 | 51.8 | 5,494.71 | 4.1 | -12.3 | 2.07 | 164/115 | not checked |
| 858 | `{"b": 0.7, "max_candles": 13, "mfi": 58, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 3,139.47 | 1.7 | -17.0 | 50.6 | 3,587.31 | 2.9 | -11.5 | 1.70 | 166/121 | not checked |
| 923 | `{"b": 0.7, "max_candles": 13, "mfi": 58, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 3,139.47 | 1.7 | -17.0 | 50.6 | 3,724.20 | 3.0 | -11.5 | 1.76 | 166/121 | not checked |
| 938 | `{"b": 0.7, "max_candles": 13, "mfi": 58, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 3,139.47 | 1.7 | -17.0 | 50.6 | 3,878.50 | 3.1 | -11.5 | 1.82 | 166/121 | not checked |
| 987 | `{"b": 0.7, "max_candles": 13, "mfi": 58, "stop_atr": 3.5, "take_profit_atr": 1.5}` | 3,139.47 | 1.7 | -17.0 | 50.6 | 3,728.69 | 3.0 | -11.5 | 1.76 | 166/121 | not checked |
| 1180 | `{"b": 0.7, "max_candles": 13, "mfi": 58, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 3,139.47 | 1.7 | -17.0 | 50.6 | 3,783.54 | 3.0 | -11.5 | 1.78 | 166/121 | not checked |
| 166 | `{"b": 0.8, "max_candles": 30, "mfi": 88, "stop_atr": 2.5, "take_profit_atr": 1.5}` | 2,017.07 | 1.1 | -15.6 | 61.5 | 786.98 | 0.7 | -8.4 | 0.62 | 39/26 | 1.00 |
| 183 | `{"b": 0.8, "max_candles": 24, "mfi": 88, "stop_atr": 2.5, "take_profit_atr": 1.5}` | 2,017.07 | 1.1 | -15.6 | 61.5 | 786.98 | 0.7 | -8.4 | 0.62 | 39/26 | not checked |
| 184 | `{"b": 0.8, "max_candles": 36, "mfi": 88, "stop_atr": 2.5, "take_profit_atr": 1.5}` | 2,017.07 | 1.1 | -15.6 | 61.5 | 786.98 | 0.7 | -8.4 | 0.62 | 39/26 | not checked |

(16 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

49 of 56 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 72% | 0.9 | 5.6 | 4.8 | 0.8 | 0.2 | 5 |
| 2 | SPY | 65% | 0.5 | 2.2 | 9.3 | 2.1 | 1.3 | 29 |
| 3 | RSP | 63% | 0.5 | 3.7 | 9.4 | 2.5 | 1.3 | 23 |
| 4 | TQQQ | 60% | 4.9 | 19.0 | 58.3 | 14.9 | 7.6 | 33 |
| 5 | GLD | 57% | 0.6 | 5.7 | 8.5 | 1.2 | 2.2 | 23 |
| 6 | VNQ | 57% | 0.5 | 6.0 | 8.5 | 0.8 | -0.1 | 20 |
| 7 | IEF | 55% | 0.4 | 1.8 | 5.2 | 1.0 | -0.8 | 0 |
| 8 | VWO | 49% | 0.6 | 5.0 | 4.5 | 4.2 | -2.5 | 1 |
| 9 | EEM | 48% | 0.4 | 3.9 | 7.9 | 1.9 | -2.8 | 2 |
| 10 | VTV | 48% | 0.1 | 2.2 | 7.2 | 0.3 | 2.6 | 23 |
| 11 | SLV | 45% | 0.2 | 7.0 | 2.0 | -0.5 | 0.4 | 12 |
| 12 | DBC | 43% | 0.5 | 4.0 | -5.7 | 3.2 | 3.0 | 13 |
| 13 | AGG | 43% | 0.3 | 1.3 | 4.0 | 0.5 | -0.7 | 6 |
| 14 | IVV | 37% | -0.3 | 2.2 | 4.6 | 0.2 | 1.8 | 12 |
| 15 | XLK | 37% | -0.5 | 1.9 | 1.8 | -0.1 | 0.7 | 18 |
| 16 | VTI | 37% | -0.6 | 1.9 | 7.3 | 1.4 | 1.3 | 11 |
| 17 | DIA | 35% | -0.2 | 1.1 | 6.2 | -0.1 | 0.5 | 17 |
| 18 | IWM | 35% | -0.4 | 1.8 | 7.5 | 1.2 | -0.9 | 15 |
| 19 | XLV | 35% | -0.5 | 1.5 | 7.1 | -0.5 | 1.8 | 23 |
| 20 | LQD | 34% | -0.3 | 1.7 | 5.4 | -0.4 | 0.1 | 9 |
| 21 | VEA | 32% | -0.2 | 3.6 | -0.3 | -1.2 | -1.5 | 9 |
| 22 | VUG | 32% | -0.7 | 1.7 | 8.1 | 0.3 | 0.3 | 15 |
| 23 | VOO | 31% | 0.3 | 4.3 | 11.9 | 2.0 | 1.2 | 18 |
| 24 | VT | 29% | -0.4 | 1.8 | 11.4 | -1.0 | -0.2 | 10 |
| 25 | EFA | 29% | -0.4 | 2.1 | 5.8 | 0.9 | -1.4 | 8 |
| 26 | TLT | 29% | -0.6 | 3.5 | 6.7 | -0.1 | -1.2 | 1 |
| 27 | USMV | 28% | 0.6 | 2.8 | 13.5 | 1.3 | 1.5 | 17 |
| 28 | SCHD | 26% | 0.3 | 3.1 | 12.3 | 2.6 | 0.7 | 15 |
| 29 | BND | 26% | -0.2 | 1.0 | 4.3 | -0.0 | -0.7 | 6 |
| 30 | ACWI | 26% | -0.3 | 2.4 | 4.7 | 1.4 | 0.5 | 4 |
| 31 | QQQ | 25% | -0.9 | 2.8 | 4.8 | -1.3 | 0.9 | 12 |
| 32 | XLB | 18% | -1.3 | 2.1 | 5.4 | 0.9 | -1.1 | 3 |
| 33 | XLI | 17% | -0.9 | 0.9 | 5.6 | -0.8 | 3.6 | 11 |
| 34 | VXUS | 15% | -0.4 | 3.4 | 1.2 | -0.7 | -1.1 | 6 |
| 35 | SOXX | 14% | -1.9 | 1.9 | 2.2 | -3.1 | 1.7 | 7 |
| 36 | VIG | 12% | -1.2 | 1.4 | 7.0 | 0.2 | 0.3 | 4 |
| 37 | TIP | 6% | -0.7 | 0.3 | 4.2 | -0.4 | -0.6 | 0 |
| 38 | XLY | 6% | -1.2 | 0.8 | 7.4 | -1.6 | 2.2 | 4 |
| 39 | XLE | 5% | -1.5 | 0.9 | 6.7 | -0.9 | 0.1 | 0 |
| 40 | XLF | 5% | -1.8 | 0.3 | 1.5 | -1.5 | 0.5 | 1 |

(9 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [percent_b_money_flow__broad__max-income__v002.md](symbols/broad/percent_b_money_flow__broad__max-income__v002.md) | 0.5 | 1.5 | 0.5 | -8.4 | 41.4 | 2388/2072 |
| broad | balanced | [percent_b_money_flow__broad__balanced__v002.md](symbols/broad/percent_b_money_flow__broad__balanced__v002.md) | 0.3 | 0.1 | 0.1 | -5.1 | 45.4 | 933/786 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,296 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
