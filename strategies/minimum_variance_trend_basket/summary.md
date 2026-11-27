# minimum_variance_trend_basket: optimization summary

Updated 2026-11-27T12:43:09Z · backtest.py version `7dbf9b5ce0` · 2,173 parameter sets tested with this version (2,173 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [minimum_variance_trend_basket__max-income__v001.md](minimum_variance_trend_basket__max-income__v001.md) | 179 | `{"max_candles": 420, "n": 84, "stop_loss_pct": 10}` | long DBC since 2025-07-01 00:00 @ 28.773376; long EFA since 2026-10-01 00:00 @ 103.411011; long SPY since 2026-05-01 00:00 @ 752.04547; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| balanced | [minimum_variance_trend_basket__balanced__v001.md](minimum_variance_trend_basket__balanced__v001.md) | 180 | `{"max_candles": 420, "n": 63, "stop_loss_pct": 18}` | long DBC since 2025-07-01 00:00 @ 29.120306; long EFA since 2026-09-01 00:00 @ 103.924449; long SPY since 2026-05-01 00:00 @ 753.769437; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 9,355.71 | 4,577.91 | 9,259.34 | 4,369.36 |
| return % | 93.56 | 45.78 | 92.59 | 43.69 |
| return %/year | 5.7 | 3.5 | 5.6 | 3.4 |
| gross profit | 13,748.66 | 14,859.72 | 14,347.69 | 15,067.05 |
| gross loss | 4,392.94 | 10,281.81 | 5,088.35 | 10,697.69 |
| trades | 81 | 103 | 84 | 106 |
| win rate % | 50.6 | 42.7 | 51.2 | 47.2 |
| avg win | 335.33 | 337.72 | 333.67 | 301.34 |
| avg loss | -109.82 | -174.27 | -124.11 | -191.03 |
| avg result / trade | 115.50 | 44.45 | 110.23 | 41.22 |
| largest single loss | -408.15 | -1,594.60 | -566.24 | -2,893.29 |
| largest loss % of equity | -2.36 | -10.42 | -3.38 | -18.09 |
| max drawdown | -1,320.40 | -4,975.73 | -1,256.87 | -5,925.91 |
| max drawdown % | -9.50 | -28.51 | -9.38 | -32.44 |
| profit factor | 3.13 | 1.45 | 2.82 | 1.41 |
| unusually bad trades | 5 | 11 | 8 | 11 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 34.0 | 37.3 | 33.8 | 36.9 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.62 |  | 0.60 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 1.1 | 1.1 |
| 2005 | 5.8 | 5.6 |
| 2006 | 3.0 | 2.8 |
| 2007 | 7.2 | 7.5 |
| 2008 | 12.6 | 12.2 |
| 2009 | 3.6 | 3.8 |
| 2010 | 6.6 | 6.6 |
| 2011 | 12.3 | 10.9 |
| 2012 | 4.8 | 4.6 |
| 2013 | 13.1 | 12.2 |
| 2014 | 2.1 | 2.6 |
| 2015 | -2.9 | -1.6 |
| 2016 (OOS) | 0.6 | 1.2 |
| 2017 (OOS) | 9.3 | 9.6 |
| 2018 (OOS) | -4.2 | 1.6 |
| 2019 (OOS) | 8.0 | 8.4 |
| 2020 (OOS) | 12.8 | 12.0 |
| 2021 (OOS) | 22.4 | 20.6 |
| 2022 (OOS) | -23.0 | -26.7 |
| 2023 (OOS) | 4.0 | 3.9 |
| 2024 (OOS) | 5.7 | 4.1 |
| 2025 (OOS) | 8.3 | 11.2 |
| 2026 (OOS) | -2.8 | -4.5 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 9.5% from a peak in-sample and 28.5% out-of-sample, and the worst single trade cost 10.4% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 9.4% from a peak in-sample and 32.4% out-of-sample, and the worst single trade cost 18.1% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 31% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1063 | `{"max_candles": 273, "n": 63, "stop_loss_pct": 10}` | 9,615.35 | 5.8 | -12.0 | 53.9 | 4,019.91 | 3.1 | -29.1 | 0.55 | 89/112 | not checked |
| 53 | `{"max_candles": 420, "n": 63, "stop_loss_pct": 10}` | 9,482.38 | 5.7 | -9.4 | 51.2 | 4,744.72 | 3.6 | -29.1 | 0.64 | 84/108 | not checked |
| 237 | `{"max_candles": 441, "n": 42, "stop_loss_pct": 17}` | 9,212.28 | 5.6 | -9.3 | 56.0 | 6,440.34 | 4.7 | -31.2 | 0.83 | 91/115 | not checked |
| 197 | `{"max_candles": 420, "n": 42, "stop_loss_pct": 17}` | 9,103.76 | 5.5 | -9.0 | 55.4 | 6,469.20 | 4.7 | -31.2 | 0.85 | 92/115 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 2,173 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
