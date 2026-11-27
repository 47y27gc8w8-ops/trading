# equal_risk_contribution_trend: optimization summary

Updated 2026-11-27T12:16:00Z · backtest.py version `7bb330d3d9` · 788 parameter sets tested with this version (788 rows in results.csv in total) · last run ended: converged: no profile improved in the last 510 iterations at the smallest step size

## Setup

- Data: DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [equal_risk_contribution_trend__max-income__v001.md](equal_risk_contribution_trend__max-income__v001.md) | 175 | `{"max_candles": 294, "n": 126, "stop_loss_pct": 15.0}` | long DBC since 2026-10-01 00:00 @ 32.37971; long EFA since 2026-05-01 00:00 @ 102.370922; long SPY since 2026-05-01 00:00 @ 743.477975; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| balanced | [equal_risk_contribution_trend__balanced__v002.md](equal_risk_contribution_trend__balanced__v002.md) | 788 | `{"max_candles": 189, "n": 63, "stop_loss_pct": 13}` | long DBC since 2026-07-01 00:00 @ 27.864179; long EFA since 2026-10-01 00:00 @ 103.411011; long SPY since 2026-05-01 00:00 @ 746.135373; long VNQ since 2026-11-02 00:00 @ 94.148239 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 11,287.05 | 5,914.55 | 10,698.13 | 6,654.79 |
| return % | 112.87 | 59.15 | 106.98 | 66.55 |
| return %/year | 6.5 | 4.4 | 6.2 | 4.8 |
| gross profit | 19,867.67 | 15,160.69 | 20,375.00 | 17,063.60 |
| gross loss | 8,580.62 | 9,246.14 | 9,676.87 | 10,408.80 |
| trades | 102 | 107 | 126 | 128 |
| win rate % | 44.1 | 41.1 | 48.4 | 40.6 |
| avg win | 441.50 | 344.56 | 334.02 | 328.15 |
| avg loss | -150.54 | -146.76 | -148.87 | -136.96 |
| avg result / trade | 110.66 | 55.28 | 84.91 | 51.99 |
| largest single loss | -483.25 | -2,118.90 | -526.13 | -783.50 |
| largest loss % of equity | -2.34 | -12.91 | -2.55 | -4.37 |
| max drawdown | -2,367.24 | -5,440.93 | -1,909.91 | -4,728.61 |
| max drawdown % | -14.28 | -30.14 | -11.84 | -25.99 |
| profit factor | 2.31 | 1.64 | 2.11 | 1.64 |
| unusually bad trades | 6 | 7 | 6 | 9 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 64.0 | 64.4 | 61.0 | 62.8 |
| buy & hold return % | 98.52 | 132.14 | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.67 |  | 0.77 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2004 | 4.4 | 1.3 |
| 2005 | 11.3 | 8.0 |
| 2006 | 12.4 | 12.5 |
| 2007 | 10.2 | 9.0 |
| 2008 | 13.5 | 15.6 |
| 2009 | 2.6 | 4.3 |
| 2010 | 6.7 | 6.4 |
| 2011 | 6.7 | 6.5 |
| 2012 | 4.5 | 4.5 |
| 2013 | 5.0 | 9.4 |
| 2014 | 3.6 | 2.7 |
| 2015 | -1.7 | -3.7 |
| 2016 (OOS) | 1.1 | 3.0 |
| 2017 (OOS) | 12.7 | 11.3 |
| 2018 (OOS) | -2.8 | -2.1 |
| 2019 (OOS) | 11.7 | 11.9 |
| 2020 (OOS) | 11.8 | 13.3 |
| 2021 (OOS) | 18.8 | 16.4 |
| 2022 (OOS) | -24.8 | -20.6 |
| 2023 (OOS) | 3.9 | 4.8 |
| 2024 (OOS) | 6.6 | 4.3 |
| 2025 (OOS) | 13.7 | 15.5 |
| 2026 (OOS) | -1.4 | -2.9 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 14.3% from a peak in-sample and 30.1% out-of-sample, and the worst single trade cost 12.9% of the account out-of-sample. About 44 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 33% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 11.8% from a peak in-sample and 26.0% out-of-sample, and the worst single trade cost 4.4% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 455 | `{"max_candles": 189, "n": 63, "stop_loss_pct": 20}` | 11,545.70 | 6.6 | -11.8 | 50.0 | 7,217.48 | 5.1 | -26.0 | 0.78 | 122/127 | not checked |
| 407 | `{"max_candles": 189, "n": 42, "stop_loss_pct": 20}` | 10,948.41 | 6.4 | -11.8 | 50.0 | 7,549.55 | 5.3 | -26.4 | 0.83 | 122/127 | not checked |
| 383 | `{"max_candles": 189, "n": 42, "stop_loss_pct": 19}` | 10,853.82 | 6.3 | -11.7 | 50.0 | 7,549.55 | 5.3 | -26.4 | 0.84 | 122/127 | not checked |
| 387 | `{"max_candles": 189, "n": 42, "stop_loss_pct": 18}` | 10,741.60 | 6.3 | -11.5 | 50.0 | 7,549.55 | 5.3 | -26.4 | 0.84 | 122/127 | not checked |
| 359 | `{"max_candles": 189, "n": 42, "stop_loss_pct": 17}` | 10,514.25 | 6.2 | -11.4 | 49.6 | 7,549.55 | 5.3 | -26.4 | 0.86 | 123/127 | not checked |
| 341 | `{"max_candles": 189, "n": 42, "stop_loss_pct": 15}` | 10,390.55 | 6.1 | -11.1 | 49.2 | 7,280.44 | 5.2 | -26.4 | 0.84 | 124/127 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 788 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
