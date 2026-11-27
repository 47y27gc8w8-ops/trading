# volume_weighted_ma_cross__broad: optimization summary

Updated 2026-11-26T05:12:25Z · backtest.py version `92af7b89e5` · 784 parameter sets tested with this version (784 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [volume_weighted_ma_cross__broad__max-income__v001.md](volume_weighted_ma_cross__broad__max-income__v001.md) | 284 | `{"fast": 10, "max_candles": 87, "slow": 70, "stop_atr": 2.0, "take_profit_atr": 10.5}` | flat (data up to 2026-11-26 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 11,562.10 | 1,666.46 |
| return % | 115.62 | 16.66 |
| return %/year | 13.9 | 5.5 |
| gross profit | 44,875.40 | 16,585.46 |
| gross loss | 33,313.30 | 14,919.00 |
| trades | 1,913 | 1,372 |
| win rate % | 26.9 | 26.5 |
| avg win | 87.31 | 45.69 |
| avg loss | -23.81 | -14.79 |
| avg result / trade | 6.04 | 1.21 |
| largest single loss | -229.16 | -216.89 |
| largest loss % of equity | -8.76 | -15.64 |
| max drawdown | -5,424.86 | -2,899.54 |
| max drawdown % | -26.59 | -24.34 |
| profit factor | 1.35 | 1.11 |
| unusually bad trades | 79 | 39 |
| … threshold (% of equity) | 9.3 | 8.4 |
| time in market % | 11.3 | 15.5 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.39 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | 2.4 |
| 2019 | 1.3 |
| 2020 | 22.3 |
| 2021 | 49.9 |
| 2022 | -20.6 |
| 2023 | 42.8 |
| 2024 (OOS) | 10.2 |
| 2025 (OOS) | 1.0 |
| 2026 (OOS) | 11.8 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 26.6% from a peak in-sample and 24.3% out-of-sample, and the worst single trade cost 15.6% of the account out-of-sample. About 27 of every 100 trades won in-sample. Out-of-sample it earned 5.5% a year against 13.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 37 | `{"fast": 10, "max_candles": 87, "slow": 70, "stop_atr": 2.0, "take_profit_atr": 10.5}` | 11,562.10 | 13.9 | -26.6 | 26.9 | 1,666.46 | 5.5 | -24.3 | 0.39 | 1913/1372 | 1.00 |
| 397 | `{"fast": 9, "max_candles": 87, "slow": 70, "stop_atr": 1.75, "take_profit_atr": 10.5}` | 8,899.61 | 11.4 | -26.0 | 25.1 | 1,073.34 | 3.6 | -24.9 | 0.32 | 1963/1426 | not checked |
| 320 | `{"fast": 9, "max_candles": 96, "slow": 70, "stop_atr": 1.75, "take_profit_atr": 10.5}` | 8,865.88 | 11.3 | -25.0 | 25.1 | 1,112.31 | 3.7 | -25.0 | 0.33 | 1963/1426 | not checked |
| 740 | `{"fast": 7, "max_candles": 42, "slow": 45, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 8,806.88 | 11.3 | -20.7 | 32.9 | 909.66 | 3.0 | -23.3 | 0.27 | 2702/1938 | not checked |
| 710 | `{"fast": 7, "max_candles": 42, "slow": 50, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 6,926.21 | 9.3 | -18.0 | 31.9 | 2,142.17 | 6.9 | -17.3 | 0.74 | 2522/1894 | not checked |
| 683 | `{"fast": 7, "max_candles": 42, "slow": 50, "stop_atr": 2.0, "take_profit_atr": 5.5}` | 5,068.87 | 7.2 | -17.9 | 32.3 | 1,967.41 | 6.4 | -17.0 | 0.89 | 2522/1894 | not checked |
| 733 | `{"fast": 7, "max_candles": 33, "slow": 50, "stop_atr": 2.0, "take_profit_atr": 6.0}` | 4,899.20 | 7.0 | -17.5 | 33.8 | 1,761.14 | 5.8 | -16.8 | 0.83 | 2522/1894 | not checked |
| 368 | `{"fast": 10, "max_candles": 33, "slow": 60, "stop_atr": 2.0, "take_profit_atr": 4.0}` | 2,845.83 | 4.3 | -16.6 | 38.3 | 534.38 | 1.8 | -17.1 | 0.42 | 2071/1466 | not checked |
| 494 | `{"fast": 10, "max_candles": 33, "slow": 60, "stop_atr": 2.25, "take_profit_atr": 3.5}` | 2,665.76 | 4.1 | -16.5 | 41.9 | 331.43 | 1.1 | -16.9 | 0.28 | 2071/1466 | not checked |
| 362 | `{"fast": 10, "max_candles": 33, "slow": 60, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 2,324.80 | 3.6 | -15.8 | 40.1 | 313.62 | 1.1 | -14.5 | 0.30 | 2071/1466 | not checked |
| 427 | `{"fast": 10, "max_candles": 24, "slow": 60, "stop_atr": 2.0, "take_profit_atr": 3.5}` | 1,688.75 | 2.7 | -15.7 | 40.5 | 204.30 | 0.7 | -13.9 | 0.26 | 2071/1466 | not checked |
| 435 | `{"fast": 7, "max_candles": 33, "slow": 50, "stop_atr": 1.25, "take_profit_atr": 5.0}` | 1,606.34 | 2.5 | -15.6 | 26.7 | 246.41 | 0.8 | -14.6 | 0.33 | 2522/1894 | not checked |
| 509 | `{"fast": 10, "max_candles": 24, "slow": 60, "stop_atr": 1.75, "take_profit_atr": 3.5}` | 1,182.48 | 1.9 | -14.3 | 38.1 | 233.28 | 0.8 | -12.1 | 0.42 | 2071/1466 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 784 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
