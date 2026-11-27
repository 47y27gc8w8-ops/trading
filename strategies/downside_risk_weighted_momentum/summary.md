# downside_risk_weighted_momentum: optimization summary

Updated 2026-11-27T11:47:16Z · backtest.py version `fa213e948c` · 843 parameter sets tested with this version (843 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [downside_risk_weighted_momentum__max-income__v001.md](downside_risk_weighted_momentum__max-income__v001.md) | 239 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 25}` | long DBC since 2026-03-02 00:00 @ 27.054976; long EFA since 2026-11-02 00:00 @ 103.721109; long SPY since 2026-08-03 00:00 @ 751.144243 |
| balanced | [downside_risk_weighted_momentum__balanced__v002.md](downside_risk_weighted_momentum__balanced__v002.md) | 843 | `{"k": 6, "max_candles": 462, "n": 252, "stop_loss_pct": 14}` | long DBC since 2025-08-01 00:00 @ 24.529351; long EEM since 2026-02-02 00:00 @ 59.679946; long EFA since 2025-04-01 00:00 @ 87.79945; long SPY since 2025-04-01 00:00 @ 646.671852; long VNQ since 2026-05-01 00:00 @ 94.653985 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 26,397.77 | 15,229.96 | 14,626.17 | 3,848.16 |
| return % | 263.98 | 152.30 | 146.26 | 38.48 |
| return %/year | 11.4 | 8.9 | 7.8 | 3.0 |
| gross profit | 40,402.30 | 24,798.64 | 20,031.38 | 9,597.20 |
| gross loss | 14,004.53 | 9,568.68 | 5,405.21 | 5,749.04 |
| trades | 99 | 89 | 77 | 68 |
| win rate % | 61.6 | 59.5 | 57.1 | 44.1 |
| avg win | 662.33 | 467.90 | 455.26 | 319.91 |
| avg loss | -368.54 | -265.80 | -163.79 | -151.29 |
| avg result / trade | 266.64 | 171.12 | 189.95 | 56.59 |
| largest single loss | -1,941.76 | -782.13 | -566.76 | -712.74 |
| largest loss % of equity | -4.70 | -4.06 | -2.58 | -5.94 |
| max drawdown | -8,771.82 | -5,286.49 | -2,168.08 | -3,491.07 |
| max drawdown % | -19.80 | -25.72 | -12.52 | -27.96 |
| profit factor | 2.88 | 2.59 | 3.71 | 1.67 |
| unusually bad trades | 8 | 4 | 4 | 7 |
| … threshold (% of equity) | 2.0 | 3.0 | 2.0 | 2.0 |
| time in market % | 35.5 | 34.9 | 60.5 | 58.9 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.78 |  | 0.39 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 7.7 | 9.0 |
| 2005 | 9.9 | 8.4 |
| 2006 | 18.2 | 14.6 |
| 2007 | 22.1 | 11.9 |
| 2008 | 25.7 | 16.7 |
| 2009 | 5.0 | -0.9 |
| 2010 | 14.2 | 5.3 |
| 2011 | 19.6 | 4.6 |
| 2012 | 8.0 | 8.3 |
| 2013 | 16.0 | 9.0 |
| 2014 | 9.0 | 10.4 |
| 2015 | -13.3 | -2.0 |
| 2016 (OOS) | 12.2 | -2.0 |
| 2017 (OOS) | 20.1 | 17.5 |
| 2018 (OOS) | 0.1 | -18.6 |
| 2019 (OOS) | -0.1 | 11.5 |
| 2020 (OOS) | 17.4 | 5.9 |
| 2021 (OOS) | 25.6 | 10.3 |
| 2022 (OOS) | -20.1 | -21.1 |
| 2023 (OOS) | 8.6 | 4.7 |
| 2024 (OOS) | 11.0 | 7.4 |
| 2025 (OOS) | 21.7 | 20.3 |
| 2026 (OOS) | 11.0 | 4.5 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 19.8% from a peak in-sample and 25.7% out-of-sample, and the worst single trade cost 4.1% of the account out-of-sample. About 62 of every 100 trades won in-sample. With 100% of equity per trade; about 39% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 12.5% from a peak in-sample and 28.0% out-of-sample, and the worst single trade cost 5.9% of the account out-of-sample. About 57 of every 100 trades won in-sample. Out-of-sample it earned 3.0% a year against 7.8% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 115 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 24}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,278.84 | 8.9 | -25.7 | 0.78 | 99/89 | not checked |
| 118 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 25}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,229.96 | 8.9 | -25.7 | 0.78 | 99/89 | 1.00 |
| 426 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 23}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,280.57 | 8.9 | -25.7 | 0.78 | 99/89 | not checked |
| 448 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 22}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,376.60 | 8.9 | -25.7 | 0.79 | 99/89 | not checked |
| 463 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 26}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,543.73 | 9.0 | -25.7 | 0.79 | 99/89 | not checked |
| 750 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 27}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,543.73 | 9.0 | -25.7 | 0.79 | 99/89 | not checked |
| 787 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 28}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,543.73 | 9.0 | -25.7 | 0.79 | 99/89 | not checked |
| 807 | `{"k": 3, "max_candles": 273, "n": 126, "stop_loss_pct": 29}` | 26,397.77 | 11.4 | -19.8 | 61.6 | 15,543.73 | 9.0 | -25.7 | 0.79 | 99/89 | not checked |
| 349 | `{"k": 4, "max_candles": 147, "n": 126, "stop_loss_pct": 19}` | 24,637.47 | 10.9 | -17.2 | 60.0 | 12,839.69 | 7.9 | -24.4 | 0.72 | 125/115 | not checked |
| 551 | `{"k": 4, "max_candles": 147, "n": 126, "stop_loss_pct": 20}` | 24,637.47 | 10.9 | -17.2 | 60.0 | 12,712.45 | 7.8 | -24.4 | 0.72 | 125/115 | not checked |
| 458 | `{"k": 4, "max_candles": 441, "n": 252, "stop_loss_pct": 18}` | 23,529.77 | 10.6 | -15.4 | 67.7 | 5,035.50 | 3.8 | -29.1 | 0.36 | 68/67 | not checked |
| 502 | `{"k": 4, "max_candles": 210, "n": 168, "stop_loss_pct": 21}` | 21,168.53 | 9.9 | -14.7 | 61.4 | 14,774.72 | 8.7 | -18.9 | 0.87 | 101/85 | not checked |
| 410 | `{"k": 4, "max_candles": 231, "n": 168, "stop_loss_pct": 21}` | 20,004.56 | 9.6 | -13.9 | 60.6 | 17,063.75 | 9.6 | -17.9 | 1.00 | 99/79 | not checked |
| 532 | `{"k": 4, "max_candles": 189, "n": 168, "stop_loss_pct": 21}` | 17,901.24 | 8.9 | -12.2 | 60.6 | 16,277.74 | 9.3 | -17.1 | 1.04 | 104/89 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 843 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
