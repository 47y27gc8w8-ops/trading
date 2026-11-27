# atr_distance_dip__broad: optimization summary

Updated 2026-11-25T22:54:08Z · backtest.py version `1e6b11acb4` · 887 parameter sets tested with this version (887 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [atr_distance_dip__broad__max-income__v002.md](atr_distance_dip__broad__max-income__v002.md) | 886 | `{"distance": 3.0, "max_candles": 8, "stop_atr": 5.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 16:00) |
| balanced | [atr_distance_dip__broad__balanced__v002.md](atr_distance_dip__broad__balanced__v002.md) | 887 | `{"distance": 4.5, "max_candles": 6, "stop_atr": 4.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 16:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,263.52 | 427.86 | 618.59 | 997.36 |
| return % | 22.64 | 4.28 | 6.19 | 9.97 |
| return %/year | 3.5 | 1.5 | 1.0 | 3.3 |
| gross profit | 6,905.60 | 4,323.83 | 903.50 | 1,254.44 |
| gross loss | 4,642.08 | 3,895.97 | 284.91 | 257.08 |
| trades | 631 | 582 | 75 | 82 |
| win rate % | 59.1 | 51.7 | 66.7 | 70.7 |
| avg win | 18.51 | 14.36 | 18.07 | 21.63 |
| avg loss | -17.99 | -13.86 | -11.40 | -10.71 |
| avg result / trade | 3.59 | 0.74 | 8.25 | 12.16 |
| largest single loss | -175.73 | -100.77 | -91.81 | -40.08 |
| largest loss % of equity | -38.80 | -28.67 | -27.45 | -10.74 |
| max drawdown | -1,217.85 | -1,213.91 | -123.73 | -351.44 |
| max drawdown % | -9.56 | -11.58 | -1.20 | -3.48 |
| profit factor | 1.49 | 1.11 | 3.17 | 4.88 |
| unusually bad trades | 59 | 73 | 5 | 6 |
| … threshold (% of equity) | 6.4 | 5.1 | 3.0 | 4.2 |
| time in market % | 1.1 | 2.1 | 0.1 | 0.2 |
| buy & hold return % | 450.49 | 71.18 | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.42 |  | 3.27 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -0.1 | 0.1 |
| 2019 | 1.6 | 0.4 |
| 2020 | 0.9 | 0.2 |
| 2021 | 23.0 | 1.1 |
| 2022 | -3.0 | 3.9 |
| 2023 | 0.4 | 0.3 |
| 2024 (OOS) | 3.7 | 7.7 |
| 2025 (OOS) | -0.8 | 0.5 |
| 2026 (OOS) | 0.1 | 1.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.6% from a peak in-sample and 11.6% out-of-sample, and the worst single trade cost 28.7% of the account out-of-sample. About 59 of every 100 trades won in-sample. Out-of-sample it earned 1.5% a year against 3.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 86% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 1.2% from a peak in-sample and 3.5% out-of-sample, and the worst single trade cost 10.7% of the account out-of-sample. About 67 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 671 | `{"distance": 3.0, "max_candles": 8, "stop_atr": 5.75, "take_profit_atr": 2.0}` | 2,363.50 | 3.6 | -9.3 | 59.1 | 394.91 | 1.4 | -10.1 | 0.37 | 624/581 | not checked |
| 539 | `{"distance": 3.0, "max_candles": 8, "stop_atr": 5.75, "take_profit_atr": 2.5}` | 2,245.86 | 3.5 | -9.2 | 59.0 | 656.14 | 2.2 | -9.9 | 0.64 | 624/580 | not checked |
| 591 | `{"distance": 3.0, "max_candles": 8, "stop_atr": 5.75, "take_profit_atr": 3.0}` | 2,209.16 | 3.4 | -9.0 | 58.6 | 795.97 | 2.7 | -10.0 | 0.78 | 624/580 | not checked |
| 466 | `{"distance": 3.25, "max_candles": 6, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 1,592.74 | 2.5 | -6.5 | 58.3 | 362.62 | 1.2 | -13.1 | 0.49 | 492/444 | not checked |
| 495 | `{"distance": 3.25, "max_candles": 6, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 1,435.75 | 2.3 | -6.3 | 58.0 | 407.97 | 1.4 | -12.8 | 0.61 | 491/443 | not checked |
| 625 | `{"distance": 3.5, "max_candles": 6, "stop_atr": 4.75, "take_profit_atr": 2.5}` | 1,234.99 | 2.0 | -5.3 | 58.9 | 236.68 | 0.8 | -13.2 | 0.41 | 353/318 | not checked |
| 278 | `{"distance": 3.5, "max_candles": 6, "stop_atr": 5.0, "take_profit_atr": 2.5}` | 1,227.57 | 2.0 | -5.3 | 58.8 | 221.25 | 0.8 | -13.3 | 0.38 | 352/317 | not checked |
| 371 | `{"distance": 3.5, "max_candles": 6, "stop_atr": 5.75, "take_profit_atr": 2.5}` | 1,226.37 | 2.0 | -5.3 | 58.8 | 265.94 | 0.9 | -13.2 | 0.46 | 352/317 | not checked |
| 606 | `{"distance": 3.5, "max_candles": 6, "stop_atr": 5.75, "take_profit_atr": 2.0}` | 1,173.86 | 1.9 | -5.2 | 59.4 | 156.44 | 0.5 | -13.1 | 0.29 | 352/318 | not checked |
| 419 | `{"distance": 3.75, "max_candles": 6, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 1,032.15 | 1.7 | -4.0 | 61.5 | 604.23 | 2.0 | -10.5 | 1.23 | 252/239 | not checked |
| 854 | `{"distance": 3.75, "max_candles": 6, "stop_atr": 4.25, "take_profit_atr": 2.0}` | 999.56 | 1.6 | -3.8 | 61.9 | 396.63 | 1.4 | -10.6 | 0.83 | 252/239 | not checked |
| 300 | `{"distance": 3.75, "max_candles": 6, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 823.34 | 1.4 | -3.8 | 61.8 | 465.58 | 1.6 | -10.5 | 1.17 | 254/240 | not checked |
| 558 | `{"distance": 4.25, "max_candles": 8, "stop_atr": 4.5, "take_profit_atr": 2.5}` | 761.12 | 1.2 | -2.5 | 66.1 | 1,034.70 | 3.5 | -5.6 | 2.77 | 112/109 | not checked |
| 679 | `{"distance": 4.25, "max_candles": 6, "stop_atr": 4.5, "take_profit_atr": 2.5}` | 695.79 | 1.1 | -2.2 | 62.3 | 1,036.99 | 3.5 | -5.2 | 3.04 | 114/113 | not checked |
| 805 | `{"distance": 4.25, "max_candles": 6, "stop_atr": 4.5, "take_profit_atr": 3.0}` | 658.81 | 1.1 | -2.1 | 62.3 | 1,207.56 | 4.0 | -5.2 | 3.72 | 114/112 | not checked |
| 344 | `{"distance": 4.5, "max_candles": 6, "stop_atr": 4.5, "take_profit_atr": 2.5}` | 634.03 | 1.0 | -1.2 | 66.2 | 994.13 | 3.3 | -3.5 | 3.20 | 74/82 | not checked |
| 713 | `{"distance": 4.5, "max_candles": 6, "stop_atr": 4.5, "take_profit_atr": 3.0}` | 608.88 | 1.0 | -1.2 | 65.8 | 1,125.35 | 3.8 | -3.5 | 3.75 | 73/81 | not checked |
| 648 | `{"distance": 4.5, "max_candles": 4, "stop_atr": 4.5, "take_profit_atr": 2.5}` | 392.31 | 0.7 | -1.2 | 66.7 | 625.42 | 2.1 | -4.2 | 3.26 | 78/91 | not checked |
| 598 | `{"distance": 4.5, "max_candles": 4, "stop_atr": 4.5, "take_profit_atr": 2.0}` | 390.86 | 0.7 | -0.9 | 66.7 | 467.00 | 1.6 | -3.9 | 2.45 | 78/91 | not checked |
| 538 | `{"distance": 4.75, "max_candles": 6, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 275.18 | 0.5 | -0.9 | 69.4 | 752.32 | 2.5 | -3.0 | 5.52 | 49/62 | not checked |
| 808 | `{"distance": 4.75, "max_candles": 4, "stop_atr": 4.25, "take_profit_atr": 2.0}` | 213.64 | 0.4 | -0.8 | 72.2 | 274.47 | 0.9 | -3.1 | 2.61 | 54/66 | not checked |
| 397 | `{"distance": 4.5, "max_candles": 2, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 133.94 | 0.2 | -0.5 | 61.5 | 912.06 | 3.1 | -1.0 | 13.30 | 91/107 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 887 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
