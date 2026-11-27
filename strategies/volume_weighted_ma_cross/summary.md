# volume_weighted_ma_cross: optimization summary

Updated 2026-11-26T05:12:26Z · backtest.py version `fef9f45d7e` · 1,941 parameter sets tested with this version (1,941 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [volume_weighted_ma_cross__max-income__v002.md](volume_weighted_ma_cross__max-income__v002.md) | 1941 | `{"fast": 11, "max_candles": 96, "slow": 70, "stop_atr": 1.25, "take_profit_atr": 10.5}` | flat (data up to 2026-11-26 00:00) |
| balanced | [volume_weighted_ma_cross__balanced__v001.md](volume_weighted_ma_cross__balanced__v001.md) | 312 | `{"fast": 5, "max_candles": 60, "slow": 55, "stop_atr": 3.5, "take_profit_atr": 2.5}` | flat (data up to 2026-11-26 00:00) |
| safe-starter | [volume_weighted_ma_cross__safe-starter__v001.md](volume_weighted_ma_cross__safe-starter__v001.md) | 1941 | `{"fast": 11, "max_candles": 96, "slow": 70, "stop_atr": 1.25, "take_profit_atr": 10.5}` | flat (data up to 2026-11-26 00:00) |

Note: one parameter set wins max-income, safe-starter. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 66,309.86 | 3,275.29 | 452.70 | 1,189.20 | 66,309.86 | 3,275.29 |
| return % | 663.10 | 32.75 | 4.53 | 11.89 | 663.10 | 32.75 |
| return %/year | 41.0 | 10.3 | 0.8 | 4.0 | 41.0 | 10.3 |
| gross profit | 130,853.68 | 16,652.42 | 30,347.49 | 13,318.73 | 130,853.68 | 16,652.42 |
| gross loss | 64,543.82 | 13,377.14 | 29,894.79 | 12,129.53 | 64,543.82 | 13,377.14 |
| trades | 78 | 49 | 113 | 66 | 78 | 49 |
| win rate % | 30.8 | 20.4 | 46.9 | 48.5 | 30.8 | 20.4 |
| avg win | 5,452.24 | 1,665.24 | 572.59 | 416.21 | 5,452.24 | 1,665.24 |
| avg loss | -1,195.26 | -343.00 | -498.25 | -356.75 | -1,195.26 | -343.00 |
| avg result / trade | 850.13 | 66.84 | 4.01 | 18.02 | 850.13 | 66.84 |
| largest single loss | -3,736.40 | -730.41 | -1,389.58 | -991.59 | -3,736.40 | -730.41 |
| largest loss % of equity | -4.83 | -4.00 | -7.96 | -7.94 | -4.83 | -4.00 |
| max drawdown | -21,994.69 | -6,642.91 | -9,682.57 | -3,536.88 | -21,994.69 | -6,642.91 |
| max drawdown % | -25.39 | -33.35 | -50.30 | -27.66 | -25.39 | -33.35 |
| profit factor | 2.03 | 1.25 | 1.01 | 1.10 | 2.03 | 1.25 |
| unusually bad trades | 0 | 0 | 1 | 1 | 0 | 0 |
| … threshold (% of equity) | 5.4 | 4.4 | 8.1 | 5.9 | 5.4 | 4.4 |
| time in market % | 13.2 | 13.3 | 10.1 | 8.2 | 13.2 | 13.3 |
| buy & hold return % | 110.38 | -25.03 | 110.38 | -25.03 | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.25 |  | 5.28 |  | 0.25 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -0.1 | -13.4 | -0.1 |
| 2019 | 6.4 | 3.3 | 6.4 |
| 2020 | 231.9 | 39.6 | 231.9 |
| 2021 | 98.6 | 38.2 | 98.6 |
| 2022 | 0.8 | -39.4 | 0.8 |
| 2023 | 8.0 | -0.1 | 8.0 |
| 2024 (OOS) | 46.9 | 21.1 | 46.9 |
| 2025 (OOS) | 16.8 | -11.6 | 16.8 |
| 2026 (OOS) | -22.6 | 4.5 | -22.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 25.4% from a peak in-sample and 33.4% out-of-sample, and the worst single trade cost 4.0% of the account out-of-sample. About 31 of every 100 trades won in-sample. Out-of-sample it earned 10.3% a year against 41.0% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 50.3% from a peak in-sample and 27.7% out-of-sample, and the worst single trade cost 7.9% of the account out-of-sample. About 47 of every 100 trades won in-sample. With 100% of equity per trade; about 20% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 25.4% from a peak in-sample and 33.4% out-of-sample, and the worst single trade cost 4.0% of the account out-of-sample. About 31 of every 100 trades won in-sample. Out-of-sample it earned 10.3% a year against 41.0% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.
- safe-starter: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1440 | `{"fast": 11, "max_candles": 96, "slow": 70, "stop_atr": 1.25, "take_profit_atr": 10.5}` | 66,309.86 | 41.0 | -25.4 | 30.8 | 3,275.29 | 10.3 | -33.4 | 0.25 | 78/49 | 1.00 |

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | SOLUSDT | 92% | 25.9 | 108.3 | 214.4 | 13.8 | 4.8 | 18 |
| 2 | BNBUSDT | 81% | 8.3 | 41.4 | 74.8 | 1.4 | -4.6 | 22 |
| 3 | LTCUSDT | 77% | 8.2 | 42.4 | -8.6 | 19.5 | -14.9 | 4 |
| 4 | ZECUSDT | 67% | 6.7 | 48.4 | -11.3 | 12.9 | -9.6 | 33 |
| 5 | LINKUSDT | 66% | 4.9 | 52.1 | 37.9 | 6.0 | -22.4 | 4 |
| 6 | ETCUSDT | 64% | 6.8 | 33.0 | 34.4 | 2.6 | 8.9 | 2 |
| 7 | VETUSDT | 64% | 6.7 | 76.9 | 53.1 | 8.9 | -13.6 | 9 |
| 8 | XLMUSDT | 59% | 2.5 | 28.2 | -11.6 | -6.0 | -27.2 | 0 |
| 9 | ADAUSDT | 58% | 3.6 | 31.4 | 45.0 | -1.5 | 18.3 | 15 |
| 10 | AVAXUSDT | 56% | 2.5 | 85.3 | 14.6 | 59.3 | -11.8 | 2 |
| 11 | DOGEUSDT | 55% | 2.2 | 34.9 | 156.4 | -2.7 | -8.8 | 15 |
| 12 | TRXUSDT | 53% | 1.0 | 36.1 | 54.0 | 7.5 | -1.8 | 2 |
| 13 | ETHUSDT | 53% | 0.6 | 70.0 | 13.4 | -1.9 | -18.3 | 4 |
| 14 | INJUSDT | 47% | -2.5 | 69.0 | 44.0 | 19.6 | -12.1 | 3 |
| 15 | STXUSDT | 45% | -2.1 | 76.0 | 105.8 | -19.7 | -31.3 | 1 |
| 16 | HBARUSDT | 44% | -2.3 | 49.5 | 26.6 | 10.3 | -32.9 | 2 |
| 17 | ATOMUSDT | 39% | -6.3 | 36.4 | 36.8 | 1.3 | -21.0 | 2 |
| 18 | BCHUSDT | 38% | -3.9 | 39.2 | 2.9 | 3.2 | -12.4 | 2 |
| 19 | JSTUSDT | 38% | -7.2 | 43.6 | 4.5 | 21.8 | -5.6 | 5 |
| 20 | NEARUSDT | 36% | -10.9 | 47.1 | -15.6 | 15.8 | 14.8 | 11 |
| 21 | BTCUSDT | 34% | -3.9 | 17.6 | 27.1 | 6.8 | 5.8 | 4 |
| 22 | DOTUSDT | 33% | -8.1 | 36.6 | -20.7 | 14.2 | 6.7 | 2 |
| 23 | FILUSDT | 30% | -9.4 | 19.1 | -67.5 | 2.8 | -3.4 | 1 |
| 24 | DASHUSDT | 28% | -7.3 | 22.8 | -20.4 | -3.6 | -30.0 | 4 |
| 25 | AAVEUSDT | 27% | -9.4 | 33.8 | -36.5 | 15.9 | 37.7 | 6 |
| 26 | UNIUSDT | 27% | -10.0 | 22.0 | -37.0 | -27.3 | -26.6 | 1 |
| 27 | ALGOUSDT | 19% | -10.1 | 15.3 | -3.8 | -14.6 | -9.9 | 4 |
| 28 | CAKEUSDT | 16% | -9.6 | 20.9 | -48.5 | -10.8 | 18.6 | 9 |
| 29 | ICPUSDT | 14% | -17.4 | 32.8 | -41.6 | -39.3 | -8.9 | 2 |
| 30 | XRPUSDT | 11% | -13.1 | 15.2 | 5.0 | -15.2 | -18.8 | 0 |
| 31 | SHIBUSDT | 2% | -18.6 | 0.3 | -41.9 | -15.3 | -2.1 | 1 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [volume_weighted_ma_cross__broad__max-income__v001.md](symbols/broad/volume_weighted_ma_cross__broad__max-income__v001.md) | 13.9 | 5.5 | 5.5 | -26.6 | 26.9 | 1913/1372 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,941 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
