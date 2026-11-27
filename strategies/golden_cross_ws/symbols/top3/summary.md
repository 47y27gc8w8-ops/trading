# golden_cross_ws__top3: optimization summary

Updated 2026-11-23T22:12:00Z · backtest.py version `f9a10d6bde` · 756 parameter sets tested with this version (756 rows in results.csv in total) · last run ended: converged: no profile improved in the last 510 iterations at the smallest step size

## Setup

- Data: QQQ, XLY, XLI (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-20
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 5 in-sample and ≥ 2 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross_ws__top3__max-income__v002.md](golden_cross_ws__top3__max-income__v002.md) | 755 | `{"fast": 120, "slow": 320, "trailing_stop_pct": 0}` | long QQQ since 2023-06-05 00:00 @ 347.612546; long XLI since 2023-03-07 00:00 @ 98.081294 |
| balanced | [golden_cross_ws__top3__balanced__v001.md](golden_cross_ws__top3__balanced__v001.md) | 185 | `{"fast": 75, "slow": 170, "trailing_stop_pct": 10}` | flat (data up to 2026-11-23 00:00) |
| safe-starter | [golden_cross_ws__top3__safe-starter__v002.md](golden_cross_ws__top3__safe-starter__v002.md) | 756 | `{"fast": 80, "slow": 270, "trailing_stop_pct": 10}` | flat (data up to 2026-11-23 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 25,893.58 | 18,550.72 | 11,582.24 | 6,081.91 | 4,097.53 | 6,119.59 |
| return % | 258.94 | 185.51 | 115.82 | 60.82 | 40.98 | 61.20 |
| return %/year | 8.4 | 10.1 | 5.0 | 4.5 | 2.2 | 4.5 |
| gross profit | 26,326.37 | 19,060.00 | 14,186.39 | 7,199.68 | 5,439.72 | 6,708.33 |
| gross loss | 432.79 | 509.29 | 2,604.16 | 1,117.77 | 1,342.19 | 588.75 |
| trades | 14 | 11 | 32 | 18 | 19 | 13 |
| win rate % | 85.7 | 90.9 | 56.2 | 66.7 | 63.2 | 76.9 |
| avg win | 2,193.86 | 1,906.00 | 788.13 | 599.97 | 453.31 | 670.83 |
| avg loss | -216.39 | -509.29 | -186.01 | -186.29 | -191.74 | -196.25 |
| avg result / trade | 1,849.54 | 1,686.43 | 361.94 | 337.88 | 215.66 | 470.74 |
| largest single loss | -363.36 | -509.29 | -340.29 | -438.52 | -438.68 | -425.28 |
| largest loss % of equity | -10.28 | -12.78 | -10.75 | -9.85 | -7.84 | -8.75 |
| max drawdown | -4,378.13 | -7,264.74 | -1,961.57 | -2,897.80 | -1,531.65 | -2,573.18 |
| max drawdown % | -19.73 | -33.40 | -14.83 | -19.28 | -9.80 | -16.98 |
| profit factor | 60.83 | 37.42 | 5.45 | 6.44 | 4.05 | 11.39 |
| unusually bad trades | 0 | 0 | 1 | 2 | 1 | 1 |
| … threshold (% of equity) | 12.1 | 25.6 | 9.7 | 4.6 | 9.2 | 5.0 |
| time in market % | 70.4 | 81.7 | 41.1 | 39.7 | 25.1 | 34.7 |
| buy & hold return % | 159.88 | 329.73 | 159.88 | 329.73 | 159.88 | 329.73 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.21 |  | 0.90 |  | 2.05 |
| period | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 3.0 | -0.0 | -0.2 |
| 2001 | -0.2 | -4.3 | 1.0 |
| 2002 | -2.9 | -6.3 | -1.2 |
| 2003 | 17.3 | 29.5 | 19.5 |
| 2004 | 13.7 | 4.6 | 3.8 |
| 2005 | -0.5 | -4.2 | -6.2 |
| 2006 | 7.5 | -0.7 | 0.5 |
| 2007 | 6.7 | 3.6 | 0.5 |
| 2008 | -4.0 | -0.9 | 0.0 |
| 2009 | 8.1 | 21.6 | 14.1 |
| 2010 | 25.2 | 11.1 | 5.9 |
| 2011 | 0.4 | 0.4 | 0.0 |
| 2012 | 12.0 | 4.0 | -0.3 |
| 2013 | 39.9 | 28.6 | 0.0 |
| 2014 | 13.0 | 0.0 | 0.0 |
| 2015 | 2.5 | 0.4 | 0.0 |
| 2016 (OOS) | 5.7 | 6.5 | 10.1 |
| 2017 (OOS) | 26.6 | 27.3 | 26.5 |
| 2018 (OOS) | -3.8 | -6.5 | -1.9 |
| 2019 (OOS) | 22.4 | -0.0 | 0.8 |
| 2020 (OOS) | 20.1 | 4.6 | 6.7 |
| 2021 (OOS) | 26.4 | 8.9 | 7.0 |
| 2022 (OOS) | -24.5 | -4.7 | -3.5 |
| 2023 (OOS) | 12.1 | 6.6 | 5.7 |
| 2024 (OOS) | 24.1 | 0.0 | 0.0 |
| 2025 (OOS) | 16.6 | 6.9 | 3.5 |
| 2026 (OOS) | -1.5 | -1.7 | -2.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 19.7% from a peak in-sample and 33.4% out-of-sample, and the worst single trade cost 12.8% of the account out-of-sample. About 86 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 14.8% from a peak in-sample and 19.3% out-of-sample, and the worst single trade cost 9.8% of the account out-of-sample. About 56 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 52% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 9.8% from a peak in-sample and 17.0% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 63 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 59% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 313 | `{"fast": 130, "slow": 350, "trailing_stop_pct": 0}` | 26,694.89 | 8.6 | -19.4 | 90.0 | 16,251.23 | 9.3 | -26.1 | 1.08 | 10/7 | not checked |
| 476 | `{"fast": 20, "slow": 290, "trailing_stop_pct": 0}` | 18,673.40 | 6.9 | -19.0 | 50.0 | 15,140.83 | 8.8 | -29.2 | 1.28 | 30/22 | not checked |
| 399 | `{"fast": 75, "slow": 240, "trailing_stop_pct": 21}` | 17,073.42 | 6.5 | -17.9 | 65.0 | 8,576.06 | 5.9 | -24.9 | 0.90 | 20/13 | not checked |
| 335 | `{"fast": 70, "slow": 240, "trailing_stop_pct": 21}` | 16,527.55 | 6.4 | -17.9 | 55.0 | 9,002.17 | 6.1 | -23.6 | 0.96 | 20/14 | not checked |
| 423 | `{"fast": 70, "slow": 210, "trailing_stop_pct": 15}` | 16,179.79 | 6.3 | -14.6 | 55.2 | 11,372.28 | 7.2 | -20.9 | 1.15 | 29/16 | not checked |
| 370 | `{"fast": 70, "slow": 210, "trailing_stop_pct": 14}` | 15,286.21 | 6.0 | -14.5 | 51.7 | 11,991.52 | 7.5 | -19.7 | 1.24 | 29/16 | not checked |
| 735 | `{"fast": 55, "slow": 230, "trailing_stop_pct": 14}` | 15,257.96 | 6.0 | -13.8 | 59.3 | 14,023.00 | 8.4 | -16.9 | 1.39 | 27/16 | not checked |
| 606 | `{"fast": 85, "slow": 220, "trailing_stop_pct": 14}` | 14,253.01 | 5.8 | -13.6 | 52.0 | 10,722.08 | 6.9 | -20.8 | 1.20 | 25/14 | not checked |
| 262 | `{"fast": 65, "slow": 250, "trailing_stop_pct": 14}` | 14,152.94 | 5.7 | -13.5 | 54.5 | 11,573.94 | 7.3 | -18.3 | 1.28 | 22/15 | not checked |
| 522 | `{"fast": 55, "slow": 230, "trailing_stop_pct": 11}` | 12,045.66 | 5.1 | -13.1 | 59.3 | 7,335.77 | 5.2 | -14.6 | 1.01 | 27/16 | not checked |
| 372 | `{"fast": 60, "slow": 230, "trailing_stop_pct": 11}` | 11,313.37 | 4.9 | -12.5 | 55.2 | 6,705.82 | 4.8 | -16.2 | 0.99 | 29/16 | not checked |
| 404 | `{"fast": 55, "slow": 230, "trailing_stop_pct": 10}` | 9,884.39 | 4.4 | -11.8 | 59.3 | 8,156.37 | 5.6 | -13.3 | 1.27 | 27/16 | not checked |
| 350 | `{"fast": 60, "slow": 230, "trailing_stop_pct": 10}` | 9,161.04 | 4.2 | -10.7 | 55.2 | 7,496.01 | 5.3 | -14.9 | 1.26 | 29/16 | not checked |
| 584 | `{"fast": 75, "slow": 250, "trailing_stop_pct": 11}` | 8,487.29 | 4.0 | -10.5 | 68.4 | 5,743.75 | 4.3 | -17.7 | 1.08 | 19/14 | not checked |
| 671 | `{"fast": 70, "slow": 290, "trailing_stop_pct": 10}` | 5,283.97 | 2.7 | -10.3 | 66.7 | 5,541.25 | 4.1 | -15.3 | 1.52 | 18/11 | not checked |
| 504 | `{"fast": 75, "slow": 260, "trailing_stop_pct": 10}` | 4,993.94 | 2.6 | -9.5 | 68.4 | 6,105.22 | 4.5 | -16.3 | 1.73 | 19/14 | not checked |
| 665 | `{"fast": 80, "slow": 280, "trailing_stop_pct": 8}` | 3,061.99 | 1.7 | -8.2 | 72.2 | 3,680.77 | 2.9 | -14.5 | 1.72 | 18/11 | not checked |
| 705 | `{"fast": 75, "slow": 280, "trailing_stop_pct": 8}` | 3,043.75 | 1.7 | -7.5 | 68.4 | 4,206.41 | 3.3 | -15.3 | 1.94 | 19/12 | not checked |
| 258 | `{"fast": 65, "slow": 270, "trailing_stop_pct": 6}` | 1,513.17 | 0.9 | -5.6 | 55.0 | 546.12 | 0.5 | -7.3 | 0.55 | 20/12 | not checked |
| 122 | `{"fast": 50, "slow": 210, "trailing_stop_pct": 3}` | 905.88 | 0.6 | -4.7 | 35.3 | 673.65 | 0.6 | -5.3 | 1.09 | 34/19 | not checked |
| 43 | `{"fast": 80, "slow": 280, "trailing_stop_pct": 4}` | 898.29 | 0.5 | -3.6 | 33.3 | 595.69 | 0.5 | -6.1 | 0.98 | 18/11 | not checked |
| 670 | `{"fast": 120, "slow": 300, "trailing_stop_pct": 2}` | 848.59 | 0.5 | -1.8 | 56.2 | 232.43 | 0.2 | -1.4 | 0.40 | 16/11 | not checked |
| 243 | `{"fast": 120, "slow": 320, "trailing_stop_pct": 1}` | 412.91 | 0.3 | -1.2 | 57.1 | 173.43 | 0.2 | -1.1 | 0.61 | 14/11 | not checked |
| 376 | `{"fast": 135, "slow": 340, "trailing_stop_pct": 1}` | 42.52 | 0.0 | -1.1 | 54.5 | 65.76 | 0.1 | -1.4 | 2.00 | 11/8 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 756 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
