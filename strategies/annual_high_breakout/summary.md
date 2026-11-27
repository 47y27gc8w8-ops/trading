# annual_high_breakout: optimization summary

Updated 2026-11-25T20:10:15Z · backtest.py version `ce9bab0dae` · 50,745 parameter sets tested with this version (50,745 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: MSFT (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [annual_high_breakout__max-income__v001.md](annual_high_breakout__max-income__v001.md) | 50743 | `{"max_bars": 66, "n": 132, "stop_atr": 3.25, "take_profit_atr": 5.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | [annual_high_breakout__balanced__v001.md](annual_high_breakout__balanced__v001.md) | 50744 | `{"max_bars": 72, "n": 132, "stop_atr": 2.25, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [annual_high_breakout__safe-starter__v001.md](annual_high_breakout__safe-starter__v001.md) | 50745 | `{"max_bars": 72, "n": 132, "stop_atr": 2.0, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 16,226.04 | 3,441.95 | 9,812.04 | 2,392.77 | 8,152.58 | 2,448.85 |
| return % | 162.26 | 34.42 | 98.12 | 23.93 | 81.53 | 24.49 |
| return %/year | 4.7 | 2.8 | 3.3 | 2.0 | 2.9 | 2.0 |
| gross profit | 35,598.27 | 10,042.70 | 21,265.41 | 7,761.51 | 20,090.35 | 7,604.80 |
| gross loss | 19,372.23 | 6,600.75 | 11,453.36 | 5,368.75 | 11,937.78 | 5,155.95 |
| trades | 37 | 23 | 41 | 26 | 43 | 27 |
| win rate % | 54.0 | 47.8 | 58.5 | 50.0 | 53.5 | 48.1 |
| avg win | 1,779.91 | 912.97 | 886.06 | 597.04 | 873.49 | 584.98 |
| avg loss | -1,139.54 | -550.06 | -673.73 | -412.98 | -596.89 | -368.28 |
| avg result / trade | 438.54 | 149.65 | 239.32 | 92.03 | 189.59 | 90.70 |
| largest single loss | -2,944.03 | -1,297.97 | -1,406.11 | -810.17 | -1,172.99 | -720.21 |
| largest loss % of equity | -11.11 | -8.81 | -8.53 | -6.14 | -7.47 | -5.47 |
| max drawdown | -13,351.95 | -3,137.50 | -4,150.98 | -1,249.78 | -4,878.31 | -1,175.16 |
| max drawdown % | -48.12 | -22.11 | -24.05 | -10.60 | -28.93 | -11.56 |
| profit factor | 1.84 | 1.52 | 1.86 | 1.45 | 1.68 | 1.48 |
| unusually bad trades | 0 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 11.3 | 9.3 | 9.7 | 7.0 | 8.2 | 6.3 |
| time in market % | 16.4 | 23.7 | 8.4 | 16.4 | 8.2 | 15.3 |
| buy & hold return % | 1,968.97 | 944.05 | 1,968.97 | 944.05 | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.58 |  | 0.60 |  | 0.70 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 24.3 | 8.6 | 9.9 |
| 1996 | 30.7 | 12.0 | 12.5 |
| 1997 | 23.5 | 12.4 | 13.1 |
| 1998 | 32.0 | 20.5 | 20.5 |
| 1999 | -20.5 | -13.0 | -16.8 |
| 2000 | -13.6 | 0.0 | 0.0 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 | 0.0 |
| 2003 | -3.9 | 6.0 | 6.0 |
| 2004 | -6.4 | -5.0 | -4.4 |
| 2005 | -0.4 | -0.4 | -0.4 |
| 2006 | 6.7 | 2.7 | 1.2 |
| 2007 | -15.5 | -8.8 | -14.5 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 25.8 | 15.0 | 15.0 |
| 2010 | 0.0 | 0.0 | 0.0 |
| 2011 | -4.7 | -3.3 | -3.0 |
| 2012 | 8.4 | 10.6 | 10.6 |
| 2013 | 15.2 | 7.0 | 7.0 |
| 2014 | 12.2 | 4.1 | 4.5 |
| 2015 | 6.2 | 7.4 | 7.4 |
| 2016 (OOS) | 1.4 | -3.6 | -3.2 |
| 2017 (OOS) | -0.8 | -3.1 | -6.4 |
| 2018 (OOS) | 4.0 | 2.7 | 3.1 |
| 2019 (OOS) | 11.5 | 5.9 | 6.3 |
| 2020 (OOS) | 1.1 | 12.8 | 12.8 |
| 2021 (OOS) | -9.5 | -3.4 | -2.4 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 22.3 | 9.2 | 9.8 |
| 2024 (OOS) | 6.6 | 3.0 | 3.0 |
| 2025 (OOS) | -5.6 | -3.9 | -3.5 |
| 2026 (OOS) | -3.4 | 3.6 | 4.3 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 48.1% from a peak in-sample and 22.1% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 54 of every 100 trades won in-sample. Out-of-sample it earned 2.8% a year against 4.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 21% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 24.1% from a peak in-sample and 10.6% out-of-sample, and the worst single trade cost 6.1% of the account out-of-sample. About 59 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 42% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 28.9% from a peak in-sample and 11.6% out-of-sample, and the worst single trade cost 5.5% of the account out-of-sample. About 53 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2856 | `{"max_bars": 66, "n": 132, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 16,796.91 | 4.8 | -47.7 | 54.0 | 3,018.81 | 2.5 | -24.7 | 0.51 | 37/24 | not checked |
| 42897 | `{"max_bars": 66, "n": 126, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 16,796.91 | 4.8 | -47.7 | 54.0 | 3,018.81 | 2.5 | -24.7 | 0.51 | 37/24 | not checked |
| 28596 | `{"max_bars": 42, "n": 186, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 15,484.16 | 4.6 | -44.7 | 54.5 | 1,307.88 | 1.1 | -21.4 | 0.25 | 33/21 | not checked |
| 23721 | `{"max_bars": 66, "n": 192, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 15,228.13 | 4.5 | -43.5 | 50.0 | 2,303.00 | 1.9 | -21.4 | 0.43 | 32/21 | not checked |
| 48064 | `{"max_bars": 66, "n": 198, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 15,228.13 | 4.5 | -43.5 | 50.0 | 2,303.00 | 1.9 | -21.4 | 0.43 | 32/21 | not checked |
| 2626 | `{"max_bars": 42, "n": 198, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 14,913.62 | 4.4 | -42.0 | 51.5 | 1,761.33 | 1.5 | -20.8 | 0.34 | 33/21 | not checked |
| 2632 | `{"max_bars": 42, "n": 192, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 14,913.62 | 4.4 | -42.0 | 51.5 | 1,761.33 | 1.5 | -20.8 | 0.34 | 33/21 | 1.00 |
| 2627 | `{"max_bars": 42, "n": 192, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 14,213.58 | 4.3 | -42.0 | 48.6 | 2,870.79 | 2.4 | -19.1 | 0.55 | 35/21 | not checked |
| 39992 | `{"max_bars": 42, "n": 198, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 14,213.58 | 4.3 | -42.0 | 48.6 | 2,870.79 | 2.4 | -19.1 | 0.55 | 35/21 | not checked |
| 19594 | `{"max_bars": 60, "n": 198, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 14,189.46 | 4.3 | -40.1 | 47.1 | 3,373.38 | 2.7 | -19.1 | 0.63 | 34/21 | not checked |
| 45386 | `{"max_bars": 60, "n": 192, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 14,189.46 | 4.3 | -40.1 | 47.1 | 3,373.38 | 2.7 | -19.1 | 0.63 | 34/21 | not checked |
| 1039 | `{"max_bars": 66, "n": 198, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 14,085.38 | 4.3 | -38.5 | 45.5 | 3,373.38 | 2.7 | -19.1 | 0.63 | 33/21 | not checked |
| 33533 | `{"max_bars": 66, "n": 192, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 14,085.38 | 4.3 | -38.5 | 45.5 | 3,373.38 | 2.7 | -19.1 | 0.63 | 33/21 | not checked |
| 15807 | `{"max_bars": 30, "n": 126, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 11,153.66 | 3.6 | -37.3 | 52.6 | 1,122.61 | 1.0 | -19.7 | 0.27 | 38/22 | not checked |
| 27499 | `{"max_bars": 30, "n": 132, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 11,153.66 | 3.6 | -37.3 | 52.6 | 1,122.61 | 1.0 | -19.7 | 0.27 | 38/22 | not checked |
| 710 | `{"max_bars": 54, "n": 132, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 1,929.14 | 1.6 | -12.3 | 0.46 | 39/25 | not checked |
| 11729 | `{"max_bars": 66, "n": 132, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |
| 12013 | `{"max_bars": 66, "n": 126, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |
| 12576 | `{"max_bars": 84, "n": 132, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |
| 15666 | `{"max_bars": 54, "n": 126, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 1,929.14 | 1.6 | -12.3 | 0.46 | 39/25 | not checked |
| 21244 | `{"max_bars": 78, "n": 126, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |
| 26142 | `{"max_bars": 90, "n": 132, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |
| 31095 | `{"max_bars": 42, "n": 126, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 1,645.79 | 1.4 | -12.7 | 0.40 | 39/25 | not checked |
| 33699 | `{"max_bars": 72, "n": 132, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |
| 39707 | `{"max_bars": 90, "n": 126, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 10,865.07 | 3.6 | -28.3 | 66.7 | 2,462.70 | 2.0 | -12.3 | 0.57 | 39/25 | not checked |

(32 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

466 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | NVR | 100% | 4.6 | 8.5 | 31.2 | 2.7 | 3.4 | 51 |
| 2 | GEBN.SW | 100% | 4.6 | 7.2 | 15.7 | 3.5 | -2.5 | 0 |
| 3 | WYNN | 100% | 4.2 | 8.0 | 11.7 | 4.1 | -0.1 | 42 |
| 4 | TXN | 100% | 4.0 | 8.7 | 13.8 | 4.3 | -1.9 | 1 |
| 5 | AOS | 100% | 3.6 | 6.1 | 15.7 | 3.6 | -0.7 | 5 |
| 6 | SOON.SW | 100% | 3.5 | 7.3 | 19.8 | 2.6 | 3.2 | 33 |
| 7 | PCAR | 100% | 3.3 | 5.0 | 15.9 | 2.6 | 1.8 | 26 |
| 8 | VLO | 100% | 2.9 | 5.4 | 18.7 | 2.7 | 1.0 | 62 |
| 9 | OKE | 100% | 2.5 | 5.0 | 13.5 | 2.3 | 3.9 | 64 |
| 10 | PGR | 100% | 2.5 | 5.0 | 14.1 | 1.4 | 3.0 | 41 |
| 11 | TRV | 100% | 2.1 | 3.5 | 11.0 | 2.2 | 1.1 | 25 |
| 12 | MSFT | 100% | 2.0 | 4.7 | 15.5 | 1.8 | 0.9 | 20 |
| 13 | IBM | 100% | 2.0 | 3.4 | 11.5 | 0.8 | -1.4 | 2 |
| 14 | MAA | 100% | 1.9 | 3.1 | 13.6 | 2.1 | -0.2 | 21 |
| 15 | MO | 100% | 1.8 | 2.9 | 19.0 | 1.2 | -0.4 | 15 |
| 16 | FITB | 100% | 1.6 | 3.6 | 6.1 | 0.6 | -1.4 | 42 |
| 17 | NOVN.SW | 100% | 0.6 | 1.8 | 7.9 | 0.6 | -1.5 | 5 |
| 18 | KNIN.SW | 98% | 3.9 | 7.8 | 18.8 | 2.4 | 0.7 | 21 |
| 19 | INTC | 98% | 3.1 | 6.4 | 12.6 | 2.8 | 0.2 | 24 |
| 20 | TPL | 98% | 3.0 | 6.3 | 19.6 | 1.1 | 7.7 | 63 |
| 21 | TSN | 98% | 2.6 | 5.8 | 7.6 | 2.7 | 0.8 | 38 |
| 22 | ALB | 98% | 2.0 | 3.5 | 12.3 | 0.6 | 2.6 | 51 |
| 23 | ROST | 98% | 1.9 | 4.5 | 28.2 | 0.3 | 0.9 | 51 |
| 24 | DGX | 98% | 1.8 | 4.3 | 18.2 | 0.7 | -0.9 | 8 |
| 25 | WRB | 98% | 1.8 | 4.3 | 13.7 | 0.6 | 0.1 | 0 |
| 26 | HD | 98% | 1.7 | 4.2 | 14.7 | 0.1 | 2.1 | 56 |
| 27 | CMS | 98% | 1.6 | 3.5 | 5.5 | 1.3 | 0.3 | 16 |
| 28 | WEC | 98% | 1.1 | 2.2 | 10.9 | 1.4 | -0.8 | 12 |
| 29 | ED | 98% | 0.8 | 1.9 | 10.1 | 0.9 | -1.4 | 8 |
| 30 | BIIB | 97% | 5.5 | 13.7 | 37.8 | 2.8 | -4.4 | 0 |
| 31 | LOGN.SW | 97% | 4.6 | 7.8 | -6.7 | 5.0 | 1.4 | 44 |
| 32 | J | 97% | 2.8 | 4.8 | 11.0 | 2.2 | -3.0 | 0 |
| 33 | RCL | 97% | 2.7 | 6.8 | 11.5 | 1.9 | 4.2 | 59 |
| 34 | SAP | 97% | 2.6 | 4.7 | 11.9 | 2.3 | -0.7 | 10 |
| 35 | ROK | 97% | 2.5 | 5.7 | 14.6 | 1.2 | -1.7 | 5 |
| 36 | BA | 97% | 2.1 | 4.4 | 11.1 | 1.8 | 0.6 | 17 |
| 37 | SWK | 97% | 1.8 | 3.9 | 11.8 | 1.8 | -0.8 | 4 |
| 38 | DRI | 97% | 1.6 | 3.6 | 16.3 | 1.5 | 0.2 | 8 |
| 39 | XEL | 97% | 1.6 | 2.8 | 7.6 | 0.6 | 0.1 | 29 |
| 40 | VTR | 97% | 1.2 | 4.0 | 15.5 | 1.1 | 1.1 | 58 |

(426 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [annual_high_breakout__broad__max-income__v002.md](symbols/broad/annual_high_breakout__broad__max-income__v002.md) | 3.6 | 2.1 | 2.1 | -8.3 | 44.1 | 10770/5717 |
| broad | balanced | [annual_high_breakout__broad__balanced__v002.md](symbols/broad/annual_high_breakout__broad__balanced__v002.md) | 2.2 | 1.6 | 1.6 | -4.0 | 46.1 | 11209/5736 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 50,745 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
