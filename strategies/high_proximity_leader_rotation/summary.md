# high_proximity_leader_rotation: optimization summary

Updated 2026-11-27T11:49:54Z · backtest.py version `b629cd4b61` · 1,060 parameter sets tested with this version (1,060 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d bars)
- In-sample (tuning): 2000-07-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [high_proximity_leader_rotation__max-income__v002.md](high_proximity_leader_rotation__max-income__v002.md) | 1059 | `{"k": 5, "max_candles": 273, "n": 294, "stop_loss_pct": 27}` | long XLB since 2026-11-02 00:00 @ 53.245969; long XLE since 2026-08-03 00:00 @ 58.908276; long XLF since 2026-08-03 00:00 @ 56.295402; long XLP since 2026-11-02 00:00 @ 89.866948; long XLV since 2026-07-01 00:00 @ 160.599188 |
| balanced | [high_proximity_leader_rotation__balanced__v002.md](high_proximity_leader_rotation__balanced__v002.md) | 1060 | `{"k": 5, "max_candles": 126, "n": 336, "stop_loss_pct": 28}` | long XLB since 2026-11-02 00:00 @ 53.245969; long XLE since 2026-08-03 00:00 @ 58.908276; long XLF since 2026-08-03 00:00 @ 56.295402; long XLP since 2026-11-02 00:00 @ 89.866948; long XLV since 2026-07-01 00:00 @ 160.599188 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 12,558.84 | 16,823.88 | 13,081.04 | 14,373.70 |
| return % | 125.59 | 168.24 | 130.81 | 143.74 |
| return %/year | 5.4 | 9.5 | 5.5 | 8.5 |
| gross profit | 27,399.79 | 32,978.02 | 29,991.32 | 31,140.48 |
| gross loss | 14,840.96 | 16,154.14 | 16,910.27 | 16,766.78 |
| trades | 202 | 185 | 235 | 205 |
| win rate % | 59.4 | 57.3 | 59.1 | 60.5 |
| avg win | 228.33 | 311.11 | 215.76 | 251.13 |
| avg loss | -180.99 | -204.48 | -176.15 | -207.00 |
| avg result / trade | 62.17 | 90.94 | 55.66 | 70.12 |
| largest single loss | -1,712.17 | -1,670.49 | -1,664.56 | -1,664.45 |
| largest loss % of equity | -13.15 | -11.66 | -13.15 | -11.66 |
| max drawdown | -5,040.28 | -4,820.52 | -4,900.02 | -5,099.68 |
| max drawdown % | -38.52 | -30.36 | -38.24 | -30.36 |
| profit factor | 1.85 | 2.04 | 1.77 | 1.86 |
| unusually bad trades | 7 | 7 | 9 | 12 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 37.3 | 41.7 | 36.3 | 40.7 |
| buy & hold return % | 139.85 | 244.45 | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.76 |  | 1.54 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 14.1 | 14.1 |
| 2001 | -21.6 | -21.6 |
| 2002 | -18.1 | -17.6 |
| 2003 | 23.6 | 22.0 |
| 2004 | 18.6 | 17.8 |
| 2005 | 8.2 | 8.1 |
| 2006 | 11.0 | 10.1 |
| 2007 | 16.1 | 15.5 |
| 2008 | -24.5 | -24.5 |
| 2009 | 19.2 | 21.3 |
| 2010 | 4.1 | 0.9 |
| 2011 | 5.9 | 8.3 |
| 2012 | 12.9 | 18.7 |
| 2013 | 31.0 | 30.4 |
| 2014 | 12.6 | 12.5 |
| 2015 | -8.8 | -9.0 |
| 2016 (OOS) | 15.8 | 16.3 |
| 2017 (OOS) | 16.3 | 16.5 |
| 2018 (OOS) | -7.1 | -8.2 |
| 2019 (OOS) | 18.8 | 17.9 |
| 2020 (OOS) | 5.3 | 5.2 |
| 2021 (OOS) | 27.5 | 28.0 |
| 2022 (OOS) | -10.3 | -13.2 |
| 2023 (OOS) | 8.9 | 5.4 |
| 2024 (OOS) | 22.4 | 22.1 |
| 2025 (OOS) | 7.7 | 6.5 |
| 2026 (OOS) | 2.7 | 1.1 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 38.5% from a peak in-sample and 30.4% out-of-sample, and the worst single trade cost 11.7% of the account out-of-sample. About 59 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 38.2% from a peak in-sample and 30.4% out-of-sample, and the worst single trade cost 11.7% of the account out-of-sample. About 59 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 609 | `{"k": 5, "max_candles": 126, "n": 357, "stop_loss_pct": 28}` | 13,142.71 | 5.6 | -38.2 | 59.8 | 13,783.92 | 8.3 | -30.4 | 1.49 | 234/207 | not checked |
| 619 | `{"k": 5, "max_candles": 126, "n": 357, "stop_loss_pct": 29}` | 13,142.71 | 5.6 | -38.2 | 59.8 | 13,783.92 | 8.3 | -30.4 | 1.49 | 234/207 | not checked |
| 639 | `{"k": 5, "max_candles": 126, "n": 357, "stop_loss_pct": 27}` | 13,142.71 | 5.6 | -38.2 | 59.8 | 13,783.92 | 8.3 | -30.4 | 1.49 | 234/207 | not checked |
| 637 | `{"k": 5, "max_candles": 210, "n": 336, "stop_loss_pct": 29}` | 12,130.76 | 5.3 | -37.9 | 57.8 | 15,518.53 | 9.0 | -30.4 | 1.71 | 204/191 | not checked |
| 745 | `{"k": 5, "max_candles": 210, "n": 336, "stop_loss_pct": 28}` | 12,130.76 | 5.3 | -37.9 | 57.8 | 15,518.53 | 9.0 | -30.4 | 1.71 | 204/191 | not checked |
| 749 | `{"k": 5, "max_candles": 210, "n": 336, "stop_loss_pct": 27}` | 12,130.76 | 5.3 | -37.9 | 57.8 | 15,518.53 | 9.0 | -30.4 | 1.71 | 204/191 | not checked |
| 567 | `{"k": 4, "max_candles": 147, "n": 378, "stop_loss_pct": 29}` | 11,436.04 | 5.0 | -36.3 | 56.7 | 15,217.26 | 8.9 | -30.4 | 1.76 | 215/193 | not checked |
| 681 | `{"k": 4, "max_candles": 147, "n": 378, "stop_loss_pct": 28}` | 11,436.04 | 5.0 | -36.3 | 56.7 | 15,217.26 | 8.9 | -30.4 | 1.76 | 215/193 | not checked |
| 791 | `{"k": 4, "max_candles": 147, "n": 378, "stop_loss_pct": 27}` | 11,436.04 | 5.0 | -36.3 | 56.7 | 15,217.26 | 8.9 | -30.4 | 1.76 | 215/193 | not checked |
| 931 | `{"k": 4, "max_candles": 147, "n": 378, "stop_loss_pct": 25}` | 11,436.04 | 5.0 | -36.3 | 56.7 | 15,217.26 | 8.9 | -30.4 | 1.76 | 215/193 | not checked |
| 946 | `{"k": 4, "max_candles": 147, "n": 378, "stop_loss_pct": 26}` | 11,436.04 | 5.0 | -36.3 | 56.7 | 15,217.26 | 8.9 | -30.4 | 1.76 | 215/193 | not checked |
| 520 | `{"k": 5, "max_candles": 147, "n": 336, "stop_loss_pct": 28}` | 11,379.29 | 5.0 | -33.8 | 58.3 | 15,389.20 | 8.9 | -30.4 | 1.78 | 223/198 | not checked |
| 672 | `{"k": 5, "max_candles": 147, "n": 336, "stop_loss_pct": 29}` | 11,379.29 | 5.0 | -33.8 | 58.3 | 15,389.20 | 8.9 | -30.4 | 1.78 | 223/198 | not checked |
| 739 | `{"k": 5, "max_candles": 147, "n": 336, "stop_loss_pct": 27}` | 11,379.29 | 5.0 | -33.8 | 58.3 | 15,389.20 | 8.9 | -30.4 | 1.78 | 223/198 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,060 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
