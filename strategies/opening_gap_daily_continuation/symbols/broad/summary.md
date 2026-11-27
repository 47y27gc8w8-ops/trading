# opening_gap_daily_continuation__broad: optimization summary

Updated 2026-11-25T09:32:41Z · backtest.py version `8790f6adcc` · 930 parameter sets tested with this version (930 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, CDW, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [opening_gap_daily_continuation__broad__max-income__v002.md](opening_gap_daily_continuation__broad__max-income__v002.md) | 929 | `{"gap": 0.0, "max_candles": 19, "stop_atr": 4.75, "take_profit_atr": 8.5}` | long APH since 2026-11-24 00:00 @ 76.112823; long CMG since 2026-10-30 00:00 @ 31.679501; long COST since 2026-11-02 00:00 @ 1016.174756; long GIS since 2026-11-23 00:00 @ 34.790433; long MKC since 2026-11-23 00:00 @ 46.694004; long PANW since 2026-11-20 00:00 @ 359.147721; long STE since 2026-11-05 00:00 @ 251.76071; long TJX since 2026-11-19 00:00 @ 138.631573; long TSN since 2026-11-17 00:00 @ 63.028901; long WMT since 2026-11-23 00:00 @ 126.677991 |
| balanced | [opening_gap_daily_continuation__broad__balanced__v002.md](opening_gap_daily_continuation__broad__balanced__v002.md) | 930 | `{"gap": 0.0, "max_candles": 7, "stop_atr": 4.75, "take_profit_atr": 8.5}` | long APH since 2026-11-24 00:00 @ 76.112823; long COST since 2026-11-23 00:00 @ 1090.467057; long GIS since 2026-11-23 00:00 @ 34.790433; long MKC since 2026-11-23 00:00 @ 46.694004; long PANW since 2026-11-20 00:00 @ 359.147721; long TJX since 2026-11-19 00:00 @ 138.631573; long TSN since 2026-11-17 00:00 @ 63.028901; long WMT since 2026-11-23 00:00 @ 126.677991 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,960.12 | 726.83 | 1,109.31 | 240.37 |
| return % | 19.60 | 7.27 | 11.09 | 2.40 |
| return %/year | 0.9 | 0.7 | 0.5 | 0.2 |
| gross profit | 14,187.31 | 6,248.07 | 11,794.08 | 5,077.33 |
| gross loss | 12,227.19 | 5,521.24 | 10,684.76 | 4,836.95 |
| trades | 22,781 | 12,254 | 23,684 | 12,676 |
| win rate % | 39.2 | 39.8 | 45.5 | 46.3 |
| avg win | 1.59 | 1.28 | 1.10 | 0.86 |
| avg loss | -0.88 | -0.75 | -0.83 | -0.71 |
| avg result / trade | 0.09 | 0.06 | 0.05 | 0.02 |
| largest single loss | -35.46 | -16.57 | -25.29 | -10.53 |
| largest loss % of equity | -10.91 | -21.31 | -11.78 | -11.86 |
| max drawdown | -694.27 | -346.22 | -593.05 | -223.02 |
| max drawdown % | -5.80 | -3.30 | -5.27 | -2.20 |
| profit factor | 1.16 | 1.13 | 1.10 | 1.05 |
| unusually bad trades | 2,505 | 1,248 | 2,350 | 1,210 |
| … threshold (% of equity) | 5.2 | 5.2 | 5.2 | 5.0 |
| time in market % | 8.4 | 9.0 | 5.5 | 5.7 |
| buy & hold return % | 1,897.80 | 476.79 | 1,897.80 | 476.79 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.76 |  | 0.44 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 1.7 | 1.7 |
| 1996 | 2.0 | 1.1 |
| 1997 | 2.1 | 1.2 |
| 1998 | 2.9 | 1.5 |
| 1999 | 1.7 | 1.1 |
| 2000 | 1.7 | 1.1 |
| 2001 | -0.2 | 0.3 |
| 2002 | -0.4 | -0.3 |
| 2003 | 2.7 | 2.3 |
| 2004 | 2.2 | 0.8 |
| 2005 | 0.9 | 0.4 |
| 2006 | 0.4 | 0.3 |
| 2007 | -0.1 | -0.7 |
| 2008 | -3.7 | -3.2 |
| 2009 | 2.1 | 2.9 |
| 2010 | 1.6 | 0.4 |
| 2011 | -1.8 | -1.2 |
| 2012 | 0.3 | 0.1 |
| 2013 | 2.9 | 1.8 |
| 2014 | 1.1 | -0.1 |
| 2015 | -1.7 | -0.8 |
| 2016 (OOS) | 1.5 | 0.6 |
| 2017 (OOS) | 1.6 | 0.2 |
| 2018 (OOS) | -0.6 | -0.7 |
| 2019 (OOS) | 2.7 | 1.0 |
| 2020 (OOS) | -0.3 | -0.6 |
| 2021 (OOS) | 1.2 | 0.9 |
| 2022 (OOS) | 0.0 | -0.4 |
| 2023 (OOS) | 2.7 | 0.8 |
| 2024 (OOS) | 2.3 | 0.5 |
| 2025 (OOS) | 0.4 | -0.3 |
| 2026 (OOS) | -0.4 | 0.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 5.8% from a peak in-sample and 3.3% out-of-sample, and the worst single trade cost 21.3% of the account out-of-sample. About 39 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 5.3% from a peak in-sample and 2.2% out-of-sample, and the worst single trade cost 11.9% of the account out-of-sample. About 45 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 627 | `{"gap": 0.0, "max_candles": 19, "stop_atr": 4.75, "take_profit_atr": 8.5}` | 1,960.12 | 0.9 | -5.8 | 39.2 | 726.83 | 0.7 | -3.3 | 0.76 | 22781/12254 | 1.00 |
| 688 | `{"gap": 0.0, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 8.0}` | 1,885.36 | 0.8 | -5.5 | 40.3 | 656.64 | 0.6 | -2.8 | 0.71 | 23015/12369 | not checked |
| 613 | `{"gap": 0.0, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 5.5}` | 1,806.55 | 0.8 | -5.4 | 40.3 | 571.91 | 0.5 | -2.5 | 0.65 | 23072/12397 | not checked |
| 522 | `{"gap": 0.0, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 1,744.12 | 0.8 | -5.4 | 40.3 | 614.78 | 0.6 | -2.6 | 0.71 | 23050/12391 | not checked |
| 778 | `{"gap": 0.0, "max_candles": 12, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 1,643.34 | 0.7 | -5.3 | 40.7 | 572.97 | 0.5 | -2.7 | 0.70 | 23114/12426 | not checked |
| 609 | `{"gap": 0.25, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 8.0}` | 1,423.97 | 0.6 | -5.1 | 40.8 | 663.90 | 0.6 | -2.7 | 0.92 | 17307/9695 | not checked |
| 746 | `{"gap": 0.25, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 5.5}` | 1,421.18 | 0.6 | -4.9 | 40.8 | 584.56 | 0.5 | -2.4 | 0.81 | 17339/9712 | not checked |
| 542 | `{"gap": 0.25, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 1,363.86 | 0.6 | -4.9 | 40.8 | 626.64 | 0.6 | -2.5 | 0.92 | 17327/9706 | not checked |
| 838 | `{"gap": 0.25, "max_candles": 12, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 1,275.82 | 0.6 | -4.8 | 41.2 | 582.40 | 0.5 | -2.6 | 0.91 | 17362/9732 | not checked |
| 438 | `{"gap": 0.25, "max_candles": 12, "stop_atr": 4.75, "take_profit_atr": 4.5}` | 1,169.67 | 0.5 | -4.8 | 41.4 | 536.95 | 0.5 | -2.6 | 0.91 | 17409/9757 | not checked |
| 799 | `{"gap": 0.5, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 5.5}` | 1,122.48 | 0.5 | -4.7 | 41.2 | 449.02 | 0.4 | -2.3 | 0.78 | 13703/7834 | not checked |
| 532 | `{"gap": 0.5, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 1,062.85 | 0.5 | -4.6 | 41.2 | 471.65 | 0.4 | -2.4 | 0.88 | 13695/7829 | not checked |
| 926 | `{"gap": 0.75, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 7.5}` | 1,027.53 | 0.5 | -4.3 | 41.4 | 548.24 | 0.5 | -2.2 | 1.04 | 11081/6499 | not checked |
| 919 | `{"gap": 0.75, "max_candles": 13, "stop_atr": 4.75, "take_profit_atr": 5.5}` | 998.92 | 0.5 | -4.3 | 41.4 | 500.80 | 0.5 | -2.0 | 1.00 | 11093/6508 | not checked |
| 507 | `{"gap": 0.75, "max_candles": 12, "stop_atr": 4.75, "take_profit_atr": 6.5}` | 930.33 | 0.4 | -4.2 | 41.8 | 514.44 | 0.5 | -2.3 | 1.09 | 11101/6518 | not checked |
| 471 | `{"gap": 0.75, "max_candles": 12, "stop_atr": 4.75, "take_profit_atr": 4.0}` | 866.01 | 0.4 | -4.1 | 42.0 | 415.64 | 0.4 | -2.2 | 0.93 | 11144/6538 | not checked |
| 360 | `{"gap": 1.25, "max_candles": 48, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 687.85 | 0.3 | -3.6 | 40.5 | 478.00 | 0.4 | -2.2 | 1.34 | 7965/4841 | not checked |
| 824 | `{"gap": 1.5, "max_candles": 43, "stop_atr": 5.5, "take_profit_atr": 4.0}` | 656.26 | 0.3 | -3.3 | 40.9 | 534.22 | 0.5 | -2.2 | 1.60 | 6831/4269 | not checked |
| 363 | `{"gap": 1.5, "max_candles": 30, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 647.64 | 0.3 | -3.2 | 40.8 | 516.31 | 0.5 | -2.3 | 1.53 | 6840/4272 | not checked |
| 262 | `{"gap": 1.75, "max_candles": 72, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 502.53 | 0.2 | -3.1 | 41.2 | 392.14 | 0.3 | -2.2 | 1.52 | 5928/3741 | not checked |
| 734 | `{"gap": 2.0, "max_candles": 49, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 440.57 | 0.2 | -3.0 | 40.6 | 426.25 | 0.4 | -2.2 | 1.81 | 5128/3346 | not checked |
| 293 | `{"gap": 1.75, "max_candles": 84, "stop_atr": 3.75, "take_profit_atr": 3.0}` | 426.83 | 0.2 | -2.9 | 41.6 | 304.67 | 0.3 | -2.2 | 1.40 | 5940/3748 | not checked |
| 804 | `{"gap": 2.0, "max_candles": 13, "stop_atr": 5.25, "take_profit_atr": 3.0}` | 385.00 | 0.2 | -2.7 | 43.1 | 253.39 | 0.2 | -1.9 | 1.28 | 5156/3371 | not checked |
| 366 | `{"gap": 1.75, "max_candles": 84, "stop_atr": 3.75, "take_profit_atr": 2.0}` | 308.38 | 0.1 | -2.7 | 45.3 | 265.28 | 0.2 | -1.9 | 1.71 | 5975/3774 | not checked |
| 173 | `{"gap": 1.75, "max_candles": 42, "stop_atr": 3.0, "take_profit_atr": 2.0}` | 303.86 | 0.1 | -2.7 | 45.1 | 230.44 | 0.2 | -1.9 | 1.50 | 5975/3775 | 1.00 |

(13 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 930 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
