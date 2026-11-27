# connors_composite_oversold: optimization summary

Updated 2026-11-25T15:43:15Z · backtest.py version `6203944f74` · 1,004 parameter sets tested with this version (1,004 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: IWM (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [connors_composite_oversold__max-income__v002.md](connors_composite_oversold__max-income__v002.md) | 1003 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 4.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [connors_composite_oversold__balanced__v002.md](connors_composite_oversold__balanced__v002.md) | 1004 | `{"buy": 15, "exit": 80.0, "max_bars": 20, "stop_atr": 2.75, "take_profit_atr": 3.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [connors_composite_oversold__safe-starter__v001.md](connors_composite_oversold__safe-starter__v001.md) | 448 | `{"buy": 10, "exit": 82.5, "max_bars": 6, "stop_atr": 1.5, "take_profit_atr": 2.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 19,686.65 | 7,697.83 | 16,472.93 | 5,238.92 | 3,655.48 | 3,086.67 |
| return % | 196.87 | 76.98 | 164.73 | 52.39 | 36.55 | 30.87 |
| return %/year | 7.8 | 5.4 | 6.9 | 4.0 | 2.2 | 2.5 |
| gross profit | 28,277.89 | 14,082.15 | 25,511.94 | 12,421.49 | 6,814.91 | 4,846.21 |
| gross loss | 8,591.23 | 6,384.32 | 9,039.00 | 7,182.57 | 3,159.43 | 1,759.54 |
| trades | 79 | 55 | 79 | 55 | 34 | 21 |
| win rate % | 79.8 | 69.1 | 79.8 | 67.3 | 70.6 | 61.9 |
| avg win | 448.86 | 370.58 | 404.95 | 335.72 | 283.95 | 372.79 |
| avg loss | -536.95 | -375.55 | -564.94 | -399.03 | -315.94 | -219.94 |
| avg result / trade | 249.20 | 139.96 | 208.52 | 95.25 | 107.51 | 146.98 |
| largest single loss | -1,427.17 | -1,038.58 | -1,033.21 | -764.65 | -364.86 | -354.25 |
| largest loss % of equity | -6.36 | -6.03 | -5.17 | -4.83 | -2.80 | -2.64 |
| max drawdown | -2,319.58 | -1,956.93 | -1,928.35 | -2,081.76 | -710.31 | -1,455.96 |
| max drawdown % | -10.21 | -16.95 | -9.52 | -17.85 | -5.46 | -14.02 |
| profit factor | 3.29 | 2.21 | 2.82 | 1.73 | 2.16 | 2.75 |
| unusually bad trades | 2 | 2 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 5.6 | 5.6 | 7.9 | 6.9 | 5.4 | 4.1 |
| time in market % | 17.2 | 17.7 | 15.9 | 16.3 | 3.5 | 2.8 |
| buy & hold return % | 166.10 | 175.35 | 166.10 | 175.35 | 166.10 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.69 |  | 0.57 |  | 1.16 |
| period | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2001 | 5.0 | 5.0 | 0.0 |
| 2002 | 2.4 | -2.7 | 0.0 |
| 2003 | 12.6 | 12.6 | 6.7 |
| 2004 | 11.9 | 9.1 | -0.4 |
| 2005 | -1.5 | -4.8 | 1.4 |
| 2006 | 14.4 | 14.7 | 5.1 |
| 2007 | 2.3 | 3.5 | -3.4 |
| 2008 | 1.2 | 1.2 | 0.0 |
| 2009 | 22.2 | 22.2 | 4.6 |
| 2010 | 11.0 | 8.9 | 11.5 |
| 2011 | -1.4 | -0.6 | -3.7 |
| 2012 | 6.3 | 7.8 | 5.9 |
| 2013 | 16.5 | 13.0 | 7.6 |
| 2014 | 3.3 | 4.2 | -0.6 |
| 2015 | 10.0 | 10.0 | -2.1 |
| 2016 (OOS) | 1.3 | 1.3 | 2.2 |
| 2017 (OOS) | 7.1 | 7.7 | -1.3 |
| 2018 (OOS) | -2.6 | -0.5 | -1.8 |
| 2019 (OOS) | -1.8 | -4.6 | -2.5 |
| 2020 (OOS) | -0.6 | -4.2 | -3.7 |
| 2021 (OOS) | 16.9 | 7.1 | 23.1 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 10.1 | 10.1 | 4.7 |
| 2024 (OOS) | 21.8 | 18.6 | 8.0 |
| 2025 (OOS) | 10.7 | 12.3 | 1.2 |
| 2026 (OOS) | -1.1 | -2.1 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 10.2% from a peak in-sample and 16.9% out-of-sample, and the worst single trade cost 6.0% of the account out-of-sample. About 80 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 59% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 9.5% from a peak in-sample and 17.9% out-of-sample, and the worst single trade cost 4.8% of the account out-of-sample. About 80 of every 100 trades won in-sample. Out-of-sample it earned 4.0% a year against 6.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 56% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 5.5% from a peak in-sample and 14.0% out-of-sample, and the worst single trade cost 2.6% of the account out-of-sample. About 71 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 71% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 744 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,697.83 | 5.4 | -16.9 | 0.69 | 79/55 | 1.00 |
| 759 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 3.5}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,702.68 | 5.4 | -16.9 | 0.69 | 79/55 | not checked |
| 760 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,697.83 | 5.4 | -16.9 | 0.69 | 79/55 | not checked |
| 762 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,253.25 | 5.1 | -16.9 | 0.66 | 79/54 | not checked |
| 776 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,253.25 | 5.1 | -16.9 | 0.66 | 79/54 | not checked |
| 860 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,253.25 | 5.1 | -16.9 | 0.66 | 79/54 | not checked |
| 885 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,697.83 | 5.4 | -16.9 | 0.69 | 79/55 | not checked |
| 894 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 3.5}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,257.98 | 5.1 | -16.9 | 0.66 | 79/54 | not checked |
| 906 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,697.83 | 5.4 | -16.9 | 0.69 | 79/55 | not checked |
| 949 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,697.83 | 5.4 | -16.9 | 0.69 | 79/55 | not checked |
| 970 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,253.25 | 5.1 | -16.9 | 0.66 | 79/54 | not checked |
| 994 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 19,686.65 | 7.8 | -10.2 | 79.8 | 7,253.25 | 5.1 | -16.9 | 0.66 | 79/54 | not checked |
| 745 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.25, "take_profit_atr": 3.5}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 6,102.22 | 4.5 | -16.1 | 0.62 | 79/55 | not checked |
| 746 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 6,097.81 | 4.5 | -16.1 | 0.62 | 79/55 | not checked |
| 748 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.25, "take_profit_atr": 4.0}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 5,866.56 | 4.3 | -16.1 | 0.60 | 79/55 | not checked |
| 749 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.25, "take_profit_atr": 4.0}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 6,097.81 | 4.5 | -16.1 | 0.62 | 79/55 | 1.00 |
| 782 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.25, "take_profit_atr": 3.5}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 5,870.91 | 4.3 | -16.1 | 0.60 | 79/55 | not checked |
| 819 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 5,866.56 | 4.3 | -16.1 | 0.60 | 79/55 | not checked |
| 919 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 6,097.81 | 4.5 | -16.1 | 0.62 | 79/55 | not checked |
| 938 | `{"buy": 15, "exit": 80.0, "max_bars": 24, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 5,866.56 | 4.3 | -16.1 | 0.60 | 79/55 | not checked |
| 981 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 17,413.91 | 7.2 | -9.8 | 79.8 | 6,097.81 | 4.5 | -16.1 | 0.62 | 79/55 | not checked |
| 656 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.0, "take_profit_atr": 4.0}` | 16,808.42 | 7.0 | -9.5 | 79.8 | 5,582.09 | 4.2 | -18.1 | 0.59 | 79/55 | not checked |
| 709 | `{"buy": 15, "exit": 80.0, "max_bars": 22, "stop_atr": 3.0, "take_profit_atr": 3.5}` | 16,808.42 | 7.0 | -9.5 | 79.8 | 5,586.36 | 4.2 | -18.1 | 0.59 | 79/55 | not checked |
| 710 | `{"buy": 14, "exit": 80.0, "max_bars": 20, "stop_atr": 2.5, "take_profit_atr": 4.0}` | 13,056.37 | 5.9 | -9.0 | 78.5 | 5,263.41 | 4.0 | -13.5 | 0.67 | 65/49 | not checked |
| 711 | `{"buy": 13, "exit": 80.0, "max_bars": 22, "stop_atr": 2.5, "take_profit_atr": 4.0}` | 11,159.38 | 5.3 | -8.8 | 78.2 | 3,946.18 | 3.1 | -15.0 | 0.59 | 55/42 | not checked |

