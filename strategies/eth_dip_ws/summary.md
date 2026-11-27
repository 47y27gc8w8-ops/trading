# eth_dip_ws: optimization summary

Updated 2026-11-23T22:10:54Z · backtest.py version `d7da2db029` · 1,505 parameter sets tested with this version (1,505 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
- In-sample (tuning): 2018-06-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.05% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [eth_dip_ws__max-income__v002.md](eth_dip_ws__max-income__v002.md) | 1504 | `{"entry": 30, "exit": 80, "rsi_n": 38, "stop_loss_pct": 6}` | long ETHUSDT since 2026-11-21 04:00 @ 1573.06614 |
| balanced | none | | | |
| safe-starter | [eth_dip_ws__safe-starter__v001.md](eth_dip_ws__safe-starter__v001.md) | 1505 | `{"entry": 30, "exit": 80, "rsi_n": 38, "stop_loss_pct": 7}` | long ETHUSDT since 2026-11-21 04:00 @ 1573.06614 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|
| net profit | 12,998.89 | 1,430.47 | 11,582.57 | 2,456.63 |
| return % | 129.99 | 14.30 | 115.83 | 24.57 |
| return %/year | 16.1 | 4.7 | 14.8 | 7.9 |
| gross profit | 26,470.67 | 4,877.71 | 25,079.53 | 5,361.31 |
| gross loss | 13,471.78 | 3,447.24 | 13,496.97 | 2,904.69 |
| trades | 30 | 8 | 27 | 6 |
| win rate % | 10.0 | 25.0 | 11.1 | 33.3 |
| avg win | 8,823.56 | 2,438.86 | 8,359.84 | 2,680.66 |
| avg loss | -498.95 | -574.54 | -562.37 | -726.17 |
| avg result / trade | 433.30 | 178.81 | 428.98 | 409.44 |
| largest single loss | -937.22 | -695.11 | -1,042.07 | -888.15 |
| largest loss % of equity | -6.23 | -6.23 | -7.23 | -7.23 |
| max drawdown | -9,240.27 | -16,295.77 | -8,856.91 | -17,949.66 |
| max drawdown % | -70.62 | -68.03 | -70.89 | -68.03 |
| profit factor | 1.97 | 1.42 | 1.86 | 1.85 |
| unusually bad trades | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 12.5 | 12.5 | 14.5 | 14.5 |
| time in market % | 61.0 | 53.9 | 61.0 | 53.9 |
| buy & hold return % | 294.92 | -24.43 | 294.92 | -24.43 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |  | 0.53 |
| period | 2018-06-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-06-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | safe-starter |
|---|---|---|
| 2018 | -51.4 | -53.4 |
| 2019 | -1.7 | -1.7 |
| 2020 | 214.9 | 214.9 |
| 2021 | 0.0 | 0.0 |
| 2022 | -26.9 | -28.4 |
| 2023 | 109.6 | 109.6 |
| 2024 (OOS) | 46.3 | 46.3 |
| 2025 (OOS) | -11.0 | -11.0 |
| 2026 (OOS) | -22.4 | -23.2 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 70.6% from a peak in-sample and 68.0% out-of-sample, and the worst single trade cost 6.2% of the account out-of-sample. About 10 of every 100 trades won in-sample. Out-of-sample it earned 4.7% a year against 16.1% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 14% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 70.9% from a peak in-sample and 68.0% out-of-sample, and the worst single trade cost 7.2% of the account out-of-sample. About 11 of every 100 trades won in-sample. Out-of-sample it earned 7.9% a year against 14.8% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 14% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1131 | `{"entry": 30, "exit": 80, "rsi_n": 38, "stop_loss_pct": 6}` | 12,998.89 | 16.1 | -70.6 | 10.0 | 1,430.47 | 4.7 | -68.0 | 0.29 | 30/8 | 0.75 |
| 1133 | `{"entry": 30, "exit": 80, "rsi_n": 36, "stop_loss_pct": 6}` | 8,408.31 | 11.6 | -69.6 | 9.5 | 1,176.70 | 3.9 | -68.0 | 0.34 | 42/8 | not checked |
| 1170 | `{"entry": 30, "exit": 75, "rsi_n": 40, "stop_loss_pct": 6}` | 667.59 | 1.2 | -67.6 | 10.5 | 1,564.24 | 5.2 | -41.8 | 4.45 | 38/15 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

33 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | INJUSDT | 32% | 5.6 | 75.8 | 178.1 | 8.5 | 23.3 | 3 |
| 2 | LINKUSDT | 32% | 1.9 | 23.5 | 102.7 | 4.2 | 17.4 | 5 |
| 3 | JSTUSDT | 29% | 1.3 | 29.9 | -7.0 | -4.5 | 36.8 | 10 |
| 4 | TRXUSDT | 29% | 0.3 | 46.5 | 23.9 | 19.3 | 12.0 | 7 |
| 5 | SOLUSDT | 26% | 0.0 | 211.0 | 186.2 | -33.6 | -7.2 | 2 |
| 6 | STXUSDT | 26% | -1.5 | 107.8 | 89.0 | -23.2 | 26.4 | 0 |
| 7 | XRPUSDT | 21% | -3.9 | 21.5 | -1.8 | -15.6 | -8.2 | 2 |
| 8 | ETHUSDT | 21% | -6.0 | 38.5 | 27.9 | -26.9 | -10.8 | 3 |
| 9 | DOGEUSDT | 18% | -0.2 | 49.7 | 117.4 | -26.1 | 1.2 | 2 |
| 10 | VETUSDT | 18% | -5.7 | 29.0 | 14.4 | -14.2 | 39.1 | 0 |
| 11 | UNIUSDT | 15% | 2.9 | 29.0 | 30.5 | -4.4 | -2.1 | 1 |
| 12 | ADAUSDT | 12% | -7.2 | 61.5 | 19.2 | -34.2 | -1.8 | 0 |
| 13 | ETCUSDT | 12% | -14.5 | 37.5 | 5.1 | -29.5 | 13.6 | 0 |
| 14 | HBARUSDT | 9% | -0.3 | 26.7 | 25.2 | -14.3 | 11.3 | 2 |
| 15 | ATOMUSDT | 9% | -1.2 | 16.9 | 14.0 | -25.9 | 16.8 | 0 |
| 16 | SHIBUSDT | 9% | -1.9 | 16.3 | 24.0 | -16.5 | 14.6 | 2 |
| 17 | ZECUSDT | 9% | -2.4 | 27.3 | -18.2 | 27.3 | -0.3 | 2 |
| 18 | ALGOUSDT | 9% | -4.4 | 29.6 | -19.7 | -27.0 | 53.0 | 0 |
| 19 | BNBUSDT | 9% | -5.9 | 41.8 | 74.0 | -20.3 | -12.4 | 0 |
| 20 | XLMUSDT | 9% | -6.0 | 3.5 | -8.1 | -13.8 | 18.0 | 3 |
| 21 | BCHUSDT | 6% | -2.8 | 2.5 | 5.9 | -29.9 | -29.0 | 0 |
| 22 | AVAXUSDT | 6% | -6.8 | 16.9 | 102.0 | -22.9 | 5.6 | 1 |
| 23 | DOTUSDT | 6% | -7.9 | 19.3 | 19.0 | -10.2 | 1.6 | 2 |
| 24 | BTCUSDT | 6% | -10.3 | 18.4 | 36.4 | -30.9 | -2.4 | 1 |
| 25 | DASHUSDT | 6% | -18.7 | 13.4 | -23.5 | -11.8 | 8.2 | 0 |
| 26 | FILUSDT | 3% | -16.5 | 19.5 | -36.9 | -44.5 | 16.1 | 0 |
| 27 | NEARUSDT | 3% | -25.0 | 1.8 | 59.7 | -29.8 | -12.3 | 0 |
| 28 | CAKEUSDT | 3% | -36.9 | 4.7 | -38.2 | -33.1 | 16.4 | 0 |
| 29 | QNTUSDT | 0% | -0.5 | n/a | -12.4 | -28.1 | 22.4 | 0 |
| 30 | AAVEUSDT | 0% | -14.4 | n/a | 13.2 | -26.2 | 26.7 | 0 |
| 31 | LTCUSDT | 0% | -19.7 | n/a | -8.3 | -32.6 | 3.2 | 0 |
| 32 | ICPUSDT | 0% | -24.9 | n/a | -43.7 | -30.0 | 13.2 | 0 |
| 33 | RAYUSDT | 0% | -48.6 | n/a | -66.9 | -49.3 | -15.5 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| INJUSDT | max-income | [eth_dip_ws__INJUSDT__max-income__v002.md](symbols/INJUSDT/eth_dip_ws__INJUSDT__max-income__v002.md) | 36.8 | 38.6 | 36.8 | -22.9 | 52.2 | 23/26 |
| INJUSDT | balanced | [eth_dip_ws__INJUSDT__balanced__v002.md](symbols/INJUSDT/eth_dip_ws__INJUSDT__balanced__v002.md) | 36.8 | 38.6 | 36.8 | -22.9 | 52.2 | 23/26 |
| INJUSDT | safe-starter | [eth_dip_ws__INJUSDT__safe-starter__v002.md](symbols/INJUSDT/eth_dip_ws__INJUSDT__safe-starter__v002.md) | 14.2 | 5.7 | 5.7 | -15.5 | 42.9 | 21/28 |
| LINKUSDT | max-income | [eth_dip_ws__LINKUSDT__max-income__v002.md](symbols/LINKUSDT/eth_dip_ws__LINKUSDT__max-income__v002.md) | 35.9 | 25.1 | 25.1 | -47.8 | 69.4 | 36/27 |
| LINKUSDT | balanced | [eth_dip_ws__LINKUSDT__balanced__v002.md](symbols/LINKUSDT/eth_dip_ws__LINKUSDT__balanced__v002.md) | 35.2 | 22.0 | 22.0 | -50.9 | 67.6 | 37/28 |
| LINKUSDT | safe-starter | [eth_dip_ws__LINKUSDT__safe-starter__v002.md](symbols/LINKUSDT/eth_dip_ws__LINKUSDT__safe-starter__v002.md) | 4.1 | 11.4 | 4.1 | -15.4 | 47.6 | 21/17 |
| TRXUSDT | max-income | [eth_dip_ws__TRXUSDT__max-income__v002.md](symbols/TRXUSDT/eth_dip_ws__TRXUSDT__max-income__v002.md) | 77.6 | 24.1 | 24.1 | -70.8 | 42.9 | 21/6 |
| TRXUSDT | balanced | [eth_dip_ws__TRXUSDT__balanced__v002.md](symbols/TRXUSDT/eth_dip_ws__TRXUSDT__balanced__v002.md) | 29.0 | 8.0 | 8.0 | -49.1 | 46.7 | 30/10 |
| TRXUSDT | safe-starter | [eth_dip_ws__TRXUSDT__safe-starter__v002.md](symbols/TRXUSDT/eth_dip_ws__TRXUSDT__safe-starter__v002.md) | 9.3 | 12.4 | 9.3 | -23.6 | 26.9 | 26/10 |
| top3 | max-income | [eth_dip_ws__top3__max-income__v001.md](symbols/top3/eth_dip_ws__top3__max-income__v001.md) | 18.0 | 8.3 | 8.3 | -54.4 | 24.4 | 201/120 |
| top3 | balanced | [eth_dip_ws__top3__balanced__v001.md](symbols/top3/eth_dip_ws__top3__balanced__v001.md) | 8.1 | 8.1 | 8.1 | -17.7 | 67.0 | 88/65 |
| top3 | safe-starter | [eth_dip_ws__top3__safe-starter__v001.md](symbols/top3/eth_dip_ws__top3__safe-starter__v001.md) | 10.8 | 4.9 | 4.9 | -15.3 | 25.6 | 39/22 |


## Analyst notes

<!-- analyst-notes:start -->
This was a ~5-minute trial run (base 2 min, screen 45 s, ~35 s per symbol, 45 s basket), not the full 24 h. Treat everything below as a first look.

**ETH itself (the user's idea as written).** The description's values (RSI 14, buy < 25, sell > 55, stop -6 %) lose badly on ETH 4h: -82.6 % in-sample 2018-2023 (123 trades, 79 of them stopped out), -28 % out-of-sample. Dips on 4h ETH often keep falling more than 6 %, so the stop fires before RSI recovers. The optimizer only found profitable ETH sets by moving away from "dip buying": RSI length 38, buy < 30, sell > 80. That holds through long trends (61 % time in market, 10 % win rate, max drawdown -70 %), the profit comes from 2020 and 2023, and 2025-2026 lose. I would not paper-trade any ETH variant. No balanced variant passed (win-rate gate 45 %).

**Where it works.** The in-sample screen ranked INJ, LINK, JST and TRX highest; ETH was only 8th. Even there the median sampled set earns far less than buy & hold, so on these coins this is a dip-buying overlay that sits in cash most of the time, not a way to beat holding in bull markets.
- **INJUSDT** (RSI 24, buy < 30, sell > 40, stop 6 %): the cleanest result. Short rebounds out of oversold, 52 % win rate, +36.8 %/yr IS and +38.6 %/yr OOS, worst drawdown -23 %, positive in every calendar year 2021-2026. Same set wins max-income and balanced. Caveat: INJ is outside the top 20, so 0.05 % slippage may be optimistic.
- **LINKUSDT** (RSI 16, buy < 26, sell > 55, stop 14-15 %): close to the user's own rule, but with a much wider stop. Good 2019-2025, but -40 % to -46 % in 2026 and drawdowns near -50 %. The wide stop is what makes it work and also what makes it dangerous.
- **TRXUSDT** max-income: +77.6 %/yr IS but only 6 OOS trades and -71 % drawdown; driven by 2020, 2021 and 2023. Not trustworthy yet. TRX safe-starter (RSI 12, buy < 16, sell > 65, stop 3 %) is steadier: about 9-12 %/yr, drawdown -24 %.
- **Basket top3 (INJ+LINK+TRX, one parameter set)**: 200+ IS trades back each result, so it is the least likely to be overfit. Balanced (RSI 16, buy < 24, sell > 35, stop 10 %) earns 8.1 %/yr in both periods, drawdown -18 %, 67 % win rate. It stopped on the time budget, not converged.

**Stability.** INJ looks stable across years and periods; LINK and TRX max-income depend on a few strong years and are hurting in 2026. Several bests needed range extensions (exit level down to 25, RSI length up to 36-44, stop up to 18 %); none sits on an edge now.

**What I would paper-trade first:** INJUSDT max-income/balanced at about 25 % of the account per trade (the summary estimates ~44 % would have kept the worst drawdown near 10 %; I'd stay below that because of the short search and INJ's thinner liquidity), and the top3 basket balanced (~50 % size; estimate ~56 %) as the more diversified alternative. Run a longer optimization before trusting any of it: the short runs searched only a few hundred to ~1,500 sets per folder.
<!-- analyst-notes:end -->

---

Searching 1,505 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
