# breakout_ws__broad: optimization summary

Updated 2026-11-24T22:22:53Z · backtest.py version `82a40057c3` · 1,595 parameter sets tested with this version (1,595 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, QNTUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT, RAYUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 12 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_ws__broad__max-income__v001.md](breakout_ws__broad__max-income__v001.md) | 1594 | `{"entry_n": 21, "exit_n": 20}` | long JSTUSDT since 2026-09-06 00:00 @ 0.11044 |
| balanced | [breakout_ws__broad__balanced__v001.md](breakout_ws__broad__balanced__v001.md) | 1595 | `{"entry_n": 57, "exit_n": 5}` | flat (data up to 2026-11-23 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 143,677.50 | 6,102.11 | 44,595.73 | 7,038.70 |
| return % | 1,436.78 | 61.02 | 445.96 | 70.39 |
| return %/year | 57.7 | 17.9 | 32.7 | 20.2 |
| gross profit | 225,174.35 | 18,981.48 | 64,733.33 | 14,900.90 |
| gross loss | 81,496.85 | 12,879.37 | 20,137.60 | 7,862.21 |
| trades | 446 | 367 | 438 | 298 |
| win rate % | 42.8 | 34.6 | 42.9 | 40.6 |
| avg win | 1,178.92 | 149.46 | 344.33 | 123.15 |
| avg loss | -319.60 | -53.66 | -80.55 | -44.42 |
| avg result / trade | 322.15 | 16.63 | 101.82 | 23.62 |
| largest single loss | -6,854.07 | -710.80 | -1,094.38 | -305.11 |
| largest loss % of equity | -35.14 | -27.47 | -20.53 | -15.88 |
| max drawdown | -121,481.67 | -8,472.83 | -7,893.88 | -4,711.20 |
| max drawdown % | -64.88 | -45.30 | -19.74 | -26.22 |
| profit factor | 2.76 | 1.47 | 3.21 | 1.90 |
| unusually bad trades | 27 | 18 | 23 | 17 |
| … threshold (% of equity) | 29.7 | 28.7 | 20.5 | 19.6 |
| time in market % | 31.1 | 45.9 | 11.5 | 13.3 |
| buy & hold return % | 534.56 | 68.80 | 534.56 | 68.80 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.31 |  | 0.62 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -7.2 | -1.9 |
| 2019 | 7.2 | 2.4 |
| 2020 | 93.3 | 25.4 |
| 2021 | 500.7 | 184.1 |
| 2022 | -39.0 | -9.5 |
| 2023 | 118.4 | 68.9 |
| 2024 (OOS) | 36.2 | 56.4 |
| 2025 (OOS) | -13.5 | -10.9 |
| 2026 (OOS) | -20.7 | -3.5 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 64.9% from a peak in-sample and 45.3% out-of-sample, and the worst single trade cost 27.5% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 17.9% a year against 57.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 15% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 19.7% from a peak in-sample and 26.2% out-of-sample, and the worst single trade cost 15.9% of the account out-of-sample. About 43 of every 100 trades won in-sample. With 100% of equity per trade; about 38% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1405 | `{"entry_n": 23, "exit_n": 20}` | 144,688.66 | 57.9 | -65.7 | 43.7 | 7,013.89 | 20.2 | -43.5 | 0.35 | 426/341 | not checked |
| 782 | `{"entry_n": 21, "exit_n": 20}` | 143,677.50 | 57.7 | -64.9 | 42.8 | 6,102.11 | 17.9 | -45.3 | 0.31 | 446/367 | 1.00 |
| 91 | `{"entry_n": 21, "exit_n": 18}` | 136,943.96 | 56.5 | -61.2 | 44.2 | 6,578.40 | 19.1 | -44.1 | 0.34 | 466/379 | not checked |
| 848 | `{"entry_n": 25, "exit_n": 17}` | 133,800.25 | 56.0 | -59.7 | 46.4 | 9,101.44 | 25.1 | -42.2 | 0.45 | 438/351 | not checked |
| 514 | `{"entry_n": 26, "exit_n": 18}` | 131,109.77 | 55.5 | -59.3 | 45.9 | 6,346.45 | 18.5 | -41.9 | 0.33 | 425/333 | not checked |
| 276 | `{"entry_n": 28, "exit_n": 17}` | 129,880.33 | 55.3 | -58.4 | 44.6 | 7,798.26 | 22.1 | -40.0 | 0.40 | 424/330 | not checked |
| 1489 | `{"entry_n": 27, "exit_n": 17}` | 128,272.14 | 55.0 | -57.7 | 46.0 | 7,512.77 | 21.4 | -41.0 | 0.39 | 428/339 | not checked |
| 11 | `{"entry_n": 21, "exit_n": 12}` | 119,434.44 | 53.3 | -40.9 | 46.7 | 14,668.72 | 36.7 | -42.3 | 0.69 | 525/448 | 1.00 |
| 22 | `{"entry_n": 21, "exit_n": 9}` | 113,914.27 | 52.2 | -33.4 | 45.7 | 14,740.49 | 36.8 | -39.7 | 0.71 | 586/483 | 1.00 |
| 566 | `{"entry_n": 30, "exit_n": 8}` | 92,869.64 | 47.5 | -30.9 | 44.4 | 15,714.84 | 38.6 | -32.6 | 0.81 | 522/387 | not checked |
| 1535 | `{"entry_n": 28, "exit_n": 7}` | 92,489.52 | 47.4 | -30.5 | 43.9 | 13,629.56 | 34.6 | -33.8 | 0.73 | 558/422 | not checked |
| 471 | `{"entry_n": 30, "exit_n": 7}` | 91,077.51 | 47.1 | -27.3 | 43.5 | 17,621.85 | 42.1 | -31.6 | 0.89 | 542/399 | not checked |
| 277 | `{"entry_n": 30, "exit_n": 6}` | 78,843.29 | 44.0 | -26.6 | 43.7 | 18,102.98 | 43.0 | -30.1 | 0.98 | 572/416 | not checked |
| 1019 | `{"entry_n": 31, "exit_n": 6}` | 71,898.83 | 42.0 | -26.0 | 43.8 | 14,944.83 | 37.2 | -30.2 | 0.89 | 562/406 | not checked |
| 673 | `{"entry_n": 25, "exit_n": 5}` | 64,882.95 | 39.9 | -24.9 | 43.2 | 10,202.52 | 27.5 | -28.8 | 0.69 | 648/492 | not checked |
| 383 | `{"entry_n": 30, "exit_n": 5}` | 64,684.44 | 39.8 | -22.6 | 43.0 | 12,837.05 | 33.1 | -27.5 | 0.83 | 603/434 | not checked |
| 492 | `{"entry_n": 29, "exit_n": 5}` | 62,143.14 | 39.0 | -22.4 | 42.7 | 13,563.00 | 34.5 | -27.6 | 0.88 | 613/449 | not checked |
| 270 | `{"entry_n": 31, "exit_n": 5}` | 59,812.31 | 38.3 | -22.2 | 42.8 | 10,653.08 | 28.5 | -27.7 | 0.74 | 593/424 | not checked |
| 1249 | `{"entry_n": 30, "exit_n": 4}` | 50,166.39 | 34.9 | -21.2 | 43.5 | 13,305.81 | 34.0 | -24.4 | 0.97 | 662/450 | not checked |
| 1280 | `{"entry_n": 29, "exit_n": 4}` | 48,161.70 | 34.1 | -21.1 | 43.4 | 14,128.00 | 35.6 | -25.2 | 1.04 | 673/465 | not checked |
| 162 | `{"entry_n": 57, "exit_n": 5}` | 44,595.73 | 32.7 | -19.7 | 42.9 | 7,038.70 | 20.2 | -26.2 | 0.62 | 438/298 | 1.00 |

## Analyst notes

<!-- analyst-notes:start -->
Main variant for this strategy, because the screen's coin ranking was not persistent (see base summary).
balanced (57/5) trades fewer, longer-confirmed breakouts and exits fast: in the market only 11–13% of the time, worst drawdown −26%.
max-income (21/20) rides trends longer and holds up much worse out-of-sample (efficiency 0.31, drawdown −45% OOS).
Short-exit sets across the Pareto front held up best out-of-sample. Profits come mostly from 2020–2021, and both
variants are negative in 2025 and 2026. No range warnings (both bests are inside the ranges). Paper-trade balanced at ~1/3 size first.
<!-- analyst-notes:end -->

---

Searching 1,595 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
