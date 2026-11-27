# bollinger_keltner_compression_release__broad: optimization summary

Updated 2026-11-26T00:11:22Z · backtest.py version `f9522f49d9` · 8,946 parameter sets tested with this version (8,946 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [bollinger_keltner_compression_release__broad__max-income__v001.md](bollinger_keltner_compression_release__broad__max-income__v001.md) | 3118 | `{"k": 1.7, "max_candles": 33, "stop_atr": 3.0, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 16:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 184.63 | 1,059.20 |
| return % | 1.85 | 10.59 |
| return %/year | 0.3 | 3.5 |
| gross profit | 24,554.23 | 13,277.78 |
| gross loss | 24,369.59 | 12,218.58 |
| trades | 2,120 | 1,424 |
| win rate % | 31.0 | 34.5 |
| avg win | 37.37 | 27.04 |
| avg loss | -16.66 | -13.10 |
| avg result / trade | 0.09 | 0.74 |
| largest single loss | -122.09 | -70.52 |
| largest loss % of equity | -14.21 | -8.81 |
| max drawdown | -4,954.11 | -2,495.65 |
| max drawdown % | -33.26 | -18.41 |
| profit factor | 1.01 | 1.09 |
| unusually bad trades | 194 | 108 |
| … threshold (% of equity) | 7.6 | 6.1 |
| time in market % | 5.7 | 8.4 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 11.42 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | -0.8 |
| 2019 | 4.8 |
| 2020 | 14.2 |
| 2021 | 14.1 |
| 2022 | -18.4 |
| 2023 | -7.7 |
| 2024 (OOS) | 19.2 |
| 2025 (OOS) | 5.9 |
| 2026 (OOS) | -10.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 33.3% from a peak in-sample and 18.4% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 31 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3024 | `{"k": 1.7, "max_candles": 33, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 201.18 | 0.3 | -36.6 | 30.9 | 1,510.98 | 5.0 | -18.3 | 14.65 | 2115/1423 | 0.57 |
| 3068 | `{"k": 1.7, "max_candles": 33, "stop_atr": 3.0, "take_profit_atr": 5.5}` | 184.63 | 0.3 | -33.3 | 31.0 | 1,059.20 | 3.5 | -18.4 | 11.42 | 2120/1424 | 0.62 |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 8,946 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
