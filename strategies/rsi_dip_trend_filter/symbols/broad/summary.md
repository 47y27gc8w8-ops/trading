# rsi_dip_trend_filter__broad: optimization summary

Updated 2026-11-25T22:42:23Z · backtest.py version `81be9c69a6` · 1,226 parameter sets tested with this version (1,226 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rsi_dip_trend_filter__broad__max-income__v002.md](rsi_dip_trend_filter__broad__max-income__v002.md) | 1226 | `{"buy": 16, "exit": 55, "max_candles": 24, "n": 6, "stop_atr": 4.0, "take_profit_atr": 3.0}` | flat (data up to 2026-11-25 16:00) |
| balanced | [rsi_dip_trend_filter__broad__balanced__v002.md](rsi_dip_trend_filter__broad__balanced__v002.md) | 1226 | `{"buy": 16, "exit": 55, "max_candles": 24, "n": 6, "stop_atr": 4.0, "take_profit_atr": 3.0}` | flat (data up to 2026-11-25 16:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,777.83 | 469.73 | 2,777.83 | 469.73 |
| return % | 27.78 | 4.70 | 27.78 | 4.70 |
| return %/year | 4.2 | 1.6 | 4.2 | 1.6 |
| gross profit | 5,298.87 | 2,333.18 | 5,298.87 | 2,333.18 |
| gross loss | 2,521.04 | 1,863.45 | 2,521.04 | 1,863.45 |
| trades | 382 | 268 | 382 | 268 |
| win rate % | 70.7 | 60.1 | 70.7 | 60.1 |
| avg win | 19.63 | 14.49 | 19.63 | 14.49 |
| avg loss | -22.51 | -17.42 | -22.51 | -17.42 |
| avg result / trade | 7.27 | 1.75 | 7.27 | 1.75 |
| largest single loss | -62.35 | -65.64 | -62.35 | -65.64 |
| largest loss % of equity | -16.59 | -17.06 | -16.59 | -17.06 |
| max drawdown | -494.65 | -1,025.99 | -494.65 | -1,025.99 |
| max drawdown % | -4.05 | -10.05 | -4.05 | -10.05 |
| profit factor | 2.10 | 1.25 | 2.10 | 1.25 |
| unusually bad trades | 15 | 28 | 15 | 28 |
| … threshold (% of equity) | 11.4 | 8.2 | 11.4 | 8.2 |
| time in market % | 1.0 | 1.4 | 1.0 | 1.4 |
| buy & hold return % | 450.49 | 71.18 | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.38 |  | 0.38 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -0.5 | -0.5 |
| 2019 | 1.3 | 1.3 |
| 2020 | 4.8 | 4.8 |
| 2021 | 13.0 | 13.0 |
| 2022 | 0.5 | 0.5 |
| 2023 | 6.5 | 6.5 |
| 2024 (OOS) | 2.9 | 2.9 |
| 2025 (OOS) | 3.1 | 3.1 |
| 2026 (OOS) | -1.1 | -1.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.0% from a peak in-sample and 10.1% out-of-sample, and the worst single trade cost 17.1% of the account out-of-sample. About 71 of every 100 trades won in-sample. Out-of-sample it earned 1.6% a year against 4.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 100% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 4.0% from a peak in-sample and 10.1% out-of-sample, and the worst single trade cost 17.1% of the account out-of-sample. About 71 of every 100 trades won in-sample. Out-of-sample it earned 1.6% a year against 4.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 100% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1142 | `{"buy": 20, "exit": 55, "max_candles": 28, "n": 7, "stop_atr": 4.75, "take_profit_atr": 3.0}` | 2,878.54 | 4.4 | -4.9 | 67.5 | 320.69 | 1.1 | -13.2 | 0.25 | 462/328 | not checked |
| 719 | `{"buy": 16, "exit": 55, "max_candles": 24, "n": 6, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 2,777.83 | 4.2 | -4.0 | 70.7 | 469.73 | 1.6 | -10.1 | 0.38 | 382/268 | 1.00 |
| 715 | `{"buy": 16, "exit": 55, "max_candles": 24, "n": 6, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,760.44 | 4.2 | -4.0 | 70.9 | 531.81 | 1.8 | -10.0 | 0.43 | 382/269 | not checked |
| 717 | `{"buy": 16, "exit": 55, "max_candles": 22, "n": 6, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 2,740.83 | 4.2 | -3.9 | 70.0 | 441.61 | 1.5 | -10.1 | 0.36 | 383/269 | not checked |
| 860 | `{"buy": 16, "exit": 55, "max_candles": 22, "n": 6, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,722.97 | 4.2 | -3.9 | 70.2 | 506.58 | 1.7 | -10.1 | 0.41 | 383/270 | not checked |
| 1092 | `{"buy": 20, "exit": 50, "max_candles": 28, "n": 8, "stop_atr": 4.75, "take_profit_atr": 3.0}` | 1,506.05 | 2.4 | -3.8 | 69.3 | 427.84 | 1.5 | -7.7 | 0.61 | 238/194 | not checked |
| 1053 | `{"buy": 20, "exit": 50, "max_candles": 28, "n": 8, "stop_atr": 4.5, "take_profit_atr": 3.0}` | 1,493.03 | 2.4 | -3.7 | 69.3 | 480.32 | 1.6 | -7.8 | 0.69 | 238/195 | not checked |
| 1153 | `{"buy": 20, "exit": 45, "max_candles": 26, "n": 8, "stop_atr": 4.5, "take_profit_atr": 3.0}` | 1,479.17 | 2.4 | -3.3 | 69.9 | 224.85 | 0.8 | -7.6 | 0.33 | 239/197 | not checked |
| 933 | `{"buy": 20, "exit": 45, "max_candles": 26, "n": 8, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 1,407.44 | 2.2 | -3.3 | 69.6 | 216.63 | 0.7 | -7.5 | 0.33 | 240/199 | not checked |
| 1186 | `{"buy": 22, "exit": 45, "max_candles": 26, "n": 9, "stop_atr": 4.5, "take_profit_atr": 3.0}` | 1,287.09 | 2.1 | -3.1 | 68.1 | 390.74 | 1.3 | -6.9 | 0.64 | 226/181 | not checked |
| 926 | `{"buy": 14, "exit": 50, "max_candles": 26, "n": 6, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 1,160.04 | 1.9 | -2.9 | 68.1 | 281.10 | 1.0 | -6.6 | 0.51 | 232/180 | not checked |
| 956 | `{"buy": 14, "exit": 45, "max_candles": 28, "n": 6, "stop_atr": 3.5, "take_profit_atr": 3.5}` | 1,143.58 | 1.9 | -2.9 | 70.1 | 143.54 | 0.5 | -7.1 | 0.27 | 234/180 | not checked |
| 832 | `{"buy": 20, "exit": 60, "max_candles": 14, "n": 9, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 1,009.35 | 1.6 | -2.8 | 59.6 | 900.15 | 3.0 | -5.2 | 1.84 | 146/115 | not checked |
| 853 | `{"buy": 20, "exit": 65, "max_candles": 14, "n": 9, "stop_atr": 4.75, "take_profit_atr": 3.5}` | 946.78 | 1.5 | -2.8 | 58.9 | 950.39 | 3.2 | -5.1 | 2.07 | 146/115 | not checked |
| 1051 | `{"buy": 20, "exit": 45, "max_candles": 26, "n": 9, "stop_atr": 4.25, "take_profit_atr": 3.5}` | 885.33 | 1.4 | -2.7 | 68.8 | 575.02 | 1.9 | -4.8 | 1.35 | 144/116 | not checked |
| 1154 | `{"buy": 20, "exit": 45, "max_candles": 24, "n": 9, "stop_atr": 4.5, "take_profit_atr": 3.5}` | 876.89 | 1.4 | -2.6 | 68.8 | 660.37 | 2.2 | -4.8 | 1.56 | 144/116 | not checked |
| 1054 | `{"buy": 20, "exit": 45, "max_candles": 26, "n": 9, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 876.73 | 1.4 | -2.6 | 68.8 | 553.70 | 1.9 | -4.8 | 1.31 | 144/117 | not checked |
| 1182 | `{"buy": 20, "exit": 50, "max_candles": 26, "n": 9, "stop_atr": 4.5, "take_profit_atr": 3.0}` | 862.77 | 1.4 | -2.5 | 69.2 | 644.76 | 2.2 | -5.1 | 1.55 | 143/116 | not checked |
| 1224 | `{"buy": 18, "exit": 50, "max_candles": 26, "n": 8, "stop_atr": 4.75, "take_profit_atr": 3.0}` | 838.66 | 1.4 | -2.5 | 69.1 | 632.52 | 2.1 | -4.9 | 1.56 | 152/120 | not checked |
| 288 | `{"buy": 20, "exit": 65, "max_candles": 12, "n": 9, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 824.91 | 1.4 | -2.2 | 55.5 | 708.31 | 2.4 | -5.5 | 1.77 | 146/117 | not checked |
| 697 | `{"buy": 20, "exit": 60, "max_candles": 12, "n": 9, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 812.77 | 1.3 | -2.2 | 55.5 | 705.77 | 2.4 | -5.6 | 1.79 | 146/117 | not checked |
| 289 | `{"buy": 20, "exit": 70, "max_candles": 12, "n": 9, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 747.06 | 1.2 | -2.2 | 54.7 | 728.38 | 2.5 | -5.4 | 2.00 | 148/117 | not checked |
| 1004 | `{"buy": 14, "exit": 50, "max_candles": 26, "n": 7, "stop_atr": 4.25, "take_profit_atr": 2.5}` | 549.54 | 0.9 | -1.8 | 71.6 | 464.05 | 1.6 | -4.7 | 1.74 | 95/76 | not checked |
| 1045 | `{"buy": 14, "exit": 50, "max_candles": 26, "n": 7, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 501.75 | 0.8 | -1.7 | 71.6 | 476.95 | 1.6 | -4.6 | 1.95 | 95/76 | not checked |
| 813 | `{"buy": 16, "exit": 60, "max_candles": 14, "n": 9, "stop_atr": 4.75, "take_profit_atr": 4.0}` | 299.76 | 0.5 | -1.4 | 65.8 | 513.45 | 1.8 | -2.7 | 3.50 | 41/28 | not checked |

(5 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,226 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
