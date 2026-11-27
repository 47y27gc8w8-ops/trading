# williams_r_recovery__broad: optimization summary

Updated 2026-11-25T23:37:47Z · backtest.py version `43bffb3ba4` · 1,289 parameter sets tested with this version (1,289 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [williams_r_recovery__broad__max-income__v002.md](williams_r_recovery__broad__max-income__v002.md) | 1288 | `{"level": -89, "max_candles": 20, "n": 7, "stop_atr": 4.0, "take_profit_atr": 4.5}` | long RSP since 2026-11-24 00:00 @ 211.85353; long XLF since 2026-11-24 00:00 @ 55.526651; long XLE since 2026-11-25 00:00 @ 59.997994; long XLV since 2026-11-24 00:00 @ 179.703889; long XLY since 2026-11-19 00:00 @ 119.625873; long USO since 2026-11-04 00:00 @ 153.265967; long VIG since 2026-11-24 00:00 @ 239.451819; long SCHD since 2026-11-24 00:00 @ 34.38031; long USMV since 2026-11-24 00:00 @ 99.879953; long VNQ since 2026-11-19 00:00 @ 94.828443; long VTV since 2026-11-24 00:00 @ 217.875341; long CSSMI.SW since 2026-11-24 00:00 @ 152.985884; long VWRL.SW since 2026-11-24 00:00 @ 146.323883; long IWDA.AS since 2026-11-24 00:00 @ 126.707999 |
| balanced | [williams_r_recovery__broad__balanced__v002.md](williams_r_recovery__broad__balanced__v002.md) | 1289 | `{"level": -88, "max_candles": 24, "n": 7, "stop_atr": 3.5, "take_profit_atr": 5.0}` | long RSP since 2026-11-24 00:00 @ 211.85353; long XLF since 2026-11-24 00:00 @ 55.526651; long XLE since 2026-11-25 00:00 @ 59.997994; long XLV since 2026-11-24 00:00 @ 179.703889; long XLY since 2026-11-19 00:00 @ 119.625873; long USO since 2026-11-25 00:00 @ 137.821333; long VIG since 2026-11-24 00:00 @ 239.451819; long SCHD since 2026-11-24 00:00 @ 34.38031; long USMV since 2026-11-24 00:00 @ 99.879953; long VNQ since 2026-11-19 00:00 @ 94.828443; long VTV since 2026-11-24 00:00 @ 217.875341; long CSSMI.SW since 2026-11-24 00:00 @ 152.985884; long VWRL.SW since 2026-11-24 00:00 @ 146.323883; long IWDA.AS since 2026-11-24 00:00 @ 126.707999 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 3,730.88 | 2,071.56 | 3,568.31 | 1,368.98 |
| return % | 37.31 | 20.72 | 35.68 | 13.69 |
| return %/year | 2.0 | 1.7 | 1.9 | 1.2 |
| gross profit | 9,408.92 | 9,149.92 | 9,570.96 | 9,098.45 |
| gross loss | 5,678.04 | 7,078.36 | 6,002.65 | 7,729.48 |
| trades | 3,621 | 3,769 | 3,829 | 4,002 |
| win rate % | 71.0 | 68.9 | 70.6 | 67.7 |
| avg win | 3.66 | 3.52 | 3.54 | 3.36 |
| avg loss | -5.41 | -6.04 | -5.33 | -5.99 |
| avg result / trade | 1.03 | 0.55 | 0.93 | 0.34 |
| largest single loss | -52.90 | -91.39 | -45.76 | -94.31 |
| largest loss % of equity | -13.16 | -37.66 | -11.53 | -37.66 |
| max drawdown | -494.69 | -505.76 | -450.36 | -490.82 |
| max drawdown % | -4.11 | -4.35 | -3.75 | -4.40 |
| profit factor | 1.66 | 1.29 | 1.59 | 1.18 |
| unusually bad trades | 370 | 427 | 409 | 361 |
| … threshold (% of equity) | 2.3 | 3.1 | 2.5 | 4.0 |
| time in market % | 10.1 | 14.6 | 10.3 | 14.8 |
| buy & hold return % | 95.12 | 303.60 | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.87 |  | 0.62 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 1.2 | 1.0 |
| 2001 | -0.8 | -0.6 |
| 2002 | -0.7 | -1.1 |
| 2003 | 4.8 | 4.6 |
| 2004 | 0.8 | 0.6 |
| 2005 | 0.7 | 0.1 |
| 2006 | 1.6 | 1.7 |
| 2007 | 2.6 | 2.6 |
| 2008 | -0.4 | -0.5 |
| 2009 | 7.7 | 7.2 |
| 2010 | -1.8 | -1.7 |
| 2011 | 0.6 | 1.0 |
| 2012 | 3.5 | 4.1 |
| 2013 | 6.9 | 6.8 |
| 2014 | 1.9 | 1.9 |
| 2015 | 3.9 | 3.7 |
| 2016 (OOS) | 4.0 | 3.9 |
| 2017 (OOS) | 3.7 | 3.6 |
| 2018 (OOS) | -3.1 | -4.1 |
| 2019 (OOS) | 4.7 | 4.9 |
| 2020 (OOS) | 2.1 | 0.1 |
| 2021 (OOS) | 4.0 | 2.2 |
| 2022 (OOS) | -3.8 | -3.4 |
| 2023 (OOS) | 1.3 | 1.7 |
| 2024 (OOS) | 2.8 | 1.9 |
| 2025 (OOS) | 3.8 | 3.4 |
| 2026 (OOS) | 0.7 | -0.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.1% from a peak in-sample and 4.3% out-of-sample, and the worst single trade cost 37.7% of the account out-of-sample. About 71 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.8% from a peak in-sample and 4.4% out-of-sample, and the worst single trade cost 37.7% of the account out-of-sample. About 71 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 907 | `{"level": -89, "max_candles": 22, "n": 7, "stop_atr": 4.75, "take_profit_atr": 5.0}` | 3,825.21 | 2.0 | -4.7 | 71.2 | 2,192.54 | 1.8 | -5.7 | 0.90 | 3564/3680 | not checked |
| 1016 | `{"level": -89, "max_candles": 22, "n": 7, "stop_atr": 4.5, "take_profit_atr": 5.0}` | 3,789.74 | 2.0 | -4.5 | 71.0 | 2,201.60 | 1.8 | -5.7 | 0.91 | 3578/3701 | not checked |
| 709 | `{"level": -89, "max_candles": 22, "n": 7, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 3,750.27 | 2.0 | -4.1 | 71.0 | 2,047.17 | 1.7 | -4.6 | 0.86 | 3621/3765 | not checked |
| 707 | `{"level": -89, "max_candles": 22, "n": 7, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 3,673.40 | 2.0 | -4.1 | 71.0 | 2,007.38 | 1.7 | -4.6 | 0.85 | 3619/3762 | not checked |
| 821 | `{"level": -89, "max_candles": 20, "n": 7, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 3,662.22 | 2.0 | -3.8 | 70.7 | 1,878.37 | 1.6 | -4.0 | 0.81 | 3652/3802 | not checked |
| 699 | `{"level": -89, "max_candles": 24, "n": 7, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 3,660.72 | 2.0 | -3.8 | 70.7 | 1,860.82 | 1.6 | -4.2 | 0.80 | 3650/3798 | not checked |
| 720 | `{"level": -89, "max_candles": 24, "n": 7, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 3,641.47 | 2.0 | -3.6 | 70.6 | 1,495.00 | 1.3 | -4.2 | 0.66 | 3684/3845 | not checked |
| 848 | `{"level": -89, "max_candles": 22, "n": 7, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 3,639.88 | 2.0 | -3.6 | 70.6 | 1,500.72 | 1.3 | -4.2 | 0.66 | 3686/3846 | not checked |
| 911 | `{"level": -89, "max_candles": 24, "n": 7, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 3,412.54 | 1.9 | -3.6 | 70.3 | 1,326.21 | 1.1 | -4.4 | 0.62 | 3727/3903 | not checked |
| 782 | `{"level": -88, "max_candles": 24, "n": 7, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 3,390.43 | 1.8 | -3.4 | 70.3 | 1,190.48 | 1.0 | -4.4 | 0.56 | 3879/4066 | not checked |
| 682 | `{"level": -88, "max_candles": 16, "n": 7, "stop_atr": 3.25, "take_profit_atr": 5.0}` | 3,359.92 | 1.8 | -3.4 | 70.1 | 1,080.04 | 0.9 | -5.0 | 0.52 | 3885/4076 | not checked |
| 695 | `{"level": -88, "max_candles": 22, "n": 7, "stop_atr": 2.75, "take_profit_atr": 4.5}` | 2,818.28 | 1.6 | -3.3 | 68.8 | 1,251.60 | 1.1 | -4.1 | 0.70 | 4007/4238 | not checked |
| 705 | `{"level": -89, "max_candles": 24, "n": 6, "stop_atr": 2.75, "take_profit_atr": 4.5}` | 2,730.77 | 1.5 | -3.1 | 67.9 | 1,752.97 | 1.5 | -4.5 | 0.98 | 4198/4388 | not checked |
| 683 | `{"level": -89, "max_candles": 22, "n": 6, "stop_atr": 2.75, "take_profit_atr": 4.5}` | 2,714.29 | 1.5 | -3.1 | 67.9 | 1,767.69 | 1.5 | -4.5 | 1.00 | 4199/4388 | not checked |
| 655 | `{"level": -93, "max_candles": 14, "n": 27, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 1,416.73 | 0.8 | -2.9 | 53.1 | 1,467.12 | 1.3 | -5.0 | 1.53 | 1334/1341 | not checked |
| 182 | `{"level": -94, "max_candles": 14, "n": 27, "stop_atr": 2.0, "take_profit_atr": 4.5}` | 1,381.81 | 0.8 | -2.6 | 52.9 | 1,289.91 | 1.1 | -5.1 | 1.38 | 1224/1226 | not checked |
| 187 | `{"level": -94, "max_candles": 14, "n": 28, "stop_atr": 2.0, "take_profit_atr": 5.0}` | 1,369.62 | 0.8 | -2.6 | 53.2 | 1,429.53 | 1.2 | -4.9 | 1.53 | 1183/1181 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,289 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
