# volume_climax_rejection__broad: optimization summary

Updated 2026-11-26T05:03:08Z · backtest.py version `9a6709b1fe` · 890 parameter sets tested with this version (890 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [volume_climax_rejection__broad__max-income__v002.md](volume_climax_rejection__broad__max-income__v002.md) | 889 | `{"max_candles": 6, "rvol": 2.5, "stop_atr": 4.5, "take_profit_atr": 1.5}` | flat (data up to 2026-11-26 00:00) |
| balanced | [volume_climax_rejection__broad__balanced__v002.md](volume_climax_rejection__broad__balanced__v002.md) | 890 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 4.75, "take_profit_atr": 1.5}` | flat (data up to 2026-11-26 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,288.86 | 913.84 | 357.05 | 536.31 |
| return % | 12.89 | 9.14 | 3.57 | 5.36 |
| return %/year | 2.1 | 3.1 | 0.6 | 1.8 |
| gross profit | 2,402.99 | 2,384.18 | 411.92 | 605.04 |
| gross loss | 1,114.13 | 1,470.33 | 54.87 | 68.73 |
| trades | 231 | 272 | 31 | 34 |
| win rate % | 61.9 | 71.3 | 77.4 | 82.3 |
| avg win | 16.80 | 12.29 | 17.16 | 21.61 |
| avg loss | -12.66 | -18.85 | -7.84 | -11.46 |
| avg result / trade | 5.58 | 3.36 | 11.52 | 15.77 |
| largest single loss | -68.65 | -78.41 | -27.24 | -40.37 |
| largest loss % of equity | -16.39 | -20.88 | -8.45 | -12.06 |
| max drawdown | -276.47 | -974.35 | -37.58 | -173.35 |
| max drawdown % | -2.54 | -9.41 | -0.38 | -1.70 |
| profit factor | 2.16 | 1.62 | 7.51 | 8.80 |
| unusually bad trades | 21 | 24 | 1 | 2 |
| … threshold (% of equity) | 4.8 | 5.8 | 3.8 | 2.5 |
| time in market % | 0.2 | 0.6 | 0.0 | 0.1 |
| buy & hold return % | 450.49 | 71.18 | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.48 |  | 3.08 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -1.0 | -0.1 |
| 2019 | 0.5 | -0.0 |
| 2020 | 3.7 | 0.6 |
| 2021 | 8.4 | 2.0 |
| 2022 | 0.6 | 0.4 |
| 2023 | 0.7 | 0.4 |
| 2024 (OOS) | -0.7 | 3.8 |
| 2025 (OOS) | 6.1 | 1.0 |
| 2026 (OOS) | 3.6 | 0.6 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 2.5% from a peak in-sample and 9.4% out-of-sample, and the worst single trade cost 20.9% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.4% from a peak in-sample and 1.7% out-of-sample, and the worst single trade cost 12.1% of the account out-of-sample. About 77 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 844 | `{"max_candles": 6, "rvol": 2.5, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 1,288.86 | 2.1 | -2.5 | 61.9 | 913.84 | 3.1 | -9.4 | 1.48 | 231/272 | 0.88 |
| 561 | `{"max_candles": 6, "rvol": 3.0, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 1,059.82 | 1.7 | -1.7 | 71.0 | 1,205.60 | 4.0 | -3.1 | 2.33 | 114/140 | not checked |
| 322 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 4.75, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 644.04 | 2.2 | -1.9 | 2.37 | 47/43 | not checked |
| 405 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 5.0, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 644.04 | 2.2 | -1.9 | 2.37 | 47/43 | not checked |
| 427 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 5.5, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 644.04 | 2.2 | -1.9 | 2.37 | 47/43 | not checked |
| 444 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 644.04 | 2.2 | -1.9 | 2.37 | 47/43 | not checked |
| 522 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 5.25, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 644.04 | 2.2 | -1.9 | 2.37 | 47/43 | not checked |
| 558 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 629.99 | 2.1 | -1.9 | 2.31 | 47/43 | not checked |
| 567 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 644.04 | 2.2 | -1.9 | 2.37 | 47/43 | not checked |
| 590 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 633.13 | 2.1 | -1.9 | 2.33 | 47/43 | not checked |
| 885 | `{"max_candles": 6, "rvol": 4.0, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 553.83 | 0.9 | -0.9 | 76.6 | 636.27 | 2.1 | -1.9 | 2.34 | 47/43 | not checked |
| 424 | `{"max_candles": 6, "rvol": 3.25, "stop_atr": 4.25, "take_profit_atr": 0.5}` | 410.18 | 0.7 | -0.6 | 85.7 | 370.43 | 1.3 | -2.2 | 1.85 | 91/102 | not checked |
| 339 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 4.75, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 536.31 | 1.8 | -1.7 | 3.08 | 31/34 | 1.00 |
| 344 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 536.31 | 1.8 | -1.7 | 3.08 | 31/34 | not checked |
| 345 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 5.0, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 536.31 | 1.8 | -1.7 | 3.08 | 31/34 | not checked |
| 391 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 536.31 | 1.8 | -1.7 | 3.08 | 31/34 | not checked |
| 468 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 5.5, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 536.31 | 1.8 | -1.7 | 3.08 | 31/34 | not checked |
| 492 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 522.25 | 1.8 | -1.7 | 3.00 | 31/34 | not checked |
| 528 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 5.25, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 536.31 | 1.8 | -1.7 | 3.08 | 31/34 | not checked |
| 695 | `{"max_candles": 6, "rvol": 4.25, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 357.05 | 0.6 | -0.4 | 77.4 | 525.40 | 1.8 | -1.7 | 3.03 | 31/34 | not checked |
| 343 | `{"max_candles": 6, "rvol": 4.5, "stop_atr": 4.75, "take_profit_atr": 1.5}` | 296.25 | 0.5 | -0.3 | 80.0 | 314.62 | 1.1 | -1.2 | 2.20 | 25/25 | not checked |
| 417 | `{"max_candles": 6, "rvol": 4.5, "stop_atr": 5.0, "take_profit_atr": 1.5}` | 296.25 | 0.5 | -0.3 | 80.0 | 314.62 | 1.1 | -1.2 | 2.20 | 25/25 | not checked |
| 422 | `{"max_candles": 6, "rvol": 4.5, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 296.25 | 0.5 | -0.3 | 80.0 | 314.62 | 1.1 | -1.2 | 2.20 | 25/25 | not checked |
| 491 | `{"max_candles": 6, "rvol": 4.5, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 296.25 | 0.5 | -0.3 | 80.0 | 301.66 | 1.0 | -1.2 | 2.10 | 25/25 | not checked |
| 706 | `{"max_candles": 6, "rvol": 4.5, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 296.25 | 0.5 | -0.3 | 80.0 | 314.62 | 1.1 | -1.2 | 2.20 | 25/25 | not checked |

(2 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 890 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
