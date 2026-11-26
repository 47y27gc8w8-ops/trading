# golden_cross__top3: optimization summary

Updated 2026-11-26T02:14:24Z · backtest.py version `58457d9bf2` · 1,108 parameter sets tested with this version (1,108 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: ^IXIC, SOXX, SMH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__top3__max-income__v001.md](golden_cross__top3__max-income__v001.md) | 580 | `{"fast": 30, "max_candles": 152, "slow": 200, "stop_atr": 4.0, "take_profit_atr": 10.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [golden_cross__top3__balanced__v002.md](golden_cross__top3__balanced__v002.md) | 1107 | `{"fast": 45, "max_candles": 80, "slow": 250, "stop_atr": 2.25, "take_profit_atr": 6.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [golden_cross__top3__safe-starter__v002.md](golden_cross__top3__safe-starter__v002.md) | 1108 | `{"fast": 10, "max_candles": 136, "slow": 280, "stop_atr": 1.5, "take_profit_atr": 6.0}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 17,222.45 | 12,850.44 | 6,782.06 | 6,529.04 | 5,343.01 | 2,491.24 |
| return % | 172.22 | 128.50 | 67.82 | 65.29 | 53.43 | 24.91 |
| return %/year | 4.9 | 7.9 | 2.5 | 4.7 | 2.1 | 2.1 |
| gross profit | 22,081.79 | 13,779.39 | 8,840.79 | 6,868.56 | 8,736.01 | 4,669.68 |
| gross loss | 4,859.34 | 928.96 | 2,058.73 | 339.52 | 3,393.00 | 2,178.44 |
| trades | 39 | 16 | 28 | 15 | 47 | 26 |
| win rate % | 61.5 | 75.0 | 64.3 | 80.0 | 44.7 | 30.8 |
| avg win | 920.07 | 1,148.28 | 491.15 | 572.38 | 416.00 | 583.71 |
| avg loss | -323.96 | -232.24 | -205.87 | -113.17 | -130.50 | -121.02 |
| avg result / trade | 441.60 | 803.15 | 242.22 | 435.27 | 113.68 | 95.82 |
| largest single loss | -659.05 | -355.55 | -291.55 | -116.77 | -313.32 | -265.50 |
| largest loss % of equity | -7.85 | -6.55 | -8.75 | -3.50 | -4.44 | -7.59 |
| max drawdown | -3,244.70 | -1,888.56 | -673.89 | -1,027.45 | -842.82 | -1,048.67 |
| max drawdown % | -12.12 | -15.50 | -5.59 | -7.72 | -5.46 | -10.27 |
| profit factor | 4.54 | 14.83 | 4.29 | 20.23 | 2.58 | 2.14 |
| unusually bad trades | 0 | 0 | 1 | 0 | 1 | 1 |
| … threshold (% of equity) | 10.8 | 11.3 | 7.6 | 7.0 | 6.1 | 6.9 |
| time in market % | 17.3 | 16.1 | 6.1 | 8.4 | 6.5 | 8.8 |
| buy & hold return % | 256.65 | 1,237.80 | 256.65 | 1,237.80 | 256.65 | 1,237.80 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.61 |  | 1.89 |  | 1.00 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 2.4 | 1.7 | -0.4 |
| 1996 | 3.7 | 0.0 | 3.6 |
| 1997 | 5.1 | 0.0 | 3.1 |
| 1998 | 4.4 | 3.4 | 5.3 |
| 1999 | 2.6 | 1.5 | 0.0 |
| 2000 | -1.2 | 0.0 | 0.0 |
| 2001 | -0.4 | 0.0 | 0.0 |
| 2002 | -3.6 | -2.7 | -2.8 |
| 2003 | 32.0 | 16.8 | 1.8 |
| 2004 | 0.4 | 1.6 | 1.2 |
| 2005 | -0.6 | 4.6 | 8.7 |
| 2006 | -2.7 | -0.6 | 0.1 |
| 2007 | 11.5 | 4.6 | 2.0 |
| 2008 | -2.6 | 0.0 | 0.0 |
| 2009 | 32.5 | 11.5 | 13.8 |
| 2010 | 13.5 | 8.0 | 4.9 |
| 2011 | 5.2 | 3.2 | -2.1 |
| 2012 | -4.2 | -2.9 | 1.9 |
| 2013 | 14.1 | 6.1 | 7.1 |
| 2014 | 0.0 | 0.0 | 0.0 |
| 2015 | -0.3 | -2.1 | -2.9 |
| 2016 (OOS) | 0.9 | -2.0 | -4.1 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 0.0 | -1.8 |
| 2019 (OOS) | 2.3 | 6.4 | -0.5 |
| 2020 (OOS) | 34.1 | 21.0 | 16.7 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 | -2.6 |
| 2023 (OOS) | 24.5 | 16.9 | 2.4 |
| 2024 (OOS) | 0.0 | 0.0 | 0.0 |
| 2025 (OOS) | 23.2 | 12.6 | 12.8 |
| 2026 (OOS) | -1.9 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 12.1% from a peak in-sample and 15.5% out-of-sample, and the worst single trade cost 6.5% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 65% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 5.6% from a peak in-sample and 7.7% out-of-sample, and the worst single trade cost 3.5% of the account out-of-sample. About 64 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 5.5% from a peak in-sample and 10.3% out-of-sample, and the worst single trade cost 7.6% of the account out-of-sample. About 45 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 97% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 242 | `{"fast": 30, "max_candles": 160, "slow": 200, "stop_atr": 4.0, "take_profit_atr": 10.0}` | 17,461.04 | 4.9 | -12.1 | 61.5 | 12,850.44 | 7.9 | -15.5 | 1.60 | 39/16 | not checked |
| 230 | `{"fast": 30, "max_candles": 152, "slow": 200, "stop_atr": 4.0, "take_profit_atr": 10.0}` | 17,222.45 | 4.9 | -12.1 | 61.5 | 12,850.44 | 7.9 | -15.5 | 1.61 | 39/16 | 1.00 |
| 711 | `{"fast": 35, "max_candles": 160, "slow": 210, "stop_atr": 4.25, "take_profit_atr": 10.0}` | 16,502.51 | 4.8 | -11.6 | 63.2 | 10,194.60 | 6.7 | -7.8 | 1.40 | 38/16 | not checked |
| 748 | `{"fast": 30, "max_candles": 160, "slow": 200, "stop_atr": 3.25, "take_profit_atr": 10.0}` | 16,372.69 | 4.7 | -11.3 | 59.0 | 9,914.23 | 6.5 | -14.6 | 1.38 | 39/16 | not checked |
| 946 | `{"fast": 35, "max_candles": 152, "slow": 200, "stop_atr": 2.25, "take_profit_atr": 10.0}` | 15,560.12 | 4.6 | -9.2 | 52.6 | 10,222.16 | 6.7 | -7.7 | 1.46 | 38/16 | not checked |
| 1070 | `{"fast": 40, "max_candles": 144, "slow": 200, "stop_atr": 2.25, "take_profit_atr": 10.0}` | 11,228.76 | 3.6 | -7.8 | 47.2 | 9,627.38 | 6.4 | -8.1 | 1.75 | 36/16 | not checked |
| 704 | `{"fast": 55, "max_candles": 72, "slow": 250, "stop_atr": 2.5, "take_profit_atr": 6.5}` | 8,213.29 | 2.9 | -6.0 | 66.7 | 4,126.41 | 3.2 | -7.7 | 1.11 | 30/16 | not checked |
| 971 | `{"fast": 40, "max_candles": 80, "slow": 250, "stop_atr": 2.0, "take_profit_atr": 7.0}` | 7,163.11 | 2.6 | -5.3 | 56.2 | 5,432.35 | 4.1 | -6.0 | 1.56 | 32/15 | not checked |
| 733 | `{"fast": 45, "max_candles": 80, "slow": 250, "stop_atr": 2.0, "take_profit_atr": 6.5}` | 6,184.65 | 2.3 | -5.3 | 60.7 | 5,335.52 | 4.0 | -7.7 | 1.73 | 28/15 | not checked |
| 644 | `{"fast": 10, "max_candles": 136, "slow": 280, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 4,912.95 | 1.9 | -5.2 | 40.4 | 1,897.61 | 1.6 | -9.3 | 0.84 | 47/26 | not checked |
| 795 | `{"fast": 10, "max_candles": 128, "slow": 280, "stop_atr": 1.25, "take_profit_atr": 6.0}` | 4,912.95 | 1.9 | -5.2 | 40.4 | 1,897.61 | 1.6 | -9.3 | 0.84 | 47/26 | not checked |
| 509 | `{"fast": 55, "max_candles": 80, "slow": 250, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 4,791.95 | 1.9 | -5.1 | 56.7 | 2,685.98 | 2.2 | -4.9 | 1.18 | 30/16 | not checked |
| 675 | `{"fast": 10, "max_candles": 128, "slow": 280, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 3,900.59 | 1.6 | -4.7 | 34.0 | 1,700.66 | 1.4 | -7.1 | 0.92 | 47/26 | not checked |
| 625 | `{"fast": 50, "max_candles": 88, "slow": 250, "stop_atr": 1.5, "take_profit_atr": 6.0}` | 3,857.47 | 1.6 | -4.5 | 48.3 | 3,114.31 | 2.5 | -5.9 | 1.60 | 29/15 | not checked |
| 662 | `{"fast": 40, "max_candles": 72, "slow": 250, "stop_atr": 1.75, "take_profit_atr": 6.0}` | 3,587.40 | 1.5 | -4.2 | 46.9 | 3,474.12 | 2.8 | -5.9 | 1.89 | 32/15 | not checked |
| 338 | `{"fast": 75, "max_candles": 56, "slow": 230, "stop_atr": 1.25, "take_profit_atr": 3.5}` | 2,758.98 | 1.2 | -4.1 | 58.3 | 1,290.52 | 1.1 | -4.0 | 0.96 | 24/13 | not checked |
| 395 | `{"fast": 75, "max_candles": 176, "slow": 230, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 2,592.30 | 1.1 | -3.5 | 87.5 | 1,409.69 | 1.2 | -2.6 | 1.11 | 24/13 | not checked |
| 431 | `{"fast": 75, "max_candles": 64, "slow": 230, "stop_atr": 1.75, "take_profit_atr": 2.0}` | 2,140.73 | 0.9 | -3.2 | 79.2 | 748.76 | 0.7 | -3.0 | 0.72 | 24/13 | not checked |
| 575 | `{"fast": 75, "max_candles": 72, "slow": 250, "stop_atr": 2.0, "take_profit_atr": 2.0}` | 1,316.86 | 0.6 | -2.9 | 65.2 | 1,047.96 | 0.9 | -1.8 | 1.56 | 23/12 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,108 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
