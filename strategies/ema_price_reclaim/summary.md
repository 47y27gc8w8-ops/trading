# ema_price_reclaim: optimization summary

Updated 2026-11-26T03:40:20Z · backtest.py version `2f1c7c7526` · 26,460 parameter sets tested with this version (26,460 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [ema_price_reclaim__max-income__v001.md](ema_price_reclaim__max-income__v001.md) | 26460 | `{"max_candles": 48, "n": 140, "stop_atr": 0.75, "take_profit_atr": 5.5}` | flat (data up to 2026-11-25 16:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 6,621.05 | 779.68 |
| return % | 66.21 | 7.80 |
| return %/year | 9.0 | 2.6 |
| gross profit | 18,549.77 | 3,864.15 |
| gross loss | 11,928.72 | 3,084.47 |
| trades | 81 | 31 |
| win rate % | 21.0 | 19.4 |
| avg win | 1,091.16 | 644.03 |
| avg loss | -186.39 | -123.38 |
| avg result / trade | 81.74 | 25.15 |
| largest single loss | -514.56 | -205.05 |
| largest loss % of equity | -4.38 | -1.76 |
| max drawdown | -3,285.85 | -2,502.36 |
| max drawdown % | -25.76 | -19.44 |
| profit factor | 1.55 | 1.25 |
| unusually bad trades | 7 | 0 |
| … threshold (% of equity) | 2.7 | 2.1 |
| time in market % | 5.3 | 5.7 |
| buy & hold return % | 313.33 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | 6.9 |
| 2019 | 3.3 |
| 2020 | -4.5 |
| 2021 | 16.4 |
| 2022 | 21.6 |
| 2023 | 12.7 |
| 2024 (OOS) | 11.6 |
| 2025 (OOS) | -4.1 |
| 2026 (OOS) | -0.5 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 25.8% from a peak in-sample and 19.4% out-of-sample, and the worst single trade cost 1.8% of the account out-of-sample. About 21 of every 100 trades won in-sample. Out-of-sample it earned 2.6% a year against 9.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 39% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 24456 | `{"max_candles": 48, "n": 140, "stop_atr": 0.75, "take_profit_atr": 5.5}` | 6,621.05 | 9.0 | -25.8 | 21.0 | 779.68 | 2.6 | -19.4 | 0.29 | 81/31 | 0.88 |
| 18869 | `{"max_candles": 48, "n": 140, "stop_atr": 0.5, "take_profit_atr": 5.0}` | 5,746.08 | 8.0 | -25.1 | 16.1 | 678.14 | 2.3 | -13.0 | 0.29 | 81/31 | 1.00 |
| 19268 | `{"max_candles": 156, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 20336 | `{"max_candles": 138, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 21172 | `{"max_candles": 120, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 22264 | `{"max_candles": 102, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 22377 | `{"max_candles": 174, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 24412 | `{"max_candles": 66, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 24779 | `{"max_candles": 48, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 24876 | `{"max_candles": 84, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 25021 | `{"max_candles": 192, "n": 150, "stop_atr": 0.75, "take_profit_atr": 4.0}` | 4,786.32 | 6.8 | -21.3 | 21.8 | 1,290.45 | 4.3 | -9.8 | 0.63 | 78/31 | not checked |
| 18847 | `{"max_candles": 156, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 19633 | `{"max_candles": 102, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 20564 | `{"max_candles": 174, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 21577 | `{"max_candles": 66, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 22670 | `{"max_candles": 84, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 23326 | `{"max_candles": 120, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 23706 | `{"max_candles": 138, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 23970 | `{"max_candles": 48, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |
| 24515 | `{"max_candles": 192, "n": 150, "stop_atr": 0.5, "take_profit_atr": 4.0}` | 2,561.07 | 3.9 | -17.9 | 16.7 | 685.00 | 2.3 | -9.2 | 0.59 | 78/31 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ATOMUSDT | 60% | 2.3 | 44.4 | 36.8 | -0.6 | -9.2 | 1 |
| 2 | DOTUSDT | 50% | -0.4 | 31.0 | -20.7 | 24.4 | -19.3 | 0 |
| 3 | NEARUSDT | 48% | -0.6 | 29.9 | -15.6 | -4.6 | 3.1 | 0 |
| 4 | XLMUSDT | 47% | -0.3 | 17.4 | -11.6 | -2.6 | -11.2 | 0 |
| 5 | ADAUSDT | 44% | -0.8 | 18.5 | 45.0 | -4.5 | -14.2 | 0 |
| 6 | BNBUSDT | 44% | -0.8 | 18.5 | 74.8 | -3.4 | -18.4 | 2 |
| 7 | JSTUSDT | 42% | -5.0 | 29.6 | 4.5 | 29.6 | 12.2 | 22 |
| 8 | UNIUSDT | 39% | -2.8 | 21.9 | -37.0 | -5.8 | -6.2 | 1 |
| 9 | AVAXUSDT | 37% | -3.8 | 95.8 | 14.6 | -17.2 | -18.4 | 3 |
| 10 | AAVEUSDT | 37% | -12.2 | 30.1 | -36.5 | -19.5 | -8.9 | 12 |
| 11 | SHIBUSDT | 32% | -2.6 | 16.5 | -41.9 | -1.8 | -7.7 | 0 |
| 12 | ICPUSDT | 31% | -4.1 | 25.4 | -41.6 | -3.5 | -10.0 | 0 |
| 13 | INJUSDT | 31% | -8.1 | 18.1 | 44.0 | 14.1 | -3.2 | 2 |
| 14 | STXUSDT | 29% | -6.4 | 40.4 | 105.8 | -10.6 | -19.8 | 5 |
| 15 | XRPUSDT | 27% | -4.7 | 21.2 | 5.0 | -5.5 | 1.8 | 0 |
| 16 | VETUSDT | 27% | -8.8 | 18.6 | 53.1 | -15.2 | -27.5 | 0 |
| 17 | TRXUSDT | 26% | -8.1 | 9.8 | 54.0 | -23.4 | -6.5 | 0 |
| 18 | ETHUSDT | 24% | -5.9 | 9.2 | 13.4 | -6.9 | 1.9 | 4 |
| 19 | LTCUSDT | 24% | -9.1 | 17.9 | -8.6 | -16.5 | -14.8 | 0 |
| 20 | SOLUSDT | 23% | -11.6 | 14.4 | 214.4 | -20.8 | -7.4 | 0 |
| 21 | BCHUSDT | 15% | -12.2 | 11.2 | 2.9 | -11.7 | -3.9 | 0 |
| 22 | ZECUSDT | 13% | -7.4 | 10.3 | -11.3 | -14.9 | 7.7 | 3 |
| 23 | CAKEUSDT | 11% | -10.7 | 25.6 | -48.5 | -26.9 | -17.4 | 1 |
| 24 | LINKUSDT | 11% | -11.1 | 8.7 | 37.9 | -16.5 | -4.0 | 0 |
| 25 | DOGEUSDT | 10% | -10.2 | 11.5 | 156.4 | -23.8 | -0.9 | 0 |
| 26 | BTCUSDT | 8% | -7.6 | 9.0 | 27.1 | -12.7 | 1.1 | 2 |
| 27 | ALGOUSDT | 8% | -12.6 | 15.6 | -3.8 | -28.1 | -18.8 | 0 |
| 28 | FILUSDT | 3% | -10.7 | 1.5 | -67.5 | -10.7 | -11.5 | 0 |
| 29 | ETCUSDT | 2% | -15.2 | 4.8 | 34.4 | -17.1 | -30.4 | 0 |
| 30 | DASHUSDT | 0% | -15.4 | n/a | -20.4 | -21.2 | -14.3 | 0 |
| 31 | HBARUSDT | 0% | -16.8 | n/a | 26.6 | -8.4 | -19.1 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 26,460 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
