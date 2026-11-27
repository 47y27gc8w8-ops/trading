# breakout_ws: optimization summary

Updated 2026-11-24T22:22:55Z · backtest.py version `0f3087d9a4` · 1,594 parameter sets tested with this version (1,594 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1d bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 12 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breakout_ws__max-income__v001.md](breakout_ws__max-income__v001.md) | 1592 | `{"entry_n": 21, "exit_n": 13}` | flat (data up to 2026-11-23 00:00) |
| balanced | [breakout_ws__balanced__v001.md](breakout_ws__balanced__v001.md) | 1593 | `{"entry_n": 56, "exit_n": 7}` | flat (data up to 2026-11-23 00:00) |
| safe-starter | [breakout_ws__safe-starter__v001.md](breakout_ws__safe-starter__v001.md) | 1594 | `{"entry_n": 52, "exit_n": 9}` | flat (data up to 2026-11-23 00:00) |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 92,830.42 | 4,615.94 | 27,333.75 | 6,568.86 | 31,188.28 | 5,016.17 |
| return % | 928.30 | 46.16 | 273.34 | 65.69 | 311.88 | 50.16 |
| return %/year | 47.5 | 14.0 | 24.6 | 19.1 | 26.6 | 15.1 |
| gross profit | 170,859.67 | 14,812.36 | 43,821.04 | 11,422.95 | 51,724.71 | 10,371.36 |
| gross loss | 78,029.26 | 10,196.42 | 16,487.28 | 4,854.09 | 20,536.43 | 5,355.20 |
| trades | 22 | 15 | 20 | 10 | 19 | 11 |
| win rate % | 40.9 | 40.0 | 55.0 | 50.0 | 57.9 | 45.5 |
| avg win | 18,984.41 | 2,468.73 | 3,983.73 | 2,284.59 | 4,702.25 | 2,074.27 |
| avg loss | -6,002.25 | -1,132.94 | -1,831.92 | -970.82 | -2,567.05 | -892.53 |
| avg result / trade | 4,219.56 | 307.73 | 1,366.69 | 656.89 | 1,641.49 | 456.02 |
| largest single loss | -23,688.28 | -2,559.48 | -4,031.93 | -1,322.19 | -4,854.87 | -1,212.93 |
| largest loss % of equity | -22.39 | -14.76 | -12.03 | -7.69 | -12.03 | -7.69 |
| max drawdown | -66,118.62 | -9,425.08 | -13,716.43 | -4,787.68 | -16,516.01 | -4,674.40 |
| max drawdown % | -53.32 | -42.38 | -41.08 | -24.00 | -37.43 | -25.15 |
| profit factor | 2.19 | 1.45 | 2.66 | 2.35 | 2.52 | 1.94 |
| unusually bad trades | 3 | 1 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 17.2 | 14.1 | 18.8 | 12.2 | 23.4 | 13.2 |
| time in market % | 48.1 | 48.2 | 26.7 | 23.1 | 31.8 | 28.4 |
| buy & hold return % | 208.29 | 44.91 | 208.29 | 44.91 | 208.29 | 44.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |  | 0.78 |  | 0.57 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2018 | -22.8 | -9.9 | -25.4 |
| 2019 | 80.3 | 97.9 | 97.9 |
| 2020 | 321.1 | 57.0 | 128.4 |
| 2021 | 68.0 | -0.5 | -0.5 |
| 2022 | -41.2 | -8.2 | -8.2 |
| 2023 | 78.0 | 46.1 | 33.9 |
| 2024 (OOS) | 90.6 | 83.9 | 64.4 |
| 2025 (OOS) | -17.4 | -0.5 | 2.1 |
| 2026 (OOS) | -1.1 | -3.6 | -4.8 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 53.3% from a peak in-sample and 42.4% out-of-sample, and the worst single trade cost 14.8% of the account out-of-sample. About 41 of every 100 trades won in-sample. Out-of-sample it earned 14.0% a year against 47.5% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 19% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks high: the account fell up to 41.1% from a peak in-sample and 24.0% out-of-sample, and the worst single trade cost 7.7% of the account out-of-sample. About 55 of every 100 trades won in-sample. With 100% of equity per trade; about 24% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks high: the account fell up to 37.4% from a peak in-sample and 25.1% out-of-sample, and the worst single trade cost 7.7% of the account out-of-sample. About 58 of every 100 trades won in-sample. Out-of-sample it earned 15.1% a year against 26.6% in-sample, so expect clearly less than the in-sample numbers suggest. With 100% of equity per trade; about 27% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1321 | `{"entry_n": 21, "exit_n": 13}` | 92,830.42 | 47.5 | -53.3 | 40.9 | 4,615.94 | 14.0 | -42.4 | 0.29 | 22/15 | 1.00 |
| 729 | `{"entry_n": 19, "exit_n": 9}` | 87,600.59 | 46.2 | -52.0 | 55.6 | 5,780.42 | 17.1 | -29.3 | 0.37 | 27/17 | not checked |
| 501 | `{"entry_n": 41, "exit_n": 14}` | 86,334.55 | 45.9 | -47.9 | 43.8 | 3,699.68 | 11.5 | -38.5 | 0.25 | 16/11 | not checked |
| 182 | `{"entry_n": 60, "exit_n": 12}` | 71,163.11 | 41.8 | -40.2 | 61.5 | 4,300.03 | 13.2 | -30.2 | 0.32 | 13/10 | not checked |
| 194 | `{"entry_n": 57, "exit_n": 12}` | 71,163.11 | 41.8 | -40.2 | 61.5 | 4,300.03 | 13.2 | -30.2 | 0.32 | 13/10 | not checked |
| 853 | `{"entry_n": 58, "exit_n": 12}` | 71,163.11 | 41.8 | -40.2 | 61.5 | 4,300.03 | 13.2 | -30.2 | 0.32 | 13/10 | not checked |
| 998 | `{"entry_n": 56, "exit_n": 12}` | 71,163.11 | 41.8 | -40.2 | 61.5 | 4,530.50 | 13.8 | -29.0 | 0.33 | 13/10 | not checked |
| 1408 | `{"entry_n": 59, "exit_n": 12}` | 71,163.11 | 41.8 | -40.2 | 61.5 | 4,300.03 | 13.2 | -30.2 | 0.32 | 13/10 | not checked |
| 274 | `{"entry_n": 59, "exit_n": 9}` | 40,085.73 | 30.8 | -37.4 | 64.7 | 5,903.33 | 17.4 | -26.3 | 0.56 | 17/10 | not checked |
| 597 | `{"entry_n": 58, "exit_n": 9}` | 40,085.73 | 30.8 | -37.4 | 64.7 | 5,903.33 | 17.4 | -26.3 | 0.56 | 17/10 | not checked |
| 1017 | `{"entry_n": 56, "exit_n": 9}` | 40,085.73 | 30.8 | -37.4 | 64.7 | 6,159.64 | 18.1 | -25.1 | 0.59 | 17/10 | not checked |
| 1044 | `{"entry_n": 60, "exit_n": 9}` | 40,085.73 | 30.8 | -37.4 | 64.7 | 5,903.33 | 17.4 | -26.3 | 0.56 | 17/10 | not checked |
| 1524 | `{"entry_n": 57, "exit_n": 9}` | 40,085.73 | 30.8 | -37.4 | 64.7 | 5,903.33 | 17.4 | -26.3 | 0.56 | 17/10 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

