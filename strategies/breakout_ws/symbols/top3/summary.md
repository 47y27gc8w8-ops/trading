# breakout_ws__top3: optimization summary

Updated 2026-11-23T22:11:08Z · backtest.py version `5f036785d9` · 1,379 parameter sets tested with this version (1,379 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: ETHUSDT, ETCUSDT, VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_ws__top3__max-income__v002.md](breakout_ws__top3__max-income__v002.md) | 1378 | `{"entry_n": 38, "exit_n": 8}` | flat (data up to 2026-11-22 00:00) |
| balanced | [breakout_ws__top3__balanced__v002.md](breakout_ws__top3__balanced__v002.md) | 1379 | `{"entry_n": 32, "exit_n": 2}` | flat (data up to 2026-11-22 00:00) |
| safe-starter | [breakout_ws__top3__safe-starter__v001.md](breakout_ws__top3__safe-starter__v001.md) | 134 | `{"entry_n": 56, "exit_n": 8}` | flat (data up to 2026-11-22 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 136,142.03 | 5,347.43 | 93,609.50 | 4,114.89 | 80,468.06 | 3,598.53 |
| return % | 1,361.42 | 53.47 | 936.09 | 41.15 | 804.68 | 35.99 |
| return %/year | 56.4 | 16.0 | 47.7 | 12.7 | 44.4 | 11.2 |
| gross profit | 189,100.03 | 11,908.22 | 155,163.81 | 10,412.48 | 124,750.70 | 9,246.53 |
| gross loss | 52,958.00 | 6,560.79 | 61,554.31 | 6,297.59 | 44,282.64 | 5,648.01 |
| trades | 59 | 28 | 99 | 38 | 50 | 24 |
| win rate % | 52.5 | 42.9 | 49.5 | 44.7 | 52.0 | 41.7 |
| avg win | 6,100.00 | 992.35 | 3,166.61 | 612.50 | 4,798.10 | 924.65 |
| avg loss | -1,891.36 | -410.05 | -1,231.09 | -299.89 | -1,845.11 | -403.43 |
| avg result / trade | 2,307.49 | 190.98 | 945.55 | 108.29 | 1,609.36 | 149.94 |
| largest single loss | -19,210.69 | -862.94 | -10,775.86 | -703.91 | -11,592.22 | -721.61 |
| largest loss % of equity | -23.53 | -12.92 | -20.53 | -9.86 | -27.48 | -15.01 |
| max drawdown | -66,067.37 | -8,290.14 | -38,970.13 | -2,877.25 | -78,334.48 | -6,732.02 |
| max drawdown % | -45.44 | -38.16 | -33.47 | -16.93 | -56.47 | -35.75 |
| profit factor | 3.57 | 1.81 | 2.52 | 1.65 | 2.82 | 1.64 |
| unusually bad trades | 5 | 0 | 9 | 1 | 1 | 0 |
| … threshold (% of equity) | 18.1 | 19.3 | 12.0 | 12.5 | 22.8 | 21.2 |
| time in market % | 26.9 | 19.1 | 15.1 | 11.1 | 22.6 | 17.6 |
| buy & hold return % | 265.38 | -61.67 | 265.38 | -61.67 | 265.38 | -61.67 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |  | 0.27 |  | 0.25 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | 1.0 | -2.6 | -4.9 |
| 2019 | -26.7 | 15.3 | -7.6 |
| 2020 | 158.9 | 42.8 | 116.5 |
| 2021 | 545.0 | 383.0 | 331.0 |
| 2022 | -20.4 | 27.6 | -25.7 |
| 2023 | 48.6 | 4.9 | 48.9 |
| 2024 (OOS) | 84.2 | 45.8 | 43.8 |
| 2025 (OOS) | -13.4 | 3.0 | -6.5 |
| 2026 (OOS) | 33.6 | -3.1 | 26.5 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 45.4% from a peak in-sample and 38.2% out-of-sample, and the worst single trade cost 12.9% of the account out-of-sample. About 53 of every 100 trades won in-sample. Out-of-sample it earned 16.0% a year against 56.4% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 22% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 33.5% from a peak in-sample and 16.9% out-of-sample, and the worst single trade cost 9.9% of the account out-of-sample. About 49 of every 100 trades won in-sample. Out-of-sample it earned 12.7% a year against 47.7% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 56.5% from a peak in-sample and 35.8% out-of-sample, and the worst single trade cost 15.0% of the account out-of-sample. About 52 of every 100 trades won in-sample. Out-of-sample it earned 11.2% a year against 44.4% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 18% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 357 | `{"entry_n": 37, "exit_n": 8}` | 142,059.62 | 57.5 | -45.1 | 52.5 | 4,982.80 | 15.0 | -38.4 | 0.26 | 59/29 | not checked |
| 366 | `{"entry_n": 41, "exit_n": 8}` | 131,618.04 | 55.6 | -42.0 | 51.7 | 4,644.31 | 14.1 | -35.8 | 0.25 | 58/27 | not checked |
| 200 | `{"entry_n": 34, "exit_n": 3}` | 111,553.28 | 51.7 | -33.0 | 50.0 | 4,235.52 | 13.0 | -19.2 | 0.25 | 88/35 | 1.00 |
| 76 | `{"entry_n": 30, "exit_n": 3}` | 98,641.20 | 48.9 | -32.5 | 47.9 | 4,458.82 | 13.6 | -22.5 | 0.28 | 96/38 | 1.00 |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,379 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
