# low_volume_pullback_rebound__broad: optimization summary

Updated 2026-11-26T05:33:18Z · backtest.py version `fab5e0caea` · 709 parameter sets tested with this version (709 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [low_volume_pullback_rebound__broad__max-income__v002.md](low_volume_pullback_rebound__broad__max-income__v002.md) | 709 | `{"fraction": 1.0, "max_candles": 32, "stop_atr": 3.0, "take_profit_atr": 7.0}` | long NESN.SW since 2026-11-25 00:00 @ 86.796028; long GIVN.SW since 2026-11-05 00:00 @ 4097.2288; long HOLN.SW since 2026-11-03 00:00 @ 70.481137; long SCMN.SW since 2026-11-25 00:00 @ 715.2145; long SOON.SW since 2026-11-24 00:00 @ 294.888428; long AES since 2026-11-03 00:00 @ 14.914473; long AFL since 2026-10-21 00:00 @ 120.239068; long A since 2026-11-24 00:00 @ 187.016095; long ALL since 2026-10-21 00:00 @ 250.655176; long AEE since 2026-10-30 00:00 @ 111.523445; long AON since 2026-11-23 00:00 @ 331.0993; long ACGL since 2026-11-05 00:00 @ 112.413711; long AJG since 2026-11-25 00:00 @ 290.087; long ADP since 2026-10-21 00:00 @ 290.867233; long AZO since 2026-10-21 00:00 @ 3148.994464; long BRO since 2026-11-23 00:00 @ 72.031605; long CAH since 2026-10-30 00:00 @ 255.09651; long CBOE since 2026-10-21 00:00 @ 315.0945; long COR since 2026-11-25 00:00 @ 350.175028; long CMG since 2026-11-10 00:00 @ 35.950781; long CB since 2026-11-05 00:00 @ 378.993669; long CHD since 2026-10-21 00:00 @ 105.131003; long CINF since 2026-11-13 00:00 @ 190.417109; long CLX since 2026-11-25 00:00 @ 107.132128; long CMS since 2026-10-23 00:00 @ 69.595229; long CL since 2026-10-15 00:00 @ 93.753179; long ED since 2026-10-21 00:00 @ 110.75242; long COST since 2026-11-12 00:00 @ 1096.598901; long DPZ since 2026-11-13 00:00 @ 343.192923; long DUK since 2026-10-23 00:00 @ 124.408972; long EW since 2026-11-12 00:00 @ 106.101821; long ERIE since 2026-10-21 00:00 @ 246.293867; long FE since 2026-10-23 00:00 @ 45.906172; long GEN since 2026-11-05 00:00 @ 31.011298; long GIS since 2026-11-23 00:00 @ 34.790433; long GILD since 2026-10-15 00:00 @ 156.436916; long GPN since 2026-11-23 00:00 @ 93.0279; long HIG since 2026-11-23 00:00 @ 136.260867; long HSY since 2026-11-05 00:00 @ 175.696939; long HD since 2026-10-23 00:00 @ 325.0975; long HRL since 2026-11-05 00:00 @ 23.0069; long IDXX since 2026-11-12 00:00 @ 711.893497; long JKHY since 2026-11-11 00:00 @ 173.121928; long LH since 2026-11-05 00:00 @ 372.661753; long MRSH since 2026-10-23 00:00 @ 198.479524; long MAS since 2026-10-23 00:00 @ 77.067879; long MTD since 2026-11-24 00:00 @ 1731.049188; long MDLZ since 2026-10-30 00:00 @ 65.0195; long MSI since 2026-10-30 00:00 @ 496.949028; long ORLY since 2026-11-12 00:00 @ 91.477432; long PAYX since 2026-11-25 00:00 @ 116.654989; long PEP since 2026-11-23 00:00 @ 138.991682; long PPG since 2026-11-24 00:00 @ 120.086018; long PG since 2026-10-15 00:00 @ 157.335933; long PGR since 2026-11-25 00:00 @ 237.791317; long PTC since 2026-11-02 00:00 @ 194.788415; long PEG since 2026-11-10 00:00 @ 74.572368; long DGX since 2026-10-21 00:00 @ 235.410598; long REGN since 2026-11-12 00:00 @ 971.601505; long RSG since 2026-10-21 00:00 @ 232.009584; long ROP since 2026-11-25 00:00 @ 478.683571; long SO since 2026-10-23 00:00 @ 92.947143; long STE since 2026-11-16 00:00 @ 264.869993; long TSCO since 2026-10-30 00:00 @ 34.500349; long TSN since 2026-11-23 00:00 @ 64.439324; long VRSK since 2026-11-25 00:00 @ 206.241847; long VZ since 2026-11-23 00:00 @ 46.283881; long WRB since 2026-10-30 00:00 @ 74.52235; long WMT since 2026-10-15 00:00 @ 120.036; long WM since 2026-11-05 00:00 @ 241.102308; long WEC since 2026-11-05 00:00 @ 118.447106; long WTW since 2026-10-21 00:00 @ 319.245739; long YUM since 2026-10-21 00:00 @ 150.495132 |
| balanced | [low_volume_pullback_rebound__broad__balanced__v001.md](low_volume_pullback_rebound__broad__balanced__v001.md) | 353 | `{"fraction": 0.5, "max_candles": 36, "stop_atr": 3.0, "take_profit_atr": 1.5}` | long CHD since 2026-11-16 00:00 @ 114.494337; long PTC since 2026-11-02 00:00 @ 194.788415 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 5,045.98 | 1,859.27 | 551.93 | 91.02 |
| return % | 50.46 | 18.59 | 5.52 | 0.91 |
| return %/year | 2.0 | 1.6 | 0.3 | 0.1 |
| gross profit | 30,869.50 | 14,169.14 | 4,938.74 | 1,089.16 |
| gross loss | 25,823.51 | 12,309.87 | 4,386.81 | 998.14 |
| trades | 48,114 | 27,706 | 11,661 | 2,946 |
| win rate % | 34.0 | 34.5 | 49.5 | 49.9 |
| avg win | 1.89 | 1.48 | 0.86 | 0.74 |
| avg loss | -0.81 | -0.68 | -0.75 | -0.68 |
| avg result / trade | 0.10 | 0.07 | 0.05 | 0.03 |
| largest single loss | -67.84 | -13.57 | -8.84 | -4.83 |
| largest loss % of equity | -15.13 | -14.64 | -32.54 | -23.22 |
| max drawdown | -1,256.71 | -713.42 | -66.20 | -50.77 |
| max drawdown % | -9.74 | -5.99 | -0.66 | -0.50 |
| profit factor | 1.20 | 1.15 | 1.13 | 1.09 |
| unusually bad trades | 5,845 | 3,308 | 913 | 218 |
| … threshold (% of equity) | 4.4 | 4.5 | 5.5 | 5.2 |
| time in market % | 20.0 | 23.4 | 2.2 | 1.2 |
| buy & hold return % | 1,822.77 | 468.04 | 1,822.77 | 468.04 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.81 |  | 0.31 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 4.2 | 0.5 |
| 1996 | 1.1 | -0.2 |
| 1997 | 4.3 | 0.3 |
| 1998 | 3.0 | 0.4 |
| 1999 | 3.6 | 0.4 |
| 2000 | -0.6 | 0.1 |
| 2001 | -4.1 | -0.2 |
| 2002 | -3.0 | -0.3 |
| 2003 | 8.6 | 1.1 |
| 2004 | 7.0 | 0.7 |
| 2005 | 0.7 | -0.2 |
| 2006 | 3.8 | 0.3 |
| 2007 | 2.4 | -0.0 |
| 2008 | -5.1 | -0.1 |
| 2009 | 6.7 | 0.5 |
| 2010 | 3.3 | 0.5 |
| 2011 | -2.0 | 0.3 |
| 2012 | 3.6 | 0.4 |
| 2013 | 6.0 | 0.6 |
| 2014 | 3.5 | 0.6 |
| 2015 | -4.0 | -0.3 |
| 2016 (OOS) | 1.8 | -0.1 |
| 2017 (OOS) | 3.8 | 0.2 |
| 2018 (OOS) | -0.2 | 0.5 |
| 2019 (OOS) | 4.2 | 0.0 |
| 2020 (OOS) | 4.3 | 0.3 |
| 2021 (OOS) | 5.2 | -0.0 |
| 2022 (OOS) | -5.1 | -0.5 |
| 2023 (OOS) | 5.3 | 0.3 |
| 2024 (OOS) | 3.3 | -0.1 |
| 2025 (OOS) | 0.5 | -0.0 |
| 2026 (OOS) | 0.1 | -0.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.7% from a peak in-sample and 6.0% out-of-sample, and the worst single trade cost 14.6% of the account out-of-sample. About 34 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.7% from a peak in-sample and 0.5% out-of-sample, and the worst single trade cost 23.2% of the account out-of-sample. About 50 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.3% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 461 | `{"fraction": 1.0, "max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 5,126.18 | 2.0 | -9.5 | 34.1 | 1,907.03 | 1.6 | -5.9 | 0.81 | 48075/27682 | not checked |
| 481 | `{"fraction": 1.0, "max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 4,863.84 | 1.9 | -8.9 | 34.1 | 1,859.52 | 1.6 | -5.8 | 0.83 | 48618/27978 | not checked |
| 591 | `{"fraction": 1.0, "max_candles": 32, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 4,856.22 | 1.9 | -8.9 | 34.1 | 1,851.08 | 1.6 | -5.8 | 0.83 | 48623/27982 | not checked |
| 631 | `{"fraction": 1.0, "max_candles": 32, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 4,847.93 | 1.9 | -8.8 | 34.1 | 1,841.56 | 1.6 | -5.8 | 0.82 | 48629/27987 | not checked |
| 470 | `{"fraction": 1.0, "max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 4,826.13 | 1.9 | -8.7 | 34.1 | 1,785.97 | 1.5 | -5.8 | 0.80 | 48976/28172 | not checked |
| 385 | `{"fraction": 0.9, "max_candles": 32, "stop_atr": 3.75, "take_profit_atr": 7.0}` | 4,825.12 | 1.9 | -8.4 | 34.2 | 1,658.36 | 1.4 | -5.8 | 0.75 | 43100/24314 | not checked |
| 551 | `{"fraction": 0.9, "max_candles": 36, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 4,768.28 | 1.9 | -8.2 | 34.2 | 1,646.81 | 1.4 | -5.8 | 0.75 | 42897/24194 | not checked |
| 604 | `{"fraction": 0.9, "max_candles": 40, "stop_atr": 3.75, "take_profit_atr": 7.0}` | 4,737.54 | 1.9 | -8.2 | 34.2 | 1,615.29 | 1.4 | -5.8 | 0.75 | 42785/24111 | not checked |
| 596 | `{"fraction": 0.9, "max_candles": 44, "stop_atr": 3.75, "take_profit_atr": 7.0}` | 4,685.02 | 1.9 | -8.2 | 34.2 | 1,610.41 | 1.4 | -5.9 | 0.75 | 42736/24079 | not checked |
| 590 | `{"fraction": 0.9, "max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 4,566.14 | 1.8 | -7.9 | 34.2 | 1,629.39 | 1.4 | -5.6 | 0.77 | 43841/24690 | not checked |
| 484 | `{"fraction": 0.9, "max_candles": 32, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 4,562.32 | 1.8 | -7.8 | 34.2 | 1,632.19 | 1.4 | -5.6 | 0.77 | 43845/24692 | not checked |
| 536 | `{"fraction": 0.9, "max_candles": 40, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 4,533.47 | 1.8 | -7.7 | 34.2 | 1,618.31 | 1.4 | -5.5 | 0.77 | 43658/24581 | not checked |
| 625 | `{"fraction": 0.9, "max_candles": 40, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 4,530.25 | 1.8 | -7.7 | 34.2 | 1,621.83 | 1.4 | -5.6 | 0.77 | 43662/24583 | not checked |
| 558 | `{"fraction": 0.9, "max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 4,522.41 | 1.8 | -7.6 | 34.2 | 1,645.75 | 1.4 | -5.7 | 0.79 | 43558/24530 | not checked |
| 485 | `{"fraction": 0.9, "max_candles": 36, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 4,460.82 | 1.8 | -7.6 | 34.2 | 1,638.50 | 1.4 | -5.7 | 0.79 | 43404/24449 | not checked |
| 454 | `{"fraction": 0.9, "max_candles": 36, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 4,456.74 | 1.8 | -7.6 | 34.2 | 1,637.27 | 1.4 | -5.7 | 0.79 | 43408/24451 | not checked |
| 548 | `{"fraction": 0.9, "max_candles": 40, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 4,454.83 | 1.8 | -7.5 | 34.2 | 1,612.77 | 1.4 | -5.7 | 0.78 | 43322/24383 | not checked |
| 607 | `{"fraction": 0.9, "max_candles": 40, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 4,452.93 | 1.8 | -7.5 | 34.2 | 1,611.12 | 1.4 | -5.7 | 0.78 | 43326/24385 | not checked |
| 657 | `{"fraction": 0.85, "max_candles": 32, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 4,052.70 | 1.6 | -7.1 | 34.4 | 1,430.06 | 1.2 | -5.5 | 0.76 | 40280/22325 | not checked |
| 526 | `{"fraction": 0.85, "max_candles": 40, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 3,997.82 | 1.6 | -7.0 | 34.3 | 1,405.79 | 1.2 | -5.5 | 0.76 | 40082/22196 | not checked |
| 437 | `{"fraction": 0.8, "max_candles": 32, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 3,962.80 | 1.6 | -6.7 | 34.5 | 1,149.97 | 1.0 | -5.5 | 0.62 | 36641/19693 | not checked |
| 445 | `{"fraction": 0.8, "max_candles": 36, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 3,894.87 | 1.6 | -6.7 | 34.5 | 1,154.10 | 1.0 | -5.5 | 0.64 | 36541/19639 | not checked |
| 384 | `{"fraction": 0.8, "max_candles": 32, "stop_atr": 2.5, "take_profit_atr": 6.0}` | 3,715.18 | 1.5 | -6.6 | 34.3 | 1,101.75 | 1.0 | -5.7 | 0.63 | 36719/19730 | not checked |
| 456 | `{"fraction": 0.75, "max_candles": 36, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 3,642.96 | 1.5 | -5.5 | 34.6 | 1,039.61 | 0.9 | -5.2 | 0.61 | 32463/16764 | not checked |
| 559 | `{"fraction": 0.75, "max_candles": 40, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 3,217.63 | 1.3 | -5.4 | 34.3 | 946.24 | 0.8 | -5.4 | 0.62 | 32544/16787 | not checked |

(27 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 709 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