33 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ETHUSDT | 100% | 32.3 | 61.6 | 20.8 | 45.1 | -21.7 | 39 |
| 2 | ETCUSDT | 100% | 30.2 | 74.9 | 14.2 | 48.9 | -29.5 | 0 |
| 3 | BNBUSDT | 98% | 75.6 | 122.7 | 80.3 | 70.4 | 21.1 | 16 |
| 4 | VETUSDT | 98% | 58.9 | 145.3 | 41.3 | 145.3 | 5.6 | 12 |
| 5 | BTCUSDT | 97% | 34.7 | 53.4 | 20.6 | 44.9 | 9.5 | 33 |
| 6 | LINKUSDT | 92% | 21.5 | 101.9 | 86.1 | 38.3 | -19.1 | 0 |
| 7 | DOGEUSDT | 91% | 79.2 | 165.6 | 134.3 | 83.9 | 29.7 | 30 |
| 8 | ADAUSDT | 75% | 78.2 | 100.6 | 41.0 | 82.0 | -25.8 | 0 |
| 9 | TRXUSDT | 64% | 11.4 | 45.5 | 30.6 | 24.6 | 32.3 | 41 |
| 10 | ATOMUSDT | 58% | 14.6 | 39.7 | 38.0 | -4.4 | -20.4 | 0 |
| 11 | LTCUSDT | 52% | 1.7 | 21.4 | -8.2 | -1.0 | -11.1 | 1 |
| 12 | ALGOUSDT | 48% | 30.8 | 73.2 | -0.0 | 40.6 | 21.9 | 11 |
| 13 | XRPUSDT | 48% | -0.8 | 47.5 | 12.1 | 3.4 | 35.4 | 25 |
| 14 | HBARUSDT | 44% | 68.8 | 112.2 | 66.2 | 96.6 | 17.1 | 6 |
| 15 | STXUSDT | 39% | 124.7 | 153.1 | 80.0 | 37.7 | -4.3 | 1 |
| 16 | INJUSDT | 38% | 27.7 | 76.6 | 38.0 | 32.9 | -10.9 | 0 |
| 17 | SOLUSDT | 36% | 298.7 | 412.6 | 283.8 | 343.8 | 5.5 | 0 |
| 18 | DOTUSDT | 36% | 70.0 | 78.1 | 15.9 | 59.8 | -14.1 | 0 |
| 19 | NEARUSDT | 28% | 70.5 | 96.6 | 4.2 | 96.6 | -1.3 | 4 |
| 20 | DASHUSDT | 28% | -4.1 | 37.7 | -25.2 | 17.9 | 52.7 | 14 |
| 21 | AVAXUSDT | 27% | 110.6 | 197.5 | 49.9 | 131.0 | -20.4 | 0 |
| 22 | BCHUSDT | 22% | -2.1 | 15.0 | 3.5 | 1.8 | -20.0 | 1 |
| 23 | ZECUSDT | 20% | -11.1 | 27.9 | -21.5 | -11.4 | 259.1 | 13 |
| 24 | UNIUSDT | 16% | 37.2 | 59.5 | 1.2 | 59.5 | 23.5 | 4 |
| 25 | XLMUSDT | 16% | -15.6 | 24.8 | -12.5 | -4.4 | 32.7 | 6 |
| 26 | JSTUSDT | 12% | 24.2 | 33.0 | 7.6 | 22.6 | 29.3 | 8 |
| 27 | CAKEUSDT | 11% | 22.8 | 26.1 | -44.8 | 30.3 | -16.7 | 0 |
| 28 | SHIBUSDT | 9% | 30.8 | 77.2 | 16.9 | 64.3 | -17.9 | 2 |
| 29 | FILUSDT | 9% | 28.4 | 26.2 | -45.8 | 8.5 | -27.1 | 1 |
| 30 | QNTUSDT | 8% | 8.6 | 22.7 | -21.3 | 14.1 | 25.1 | 4 |
| 31 | ICPUSDT | 6% | 26.9 | 24.4 | -48.4 | 1.7 | -36.4 | 0 |
| 32 | RAYUSDT | 2% | 60.6 | 70.8 | -60.9 | 23.6 | 70.8 | 1 |
| 33 | AAVEUSDT | 2% | -32.1 | 7.5 | -41.8 | -6.7 | 0.2 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| BNBUSDT | max-income | [breakout_ws__BNBUSDT__max-income__v001.md](symbols/BNBUSDT/breakout_ws__BNBUSDT__max-income__v001.md) | 107.3 | 30.1 | 30.1 | -56.8 | 60.0 | 20/10 |
| BNBUSDT | balanced | [breakout_ws__BNBUSDT__balanced__v001.md](symbols/BNBUSDT/breakout_ws__BNBUSDT__balanced__v001.md) | 98.1 | 26.3 | 26.3 | -64.9 | 54.2 | 24/12 |
| BNBUSDT | safe-starter | [breakout_ws__BNBUSDT__safe-starter__v001.md](symbols/BNBUSDT/breakout_ws__BNBUSDT__safe-starter__v001.md) | 89.4 | 24.9 | 24.9 | -49.4 | 50.0 | 20/9 |
| ETCUSDT | none passed | | | | | | | |
| ETHUSDT | max-income | [breakout_ws__ETHUSDT__max-income__v001.md](symbols/ETHUSDT/breakout_ws__ETHUSDT__max-income__v001.md) | 54.9 | 15.1 | 15.1 | -66.6 | 48.1 | 52/26 |
| ETHUSDT | balanced | [breakout_ws__ETHUSDT__balanced__v002.md](symbols/ETHUSDT/breakout_ws__ETHUSDT__balanced__v002.md) | 20.1 | 7.5 | 7.5 | -49.8 | 47.9 | 48/20 |
| ETHUSDT | safe-starter | [breakout_ws__ETHUSDT__safe-starter__v001.md](symbols/ETHUSDT/breakout_ws__ETHUSDT__safe-starter__v001.md) | 22.4 | 8.9 | 8.9 | -35.1 | 44.8 | 29/13 |
| VETUSDT | max-income | [breakout_ws__VETUSDT__max-income__v001.md](symbols/VETUSDT/breakout_ws__VETUSDT__max-income__v001.md) | 107.2 | 27.8 | 27.8 | -54.0 | 55.0 | 20/8 |
| VETUSDT | balanced | [breakout_ws__VETUSDT__balanced__v001.md](symbols/VETUSDT/breakout_ws__VETUSDT__balanced__v001.md) | 69.3 | 26.5 | 26.5 | -43.8 | 55.6 | 27/9 |
| VETUSDT | safe-starter | [breakout_ws__VETUSDT__safe-starter__v001.md](symbols/VETUSDT/breakout_ws__VETUSDT__safe-starter__v001.md) | 62.9 | 17.8 | 17.8 | -47.0 | 53.3 | 30/13 |
| broad | max-income | [breakout_ws__broad__max-income__v001.md](symbols/broad/breakout_ws__broad__max-income__v001.md) | 57.7 | 17.9 | 17.9 | -64.9 | 42.8 | 446/367 |
| broad | balanced | [breakout_ws__broad__balanced__v001.md](symbols/broad/breakout_ws__broad__balanced__v001.md) | 32.7 | 20.2 | 20.2 | -26.2 | 42.9 | 438/298 |
| top3 | max-income | [breakout_ws__top3__max-income__v002.md](symbols/top3/breakout_ws__top3__max-income__v002.md) | 56.4 | 16.0 | 16.0 | -45.4 | 52.5 | 59/28 |
| top3 | balanced | [breakout_ws__top3__balanced__v002.md](symbols/top3/breakout_ws__top3__balanced__v002.md) | 47.7 | 12.7 | 12.7 | -33.5 | 49.5 | 99/38 |
| top3 | safe-starter | [breakout_ws__top3__safe-starter__v001.md](symbols/top3/breakout_ws__top3__safe-starter__v001.md) | 44.4 | 11.2 | 11.2 | -56.5 | 52.0 | 50/24 |


