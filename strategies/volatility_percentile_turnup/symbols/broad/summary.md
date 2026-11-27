# volatility_percentile_turnup__broad: optimization summary

Updated 2026-11-25T06:02:46Z · backtest.py version `d7b311e4b8` · 757 parameter sets tested with this version (757 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [volatility_percentile_turnup__broad__max-income__v001.md](volatility_percentile_turnup__broad__max-income__v001.md) | 237 | `{"max_candles": 36, "n": 90, "stop_atr": 3.75, "take_profit_atr": 6.0}` | flat (data up to 2026-11-24 00:00) |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 659.20 | 519.73 |
| return % | 6.59 | 5.20 |
| return %/year | 0.4 | 0.5 |
| gross profit | 4,085.00 | 4,345.03 |
| gross loss | 3,425.80 | 3,825.30 |
| trades | 1,455 | 1,650 |
| win rate % | 38.4 | 37.9 |
| avg win | 7.32 | 6.94 |
| avg loss | -3.82 | -3.74 |
| avg result / trade | 0.45 | 0.31 |
| largest single loss | -27.45 | -44.01 |
| largest loss % of equity | -8.26 | -15.51 |
| max drawdown | -575.49 | -698.03 |
| max drawdown % | -5.58 | -6.64 |
| profit factor | 1.19 | 1.14 |
| unusually bad trades | 133 | 170 |
| … threshold (% of equity) | 3.3 | 3.1 |
| time in market % | 9.7 | 15.6 |
| buy & hold return % | 92.38 | 306.09 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.18 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 2000 | 0.1 |
| 2001 | -1.5 |
| 2002 | -1.3 |
| 2003 | 0.3 |
| 2004 | -0.1 |
| 2005 | 0.1 |
| 2006 | 0.7 |
| 2007 | -0.8 |
| 2008 | -1.0 |
| 2009 | 2.4 |
| 2010 | 3.1 |
| 2011 | 0.7 |
| 2012 | 5.3 |
| 2013 | 0.3 |
| 2014 | 1.1 |
| 2015 | -2.8 |
| 2016 (OOS) | -2.1 |
| 2017 (OOS) | 2.6 |
| 2018 (OOS) | -1.6 |
| 2019 (OOS) | 0.7 |
| 2020 (OOS) | 1.7 |
| 2021 (OOS) | -0.8 |
| 2022 (OOS) | -2.7 |
| 2023 (OOS) | 4.1 |
| 2024 (OOS) | -0.6 |
| 2025 (OOS) | 1.6 |
| 2026 (OOS) | 2.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.6% from a peak in-sample and 6.6% out-of-sample, and the worst single trade cost 15.5% of the account out-of-sample. About 38 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 119 | `{"max_candles": 36, "n": 90, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 659.71 | 0.4 | -5.6 | 38.4 | 511.74 | 0.5 | -6.7 | 1.15 | 1455/1651 | not checked |
| 484 | `{"max_candles": 42, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 636.46 | 0.4 | -4.6 | 38.9 | 195.51 | 0.2 | -5.4 | 0.46 | 1504/1720 | not checked |
| 456 | `{"max_candles": 48, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 491 | `{"max_candles": 54, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 503 | `{"max_candles": 60, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 566 | `{"max_candles": 66, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 626 | `{"max_candles": 72, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 639 | `{"max_candles": 78, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 653 | `{"max_candles": 84, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 689 | `{"max_candles": 90, "n": 100, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 628.51 | 0.4 | -4.6 | 38.9 | 188.82 | 0.2 | -5.5 | 0.45 | 1504/1720 | not checked |
| 501 | `{"max_candles": 54, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 504 | `{"max_candles": 48, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 505 | `{"max_candles": 60, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 575 | `{"max_candles": 72, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 586 | `{"max_candles": 66, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 657 | `{"max_candles": 78, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 665 | `{"max_candles": 84, "n": 100, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 612.25 | 0.4 | -4.6 | 38.8 | 191.04 | 0.2 | -5.5 | 0.46 | 1505/1720 | not checked |
| 441 | `{"max_candles": 78, "n": 100, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 594.37 | 0.4 | -4.6 | 38.7 | 185.62 | 0.2 | -5.5 | 0.47 | 1505/1721 | not checked |
| 490 | `{"max_candles": 66, "n": 100, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 594.37 | 0.4 | -4.6 | 38.7 | 185.62 | 0.2 | -5.5 | 0.47 | 1505/1721 | not checked |
| 532 | `{"max_candles": 54, "n": 100, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 594.37 | 0.4 | -4.6 | 38.7 | 185.62 | 0.2 | -5.5 | 0.47 | 1505/1721 | not checked |
| 549 | `{"max_candles": 48, "n": 100, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 594.37 | 0.4 | -4.6 | 38.7 | 185.62 | 0.2 | -5.5 | 0.47 | 1505/1721 | not checked |
| 552 | `{"max_candles": 60, "n": 100, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 594.37 | 0.4 | -4.6 | 38.7 | 185.62 | 0.2 | -5.5 | 0.47 | 1505/1721 | not checked |
| 752 | `{"max_candles": 72, "n": 100, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 594.37 | 0.4 | -4.6 | 38.7 | 185.62 | 0.2 | -5.5 | 0.47 | 1505/1721 | not checked |
| 564 | `{"max_candles": 42, "n": 110, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 422.76 | 0.3 | -4.6 | 38.1 | 105.13 | 0.1 | -5.0 | 0.39 | 1503/1709 | not checked |
| 541 | `{"max_candles": 60, "n": 110, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 414.46 | 0.2 | -4.6 | 38.1 | 105.13 | 0.1 | -5.0 | 0.40 | 1503/1709 | not checked |

(13 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 757 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
