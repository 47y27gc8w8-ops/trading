# three_bar_momentum_thrust__broad: optimization summary

Updated 2026-11-26T01:55:20Z · backtest.py version `b419c00cd0` · 807 parameter sets tested with this version (807 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [three_bar_momentum_thrust__broad__max-income__v002.md](three_bar_momentum_thrust__broad__max-income__v002.md) | 807 | `{"max_candles": 51, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | flat (data up to 2026-11-25 16:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 1,710.35 | 770.18 |
| return % | 17.10 | 7.70 |
| return %/year | 2.7 | 2.6 |
| gross profit | 23,219.15 | 7,462.78 |
| gross loss | 21,508.81 | 6,692.60 |
| trades | 1,514 | 707 |
| win rate % | 32.9 | 33.2 |
| avg win | 46.62 | 31.76 |
| avg loss | -21.17 | -14.18 |
| avg result / trade | 1.13 | 1.09 |
| largest single loss | -646.02 | -100.62 |
| largest loss % of equity | -19.24 | -14.27 |
| max drawdown | -6,605.95 | -1,289.78 |
| max drawdown % | -36.92 | -11.30 |
| profit factor | 1.08 | 1.11 |
| unusually bad trades | 106 | 66 |
| … threshold (% of equity) | 8.2 | 6.8 |
| time in market % | 1.9 | 1.7 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.96 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | -2.0 |
| 2019 | 1.0 |
| 2020 | 4.2 |
| 2021 | 25.0 |
| 2022 | -6.2 |
| 2023 | -3.2 |
| 2024 (OOS) | 32.8 |
| 2025 (OOS) | -12.5 |
| 2026 (OOS) | -2.5 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 36.9% from a peak in-sample and 11.3% out-of-sample, and the worst single trade cost 14.3% of the account out-of-sample. About 33 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 27% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 278 | `{"max_candles": 51, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 292 | `{"max_candles": 60, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 361 | `{"max_candles": 42, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 418 | `{"max_candles": 33, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 431 | `{"max_candles": 69, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 473 | `{"max_candles": 78, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 480 | `{"max_candles": 87, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 495 | `{"max_candles": 96, "roc": 9.5, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 1,711.65 | 2.7 | -37.0 | 32.9 | 750.71 | 2.5 | -11.3 | 0.93 | 1514/707 | not checked |
| 281 | `{"max_candles": 42, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 282 | `{"max_candles": 60, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 283 | `{"max_candles": 51, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | 1.00 |
| 312 | `{"max_candles": 33, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 430 | `{"max_candles": 69, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 454 | `{"max_candles": 78, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 503 | `{"max_candles": 87, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 504 | `{"max_candles": 96, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 1,710.35 | 2.7 | -36.9 | 32.9 | 770.18 | 2.6 | -11.3 | 0.96 | 1514/707 | not checked |
| 229 | `{"max_candles": 51, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 1,539.36 | 2.5 | -36.0 | 33.1 | 585.13 | 2.0 | -11.8 | 0.81 | 1524/715 | not checked |
| 253 | `{"max_candles": 42, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 1,539.36 | 2.5 | -36.0 | 33.1 | 585.13 | 2.0 | -11.8 | 0.81 | 1524/715 | not checked |
| 777 | `{"max_candles": 33, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.0}` | 1,539.36 | 2.5 | -36.0 | 33.1 | 585.13 | 2.0 | -11.8 | 0.81 | 1524/715 | not checked |
| 276 | `{"max_candles": 60, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 1,513.63 | 2.4 | -34.9 | 33.1 | 652.67 | 2.2 | -11.9 | 0.92 | 1518/709 | not checked |
| 280 | `{"max_candles": 51, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 1,513.63 | 2.4 | -34.9 | 33.1 | 652.67 | 2.2 | -11.9 | 0.92 | 1518/709 | not checked |
| 417 | `{"max_candles": 42, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 1,513.63 | 2.4 | -34.9 | 33.1 | 652.67 | 2.2 | -11.9 | 0.92 | 1518/709 | not checked |
| 440 | `{"max_candles": 33, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 1,513.63 | 2.4 | -34.9 | 33.1 | 652.67 | 2.2 | -11.9 | 0.92 | 1518/709 | not checked |
| 486 | `{"max_candles": 78, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 1,513.63 | 2.4 | -34.9 | 33.1 | 652.67 | 2.2 | -11.9 | 0.92 | 1518/709 | not checked |
| 506 | `{"max_candles": 87, "roc": 9.5, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 1,513.63 | 2.4 | -34.9 | 33.1 | 652.67 | 2.2 | -11.9 | 0.92 | 1518/709 | not checked |

(57 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 807 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