## Analyst notes

<!-- analyst-notes:start -->
**Short trial run (~10 min total, as asked).** Daily bars, the 2-parameter grid (1,568 sets) is small, so
the base run and the four single-coin runs tested their whole grid; only the 3-coin basket stopped on
its time budget (1,379 sets). A longer run will mostly add range extensions and more basket coverage.

**What the variants do differently.** max-income variants use a mid-length breakout (21–38 days) with a
slower exit (8–17 days) and ride big trends but give back a lot (drawdowns 45–67%). balanced/safe-starter
variants mostly use a *much shorter exit* (2–9 days) and often a longer entry (50–59 days on BTC/ETH):
fewer, cleaner breakouts and quick exits, lower time in market, smaller drawdowns, lower return.

**Where it works.** In the in-sample screen the idea is profitable on most large, long-listed coins
(ETH, ETC, BNB, VET, BTC, LINK, DOGE: 94–100% of sampled settings profitable) and weak on coins that
mostly drifted down or chopped (LTC, BCH, XLM, AAVE, FIL, ICP). That fits the user's intuition: it is a
trend follower. Coins listed after ~2022 could not be tested (too little in-sample history).
- **VETUSDT**: best evidence. All three variants pass out-of-sample (+18–28 %/yr) while VET itself fell
  ~87% in 2024–2026: the exit rule kept it out of the decline.
