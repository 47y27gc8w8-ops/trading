# linear_regression_residual_reversion__broad: optimization summary

Updated 2026-11-26T04:18:19Z · backtest.py version `13c553f78f` · 1,032 parameter sets tested with this version (1,032 rows in results.csv in total) · last run ended: converged: no profile improved in the last 500 iterations at the smallest step size

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [linear_regression_residual_reversion__broad__max-income__v002.md](linear_regression_residual_reversion__broad__max-income__v002.md) | 1031 | `{"max_candles": 24, "n": 20, "stop_atr": 3.75, "take_profit_atr": 2.5, "z": 1.75}` | long XLF since 2026-11-18 00:00 @ 56.797033; long XLY since 2026-11-17 00:00 @ 117.675291; long XLP since 2026-11-20 00:00 @ 90.957279; long XLU since 2026-11-18 00:00 @ 43.212961; long HYG since 2026-11-13 00:00 @ 77.103126; long GDX since 2026-11-19 00:00 @ 74.352301; long VIG since 2026-11-18 00:00 @ 245.57365; long VNQ since 2026-11-17 00:00 @ 95.718709; long VTV since 2026-11-18 00:00 @ 222.906848; long CSSMI.SW since 2026-11-18 00:00 @ 155.166531; long ^SSMI since 2026-11-18 00:00 @ 14967.729206; long ^FTSE since 2026-11-18 00:00 @ 10693.806789 |
| balanced | [linear_regression_residual_reversion__broad__balanced__v002.md](linear_regression_residual_reversion__broad__balanced__v002.md) | 1032 | `{"max_candles": 24, "n": 20, "stop_atr": 2.0, "take_profit_atr": 3.5, "z": 3.0}` | long XLY since 2026-11-23 00:00 @ 116.514947; long XLU since 2026-11-18 00:00 @ 43.212961; long HYG since 2026-11-17 00:00 @ 76.743017; long VIG since 2026-11-20 00:00 @ 240.732202; long VNQ since 2026-11-18 00:00 @ 94.208254; long ^FTSE since 2026-11-19 00:00 @ 10554.264939 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 119,420.95 | 4,299.96 | 4,031.72 | 885.78 |
| return % | 1,194.21 | 43.00 | 40.32 | 8.86 |
| return %/year | 13.0 | 3.3 | 1.6 | 0.8 |
| gross profit | 293,704.58 | 17,501.28 | 11,158.80 | 7,029.88 |
| gross loss | 174,283.63 | 13,201.31 | 7,127.08 | 6,144.09 |
| trades | 7,424 | 6,776 | 3,780 | 3,500 |
| win rate % | 66.6 | 64.0 | 63.5 | 57.9 |
| avg win | 59.41 | 4.03 | 4.65 | 3.47 |
| avg loss | -70.28 | -5.41 | -5.16 | -4.17 |
| avg result / trade | 16.09 | 0.63 | 1.07 | 0.25 |
| largest single loss | -14,028.41 | -168.37 | -176.03 | -47.50 |
| largest loss % of equity | -14.59 | -26.93 | -12.03 | -29.97 |
| max drawdown | -53,631.12 | -1,409.59 | -553.89 | -712.50 |
| max drawdown % | -47.33 | -11.79 | -3.88 | -6.89 |
| profit factor | 1.69 | 1.33 | 1.57 | 1.14 |
| unusually bad trades | 761 | 631 | 164 | 148 |
| … threshold (% of equity) | 3.3 | 3.9 | 4.4 | 4.3 |
| time in market % | 13.4 | 22.7 | 5.5 | 9.2 |
| buy & hold return % | 124.13 | 280.02 | 124.13 | 280.02 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |  | 0.48 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 2.1 | 1.7 |
| 1996 | 0.7 | -0.5 |
| 1997 | 1.0 | 0.4 |
| 1998 | 1.7 | 0.2 |
| 1999 | 3.5 | 1.9 |
| 2000 | 6.5 | 0.4 |
| 2001 | 10.7 | 1.9 |
| 2002 | 33.0 | 2.3 |
| 2003 | 1.2 | 2.5 |
| 2004 | -6.6 | 1.6 |
| 2005 | 11.6 | 0.4 |
| 2006 | 19.6 | 2.5 |
| 2007 | 13.0 | -0.9 |
| 2008 | 83.7 | 6.9 |
| 2009 | 33.7 | 3.0 |
| 2010 | -14.4 | -0.3 |
| 2011 | 59.8 | 5.2 |
| 2012 | -8.3 | 2.6 |
| 2013 | -2.5 | 0.1 |
| 2014 | 1.3 | 1.4 |
| 2015 | 74.1 | 1.4 |
| 2016 (OOS) | 11.8 | 1.1 |
| 2017 (OOS) | 21.6 | 2.6 |
| 2018 (OOS) | 26.6 | -3.5 |
| 2019 (OOS) | -10.0 | -4.8 |
| 2020 (OOS) | -22.3 | -0.0 |
| 2021 (OOS) | 68.8 | 5.3 |
| 2022 (OOS) | 48.3 | -3.2 |
| 2023 (OOS) | -15.4 | -0.3 |
| 2024 (OOS) | 47.7 | 3.4 |
| 2025 (OOS) | -22.2 | 2.3 |
| 2026 (OOS) | 301.4 | 6.6 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 47.3% from a peak in-sample and 11.8% out-of-sample, and the worst single trade cost 26.9% of the account out-of-sample. About 67 of every 100 trades won in-sample. Out-of-sample it earned 3.3% a year against 13.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 21% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 3.9% from a peak in-sample and 6.9% out-of-sample, and the worst single trade cost 30.0% of the account out-of-sample. About 63 of every 100 trades won in-sample. Out-of-sample it earned 0.8% a year against 1.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 824 | `{"max_candles": 21, "n": 20, "stop_atr": 3.75, "take_profit_atr": 2.5, "z": 1.75}` | 119,491.33 | 13.0 | -47.3 | 66.6 | 4,300.43 | 3.3 | -11.8 | 0.26 | 7429/6776 | not checked |
| 644 | `{"max_candles": 21, "n": 20, "stop_atr": 3.5, "take_profit_atr": 2.5, "z": 1.75}` | 112,521.00 | 12.7 | -47.0 | 66.5 | 4,348.04 | 3.4 | -11.6 | 0.27 | 7460/6814 | not checked |
| 646 | `{"max_candles": 21, "n": 20, "stop_atr": 3.75, "take_profit_atr": 3.0, "z": 1.75}` | 96,775.96 | 11.9 | -45.6 | 66.5 | 4,233.02 | 3.3 | -11.9 | 0.28 | 7386/6748 | not checked |
| 607 | `{"max_candles": 21, "n": 20, "stop_atr": 3.5, "take_profit_atr": 3.0, "z": 1.75}` | 91,139.19 | 11.7 | -45.3 | 66.4 | 4,264.39 | 3.3 | -11.8 | 0.28 | 7417/6786 | not checked |
| 1019 | `{"max_candles": 25, "n": 25, "stop_atr": 4.0, "take_profit_atr": 4.5, "z": 1.5}` | 68,984.64 | 10.3 | -29.4 | 66.5 | 3,328.99 | 2.7 | -17.0 | 0.26 | 6752/6086 | not checked |
| 1003 | `{"max_candles": 27, "n": 25, "stop_atr": 4.0, "take_profit_atr": 4.0, "z": 1.5}` | 67,928.17 | 10.3 | -29.2 | 66.5 | 3,257.40 | 2.6 | -17.0 | 0.26 | 6753/6088 | not checked |
| 983 | `{"max_candles": 25, "n": 25, "stop_atr": 3.75, "take_profit_atr": 4.5, "z": 1.5}` | 63,339.62 | 10.0 | -28.2 | 66.4 | 3,390.62 | 2.7 | -16.6 | 0.27 | 6790/6127 | not checked |
| 1015 | `{"max_candles": 26, "n": 25, "stop_atr": 3.75, "take_profit_atr": 4.0, "z": 1.5}` | 62,375.13 | 9.9 | -28.1 | 66.4 | 3,323.79 | 2.7 | -16.6 | 0.27 | 6791/6129 | not checked |
| 787 | `{"max_candles": 25, "n": 25, "stop_atr": 3.25, "take_profit_atr": 6.0, "z": 1.5}` | 57,459.32 | 9.5 | -27.0 | 66.2 | 2,915.14 | 2.4 | -16.8 | 0.25 | 6926/6276 | not checked |
| 907 | `{"max_candles": 26, "n": 25, "stop_atr": 3.5, "take_profit_atr": 5.0, "z": 1.5}` | 55,836.18 | 9.4 | -26.5 | 66.3 | 2,885.32 | 2.4 | -16.1 | 0.25 | 6857/6178 | not checked |
| 1029 | `{"max_candles": 25, "n": 25, "stop_atr": 3.75, "take_profit_atr": 5.0, "z": 1.5}` | 53,344.86 | 9.2 | -26.0 | 66.4 | 3,138.10 | 2.5 | -16.5 | 0.28 | 6790/6122 | not checked |
| 828 | `{"max_candles": 25, "n": 25, "stop_atr": 3.0, "take_profit_atr": 5.0, "z": 1.5}` | 49,788.49 | 8.9 | -25.7 | 65.8 | 2,764.20 | 2.3 | -16.8 | 0.26 | 7022/6384 | not checked |
| 858 | `{"max_candles": 25, "n": 25, "stop_atr": 2.75, "take_profit_atr": 5.0, "z": 1.5}` | 44,500.53 | 8.4 | -25.6 | 65.1 | 2,624.99 | 2.2 | -15.9 | 0.26 | 7130/6537 | not checked |
| 851 | `{"max_candles": 15, "n": 25, "stop_atr": 3.25, "take_profit_atr": 1.5, "z": 1.5}` | 32,433.91 | 7.1 | -18.9 | 69.2 | 2,170.40 | 1.8 | -13.5 | 0.26 | 7627/6873 | not checked |
| 900 | `{"max_candles": 15, "n": 25, "stop_atr": 3.5, "take_profit_atr": 1.5, "z": 1.5}` | 31,567.21 | 7.0 | -18.7 | 69.2 | 2,154.11 | 1.8 | -13.7 | 0.26 | 7553/6764 | not checked |
| 629 | `{"max_candles": 24, "n": 45, "stop_atr": 3.75, "take_profit_atr": 3.5, "z": 2.0}` | 14,529.67 | 4.4 | -15.1 | 65.5 | 1,303.89 | 1.1 | -14.1 | 0.26 | 3819/3501 | not checked |
| 167 | `{"max_candles": 14, "n": 120, "stop_atr": 3.0, "take_profit_atr": 3.5, "z": 1.5}` | 12,115.34 | 3.9 | -13.8 | 57.7 | 2,694.66 | 2.2 | -21.1 | 0.58 | 3597/3707 | 1.00 |
| 159 | `{"max_candles": 14, "n": 120, "stop_atr": 2.75, "take_profit_atr": 3.5, "z": 1.5}` | 11,193.58 | 3.6 | -13.2 | 56.5 | 2,672.11 | 2.2 | -20.6 | 0.60 | 3694/3783 | 1.00 |
| 168 | `{"max_candles": 14, "n": 120, "stop_atr": 2.75, "take_profit_atr": 3.0, "z": 1.5}` | 10,652.85 | 3.5 | -13.0 | 57.0 | 2,487.25 | 2.1 | -20.8 | 0.58 | 3730/3839 | not checked |
| 176 | `{"max_candles": 14, "n": 120, "stop_atr": 3.0, "take_profit_atr": 3.0, "z": 1.5}` | 10,510.68 | 3.5 | -12.5 | 58.3 | 2,463.61 | 2.0 | -21.4 | 0.59 | 3644/3760 | not checked |
| 166 | `{"max_candles": 14, "n": 120, "stop_atr": 2.5, "take_profit_atr": 3.5, "z": 1.5}` | 10,362.18 | 3.5 | -12.3 | 54.9 | 2,523.80 | 2.1 | -20.1 | 0.61 | 3830/3878 | not checked |
| 220 | `{"max_candles": 17, "n": 50, "stop_atr": 2.75, "take_profit_atr": 5.5, "z": 2.25}` | 9,007.95 | 3.1 | -11.1 | 60.1 | 1,051.07 | 0.9 | -10.4 | 0.30 | 3395/3133 | not checked |
| 682 | `{"max_candles": 24, "n": 20, "stop_atr": 2.25, "take_profit_atr": 4.0, "z": 2.75}` | 8,131.56 | 2.9 | -9.2 | 64.4 | 1,114.16 | 1.0 | -8.2 | 0.34 | 4493/4166 | not checked |
| 52 | `{"max_candles": 14, "n": 55, "stop_atr": 2.5, "take_profit_atr": 3.5, "z": 2.0}` | 6,639.94 | 2.5 | -8.8 | 56.1 | 751.86 | 0.7 | -11.3 | 0.27 | 4011/3628 | 1.00 |
| 112 | `{"max_candles": 15, "n": 55, "stop_atr": 2.5, "take_profit_atr": 3.5, "z": 2.0}` | 6,281.72 | 2.4 | -8.7 | 56.6 | 928.85 | 0.8 | -11.0 | 0.35 | 3984/3601 | 1.00 |

(17 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,032 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
