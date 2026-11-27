# mfi_momentum_confirmation__broad: optimization summary

Updated 2026-11-26T04:55:51Z · backtest.py version `1f39108d70` · 921 parameter sets tested with this version (921 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [mfi_momentum_confirmation__broad__max-income__v002.md](mfi_momentum_confirmation__broad__max-income__v002.md) | 920 | `{"level": 85.0, "max_candles": 87, "stop_atr": 4.0, "take_profit_atr": 5.5}` | long FILUSDT since 2026-11-23 16:00 @ 0.573973 |
| balanced | [mfi_momentum_confirmation__broad__balanced__v002.md](mfi_momentum_confirmation__broad__balanced__v002.md) | 921 | `{"level": 90.0, "max_candles": 96, "stop_atr": 5.25, "take_profit_atr": 5.5}` | flat (data up to 2026-11-26 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 4,072.09 | 1,229.92 | 2,976.03 | 687.16 |
| return % | 40.72 | 12.30 | 29.76 | 6.87 |
| return %/year | 6.0 | 4.1 | 4.5 | 2.3 |
| gross profit | 17,270.76 | 7,531.83 | 7,929.22 | 4,199.75 |
| gross loss | 13,198.67 | 6,301.91 | 4,953.19 | 3,512.59 |
| trades | 796 | 572 | 361 | 265 |
| win rate % | 41.8 | 42.5 | 45.4 | 43.0 |
| avg win | 51.86 | 31.00 | 48.35 | 36.84 |
| avg loss | -28.51 | -19.15 | -25.14 | -23.26 |
| avg result / trade | 5.12 | 2.15 | 8.24 | 2.59 |
| largest single loss | -446.95 | -115.47 | -117.87 | -107.06 |
| largest loss % of equity | -14.82 | -15.94 | -14.89 | -15.46 |
| max drawdown | -2,263.61 | -874.97 | -526.63 | -710.75 |
| max drawdown % | -14.65 | -7.64 | -4.11 | -6.53 |
| profit factor | 1.31 | 1.20 | 1.60 | 1.20 |
| unusually bad trades | 84 | 46 | 35 | 26 |
| … threshold (% of equity) | 10.2 | 9.4 | 10.5 | 10.7 |
| time in market % | 2.8 | 4.1 | 1.3 | 2.0 |
| buy & hold return % | 450.49 | 71.18 | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.69 |  | 0.52 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -0.4 | -0.2 |
| 2019 | -1.5 | -1.3 |
| 2020 | 11.3 | 9.0 |
| 2021 | 29.8 | 17.6 |
| 2022 | -4.0 | 1.8 |
| 2023 | 3.5 | 0.9 |
| 2024 (OOS) | 9.5 | 7.9 |
| 2025 (OOS) | -3.4 | 0.4 |
| 2026 (OOS) | 3.7 | 0.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 14.7% from a peak in-sample and 7.6% out-of-sample, and the worst single trade cost 15.9% of the account out-of-sample. About 42 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 68% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 4.1% from a peak in-sample and 6.5% out-of-sample, and the worst single trade cost 15.5% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 2.3% a year against 4.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 474 | `{"level": 85.0, "max_candles": 42, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 4,097.20 | 6.0 | -14.6 | 42.0 | 1,231.24 | 4.1 | -7.6 | 0.68 | 796/572 | not checked |
| 887 | `{"level": 85.0, "max_candles": 42, "stop_atr": 5.0, "take_profit_atr": 5.5}` | 3,962.78 | 5.8 | -13.7 | 42.1 | 1,206.15 | 4.0 | -8.3 | 0.69 | 796/571 | not checked |
| 903 | `{"level": 80.0, "max_candles": 105, "stop_atr": 5.75, "take_profit_atr": 6.0}` | 3,777.75 | 5.6 | -12.8 | 42.1 | 2,492.76 | 8.0 | -11.0 | 1.43 | 1323/905 | not checked |
| 896 | `{"level": 80.0, "max_candles": 105, "stop_atr": 5.5, "take_profit_atr": 6.0}` | 3,651.34 | 5.4 | -12.8 | 42.1 | 2,503.39 | 8.0 | -11.0 | 1.49 | 1323/905 | not checked |
| 914 | `{"level": 80.0, "max_candles": 114, "stop_atr": 5.5, "take_profit_atr": 6.0}` | 3,651.34 | 5.4 | -12.8 | 42.1 | 2,503.39 | 8.0 | -11.0 | 1.49 | 1323/905 | not checked |
| 621 | `{"level": 82.5, "max_candles": 69, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 700 | `{"level": 82.5, "max_candles": 114, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 714 | `{"level": 82.5, "max_candles": 78, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 718 | `{"level": 82.5, "max_candles": 60, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 722 | `{"level": 82.5, "max_candles": 96, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 732 | `{"level": 82.5, "max_candles": 87, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 822 | `{"level": 82.5, "max_candles": 105, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 3,456.79 | 5.2 | -10.7 | 41.0 | 1,835.84 | 6.0 | -8.6 | 1.17 | 1026/696 | not checked |
| 854 | `{"level": 82.5, "max_candles": 51, "stop_atr": 5.0, "take_profit_atr": 5.5}` | 3,334.30 | 5.0 | -10.5 | 40.9 | 1,844.59 | 6.0 | -8.5 | 1.21 | 1026/696 | not checked |
| 488 | `{"level": 90.0, "max_candles": 105, "stop_atr": 5.75, "take_profit_atr": 5.5}` | 3,172.65 | 4.8 | -4.1 | 45.4 | 739.80 | 2.5 | -6.5 | 0.52 | 361/265 | not checked |
| 526 | `{"level": 90.0, "max_candles": 96, "stop_atr": 5.75, "take_profit_atr": 5.5}` | 3,172.65 | 4.8 | -4.1 | 45.4 | 739.80 | 2.5 | -6.5 | 0.52 | 361/265 | not checked |
| 396 | `{"level": 90.0, "max_candles": 87, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 2,976.03 | 4.5 | -4.1 | 45.4 | 687.16 | 2.3 | -6.5 | 0.52 | 361/265 | not checked |
| 397 | `{"level": 90.0, "max_candles": 96, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 2,976.03 | 4.5 | -4.1 | 45.4 | 687.16 | 2.3 | -6.5 | 0.52 | 361/265 | 1.00 |
| 507 | `{"level": 90.0, "max_candles": 105, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 2,976.03 | 4.5 | -4.1 | 45.4 | 687.16 | 2.3 | -6.5 | 0.52 | 361/265 | not checked |
| 375 | `{"level": 92.5, "max_candles": 87, "stop_atr": 5.75, "take_profit_atr": 5.5}` | 1,349.59 | 2.2 | -4.0 | 46.1 | 386.12 | 1.3 | -3.7 | 0.61 | 204/160 | not checked |
| 477 | `{"level": 92.5, "max_candles": 96, "stop_atr": 5.75, "take_profit_atr": 5.5}` | 1,349.59 | 2.2 | -4.0 | 46.1 | 386.12 | 1.3 | -3.7 | 0.61 | 204/160 | not checked |
| 498 | `{"level": 92.5, "max_candles": 105, "stop_atr": 5.75, "take_profit_atr": 5.5}` | 1,349.59 | 2.2 | -4.0 | 46.1 | 386.12 | 1.3 | -3.7 | 0.61 | 204/160 | not checked |
| 448 | `{"level": 92.5, "max_candles": 96, "stop_atr": 5.5, "take_profit_atr": 5.5}` | 1,327.27 | 2.1 | -3.9 | 46.1 | 395.93 | 1.4 | -3.7 | 0.63 | 204/160 | not checked |
| 862 | `{"level": 92.5, "max_candles": 105, "stop_atr": 5.5, "take_profit_atr": 5.5}` | 1,327.27 | 2.1 | -3.9 | 46.1 | 395.93 | 1.4 | -3.7 | 0.63 | 204/160 | not checked |
| 439 | `{"level": 90.0, "max_candles": 60, "stop_atr": 2.75, "take_profit_atr": 1.5}` | 693.51 | 1.1 | -3.9 | 65.7 | 351.87 | 1.2 | -2.7 | 1.05 | 367/273 | not checked |
| 749 | `{"level": 95.0, "max_candles": 15, "stop_atr": 5.0, "take_profit_atr": 6.0}` | 395.93 | 0.7 | -2.8 | 44.7 | 133.35 | 0.5 | -3.4 | 0.70 | 94/83 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 921 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
