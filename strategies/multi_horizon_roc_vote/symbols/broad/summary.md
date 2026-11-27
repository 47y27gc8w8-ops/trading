# multi_horizon_roc_vote__broad: optimization summary

Updated 2026-11-26T00:27:03Z · backtest.py version `ccff135819` · 5,806 parameter sets tested with this version (5,806 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [multi_horizon_roc_vote__broad__max-income__v002.md](multi_horizon_roc_vote__broad__max-income__v002.md) | 5806 | `{"max_candles": 120, "stop_atr": 3.0, "take_profit_atr": 10.5, "votes": 2}` | flat (data up to 2026-11-24 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 9,958.26 | 2,135.69 |
| return % | 99.58 | 21.36 |
| return %/year | 13.3 | 6.9 |
| gross profit | 39,666.17 | 14,689.77 |
| gross loss | 29,707.92 | 12,554.08 |
| trades | 1,082 | 861 |
| win rate % | 29.5 | 26.8 |
| avg win | 124.35 | 63.59 |
| avg loss | -38.94 | -19.93 |
| avg result / trade | 9.20 | 2.48 |
| largest single loss | -885.93 | -188.57 |
| largest loss % of equity | -19.23 | -13.15 |
| max drawdown | -15,918.02 | -3,312.67 |
| max drawdown % | -52.80 | -24.95 |
| profit factor | 1.33 | 1.17 |
| unusually bad trades | 186 | 119 |
| … threshold (% of equity) | 8.8 | 8.3 |
| time in market % | 19.0 | 25.9 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2018 | -2.6 |
| 2019 | 0.6 |
| 2020 | 58.6 |
| 2021 | 65.7 |
| 2022 | -40.7 |
| 2023 | 30.8 |
| 2024 (OOS) | 12.4 |
| 2025 (OOS) | -6.3 |
| 2026 (OOS) | 2.1 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 52.8% from a peak in-sample and 24.9% out-of-sample, and the worst single trade cost 13.2% of the account out-of-sample. About 29 of every 100 trades won in-sample. Out-of-sample it earned 6.9% a year against 13.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 19% per trade would have kept the worst drawdown near 10% (rough estimate).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5372 | `{"max_candles": 132, "stop_atr": 2.75, "take_profit_atr": 10.5, "votes": 2}` | 10,447.53 | 13.8 | -52.3 | 29.5 | 1,988.27 | 6.5 | -24.6 | 0.47 | 1082/861 | not checked |
| 5504 | `{"max_candles": 108, "stop_atr": 2.75, "take_profit_atr": 10.5, "votes": 2}` | 10,152.64 | 13.5 | -52.2 | 29.5 | 2,002.04 | 6.5 | -24.5 | 0.48 | 1082/861 | not checked |
| 5469 | `{"max_candles": 132, "stop_atr": 2.5, "take_profit_atr": 9.5, "votes": 2}` | 9,525.08 | 12.8 | -48.6 | 29.6 | 1,569.13 | 5.2 | -24.9 | 0.40 | 1082/861 | not checked |
| 5510 | `{"max_candles": 108, "stop_atr": 2.5, "take_profit_atr": 9.5, "votes": 2}` | 9,487.62 | 12.8 | -47.4 | 29.6 | 1,573.91 | 5.2 | -24.9 | 0.41 | 1082/861 | not checked |
| 5498 | `{"max_candles": 96, "stop_atr": 2.5, "take_profit_atr": 9.5, "votes": 2}` | 9,386.19 | 12.7 | -47.4 | 29.6 | 1,578.09 | 5.2 | -24.9 | 0.41 | 1082/861 | not checked |
| 5608 | `{"max_candles": 180, "stop_atr": 2.5, "take_profit_atr": 8.0, "votes": 2}` | 7,859.60 | 11.0 | -46.4 | 29.9 | 930.43 | 3.1 | -24.1 | 0.28 | 1082/861 | not checked |
| 5610 | `{"max_candles": 192, "stop_atr": 2.5, "take_profit_atr": 8.0, "votes": 2}` | 7,859.60 | 11.0 | -46.4 | 29.9 | 930.43 | 3.1 | -24.1 | 0.28 | 1082/861 | not checked |
| 5650 | `{"max_candles": 168, "stop_atr": 2.5, "take_profit_atr": 8.0, "votes": 2}` | 7,859.60 | 11.0 | -46.4 | 29.9 | 930.43 | 3.1 | -24.1 | 0.28 | 1082/861 | not checked |
| 5692 | `{"max_candles": 156, "stop_atr": 2.5, "take_profit_atr": 8.0, "votes": 2}` | 7,859.60 | 11.0 | -46.4 | 29.9 | 930.43 | 3.1 | -24.1 | 0.28 | 1082/861 | not checked |
| 5754 | `{"max_candles": 144, "stop_atr": 2.5, "take_profit_atr": 8.0, "votes": 2}` | 7,859.60 | 11.0 | -46.4 | 29.9 | 930.43 | 3.1 | -24.1 | 0.28 | 1082/861 | not checked |
| 5646 | `{"max_candles": 60, "stop_atr": 3.5, "take_profit_atr": 8.0, "votes": 3}` | 5,780.37 | 8.6 | -38.5 | 35.0 | 905.78 | 3.0 | -30.1 | 0.35 | 523/394 | not checked |
| 5415 | `{"max_candles": 48, "stop_atr": 3.75, "take_profit_atr": 7.5, "votes": 3}` | 5,464.18 | 8.2 | -34.9 | 37.0 | 622.82 | 2.1 | -30.7 | 0.26 | 532/405 | not checked |
| 5122 | `{"max_candles": 48, "stop_atr": 3.5, "take_profit_atr": 6.5, "votes": 3}` | 3,971.32 | 6.2 | -34.7 | 37.5 | 500.95 | 1.7 | -28.8 | 0.27 | 536/410 | not checked |
| 5791 | `{"max_candles": 36, "stop_atr": 1.75, "take_profit_atr": 10.0, "votes": 3}` | 3,825.77 | 6.0 | -34.0 | 30.9 | 1,202.33 | 4.0 | -26.7 | 0.67 | 628/483 | not checked |
| 5115 | `{"max_candles": 48, "stop_atr": 3.25, "take_profit_atr": 6.5, "votes": 3}` | 3,737.37 | 5.9 | -33.9 | 36.9 | 469.06 | 1.6 | -28.5 | 0.27 | 542/414 | not checked |
| 5097 | `{"max_candles": 48, "stop_atr": 2.75, "take_profit_atr": 6.5, "votes": 3}` | 3,355.89 | 5.3 | -32.8 | 35.7 | 447.91 | 1.5 | -29.0 | 0.29 | 557/429 | 1.00 |
| 5293 | `{"max_candles": 48, "stop_atr": 2.0, "take_profit_atr": 7.5, "votes": 3}` | 3,260.18 | 5.2 | -31.7 | 31.7 | 398.43 | 1.4 | -27.1 | 0.26 | 597/453 | not checked |
| 5203 | `{"max_candles": 48, "stop_atr": 1.75, "take_profit_atr": 7.0, "votes": 3}` | 2,938.67 | 4.8 | -31.7 | 30.6 | 682.82 | 2.3 | -25.2 | 0.49 | 624/473 | not checked |
| 5137 | `{"max_candles": 48, "stop_atr": 2.0, "take_profit_atr": 7.0, "votes": 3}` | 2,451.24 | 4.0 | -31.5 | 31.8 | 558.47 | 1.9 | -27.1 | 0.47 | 598/457 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 5,806 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
