# monthly_loser_rebound_basket: optimization summary

Updated 2026-11-27T12:21:21Z · backtest.py version `8b81321b31` · 2,545 parameter sets tested with this version (2,545 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d bars)
- In-sample (tuning): 2000-07-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [monthly_loser_rebound_basket__max-income__v001.md](monthly_loser_rebound_basket__max-income__v001.md) | 2544 | `{"k": 5, "max_candles": 147, "stop_loss_pct": 28}` | long XLB since 2026-11-02 00:00 @ 53.245969; long XLF since 2026-09-01 00:00 @ 56.53762; long XLK since 2026-10-01 00:00 @ 196.929056; long XLRE since 2026-11-02 00:00 @ 43.172948; long XLY since 2026-11-02 00:00 @ 116.925066 |
| balanced | [monthly_loser_rebound_basket__balanced__v001.md](monthly_loser_rebound_basket__balanced__v001.md) | 2545 | `{"k": 5, "max_candles": 315, "stop_loss_pct": 28}` | long XLB since 2026-11-02 00:00 @ 53.245969; long XLF since 2026-09-01 00:00 @ 56.549908; long XLK since 2026-10-01 00:00 @ 196.929056; long XLRE since 2026-11-02 00:00 @ 43.172948; long XLY since 2026-11-02 00:00 @ 116.925066 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 12,004.78 | 14,487.53 | 11,334.05 | 14,686.85 |
| return % | 120.05 | 144.88 | 113.34 | 146.87 |
| return %/year | 5.2 | 8.6 | 5.0 | 8.7 |
| gross profit | 31,743.37 | 39,265.76 | 30,640.99 | 39,797.74 |
| gross loss | 19,738.59 | 24,778.23 | 19,306.94 | 25,110.89 |
| trades | 320 | 294 | 313 | 292 |
| win rate % | 65.0 | 62.6 | 64.9 | 62.3 |
| avg win | 152.61 | 213.40 | 150.94 | 218.67 |
| avg loss | -176.24 | -225.26 | -175.52 | -228.28 |
| avg result / trade | 37.51 | 49.28 | 36.21 | 50.30 |
| largest single loss | -1,723.46 | -2,079.58 | -1,659.56 | -2,099.02 |
| largest loss % of equity | -13.15 | -13.43 | -13.15 | -13.43 |
| max drawdown | -5,160.02 | -5,568.06 | -4,968.70 | -5,620.11 |
| max drawdown % | -34.34 | -31.40 | -38.86 | -31.40 |
| profit factor | 1.61 | 1.58 | 1.59 | 1.58 |
| unusually bad trades | 13 | 15 | 14 | 15 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 37.3 | 41.8 | 37.5 | 41.8 |
| buy & hold return % | 139.85 | 244.45 | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.64 |  | 1.73 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 10.2 | 10.2 |
| 2001 | -19.5 | -19.2 |
| 2002 | -15.3 | -18.9 |
| 2003 | 31.9 | 31.9 |
| 2004 | 18.7 | 18.7 |
| 2005 | 4.5 | 4.8 |
| 2006 | 11.0 | 11.0 |
| 2007 | 10.9 | 10.9 |
| 2008 | -24.9 | -24.9 |
| 2009 | 21.5 | 21.5 |
| 2010 | -3.7 | -3.7 |
| 2011 | 2.4 | 2.8 |
| 2012 | 9.5 | 9.8 |
| 2013 | 31.9 | 31.9 |
| 2014 | 17.0 | 17.0 |
| 2015 | -4.4 | -4.4 |
| 2016 (OOS) | 15.0 | 15.9 |
| 2017 (OOS) | 22.1 | 22.1 |
| 2018 (OOS) | -3.1 | -3.1 |
| 2019 (OOS) | 21.5 | 22.6 |
| 2020 (OOS) | 1.6 | 1.9 |
| 2021 (OOS) | 28.2 | 28.2 |
| 2022 (OOS) | -13.1 | -13.1 |
| 2023 (OOS) | 8.9 | 8.9 |
| 2024 (OOS) | 11.8 | 11.8 |
| 2025 (OOS) | 10.6 | 10.6 |
| 2026 (OOS) | -5.0 | -5.4 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 34.3% from a peak in-sample and 31.4% out-of-sample, and the worst single trade cost 13.4% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 29% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 38.9% from a peak in-sample and 31.4% out-of-sample, and the worst single trade cost 13.4% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1864 | `{"k": 5, "max_candles": 147, "stop_loss_pct": 29}` | 12,004.78 | 5.2 | -34.3 | 65.0 | 14,487.53 | 8.6 | -31.4 | 1.64 | 320/294 | not checked |
| 1867 | `{"k": 5, "max_candles": 147, "stop_loss_pct": 28}` | 12,004.78 | 5.2 | -34.3 | 65.0 | 14,487.53 | 8.6 | -31.4 | 1.64 | 320/294 | 1.00 |
| 1862 | `{"k": 6, "max_candles": 147, "stop_loss_pct": 28}` | 11,190.85 | 5.0 | -34.3 | 63.2 | 12,445.14 | 7.7 | -31.0 | 1.55 | 302/282 | not checked |
| 2416 | `{"k": 6, "max_candles": 147, "stop_loss_pct": 29}` | 11,190.85 | 5.0 | -34.3 | 63.2 | 12,445.14 | 7.7 | -31.0 | 1.55 | 302/282 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 2,545 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
