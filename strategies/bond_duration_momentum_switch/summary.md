# bond_duration_momentum_switch: optimization summary

Updated 2026-11-24T22:30:16Z · backtest.py version `430dea9a89` · 15,069 parameter sets tested with this version (15,069 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: SHY, IEF, TLT (etf, 1d bars)
- In-sample (tuning): 2003-07-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [bond_duration_momentum_switch__max-income__v001.md](bond_duration_momentum_switch__max-income__v001.md) | 15068 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 8}` | long SHY since 2026-07-01 00:00 @ 80.896816 |
| balanced | [bond_duration_momentum_switch__balanced__v001.md](bond_duration_momentum_switch__balanced__v001.md) | 15069 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 22}` | long SHY since 2026-11-02 00:00 @ 81.474432 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 9,670.36 | 1,638.17 | 6,449.02 | 1,923.73 |
| return % | 96.70 | 16.38 | 64.49 | 19.24 |
| return %/year | 5.6 | 1.4 | 4.1 | 1.6 |
| gross profit | 16,499.64 | 5,646.55 | 12,701.81 | 8,408.41 |
| gross loss | 6,829.28 | 4,008.38 | 6,252.78 | 6,484.68 |
| trades | 49 | 41 | 46 | 42 |
| win rate % | 44.9 | 56.1 | 50.0 | 42.9 |
| avg win | 749.98 | 245.50 | 552.25 | 467.13 |
| avg loss | -252.94 | -222.69 | -271.86 | -270.19 |
| avg result / trade | 197.35 | 39.96 | 140.20 | 45.80 |
| largest single loss | -1,434.56 | -629.41 | -1,209.97 | -1,214.77 |
| largest loss % of equity | -8.12 | -4.92 | -7.77 | -8.76 |
| max drawdown | -4,508.81 | -3,020.73 | -3,194.72 | -3,302.36 |
| max drawdown % | -22.62 | -21.11 | -19.87 | -22.02 |
| profit factor | 2.42 | 1.41 | 2.03 | 1.30 |
| unusually bad trades | 9 | 2 | 9 | 10 |
| … threshold (% of equity) | 2.0 | 3.6 | 2.0 | 2.0 |
| time in market % | 88.0 | 78.9 | 86.8 | 81.8 |
| buy & hold return % | 74.67 | 7.48 | 74.67 | 7.48 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.25 |  | 0.40 |
| period | 2003-07-01 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2003-07-01 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2003 | 0.6 | 2.9 |
| 2004 | 4.2 | 0.4 |
| 2005 | 8.1 | 3.3 |
| 2006 | 1.4 | -0.4 |
| 2007 | 6.5 | 6.6 |
| 2008 | 29.0 | 26.9 |
| 2009 | -16.3 | -17.5 |
| 2010 | 10.2 | 4.4 |
| 2011 | 34.5 | 35.3 |
| 2012 | -7.2 | -6.5 |
| 2013 | -13.3 | -11.5 |
| 2014 | 19.6 | 22.3 |
| 2015 | 4.5 | -2.9 |
| 2016 (OOS) | 4.0 | 4.8 |
| 2017 (OOS) | 5.3 | 5.2 |
| 2018 (OOS) | -5.6 | -4.5 |
| 2019 (OOS) | 16.1 | 18.6 |
| 2020 (OOS) | 10.3 | 12.4 |
| 2021 (OOS) | -1.7 | 3.1 |
| 2022 (OOS) | -6.1 | -1.3 |
| 2023 (OOS) | -1.0 | -2.3 |
| 2024 (OOS) | -5.2 | -15.7 |
| 2025 (OOS) | 3.0 | 3.1 |
| 2026 (OOS) | -0.9 | -1.4 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 22.6% from a peak in-sample and 21.1% out-of-sample, and the worst single trade cost 4.9% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 1.4% a year against 5.6% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 44% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 19.9% from a peak in-sample and 22.0% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 50 of every 100 trades won in-sample. Out-of-sample it earned 1.6% a year against 4.1% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 45% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 62 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 9}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 70 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 23}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 539 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 17}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 1575 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 25}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 2584 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 21}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 2887 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 12}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 3372 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 14}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 4686 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 13}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 6228 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 11}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 7189 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 18}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 7465 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 19}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 7503 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 15}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 8686 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 22}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 9247 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 10}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 9969 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 16}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 11229 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 24}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 12210 | `{"max_candles": 294, "n": 72, "stop_loss_pct": 20}` | 9,745.96 | 5.6 | -22.3 | 44.9 | 1,638.17 | 1.4 | -21.1 | 0.25 | 49/41 | not checked |
| 230 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 21}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |
| 231 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 23}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |
| 234 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 22}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | 1.00 |
| 326 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 16}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |
| 2239 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 24}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |
| 6043 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 17}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |
| 6493 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 13}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |
| 8232 | `{"max_candles": 147, "n": 90, "stop_loss_pct": 20}` | 6,449.02 | 4.1 | -19.9 | 50.0 | 1,923.73 | 1.6 | -22.0 | 0.40 | 46/42 | not checked |

(9 more on the front, see results.csv)


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 15,069 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
