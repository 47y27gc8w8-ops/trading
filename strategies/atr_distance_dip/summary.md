# atr_distance_dip: optimization summary

Updated 2026-11-25T22:54:10Z · backtest.py version `841fa309ff` · 20,811 parameter sets tested with this version (20,811 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [atr_distance_dip__max-income__v001.md](atr_distance_dip__max-income__v001.md) | 20810 | `{"distance": 3.5, "max_candles": 12, "stop_atr": 4.0, "take_profit_atr": 2.0}` | flat (data up to 2026-11-25 16:00) |
| balanced | [atr_distance_dip__balanced__v001.md](atr_distance_dip__balanced__v001.md) | 20811 | `{"distance": 3.5, "max_candles": 14, "stop_atr": 4.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 16:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,877.95 | 432.36 | 3,015.22 | 434.21 |
| return % | 28.78 | 4.32 | 30.15 | 4.34 |
| return %/year | 4.4 | 1.5 | 4.6 | 1.5 |
| gross profit | 6,711.00 | 3,594.01 | 5,505.57 | 3,764.53 |
| gross loss | 3,833.06 | 3,161.65 | 2,490.36 | 3,330.32 |
| trades | 20 | 16 | 20 | 16 |
| win rate % | 55.0 | 62.5 | 55.0 | 62.5 |
| avg win | 610.09 | 359.40 | 500.51 | 376.45 |
| avg loss | -425.90 | -526.94 | -276.71 | -555.05 |
| avg result / trade | 143.90 | 27.02 | 150.76 | 27.14 |
| largest single loss | -1,925.66 | -1,200.32 | -817.26 | -1,288.87 |
| largest loss % of equity | -13.16 | -10.19 | -6.17 | -10.81 |
| max drawdown | -4,107.98 | -1,613.70 | -3,297.49 | -1,740.71 |
| max drawdown % | -27.72 | -13.58 | -28.45 | -14.42 |
| profit factor | 1.75 | 1.14 | 2.21 | 1.13 |
| unusually bad trades | 2 | 1 | 4 | 1 |
| … threshold (% of equity) | 4.3 | 8.5 | 2.2 | 8.5 |
| time in market % | 1.4 | 2.3 | 1.8 | 2.5 |
| buy & hold return % | 110.38 | -25.03 | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.34 |  | 0.33 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | 8.6 | -5.0 |
| 2019 | 3.2 | 3.4 |
| 2020 | 10.4 | 10.1 |
| 2021 | -0.4 | 20.7 |
| 2022 | 1.8 | -4.9 |
| 2023 | 2.8 | 4.8 |
| 2024 (OOS) | 8.7 | 9.9 |
| 2025 (OOS) | 3.1 | 2.5 |
| 2026 (OOS) | -6.9 | -7.4 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 27.7% from a peak in-sample and 13.6% out-of-sample, and the worst single trade cost 10.2% of the account out-of-sample. About 55 of every 100 trades won in-sample. Out-of-sample it earned 1.5% a year against 4.4% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 28.4% from a peak in-sample and 14.4% out-of-sample, and the worst single trade cost 10.8% of the account out-of-sample. About 55 of every 100 trades won in-sample. Out-of-sample it earned 1.5% a year against 4.6% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 35% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 18305 | `{"distance": 3.5, "max_candles": 14, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 3,015.22 | 4.6 | -28.4 | 55.0 | 434.21 | 1.5 | -14.4 | 0.33 | 20/16 | 1.00 |
| 3995 | `{"distance": 3.5, "max_candles": 12, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 2,877.95 | 4.4 | -27.7 | 55.0 | 432.36 | 1.5 | -13.6 | 0.34 | 20/16 | 1.00 |
| 4003 | `{"distance": 3.5, "max_candles": 14, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 2,555.96 | 3.9 | -27.2 | 60.0 | 509.74 | 1.7 | -13.4 | 0.44 | 20/16 | not checked |
| 735 | `{"distance": 3.5, "max_candles": 14, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 1,832.65 | 2.9 | -26.2 | 61.9 | 497.40 | 1.7 | -14.2 | 0.58 | 21/16 | 1.00 |
| 6094 | `{"distance": 3.5, "max_candles": 14, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 765.35 | 1.2 | -25.3 | 61.9 | 248.38 | 0.8 | -12.6 | 0.68 | 21/17 | not checked |
| 14490 | `{"distance": 3.5, "max_candles": 16, "stop_atr": 3.5, "take_profit_atr": 1.5}` | 539.67 | 0.9 | -24.9 | 65.0 | 163.80 | 0.6 | -14.5 | 0.63 | 20/17 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TRXUSDT | 49% | 0.9 | 12.4 | 54.0 | 0.6 | -10.5 | 0 |
| 2 | JSTUSDT | 48% | 5.1 | 29.7 | 4.5 | 19.9 | 0.2 | 15 |
| 3 | BNBUSDT | 48% | 1.0 | 9.5 | 74.8 | 0.5 | 6.3 | 19 |
| 4 | STXUSDT | 41% | 2.8 | 50.4 | 105.8 | -4.3 | -17.7 | 0 |
| 5 | INJUSDT | 38% | 9.7 | 72.6 | 44.0 | 50.0 | -1.9 | 1 |
| 6 | HBARUSDT | 37% | 1.1 | 19.1 | 26.6 | -0.6 | 10.9 | 19 |
| 7 | ATOMUSDT | 37% | 0.9 | 42.6 | 36.8 | 10.5 | -16.9 | 0 |
| 8 | DOGEUSDT | 32% | 4.2 | 14.7 | 156.4 | 5.5 | -16.0 | 0 |
| 9 | ADAUSDT | 30% | -0.1 | 11.2 | 45.0 | -4.7 | -2.5 | 10 |
| 10 | LTCUSDT | 27% | -0.6 | 11.4 | -8.6 | 0.8 | -11.7 | 11 |
| 11 | ETCUSDT | 24% | 1.7 | 18.9 | 34.4 | -12.9 | -16.8 | 0 |
| 12 | SOLUSDT | 22% | -0.5 | 22.9 | 214.4 | -3.9 | -24.3 | 0 |
| 13 | VETUSDT | 22% | -0.6 | 23.0 | 53.1 | 14.1 | -9.6 | 0 |
| 14 | CAKEUSDT | 21% | 9.3 | 12.8 | -48.5 | 4.9 | -3.3 | 0 |
| 15 | XLMUSDT | 13% | -5.4 | 5.4 | -11.6 | -20.1 | -12.1 | 7 |
| 16 | ETHUSDT | 13% | -6.3 | 7.8 | 13.4 | -20.6 | -18.9 | 2 |
| 17 | ZECUSDT | 10% | -2.5 | 11.6 | -11.3 | 1.8 | 8.8 | 1 |
| 18 | SHIBUSDT | 8% | 7.0 | 23.2 | -41.9 | 2.7 | -9.1 | 0 |
| 19 | XRPUSDT | 6% | -4.8 | 1.9 | 5.0 | -3.4 | 1.1 | 4 |
| 20 | UNIUSDT | 6% | -5.0 | 8.8 | -37.0 | 2.6 | -1.9 | 0 |
| 21 | AVAXUSDT | 5% | -1.6 | 9.9 | 14.6 | -35.2 | -18.5 | 2 |
| 22 | ALGOUSDT | 5% | -5.3 | 6.3 | -3.8 | -14.7 | 6.7 | 2 |
| 23 | FILUSDT | 3% | -4.0 | 1.5 | -67.5 | -8.7 | -18.1 | 0 |
| 24 | ICPUSDT | 2% | -3.7 | 0.9 | -41.6 | -14.0 | -22.5 | 0 |
| 25 | DOTUSDT | 2% | -6.1 | 2.5 | -20.7 | -17.4 | -7.0 | 1 |
| 26 | DASHUSDT | 2% | -8.6 | 1.3 | -20.4 | -19.3 | -30.8 | 0 |
| 27 | AAVEUSDT | 2% | -8.8 | 0.1 | -36.5 | -18.9 | -4.0 | 0 |
| 28 | BCHUSDT | 2% | -11.3 | 12.0 | 2.9 | -23.7 | -12.2 | 0 |
| 29 | BTCUSDT | 0% | -9.6 | n/a | 27.1 | -9.8 | -7.2 | 0 |
| 30 | NEARUSDT | 0% | -15.4 | n/a | -15.6 | -13.8 | -5.2 | 0 |
| 31 | LINKUSDT | 0% | -16.4 | n/a | 37.9 | -16.9 | -5.7 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [atr_distance_dip__broad__max-income__v002.md](symbols/broad/atr_distance_dip__broad__max-income__v002.md) | 3.5 | 1.5 | 1.5 | -11.6 | 59.1 | 631/582 |
| broad | balanced | [atr_distance_dip__broad__balanced__v002.md](symbols/broad/atr_distance_dip__broad__balanced__v002.md) | 1.0 | 3.3 | 1.0 | -3.5 | 66.7 | 75/82 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 20,811 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
