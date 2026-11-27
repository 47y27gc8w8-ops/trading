# failed_downside_breakout__broad: optimization summary

Updated 2026-11-26T00:51:40Z · backtest.py version `af30724b73` · 847 parameter sets tested with this version (847 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [failed_downside_breakout__broad__max-income__v002.md](failed_downside_breakout__broad__max-income__v002.md) | 847 | `{"max_candles": 40, "n": 12, "stop_atr": 4.75, "take_profit_atr": 1.5}` | long RSP since 2026-11-19 00:00 @ 215.974777; long XLE since 2026-11-25 00:00 @ 59.997994; long USO since 2026-11-11 00:00 @ 142.702802; long CSSMI.SW since 2026-11-24 00:00 @ 152.985884 |
| balanced | [failed_downside_breakout__broad__balanced__v001.md](failed_downside_breakout__broad__balanced__v001.md) | 294 | `{"max_candles": 80, "n": 46, "stop_atr": 3.0, "take_profit_atr": 1.5}` | long XLE since 2026-11-25 00:00 @ 59.997994; long USO since 2026-11-25 00:00 @ 137.821333 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 46,801.39 | 10,211.41 | 5,430.29 | 3,481.80 |
| return % | 468.01 | 102.11 | 54.30 | 34.82 |
| return %/year | 8.6 | 6.7 | 2.1 | 2.8 |
| gross profit | 68,888.02 | 18,864.01 | 11,061.90 | 6,926.69 |
| gross loss | 22,086.63 | 8,652.60 | 5,631.61 | 3,444.90 |
| trades | 4,078 | 3,384 | 1,857 | 1,525 |
| win rate % | 71.0 | 71.4 | 65.9 | 69.1 |
| avg win | 23.80 | 7.81 | 9.04 | 6.57 |
| avg loss | -18.67 | -8.94 | -8.88 | -7.31 |
| avg result / trade | 11.48 | 3.02 | 2.92 | 2.28 |
| largest single loss | -2,761.52 | -1,216.43 | -240.62 | -125.07 |
| largest loss % of equity | -5.70 | -11.81 | -11.46 | -13.90 |
| max drawdown | -10,655.18 | -2,336.72 | -890.70 | -713.77 |
| max drawdown % | -18.90 | -11.09 | -8.29 | -6.74 |
| profit factor | 3.12 | 2.18 | 1.96 | 2.01 |
| unusually bad trades | 369 | 353 | 88 | 67 |
| … threshold (% of equity) | 6.3 | 4.5 | 10.3 | 8.1 |
| time in market % | 7.8 | 12.2 | 3.2 | 5.0 |
| buy & hold return % | 131.76 | 280.60 | 131.76 | 280.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.77 |  | 1.33 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 3.1 | 0.8 |
| 1996 | 3.5 | 0.7 |
| 1997 | 0.9 | 0.4 |
| 1998 | -1.3 | -0.2 |
| 1999 | 6.1 | 1.2 |
| 2000 | 3.9 | 0.4 |
| 2001 | -5.2 | -2.7 |
| 2002 | -5.1 | -3.1 |
| 2003 | 5.4 | 0.7 |
| 2004 | 2.6 | 1.3 |
| 2005 | 8.3 | 2.2 |
| 2006 | 16.3 | 2.9 |
| 2007 | 11.4 | 2.0 |
| 2008 | -7.8 | -5.1 |
| 2009 | 17.8 | 1.3 |
| 2010 | 13.0 | 5.1 |
| 2011 | 1.8 | 2.9 |
| 2012 | 23.8 | 3.2 |
| 2013 | 24.0 | 3.5 |
| 2014 | 27.6 | 5.3 |
| 2015 | 45.3 | 23.7 |
| 2016 (OOS) | 36.5 | 16.0 |
| 2017 (OOS) | 60.7 | 33.2 |
| 2018 (OOS) | 57.0 | 10.3 |
| 2019 (OOS) | 41.1 | 35.2 |
| 2020 (OOS) | 21.8 | 8.7 |
| 2021 (OOS) | 107.1 | 39.5 |
| 2022 (OOS) | 23.7 | 0.1 |
| 2023 (OOS) | 26.0 | 12.0 |
| 2024 (OOS) | 74.9 | 38.9 |
| 2025 (OOS) | 105.7 | 33.7 |
| 2026 (OOS) | -5.5 | 9.5 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 18.9% from a peak in-sample and 11.1% out-of-sample, and the worst single trade cost 11.8% of the account out-of-sample. About 71 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 53% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 8.3% from a peak in-sample and 6.7% out-of-sample, and the worst single trade cost 13.9% of the account out-of-sample. About 66 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 377 | `{"max_candles": 40, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.80 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 437 | `{"max_candles": 44, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,126.12 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 493 | `{"max_candles": 64, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,126.00 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 509 | `{"max_candles": 68, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.99 | 6.1 | -12.8 | 0.70 | 4141/3446 | not checked |
| 512 | `{"max_candles": 60, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,126.29 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 560 | `{"max_candles": 72, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.75 | 6.1 | -12.8 | 0.70 | 4141/3446 | not checked |
| 574 | `{"max_candles": 56, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.92 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 593 | `{"max_candles": 52, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.84 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 600 | `{"max_candles": 48, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.87 | 6.1 | -12.8 | 0.70 | 4141/3447 | not checked |
| 622 | `{"max_candles": 76, "n": 12, "stop_atr": 4.25, "take_profit_atr": 1.5}` | 48,548.41 | 8.8 | -19.2 | 70.7 | 9,125.82 | 6.1 | -12.8 | 0.70 | 4141/3445 | not checked |
| 319 | `{"max_candles": 40, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.81 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 372 | `{"max_candles": 56, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.85 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 397 | `{"max_candles": 52, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.77 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 439 | `{"max_candles": 44, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,368.05 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 489 | `{"max_candles": 60, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,368.23 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 530 | `{"max_candles": 68, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.92 | 6.8 | -11.0 | 0.78 | 4106/3410 | not checked |
| 543 | `{"max_candles": 48, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.80 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 642 | `{"max_candles": 72, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.67 | 6.8 | -11.0 | 0.78 | 4106/3410 | not checked |
| 684 | `{"max_candles": 64, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.94 | 6.8 | -11.0 | 0.78 | 4106/3411 | not checked |
| 736 | `{"max_candles": 76, "n": 12, "stop_atr": 4.5, "take_profit_atr": 1.5}` | 47,645.34 | 8.7 | -19.0 | 70.8 | 10,367.75 | 6.8 | -11.0 | 0.78 | 4106/3409 | not checked |
| 352 | `{"max_candles": 44, "n": 12, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 47,557.53 | 8.7 | -18.1 | 71.5 | 8,070.19 | 5.6 | -9.3 | 0.64 | 3994/3316 | not checked |
| 433 | `{"max_candles": 68, "n": 12, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 47,557.53 | 8.7 | -18.1 | 71.5 | 8,069.34 | 5.6 | -9.3 | 0.64 | 3994/3314 | not checked |
| 454 | `{"max_candles": 72, "n": 12, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 47,557.53 | 8.7 | -18.1 | 71.5 | 8,069.34 | 5.6 | -9.3 | 0.64 | 3994/3314 | not checked |
| 463 | `{"max_candles": 64, "n": 12, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 47,557.53 | 8.7 | -18.1 | 71.5 | 8,068.99 | 5.6 | -9.3 | 0.64 | 3994/3315 | not checked |
| 494 | `{"max_candles": 48, "n": 12, "stop_atr": 5.75, "take_profit_atr": 1.5}` | 47,557.53 | 8.7 | -18.1 | 71.5 | 8,069.31 | 5.6 | -9.3 | 0.64 | 3994/3316 | not checked |

(170 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 847 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
