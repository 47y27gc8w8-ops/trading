# multi_horizon_roc_vote: optimization summary

Updated 2026-11-26T00:27:03Z · backtest.py version `866a9ad9a7` · 6,253 parameter sets tested with this version (6,253 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [multi_horizon_roc_vote__max-income__v001.md](multi_horizon_roc_vote__max-income__v001.md) | 6253 | `{"max_candles": 60, "stop_atr": 4.0, "take_profit_atr": 2.5, "votes": 4}` | flat (data up to 2026-11-24 00:00) |
| balanced | [multi_horizon_roc_vote__balanced__v001.md](multi_horizon_roc_vote__balanced__v001.md) | 6253 | `{"max_candles": 60, "stop_atr": 4.0, "take_profit_atr": 2.5, "votes": 4}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,867.42 | 882.02 | 2,867.42 | 882.02 |
| return % | 28.67 | 8.82 | 28.67 | 8.82 |
| return %/year | 4.7 | 3.0 | 4.7 | 3.0 |
| gross profit | 15,846.33 | 5,443.25 | 15,846.33 | 5,443.25 |
| gross loss | 12,978.90 | 4,561.23 | 12,978.90 | 4,561.23 |
| trades | 20 | 11 | 20 | 11 |
| win rate % | 65.0 | 63.6 | 65.0 | 63.6 |
| avg win | 1,218.95 | 777.61 | 1,218.95 | 777.61 |
| avg loss | -1,854.13 | -1,140.31 | -1,854.13 | -1,140.31 |
| avg result / trade | 143.37 | 80.18 | 143.37 | 80.18 |
| largest single loss | -3,063.87 | -1,865.30 | -3,063.87 | -1,865.30 |
| largest loss % of equity | -24.00 | -15.01 | -24.00 | -15.01 |
| max drawdown | -5,702.96 | -2,320.64 | -5,702.96 | -2,320.64 |
| max drawdown % | -38.92 | -18.51 | -38.92 | -18.51 |
| profit factor | 1.22 | 1.19 | 1.22 | 1.19 |
| unusually bad trades | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 30.6 | 19.4 | 30.6 | 19.4 |
| time in market % | 17.9 | 26.4 | 17.9 | 26.4 |
| buy & hold return % | 547.53 | 44.90 | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.64 |  | 0.64 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | 0.0 | 0.0 |
| 2019 | -3.0 | -3.0 |
| 2020 | 18.7 | 18.7 |
| 2021 | 2.4 | 2.4 |
| 2022 | 0.0 | 0.0 |
| 2023 | 9.1 | 9.1 |
| 2024 (OOS) | 7.5 | 7.5 |
| 2025 (OOS) | 13.1 | 13.1 |
| 2026 (OOS) | -10.5 | -10.5 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 38.9% from a peak in-sample and 18.5% out-of-sample, and the worst single trade cost 15.0% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 38.9% from a peak in-sample and 18.5% out-of-sample, and the worst single trade cost 15.0% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 26% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 928 | `{"max_candles": 60, "stop_atr": 4.0, "take_profit_atr": 2.5, "votes": 4}` | 2,867.42 | 4.7 | -38.9 | 65.0 | 882.02 | 3.0 | -18.5 | 0.64 | 20/11 | 0.67 |

## Screening: where does the strategy work? (in-sample ranking)

29 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | LINKUSDT | 68% | 16.4 | 49.7 | 50.7 | 0.1 | 12.5 | 11 |
| 2 | ETHUSDT | 61% | 7.9 | 24.5 | 31.8 | 10.6 | -18.4 | 3 |
| 3 | BNBUSDT | 55% | 20.7 | 37.6 | 85.8 | -6.0 | -16.8 | 0 |
| 4 | TRXUSDT | 53% | 6.2 | 24.8 | 34.3 | -17.6 | 0.3 | 27 |
| 5 | LTCUSDT | 47% | 11.2 | 22.4 | 3.9 | 0.7 | -19.6 | 2 |
| 6 | XRPUSDT | 39% | -4.2 | 41.8 | 15.2 | -11.6 | -16.7 | 0 |
| 7 | VETUSDT | 37% | -9.9 | 47.2 | 38.6 | -17.1 | 0.2 | 1 |
| 8 | BTCUSDT | 34% | -1.8 | 19.3 | 40.0 | 1.4 | -16.1 | 1 |
| 9 | XLMUSDT | 34% | -2.5 | 32.0 | 4.9 | -8.6 | -33.8 | 2 |
| 10 | DOGEUSDT | 34% | -21.2 | 21.1 | 165.4 | -28.2 | -1.6 | 20 |
| 11 | ZECUSDT | 32% | 29.3 | 46.9 | -11.6 | 42.5 | 20.5 | 20 |
| 12 | CAKEUSDT | 32% | 2.2 | 33.2 | -48.0 | 6.4 | -5.6 | 0 |
| 13 | STXUSDT | 27% | 6.3 | 16.7 | 71.6 | -6.7 | -38.8 | 5 |
| 14 | AVAXUSDT | 27% | -0.2 | 39.1 | 68.8 | -14.3 | -6.2 | 0 |
| 15 | BCHUSDT | 21% | 3.3 | 42.5 | 5.2 | 33.8 | -20.7 | 1 |
| 16 | AAVEUSDT | 21% | -10.5 | 11.4 | -41.0 | -48.6 | 5.2 | 0 |
| 17 | ETCUSDT | 19% | -12.6 | 19.8 | 24.9 | -16.1 | -6.8 | 2 |
| 18 | FILUSDT | 18% | -2.2 | 16.9 | -61.2 | -30.4 | -12.1 | 0 |
| 19 | UNIUSDT | 18% | -13.7 | 15.6 | -31.7 | -18.8 | -16.7 | 7 |
| 20 | ADAUSDT | 15% | 2.2 | 16.2 | 71.3 | -8.2 | -4.9 | 1 |
| 21 | INJUSDT | 13% | -3.2 | 14.3 | 75.0 | 8.4 | -25.6 | 0 |
| 22 | ATOMUSDT | 10% | -9.6 | 13.2 | 21.4 | -9.1 | -5.6 | 1 |
| 23 | ALGOUSDT | 6% | -6.8 | 18.3 | 5.0 | -23.9 | -24.6 | 1 |
| 24 | SOLUSDT | 2% | -2.4 | 7.0 | 40.8 | -13.4 | 13.3 | 1 |
| 25 | DASHUSDT | 2% | -2.9 | 2.1 | -27.1 | -11.1 | -2.8 | 0 |
| 26 | HBARUSDT | 2% | -17.1 | 0.8 | 22.5 | 0.8 | -18.0 | 0 |
| 27 | NEARUSDT | 0% | 44.9 | n/a | 13.7 | -2.0 | -31.5 | 0 |
| 28 | DOTUSDT | 0% | -11.5 | n/a | -32.1 | 4.7 | -12.4 | 0 |
| 29 | JSTUSDT | 0% | -19.9 | n/a | -26.7 | -9.2 | 6.2 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [multi_horizon_roc_vote__broad__max-income__v002.md](symbols/broad/multi_horizon_roc_vote__broad__max-income__v002.md) | 13.3 | 6.9 | 6.9 | -52.8 | 29.5 | 1082/861 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 6,253 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
