# three_bar_momentum_thrust: optimization summary

Updated 2026-11-26T01:55:21Z · backtest.py version `ee689764b5` · 24,669 parameter sets tested with this version (24,669 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SOLUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [three_bar_momentum_thrust__max-income__v001.md](three_bar_momentum_thrust__max-income__v001.md) | 24669 | `{"max_candles": 42, "roc": 10.0, "stop_atr": 3.5, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 16:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 2,038.62 | 530.48 |
| return % | 20.39 | 5.30 |
| return %/year | 6.5 | 1.8 |
| gross profit | 14,765.82 | 2,092.51 |
| gross loss | 12,727.20 | 1,562.04 |
| trades | 51 | 11 |
| win rate % | 43.1 | 54.5 |
| avg win | 671.17 | 348.75 |
| avg loss | -438.87 | -312.41 |
| avg result / trade | 39.97 | 48.23 |
| largest single loss | -992.49 | -576.99 |
| largest loss % of equity | -9.20 | -5.32 |
| max drawdown | -5,032.03 | -1,510.00 |
| max drawdown % | -45.24 | -13.36 |
| profit factor | 1.16 | 1.34 |
| unusually bad trades | 3 | 1 |
| … threshold (% of equity) | 9.1 | 5.2 |
| time in market % | 2.6 | 0.8 |
| buy & hold return % | 2,768.91 | -29.19 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |
| period | 2021-01-24 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2021 | -12.9 |
| 2022 | -2.3 |
| 2023 | 41.4 |
| 2024 (OOS) | -2.3 |
| 2025 (OOS) | 3.4 |
| 2026 (OOS) | 4.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 45.2% from a peak in-sample and 13.4% out-of-sample, and the worst single trade cost 5.3% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 1.8% a year against 6.5% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 22% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 690 | `{"max_candles": 42, "roc": 10.0, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | 0.71 |
| 697 | `{"max_candles": 42, "roc": 10.0, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 698 | `{"max_candles": 42, "roc": 10.0, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 700 | `{"max_candles": 33, "roc": 10.0, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 701 | `{"max_candles": 51, "roc": 10.0, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 895 | `{"max_candles": 60, "roc": 10.0, "stop_atr": 2.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 1115 | `{"max_candles": 60, "roc": 10.0, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 1340 | `{"max_candles": 78, "roc": 10.0, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 1687 | `{"max_candles": 24, "roc": 10.0, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 2534 | `{"max_candles": 96, "roc": 10.0, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 2606 | `{"max_candles": 78, "roc": 10.0, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 2619 | `{"max_candles": 87, "roc": 10.0, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 2941 | `{"max_candles": 69, "roc": 10.0, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 3148 | `{"max_candles": 96, "roc": 10.0, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 3276 | `{"max_candles": 51, "roc": 10.0, "stop_atr": 3.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 3586 | `{"max_candles": 60, "roc": 10.0, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 3953 | `{"max_candles": 60, "roc": 10.0, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4057 | `{"max_candles": 69, "roc": 10.0, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4319 | `{"max_candles": 33, "roc": 10.0, "stop_atr": 3.0, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4704 | `{"max_candles": 51, "roc": 10.0, "stop_atr": 2.5, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4743 | `{"max_candles": 42, "roc": 10.0, "stop_atr": 2.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4789 | `{"max_candles": 24, "roc": 10.0, "stop_atr": 2.75, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4847 | `{"max_candles": 96, "roc": 10.0, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 4866 | `{"max_candles": 51, "roc": 10.0, "stop_atr": 3.25, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |
| 5306 | `{"max_candles": 78, "roc": 10.0, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 2,038.62 | 6.5 | -45.2 | 43.1 | 530.48 | 1.8 | -13.4 | 0.28 | 51/11 | not checked |

(200 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TRXUSDT | 73% | 6.7 | 23.6 | 54.0 | 7.5 | 12.2 | 24 |
| 2 | DOGEUSDT | 60% | 2.4 | 45.4 | 156.4 | -9.1 | -0.4 | 21 |
| 3 | XRPUSDT | 50% | 0.0 | 38.8 | 5.0 | -25.0 | -1.7 | 6 |
| 4 | ADAUSDT | 50% | -0.1 | 20.1 | 45.0 | -10.5 | -16.7 | 1 |
| 5 | BNBUSDT | 45% | -0.5 | 13.8 | 74.8 | -10.5 | -12.1 | 0 |
| 6 | ETCUSDT | 35% | -2.9 | 11.7 | 34.4 | -8.2 | -8.2 | 4 |
| 7 | SHIBUSDT | 31% | -6.4 | 24.0 | -41.9 | -32.4 | -1.3 | 7 |
| 8 | ICPUSDT | 23% | -6.3 | 17.2 | -41.6 | -30.6 | -17.4 | 9 |
| 9 | STXUSDT | 18% | -7.4 | 8.5 | 105.8 | -17.2 | -31.0 | 2 |
| 10 | ETHUSDT | 16% | -6.1 | 8.1 | 13.4 | -7.5 | -14.9 | 6 |
| 11 | LTCUSDT | 15% | -15.4 | 6.4 | -8.6 | -23.6 | -22.6 | 0 |
| 12 | AVAXUSDT | 13% | -15.7 | 14.6 | 14.6 | -31.4 | -35.6 | 0 |
| 13 | BCHUSDT | 13% | -17.6 | 12.6 | 2.9 | -18.3 | -11.9 | 8 |
| 14 | SOLUSDT | 11% | -15.2 | 13.0 | 214.4 | -27.3 | -35.8 | 2 |
| 15 | BTCUSDT | 5% | -5.8 | 2.2 | 27.1 | -11.2 | -8.9 | 0 |
| 16 | DASHUSDT | 5% | -16.8 | 1.8 | -20.4 | -29.0 | -16.3 | 0 |
| 17 | FILUSDT | 5% | -24.7 | 2.8 | -67.5 | -45.5 | -20.4 | 0 |
| 18 | UNIUSDT | 5% | -27.5 | 2.4 | -37.0 | -36.1 | -9.7 | 0 |
| 19 | JSTUSDT | 2% | -15.4 | 0.4 | 4.5 | 0.4 | -6.1 | 0 |
| 20 | ZECUSDT | 2% | -16.6 | 1.9 | -11.3 | -32.3 | 58.4 | 1 |
| 21 | ATOMUSDT | 2% | -16.6 | 3.0 | 36.8 | -26.5 | -0.6 | 0 |
| 22 | LINKUSDT | 2% | -19.8 | 0.1 | 37.9 | -28.9 | -2.5 | 0 |
| 23 | VETUSDT | 2% | -22.7 | 2.1 | 53.1 | -33.8 | -31.2 | 0 |
| 24 | AAVEUSDT | 2% | -27.8 | 2.1 | -36.5 | -39.8 | 24.7 | 0 |
| 25 | XLMUSDT | 0% | -15.8 | n/a | -11.6 | -26.3 | -2.0 | 0 |
| 26 | DOTUSDT | 0% | -21.9 | n/a | -20.7 | -41.0 | -10.2 | 0 |
| 27 | CAKEUSDT | 0% | -22.1 | n/a | -48.5 | -44.4 | -5.2 | 0 |
| 28 | HBARUSDT | 0% | -27.4 | n/a | 26.6 | -35.3 | 32.8 | 0 |
| 29 | ALGOUSDT | 0% | -31.9 | n/a | -3.8 | -45.5 | -18.9 | 0 |
| 30 | INJUSDT | 0% | -35.5 | n/a | 44.0 | -43.3 | -23.4 | 0 |
| 31 | NEARUSDT | 0% | -40.2 | n/a | -15.6 | -43.1 | -36.0 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [three_bar_momentum_thrust__broad__max-income__v002.md](symbols/broad/three_bar_momentum_thrust__broad__max-income__v002.md) | 2.7 | 2.6 | 2.6 | -36.9 | 32.9 | 1514/707 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 24,669 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
