# rolling_resistance_retest__broad: optimization summary

Updated 2026-11-26T01:41:38Z · backtest.py version `b2278f94a6` · 916 parameter sets tested with this version (916 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rolling_resistance_retest__broad__max-income__v002.md](rolling_resistance_retest__broad__max-income__v002.md) | 916 | `{"max_candles": 42, "n": 7, "stop_atr": 3.75, "take_profit_atr": 9.5}` | flat (data up to 2026-11-25 16:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 6,690.34 | 881.01 |
| return % | 66.90 | 8.81 |
| return %/year | 9.1 | 3.0 |
| gross profit | 25,407.78 | 9,980.51 |
| gross loss | 18,717.43 | 9,099.50 |
| trades | 1,222 | 941 |
| win rate % | 29.8 | 27.9 |
| avg win | 69.80 | 37.95 |
| avg loss | -21.82 | -13.42 |
| avg result / trade | 5.47 | 0.94 |
| largest single loss | -439.61 | -128.80 |
| largest loss % of equity | -10.64 | -30.96 |
| max drawdown | -1,608.35 | -1,265.14 |
| max drawdown % | -10.28 | -11.09 |
| profit factor | 1.36 | 1.10 |
| unusually bad trades | 103 | 64 |
| … threshold (% of equity) | 8.8 | 6.9 |
| time in market % | 5.5 | 8.6 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.33 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | -2.5 |
| 2019 | -0.2 |
| 2020 | 8.2 |
| 2021 | 42.1 |
| 2022 | 3.5 |
| 2023 | 7.8 |
| 2024 (OOS) | 13.3 |
| 2025 (OOS) | -5.7 |
| 2026 (OOS) | -0.7 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 10.3% from a peak in-sample and 11.1% out-of-sample, and the worst single trade cost 31.0% of the account out-of-sample. About 30 of every 100 trades won in-sample. Out-of-sample it earned 3.0% a year against 9.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 90% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 453 | `{"max_candles": 42, "n": 7, "stop_atr": 3.0, "take_profit_atr": 9.5}` | 6,822.43 | 9.2 | -9.9 | 29.2 | 859.44 | 2.9 | -10.7 | 0.31 | 1224/942 | not checked |
| 697 | `{"max_candles": 42, "n": 7, "stop_atr": 2.75, "take_profit_atr": 9.5}` | 6,362.44 | 8.7 | -9.6 | 28.8 | 804.32 | 2.7 | -10.5 | 0.31 | 1224/943 | not checked |
| 626 | `{"max_candles": 42, "n": 7, "stop_atr": 2.75, "take_profit_atr": 10.5}` | 5,683.50 | 7.9 | -9.5 | 28.3 | 1,164.22 | 3.9 | -10.3 | 0.49 | 1221/943 | not checked |
| 370 | `{"max_candles": 42, "n": 7, "stop_atr": 4.0, "take_profit_atr": 8.0}` | 5,166.53 | 7.3 | -9.4 | 30.2 | 911.48 | 3.1 | -10.7 | 0.42 | 1230/945 | 1.00 |
| 375 | `{"max_candles": 42, "n": 7, "stop_atr": 3.75, "take_profit_atr": 8.0}` | 5,124.67 | 7.2 | -9.3 | 30.2 | 674.38 | 2.3 | -11.2 | 0.31 | 1230/945 | not checked |
| 753 | `{"max_candles": 42, "n": 7, "stop_atr": 3.0, "take_profit_atr": 8.0}` | 5,062.58 | 7.2 | -8.8 | 29.6 | 676.71 | 2.3 | -10.7 | 0.32 | 1232/946 | not checked |
| 755 | `{"max_candles": 42, "n": 7, "stop_atr": 2.75, "take_profit_atr": 8.0}` | 4,859.01 | 6.9 | -8.7 | 29.3 | 641.05 | 2.2 | -10.5 | 0.31 | 1232/947 | not checked |
| 612 | `{"max_candles": 24, "n": 7, "stop_atr": 4.25, "take_profit_atr": 9.0}` | 4,440.12 | 6.4 | -8.4 | 34.4 | 1,020.20 | 3.4 | -7.6 | 0.53 | 1260/968 | not checked |
| 604 | `{"max_candles": 24, "n": 7, "stop_atr": 4.25, "take_profit_atr": 9.5}` | 4,295.00 | 6.2 | -8.3 | 34.4 | 1,037.71 | 3.5 | -7.4 | 0.56 | 1260/968 | not checked |
| 514 | `{"max_candles": 24, "n": 7, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 2,443.91 | 3.8 | -8.0 | 34.4 | 739.33 | 2.5 | -8.3 | 0.66 | 1266/968 | not checked |
| 496 | `{"max_candles": 24, "n": 7, "stop_atr": 4.25, "take_profit_atr": 6.5}` | 2,299.40 | 3.6 | -7.8 | 34.7 | 542.81 | 1.8 | -8.5 | 0.52 | 1268/969 | not checked |
| 346 | `{"max_candles": 24, "n": 7, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 2,282.90 | 3.5 | -7.6 | 34.6 | 581.68 | 2.0 | -8.3 | 0.56 | 1268/969 | not checked |
| 674 | `{"max_candles": 15, "n": 7, "stop_atr": 4.25, "take_profit_atr": 9.0}` | 1,690.39 | 2.7 | -7.3 | 37.9 | 1,216.37 | 4.0 | -7.5 | 1.51 | 1287/985 | not checked |
| 694 | `{"max_candles": 15, "n": 7, "stop_atr": 4.0, "take_profit_atr": 7.5}` | 1,034.23 | 1.7 | -7.2 | 38.0 | 937.56 | 3.1 | -8.1 | 1.88 | 1289/986 | not checked |
| 567 | `{"max_candles": 15, "n": 7, "stop_atr": 4.5, "take_profit_atr": 7.5}` | 1,012.80 | 1.6 | -7.1 | 38.0 | 941.70 | 3.2 | -8.1 | 1.93 | 1289/986 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 916 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
