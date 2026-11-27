# return_percentile_shock__broad: optimization summary

Updated 2026-11-25T11:07:11Z · backtest.py version `a357bf14a8` · 722 parameter sets tested with this version (722 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [return_percentile_shock__broad__max-income__v001.md](return_percentile_shock__broad__max-income__v001.md) | 222 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | long XLP since 2026-11-20 00:00 @ 90.957279; long USO since 2026-11-24 00:00 @ 135.160531; long VIG since 2026-11-23 00:00 @ 240.492124; long VTV since 2026-11-23 00:00 @ 218.265457; long CSSMI.SW since 2026-11-18 00:00 @ 155.166531 |
| balanced | [return_percentile_shock__broad__balanced__v001.md](return_percentile_shock__broad__balanced__v001.md) | 222 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | long XLP since 2026-11-20 00:00 @ 90.957279; long USO since 2026-11-24 00:00 @ 135.160531; long VIG since 2026-11-23 00:00 @ 240.492124; long VTV since 2026-11-23 00:00 @ 218.265457; long CSSMI.SW since 2026-11-18 00:00 @ 155.166531 |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,211.90 | 1,131.14 | 1,211.90 | 1,131.14 |
| return % | 12.12 | 11.31 | 12.12 | 11.31 |
| return %/year | 0.7 | 1.0 | 0.7 | 1.0 |
| gross profit | 8,477.13 | 10,304.34 | 8,477.13 | 10,304.34 |
| gross loss | 7,265.23 | 9,173.20 | 7,265.23 | 9,173.20 |
| trades | 6,328 | 6,950 | 6,328 | 6,950 |
| win rate % | 60.6 | 60.3 | 60.6 | 60.3 |
| avg win | 2.21 | 2.46 | 2.21 | 2.46 |
| avg loss | -2.91 | -3.32 | -2.91 | -3.32 |
| avg result / trade | 0.19 | 0.16 | 0.19 | 0.16 |
| largest single loss | -54.85 | -144.29 | -54.85 | -144.29 |
| largest loss % of equity | -19.28 | -21.83 | -19.28 | -21.83 |
| max drawdown | -756.41 | -1,069.62 | -756.41 | -1,069.62 |
| max drawdown % | -6.70 | -10.14 | -6.70 | -10.14 |
| profit factor | 1.17 | 1.12 | 1.17 | 1.12 |
| unusually bad trades | 527 | 655 | 527 | 655 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 10.1 | 15.9 | 10.1 | 15.9 |
| buy & hold return % | 92.38 | 306.09 | 92.38 | 306.09 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.38 |  | 1.38 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | -0.2 | -0.2 |
| 2001 | -0.3 | -0.3 |
| 2002 | 0.0 | 0.0 |
| 2003 | 3.3 | 3.3 |
| 2004 | -0.5 | -0.5 |
| 2005 | -1.0 | -1.0 |
| 2006 | 1.4 | 1.4 |
| 2007 | 0.1 | 0.1 |
| 2008 | -0.7 | -0.7 |
| 2009 | 7.3 | 7.3 |
| 2010 | -0.4 | -0.4 |
| 2011 | -2.5 | -2.5 |
| 2012 | -0.2 | -0.2 |
| 2013 | 4.4 | 4.4 |
| 2014 | 1.6 | 1.6 |
| 2015 | -0.6 | -0.6 |
| 2016 (OOS) | 2.3 | 2.3 |
| 2017 (OOS) | 3.3 | 3.3 |
| 2018 (OOS) | -7.9 | -7.9 |
| 2019 (OOS) | 1.4 | 1.4 |
| 2020 (OOS) | 4.1 | 4.1 |
| 2021 (OOS) | 11.7 | 11.7 |
| 2022 (OOS) | -4.9 | -4.9 |
| 2023 (OOS) | -1.3 | -1.3 |
| 2024 (OOS) | 5.4 | 5.4 |
| 2025 (OOS) | 1.7 | 1.7 |
| 2026 (OOS) | 0.8 | 0.8 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 6.7% from a peak in-sample and 10.1% out-of-sample, and the worst single trade cost 21.8% of the account out-of-sample. About 61 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 99% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 6.7% from a peak in-sample and 10.1% out-of-sample, and the worst single trade cost 21.8% of the account out-of-sample. About 61 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 99% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 295 | `{"max_candles": 14, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,262.82 | 0.8 | -7.2 | 60.7 | 1,195.69 | 1.0 | -10.1 | 1.39 | 6305/6932 | not checked |
| 315 | `{"max_candles": 14, "n": 10, "rank": 7, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,262.82 | 0.8 | -7.2 | 60.7 | 1,195.69 | 1.0 | -10.1 | 1.39 | 6305/6932 | not checked |
| 405 | `{"max_candles": 14, "n": 10, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,262.82 | 0.8 | -7.2 | 60.7 | 1,195.69 | 1.0 | -10.1 | 1.39 | 6305/6932 | not checked |
| 426 | `{"max_candles": 14, "n": 10, "rank": 6, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,262.82 | 0.8 | -7.2 | 60.7 | 1,195.69 | 1.0 | -10.1 | 1.39 | 6305/6932 | not checked |
| 576 | `{"max_candles": 14, "n": 10, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,262.82 | 0.8 | -7.2 | 60.7 | 1,195.69 | 1.0 | -10.1 | 1.39 | 6305/6932 | not checked |
| 429 | `{"max_candles": 18, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 529 | `{"max_candles": 18, "n": 10, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 580 | `{"max_candles": 18, "n": 10, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 582 | `{"max_candles": 20, "n": 10, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 598 | `{"max_candles": 20, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 670 | `{"max_candles": 18, "n": 10, "rank": 7, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 696 | `{"max_candles": 20, "n": 10, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,258.61 | 0.7 | -7.2 | 60.7 | 1,221.76 | 1.1 | -10.1 | 1.43 | 6304/6932 | not checked |
| 4 | `{"max_candles": 8, "n": 10, "rank": 7, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,211.90 | 0.7 | -6.7 | 60.6 | 1,131.14 | 1.0 | -10.1 | 1.38 | 6328/6950 | not checked |
| 5 | `{"max_candles": 8, "n": 10, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,211.90 | 0.7 | -6.7 | 60.6 | 1,131.14 | 1.0 | -10.1 | 1.38 | 6328/6950 | not checked |
| 11 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,211.90 | 0.7 | -6.7 | 60.6 | 1,131.14 | 1.0 | -10.1 | 1.38 | 6328/6950 | 1.00 |
| 268 | `{"max_candles": 8, "n": 10, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,211.90 | 0.7 | -6.7 | 60.6 | 1,131.14 | 1.0 | -10.1 | 1.38 | 6328/6950 | not checked |
| 490 | `{"max_candles": 8, "n": 10, "rank": 6, "stop_atr": 5.0, "take_profit_atr": 2.0}` | 1,211.90 | 0.7 | -6.7 | 60.6 | 1,131.14 | 1.0 | -10.1 | 1.38 | 6328/6950 | not checked |
| 8 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 5.0, "take_profit_atr": 2.5}` | 1,148.75 | 0.7 | -6.7 | 60.5 | 1,196.81 | 1.0 | -10.0 | 1.53 | 6328/6950 | not checked |
| 247 | `{"max_candles": 8, "n": 10, "rank": 7, "stop_atr": 5.0, "take_profit_atr": 2.5}` | 1,148.75 | 0.7 | -6.7 | 60.5 | 1,196.81 | 1.0 | -10.0 | 1.53 | 6328/6950 | not checked |
| 297 | `{"max_candles": 8, "n": 10, "rank": 6, "stop_atr": 5.0, "take_profit_atr": 2.5}` | 1,148.75 | 0.7 | -6.7 | 60.5 | 1,196.81 | 1.0 | -10.0 | 1.53 | 6328/6950 | not checked |
| 299 | `{"max_candles": 8, "n": 10, "rank": 10, "stop_atr": 5.0, "take_profit_atr": 2.5}` | 1,148.75 | 0.7 | -6.7 | 60.5 | 1,196.81 | 1.0 | -10.0 | 1.53 | 6328/6950 | not checked |
| 372 | `{"max_candles": 8, "n": 10, "rank": 9, "stop_atr": 5.0, "take_profit_atr": 2.5}` | 1,148.75 | 0.7 | -6.7 | 60.5 | 1,196.81 | 1.0 | -10.0 | 1.53 | 6328/6950 | not checked |
| 242 | `{"max_candles": 8, "n": 10, "rank": 8, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 1,069.75 | 0.6 | -5.9 | 60.5 | 942.78 | 0.8 | -8.9 | 1.30 | 6334/6982 | not checked |
| 322 | `{"max_candles": 8, "n": 10, "rank": 9, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 1,069.75 | 0.6 | -5.9 | 60.5 | 942.78 | 0.8 | -8.9 | 1.30 | 6334/6982 | not checked |
| 271 | `{"max_candles": 8, "n": 10, "rank": 7, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 1,009.79 | 0.6 | -5.9 | 60.5 | 983.93 | 0.9 | -8.8 | 1.45 | 6334/6982 | not checked |

(11 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 722 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
