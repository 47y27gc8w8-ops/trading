# rsi_bullish_divergence_fixed_window__broad: optimization summary

Updated 2026-11-25T10:55:18Z · backtest.py version `32e35a6a14` · 1,664 parameter sets tested with this version (1,664 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rsi_bullish_divergence_fixed_window__broad__max-income__v002.md](rsi_bullish_divergence_fixed_window__broad__max-income__v002.md) | 1663 | `{"gap": 0, "max_candles": 34, "n": 14, "stop_atr": 5.0, "take_profit_atr": 5.0}` | long SPY since 2026-11-18 00:00 @ 733.590006; long VOO since 2026-11-18 00:00 @ 674.312218; long IVV since 2026-11-18 00:00 @ 736.840981; long VTI since 2026-11-18 00:00 @ 360.778214; long XLE since 2026-11-19 00:00 @ 61.728512; long USO since 2026-11-17 00:00 @ 142.622776; long IWDA.AS since 2026-11-18 00:00 @ 128.278477 |
| balanced | [rsi_bullish_divergence_fixed_window__broad__balanced__v002.md](rsi_bullish_divergence_fixed_window__broad__balanced__v002.md) | 1664 | `{"gap": 1, "max_candles": 26, "n": 40, "stop_atr": 4.75, "take_profit_atr": 5.5}` | long SPY since 2026-11-18 00:00 @ 733.590006; long VOO since 2026-11-18 00:00 @ 674.312218; long IVV since 2026-11-18 00:00 @ 736.840981; long VTI since 2026-11-18 00:00 @ 360.778214; long DIA since 2026-11-18 00:00 @ 505.129066; long XLE since 2026-11-19 00:00 @ 61.728512; long IWDA.AS since 2026-11-18 00:00 @ 128.278477 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,503.85 | 1,430.91 | 1,618.22 | 1,235.59 |
| return % | 25.04 | 14.31 | 16.18 | 12.36 |
| return %/year | 1.4 | 1.2 | 0.9 | 1.1 |
| gross profit | 3,916.12 | 3,323.75 | 2,154.12 | 2,008.02 |
| gross loss | 1,412.28 | 1,892.84 | 535.90 | 772.43 |
| trades | 589 | 534 | 309 | 312 |
| win rate % | 75.9 | 70.0 | 74.4 | 73.1 |
| avg win | 8.76 | 8.89 | 9.37 | 8.81 |
| avg loss | -9.95 | -11.83 | -6.78 | -9.20 |
| avg result / trade | 4.25 | 2.68 | 5.24 | 3.96 |
| largest single loss | -41.71 | -158.20 | -30.13 | -108.51 |
| largest loss % of equity | -19.13 | -33.74 | -14.36 | -27.73 |
| max drawdown | -337.29 | -595.73 | -167.21 | -334.08 |
| max drawdown % | -2.74 | -5.00 | -1.60 | -2.90 |
| profit factor | 2.77 | 1.76 | 4.02 | 2.60 |
| unusually bad trades | 17 | 53 | 26 | 33 |
| … threshold (% of equity) | 8.4 | 6.1 | 4.4 | 4.2 |
| time in market % | 5.2 | 6.9 | 2.6 | 3.5 |
| buy & hold return % | 95.12 | 303.60 | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.88 |  | 1.15 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 0.6 | 0.2 |
| 2001 | 0.3 | 0.2 |
| 2002 | -0.7 | -0.7 |
| 2003 | 1.1 | 0.2 |
| 2004 | 1.3 | 0.9 |
| 2005 | 1.6 | 1.1 |
| 2006 | -0.2 | 0.2 |
| 2007 | 2.5 | 1.7 |
| 2008 | -0.6 | -0.0 |
| 2009 | 2.7 | 1.0 |
| 2010 | 3.8 | 3.4 |
| 2011 | 2.5 | 2.7 |
| 2012 | 0.0 | 0.9 |
| 2013 | 2.9 | 0.7 |
| 2014 | 2.3 | 2.1 |
| 2015 | 2.7 | 0.6 |
| 2016 (OOS) | 0.5 | 1.0 |
| 2017 (OOS) | 0.9 | 0.2 |
| 2018 (OOS) | 2.2 | 0.4 |
| 2019 (OOS) | 4.3 | 3.4 |
| 2020 (OOS) | 4.1 | -0.3 |
| 2021 (OOS) | 5.0 | 2.6 |
| 2022 (OOS) | -2.7 | 0.4 |
| 2023 (OOS) | 1.5 | 1.3 |
| 2024 (OOS) | 1.6 | 2.8 |
| 2025 (OOS) | -0.9 | 0.9 |
| 2026 (OOS) | -1.6 | -0.3 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 2.7% from a peak in-sample and 5.0% out-of-sample, and the worst single trade cost 33.7% of the account out-of-sample. About 76 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 1.6% from a peak in-sample and 2.9% out-of-sample, and the worst single trade cost 27.7% of the account out-of-sample. About 74 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1373 | `{"gap": 0, "max_candles": 34, "n": 14, "stop_atr": 5.75, "take_profit_atr": 6.0}` | 2,584.44 | 1.4 | -2.9 | 77.2 | 1,455.04 | 1.3 | -5.3 | 0.87 | 587/533 | not checked |
| 1413 | `{"gap": 0, "max_candles": 34, "n": 14, "stop_atr": 5.5, "take_profit_atr": 6.0}` | 2,528.85 | 1.4 | -2.8 | 76.7 | 1,343.29 | 1.2 | -5.3 | 0.82 | 587/534 | not checked |
| 1365 | `{"gap": 0, "max_candles": 34, "n": 14, "stop_atr": 5.25, "take_profit_atr": 6.0}` | 2,517.78 | 1.4 | -2.8 | 76.2 | 1,358.94 | 1.2 | -5.3 | 0.84 | 589/534 | not checked |
| 1434 | `{"gap": 0, "max_candles": 34, "n": 14, "stop_atr": 5.0, "take_profit_atr": 6.0}` | 2,507.97 | 1.4 | -2.7 | 75.9 | 1,436.87 | 1.2 | -5.0 | 0.88 | 589/534 | not checked |
| 1252 | `{"gap": 0, "max_candles": 34, "n": 18, "stop_atr": 5.0, "take_profit_atr": 5.5}` | 2,414.01 | 1.4 | -2.7 | 75.8 | 1,579.46 | 1.4 | -4.5 | 1.00 | 587/527 | not checked |
| 1376 | `{"gap": 0, "max_candles": 34, "n": 14, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 2,357.48 | 1.3 | -2.7 | 74.7 | 1,382.17 | 1.2 | -5.0 | 0.90 | 589/534 | not checked |
| 1307 | `{"gap": 0, "max_candles": 34, "n": 18, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 2,253.22 | 1.3 | -2.7 | 74.5 | 1,525.70 | 1.3 | -4.6 | 1.02 | 587/527 | not checked |
| 1443 | `{"gap": 1, "max_candles": 34, "n": 12, "stop_atr": 5.0, "take_profit_atr": 6.0}` | 2,185.14 | 1.2 | -1.9 | 79.9 | 1,250.34 | 1.1 | -3.2 | 0.88 | 363/342 | not checked |
| 1580 | `{"gap": 1, "max_candles": 34, "n": 10, "stop_atr": 5.0, "take_profit_atr": 6.0}` | 2,077.56 | 1.2 | -1.9 | 80.5 | 1,138.22 | 1.0 | -4.1 | 0.84 | 344/328 | not checked |
| 1280 | `{"gap": 1, "max_candles": 34, "n": 26, "stop_atr": 5.0, "take_profit_atr": 5.0}` | 1,922.52 | 1.1 | -1.9 | 78.4 | 1,201.86 | 1.1 | -3.0 | 0.95 | 371/355 | not checked |
| 1225 | `{"gap": 1, "max_candles": 34, "n": 40, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 1,723.55 | 1.0 | -1.7 | 78.6 | 1,299.39 | 1.1 | -2.9 | 1.13 | 304/305 | not checked |
| 1100 | `{"gap": 1, "max_candles": 34, "n": 38, "stop_atr": 5.25, "take_profit_atr": 6.0}` | 1,717.24 | 1.0 | -1.7 | 78.3 | 1,219.20 | 1.1 | -2.4 | 1.06 | 313/309 | not checked |
| 973 | `{"gap": 1, "max_candles": 26, "n": 40, "stop_atr": 5.25, "take_profit_atr": 6.0}` | 1,669.70 | 1.0 | -1.6 | 75.7 | 1,183.51 | 1.0 | -2.6 | 1.06 | 309/312 | not checked |
| 1218 | `{"gap": 2, "max_candles": 36, "n": 26, "stop_atr": 5.0, "take_profit_atr": 4.5}` | 1,493.47 | 0.9 | -1.6 | 79.5 | 837.49 | 0.7 | -1.8 | 0.85 | 239/252 | not checked |
| 795 | `{"gap": 1, "max_candles": 34, "n": 42, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 1,407.05 | 0.8 | -1.5 | 74.0 | 1,160.05 | 1.0 | -2.5 | 1.22 | 292/298 | not checked |
| 1588 | `{"gap": 2, "max_candles": 36, "n": 10, "stop_atr": 5.0, "take_profit_atr": 6.0}` | 1,380.35 | 0.8 | -1.5 | 80.4 | 648.34 | 0.6 | -2.5 | 0.72 | 199/200 | not checked |
| 657 | `{"gap": 1, "max_candles": 26, "n": 42, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 1,296.89 | 0.8 | -1.5 | 70.8 | 1,091.17 | 1.0 | -2.2 | 1.25 | 298/304 | not checked |
| 559 | `{"gap": 1, "max_candles": 20, "n": 42, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 1,226.81 | 0.7 | -1.5 | 71.3 | 1,116.61 | 1.0 | -2.3 | 1.34 | 300/310 | not checked |
| 627 | `{"gap": 1, "max_candles": 26, "n": 48, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 1,078.50 | 0.6 | -1.4 | 72.7 | 972.50 | 0.9 | -2.4 | 1.34 | 245/261 | not checked |
| 565 | `{"gap": 2, "max_candles": 26, "n": 44, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 899.61 | 0.5 | -1.4 | 68.5 | 726.13 | 0.7 | -1.3 | 1.20 | 200/226 | not checked |
| 637 | `{"gap": 1, "max_candles": 26, "n": 50, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 861.96 | 0.5 | -1.4 | 67.8 | 934.70 | 0.8 | -2.0 | 1.58 | 239/241 | not checked |
| 1631 | `{"gap": 3, "max_candles": 38, "n": 30, "stop_atr": 4.25, "take_profit_atr": 5.0}` | 851.20 | 0.5 | -1.2 | 78.2 | 688.53 | 0.6 | -1.3 | 1.20 | 147/174 | not checked |
| 1067 | `{"gap": 3, "max_candles": 24, "n": 40, "stop_atr": 4.5, "take_profit_atr": 5.5}` | 753.70 | 0.5 | -1.2 | 71.6 | 692.59 | 0.6 | -1.2 | 1.35 | 148/172 | not checked |
| 635 | `{"gap": 3, "max_candles": 26, "n": 42, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 752.01 | 0.5 | -1.1 | 74.0 | 563.10 | 0.5 | -1.1 | 1.11 | 146/167 | not checked |
| 639 | `{"gap": 3, "max_candles": 20, "n": 50, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 583.12 | 0.4 | -0.9 | 71.8 | 519.21 | 0.5 | -1.0 | 1.31 | 131/128 | not checked |

(11 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,664 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
