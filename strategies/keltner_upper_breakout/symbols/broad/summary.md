# keltner_upper_breakout__broad: optimization summary

Updated 2026-11-26T02:48:09Z · backtest.py version `ee08b24994` · 775 parameter sets tested with this version (775 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [keltner_upper_breakout__broad__max-income__v002.md](keltner_upper_breakout__broad__max-income__v002.md) | 775 | `{"k": 1.5, "max_candles": 44, "stop_atr": 1.75, "take_profit_atr": 6.5}` | long IEF since 2026-11-23 00:00 @ 91.317388; long SHY since 2026-11-23 00:00 @ 81.514445; long SQQQ since 2026-11-18 00:00 @ 46.043808 |
| balanced | [keltner_upper_breakout__broad__balanced__v001.md](keltner_upper_breakout__broad__balanced__v001.md) | 243 | `{"k": 3.0, "max_candles": 72, "stop_atr": 2.25, "take_profit_atr": 2.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 921.04 | 3,970.48 | 52.61 | 10.93 |
| return % | 9.21 | 39.70 | 0.53 | 0.11 |
| return %/year | 0.4 | 3.1 | 0.0 | 0.0 |
| gross profit | 11,192.22 | 14,125.80 | 2,835.56 | 3,319.61 |
| gross loss | 10,271.18 | 10,155.32 | 2,782.95 | 3,308.67 |
| trades | 4,806 | 4,431 | 1,316 | 1,629 |
| win rate % | 36.7 | 39.4 | 47.8 | 47.4 |
| avg win | 6.35 | 8.10 | 4.51 | 4.30 |
| avg loss | -3.38 | -3.78 | -4.05 | -3.86 |
| avg result / trade | 0.19 | 0.90 | 0.04 | 0.01 |
| largest single loss | -33.49 | -113.67 | -24.27 | -28.55 |
| largest loss % of equity | -7.55 | -8.83 | -14.73 | -18.27 |
| max drawdown | -1,271.45 | -1,163.94 | -349.77 | -552.95 |
| max drawdown % | -11.59 | -8.38 | -3.40 | -5.46 |
| profit factor | 1.09 | 1.39 | 1.02 | 1.00 |
| unusually bad trades | 451 | 373 | 78 | 124 |
| … threshold (% of equity) | 3.6 | 3.3 | 4.3 | 4.1 |
| time in market % | 18.8 | 35.3 | 3.5 | 8.2 |
| buy & hold return % | 127.68 | 280.36 | 127.68 | 280.36 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 7.43 |  | 0.50 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 1.4 | 0.4 |
| 1996 | 0.8 | 0.7 |
| 1997 | 1.8 | 0.7 |
| 1998 | 3.4 | -0.1 |
| 1999 | 1.7 | 0.1 |
| 2000 | -3.3 | -0.8 |
| 2001 | -1.9 | 0.0 |
| 2002 | -3.6 | -0.3 |
| 2003 | 1.0 | 0.1 |
| 2004 | 0.1 | 0.4 |
| 2005 | 1.9 | 0.4 |
| 2006 | 0.4 | -0.2 |
| 2007 | -0.9 | -0.3 |
| 2008 | -0.9 | 0.4 |
| 2009 | 0.4 | -0.4 |
| 2010 | 6.0 | 0.2 |
| 2011 | -3.1 | -1.9 |
| 2012 | 1.6 | 0.9 |
| 2013 | 5.7 | 1.0 |
| 2014 | 0.7 | 0.2 |
| 2015 | -3.6 | -0.8 |
| 2016 (OOS) | 2.8 | 0.2 |
| 2017 (OOS) | 3.8 | 0.3 |
| 2018 (OOS) | -2.4 | -0.2 |
| 2019 (OOS) | 7.9 | -1.2 |
| 2020 (OOS) | 7.7 | -0.5 |
| 2021 (OOS) | 2.5 | -0.0 |
| 2022 (OOS) | -2.8 | -0.6 |
| 2023 (OOS) | 13.2 | 1.7 |
| 2024 (OOS) | 0.7 | -2.0 |
| 2025 (OOS) | 1.8 | 2.1 |
| 2026 (OOS) | 5.6 | 2.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 11.6% from a peak in-sample and 8.4% out-of-sample, and the worst single trade cost 8.8% of the account out-of-sample. About 37 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 86% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 3.4% from a peak in-sample and 5.5% out-of-sample, and the worst single trade cost 18.3% of the account out-of-sample. About 48 of every 100 trades won in-sample. Out-of-sample it earned 0.0% a year against 0.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 412 | `{"k": 1.5, "max_candles": 40, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 943.80 | 0.4 | -11.7 | 36.6 | 4,177.23 | 3.3 | -8.6 | 7.58 | 4824/4447 | not checked |
| 414 | `{"k": 1.5, "max_candles": 44, "stop_atr": 1.75, "take_profit_atr": 6.5}` | 921.04 | 0.4 | -11.6 | 36.7 | 3,970.48 | 3.1 | -8.4 | 7.43 | 4806/4431 | 1.00 |
| 532 | `{"k": 1.5, "max_candles": 40, "stop_atr": 1.75, "take_profit_atr": 7.0}` | 914.09 | 0.4 | -11.4 | 36.6 | 4,193.54 | 3.3 | -8.5 | 7.79 | 4783/4410 | not checked |
| 503 | `{"k": 1.5, "max_candles": 40, "stop_atr": 2.25, "take_profit_atr": 7.0}` | 833.36 | 0.4 | -11.3 | 37.7 | 4,351.84 | 3.4 | -7.2 | 8.87 | 4695/4324 | not checked |
| 523 | `{"k": 1.5, "max_candles": 44, "stop_atr": 2.25, "take_profit_atr": 7.0}` | 814.29 | 0.4 | -11.2 | 37.8 | 4,136.31 | 3.2 | -7.2 | 8.73 | 4673/4304 | not checked |
| 538 | `{"k": 1.5, "max_candles": 44, "stop_atr": 2.5, "take_profit_atr": 7.0}` | 808.85 | 0.4 | -11.1 | 38.0 | 4,055.12 | 3.2 | -7.3 | 8.60 | 4662/4291 | not checked |
| 81 | `{"k": 1.25, "max_candles": 44, "stop_atr": 1.5, "take_profit_atr": 6.0}` | 785.79 | 0.4 | -11.0 | 35.3 | 3,904.51 | 3.1 | -7.2 | 8.53 | 5703/5147 | not checked |
| 539 | `{"k": 1.75, "max_candles": 40, "stop_atr": 1.75, "take_profit_atr": 7.0}` | 710.72 | 0.3 | -10.5 | 36.8 | 3,072.51 | 2.5 | -6.6 | 7.54 | 4083/3850 | not checked |
| 390 | `{"k": 1.5, "max_candles": 44, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 630.03 | 0.3 | -10.5 | 36.7 | 3,560.43 | 2.8 | -6.7 | 9.79 | 5226/4810 | not checked |
| 300 | `{"k": 1.5, "max_candles": 80, "stop_atr": 2.25, "take_profit_atr": 4.0}` | 552.47 | 0.3 | -10.4 | 37.9 | 3,700.82 | 2.9 | -5.7 | 11.27 | 5117/4711 | not checked |
| 309 | `{"k": 1.5, "max_candles": 48, "stop_atr": 2.25, "take_profit_atr": 4.0}` | 552.47 | 0.3 | -10.4 | 37.9 | 3,716.70 | 3.0 | -5.7 | 11.35 | 5117/4713 | not checked |
| 372 | `{"k": 1.5, "max_candles": 52, "stop_atr": 2.25, "take_profit_atr": 4.0}` | 552.47 | 0.3 | -10.4 | 37.9 | 3,725.94 | 3.0 | -5.7 | 11.35 | 5117/4711 | not checked |
| 401 | `{"k": 1.5, "max_candles": 76, "stop_atr": 2.25, "take_profit_atr": 4.0}` | 552.47 | 0.3 | -10.4 | 37.9 | 3,700.82 | 2.9 | -5.7 | 11.27 | 5117/4711 | not checked |
| 589 | `{"k": 1.75, "max_candles": 40, "stop_atr": 1.5, "take_profit_atr": 7.0}` | 527.91 | 0.2 | -10.0 | 35.3 | 3,058.03 | 2.5 | -6.6 | 9.92 | 4198/3970 | not checked |
| 363 | `{"k": 2.0, "max_candles": 64, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 523.95 | 0.2 | -8.5 | 38.7 | 2,222.87 | 1.9 | -7.0 | 7.75 | 3359/3296 | not checked |
| 741 | `{"k": 2.0, "max_candles": 40, "stop_atr": 2.25, "take_profit_atr": 7.0}` | 497.44 | 0.2 | -8.0 | 37.6 | 1,966.40 | 1.7 | -6.6 | 7.22 | 3286/3259 | not checked |
| 755 | `{"k": 3.25, "max_candles": 44, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 224.83 | 0.1 | -3.6 | 39.6 | 142.15 | 0.1 | -7.7 | 1.18 | 747/951 | not checked |
| 139 | `{"k": 3.0, "max_candles": 68, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 52.61 | 0.0 | -3.4 | 47.8 | 10.93 | 0.0 | -5.5 | 0.50 | 1316/1629 | not checked |
| 140 | `{"k": 3.0, "max_candles": 76, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 52.61 | 0.0 | -3.4 | 47.8 | 10.93 | 0.0 | -5.5 | 0.50 | 1316/1629 | not checked |
| 141 | `{"k": 3.0, "max_candles": 72, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 52.61 | 0.0 | -3.4 | 47.8 | 10.93 | 0.0 | -5.5 | 0.50 | 1316/1629 | 0.71 |
| 766 | `{"k": 3.0, "max_candles": 64, "stop_atr": 2.25, "take_profit_atr": 2.5}` | 52.61 | 0.0 | -3.4 | 47.8 | 10.93 | 0.0 | -5.5 | 0.50 | 1316/1629 | not checked |
| 716 | `{"k": 3.0, "max_candles": 72, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 10.84 | 0.0 | -3.2 | 43.0 | 54.61 | 0.1 | -4.9 | 5.00 | 1336/1654 | not checked |
| 773 | `{"k": 3.0, "max_candles": 68, "stop_atr": 1.75, "take_profit_atr": 2.5}` | 10.84 | 0.0 | -3.2 | 43.0 | 54.61 | 0.1 | -4.9 | 5.00 | 1336/1654 | not checked |
| 655 | `{"k": 3.5, "max_candles": 72, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 3.64 | 0.0 | -2.1 | 37.5 | 125.22 | 0.1 | -4.9 | n/a | 498/691 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 775 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
