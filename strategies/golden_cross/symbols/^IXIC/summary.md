# golden_cross__^IXIC: optimization summary

Updated 2026-11-26T02:13:06Z · backtest.py version `c9c614bfa8` · 1,422 parameter sets tested with this version (1,422 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: ^IXIC (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__^IXIC__max-income__v002.md](golden_cross__^IXIC__max-income__v002.md) | 1421 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 4.0, "take_profit_atr": 10.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [golden_cross__^IXIC__balanced__v002.md](golden_cross__^IXIC__balanced__v002.md) | 1422 | `{"fast": 25, "max_candles": 72, "slow": 270, "stop_atr": 4.0, "take_profit_atr": 9.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | [golden_cross__^IXIC__safe-starter__v001.md](golden_cross__^IXIC__safe-starter__v001.md) | 426 | `{"fast": 25, "max_candles": 88, "slow": 280, "stop_atr": 3.75, "take_profit_atr": 5.0}` | flat (data up to 2026-11-25 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 35,793.69 | 6,574.88 | 17,430.91 | 7,131.38 | 7,674.22 | 4,840.93 |
| return % | 357.94 | 65.75 | 174.31 | 71.31 | 76.74 | 48.41 |
| return %/year | 7.5 | 4.8 | 4.9 | 5.1 | 2.8 | 3.7 |
| gross profit | 37,311.86 | 7,347.62 | 18,061.38 | 7,573.10 | 7,908.38 | 5,009.05 |
| gross loss | 1,518.17 | 772.74 | 630.47 | 441.73 | 234.16 | 168.12 |
| trades | 20 | 9 | 11 | 6 | 10 | 6 |
| win rate % | 85.0 | 66.7 | 90.9 | 83.3 | 90.0 | 83.3 |
| avg win | 2,194.82 | 1,224.60 | 1,806.14 | 1,514.62 | 878.71 | 1,001.81 |
| avg loss | -506.06 | -257.58 | -630.47 | -441.73 | -234.16 | -168.12 |
| avg result / trade | 1,789.68 | 730.54 | 1,584.63 | 1,188.56 | 767.42 | 806.82 |
| largest single loss | -1,008.11 | -381.22 | -630.47 | -441.73 | -234.16 | -168.12 |
| largest loss % of equity | -2.64 | -3.81 | -2.25 | -4.42 | -1.31 | -1.68 |
| max drawdown | -2,786.66 | -761.67 | -1,370.25 | -1,090.63 | -823.87 | -649.79 |
| max drawdown % | -14.42 | -7.25 | -7.79 | -10.18 | -4.52 | -5.27 |
| profit factor | 24.58 | 9.51 | 28.65 | 17.14 | 33.77 | 29.79 |
| unusually bad trades | 1 | 0 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 2.2 | 4.5 | 4.5 | 8.8 | 2.6 | 3.4 |
| time in market % | 17.0 | 14.9 | 10.9 | 12.9 | 5.0 | 6.5 |
| buy & hold return % | 566.49 | 391.86 | 566.49 | 391.86 | 566.49 | 391.86 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.63 |  | 1.03 |  | 1.34 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1995 | 7.7 | 6.7 | 3.7 |
| 1996 | 8.5 | 0.0 | 0.0 |
| 1997 | 15.8 | 14.0 | 0.0 |
| 1998 | 21.2 | 17.1 | 9.4 |
| 1999 | 4.2 | 0.0 | 0.0 |
| 2000 | 11.3 | 0.0 | 0.0 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 | 0.0 |
| 2003 | 19.7 | 15.9 | 8.5 |
| 2004 | 8.8 | 6.5 | 5.7 |
| 2005 | 4.9 | -1.3 | 5.0 |
| 2006 | 12.5 | 6.2 | 5.6 |
| 2007 | 0.0 | 3.6 | 0.0 |
| 2008 | 0.0 | 0.0 | 0.0 |
| 2009 | 13.8 | 17.7 | 8.6 |
| 2010 | 13.8 | 11.7 | 7.8 |
| 2011 | -1.6 | 0.8 | 0.0 |
| 2012 | 16.8 | 11.0 | 6.0 |
| 2013 | 4.6 | 0.0 | 0.0 |
| 2014 | 0.0 | 0.0 | 0.0 |
| 2015 | 0.9 | -2.2 | -1.2 |
| 2016 (OOS) | -8.8 | -3.7 | -0.4 |
| 2017 (OOS) | 0.0 | 0.0 | 0.0 |
| 2018 (OOS) | -1.8 | 0.0 | 0.0 |
| 2019 (OOS) | 5.6 | 4.4 | 5.4 |
| 2020 (OOS) | 26.1 | 25.7 | 14.1 |
| 2021 (OOS) | 0.0 | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 | 0.0 |
| 2023 (OOS) | 14.3 | 15.0 | 8.0 |
| 2024 (OOS) | 0.0 | 0.0 | 0.0 |
| 2025 (OOS) | 13.4 | 14.1 | 10.1 |
| 2026 (OOS) | 0.0 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 14.4% from a peak in-sample and 7.2% out-of-sample, and the worst single trade cost 3.8% of the account out-of-sample. About 85 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 69% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 7.8% from a peak in-sample and 10.2% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 91 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 98% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 4.5% from a peak in-sample and 5.3% out-of-sample, and the worst single trade cost 1.7% of the account out-of-sample. About 90 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 951 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,460.82 | 4.7 | -7.4 | 0.62 | 20/9 | not checked |
| 952 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,574.88 | 4.8 | -7.2 | 0.63 | 20/9 | not checked |
| 954 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,574.88 | 4.8 | -7.2 | 0.63 | 20/9 | 1.00 |
| 1021 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,510.73 | 4.7 | -7.2 | 0.63 | 20/9 | not checked |
| 1078 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 4.5, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,574.88 | 4.8 | -7.2 | 0.63 | 20/9 | not checked |
| 1157 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 3.25, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,346.68 | 4.6 | -7.9 | 0.61 | 20/9 | not checked |
| 1166 | `{"fast": 10, "max_candles": 64, "slow": 270, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 35,793.69 | 7.5 | -14.4 | 85.0 | 6,574.88 | 4.8 | -7.2 | 0.63 | 20/9 | not checked |
| 844 | `{"fast": 20, "max_candles": 80, "slow": 250, "stop_atr": 4.0, "take_profit_atr": 10.0}` | 25,400.49 | 6.2 | -10.0 | 85.7 | 7,831.24 | 5.5 | -11.0 | 0.88 | 14/7 | 1.00 |
| 850 | `{"fast": 20, "max_candles": 80, "slow": 250, "stop_atr": 4.25, "take_profit_atr": 10.0}` | 25,400.49 | 6.2 | -10.0 | 85.7 | 7,831.24 | 5.5 | -11.0 | 0.88 | 14/7 | not checked |
| 941 | `{"fast": 20, "max_candles": 80, "slow": 250, "stop_atr": 4.5, "take_profit_atr": 10.0}` | 25,400.49 | 6.2 | -10.0 | 85.7 | 7,791.37 | 5.4 | -11.2 | 0.88 | 14/7 | not checked |
| 1172 | `{"fast": 15, "max_candles": 80, "slow": 260, "stop_atr": 4.0, "take_profit_atr": 10.0}` | 23,940.93 | 6.0 | -9.0 | 75.0 | 6,477.66 | 4.7 | -13.0 | 0.78 | 16/8 | not checked |
| 992 | `{"fast": 15, "max_candles": 64, "slow": 260, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 22,113.20 | 5.7 | -8.9 | 75.0 | 3,799.04 | 3.0 | -9.9 | 0.52 | 16/8 | not checked |
| 1114 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 4.5, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,573.02 | 3.5 | -7.9 | 0.63 | 17/9 | not checked |
| 1155 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,573.02 | 3.5 | -7.9 | 0.63 | 17/9 | not checked |
| 1197 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 3.75, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,573.02 | 3.5 | -7.9 | 0.63 | 17/9 | not checked |
| 1293 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,573.02 | 3.5 | -7.9 | 0.63 | 17/9 | not checked |
| 1313 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 3.5, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,439.92 | 3.4 | -7.9 | 0.61 | 17/9 | not checked |
| 1341 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,573.02 | 3.5 | -7.9 | 0.63 | 17/9 | not checked |
| 1376 | `{"fast": 10, "max_candles": 56, "slow": 280, "stop_atr": 3.25, "take_profit_atr": 10.5}` | 21,403.22 | 5.6 | -7.8 | 76.5 | 4,296.44 | 3.3 | -8.0 | 0.60 | 17/9 | not checked |
| 640 | `{"fast": 25, "max_candles": 48, "slow": 270, "stop_atr": 4.5, "take_profit_atr": 10.5}` | 16,248.23 | 4.7 | -7.2 | 90.9 | 4,860.52 | 3.7 | -6.3 | 0.79 | 11/6 | not checked |
| 690 | `{"fast": 25, "max_candles": 48, "slow": 270, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 16,248.23 | 4.7 | -7.2 | 90.9 | 4,900.10 | 3.7 | -6.3 | 0.79 | 11/6 | not checked |
| 733 | `{"fast": 25, "max_candles": 48, "slow": 270, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 16,248.23 | 4.7 | -7.2 | 90.9 | 4,820.94 | 3.7 | -6.3 | 0.78 | 11/6 | not checked |
| 756 | `{"fast": 25, "max_candles": 48, "slow": 280, "stop_atr": 4.5, "take_profit_atr": 10.5}` | 12,154.73 | 3.9 | -7.0 | 90.0 | 5,250.99 | 4.0 | -6.3 | 1.02 | 10/6 | not checked |
| 823 | `{"fast": 25, "max_candles": 48, "slow": 280, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 12,154.73 | 3.9 | -7.0 | 90.0 | 5,250.99 | 4.0 | -6.3 | 1.02 | 10/6 | not checked |
| 826 | `{"fast": 25, "max_candles": 48, "slow": 280, "stop_atr": 4.25, "take_profit_atr": 10.5}` | 12,154.73 | 3.9 | -7.0 | 90.0 | 5,250.99 | 4.0 | -6.3 | 1.02 | 10/6 | not checked |

(16 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,422 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