(10 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SPY | 83% | 1.7 | 5.0 | 9.3 | 0.9 | 0.1 | 28 |
| 2 | XLE | 77% | 1.4 | 5.1 | 7.2 | 1.5 | 1.0 | 33 |
| 3 | IVV | 74% | 0.8 | 3.9 | 5.4 | 0.4 | 0.5 | 33 |
| 4 | SOXX | 73% | 1.5 | 5.7 | 6.5 | 1.1 | -0.5 | 33 |
| 5 | VUG | 73% | 1.2 | 6.4 | 8.5 | 1.2 | 1.9 | 41 |
| 6 | XLF | 73% | 1.1 | 5.2 | 2.5 | 1.4 | -0.0 | 18 |
| 7 | XLI | 73% | 0.9 | 3.2 | 5.8 | 1.2 | 1.6 | 40 |
| 8 | VIG | 71% | 1.5 | 5.4 | 6.0 | 1.4 | -0.5 | 13 |
| 9 | VTV | 71% | 1.2 | 4.7 | 6.6 | 1.4 | -0.1 | 14 |
| 10 | IWM | 71% | 1.0 | 7.8 | 7.0 | 1.1 | 3.2 | 46 |
| 11 | RSP | 71% | 1.0 | 5.6 | 9.0 | 0.8 | 0.9 | 32 |
| 12 | VTI | 71% | 0.8 | 4.3 | 8.6 | 0.6 | 1.2 | 39 |
| 13 | TQQQ | 65% | 7.5 | 26.2 | 41.9 | 8.3 | 1.2 | 32 |
| 14 | CSSMI.SW | 65% | 1.2 | 4.7 | 8.4 | 1.4 | -0.4 | 0 |
| 15 | SMH | 62% | 0.9 | 4.4 | 1.7 | 0.5 | 0.7 | 28 |
| 16 | CSPX.L | 61% | 2.0 | 7.2 | 16.9 | 1.2 | -0.3 | 26 |
| 17 | XLY | 61% | 0.4 | 3.6 | 7.5 | 0.6 | -0.9 | 19 |
| 18 | TLT | 59% | 0.2 | 1.7 | 7.1 | 0.9 | 1.2 | 25 |
| 19 | XLV | 56% | 0.3 | 3.6 | 7.1 | -0.2 | -1.5 | 0 |
| 20 | VWO | 50% | 0.2 | 5.8 | 2.5 | -0.2 | -0.4 | 4 |
| 21 | CSNDX.SW | 48% | 1.1 | 6.5 | 16.1 | 1.3 | 0.2 | 10 |
| 22 | EEM | 48% | 0.3 | 3.8 | 6.3 | 0.3 | -1.0 | 9 |
| 23 | VOO | 47% | 1.6 | 6.9 | 15.3 | 1.2 | 0.1 | 17 |
| 24 | XLK | 47% | 0.4 | 2.5 | -0.3 | -0.2 | -0.5 | 17 |
| 25 | QQQ | 47% | 0.4 | 2.1 | 0.7 | 1.6 | 0.0 | 22 |
| 26 | DIA | 44% | -0.0 | 2.7 | 6.0 | 0.1 | 0.6 | 21 |
| 27 | VNQ | 44% | -0.0 | 5.7 | 8.0 | -0.8 | -0.1 | 3 |
| 28 | ACWI | 39% | 0.4 | 5.7 | 12.3 | -0.4 | 0.8 | 15 |
| 29 | GLD | 39% | 0.1 | 2.5 | 7.4 | 0.2 | 0.3 | 25 |
| 30 | TIP | 38% | -0.0 | 0.7 | 3.8 | 0.1 | -0.3 | 3 |
| 31 | IWDA.AS | 36% | 0.6 | 4.9 | 13.8 | 0.8 | -0.7 | 5 |
| 32 | EFA | 36% | -0.0 | 3.9 | 7.1 | -0.5 | 1.9 | 11 |
| 33 | CSSPX.SW | 33% | 0.1 | 5.5 | 12.3 | -0.2 | 0.2 | 19 |
| 34 | XLP | 32% | 0.1 | 1.4 | 7.6 | -0.3 | -0.3 | 2 |
| 35 | VEA | 32% | 0.0 | 3.0 | 1.6 | -0.5 | 0.4 | 11 |
| 36 | VT | 30% | 0.6 | 3.5 | 10.9 | 0.9 | 0.9 | 13 |
| 37 | GDX | 30% | 0.3 | 3.0 | -11.0 | 0.9 | -0.5 | 12 |
| 38 | XLB | 30% | -0.1 | 1.5 | 5.8 | 0.1 | 0.9 | 16 |
| 39 | SLV | 27% | 0.9 | 6.7 | 0.1 | 0.2 | -0.0 | 3 |
| 40 | USMV | 24% | 0.0 | 4.2 | 13.8 | -0.3 | -0.5 | 2 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [connors_composite_oversold__broad__max-income__v002.md](symbols/broad/connors_composite_oversold__broad__max-income__v002.md) | 1.9 | 2.4 | 1.9 | -6.8 | 68.3 | 4373/4506 |
| broad | balanced | [connors_composite_oversold__broad__balanced__v001.md](symbols/broad/connors_composite_oversold__broad__balanced__v001.md) | 1.6 | 1.6 | 1.6 | -5.6 | 68.2 | 3812/3959 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,004 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