- **BNBUSDT**: passes (+25–30 %/yr OOS vs buy & hold ~+22 %/yr), but in-sample it trailed buy & hold;
  drawdowns of 49–65% are as bad as holding.
- **BTCUSDT** (base run): steady, +14–19 %/yr OOS, OOS efficiency 0.29–0.78; balanced (56/7) looks most stable.
- **ETHUSDT**: passes but weakly out-of-sample (+7.5–15 %/yr), ETH buy & hold was −24% OOS.
- **ETCUSDT**: profitable in-sample for every setting but **nothing passed**: most sets lost money in
  2024–2026 or had < 12 in-sample trades. Treat ETC as "doesn't work".
- **Basket ETH+ETC+VET** (one parameter set for all three): +11–16 %/yr OOS with 24–38 OOS trades, the
  most trades behind any result here; it is dragged down by ETC.

**Stability.** Calendar-year returns are lumpy: most profit comes from 2019–2020 and 2023–2024 trend
years; 2018, 2022 and 2025 are flat to negative for most variants. OOS returns are 25–80% of IS returns,
so expect clearly less than the in-sample numbers.

**Range notes.** exit_n was extended down to its floor (2, set by valid()) on ETH and in the basket; the
ETH balanced (23/2) and basket balanced (32/2) variants sit on that floor. An exit after 2 days is a
legitimate value of the rule but far from the user's "10 days"; it trades a lot and is fee-sensitive.

