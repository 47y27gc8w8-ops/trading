# golden_cross__broad: optimization summary

Updated 2026-11-26T02:12:40Z · backtest.py version `de16b83fb5` · 1,181 parameter sets tested with this version (1,181 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 8 in-sample and ≥ 3 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [golden_cross__broad__max-income__v002.md](golden_cross__broad__max-income__v002.md) | 1180 | `{"fast": 20, "max_candles": 184, "slow": 210, "stop_atr": 4.25, "take_profit_atr": 10.0}` | long SPY since 2026-04-14 00:00 @ 684.429088; long XLF since 2026-06-22 00:00 @ 53.446926; long XLY since 2026-11-10 00:00 @ 120.216054; long XLP since 2026-10-19 00:00 @ 86.876053; long VNQ since 2026-11-10 00:00 @ 96.578968; long ^GSPC since 2026-04-17 00:00 @ 7076.67217; long ^DJI since 2026-04-16 00:00 @ 48572.387659; long ^VIX since 2026-11-06 00:00 @ 27.688304; long ^GDAXI since 2026-05-07 00:00 @ 24947.841483 |
| balanced | [golden_cross__broad__balanced__v002.md](golden_cross__broad__balanced__v002.md) | 1181 | `{"fast": 70, "max_candles": 64, "slow": 210, "stop_atr": 2.75, "take_profit_atr": 6.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 4,272.23 | 5,064.93 | 1,621.72 | 257.45 |
| return % | 42.72 | 50.65 | 16.22 | 2.57 |
| return %/year | 1.7 | 3.8 | 0.7 | 0.2 |
| gross profit | 7,559.30 | 7,821.98 | 2,838.84 | 1,849.95 |
| gross loss | 3,287.07 | 2,757.05 | 1,217.12 | 1,592.50 |
| trades | 652 | 615 | 391 | 386 |
| win rate % | 46.5 | 48.8 | 54.2 | 35.2 |
| avg win | 24.95 | 26.07 | 13.39 | 13.60 |
| avg loss | -9.42 | -8.75 | -6.80 | -6.37 |
| avg result / trade | 6.55 | 8.24 | 4.15 | 0.67 |
| largest single loss | -39.54 | -45.29 | -44.06 | -57.17 |
| largest loss % of equity | -28.96 | -33.51 | -27.32 | -36.92 |
| max drawdown | -910.60 | -916.61 | -258.23 | -418.45 |
| max drawdown % | -6.31 | -7.29 | -2.57 | -4.12 |
| profit factor | 2.30 | 2.84 | 2.33 | 1.16 |
| unusually bad trades | 44 | 38 | 21 | 18 |
| … threshold (% of equity) | 9.8 | 9.3 | 7.5 | 6.6 |
| time in market % | 13.6 | 25.3 | 3.9 | 5.9 |
| buy & hold return % | 124.26 | 281.73 | 124.26 | 281.73 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.25 |  | 0.32 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.4 | -0.1 |
| 1996 | 0.5 | 0.1 |
| 1997 | 0.5 | -0.2 |
| 1998 | 0.3 | -0.2 |
| 1999 | 1.3 | 0.6 |
| 2000 | -1.6 | -0.7 |
| 2001 | -1.7 | -0.9 |
| 2002 | -2.3 | -0.7 |
| 2003 | 8.0 | 3.2 |
| 2004 | 1.8 | 0.8 |
| 2005 | 0.5 | -1.3 |
| 2006 | 4.5 | 1.5 |
| 2007 | 1.4 | 0.5 |
| 2008 | -2.2 | -0.2 |
| 2009 | 14.0 | 6.5 |
| 2010 | 6.4 | 3.7 |
| 2011 | 0.9 | 0.8 |
| 2012 | 5.0 | 0.9 |
| 2013 | 3.3 | 1.0 |
| 2014 | -0.7 | 0.0 |
| 2015 | -2.7 | -0.0 |
| 2016 (OOS) | 3.9 | -0.5 |
| 2017 (OOS) | 1.4 | 0.5 |
| 2018 (OOS) | -1.3 | -0.5 |
| 2019 (OOS) | 6.5 | -1.7 |
| 2020 (OOS) | 14.0 | 2.7 |
| 2021 (OOS) | 1.1 | 0.4 |
| 2022 (OOS) | -3.4 | 0.2 |
| 2023 (OOS) | 6.6 | -0.7 |
| 2024 (OOS) | 2.3 | 1.0 |
| 2025 (OOS) | 12.3 | 2.4 |
| 2026 (OOS) | 4.0 | -0.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 6.3% from a peak in-sample and 7.3% out-of-sample, and the worst single trade cost 33.5% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 2.6% from a peak in-sample and 4.1% out-of-sample, and the worst single trade cost 36.9% of the account out-of-sample. About 54 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.7% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1099 | `{"fast": 35, "max_candles": 192, "slow": 200, "stop_atr": 4.75, "take_profit_atr": 10.0}` | 4,393.96 | 1.8 | -8.1 | 53.3 | 3,797.47 | 3.0 | -7.1 | 1.71 | 510/480 | not checked |
| 1137 | `{"fast": 35, "max_candles": 192, "slow": 210, "stop_atr": 4.75, "take_profit_atr": 10.0}` | 4,330.27 | 1.7 | -6.0 | 52.0 | 3,541.79 | 2.8 | -8.2 | 1.63 | 496/475 | not checked |
| 1177 | `{"fast": 35, "max_candles": 192, "slow": 210, "stop_atr": 4.5, "take_profit_atr": 10.0}` | 4,291.42 | 1.7 | -5.8 | 51.2 | 3,443.61 | 2.8 | -8.1 | 1.60 | 496/475 | not checked |
| 1150 | `{"fast": 35, "max_candles": 192, "slow": 210, "stop_atr": 4.25, "take_profit_atr": 10.0}` | 4,155.75 | 1.7 | -5.7 | 50.4 | 3,409.05 | 2.7 | -7.8 | 1.64 | 496/475 | not checked |
| 711 | `{"fast": 35, "max_candles": 168, "slow": 210, "stop_atr": 4.0, "take_profit_atr": 10.0}` | 3,919.35 | 1.6 | -5.7 | 50.2 | 3,234.92 | 2.6 | -7.5 | 1.64 | 496/475 | not checked |
| 872 | `{"fast": 35, "max_candles": 176, "slow": 210, "stop_atr": 4.0, "take_profit_atr": 10.0}` | 3,908.73 | 1.6 | -5.6 | 50.0 | 3,283.83 | 2.6 | -7.7 | 1.67 | 496/475 | not checked |
| 834 | `{"fast": 35, "max_candles": 168, "slow": 220, "stop_atr": 3.75, "take_profit_atr": 10.0}` | 3,795.07 | 1.5 | -5.4 | 50.3 | 3,162.40 | 2.6 | -6.2 | 1.66 | 473/469 | not checked |
| 724 | `{"fast": 35, "max_candles": 168, "slow": 210, "stop_atr": 3.5, "take_profit_atr": 10.0}` | 3,746.73 | 1.5 | -5.3 | 48.6 | 2,846.31 | 2.3 | -7.2 | 1.52 | 496/475 | not checked |
| 578 | `{"fast": 30, "max_candles": 192, "slow": 210, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 3,383.96 | 1.4 | -5.0 | 44.7 | 3,488.83 | 2.8 | -6.6 | 1.99 | 519/506 | not checked |
| 473 | `{"fast": 30, "max_candles": 168, "slow": 230, "stop_atr": 3.0, "take_profit_atr": 10.0}` | 2,938.11 | 1.2 | -4.2 | 45.6 | 3,688.74 | 2.9 | -6.3 | 2.38 | 482/494 | not checked |
| 590 | `{"fast": 30, "max_candles": 168, "slow": 230, "stop_atr": 2.75, "take_profit_atr": 10.0}` | 2,907.25 | 1.2 | -4.1 | 44.0 | 3,745.09 | 3.0 | -6.1 | 2.43 | 482/494 | not checked |
| 481 | `{"fast": 30, "max_candles": 120, "slow": 260, "stop_atr": 3.25, "take_profit_atr": 10.0}` | 2,210.83 | 1.0 | -3.8 | 46.4 | 2,536.21 | 2.1 | -5.8 | 2.19 | 444/481 | not checked |
| 161 | `{"fast": 45, "max_candles": 96, "slow": 210, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 1,907.46 | 0.8 | -3.7 | 53.0 | 1,002.36 | 0.9 | -4.2 | 1.05 | 466/441 | not checked |
| 766 | `{"fast": 70, "max_candles": 72, "slow": 210, "stop_atr": 2.75, "take_profit_atr": 7.0}` | 1,859.21 | 0.8 | -3.1 | 54.5 | 433.96 | 0.4 | -3.9 | 0.48 | 391/386 | not checked |
| 1153 | `{"fast": 70, "max_candles": 72, "slow": 210, "stop_atr": 3.0, "take_profit_atr": 6.5}` | 1,786.08 | 0.8 | -2.7 | 56.0 | 341.27 | 0.3 | -4.2 | 0.39 | 391/386 | not checked |
| 1061 | `{"fast": 70, "max_candles": 72, "slow": 210, "stop_atr": 2.75, "take_profit_atr": 6.5}` | 1,762.76 | 0.8 | -2.7 | 55.0 | 360.18 | 0.3 | -3.9 | 0.42 | 391/386 | not checked |
| 683 | `{"fast": 70, "max_candles": 64, "slow": 210, "stop_atr": 3.0, "take_profit_atr": 6.5}` | 1,654.27 | 0.7 | -2.6 | 55.5 | 223.13 | 0.2 | -4.3 | 0.27 | 391/386 | not checked |
| 1062 | `{"fast": 70, "max_candles": 64, "slow": 210, "stop_atr": 2.75, "take_profit_atr": 6.5}` | 1,621.72 | 0.7 | -2.6 | 54.2 | 257.45 | 0.2 | -4.1 | 0.32 | 391/386 | 1.00 |
| 886 | `{"fast": 70, "max_candles": 64, "slow": 210, "stop_atr": 3.0, "take_profit_atr": 6.0}` | 1,591.84 | 0.7 | -2.4 | 56.0 | 200.96 | 0.2 | -4.3 | 0.25 | 391/386 | not checked |
| 1059 | `{"fast": 70, "max_candles": 64, "slow": 210, "stop_atr": 2.75, "take_profit_atr": 6.0}` | 1,554.95 | 0.7 | -2.3 | 54.7 | 231.66 | 0.2 | -4.1 | 0.30 | 391/386 | not checked |
| 402 | `{"fast": 70, "max_candles": 80, "slow": 240, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 1,033.22 | 0.5 | -2.2 | 56.8 | 342.28 | 0.3 | -2.5 | 0.66 | 345/353 | not checked |
| 349 | `{"fast": 60, "max_candles": 176, "slow": 210, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 823.74 | 0.4 | -2.1 | 71.6 | 112.70 | 0.1 | -3.4 | 0.26 | 416/399 | not checked |
| 436 | `{"fast": 35, "max_candles": 56, "slow": 210, "stop_atr": 1.0, "take_profit_atr": 6.0}` | 594.43 | 0.3 | -1.6 | 24.8 | 326.78 | 0.3 | -3.5 | 1.07 | 496/475 | not checked |
| 353 | `{"fast": 60, "max_candles": 56, "slow": 300, "stop_atr": 2.0, "take_profit_atr": 1.5}` | 419.22 | 0.2 | -1.4 | 57.2 | 102.34 | 0.1 | -0.8 | 0.45 | 299/312 | not checked |
| 357 | `{"fast": 80, "max_candles": 160, "slow": 250, "stop_atr": 1.0, "take_profit_atr": 4.0}` | 238.30 | 0.1 | -1.2 | 29.0 | 148.59 | 0.1 | -2.4 | 1.27 | 321/334 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,181 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
