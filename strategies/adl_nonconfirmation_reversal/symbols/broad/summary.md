# adl_nonconfirmation_reversal__broad: optimization summary

Updated 2026-11-25T06:09:10Z · backtest.py version `cdafece0cc` · 802 parameter sets tested with this version (802 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [adl_nonconfirmation_reversal__broad__max-income__v002.md](adl_nonconfirmation_reversal__broad__max-income__v002.md) | 802 | `{"max_candles": 72, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.0}` | long DBC since 2026-11-23 00:00 @ 29.50885 |
| balanced | [adl_nonconfirmation_reversal__broad__balanced__v001.md](adl_nonconfirmation_reversal__broad__balanced__v001.md) | 272 | `{"max_candles": 72, "n": 28, "stop_atr": 1.5, "take_profit_atr": 4.0}` | long DBC since 2026-11-23 00:00 @ 29.50885 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 315.34 | 142.35 | 281.65 | 391.61 |
| return % | 3.15 | 1.42 | 2.82 | 3.92 |
| return %/year | 0.2 | 0.1 | 0.2 | 0.3 |
| gross profit | 2,497.18 | 2,688.93 | 2,330.47 | 2,633.44 |
| gross loss | 2,181.84 | 2,546.58 | 2,048.82 | 2,241.83 |
| trades | 615 | 791 | 590 | 728 |
| win rate % | 50.7 | 51.2 | 45.9 | 48.4 |
| avg win | 8.00 | 6.64 | 8.60 | 7.48 |
| avg loss | -7.20 | -6.60 | -6.42 | -5.96 |
| avg result / trade | 0.51 | 0.18 | 0.48 | 0.54 |
| largest single loss | -29.71 | -56.09 | -27.48 | -56.93 |
| largest loss % of equity | -14.56 | -18.99 | -14.56 | -27.12 |
| max drawdown | -520.13 | -653.32 | -432.53 | -574.37 |
| max drawdown % | -5.16 | -6.26 | -4.29 | -5.52 |
| profit factor | 1.15 | 1.06 | 1.14 | 1.18 |
| unusually bad trades | 34 | 53 | 42 | 57 |
| … threshold (% of equity) | 6.4 | 5.6 | 5.5 | 5.0 |
| time in market % | 2.1 | 3.4 | 1.8 | 3.0 |
| buy & hold return % | 95.12 | 303.60 | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.68 |  | 2.06 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | -0.1 | -0.2 |
| 2001 | 0.8 | 1.0 |
| 2002 | -2.3 | -2.3 |
| 2003 | 0.3 | 0.2 |
| 2004 | 0.0 | 0.1 |
| 2005 | 0.2 | 0.2 |
| 2006 | -0.8 | -0.7 |
| 2007 | 0.1 | 0.3 |
| 2008 | -1.1 | -0.9 |
| 2009 | 0.4 | 0.7 |
| 2010 | 1.7 | 1.6 |
| 2011 | 2.1 | 1.1 |
| 2012 | -0.6 | -0.3 |
| 2013 | 0.3 | 0.2 |
| 2014 | 2.3 | 1.9 |
| 2015 | -0.1 | 0.1 |
| 2016 (OOS) | 1.4 | 1.4 |
| 2017 (OOS) | 0.8 | 0.4 |
| 2018 (OOS) | 0.1 | 0.1 |
| 2019 (OOS) | 0.7 | 0.9 |
| 2020 (OOS) | -2.9 | -2.5 |
| 2021 (OOS) | 1.3 | 1.1 |
| 2022 (OOS) | -2.2 | -0.8 |
| 2023 (OOS) | 1.6 | 2.0 |
| 2024 (OOS) | 2.0 | 2.1 |
| 2025 (OOS) | 0.2 | 0.5 |
| 2026 (OOS) | -1.0 | -0.5 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.2% from a peak in-sample and 6.3% out-of-sample, and the worst single trade cost 19.0% of the account out-of-sample. About 51 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.3% from a peak in-sample and 5.5% out-of-sample, and the worst single trade cost 27.1% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 398 | `{"max_candles": 72, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 414 | `{"max_candles": 76, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 494 | `{"max_candles": 68, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 545 | `{"max_candles": 80, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 564 | `{"max_candles": 84, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 578 | `{"max_candles": 88, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 587 | `{"max_candles": 92, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 625 | `{"max_candles": 64, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 659 | `{"max_candles": 96, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 689 | `{"max_candles": 60, "n": 26, "stop_atr": 1.75, "take_profit_atr": 5.25}` | 317.38 | 0.2 | -5.2 | 50.7 | 147.48 | 0.1 | -6.2 | 0.65 | 615/791 | not checked |
| 434 | `{"max_candles": 72, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 438 | `{"max_candles": 68, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 475 | `{"max_candles": 76, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 478 | `{"max_candles": 80, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 537 | `{"max_candles": 84, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 549 | `{"max_candles": 64, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 597 | `{"max_candles": 96, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 604 | `{"max_candles": 92, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 655 | `{"max_candles": 88, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 671 | `{"max_candles": 60, "n": 26, "stop_atr": 1.5, "take_profit_atr": 5.25}` | 282.14 | 0.2 | -4.2 | 45.9 | 280.28 | 0.2 | -6.0 | 1.47 | 621/804 | not checked |
| 456 | `{"max_candles": 76, "n": 26, "stop_atr": 1.25, "take_profit_atr": 5.25}` | 241.15 | 0.1 | -3.4 | 40.1 | 187.05 | 0.2 | -6.0 | 1.13 | 626/821 | not checked |
| 497 | `{"max_candles": 72, "n": 26, "stop_atr": 1.25, "take_profit_atr": 5.25}` | 241.15 | 0.1 | -3.4 | 40.1 | 187.05 | 0.2 | -6.0 | 1.13 | 626/821 | not checked |
| 540 | `{"max_candles": 88, "n": 26, "stop_atr": 1.25, "take_profit_atr": 5.25}` | 241.15 | 0.1 | -3.4 | 40.1 | 187.05 | 0.2 | -6.0 | 1.13 | 626/821 | not checked |
| 568 | `{"max_candles": 68, "n": 26, "stop_atr": 1.25, "take_profit_atr": 5.25}` | 241.15 | 0.1 | -3.4 | 40.1 | 187.05 | 0.2 | -6.0 | 1.13 | 626/821 | not checked |
| 471 | `{"max_candles": 44, "n": 58, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 204.09 | 0.1 | -2.2 | 38.5 | 426.89 | 0.4 | -1.2 | 2.92 | 366/433 | not checked |

(1 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 802 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
