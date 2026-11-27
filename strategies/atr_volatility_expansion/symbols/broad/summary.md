# atr_volatility_expansion__broad: optimization summary

Updated 2026-11-25T23:05:35Z · backtest.py version `2d6341ae0f` · 753 parameter sets tested with this version (753 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [atr_volatility_expansion__broad__max-income__v001.md](atr_volatility_expansion__broad__max-income__v001.md) | 214 | `{"k": 3.0, "max_candles": 33, "stop_atr": 4.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 16:00) |
| balanced | [atr_volatility_expansion__broad__balanced__v002.md](atr_volatility_expansion__broad__balanced__v002.md) | 753 | `{"k": 3.25, "max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 16:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,081.48 | 1,121.52 | 1,140.08 | 682.99 |
| return % | 20.81 | 11.22 | 11.40 | 6.83 |
| return %/year | 3.2 | 3.7 | 1.8 | 2.3 |
| gross profit | 9,593.90 | 6,350.43 | 6,374.61 | 4,206.06 |
| gross loss | 7,512.42 | 5,228.91 | 5,234.53 | 3,523.07 |
| trades | 715 | 591 | 563 | 449 |
| win rate % | 40.1 | 36.5 | 48.9 | 44.5 |
| avg win | 33.43 | 29.40 | 23.18 | 21.03 |
| avg loss | -17.55 | -13.94 | -18.18 | -14.15 |
| avg result / trade | 2.91 | 1.90 | 2.03 | 1.52 |
| largest single loss | -91.14 | -82.88 | -69.66 | -57.10 |
| largest loss % of equity | -18.21 | -19.37 | -12.45 | -19.00 |
| max drawdown | -770.39 | -809.32 | -330.51 | -496.30 |
| max drawdown % | -6.68 | -6.90 | -3.01 | -4.52 |
| profit factor | 1.28 | 1.21 | 1.22 | 1.19 |
| unusually bad trades | 80 | 65 | 38 | 37 |
| … threshold (% of equity) | 8.1 | 6.4 | 9.2 | 7.3 |
| time in market % | 1.5 | 2.6 | 0.7 | 1.3 |
| buy & hold return % | 450.49 | 71.18 | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.15 |  | 1.25 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | 1.0 | 0.6 |
| 2019 | 3.7 | 2.4 |
| 2020 | 0.8 | 3.1 |
| 2021 | 2.7 | 1.0 |
| 2022 | 2.1 | 2.3 |
| 2023 | 9.2 | 1.5 |
| 2024 (OOS) | 6.1 | 3.7 |
| 2025 (OOS) | 8.1 | 5.0 |
| 2026 (OOS) | -4.3 | -1.8 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 6.7% from a peak in-sample and 6.9% out-of-sample, and the worst single trade cost 19.4% of the account out-of-sample. About 40 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.0% from a peak in-sample and 4.5% out-of-sample, and the worst single trade cost 19.0% of the account out-of-sample. About 49 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 347 | `{"k": 3.0, "max_candles": 24, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 2,169.99 | 3.4 | -6.0 | 40.1 | 1,164.97 | 3.9 | -6.8 | 1.15 | 716/591 | not checked |
| 278 | `{"k": 3.0, "max_candles": 24, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 2,083.52 | 3.2 | -6.0 | 40.1 | 1,076.27 | 3.6 | -6.8 | 1.11 | 716/591 | not checked |
| 220 | `{"k": 3.25, "max_candles": 24, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 2,051.35 | 3.2 | -4.7 | 40.2 | 1,359.63 | 4.5 | -4.6 | 1.40 | 552/438 | not checked |
| 388 | `{"k": 3.0, "max_candles": 24, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 1,907.36 | 3.0 | -4.7 | 39.9 | 1,156.05 | 3.9 | -6.3 | 1.28 | 719/592 | not checked |
| 380 | `{"k": 3.25, "max_candles": 24, "stop_atr": 3.0, "take_profit_atr": 5.0}` | 1,896.59 | 3.0 | -4.3 | 39.9 | 1,278.06 | 4.2 | -4.6 | 1.42 | 552/438 | not checked |
| 418 | `{"k": 3.25, "max_candles": 24, "stop_atr": 2.75, "take_profit_atr": 5.0}` | 1,703.65 | 2.7 | -4.0 | 39.5 | 1,247.04 | 4.1 | -4.7 | 1.53 | 552/439 | not checked |
| 440 | `{"k": 3.25, "max_candles": 24, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 1,657.33 | 2.6 | -3.8 | 39.0 | 1,036.22 | 3.5 | -5.4 | 1.32 | 554/439 | not checked |
| 221 | `{"k": 3.25, "max_candles": 87, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 1,209.97 | 1.9 | -3.8 | 49.6 | 1,134.44 | 3.8 | -3.9 | 1.94 | 562/448 | not checked |
| 232 | `{"k": 3.25, "max_candles": 96, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 1,209.97 | 1.9 | -3.8 | 49.6 | 1,134.44 | 3.8 | -3.9 | 1.94 | 562/448 | not checked |
| 301 | `{"k": 3.25, "max_candles": 78, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 1,209.97 | 1.9 | -3.8 | 49.6 | 1,134.44 | 3.8 | -3.9 | 1.94 | 562/448 | not checked |
| 334 | `{"k": 3.25, "max_candles": 105, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 1,209.97 | 1.9 | -3.8 | 49.6 | 1,134.44 | 3.8 | -3.9 | 1.94 | 562/448 | not checked |
| 613 | `{"k": 3.25, "max_candles": 114, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 1,209.97 | 1.9 | -3.8 | 49.6 | 1,134.44 | 3.8 | -3.9 | 1.94 | 562/448 | not checked |
| 664 | `{"k": 3.25, "max_candles": 69, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 1,209.97 | 1.9 | -3.8 | 49.6 | 1,134.44 | 3.8 | -3.9 | 1.94 | 562/448 | not checked |
| 235 | `{"k": 3.25, "max_candles": 87, "stop_atr": 3.0, "take_profit_atr": 2.5}` | 1,203.81 | 1.9 | -3.5 | 49.5 | 1,045.67 | 3.5 | -3.9 | 1.80 | 562/448 | not checked |
| 236 | `{"k": 3.25, "max_candles": 105, "stop_atr": 3.0, "take_profit_atr": 2.5}` | 1,203.81 | 1.9 | -3.5 | 49.5 | 1,045.67 | 3.5 | -3.9 | 1.80 | 562/448 | not checked |
| 237 | `{"k": 3.25, "max_candles": 96, "stop_atr": 3.0, "take_profit_atr": 2.5}` | 1,203.81 | 1.9 | -3.5 | 49.5 | 1,045.67 | 3.5 | -3.9 | 1.80 | 562/448 | 1.00 |
| 332 | `{"k": 3.25, "max_candles": 78, "stop_atr": 3.0, "take_profit_atr": 2.5}` | 1,203.81 | 1.9 | -3.5 | 49.5 | 1,045.67 | 3.5 | -3.9 | 1.80 | 562/448 | not checked |
| 414 | `{"k": 3.25, "max_candles": 69, "stop_atr": 3.0, "take_profit_atr": 2.5}` | 1,203.81 | 1.9 | -3.5 | 49.5 | 1,045.67 | 3.5 | -3.9 | 1.80 | 562/448 | not checked |
| 715 | `{"k": 3.25, "max_candles": 87, "stop_atr": 2.5, "take_profit_atr": 2.5}` | 1,140.08 | 1.8 | -3.0 | 48.9 | 682.99 | 2.3 | -4.5 | 1.25 | 563/449 | not checked |
| 716 | `{"k": 3.25, "max_candles": 105, "stop_atr": 2.5, "take_profit_atr": 2.5}` | 1,140.08 | 1.8 | -3.0 | 48.9 | 682.99 | 2.3 | -4.5 | 1.25 | 563/449 | not checked |
| 717 | `{"k": 3.25, "max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 2.5}` | 1,140.08 | 1.8 | -3.0 | 48.9 | 682.99 | 2.3 | -4.5 | 1.25 | 563/449 | 1.00 |
| 712 | `{"k": 3.25, "max_candles": 96, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 970.96 | 1.6 | -2.7 | 47.7 | 677.14 | 2.3 | -4.4 | 1.45 | 564/449 | not checked |
| 739 | `{"k": 3.25, "max_candles": 87, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 970.96 | 1.6 | -2.7 | 47.7 | 677.14 | 2.3 | -4.4 | 1.45 | 564/449 | not checked |
| 263 | `{"k": 3.25, "max_candles": 114, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 823.32 | 1.4 | -2.6 | 53.8 | 358.52 | 1.2 | -3.8 | 0.90 | 563/450 | not checked |
| 594 | `{"k": 3.25, "max_candles": 87, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 823.32 | 1.4 | -2.6 | 53.8 | 358.52 | 1.2 | -3.8 | 0.90 | 563/450 | not checked |

(2 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 753 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
