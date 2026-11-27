# rsi_dip_trend_filter: optimization summary

Updated 2026-11-25T22:42:24Z · backtest.py version `028e59b880` · 1,340 parameter sets tested with this version (1,340 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rsi_dip_trend_filter__max-income__v002.md](rsi_dip_trend_filter__max-income__v002.md) | 948 | `{"buy": 34, "exit": 65, "max_candles": 16, "n": 19, "stop_atr": 1.5, "take_profit_atr": 4.0}` | flat (data up to 2026-11-25 16:00) |
| balanced | [rsi_dip_trend_filter__balanced__v001.md](rsi_dip_trend_filter__balanced__v001.md) | 758 | `{"buy": 34, "exit": 65, "max_candles": 14, "n": 19, "stop_atr": 1.75, "take_profit_atr": 3.5}` | flat (data up to 2026-11-25 16:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,027.76 | 285.92 | 880.77 | 243.41 |
| return % | 10.28 | 2.86 | 8.81 | 2.43 |
| return %/year | 1.7 | 1.0 | 1.4 | 0.8 |
| gross profit | 4,500.53 | 1,371.94 | 4,632.84 | 1,201.92 |
| gross loss | 3,472.77 | 1,086.02 | 3,752.07 | 958.50 |
| trades | 21 | 8 | 20 | 8 |
| win rate % | 38.1 | 37.5 | 45.0 | 50.0 |
| avg win | 562.57 | 457.31 | 514.76 | 300.48 |
| avg loss | -267.14 | -217.20 | -341.10 | -239.63 |
| avg result / trade | 48.94 | 35.74 | 44.04 | 30.43 |
| largest single loss | -545.82 | -273.24 | -631.79 | -309.31 |
| largest loss % of equity | -5.46 | -2.67 | -6.32 | -3.06 |
| max drawdown | -1,960.06 | -1,231.98 | -2,253.33 | -1,371.00 |
| max drawdown % | -18.85 | -11.48 | -22.35 | -12.77 |
| profit factor | 1.30 | 1.26 | 1.24 | 1.25 |
| unusually bad trades | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 6.0 | 4.5 | 7.1 | 4.6 |
| time in market % | 1.5 | 0.7 | 1.3 | 0.9 |
| buy & hold return % | 313.33 | 44.90 | 313.33 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.59 |  | 0.58 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -16.9 | -19.2 |
| 2019 | -1.2 | -0.2 |
| 2020 | 9.3 | 8.4 |
| 2021 | 22.5 | 25.2 |
| 2022 | -3.0 | -3.4 |
| 2023 | 3.3 | 3.0 |
| 2024 (OOS) | -5.0 | -3.2 |
| 2025 (OOS) | 6.1 | 4.5 |
| 2026 (OOS) | 2.0 | 1.3 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 18.9% from a peak in-sample and 11.5% out-of-sample, and the worst single trade cost 2.7% of the account out-of-sample. About 38 of every 100 trades won in-sample. Out-of-sample it earned 1.0% a year against 1.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 22.4% from a peak in-sample and 12.8% out-of-sample, and the worst single trade cost 3.1% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 0.8% a year against 1.4% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 45% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 939 | `{"buy": 34, "exit": 60, "max_candles": 16, "n": 19, "stop_atr": 1.5, "take_profit_atr": 4.0}` | 1,027.76 | 1.7 | -18.9 | 38.1 | 285.92 | 1.0 | -11.5 | 0.59 | 21/8 | not checked |
| 940 | `{"buy": 34, "exit": 70, "max_candles": 16, "n": 19, "stop_atr": 1.5, "take_profit_atr": 4.0}` | 1,027.76 | 1.7 | -18.9 | 38.1 | 285.92 | 1.0 | -11.5 | 0.59 | 21/8 | not checked |
| 947 | `{"buy": 34, "exit": 65, "max_candles": 16, "n": 19, "stop_atr": 1.5, "take_profit_atr": 4.0}` | 1,027.76 | 1.7 | -18.9 | 38.1 | 285.92 | 1.0 | -11.5 | 0.59 | 21/8 | 0.75 |

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | BNBUSDT | 32% | 0.0 | 25.6 | 74.8 | 5.5 | 0.6 | 6 |
| 2 | JSTUSDT | 29% | 1.2 | 35.6 | 4.5 | -0.2 | 1.9 | 8 |
| 3 | XRPUSDT | 29% | 0.0 | 18.4 | 5.0 | 5.3 | 3.7 | 0 |
| 4 | SOLUSDT | 27% | 7.1 | 40.1 | 214.4 | 9.3 | -5.4 | 0 |
| 5 | INJUSDT | 27% | 0.0 | 52.3 | 44.0 | 12.2 | 0.6 | 2 |
| 6 | HBARUSDT | 25% | 0.0 | 30.4 | 26.6 | -4.5 | 0.0 | 2 |
| 7 | ATOMUSDT | 25% | 0.0 | 32.3 | 36.8 | 3.2 | -3.8 | 0 |
| 8 | ALGOUSDT | 24% | 0.0 | 22.3 | -3.8 | -4.7 | 8.3 | 1 |
| 9 | ADAUSDT | 21% | 0.4 | 35.3 | 45.0 | -1.1 | -4.0 | 1 |
| 10 | DOGEUSDT | 21% | 0.0 | 36.5 | 156.4 | -6.3 | 3.4 | 1 |
| 11 | DOTUSDT | 21% | 0.0 | 40.2 | -20.7 | 3.1 | 1.4 | 0 |
| 12 | NEARUSDT | 19% | 0.0 | 69.8 | -15.6 | -2.6 | 10.6 | 6 |
| 13 | UNIUSDT | 19% | 0.0 | 39.8 | -37.0 | -5.7 | -0.9 | 0 |
| 14 | AAVEUSDT | 19% | 0.0 | 31.1 | -36.5 | 1.4 | 0.2 | 4 |
| 15 | STXUSDT | 17% | 0.0 | 28.0 | 105.8 | -5.0 | 11.0 | 2 |
| 16 | VETUSDT | 16% | 0.1 | 13.0 | 53.1 | 5.2 | 10.6 | 0 |
| 17 | XLMUSDT | 16% | 0.0 | 12.6 | -11.6 | -3.6 | 1.9 | 5 |
| 18 | LINKUSDT | 14% | 0.0 | 15.4 | 37.9 | -0.6 | -3.0 | 0 |
| 19 | ETHUSDT | 14% | -1.9 | 12.2 | 13.4 | -2.2 | -7.7 | 0 |
| 20 | FILUSDT | 11% | 0.0 | 8.2 | -67.5 | -0.2 | 1.5 | 0 |
| 21 | ETCUSDT | 11% | -0.9 | 9.1 | 34.4 | -13.8 | -10.4 | 0 |
| 22 | ZECUSDT | 10% | 0.0 | 6.0 | -11.3 | -9.4 | 2.3 | 5 |
| 23 | ICPUSDT | 8% | 0.0 | 16.8 | -41.6 | -2.0 | 12.2 | 0 |
| 24 | TRXUSDT | 6% | 0.0 | 11.4 | 54.0 | 4.1 | 1.1 | 0 |
| 25 | CAKEUSDT | 6% | 0.0 | 5.4 | -48.5 | 3.1 | 14.6 | 0 |
| 26 | LTCUSDT | 5% | 0.0 | 4.8 | -8.6 | -0.1 | 8.9 | 1 |
| 27 | AVAXUSDT | 5% | 0.0 | 24.2 | 14.6 | 6.5 | -1.1 | 0 |
| 28 | DASHUSDT | 5% | 0.0 | 2.7 | -20.4 | 0.8 | 2.9 | 1 |
| 29 | BCHUSDT | 3% | -2.2 | 0.4 | 2.9 | -6.0 | -11.4 | 0 |
| 30 | BTCUSDT | 3% | -2.6 | 1.7 | 27.1 | -1.2 | -1.1 | 2 |
| 31 | SHIBUSDT | 0% | 0.0 | n/a | -41.9 | 7.6 | -0.8 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [rsi_dip_trend_filter__broad__max-income__v002.md](symbols/broad/rsi_dip_trend_filter__broad__max-income__v002.md) | 4.2 | 1.6 | 1.6 | -10.1 | 70.7 | 382/268 |
| broad | balanced | [rsi_dip_trend_filter__broad__balanced__v002.md](symbols/broad/rsi_dip_trend_filter__broad__balanced__v002.md) | 4.2 | 1.6 | 1.6 | -10.1 | 70.7 | 382/268 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,340 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
