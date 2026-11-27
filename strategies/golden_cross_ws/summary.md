# golden_cross_ws: optimization summary

Updated 2026-11-23T22:12:39Z · backtest.py version `12324f9774` · 2,790 parameter sets tested with this version (2,790 rows in results.csv in total) · last run ended: report only

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-20
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 5 in-sample and ≥ 2 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross_ws__max-income__v001.md](golden_cross_ws__max-income__v001.md) | 176 | `{"fast": 105, "slow": 120, "trailing_stop_pct": 24}` | long SPY since 2025-08-12 00:00 @ 629.92016 |
| balanced | [golden_cross_ws__balanced__v001.md](golden_cross_ws__balanced__v001.md) | 176 | `{"fast": 105, "slow": 120, "trailing_stop_pct": 24}` | long SPY since 2025-08-12 00:00 @ 629.92016 |
| safe-starter | [golden_cross_ws__safe-starter__v002.md](golden_cross_ws__safe-starter__v002.md) | 2790 | `{"fast": 35, "slow": 290, "trailing_stop_pct": 7}` | flat (data up to 2026-11-23 00:00) |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 68,871.79 | 10,805.26 | 68,871.79 | 10,805.26 | 5,148.64 | 5,936.99 |
| return % | 688.72 | 108.05 | 688.72 | 108.05 | 51.49 | 59.37 |
| return %/year | 10.3 | 7.0 | 10.3 | 7.0 | 2.0 | 4.4 |
| gross profit | 77,614.27 | 14,855.29 | 77,614.27 | 14,855.29 | 5,148.64 | 6,336.53 |
| gross loss | 8,742.48 | 4,050.03 | 8,742.48 | 4,050.03 | -0.00 | 399.54 |
| trades | 28 | 10 | 28 | 10 | 5 | 6 |
| win rate % | 75.0 | 70.0 | 75.0 | 70.0 | 100.0 | 66.7 |
| avg win | 3,695.92 | 2,122.18 | 3,695.92 | 2,122.18 | 1,029.73 | 1,584.13 |
| avg loss | -1,248.93 | -1,350.01 | -1,248.93 | -1,350.01 | 0.00 | -199.77 |
| avg result / trade | 2,459.71 | 1,080.53 | 2,459.71 | 1,080.53 | 1,029.73 | 989.50 |
| largest single loss | -2,982.06 | -2,164.66 | -2,982.06 | -2,164.66 | 0.00 | -211.84 |
| largest loss % of equity | -10.90 | -14.92 | -10.90 | -14.92 | 0.00 | -1.60 |
| max drawdown | -10,159.39 | -4,596.52 | -10,159.39 | -4,596.52 | -1,352.83 | -1,693.03 |
| max drawdown % | -21.57 | -30.21 | -21.57 | -30.21 | -8.34 | -11.80 |
| profit factor | 8.88 | 3.67 | 8.88 | 3.67 | 999.00 | 15.86 |
| unusually bad trades | 2 | 0 | 2 | 0 | 0 | 0 |
| … threshold (% of equity) | 5.3 | 22.5 | 5.3 | 22.5 | 2.0 | 2.9 |
| time in market % | 70.6 | 78.9 | 70.6 | 78.9 | 11.6 | 33.2 |
| buy & hold return % | 551.07 | 309.13 | 551.07 | 309.13 | 551.07 | 309.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.67 |  | 0.67 |  | 2.19 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 28.4 | 28.4 | 0.0 |
| 1996 | 22.5 | 22.5 | 0.0 |
| 1997 | 33.5 | 33.5 | 0.0 |
| 1998 | 6.5 | 6.5 | 16.0 |
| 1999 | 20.6 | 20.6 | 4.2 |
| 2000 | 1.4 | 1.4 | 0.0 |
| 2001 | -10.9 | -10.9 | 0.0 |
| 2002 | -3.3 | -3.3 | 0.0 |
| 2003 | 28.3 | 28.3 | 17.4 |
| 2004 | 12.7 | 12.7 | -2.3 |
| 2005 | 2.1 | 2.1 | 0.0 |
| 2006 | 6.4 | 6.4 | 0.0 |
| 2007 | 8.3 | 8.3 | 0.0 |
| 2008 | -9.2 | -9.2 | 0.0 |
| 2009 | 21.8 | 21.8 | 12.4 |
| 2010 | 5.4 | 5.4 | -4.0 |
| 2011 | 7.4 | 7.4 | 0.0 |
| 2012 | 8.5 | 8.5 | 1.1 |
| 2013 | 32.3 | 32.3 | 0.0 |
| 2014 | 13.5 | 13.5 | 0.0 |
| 2015 | -3.5 | -3.5 | 0.3 |
| 2016 (OOS) | 15.3 | 15.3 | 4.3 |
| 2017 (OOS) | 21.7 | 21.7 | 21.7 |
| 2018 (OOS) | -12.0 | -12.0 | -0.2 |
| 2019 (OOS) | 12.5 | 12.5 | -1.6 |
| 2020 (OOS) | -11.1 | -11.1 | 7.4 |
| 2021 (OOS) | 28.7 | 28.7 | 0.0 |
| 2022 (OOS) | -9.0 | -9.0 | 0.0 |
| 2023 (OOS) | 19.0 | 19.0 | 3.2 |
| 2024 (OOS) | 24.2 | 24.2 | 0.0 |
| 2025 (OOS) | -4.5 | -4.5 | 15.9 |
| 2026 (OOS) | 1.9 | 1.9 | -4.9 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 21.6% from a peak in-sample and 30.2% out-of-sample, and the worst single trade cost 14.9% of the account out-of-sample. About 75 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 33% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 21.6% from a peak in-sample and 30.2% out-of-sample, and the worst single trade cost 14.9% of the account out-of-sample. About 75 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 33% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 8.3% from a peak in-sample and 11.8% out-of-sample, and the worst single trade cost 1.6% of the account out-of-sample. About 100 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 85% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 52 | `{"fast": 105, "slow": 120, "trailing_stop_pct": 24}` | 68,871.79 | 10.3 | -21.6 | 75.0 | 10,805.26 | 7.0 | -30.2 | 0.67 | 28/10 | 1.00 |
| 61 | `{"fast": 105, "slow": 120, "trailing_stop_pct": 23}` | 68,871.79 | 10.3 | -21.6 | 75.0 | 10,805.26 | 7.0 | -30.2 | 0.67 | 28/10 | not checked |
| 62 | `{"fast": 105, "slow": 120, "trailing_stop_pct": 25}` | 68,871.79 | 10.3 | -21.6 | 75.0 | 10,667.91 | 6.9 | -30.7 | 0.67 | 28/10 | not checked |
| 204 | `{"fast": 105, "slow": 120, "trailing_stop_pct": 22}` | 68,871.79 | 10.3 | -21.6 | 75.0 | 10,805.26 | 7.0 | -30.2 | 0.67 | 28/10 | not checked |
| 59 | `{"fast": 110, "slow": 120, "trailing_stop_pct": 24}` | 60,912.21 | 9.8 | -21.3 | 69.4 | 12,354.95 | 7.7 | -28.5 | 0.79 | 36/11 | not checked |
| 247 | `{"fast": 110, "slow": 120, "trailing_stop_pct": 23}` | 60,912.21 | 9.8 | -21.3 | 69.4 | 12,354.95 | 7.7 | -28.5 | 0.79 | 36/11 | not checked |
| 262 | `{"fast": 110, "slow": 120, "trailing_stop_pct": 25}` | 60,912.21 | 9.8 | -21.3 | 69.4 | 12,207.38 | 7.6 | -29.0 | 0.78 | 36/11 | not checked |
| 275 | `{"fast": 110, "slow": 120, "trailing_stop_pct": 22}` | 60,912.21 | 9.8 | -21.3 | 69.4 | 12,354.95 | 7.7 | -28.5 | 0.79 | 36/11 | not checked |
| 1667 | `{"fast": 60, "slow": 130, "trailing_stop_pct": 25}` | 57,633.13 | 9.5 | -19.0 | 64.7 | 14,582.28 | 8.6 | -24.9 | 0.91 | 17/9 | not checked |
| 2752 | `{"fast": 60, "slow": 130, "trailing_stop_pct": 22}` | 57,633.13 | 9.5 | -19.0 | 64.7 | 14,745.64 | 8.7 | -24.4 | 0.91 | 17/9 | not checked |
| 1864 | `{"fast": 10, "slow": 180, "trailing_stop_pct": 16}` | 37,911.48 | 7.8 | -16.1 | 60.9 | 18,107.03 | 10.0 | -21.9 | 1.29 | 23/10 | not checked |
| 1154 | `{"fast": 35, "slow": 230, "trailing_stop_pct": 12}` | 24,660.03 | 6.1 | -15.4 | 85.7 | 22,075.13 | 11.3 | -17.1 | 1.85 | 7/5 | not checked |
| 1183 | `{"fast": 35, "slow": 240, "trailing_stop_pct": 12}` | 24,483.38 | 6.1 | -15.1 | 83.3 | 22,158.61 | 11.3 | -16.8 | 1.87 | 6/5 | not checked |
| 235 | `{"fast": 40, "slow": 270, "trailing_stop_pct": 11}` | 23,230.06 | 5.9 | -14.8 | 85.7 | 22,907.33 | 11.6 | -14.6 | 1.96 | 7/5 | not checked |
| 658 | `{"fast": 35, "slow": 290, "trailing_stop_pct": 13}` | 22,536.74 | 5.8 | -14.6 | 100.0 | 19,153.52 | 10.3 | -18.1 | 1.79 | 5/6 | not checked |
| 1118 | `{"fast": 35, "slow": 290, "trailing_stop_pct": 11}` | 21,358.67 | 5.6 | -13.3 | 100.0 | 21,356.88 | 11.1 | -14.9 | 1.98 | 5/6 | not checked |
| 143 | `{"fast": 55, "slow": 220, "trailing_stop_pct": 10}` | 13,074.69 | 4.1 | -12.8 | 85.7 | 6,829.77 | 4.9 | -15.1 | 1.21 | 7/5 | not checked |
| 2134 | `{"fast": 50, "slow": 220, "trailing_stop_pct": 8}` | 12,289.97 | 3.9 | -10.9 | 71.4 | 5,341.37 | 4.0 | -14.0 | 1.03 | 7/5 | not checked |
| 1624 | `{"fast": 60, "slow": 230, "trailing_stop_pct": 8}` | 10,580.92 | 3.5 | -9.1 | 71.4 | 6,735.62 | 4.8 | -12.2 | 1.39 | 7/5 | not checked |
| 2692 | `{"fast": 65, "slow": 210, "trailing_stop_pct": 7}` | 9,924.67 | 3.3 | -8.1 | 87.5 | 2,775.25 | 2.3 | -15.6 | 0.68 | 8/5 | not checked |
| 822 | `{"fast": 60, "slow": 240, "trailing_stop_pct": 7}` | 5,043.28 | 2.0 | -7.8 | 83.3 | 5,022.71 | 3.8 | -11.8 | 1.94 | 6/5 | not checked |
| 428 | `{"fast": 35, "slow": 290, "trailing_stop_pct": 6}` | 3,950.84 | 1.6 | -7.3 | 100.0 | 2,032.43 | 1.7 | -10.3 | 1.07 | 5/6 | not checked |
| 2407 | `{"fast": 10, "slow": 240, "trailing_stop_pct": 4}` | 3,099.30 | 1.3 | -7.1 | 46.7 | 2,312.67 | 1.9 | -8.5 | 1.50 | 15/8 | not checked |
| 1730 | `{"fast": 40, "slow": 270, "trailing_stop_pct": 3}` | 1,837.96 | 0.8 | -4.9 | 71.4 | 315.70 | 0.3 | -7.0 | 0.36 | 7/5 | not checked |
| 1152 | `{"fast": 35, "slow": 270, "trailing_stop_pct": 3}` | 1,444.15 | 0.6 | -3.6 | 60.0 | 272.59 | 0.2 | -6.0 | 0.39 | 5/5 | not checked |

