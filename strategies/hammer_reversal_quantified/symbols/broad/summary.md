# hammer_reversal_quantified__broad: optimization summary

Updated 2026-11-26T02:24:57Z · backtest.py version `afbd7797ed` · 750 parameter sets tested with this version (750 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [hammer_reversal_quantified__broad__max-income__v001.md](hammer_reversal_quantified__broad__max-income__v001.md) | 235 | `{"max_candles": 52, "ratio": 2.25, "stop_atr": 3.75, "take_profit_atr": 2.0}` | flat (data up to 2026-11-25 00:00) |
| balanced | [hammer_reversal_quantified__broad__balanced__v002.md](hammer_reversal_quantified__broad__balanced__v002.md) | 750 | `{"max_candles": 32, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 1.0}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 461.54 | 113.77 | 366.95 | 85.39 |
| return % | 4.62 | 1.14 | 3.67 | 0.85 |
| return %/year | 0.2 | 0.1 | 0.2 | 0.1 |
| gross profit | 1,148.03 | 913.15 | 961.33 | 800.96 |
| gross loss | 686.50 | 799.38 | 594.39 | 715.58 |
| trades | 616 | 595 | 621 | 599 |
| win rate % | 70.5 | 69.2 | 73.4 | 71.8 |
| avg win | 2.65 | 2.22 | 2.11 | 1.86 |
| avg loss | -3.77 | -4.37 | -3.60 | -4.23 |
| avg result / trade | 0.75 | 0.19 | 0.59 | 0.14 |
| largest single loss | -23.88 | -43.13 | -14.62 | -43.13 |
| largest loss % of equity | -10.68 | -28.04 | -7.86 | -28.04 |
| max drawdown | -129.53 | -153.00 | -55.31 | -133.95 |
| max drawdown % | -1.25 | -1.49 | -0.55 | -1.33 |
| profit factor | 1.67 | 1.14 | 1.62 | 1.12 |
| unusually bad trades | 54 | 78 | 36 | 26 |
| … threshold (% of equity) | 2.8 | 2.3 | 3.7 | 4.5 |
| time in market % | 0.8 | 1.4 | 0.5 | 1.0 |
| buy & hold return % | 119.84 | 280.02 | 119.84 | 280.02 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.46 |  | 0.47 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.2 | 0.1 |
| 1996 | -0.1 | -0.1 |
| 1997 | 0.2 | 0.1 |
| 1998 | 0.1 | 0.1 |
| 1999 | 0.3 | 0.1 |
| 2000 | 0.3 | 0.2 |
| 2001 | 0.2 | 0.3 |
| 2002 | -0.0 | -0.1 |
| 2003 | 0.5 | 0.4 |
| 2004 | -0.1 | -0.3 |
| 2005 | 0.1 | 0.1 |
| 2006 | 0.1 | 0.1 |
| 2007 | -0.1 | 0.2 |
| 2008 | -0.2 | -0.1 |
| 2009 | 0.6 | 0.5 |
| 2010 | 0.7 | 0.7 |
| 2011 | 0.5 | 0.3 |
| 2012 | -0.3 | 0.1 |
| 2013 | 0.6 | 0.4 |
| 2014 | -0.1 | -0.0 |
| 2015 | 0.9 | 0.5 |
| 2016 (OOS) | 0.0 | -0.0 |
| 2017 (OOS) | 0.4 | 0.3 |
| 2018 (OOS) | -0.0 | -0.1 |
| 2019 (OOS) | 0.4 | 0.2 |
| 2020 (OOS) | -0.7 | -0.6 |
| 2021 (OOS) | 1.3 | 1.0 |
| 2022 (OOS) | -0.6 | -0.0 |
| 2023 (OOS) | 0.2 | -0.2 |
| 2024 (OOS) | 0.7 | 0.6 |
| 2025 (OOS) | -0.6 | -0.3 |
| 2026 (OOS) | -0.1 | 0.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 1.2% from a peak in-sample and 1.5% out-of-sample, and the worst single trade cost 28.0% of the account out-of-sample. About 70 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.6% from a peak in-sample and 1.3% out-of-sample, and the worst single trade cost 28.0% of the account out-of-sample. About 73 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 228 | `{"max_candles": 52, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 382 | `{"max_candles": 56, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 492 | `{"max_candles": 48, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 522 | `{"max_candles": 44, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 599 | `{"max_candles": 60, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 621 | `{"max_candles": 64, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 673 | `{"max_candles": 68, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 679 | `{"max_candles": 72, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 698 | `{"max_candles": 76, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 719 | `{"max_candles": 40, "ratio": 2.25, "stop_atr": 3.5, "take_profit_atr": 2.0}` | 466.42 | 0.2 | -1.2 | 70.5 | 140.73 | 0.1 | -1.4 | 0.59 | 617/596 | not checked |
| 49 | `{"max_candles": 36, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | 1.00 |
| 59 | `{"max_candles": 32, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 60 | `{"max_candles": 40, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 293 | `{"max_candles": 28, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 337 | `{"max_candles": 48, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 397 | `{"max_candles": 52, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 416 | `{"max_candles": 44, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 419 | `{"max_candles": 56, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 425 | `{"max_candles": 24, "ratio": 2.25, "stop_atr": 2.75, "take_profit_atr": 2.0}` | 426.07 | 0.2 | -1.1 | 69.8 | 93.83 | 0.1 | -1.2 | 0.45 | 620/596 | not checked |
| 56 | `{"max_candles": 36, "ratio": 2.25, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 400.18 | 0.2 | -1.0 | 69.2 | 116.55 | 0.1 | -1.2 | 0.58 | 621/596 | not checked |
| 307 | `{"max_candles": 44, "ratio": 2.25, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 400.18 | 0.2 | -1.0 | 69.2 | 116.55 | 0.1 | -1.2 | 0.58 | 621/596 | not checked |
| 312 | `{"max_candles": 32, "ratio": 2.25, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 400.18 | 0.2 | -1.0 | 69.2 | 116.55 | 0.1 | -1.2 | 0.58 | 621/596 | not checked |
| 437 | `{"max_candles": 56, "ratio": 2.25, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 400.18 | 0.2 | -1.0 | 69.2 | 116.55 | 0.1 | -1.2 | 0.58 | 621/596 | not checked |
| 478 | `{"max_candles": 48, "ratio": 2.25, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 400.18 | 0.2 | -1.0 | 69.2 | 116.55 | 0.1 | -1.2 | 0.58 | 621/596 | not checked |
| 484 | `{"max_candles": 52, "ratio": 2.25, "stop_atr": 2.5, "take_profit_atr": 2.0}` | 400.18 | 0.2 | -1.0 | 69.2 | 116.55 | 0.1 | -1.2 | 0.58 | 621/596 | not checked |

(18 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 750 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
