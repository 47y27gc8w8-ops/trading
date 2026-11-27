# single_etf_volatility_target: optimization summary

Updated 2026-11-27T12:33:06Z · backtest.py version `e2f6a72d5f` · 12,688 parameter sets tested with this version (12,688 rows in results.csv in total) · last run ended: no untested valid parameter sets left to try

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1994-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 10 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [single_etf_volatility_target__max-income__v002.md](single_etf_volatility_target__max-income__v002.md) | 12686 | `{"max_candles": 441, "stop_loss_pct": 7, "target": 0.28}` | long SPY since 2026-05-01 00:00 @ 717.829936 |
| balanced | [single_etf_volatility_target__balanced__v002.md](single_etf_volatility_target__balanced__v002.md) | 12687 | `{"max_candles": 210, "stop_loss_pct": 13, "target": 0.03}` | long SPY since 2026-05-01 00:00 @ 730.640981 |
| safe-starter | [single_etf_volatility_target__safe-starter__v002.md](single_etf_volatility_target__safe-starter__v002.md) | 12688 | `{"max_candles": 315, "stop_loss_pct": 7, "target": 0.03}` | long SPY since 2026-05-01 00:00 @ 730.640981 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 85,991.30 | 13,363.51 | 6,199.05 | 2,484.93 | 5,739.27 | 2,660.42 |
| return % | 859.91 | 133.64 | 61.99 | 24.85 | 57.39 | 26.60 |
| return %/year | 10.8 | 8.1 | 2.2 | 2.1 | 2.1 | 2.2 |
| gross profit | 91,731.19 | 17,115.72 | 7,525.40 | 3,348.15 | 6,397.13 | 3,437.87 |
| gross loss | 5,739.89 | 3,752.21 | 1,326.35 | 863.22 | 657.86 | 777.45 |
| trades | 16 | 12 | 25 | 16 | 19 | 13 |
| win rate % | 68.8 | 66.7 | 72.0 | 50.0 | 79.0 | 46.1 |
| avg win | 8,339.20 | 2,139.47 | 418.08 | 418.52 | 426.48 | 572.98 |
| avg loss | -1,147.98 | -938.05 | -189.48 | -107.90 | -164.46 | -111.06 |
| avg result / trade | 5,374.46 | 1,113.63 | 247.96 | 155.31 | 302.07 | 204.65 |
| largest single loss | -1,752.33 | -1,326.35 | -357.98 | -261.97 | -270.16 | -185.09 |
| largest loss % of equity | -7.12 | -7.12 | -3.58 | -2.28 | -2.70 | -1.54 |
| max drawdown | -11,183.50 | -5,200.89 | -404.13 | -601.82 | -558.89 | -653.39 |
| max drawdown % | -17.31 | -25.41 | -4.04 | -5.00 | -3.87 | -5.36 |
| profit factor | 15.98 | 4.56 | 5.67 | 3.88 | 9.72 | 4.42 |
| unusually bad trades | 0 | 0 | 1 | 1 | 0 | 0 |
| … threshold (% of equity) | 11.3 | 14.2 | 2.5 | 2.0 | 2.9 | 2.0 |
| time in market % | 73.8 | 81.3 | 70.5 | 80.5 | 73.3 | 79.7 |
| buy & hold return % | 555.68 | 328.39 | 555.68 | 328.39 | 555.68 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.75 |  | 0.93 |  | 1.05 |
| period | 1994-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1994-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1994-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 1994 | -7.3 | -3.5 | -2.6 |
| 1995 | 37.5 | 12.4 | 12.1 |
| 1996 | 22.4 | 5.7 | 3.5 |
| 1997 | 33.5 | 4.1 | 5.1 |
| 1998 | 21.4 | 0.6 | 1.1 |
| 1999 | 12.7 | 2.2 | 1.6 |
| 2000 | -1.1 | -0.8 | -0.6 |
| 2001 | 0.0 | 0.0 | 0.0 |
| 2002 | -5.6 | -1.0 | -1.0 |
| 2003 | 22.4 | 4.1 | 4.1 |
| 2004 | 10.7 | 3.5 | 2.5 |
| 2005 | 4.4 | 0.4 | 0.9 |
| 2006 | 15.5 | 3.5 | 4.5 |
| 2007 | 5.1 | 0.8 | 0.1 |
| 2008 | 0.1 | 0.0 | 0.0 |
| 2009 | 21.0 | 2.9 | 2.9 |
| 2010 | 7.2 | 1.1 | 1.3 |
| 2011 | -1.9 | 0.8 | -0.1 |
| 2012 | 13.8 | 1.9 | 1.8 |
| 2013 | 25.9 | 6.3 | 7.1 |
| 2014 | 13.5 | 4.3 | 4.2 |
| 2015 | 1.6 | 0.5 | -1.7 |
| 2016 (OOS) | 9.1 | 2.4 | 2.4 |
| 2017 (OOS) | 22.4 | 7.9 | 8.1 |
| 2018 (OOS) | -4.7 | 1.5 | 2.4 |
| 2019 (OOS) | 7.7 | 0.9 | 0.9 |
| 2020 (OOS) | 13.3 | 0.2 | 0.2 |
| 2021 (OOS) | 28.7 | 5.7 | 5.8 |
| 2022 (OOS) | -21.0 | -4.2 | -4.5 |
| 2023 (OOS) | 9.3 | 1.6 | 1.5 |
| 2024 (OOS) | 24.9 | 5.7 | 5.8 |
| 2025 (OOS) | 10.4 | 2.4 | 2.9 |
| 2026 (OOS) | -3.4 | -1.4 | -1.4 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.3% from a peak in-sample and 25.4% out-of-sample, and the worst single trade cost 7.1% of the account out-of-sample. About 69 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 39% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 4.0% from a peak in-sample and 5.0% out-of-sample, and the worst single trade cost 2.3% of the account out-of-sample. About 72 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **safe-starter**: Risk looks low: the account fell up to 3.9% from a peak in-sample and 5.4% out-of-sample, and the worst single trade cost 1.5% of the account out-of-sample. About 79 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5690 | `{"max_candles": 441, "stop_loss_pct": 7, "target": 0.3}` | 86,269.58 | 10.8 | -17.3 | 68.8 | 13,562.57 | 8.2 | -25.4 | 0.76 | 16/12 | not checked |
| 5829 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.3}` | 77,726.16 | 10.4 | -15.4 | 68.0 | 12,658.45 | 7.8 | -27.6 | 0.75 | 25/16 | not checked |
| 8330 | `{"max_candles": 189, "stop_loss_pct": 5, "target": 0.23}` | 64,117.73 | 9.5 | -15.3 | 58.6 | 10,299.64 | 6.7 | -23.6 | 0.70 | 29/20 | not checked |
| 5632 | `{"max_candles": 147, "stop_loss_pct": 8, "target": 0.3}` | 63,400.16 | 9.5 | -14.9 | 63.6 | 12,556.20 | 7.8 | -29.2 | 0.82 | 33/21 | not checked |
| 5921 | `{"max_candles": 126, "stop_loss_pct": 5, "target": 0.3}` | 60,271.64 | 9.3 | -14.7 | 66.7 | 8,134.74 | 5.6 | -24.2 | 0.61 | 39/25 | not checked |
| 972 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.15}` | 57,005.80 | 9.0 | -14.1 | 68.0 | 11,635.49 | 7.3 | -22.4 | 0.81 | 25/16 | not checked |
| 5928 | `{"max_candles": 126, "stop_loss_pct": 6, "target": 0.3}` | 56,456.37 | 9.0 | -13.9 | 66.7 | 7,488.49 | 5.3 | -28.1 | 0.59 | 39/25 | not checked |
| 5153 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.14}` | 54,363.16 | 8.8 | -13.2 | 68.0 | 11,382.91 | 7.2 | -21.5 | 0.82 | 25/16 | not checked |
| 4403 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.13}` | 50,751.29 | 8.6 | -12.3 | 68.0 | 10,990.99 | 7.0 | -20.3 | 0.82 | 25/16 | not checked |
| 305 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.12}` | 46,276.68 | 8.2 | -11.4 | 68.0 | 10,441.66 | 6.8 | -18.8 | 0.83 | 25/16 | not checked |
| 1023 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.11}` | 40,935.70 | 7.7 | -11.2 | 68.0 | 9,687.55 | 6.4 | -17.4 | 0.84 | 25/16 | not checked |
| 4453 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.1}` | 35,568.19 | 7.1 | -10.9 | 68.0 | 8,758.87 | 6.0 | -15.9 | 0.83 | 25/16 | not checked |
| 6252 | `{"max_candles": 189, "stop_loss_pct": 5, "target": 0.1}` | 32,299.04 | 6.8 | -10.8 | 58.6 | 6,302.50 | 4.6 | -16.8 | 0.68 | 29/20 | not checked |
| 1533 | `{"max_candles": 210, "stop_loss_pct": 12, "target": 0.09}` | 30,097.83 | 6.5 | -10.8 | 72.0 | 7,941.33 | 5.5 | -14.4 | 0.85 | 25/16 | not checked |
| 3700 | `{"max_candles": 210, "stop_loss_pct": 8, "target": 0.09}` | 28,866.95 | 6.4 | -10.7 | 69.2 | 7,874.20 | 5.5 | -16.6 | 0.86 | 26/16 | not checked |
| 9072 | `{"max_candles": 189, "stop_loss_pct": 5, "target": 0.09}` | 27,071.04 | 6.1 | -9.8 | 62.1 | 5,644.24 | 4.2 | -16.9 | 0.68 | 29/20 | not checked |
| 525 | `{"max_candles": 210, "stop_loss_pct": 8, "target": 0.08}` | 24,141.15 | 5.7 | -9.5 | 69.2 | 7,143.52 | 5.1 | -14.8 | 0.89 | 26/16 | not checked |
| 8771 | `{"max_candles": 189, "stop_loss_pct": 5, "target": 0.08}` | 22,734.81 | 5.5 | -8.8 | 62.1 | 5,086.85 | 3.9 | -16.3 | 0.69 | 29/20 | not checked |
| 495 | `{"max_candles": 210, "stop_loss_pct": 8, "target": 0.07}` | 19,665.70 | 5.1 | -8.3 | 69.2 | 6,319.96 | 4.6 | -13.1 | 0.91 | 26/16 | not checked |
| 9613 | `{"max_candles": 189, "stop_loss_pct": 5, "target": 0.07}` | 18,630.16 | 4.9 | -7.7 | 62.1 | 4,458.21 | 3.4 | -15.5 | 0.70 | 29/20 | not checked |
| 948 | `{"max_candles": 441, "stop_loss_pct": 8, "target": 0.06}` | 16,701.06 | 4.6 | -7.7 | 75.0 | 5,115.88 | 3.9 | -12.9 | 0.85 | 16/12 | not checked |
| 424 | `{"max_candles": 210, "stop_loss_pct": 8, "target": 0.06}` | 15,510.85 | 4.3 | -7.2 | 69.2 | 5,390.65 | 4.0 | -11.3 | 0.93 | 26/16 | not checked |
| 9796 | `{"max_candles": 189, "stop_loss_pct": 5, "target": 0.06}` | 14,754.52 | 4.2 | -6.6 | 62.1 | 3,874.81 | 3.0 | -13.6 | 0.72 | 29/20 | not checked |
| 5419 | `{"max_candles": 441, "stop_loss_pct": 8, "target": 0.05}` | 12,748.16 | 3.8 | -6.4 | 75.0 | 4,205.88 | 3.3 | -10.9 | 0.86 | 16/12 | not checked |
| 3050 | `{"max_candles": 210, "stop_loss_pct": 8, "target": 0.05}` | 11,901.00 | 3.6 | -6.0 | 69.2 | 4,416.34 | 3.4 | -9.5 | 0.94 | 26/16 | 1.00 |

(13 more on the front, see results.csv)


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 12,688 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