(3 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

63 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | QQQ | 100% | 5.0 | 7.7 | 2.0 | 7.7 | 16.4 | 23 |
| 2 | ^GSPC | 100% | 5.0 | 9.1 | 7.4 | 5.1 | 7.5 | 23 |
| 3 | XLY | 100% | 4.4 | 7.5 | 8.6 | 3.6 | 4.9 | 22 |
| 4 | TLT | 100% | 3.5 | 4.8 | 6.9 | 3.2 | 0.6 | 3 |
| 5 | IEF | 100% | 3.0 | 3.9 | 5.1 | 3.0 | 1.0 | 17 |
| 6 | ^DJI | 100% | 2.0 | 6.7 | 7.5 | 2.8 | 3.5 | 23 |
| 7 | ^IXIC | 96% | 6.2 | 11.4 | 9.5 | 7.5 | 12.8 | 22 |
| 8 | ^SSMI | 96% | 5.9 | 7.7 | 5.9 | 6.6 | 0.9 | 6 |
| 9 | XLP | 96% | 5.4 | 7.3 | 8.4 | 6.2 | 2.8 | 13 |
| 10 | ^RUT | 96% | 3.2 | 5.8 | 7.5 | 4.2 | 1.3 | 18 |
| 11 | ^GDAXI | 92% | 7.5 | 9.6 | 8.1 | 8.6 | 4.3 | 14 |
| 12 | XLI | 92% | 5.2 | 6.5 | 6.6 | 5.8 | 4.5 | 21 |
| 13 | EFA | 92% | 5.0 | 7.6 | 7.2 | 5.3 | 3.3 | 20 |
| 14 | VUG | 92% | 4.3 | 7.9 | 8.7 | 5.7 | 11.8 | 21 |
| 15 | LQD | 92% | 3.3 | 4.1 | 5.1 | 3.3 | 0.8 | 10 |
| 16 | ^FTSE | 92% | 3.1 | 4.1 | 3.5 | 3.8 | 1.5 | 13 |
| 17 | XLK | 92% | 2.7 | 5.9 | -0.6 | 4.6 | 16.8 | 21 |
| 18 | XLF | 92% | 2.5 | 5.3 | 3.0 | 5.3 | 6.1 | 21 |
| 19 | ^N225 | 92% | 1.7 | 3.0 | -0.2 | 2.8 | 7.0 | 22 |
| 20 | SMH | 92% | 1.6 | 5.7 | 1.4 | 4.4 | 24.8 | 21 |
| 21 | XLE | 88% | 5.6 | 9.9 | 7.1 | 8.4 | 8.6 | 14 |
| 22 | SOXX | 88% | 4.1 | 9.3 | 8.8 | 6.8 | 23.6 | 20 |
| 23 | IWM | 88% | 3.9 | 7.2 | 7.4 | 3.0 | 1.6 | 18 |
| 24 | VNQ | 83% | 5.1 | 8.8 | 7.4 | 6.5 | -2.0 | 5 |
| 25 | SPY | 83% | 5.0 | 10.3 | 9.3 | 6.3 | 9.0 | 20 |
| 26 | XLB | 83% | 3.2 | 4.9 | 7.3 | 4.9 | 3.1 | 18 |
| 27 | XLV | 83% | 2.7 | 5.0 | 7.6 | 3.6 | 3.1 | 19 |
| 28 | DIA | 83% | 2.4 | 4.6 | 5.7 | 4.6 | 5.8 | 19 |
| 29 | XLU | 79% | 6.7 | 8.9 | 7.3 | 8.6 | 5.5 | 18 |
| 30 | IVV | 79% | 4.7 | 8.6 | 5.8 | 7.7 | 9.1 | 18 |
| 31 | VTI | 75% | 6.6 | 10.1 | 9.1 | 9.3 | 8.8 | 17 |
| 32 | ACWI | 75% | 3.0 | 6.9 | 9.4 | 4.9 | 7.7 | 18 |
| 33 | AGG | 75% | 2.5 | 3.4 | 4.1 | 1.3 | 1.3 | 17 |
| 34 | RSP | 67% | 6.4 | 10.2 | 8.8 | 9.3 | 5.3 | 14 |
| 35 | TIP | 67% | 2.6 | 3.5 | 3.7 | 2.6 | 2.1 | 14 |
| 36 | EEM | 62% | 0.9 | 9.3 | 7.6 | 5.8 | 3.8 | 15 |
| 37 | BND | 54% | 2.7 | 3.5 | 4.3 | 2.1 | 1.2 | 10 |
| 38 | HYG | 50% | 5.3 | 7.2 | 5.1 | 6.6 | 2.4 | 12 |
| 39 | GLD | 50% | 4.8 | 7.7 | 6.2 | 5.7 | 8.1 | 12 |
| 40 | SHY | 50% | 1.7 | 1.9 | 2.1 | 1.8 | 1.9 | 12 |

(23 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| QQQ | max-income | [golden_cross_ws__QQQ__max-income__v002.md](symbols/QQQ/golden_cross_ws__QQQ__max-income__v002.md) | 9.4 | 15.3 | 9.4 | -28.6 | 80.0 | 5/4 |
| QQQ | balanced | [golden_cross_ws__QQQ__balanced__v002.md](symbols/QQQ/golden_cross_ws__QQQ__balanced__v002.md) | 6.8 | 5.1 | 5.1 | -15.2 | 88.9 | 9/4 |
| QQQ | safe-starter | [golden_cross_ws__QQQ__safe-starter__v002.md](symbols/QQQ/golden_cross_ws__QQQ__safe-starter__v002.md) | 2.2 | 2.0 | 2.0 | -10.6 | 44.4 | 9/4 |
| XLI | max-income | [golden_cross_ws__XLI__max-income__v001.md](symbols/XLI/golden_cross_ws__XLI__max-income__v001.md) | 7.7 | 4.3 | 4.3 | -42.7 | 50.0 | 12/7 |
| XLI | balanced | [golden_cross_ws__XLI__balanced__v002.md](symbols/XLI/golden_cross_ws__XLI__balanced__v002.md) | 0.7 | 0.2 | 0.2 | -2.1 | 66.7 | 9/6 |
| XLI | safe-starter | [golden_cross_ws__XLI__safe-starter__v002.md](symbols/XLI/golden_cross_ws__XLI__safe-starter__v002.md) | 4.2 | 2.6 | 2.6 | -16.5 | 55.0 | 20/12 |
| XLY | max-income | [golden_cross_ws__XLY__max-income__v002.md](symbols/XLY/golden_cross_ws__XLY__max-income__v002.md) | 7.8 | 4.4 | 4.4 | -35.9 | 62.5 | 8/4 |
| XLY | balanced | [golden_cross_ws__XLY__balanced__v001.md](symbols/XLY/golden_cross_ws__XLY__balanced__v001.md) | 7.2 | 8.4 | 7.2 | -29.6 | 58.8 | 17/9 |
| XLY | safe-starter | [golden_cross_ws__XLY__safe-starter__v002.md](symbols/XLY/golden_cross_ws__XLY__safe-starter__v002.md) | 2.5 | 2.1 | 2.1 | -17.1 | 63.6 | 11/6 |
| top3 | max-income | [golden_cross_ws__top3__max-income__v002.md](symbols/top3/golden_cross_ws__top3__max-income__v002.md) | 8.4 | 10.1 | 8.4 | -33.4 | 85.7 | 14/11 |
| top3 | balanced | [golden_cross_ws__top3__balanced__v001.md](symbols/top3/golden_cross_ws__top3__balanced__v001.md) | 5.0 | 4.5 | 4.5 | -19.3 | 56.2 | 32/18 |
| top3 | safe-starter | [golden_cross_ws__top3__safe-starter__v002.md](symbols/top3/golden_cross_ws__top3__safe-starter__v002.md) | 2.2 | 4.5 | 2.2 | -17.0 | 63.2 | 19/13 |


## Analyst notes

<!-- analyst-notes:start -->
**Short trial run (~5 min total): treat these as first indications, not final variants.**

- **The plain 50/200 golden cross on SPY is hard to beat.** Defaults (no trailing stop): in-sample 6.3 %/yr, out-of-sample 9.0 %/yr, max drawdown -34 % (OOS), 9 + 5 trades. The tuned SPY max-income/balanced variant (fast 105 / slow 120, trailing stop 24 %) earns more in-sample (10.3 %/yr) but *less* out-of-sample (7.0 %/yr) with about the same drawdown. Two averages that close together act like a fast price-trend filter that happened to fit 1995–2015 well; I would not prefer it over 50/200.
- **Trailing stop:** wide stops (20–25 %) almost never fire and change little. Tight stops (6–12 %) cut drawdowns sharply but, because the rule only re-enters on a *fresh* golden cross, they leave the strategy in cash for years after a stop (SPY safe-starter 35/290/7 %: in the market 12 % of the in-sample time, 2 %/yr). That's why the safe-starter variants all look like "barely trades". If re-entry while the trend is still up were allowed (open question 1), a tight stop could look very different.
- **Where it works:** across 63 ETFs the rule is profitable in-sample for 92–100 % of sampled settings on broad equity ETFs (QQQ, XLY, XLI, XLK, EFA, VUG) and bonds (TLT, IEF). As expected for a trend filter, it mostly earns *less* than buy & hold; its value is avoiding the long bear markets (2000–02, 2008), not more return. QQQ is the exception (IS beat buy & hold because of the dot-com crash).
- **Best candidates:** QQQ max-income (fast 70 / slow 240, no stop): 9.4 %/yr IS, 15.3 %/yr OOS, worst DD -28.6 %, neighbours all profitable, but only 5 + 4 trades, so the evidence is thin. The QQQ/XLY/XLI basket max-income (120/320, no stop) is backed by 14 + 11 trades: 8.4 / 10.1 %/yr, DD -33 %.
- **Stability:** yearly returns are spread over many years (no single lucky stretch), losses cluster in choppy years (2001, 2008 entry, 2018, 2020, 2022) when a cross whipsaws. Trade counts are tiny everywhere (≈ one trade every 2 years), so every number here carries large uncertainty.
- **Range warnings:** slow was widened 300 → 350 for XLY, XLI and the basket (bests near the upper edge), fast widened down to 1 for XLI balanced. The XLI balanced variant (21/300, 1 % stop: 0.2 %/yr) and XLI safe-starter (fast 6) are not meaningful golden-cross variants; ignore them.
- **What I'd paper-trade first:** the plain 50/200 on SPY or the QQQ 70/240 variant, no trailing stop, at about 30–35 % of the account (the size that would have kept the worst drawdown near 10 %). A longer run (1–2 h) would refine the per-symbol results; it won't add trades, which is the real limit.
<!-- analyst-notes:end -->

---

Searching 2,790 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
