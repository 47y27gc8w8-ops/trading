# breakout_bl: optimization summary

Updated 2026-11-24T23:10:04Z · backtest.py version `3f84a6b068` · 1,594 parameter sets tested with this version (1,594 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SOLUSDT, VETUSDT, ADAUSDT, HBARUSDT, BTCUSDT, DOGEUSDT, BNBUSDT, AVAXUSDT, SHIBUSDT, DOTUSDT, NEARUSDT, UNIUSDT, ALGOUSDT, RAYUSDT, ETHUSDT, ETCUSDT, TRXUSDT, NEXOUSDT, LINKUSDT, XRPUSDT, STXUSDT, XLMUSDT, JSTUSDT, DASHUSDT, AAVEUSDT, QNTUSDT, FILUSDT, ZECUSDT, CAKEUSDT, BCHUSDT, INJUSDT, ATOMUSDT, LTCUSDT, APTUSDT, ICPUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 12 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_bl__max-income__v001.md](breakout_bl__max-income__v001.md) | 1593 | `{"entry_n": 21, "exit_n": 20}` | long JSTUSDT since 2026-09-06 00:00 @ 0.11044 |
| balanced | [breakout_bl__balanced__v001.md](breakout_bl__balanced__v001.md) | 1594 | `{"entry_n": 57, "exit_n": 5}` | flat (data up to 2026-11-23 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 135,523.68 | 5,482.84 | 42,228.38 | 6,528.96 |
| return % | 1,355.24 | 54.83 | 422.28 | 65.29 |
| return %/year | 56.3 | 16.3 | 31.7 | 19.0 |
| gross profit | 212,506.22 | 18,139.82 | 61,215.26 | 14,210.75 |
| gross loss | 76,982.54 | 12,656.98 | 18,986.88 | 7,681.79 |
| trades | 451 | 389 | 441 | 311 |
| win rate % | 42.8 | 34.2 | 43.3 | 40.2 |
| avg win | 1,101.07 | 136.39 | 320.50 | 113.69 |
| avg loss | -298.38 | -49.44 | -75.95 | -41.30 |
| avg result / trade | 300.50 | 14.09 | 95.76 | 20.99 |
| largest single loss | -6,462.41 | -670.18 | -1,031.84 | -287.68 |
| largest loss % of equity | -35.14 | -27.47 | -20.53 | -15.88 |
| max drawdown | -114,682.52 | -8,249.39 | -7,442.80 | -4,532.62 |
| max drawdown % | -64.75 | -45.16 | -19.44 | -25.74 |
| profit factor | 2.76 | 1.43 | 3.22 | 1.85 |
| unusually bad trades | 27 | 19 | 23 | 18 |
| … threshold (% of equity) | 29.8 | 28.4 | 20.5 | 19.8 |
| time in market % | 29.6 | 45.4 | 11.0 | 13.1 |
| buy & hold return % | 502.60 | 61.42 | 502.60 | 61.42 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |  | 0.60 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2018 | -6.8 | -1.8 |
| 2019 | 6.7 | 2.2 |
| 2020 | 88.0 | 23.9 |
| 2021 | 485.4 | 175.7 |
| 2022 | -38.8 | -9.3 |
| 2023 | 117.7 | 68.2 |
| 2024 (OOS) | 36.0 | 55.6 |
| 2025 (OOS) | -13.5 | -10.8 |
| 2026 (OOS) | -20.7 | -3.7 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 64.8% from a peak in-sample and 45.2% out-of-sample, and the worst single trade cost 27.5% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 16.3% a year against 56.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 15% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 19.4% from a peak in-sample and 25.7% out-of-sample, and the worst single trade cost 15.9% of the account out-of-sample. About 43 of every 100 trades won in-sample. Out-of-sample it earned 19.0% a year against 31.7% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 39% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1403 | `{"entry_n": 23, "exit_n": 20}` | 136,474.75 | 56.5 | -65.5 | 43.6 | 6,360.88 | 18.6 | -43.3 | 0.33 | 431/362 | not checked |
| 780 | `{"entry_n": 21, "exit_n": 20}` | 135,523.68 | 56.3 | -64.8 | 42.8 | 5,482.84 | 16.3 | -45.2 | 0.29 | 451/389 | 1.00 |
| 88 | `{"entry_n": 21, "exit_n": 18}` | 129,174.91 | 55.1 | -61.1 | 44.2 | 5,937.75 | 17.5 | -43.8 | 0.32 | 471/401 | not checked |
| 846 | `{"entry_n": 25, "exit_n": 17}` | 126,282.44 | 54.6 | -59.6 | 46.4 | 8,346.64 | 23.4 | -41.8 | 0.43 | 442/371 | not checked |
| 512 | `{"entry_n": 26, "exit_n": 18}` | 123,735.49 | 54.1 | -59.2 | 45.9 | 5,756.41 | 17.0 | -41.5 | 0.32 | 429/352 | not checked |
| 274 | `{"entry_n": 28, "exit_n": 17}` | 122,586.51 | 53.9 | -58.3 | 44.6 | 7,111.60 | 20.4 | -39.7 | 0.38 | 428/349 | not checked |
| 1487 | `{"entry_n": 27, "exit_n": 17}` | 121,070.22 | 53.6 | -57.5 | 46.1 | 6,856.07 | 19.8 | -40.6 | 0.37 | 432/358 | not checked |
| 11 | `{"entry_n": 21, "exit_n": 12}` | 112,746.44 | 51.9 | -40.7 | 46.6 | 13,520.15 | 34.4 | -41.9 | 0.66 | 530/475 | 1.00 |
| 22 | `{"entry_n": 21, "exit_n": 9}` | 107,553.87 | 50.8 | -33.2 | 45.7 | 13,635.09 | 34.6 | -39.5 | 0.68 | 591/511 | 1.00 |
| 564 | `{"entry_n": 30, "exit_n": 8}` | 87,767.49 | 46.3 | -30.7 | 44.5 | 14,646.64 | 36.6 | -32.2 | 0.79 | 526/408 | not checked |
| 1533 | `{"entry_n": 28, "exit_n": 7}` | 87,409.08 | 46.2 | -30.2 | 44.0 | 12,683.76 | 32.8 | -33.3 | 0.71 | 562/444 | not checked |
| 469 | `{"entry_n": 30, "exit_n": 7}` | 86,077.76 | 45.8 | -27.1 | 43.6 | 16,460.61 | 40.0 | -31.2 | 0.87 | 546/420 | not checked |
| 275 | `{"entry_n": 30, "exit_n": 6}` | 74,547.08 | 42.8 | -26.4 | 43.8 | 16,926.78 | 40.9 | -29.9 | 0.95 | 576/438 | not checked |
| 1017 | `{"entry_n": 31, "exit_n": 6}` | 67,999.45 | 40.9 | -25.8 | 43.8 | 13,942.76 | 35.2 | -29.9 | 0.86 | 566/427 | not checked |
| 671 | `{"entry_n": 25, "exit_n": 5}` | 61,318.58 | 38.8 | -24.7 | 43.3 | 9,518.36 | 26.0 | -28.5 | 0.67 | 653/516 | not checked |
| 381 | `{"entry_n": 30, "exit_n": 5}` | 61,131.42 | 38.7 | -22.4 | 43.1 | 11,975.56 | 31.3 | -27.1 | 0.81 | 608/456 | not checked |
| 490 | `{"entry_n": 29, "exit_n": 5}` | 58,735.34 | 37.9 | -22.2 | 42.9 | 12,639.60 | 32.7 | -27.3 | 0.86 | 618/472 | not checked |
| 268 | `{"entry_n": 31, "exit_n": 5}` | 56,537.69 | 37.2 | -22.0 | 43.0 | 9,909.15 | 26.9 | -27.2 | 0.72 | 598/445 | not checked |
| 1247 | `{"entry_n": 30, "exit_n": 4}` | 47,360.11 | 33.8 | -21.0 | 43.6 | 12,454.88 | 32.3 | -24.3 | 0.95 | 669/472 | not checked |
| 1278 | `{"entry_n": 29, "exit_n": 4}` | 45,469.97 | 33.1 | -20.8 | 43.5 | 13,210.11 | 33.8 | -25.0 | 1.02 | 680/488 | not checked |
| 160 | `{"entry_n": 57, "exit_n": 5}` | 42,228.38 | 31.7 | -19.4 | 43.3 | 6,528.96 | 19.0 | -25.7 | 0.60 | 441/311 | 1.00 |

## Screening: where does the strategy work? (in-sample ranking)

33 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ETHUSDT | 100% | 31.9 | 61.6 | 20.8 | 45.1 | -21.7 | 40 |
| 2 | ETCUSDT | 100% | 30.2 | 74.9 | 14.2 | 48.9 | -29.5 | 0 |
| 3 | BNBUSDT | 98% | 75.7 | 122.7 | 80.3 | 70.4 | 21.1 | 16 |
| 4 | VETUSDT | 98% | 58.6 | 145.3 | 41.3 | 145.3 | 5.6 | 11 |
| 5 | BTCUSDT | 97% | 34.8 | 53.4 | 20.6 | 44.9 | 9.5 | 31 |
| 6 | LINKUSDT | 92% | 18.4 | 101.9 | 86.1 | 38.3 | -19.1 | 0 |
| 7 | DOGEUSDT | 90% | 81.3 | 165.6 | 134.3 | 83.9 | 29.7 | 28 |
| 8 | ADAUSDT | 75% | 78.2 | 97.0 | 41.0 | 82.0 | -25.8 | 0 |
| 9 | TRXUSDT | 65% | 12.1 | 45.5 | 30.6 | 24.6 | 32.3 | 41 |
| 10 | ATOMUSDT | 57% | 13.7 | 39.7 | 38.0 | -4.4 | -20.4 | 0 |
| 11 | LTCUSDT | 52% | 2.4 | 21.4 | -8.2 | -1.0 | -11.1 | 1 |
| 12 | ALGOUSDT | 51% | 29.4 | 73.2 | -0.0 | 40.6 | 21.9 | 13 |
| 13 | XRPUSDT | 48% | -1.0 | 47.5 | 12.1 | 3.4 | 35.4 | 24 |
| 14 | HBARUSDT | 44% | 66.8 | 112.2 | 66.2 | 96.6 | 17.1 | 6 |
| 15 | STXUSDT | 38% | 129.8 | 153.1 | 80.0 | 37.7 | -4.3 | 2 |
| 16 | INJUSDT | 38% | 29.3 | 76.6 | 38.0 | 32.9 | -10.9 | 0 |
| 17 | DOTUSDT | 37% | 69.9 | 77.5 | 15.9 | 59.8 | -14.1 | 0 |
| 18 | SOLUSDT | 35% | 298.7 | 412.6 | 283.8 | 343.8 | 5.5 | 0 |
| 19 | NEARUSDT | 29% | 70.4 | 96.6 | 4.2 | 96.6 | -1.3 | 4 |
| 20 | DASHUSDT | 29% | -4.1 | 37.7 | -25.2 | 17.9 | 52.7 | 14 |
| 21 | AVAXUSDT | 27% | 112.1 | 197.5 | 49.9 | 131.0 | -20.4 | 0 |
| 22 | BCHUSDT | 22% | -2.0 | 15.0 | 3.5 | 1.8 | -20.0 | 1 |
| 23 | ZECUSDT | 21% | -10.3 | 27.9 | -21.5 | -11.4 | 259.1 | 13 |
| 24 | UNIUSDT | 16% | 37.2 | 59.5 | 1.2 | 59.5 | 23.5 | 4 |
| 25 | XLMUSDT | 16% | -15.5 | 24.8 | -12.5 | -4.4 | 32.7 | 6 |
| 26 | JSTUSDT | 13% | 24.2 | 33.0 | 7.6 | 22.6 | 29.3 | 8 |
| 27 | CAKEUSDT | 11% | 22.9 | 26.1 | -44.8 | 30.3 | -16.7 | 0 |
| 28 | SHIBUSDT | 10% | 29.4 | 77.2 | 16.9 | 64.3 | -17.9 | 2 |
| 29 | FILUSDT | 10% | 28.4 | 26.2 | -45.8 | 8.5 | -27.1 | 1 |
| 30 | QNTUSDT | 8% | 8.7 | 22.7 | -21.3 | 14.1 | 25.1 | 4 |
| 31 | ICPUSDT | 6% | 26.5 | 24.4 | -48.4 | 1.7 | -36.4 | 0 |
| 32 | RAYUSDT | 2% | 60.6 | 70.8 | -60.9 | 23.6 | 70.8 | 1 |
| 33 | AAVEUSDT | 2% | -32.2 | 7.5 | -41.8 | -6.7 | 0.2 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [breakout_bl__broad__max-income__v001.md](symbols/broad/breakout_bl__broad__max-income__v001.md) | 57.7 | 17.9 | 17.9 | -64.9 | 42.8 | 446/367 |
| broad | balanced | [breakout_bl__broad__balanced__v001.md](symbols/broad/breakout_bl__broad__balanced__v001.md) | 47.1 | 31.0 | 31.0 | -34.3 | 45.1 | 543/420 |


## Analyst notes

<!-- analyst-notes:start -->
**Written 2026-11-25 after the first skill run (base 35-coin basket + crypto screen + broad 33-coin basket, full grids).**

- **What the variants do differently.** max-income (21/20) uses a slow exit. It rides trends longest and gives back a lot: −65 % IS drawdown, and OOS earns only 31 % of its IS rate. balanced (base 57/5, broad 27/8) uses a fast exit. It cuts losers within a week, with about half the drawdown and much better OOS efficiency (0.60–0.66). The whole Pareto front points the same way: exits of 5–8 days with entries of 27–31 days (e.g. 30/6, 30/7) are the sets that held up OOS (32–41 %/yr OOS, −24 to −33 % DD). This matches the earlier standalone study, which also found exit_n ≈ 5 better than the description's 10.
- **Where it works.** The ranking persistence check is NOT PERSISTENT (rank correlation −0.29; the top-8 coins of the first IS half made −17 %/yr in the second half vs +3 %/yr for the rest). The earlier walk-forward study found the same. So there's no reliable per-coin answer to "which coins trend". The strategy works, or doesn't, as a basket, and per-symbol runs were deliberately not done. The screen's top coins (ETH, ETC, BNB, VET, BTC) are a description of the past.
- **Stability: a real concern.** In-sample is dominated by 2021 (+292 % for broad-balanced). The other IS years are mixed (2018 −2, 2019 +2, 2022 −20). OOS is +34 % in 2024, then −19 % in 2025 and −3 % in 2026. On top of that, **one coin, ZEC, earned 9,354 of the 11,832 OOS profit (79 %)** of broad-balanced, and only 17 of 33 coins were profitable OOS. Without ZEC the OOS result is roughly +2,500 on 10,000 over 2.9 years (≈ 8 %/yr). This is how trend following normally makes money (a few huge winners pay for many small losers), and it is why the basket must stay broad. But it means the 31 %/yr OOS figure rests on one outlier and should not be extrapolated.
- **No safe-starter.** Every set has many "unusually bad" trades (crypto gaps through the 5–20-day lows), so none meets the ≤ 1 rule. The gate was not loosened.
- **Range warnings:** none. Best sets sit inside 5–60 / 3–30. The base balanced 57/5 is near the top of entry_n but not on the edge.
- **Paper-trade first:** broad-balanced 27/8 (or its Pareto neighbour 30/6) on the whole ≥ 2-year-history basket, at about **25–30 % of equity in total**, not 100 %. The summary computes 29 % to keep the worst drawdown near 10 %. Expect long flat or losing stretches (2025-style) between rare big trends. Treat the coin list as a history/liquidity filter and add newly eligible coins rather than dropping losers.
<!-- analyst-notes:end -->

---

Searching 1,594 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
