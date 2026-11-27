# consistent_winner_rotation: optimization summary

Updated 2026-11-27T11:49:06Z · backtest.py version `ee39969495` · 911 parameter sets tested with this version (911 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d bars)
- In-sample (tuning): 2000-07-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [consistent_winner_rotation__max-income__v002.md](consistent_winner_rotation__max-income__v002.md) | 910 | `{"k": 5, "max_candles": 315, "n": 19, "stop_loss_pct": 11}` | long XLE since 2026-02-02 00:00 @ 49.758662; long XLF since 2026-11-02 00:00 @ 56.977087; long XLP since 2026-11-02 00:00 @ 89.866948; long XLV since 2026-09-01 00:00 @ 172.013467 |
| balanced | [consistent_winner_rotation__balanced__v002.md](consistent_winner_rotation__balanced__v002.md) | 911 | `{"k": 5, "max_candles": 336, "n": 19, "stop_loss_pct": 11}` | long XLE since 2026-02-02 00:00 @ 49.758662; long XLF since 2026-11-02 00:00 @ 56.977087; long XLP since 2026-11-02 00:00 @ 89.866948; long XLV since 2026-09-01 00:00 @ 172.013467 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 12,353.12 | 17,635.66 | 12,303.07 | 16,551.44 |
| return % | 123.53 | 176.36 | 123.03 | 165.51 |
| return %/year | 5.3 | 9.8 | 5.3 | 9.4 |
| gross profit | 27,232.79 | 34,830.39 | 27,159.46 | 33,562.31 |
| gross loss | 14,879.67 | 17,194.72 | 14,856.39 | 17,010.87 |
| trades | 165 | 152 | 165 | 151 |
| win rate % | 50.9 | 52.0 | 50.9 | 51.7 |
| avg win | 324.20 | 440.89 | 323.33 | 430.29 |
| avg loss | -183.70 | -235.54 | -183.41 | -233.03 |
| avg result / trade | 74.87 | 116.02 | 74.56 | 109.61 |
| largest single loss | -924.76 | -731.55 | -909.02 | -705.51 |
| largest loss % of equity | -5.67 | -2.78 | -5.67 | -2.78 |
| max drawdown | -4,800.94 | -5,770.99 | -4,719.22 | -6,051.36 |
| max drawdown % | -35.57 | -24.31 | -35.57 | -24.65 |
| profit factor | 1.83 | 2.03 | 1.83 | 1.97 |
| unusually bad trades | 17 | 21 | 18 | 21 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 35.9 | 41.0 | 36.0 | 41.2 |
| buy & hold return % | 139.85 | 244.45 | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.84 |  | 1.77 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 14.2 | 14.2 |
| 2001 | -20.2 | -20.2 |
| 2002 | -12.1 | -12.1 |
| 2003 | 24.8 | 24.8 |
| 2004 | 15.6 | 15.4 |
| 2005 | 10.5 | 10.0 |
| 2006 | 16.2 | 13.0 |
| 2007 | 14.2 | 16.1 |
| 2008 | -23.6 | -23.6 |
| 2009 | 20.4 | 20.4 |
| 2010 | -1.7 | -1.7 |
| 2011 | 5.4 | 5.4 |
| 2012 | 5.9 | 7.4 |
| 2013 | 36.6 | 37.1 |
| 2014 | 10.0 | 9.9 |
| 2015 | -13.0 | -13.0 |
| 2016 (OOS) | 10.0 | 10.0 |
| 2017 (OOS) | 19.8 | 20.0 |
| 2018 (OOS) | -6.3 | -7.2 |
| 2019 (OOS) | 18.7 | 18.7 |
| 2020 (OOS) | 29.3 | 29.3 |
| 2021 (OOS) | 24.9 | 25.8 |
| 2022 (OOS) | -18.1 | -19.3 |
| 2023 (OOS) | 11.1 | 11.1 |
| 2024 (OOS) | 16.1 | 13.7 |
| 2025 (OOS) | 6.0 | 6.0 |
| 2026 (OOS) | 0.7 | 0.3 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 35.6% from a peak in-sample and 24.3% out-of-sample, and the worst single trade cost 2.8% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 28% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 35.6% from a peak in-sample and 24.6% out-of-sample, and the worst single trade cost 2.8% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 28% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 386 | `{"k": 5, "max_candles": 336, "n": 19, "stop_loss_pct": 12}` | 12,476.73 | 5.4 | -36.9 | 51.8 | 16,437.61 | 9.3 | -25.0 | 1.74 | 164/150 | not checked |
| 371 | `{"k": 5, "max_candles": 315, "n": 19, "stop_loss_pct": 11}` | 12,353.12 | 5.3 | -35.6 | 50.9 | 17,635.66 | 9.8 | -24.3 | 1.84 | 165/152 | 1.00 |
| 385 | `{"k": 5, "max_candles": 336, "n": 19, "stop_loss_pct": 10}` | 11,386.40 | 5.0 | -34.9 | 49.7 | 13,559.69 | 8.2 | -28.3 | 1.63 | 169/156 | not checked |
| 847 | `{"k": 3, "max_candles": 252, "n": 9, "stop_loss_pct": 11}` | 10,906.14 | 4.9 | -34.3 | 50.7 | 14,479.86 | 8.6 | -27.0 | 1.76 | 142/123 | not checked |
| 404 | `{"k": 5, "max_candles": 252, "n": 14, "stop_loss_pct": 10}` | 10,156.16 | 4.6 | -34.2 | 51.8 | 16,152.58 | 9.2 | -25.1 | 1.99 | 193/156 | not checked |
| 473 | `{"k": 4, "max_candles": 168, "n": 12, "stop_loss_pct": 10}` | 9,847.46 | 4.5 | -33.3 | 53.3 | 14,301.40 | 8.5 | -26.5 | 1.88 | 184/149 | not checked |
| 695 | `{"k": 4, "max_candles": 126, "n": 12, "stop_loss_pct": 10}` | 8,014.29 | 3.9 | -32.7 | 53.5 | 14,344.38 | 8.5 | -29.5 | 2.20 | 200/157 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 911 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
