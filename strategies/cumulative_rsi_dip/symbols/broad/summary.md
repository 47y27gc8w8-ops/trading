# cumulative_rsi_dip__broad: optimization summary

Updated 2026-11-25T13:38:03Z · backtest.py version `6d8d9a1bae` · 800 parameter sets tested with this version (800 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [cumulative_rsi_dip__broad__max-income__v001.md](cumulative_rsi_dip__broad__max-income__v001.md) | 299 | `{"max_bars": 24, "n": 2, "stop_atr": 4.0, "take_profit_atr": 4.5, "threshold": 38}` | long DIA since 2026-11-18 00:00 @ 505.129066; long RSP since 2026-11-18 00:00 @ 215.284567; long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-19 00:00 @ 61.728512; long XLV since 2026-11-19 00:00 @ 180.454114; long XLP since 2026-11-20 00:00 @ 90.957279; long XLB since 2026-11-17 00:00 @ 51.335396; long DBC since 2026-11-18 00:00 @ 29.858955; long VIG since 2026-11-18 00:00 @ 245.57365; long SCHD since 2026-11-19 00:00 @ 34.690404; long USMV since 2026-11-18 00:00 @ 101.720509; long VNQ since 2026-11-18 00:00 @ 94.208254; long VTV since 2026-11-18 00:00 @ 222.906848; long CSSMI.SW since 2026-11-19 00:00 @ 154.406309; long VWRL.SW since 2026-11-18 00:00 @ 149.184741; long IWDA.AS since 2026-11-19 00:00 @ 128.378498 |
| balanced | [cumulative_rsi_dip__broad__balanced__v001.md](cumulative_rsi_dip__broad__balanced__v001.md) | 300 | `{"max_bars": 12, "n": 2, "stop_atr": 2.5, "take_profit_atr": 3.0, "threshold": 30}` | long XLF since 2026-11-19 00:00 @ 56.526951; long XLE since 2026-11-20 00:00 @ 60.728212; long XLV since 2026-11-19 00:00 @ 180.454114; long XLP since 2026-11-20 00:00 @ 90.957279; long SCHD since 2026-11-19 00:00 @ 34.690404; long VNQ since 2026-11-18 00:00 @ 94.208254; long CSSMI.SW since 2026-11-20 00:00 @ 152.385698 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 2,823.95 | 1,329.77 | 2,148.71 | 539.24 |
| return % | 28.24 | 13.30 | 21.49 | 5.39 |
| return %/year | 1.2 | 1.1 | 0.9 | 0.5 |
| gross profit | 8,571.21 | 7,762.41 | 7,052.18 | 6,040.23 |
| gross loss | 5,747.26 | 6,432.64 | 4,903.46 | 5,500.99 |
| trades | 4,562 | 4,825 | 3,788 | 3,991 |
| win rate % | 64.6 | 63.7 | 64.6 | 63.5 |
| avg win | 2.91 | 2.53 | 2.88 | 2.38 |
| avg loss | -3.56 | -3.67 | -3.66 | -3.78 |
| avg result / trade | 0.62 | 0.28 | 0.57 | 0.14 |
| largest single loss | -47.01 | -68.70 | -45.53 | -29.93 |
| largest loss % of equity | -11.69 | -17.49 | -8.99 | -17.37 |
| max drawdown | -581.56 | -913.97 | -335.53 | -655.43 |
| max drawdown % | -4.82 | -8.74 | -2.87 | -6.37 |
| profit factor | 1.49 | 1.21 | 1.44 | 1.10 |
| unusually bad trades | 391 | 525 | 456 | 417 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.7 |
| time in market % | 6.1 | 11.8 | 4.5 | 8.6 |
| buy & hold return % | 100.07 | 303.60 | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.97 |  | 0.52 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.2 | 0.1 |
| 1996 | 0.1 | 0.1 |
| 1997 | 0.1 | 0.4 |
| 1998 | 0.4 | 0.2 |
| 1999 | 0.4 | 0.1 |
| 2000 | 0.8 | 0.1 |
| 2001 | 0.6 | 0.4 |
| 2002 | -0.6 | -0.3 |
| 2003 | 3.1 | 2.8 |
| 2004 | 0.4 | 0.4 |
| 2005 | 0.4 | 0.1 |
| 2006 | 2.4 | 1.4 |
| 2007 | 2.7 | 2.7 |
| 2008 | -1.0 | -0.4 |
| 2009 | 5.1 | 4.7 |
| 2010 | 0.2 | 0.0 |
| 2011 | -0.2 | 0.6 |
| 2012 | 2.7 | 3.4 |
| 2013 | 4.8 | 3.0 |
| 2014 | 1.3 | 0.0 |
| 2015 | 1.4 | 0.1 |
| 2016 (OOS) | 2.6 | 0.9 |
| 2017 (OOS) | 3.1 | 2.1 |
| 2018 (OOS) | -7.2 | -3.6 |
| 2019 (OOS) | 0.0 | -0.4 |
| 2020 (OOS) | 2.6 | -0.3 |
| 2021 (OOS) | 9.7 | 4.9 |
| 2022 (OOS) | -2.5 | -1.7 |
| 2023 (OOS) | -0.1 | -1.1 |
| 2024 (OOS) | 4.5 | 2.6 |
| 2025 (OOS) | 4.0 | 3.5 |
| 2026 (OOS) | 1.2 | -1.6 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 4.8% from a peak in-sample and 8.7% out-of-sample, and the worst single trade cost 17.5% of the account out-of-sample. About 65 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 2.9% from a peak in-sample and 6.4% out-of-sample, and the worst single trade cost 17.4% of the account out-of-sample. About 65 of every 100 trades won in-sample. Out-of-sample it earned 0.5% a year against 0.9% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 563 | `{"max_bars": 28, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,446.74 | 1.2 | -9.1 | 1.01 | 4526/4787 | not checked |
| 564 | `{"max_bars": 18, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,446.74 | 1.2 | -9.1 | 1.01 | 4526/4787 | not checked |
| 565 | `{"max_bars": 20, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,446.74 | 1.2 | -9.1 | 1.01 | 4526/4787 | not checked |
| 566 | `{"max_bars": 26, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,446.74 | 1.2 | -9.1 | 1.01 | 4526/4787 | not checked |
| 586 | `{"max_bars": 24, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,446.74 | 1.2 | -9.1 | 1.01 | 4526/4787 | not checked |
| 597 | `{"max_bars": 22, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,446.74 | 1.2 | -9.1 | 1.01 | 4526/4787 | not checked |
| 696 | `{"max_bars": 16, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,946.59 | 1.2 | -5.7 | 64.7 | 1,441.31 | 1.2 | -9.1 | 1.00 | 4526/4787 | not checked |
| 718 | `{"max_bars": 14, "n": 2, "stop_atr": 4.75, "take_profit_atr": 6.0, "threshold": 38}` | 2,944.18 | 1.2 | -5.7 | 64.7 | 1,421.23 | 1.2 | -9.1 | 0.99 | 4526/4788 | not checked |
| 506 | `{"max_bars": 28, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,354.60 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 519 | `{"max_bars": 18, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,354.60 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 524 | `{"max_bars": 26, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,354.60 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 527 | `{"max_bars": 20, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,354.60 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 578 | `{"max_bars": 16, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,353.82 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 623 | `{"max_bars": 22, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,354.60 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 644 | `{"max_bars": 24, "n": 2, "stop_atr": 4.5, "take_profit_atr": 6.0, "threshold": 38}` | 2,882.16 | 1.2 | -5.4 | 64.7 | 1,354.60 | 1.2 | -9.4 | 0.97 | 4536/4798 | not checked |
| 443 | `{"max_bars": 28, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 38}` | 2,879.31 | 1.2 | -5.1 | 64.7 | 1,344.99 | 1.2 | -9.2 | 0.97 | 4548/4813 | not checked |
| 444 | `{"max_bars": 18, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 38}` | 2,879.31 | 1.2 | -5.1 | 64.7 | 1,344.99 | 1.2 | -9.2 | 0.97 | 4548/4813 | not checked |
| 525 | `{"max_bars": 26, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 38}` | 2,879.31 | 1.2 | -5.1 | 64.7 | 1,344.99 | 1.2 | -9.2 | 0.97 | 4548/4813 | not checked |
| 539 | `{"max_bars": 24, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 38}` | 2,879.31 | 1.2 | -5.1 | 64.7 | 1,344.99 | 1.2 | -9.2 | 0.97 | 4548/4813 | not checked |
| 689 | `{"max_bars": 20, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 38}` | 2,879.31 | 1.2 | -5.1 | 64.7 | 1,344.99 | 1.2 | -9.2 | 0.97 | 4548/4813 | not checked |
| 447 | `{"max_bars": 14, "n": 2, "stop_atr": 4.0, "take_profit_atr": 5.5, "threshold": 38}` | 2,832.28 | 1.2 | -4.8 | 64.6 | 1,290.39 | 1.1 | -8.7 | 0.93 | 4562/4826 | not checked |
| 453 | `{"max_bars": 28, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 40}` | 2,738.06 | 1.2 | -4.7 | 64.1 | 1,523.97 | 1.3 | -9.6 | 1.13 | 4779/5067 | not checked |
| 464 | `{"max_bars": 18, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 40}` | 2,738.06 | 1.2 | -4.7 | 64.1 | 1,523.97 | 1.3 | -9.6 | 1.13 | 4779/5067 | not checked |
| 487 | `{"max_bars": 20, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 40}` | 2,738.06 | 1.2 | -4.7 | 64.1 | 1,523.97 | 1.3 | -9.6 | 1.13 | 4779/5067 | not checked |
| 499 | `{"max_bars": 26, "n": 2, "stop_atr": 4.25, "take_profit_atr": 6.0, "threshold": 40}` | 2,738.06 | 1.2 | -4.7 | 64.1 | 1,523.97 | 1.3 | -9.6 | 1.13 | 4779/5067 | not checked |

(28 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 800 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