**Paper-trade first:** VETUSDT balanced (32/4): 26.5 %/yr conservative, worst DD −44%, 27/9 trades.
Size ~20–25% of the account per trade (the size that would have held the worst drawdown near 10%), not
100%. Second choice for a lower-volatility coin: BTCUSDT balanced (56/7), ~24% size. VET has few OOS
trades (9), so the evidence is thin.
**Update 2026-11-25: re-screen + broad basket.** The re-screen (60 configured coins, 33 with enough data) now includes
the ranking-persistence check, and it came out **NOT PERSISTENT**: coins that did best in the first half of the
in-sample period did *worse* than the rest in the second half (rank correlation −0.29; top 8 −17%/yr vs +1.4%/yr).
So the idea "it only works on trending coins" can't be turned into a coin pick in advance with this evidence: which coins
trend is only clear afterwards. Treat the BNB/ETH/VET/ETC and top-3 variants above as **low confidence** (the
leaderboard marks them ⚠). The **broad basket** (one setting across all 33 coins, 446/367 trades) is now the main result:
- balanced `entry 57 / exit 5`: 32.7%/yr IS, 20.2%/yr OOS, worst drawdown −26%, efficiency 0.62.
- max-income `entry 21 / exit 20`: 57.7%/yr IS but 17.9%/yr OOS with −65%/−45% drawdowns. Slow exits give back a lot.
- No safe-starter: every set has many unusually bad trades (gap-downs on small coins with 100% sizing).
Across the in-sample Pareto front, short exits (4–9 days) kept their return out-of-sample much better (efficiency
~0.7–1.0) than slow exits (~0.3–0.45). This is an observation, not a selection.
**Main risk:** profits are concentrated in 2020–2021 (+184% balanced, +501% max-income in 2021), and both broad variants
lost money in 2025 (−11/−14%) and 2026 so far (−4/−21%). The edge looks to have weakened in the recent choppy market.
**Paper-trade first:** broad balanced (57/5) at about 1/3 of the normal size per position (summary suggests ~38%). Watch
whether 2026's losses keep going before adding size. Per-coin variants only as an experiment.
<!-- analyst-notes:end -->

---

Searching 1,594 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
