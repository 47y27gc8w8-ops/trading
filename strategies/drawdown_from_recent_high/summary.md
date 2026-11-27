# drawdown_from_recent_high: optimization summary

Updated 2026-11-26T00:05:23Z · backtest.py version `378b9dfe9b` · 1,268 parameter sets tested with this version (1,268 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [drawdown_from_recent_high__max-income__v002.md](drawdown_from_recent_high__max-income__v002.md) | 1267 | `{"dip": 12, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [drawdown_from_recent_high__balanced__v002.md](drawdown_from_recent_high__balanced__v002.md) | 1267 | `{"dip": 12, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | [drawdown_from_recent_high__safe-starter__v001.md](drawdown_from_recent_high__safe-starter__v001.md) | 1268 | `{"dip": 13, "max_candles": 2, "n": 12, "stop_atr": 3.5, "take_profit_atr": 4.5}` | flat (data up to 2026-11-24 00:00) |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 5,014.26 | 3,882.74 | 5,014.26 | 3,882.74 | 3,295.41 | 1,235.02 |
| return % | 50.14 | 38.83 | 50.14 | 38.83 | 32.95 | 12.35 |
| return %/year | 7.6 | 12.0 | 7.6 | 12.0 | 5.3 | 4.1 |
| gross profit | 15,519.93 | 5,728.71 | 15,519.93 | 5,728.71 | 7,953.69 | 1,418.37 |
| gross loss | 10,505.67 | 1,845.97 | 10,505.67 | 1,845.97 | 4,658.27 | 183.35 |
| trades | 48 | 15 | 48 | 15 | 29 | 5 |
| win rate % | 54.2 | 66.7 | 54.2 | 66.7 | 62.1 | 60.0 |
| avg win | 596.92 | 572.87 | 596.92 | 572.87 | 441.87 | 472.79 |
| avg loss | -477.53 | -369.19 | -477.53 | -369.19 | -423.48 | -91.67 |
| avg result / trade | 104.46 | 258.85 | 104.46 | 258.85 | 113.63 | 247.00 |
| largest single loss | -1,166.38 | -1,444.91 | -1,166.38 | -1,444.91 | -930.66 | -151.24 |
| largest loss % of equity | -7.27 | -9.21 | -7.27 | -9.21 | -7.27 | -1.33 |
| max drawdown | -3,425.31 | -1,838.66 | -3,425.31 | -1,838.66 | -2,682.81 | -279.18 |
| max drawdown % | -21.30 | -11.70 | -21.30 | -11.70 | -20.91 | -2.44 |
| profit factor | 1.48 | 3.10 | 1.48 | 3.10 | 1.71 | 7.74 |
| unusually bad trades | 5 | 1 | 5 | 1 | 0 | 0 |
| … threshold (% of equity) | 6.3 | 2.0 | 6.3 | 2.0 | 8.2 | 2.0 |
| time in market % | 4.5 | 2.6 | 4.5 | 2.6 | 2.7 | 0.8 |
| buy & hold return % | 547.53 | 44.90 | 547.53 | 44.90 | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.58 |  | 1.58 |  | 0.78 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | 0.0 | 0.0 | 0.0 |
| 2019 | 15.9 | 15.9 | -1.6 |
| 2020 | 0.0 | 0.0 | 0.4 |
| 2021 | 18.0 | 18.0 | 34.5 |
| 2022 | 0.0 | 0.0 | 0.0 |
| 2023 | 9.7 | 9.7 | 0.1 |
| 2024 (OOS) | 36.6 | 36.6 | 14.2 |
| 2025 (OOS) | 1.6 | 1.6 | -1.6 |
| 2026 (OOS) | 0.0 | 0.0 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 21.3% from a peak in-sample and 11.7% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 54 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 47% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 21.3% from a peak in-sample and 11.7% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 54 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 47% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 20.9% from a peak in-sample and 2.4% out-of-sample, and the worst single trade cost 1.3% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 48% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 747 | `{"dip": 12, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 5,014.26 | 7.6 | -21.3 | 54.2 | 3,882.74 | 12.0 | -11.7 | 1.58 | 48/15 | 0.78 |
| 760 | `{"dip": 12, "max_candles": 2, "n": 17, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,014.26 | 7.6 | -21.3 | 54.2 | 3,882.74 | 12.0 | -11.7 | 1.58 | 48/15 | not checked |
| 761 | `{"dip": 12, "max_candles": 2, "n": 17, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 5,014.26 | 7.6 | -21.3 | 54.2 | 3,882.74 | 12.0 | -11.7 | 1.58 | 48/15 | not checked |
| 1081 | `{"dip": 12, "max_candles": 2, "n": 17, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 5,014.26 | 7.6 | -21.3 | 54.2 | 3,882.74 | 12.0 | -11.7 | 1.58 | 48/15 | not checked |
| 848 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 884 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 901 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 944 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 989 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 994 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.25, "take_profit_atr": 4.0}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1005 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1007 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1039 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1061 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1084 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1104 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1217 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |
| 1240 | `{"dip": 14, "max_candles": 2, "n": 17, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 4,265.20 | 6.6 | -20.9 | 61.1 | 1,953.68 | 6.4 | -0.6 | 0.96 | 36/5 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

29 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | DOGEUSDT | 78% | 16.2 | 41.2 | 165.4 | 23.4 | -12.8 | 0 |
| 2 | INJUSDT | 78% | 15.2 | 37.5 | 75.0 | 3.6 | 4.7 | 12 |
| 3 | HBARUSDT | 42% | 1.4 | 54.1 | 22.5 | -12.5 | -16.2 | 2 |
| 4 | TRXUSDT | 31% | -4.4 | 27.3 | 34.3 | -7.7 | 2.6 | 6 |
| 5 | ALGOUSDT | 27% | -5.5 | 29.3 | 5.0 | -18.8 | -24.3 | 0 |
| 6 | ADAUSDT | 20% | -4.8 | 17.4 | 71.3 | -12.0 | -14.9 | 0 |
| 7 | LINKUSDT | 20% | -10.2 | 19.9 | 50.7 | -10.5 | -37.6 | 3 |
| 8 | BTCUSDT | 17% | -3.1 | 7.6 | 40.0 | 1.8 | -0.1 | 8 |
| 9 | BNBUSDT | 17% | -14.6 | 16.2 | 85.8 | -17.5 | -8.7 | 4 |
| 10 | XLMUSDT | 16% | -9.8 | 20.8 | 4.9 | -9.4 | -8.6 | 3 |
| 11 | BCHUSDT | 14% | -14.0 | 6.8 | 5.2 | -14.5 | -4.7 | 1 |
| 12 | FILUSDT | 12% | 9.8 | 10.8 | -61.2 | 4.9 | -21.5 | 0 |
| 13 | AVAXUSDT | 9% | -10.5 | 10.8 | 68.8 | -10.0 | -19.3 | 0 |
| 14 | ATOMUSDT | 9% | -19.9 | 17.5 | 21.4 | -21.4 | -19.1 | 0 |
| 15 | ETHUSDT | 8% | -9.2 | 12.5 | 31.8 | -20.1 | -23.5 | 1 |
| 16 | STXUSDT | 8% | -20.1 | 18.5 | 71.6 | -25.0 | -11.3 | 1 |
| 17 | AAVEUSDT | 3% | 11.1 | 5.1 | -41.0 | 13.8 | -29.3 | 0 |
| 18 | DOTUSDT | 3% | -13.8 | 4.8 | -32.1 | -23.4 | -22.6 | 0 |
| 19 | ETCUSDT | 3% | -18.7 | 6.8 | 24.9 | -12.6 | -22.9 | 0 |
| 20 | SOLUSDT | 3% | -19.8 | 5.5 | 40.8 | -21.6 | -24.7 | 0 |
| 21 | XRPUSDT | 2% | -26.7 | 0.3 | 15.2 | -30.3 | 13.5 | 1 |
| 22 | CAKEUSDT | 0% | 0.2 | n/a | -48.0 | -3.9 | -21.4 | 0 |
| 23 | UNIUSDT | 0% | -9.4 | n/a | -31.7 | -9.3 | -36.3 | 0 |
| 24 | LTCUSDT | 0% | -16.4 | n/a | 3.9 | -13.4 | -8.5 | 0 |
| 25 | DASHUSDT | 0% | -22.2 | n/a | -27.1 | -19.8 | -29.6 | 0 |
| 26 | NEARUSDT | 0% | -24.1 | n/a | 13.7 | -30.9 | -42.3 | 0 |
| 27 | JSTUSDT | 0% | -25.2 | n/a | -26.7 | -20.4 | 1.0 | 0 |
| 28 | VETUSDT | 0% | -29.6 | n/a | 38.6 | -24.6 | -17.4 | 0 |
| 29 | ZECUSDT | 0% | -34.2 | n/a | -11.6 | -34.2 | -56.0 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [drawdown_from_recent_high__broad__max-income__v002.md](symbols/broad/drawdown_from_recent_high__broad__max-income__v002.md) | 8.7 | 3.1 | 3.1 | -12.8 | 82.2 | 387/266 |
| broad | balanced | [drawdown_from_recent_high__broad__balanced__v002.md](symbols/broad/drawdown_from_recent_high__broad__balanced__v002.md) | 3.6 | 1.1 | 1.1 | -3.2 | 91.4 | 70/23 |
| broad | safe-starter | [drawdown_from_recent_high__broad__safe-starter__v001.md](symbols/broad/drawdown_from_recent_high__broad__safe-starter__v001.md) | 7.7 | 2.6 | 2.6 | -12.7 | 84.2 | 379/270 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,268 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
