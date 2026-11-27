# inverse_volatility_trend_basket: optimization summary

Updated 2026-11-27T11:55:06Z · backtest.py version `aa09d6f490` · 845 parameter sets tested with this version (845 rows in results.csv in total) · last run ended: converged: no profile improved in the last 510 iterations at the smallest step size

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [inverse_volatility_trend_basket__max-income__v002.md](inverse_volatility_trend_basket__max-income__v002.md) | 844 | `{"max_candles": 399, "n": 170, "stop_loss_pct": 16}` | long DBC since 2025-07-01 00:00 @ 26.249151; long EFA since 2026-10-01 00:00 @ 103.411011; long SPY since 2026-05-01 00:00 @ 737.477845; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| balanced | [inverse_volatility_trend_basket__balanced__v002.md](inverse_volatility_trend_basket__balanced__v002.md) | 845 | `{"max_candles": 441, "n": 180, "stop_loss_pct": 19}` | long DBC since 2025-07-01 00:00 @ 25.900739; long SPY since 2026-05-01 00:00 @ 732.35537; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 15,275.68 | 10,996.85 | 14,341.90 | 12,405.17 |
| return % | 152.76 | 109.97 | 143.42 | 124.05 |
| return %/year | 8.0 | 7.0 | 7.7 | 7.7 |
| gross profit | 24,137.29 | 19,909.57 | 21,884.89 | 20,274.09 |
| gross loss | 8,861.62 | 8,912.72 | 7,542.98 | 7,868.92 |
| trades | 96 | 101 | 88 | 93 |
| win rate % | 44.8 | 45.5 | 46.6 | 46.2 |
| avg win | 561.33 | 432.82 | 533.78 | 471.49 |
| avg loss | -167.20 | -162.05 | -160.49 | -157.38 |
| avg result / trade | 159.12 | 108.88 | 162.98 | 133.39 |
| largest single loss | -637.30 | -2,020.85 | -585.43 | -1,826.89 |
| largest loss % of equity | -2.48 | -10.92 | -2.48 | -9.59 |
| max drawdown | -3,058.94 | -5,400.74 | -2,159.44 | -4,520.24 |
| max drawdown % | -13.32 | -26.01 | -11.80 | -21.73 |
| profit factor | 2.72 | 2.23 | 2.90 | 2.58 |
| unusually bad trades | 3 | 3 | 2 | 3 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 63.2 | 65.5 | 63.8 | 65.5 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.88 |  | 1.00 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 6.4 | 6.5 |
| 2005 | 11.4 | 11.6 |
| 2006 | 17.0 | 13.8 |
| 2007 | 11.3 | 12.3 |
| 2008 | 20.5 | 15.3 |
| 2009 | 6.4 | 9.0 |
| 2010 | 9.3 | 10.1 |
| 2011 | 9.5 | 6.6 |
| 2012 | -0.3 | 0.8 |
| 2013 | 10.6 | 6.3 |
| 2014 | 2.4 | 4.1 |
| 2015 | -5.5 | -2.5 |
| 2016 (OOS) | 8.1 | 8.9 |
| 2017 (OOS) | 13.9 | 14.3 |
| 2018 (OOS) | 1.4 | -0.3 |
| 2019 (OOS) | 10.5 | 10.9 |
| 2020 (OOS) | 18.4 | 20.1 |
| 2021 (OOS) | 19.7 | 19.3 |
| 2022 (OOS) | -18.8 | -15.1 |
| 2023 (OOS) | 4.8 | 6.4 |
| 2024 (OOS) | 6.4 | 6.2 |
| 2025 (OOS) | 19.2 | 18.1 |
| 2026 (OOS) | 0.6 | 2.2 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 13.3% from a peak in-sample and 26.0% out-of-sample, and the worst single trade cost 10.9% of the account out-of-sample. About 45 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 11.8% from a peak in-sample and 21.7% out-of-sample, and the worst single trade cost 9.6% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 46% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 333 | `{"max_candles": 399, "n": 170, "stop_loss_pct": 16}` | 15,275.68 | 8.0 | -13.3 | 44.8 | 10,996.85 | 7.0 | -26.0 | 0.88 | 96/101 | 1.00 |
| 720 | `{"max_candles": 420, "n": 240, "stop_loss_pct": 21}` | 15,169.56 | 8.0 | -11.8 | 47.0 | 7,930.29 | 5.5 | -24.0 | 0.69 | 83/98 | not checked |
| 767 | `{"max_candles": 420, "n": 240, "stop_loss_pct": 22}` | 15,169.56 | 8.0 | -11.8 | 47.0 | 7,930.29 | 5.5 | -24.0 | 0.69 | 83/98 | not checked |
| 772 | `{"max_candles": 420, "n": 240, "stop_loss_pct": 23}` | 15,169.56 | 8.0 | -11.8 | 47.0 | 7,930.29 | 5.5 | -24.0 | 0.69 | 83/98 | not checked |
| 795 | `{"max_candles": 420, "n": 240, "stop_loss_pct": 24}` | 15,169.56 | 8.0 | -11.8 | 47.0 | 7,930.29 | 5.5 | -24.0 | 0.69 | 83/98 | not checked |
| 819 | `{"max_candles": 420, "n": 240, "stop_loss_pct": 25}` | 15,169.56 | 8.0 | -11.8 | 47.0 | 7,930.29 | 5.5 | -24.0 | 0.69 | 83/98 | not checked |
| 338 | `{"max_candles": 420, "n": 180, "stop_loss_pct": 17}` | 14,770.11 | 7.9 | -11.8 | 45.6 | 9,978.37 | 6.6 | -29.8 | 0.83 | 90/96 | not checked |
| 739 | `{"max_candles": 420, "n": 220, "stop_loss_pct": 21}` | 13,570.18 | 7.4 | -11.3 | 43.0 | 7,809.82 | 5.5 | -26.8 | 0.73 | 86/102 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 845 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
