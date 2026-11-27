# dual_momentum_allocation: optimization summary

Updated 2026-11-27T12:32:30Z · backtest.py version `164566c210` · 4,839 parameter sets tested with this version (4,839 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: EFA, IEF, SPY (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [dual_momentum_allocation__max-income__v001.md](dual_momentum_allocation__max-income__v001.md) | 4838 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 20}` | long EFA since 2026-11-02 00:00 @ 103.721109 |
| balanced | [dual_momentum_allocation__balanced__v001.md](dual_momentum_allocation__balanced__v001.md) | 4839 | `{"max_candles": 420, "n": 315, "stop_loss_pct": 21}` | long EFA since 2026-11-02 00:00 @ 103.721109 |
| safe-starter | [dual_momentum_allocation__safe-starter__v001.md](dual_momentum_allocation__safe-starter__v001.md) | 4838 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 20}` | long EFA since 2026-11-02 00:00 @ 103.721109 |

Note: one parameter set wins max-income, safe-starter. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 31,213.92 | 9,241.37 | 29,795.60 | 11,860.15 | 31,213.92 | 9,241.37 |
| return % | 312.14 | 92.41 | 297.96 | 118.60 | 312.14 | 92.41 |
| return %/year | 12.5 | 6.2 | 12.2 | 7.5 | 12.5 | 6.2 |
| gross profit | 36,637.98 | 16,785.57 | 33,751.10 | 16,758.58 | 36,637.98 | 16,785.57 |
| gross loss | 5,424.07 | 7,544.20 | 3,955.51 | 4,898.43 | 5,424.07 | 7,544.20 |
| trades | 20 | 27 | 18 | 26 | 20 | 27 |
| win rate % | 65.0 | 70.4 | 66.7 | 69.2 | 65.0 | 70.4 |
| avg win | 2,818.31 | 883.45 | 2,812.59 | 931.03 | 2,818.31 | 883.45 |
| avg loss | -774.87 | -943.03 | -659.25 | -612.30 | -774.87 | -943.03 |
| avg result / trade | 1,560.70 | 342.27 | 1,655.31 | 456.16 | 1,560.70 | 342.27 |
| largest single loss | -1,168.01 | -3,075.43 | -1,535.74 | -1,127.99 | -1,168.01 | -3,075.43 |
| largest loss % of equity | -2.72 | -20.10 | -8.28 | -4.90 | -2.72 | -20.10 |
| max drawdown | -5,600.52 | -4,436.15 | -3,419.11 | -4,197.13 | -5,600.52 | -4,436.15 |
| max drawdown % | -17.46 | -27.64 | -17.46 | -24.65 | -17.46 | -27.64 |
| profit factor | 6.75 | 2.23 | 8.53 | 3.42 | 6.75 | 2.23 |
| unusually bad trades | 0 | 1 | 1 | 1 | 0 | 1 |
| … threshold (% of equity) | 7.1 | 9.0 | 5.5 | 7.7 | 7.1 | 9.0 |
| time in market % | 32.0 | 32.5 | 32.4 | 32.9 | 32.0 | 32.5 |
| buy & hold return % | 97.27 | 157.89 | 97.27 | 157.89 | 97.27 | 157.89 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.49 |  | 0.61 |  | 0.49 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2004 | 17.7 | 17.7 | 17.7 |
| 2005 | 15.5 | 13.2 | 15.5 |
| 2006 | 33.5 | 25.8 | 33.5 |
| 2007 | 14.7 | 9.2 | 14.7 |
| 2008 | 5.4 | 5.4 | 5.4 |
| 2009 | -10.0 | -6.3 | -10.0 |
| 2010 | 9.2 | 9.2 | 9.2 |
| 2011 | 15.6 | 15.6 | 15.6 |
| 2012 | 16.0 | 16.0 | 16.0 |
| 2013 | 30.6 | 30.6 | 30.6 |
| 2014 | 13.5 | 13.5 | 13.5 |
| 2015 | -3.7 | 1.5 | -3.7 |
| 2016 (OOS) | -6.1 | -6.1 | -6.1 |
| 2017 (OOS) | 19.3 | 19.3 | 19.3 |
| 2018 (OOS) | -8.2 | -8.2 | -8.2 |
| 2019 (OOS) | 17.2 | 17.2 | 17.2 |
| 2020 (OOS) | 3.0 | 3.0 | 3.0 |
| 2021 (OOS) | 20.3 | 28.7 | 20.3 |
| 2022 (OOS) | -21.0 | -18.3 | -21.0 |
| 2023 (OOS) | 14.4 | 14.4 | 14.4 |
| 2024 (OOS) | 19.9 | 19.9 | 19.9 |
| 2025 (OOS) | 10.4 | 13.5 | 10.4 |
| 2026 (OOS) | 1.7 | 1.7 | 1.7 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.5% from a peak in-sample and 27.6% out-of-sample, and the worst single trade cost 20.1% of the account out-of-sample. About 65 of every 100 trades won in-sample. Out-of-sample it earned 6.2% a year against 12.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 17.5% from a peak in-sample and 24.6% out-of-sample, and the worst single trade cost 4.9% of the account out-of-sample. About 67 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 41% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 17.5% from a peak in-sample and 27.6% out-of-sample, and the worst single trade cost 20.1% of the account out-of-sample. About 65 of every 100 trades won in-sample. Out-of-sample it earned 6.2% a year against 12.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3193 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 19}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 9,481.88 | 6.3 | -26.7 | 0.50 | 20/27 | not checked |
| 3194 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 21}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 9,734.38 | 6.4 | -25.8 | 0.51 | 20/27 | not checked |
| 3197 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 20}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 9,241.37 | 6.2 | -27.6 | 0.49 | 20/27 | 1.00 |
| 3272 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 18}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 9,722.40 | 6.4 | -25.8 | 0.51 | 20/27 | not checked |
| 3340 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 16}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 8,403.71 | 5.8 | -30.8 | 0.46 | 20/27 | not checked |
| 3650 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 22}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 7,799.89 | 5.4 | -30.4 | 0.43 | 20/27 | not checked |
| 4035 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 25}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 11,051.88 | 7.1 | -25.1 | 0.56 | 20/27 | not checked |
| 4126 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 23}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 7,799.89 | 5.4 | -30.4 | 0.43 | 20/27 | not checked |
| 4479 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 17}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 9,962.92 | 6.6 | -24.9 | 0.52 | 20/27 | not checked |
| 4617 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 24}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 11,051.88 | 7.1 | -25.1 | 0.56 | 20/27 | not checked |
| 4829 | `{"max_candles": 273, "n": 315, "stop_loss_pct": 15}` | 31,213.92 | 12.5 | -17.5 | 65.0 | 6,642.41 | 4.8 | -34.9 | 0.38 | 20/28 | not checked |
| 3308 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 24}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 10,904.85 | 7.0 | -26.5 | 0.58 | 20/27 | not checked |
| 3694 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 25}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 8,875.20 | 6.0 | -30.9 | 0.50 | 20/27 | not checked |
| 4069 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 22}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 10,657.49 | 6.9 | -27.3 | 0.57 | 20/27 | not checked |
| 4075 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 23}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 10,392.65 | 6.8 | -28.3 | 0.56 | 20/27 | not checked |
| 4084 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 19}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 9,541.06 | 6.3 | -31.3 | 0.53 | 20/27 | not checked |
| 4095 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 17}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 10,023.56 | 6.6 | -29.6 | 0.55 | 20/27 | not checked |
| 4339 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 21}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 10,922.33 | 7.0 | -26.4 | 0.58 | 20/27 | not checked |
| 4661 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 18}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 9,777.06 | 6.5 | -30.4 | 0.54 | 20/27 | not checked |
| 4694 | `{"max_candles": 315, "n": 315, "stop_loss_pct": 20}` | 29,001.46 | 12.0 | -16.6 | 70.0 | 11,180.26 | 7.1 | -25.5 | 0.59 | 20/27 | not checked |
| 4181 | `{"max_candles": 462, "n": 315, "stop_loss_pct": 12}` | 27,193.44 | 11.6 | -15.8 | 73.7 | 8,989.21 | 6.1 | -31.3 | 0.53 | 19/28 | not checked |
| 3398 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 15}` | 26,023.08 | 11.3 | -15.8 | 62.2 | 13,268.66 | 8.1 | -34.4 | 0.71 | 45/45 | not checked |
| 3530 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 23}` | 26,023.08 | 11.3 | -15.8 | 62.2 | 15,064.14 | 8.8 | -29.3 | 0.78 | 45/45 | not checked |
| 3619 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 24}` | 26,023.08 | 11.3 | -15.8 | 62.2 | 15,064.14 | 8.8 | -29.3 | 0.78 | 45/45 | not checked |
| 3827 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 22}` | 26,023.08 | 11.3 | -15.8 | 62.2 | 15,064.14 | 8.8 | -29.3 | 0.78 | 45/45 | not checked |

(8 more on the front, see results.csv)


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 4,839 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
