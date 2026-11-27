# drawdown_defensive_switch: optimization summary

Updated 2026-11-27T12:18:19Z · backtest.py version `71d2033794` · 850 parameter sets tested with this version (850 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: IEF, SPY (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [drawdown_defensive_switch__max-income__v002.md](drawdown_defensive_switch__max-income__v002.md) | 849 | `{"dd": 9, "max_candles": 252, "n": 105, "stop_loss_pct": 24}` | long SPY since 2026-07-01 00:00 @ 743.377539 |
| balanced | [drawdown_defensive_switch__balanced__v002.md](drawdown_defensive_switch__balanced__v002.md) | 850 | `{"dd": 6, "max_candles": 189, "n": 105, "stop_loss_pct": 7}` | long SPY since 2026-05-01 00:00 @ 717.829936 |
| safe-starter | [drawdown_defensive_switch__safe-starter__v001.md](drawdown_defensive_switch__safe-starter__v001.md) | 291 | `{"dd": 5, "max_candles": 189, "n": 210, "stop_loss_pct": 22}` | long SPY since 2026-05-01 00:00 @ 717.829936 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 22,666.96 | 28,493.38 | 21,088.13 | 10,954.75 | 15,800.26 | 15,655.96 |
| return % | 226.67 | 284.93 | 210.88 | 109.55 | 158.00 | 156.56 |
| return %/year | 10.4 | 13.2 | 9.9 | 7.0 | 8.2 | 9.0 |
| gross profit | 26,337.66 | 34,129.84 | 24,884.51 | 15,201.55 | 17,494.63 | 17,952.61 |
| gross loss | 3,670.69 | 5,636.46 | 3,796.38 | 4,246.81 | 1,694.37 | 2,296.65 |
| trades | 17 | 15 | 25 | 24 | 26 | 22 |
| win rate % | 64.7 | 66.7 | 76.0 | 62.5 | 76.9 | 68.2 |
| avg win | 2,394.33 | 3,412.98 | 1,309.71 | 1,013.44 | 874.73 | 1,196.84 |
| avg loss | -611.78 | -1,127.29 | -632.73 | -471.87 | -282.39 | -328.09 |
| avg result / trade | 1,333.35 | 1,899.56 | 843.53 | 456.45 | 607.70 | 711.63 |
| largest single loss | -999.34 | -1,397.76 | -1,485.69 | -1,178.42 | -449.15 | -747.18 |
| largest loss % of equity | -8.25 | -5.65 | -7.12 | -7.12 | -1.71 | -4.05 |
| max drawdown | -4,986.85 | -6,080.13 | -2,602.39 | -4,620.84 | -2,159.74 | -3,173.79 |
| max drawdown % | -19.80 | -22.52 | -12.46 | -25.41 | -12.02 | -13.31 |
| profit factor | 7.17 | 6.05 | 6.55 | 3.58 | 10.32 | 7.82 |
| unusually bad trades | 2 | 0 | 2 | 3 | 0 | 1 |
| … threshold (% of equity) | 4.5 | 11.3 | 4.2 | 3.1 | 3.6 | 3.1 |
| time in market % | 47.3 | 44.4 | 46.9 | 42.1 | 46.1 | 40.0 |
| buy & hold return % | 107.13 | 169.81 | 107.13 | 169.81 | 107.13 | 169.81 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.27 |  | 0.71 |  | 1.10 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2004 | 8.3 | 3.6 | 3.6 |
| 2005 | 2.4 | 3.5 | 3.5 |
| 2006 | 13.9 | 16.4 | 14.2 |
| 2007 | 1.6 | 2.2 | 4.2 |
| 2008 | -1.2 | 8.4 | 19.3 |
| 2009 | 23.6 | 27.8 | -2.5 |
| 2010 | 25.9 | 11.4 | 8.2 |
| 2011 | 2.8 | 1.5 | 5.7 |
| 2012 | 16.5 | 5.4 | 3.1 |
| 2013 | 28.1 | 27.6 | 27.6 |
| 2014 | 13.8 | 13.6 | 13.6 |
| 2015 | -5.1 | 1.9 | 1.9 |
| 2016 (OOS) | 7.9 | 6.7 | 6.6 |
| 2017 (OOS) | 20.0 | 17.9 | 17.9 |
| 2018 (OOS) | -5.0 | -7.9 | 5.6 |
| 2019 (OOS) | 19.5 | 8.3 | 8.5 |
| 2020 (OOS) | 26.6 | 1.1 | 1.1 |
| 2021 (OOS) | 25.2 | 34.5 | 26.0 |
| 2022 (OOS) | -18.3 | -21.0 | -5.2 |
| 2023 (OOS) | 19.5 | 11.2 | 5.3 |
| 2024 (OOS) | 20.0 | 19.3 | 19.3 |
| 2025 (OOS) | 13.3 | 10.5 | 10.5 |
| 2026 (OOS) | 8.2 | 0.2 | 0.2 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 19.8% from a peak in-sample and 22.5% out-of-sample, and the worst single trade cost 5.7% of the account out-of-sample. About 65 of every 100 trades won in-sample. With 100% of equity per trade; about 44% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 12.5% from a peak in-sample and 25.4% out-of-sample, and the worst single trade cost 7.1% of the account out-of-sample. About 76 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 39% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks low: the account fell up to 12.0% from a peak in-sample and 13.3% out-of-sample, and the worst single trade cost 4.0% of the account out-of-sample. About 77 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 75% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 688 | `{"dd": 6, "max_candles": 189, "n": 84, "stop_loss_pct": 6}` | 22,758.87 | 10.4 | -12.0 | 76.0 | 11,081.60 | 7.1 | -25.6 | 0.68 | 25/25 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 850 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
