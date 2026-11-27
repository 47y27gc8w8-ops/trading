# mfi_washout__broad: optimization summary

Updated 2026-11-26T02:08:30Z · backtest.py version `2be84cbca4` · 820 parameter sets tested with this version (865 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [mfi_washout__broad__max-income__v002.md](mfi_washout__broad__max-income__v002.md) | 865 | `{"level": 48, "max_candles": 24, "n": 18, "stop_atr": 4.75, "take_profit_atr": 5.0}` | long LOGN.SW since 2026-11-05 00:00 @ 82.144639; long KNIN.SW since 2026-11-13 00:00 @ 236.57095; long SOON.SW since 2026-11-17 00:00 @ 289.0867; long MMM since 2026-11-23 00:00 @ 182.0546; long ABT since 2026-11-17 00:00 @ 106.53195; long ACN since 2026-11-23 00:00 @ 222.756809; long AMZN since 2026-11-05 00:00 @ 271.511422; long AEP since 2026-11-10 00:00 @ 126.217854; long AMP since 2026-11-24 00:00 @ 490.967253; long AME since 2026-11-11 00:00 @ 243.382991; long APO since 2026-11-11 00:00 @ 122.907259; long AAPL since 2026-11-05 00:00 @ 353.727399; long AZO since 2026-11-13 00:00 @ 3261.81834; long AVY since 2026-11-24 00:00 @ 184.525342; long BALL since 2026-11-19 00:00 @ 64.119228; long BAX since 2026-11-25 00:00 @ 26.808039; long TECH since 2026-10-23 00:00 @ 72.542018; long BRO since 2026-11-17 00:00 @ 72.541753; long CTAS since 2026-11-24 00:00 @ 223.387003; long CTSH since 2026-11-25 00:00 @ 61.498444; long CCI since 2026-11-23 00:00 @ 82.984887; long DXCM since 2026-11-18 00:00 @ 81.694499; long EMR since 2026-11-10 00:00 @ 167.311825; long EOG since 2026-11-09 00:00 @ 145.213549; long EQIX since 2026-10-30 00:00 @ 1032.646298; long ESS since 2026-11-06 00:00 @ 267.130103; long EXPD since 2026-11-20 00:00 @ 195.758707; long FDS since 2026-11-23 00:00 @ 312.32368; long FERG since 2026-10-30 00:00 @ 239.686747; long GIS since 2026-11-23 00:00 @ 34.790433; long GILD since 2026-11-23 00:00 @ 167.26017; long GPN since 2026-11-17 00:00 @ 89.336791; long HCA since 2026-11-05 00:00 @ 515.234541; long DOC since 2026-11-23 00:00 @ 19.425826; long HPQ since 2026-11-05 00:00 @ 30.009; long ILMN since 2026-11-12 00:00 @ 204.471327; long INCY since 2026-10-29 00:00 @ 111.673491; long ISRG since 2026-11-17 00:00 @ 437.461186; long IVZ since 2026-10-28 00:00 @ 28.670502; long JPM since 2026-11-10 00:00 @ 344.063179; long KMB since 2026-11-06 00:00 @ 108.132428; long LYV since 2026-11-13 00:00 @ 181.624478; long LOW since 2026-11-23 00:00 @ 222.77682; long MTB since 2026-11-03 00:00 @ 223.54704; long MAS since 2026-11-19 00:00 @ 83.925172; long MRK since 2026-11-02 00:00 @ 148.864653; long MNST since 2026-11-17 00:00 @ 45.813739; long MCO since 2026-11-24 00:00 @ 480.184021; long NDSN since 2026-11-04 00:00 @ 331.659466; long NXPI since 2026-10-30 00:00 @ 259.607858; long ORLY since 2026-11-25 00:00 @ 95.958779; long OXY since 2026-11-13 00:00 @ 59.0177; long OKE since 2026-11-11 00:00 @ 88.396514; long PFE since 2026-11-17 00:00 @ 28.488544; long PNW since 2026-11-19 00:00 @ 103.691102; long PTC since 2026-11-11 00:00 @ 196.55895; long PHM since 2026-11-23 00:00 @ 125.647684; long QCOM since 2026-11-10 00:00 @ 168.780615; long PWR since 2026-11-04 00:00 @ 627.258128; long RL since 2026-11-10 00:00 @ 399.549822; long RMD since 2026-11-12 00:00 @ 238.851633; long RVTY since 2026-11-04 00:00 @ 167.740309; long SHW since 2026-11-13 00:00 @ 350.485119; long STLD since 2026-11-11 00:00 @ 239.171736; long SNPS since 2026-11-12 00:00 @ 455.396588; long TROW since 2026-11-19 00:00 @ 110.203049; long TRGP since 2026-11-16 00:00 @ 295.628671; long TEL since 2026-11-11 00:00 @ 222.253084; long TMO since 2026-11-18 00:00 @ 680.984263; long WAB since 2026-11-03 00:00 @ 288.80951; long DIS since 2026-11-19 00:00 @ 122.006592; long WSM since 2026-11-19 00:00 @ 243.262959; long WDAY since 2026-11-12 00:00 @ 191.07731; long ZBH since 2026-11-18 00:00 @ 100.980282 |
| balanced | [mfi_washout__broad__balanced__v001.md](mfi_washout__broad__balanced__v001.md) | 580 | `{"level": 24, "max_candles": 24, "n": 14, "stop_atr": 3.25, "take_profit_atr": 3.5}` | long APA since 2026-11-25 00:00 @ 44.763425; long BIIB since 2026-11-23 00:00 @ 250.265059; long CVX since 2026-11-23 00:00 @ 206.0618; long COP since 2026-11-23 00:00 @ 134.650384; long DE since 2026-11-24 00:00 @ 634.270241; long EL since 2026-11-20 00:00 @ 101.27037; long XOM since 2026-11-23 00:00 @ 157.987384; long HAS since 2026-11-24 00:00 @ 112.77382; long IFF since 2026-11-25 00:00 @ 84.925472; long MSFT since 2026-11-19 00:00 @ 519.65585; long NTAP since 2026-11-20 00:00 @ 168.120428; long NSC since 2026-11-24 00:00 @ 315.86472; long PANW since 2026-11-19 00:00 @ 355.916741; long PSX since 2026-11-25 00:00 @ 232.58976; long RL since 2026-11-24 00:00 @ 386.095805; long URI since 2026-11-24 00:00 @ 1020.306; long VLO since 2026-11-10 00:00 @ 346.183811 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 7,088.45 | 3,144.91 | 1,497.87 | 588.95 |
| return % | 70.88 | 31.45 | 14.98 | 5.89 |
| return %/year | 2.6 | 2.5 | 0.7 | 0.5 |
| gross profit | 29,028.04 | 14,379.30 | 6,285.70 | 2,935.16 |
| gross loss | 21,939.59 | 11,234.39 | 4,787.83 | 2,346.22 |
| trades | 33,340 | 19,588 | 8,433 | 4,342 |
| win rate % | 63.6 | 63.3 | 61.9 | 61.0 |
| avg win | 1.37 | 1.16 | 1.20 | 1.11 |
| avg loss | -1.81 | -1.56 | -1.49 | -1.39 |
| avg result / trade | 0.21 | 0.16 | 0.18 | 0.14 |
| largest single loss | -81.77 | -23.45 | -12.24 | -11.62 |
| largest loss % of equity | -10.59 | -34.83 | -15.14 | -37.02 |
| max drawdown | -1,384.16 | -690.67 | -203.44 | -191.53 |
| max drawdown % | -9.86 | -5.72 | -1.89 | -1.85 |
| profit factor | 1.32 | 1.28 | 1.31 | 1.25 |
| unusually bad trades | 3,069 | 1,367 | 406 | 138 |
| … threshold (% of equity) | 8.9 | 10.2 | 11.6 | 12.0 |
| time in market % | 18.2 | 21.2 | 4.4 | 4.4 |
| buy & hold return % | 1,777.75 | 470.42 | 1,777.75 | 470.42 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.98 |  | 0.79 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 5.1 | 1.7 |
| 1996 | 3.0 | 0.6 |
| 1997 | 3.7 | 1.4 |
| 1998 | 0.9 | 0.0 |
| 1999 | 1.9 | -0.2 |
| 2000 | 3.0 | 0.9 |
| 2001 | -2.3 | 0.5 |
| 2002 | -3.6 | -1.1 |
| 2003 | 8.1 | 1.2 |
| 2004 | 4.3 | 1.0 |
| 2005 | 2.5 | 0.5 |
| 2006 | 4.6 | -0.2 |
| 2007 | 2.8 | 0.9 |
| 2008 | -8.5 | -1.0 |
| 2009 | 7.3 | 2.0 |
| 2010 | 6.8 | 1.8 |
| 2011 | 1.7 | 0.8 |
| 2012 | 2.6 | 0.1 |
| 2013 | 10.6 | 2.4 |
| 2014 | 2.5 | 0.5 |
| 2015 | -1.0 | 0.1 |
| 2016 (OOS) | 0.1 | 0.1 |
| 2017 (OOS) | 6.1 | 1.1 |
| 2018 (OOS) | 0.3 | 0.4 |
| 2019 (OOS) | 6.2 | 1.3 |
| 2020 (OOS) | 1.3 | -0.3 |
| 2021 (OOS) | 8.2 | 1.7 |
| 2022 (OOS) | -3.4 | -0.9 |
| 2023 (OOS) | 1.3 | 0.2 |
| 2024 (OOS) | 3.3 | 0.7 |
| 2025 (OOS) | 1.2 | -0.1 |
| 2026 (OOS) | 1.7 | 1.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.9% from a peak in-sample and 5.7% out-of-sample, and the worst single trade cost 34.8% of the account out-of-sample. About 64 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 1.9% from a peak in-sample and 1.9% out-of-sample, and the worst single trade cost 37.0% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

### Range warnings

- max-income: `level` = 48 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 847 | `{"level": 48, "max_candles": 26, "n": 18, "stop_atr": 4.75, "take_profit_atr": 5.0}` | 7,310.79 | 2.6 | -10.0 | 64.2 | 3,194.79 | 2.6 | -5.8 | 0.97 | 32689/19190 | not checked |
| 844 | `{"level": 48, "max_candles": 24, "n": 18, "stop_atr": 4.75, "take_profit_atr": 4.5}` | 7,234.34 | 2.6 | -9.9 | 63.7 | 3,068.72 | 2.5 | -5.6 | 0.95 | 33407/19619 | not checked |
| 864 | `{"level": 48, "max_candles": 24, "n": 24, "stop_atr": 4.75, "take_profit_atr": 4.5}` | 7,144.85 | 2.6 | -8.6 | 62.8 | 3,312.66 | 2.7 | -5.3 | 1.02 | 28018/16598 | not checked |
| 819 | `{"level": 36, "max_candles": 28, "n": 12, "stop_atr": 5.0, "take_profit_atr": 5.5}` | 6,247.57 | 2.3 | -7.6 | 66.7 | 3,015.67 | 2.5 | -6.1 | 1.05 | 28221/15823 | not checked |
| 793 | `{"level": 36, "max_candles": 24, "n": 13, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 5,755.44 | 2.2 | -6.8 | 64.9 | 2,983.38 | 2.4 | -5.4 | 1.11 | 26273/14755 | not checked |
| 701 | `{"level": 36, "max_candles": 24, "n": 12, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 5,314.15 | 2.0 | -6.8 | 64.8 | 2,667.95 | 2.2 | -5.3 | 1.07 | 29523/16536 | not checked |
| 654 | `{"level": 36, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 5,299.74 | 2.0 | -6.5 | 64.5 | 2,607.41 | 2.1 | -5.1 | 1.05 | 29807/16685 | not checked |
| 635 | `{"level": 36, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 5,264.08 | 2.0 | -6.4 | 64.5 | 2,538.90 | 2.1 | -5.1 | 1.03 | 29814/16688 | 1.00 |
| 653 | `{"level": 36, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 5,197.94 | 2.0 | -6.2 | 64.5 | 2,506.16 | 2.1 | -5.1 | 1.03 | 29826/16694 | not checked |
| 723 | `{"level": 36, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 5,038.52 | 2.0 | -6.2 | 64.6 | 2,454.19 | 2.0 | -5.0 | 1.04 | 29856/16708 | not checked |
| 622 | `{"level": 34, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 4,883.68 | 1.9 | -6.2 | 64.4 | 2,271.56 | 1.9 | -4.9 | 0.99 | 26905/14901 | 1.00 |
| 640 | `{"level": 34, "max_candles": 22, "n": 12, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 4,804.65 | 1.9 | -6.0 | 64.1 | 2,199.61 | 1.8 | -4.8 | 0.97 | 27140/15023 | not checked |
| 754 | `{"level": 34, "max_candles": 22, "n": 12, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 4,731.32 | 1.9 | -5.8 | 64.1 | 2,159.84 | 1.8 | -4.8 | 0.97 | 27144/15027 | not checked |
| 684 | `{"level": 32, "max_candles": 26, "n": 11, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,539.98 | 1.8 | -5.8 | 65.5 | 2,117.38 | 1.8 | -5.7 | 0.99 | 26390/14545 | not checked |
| 604 | `{"level": 32, "max_candles": 24, "n": 11, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,514.58 | 1.8 | -5.6 | 65.1 | 2,073.41 | 1.8 | -5.8 | 0.98 | 26538/14636 | not checked |
| 665 | `{"level": 32, "max_candles": 26, "n": 11, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 4,394.64 | 1.8 | -5.5 | 65.0 | 2,054.50 | 1.7 | -5.5 | 0.99 | 26627/14680 | not checked |
| 606 | `{"level": 32, "max_candles": 24, "n": 11, "stop_atr": 3.75, "take_profit_atr": 5.0}` | 4,369.53 | 1.7 | -5.4 | 64.7 | 2,009.57 | 1.7 | -5.5 | 0.98 | 26770/14767 | not checked |
| 586 | `{"level": 32, "max_candles": 24, "n": 11, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 4,327.25 | 1.7 | -5.4 | 64.7 | 1,989.18 | 1.7 | -5.5 | 0.97 | 26779/14770 | 1.00 |
| 605 | `{"level": 32, "max_candles": 24, "n": 11, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 4,256.67 | 1.7 | -5.4 | 64.8 | 1,914.55 | 1.6 | -5.4 | 0.95 | 26796/14778 | not checked |
| 807 | `{"level": 30, "max_candles": 24, "n": 13, "stop_atr": 4.75, "take_profit_atr": 6.5}` | 4,175.60 | 1.7 | -5.3 | 64.9 | 1,911.57 | 1.6 | -5.0 | 0.96 | 17783/9558 | not checked |
| 603 | `{"level": 32, "max_candles": 24, "n": 11, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 4,162.28 | 1.7 | -5.3 | 64.2 | 1,968.25 | 1.7 | -5.2 | 0.99 | 27074/14905 | not checked |
| 690 | `{"level": 30, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 3,691.83 | 1.5 | -5.1 | 64.1 | 1,751.97 | 1.5 | -4.6 | 0.99 | 20821/11249 | not checked |
| 584 | `{"level": 30, "max_candles": 24, "n": 12, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 3,590.05 | 1.5 | -4.8 | 64.2 | 1,669.21 | 1.4 | -4.6 | 0.97 | 20832/11258 | not checked |
| 296 | `{"level": 30, "max_candles": 24, "n": 13, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 3,510.11 | 1.4 | -4.6 | 63.7 | 1,615.57 | 1.4 | -4.1 | 0.96 | 18248/9821 | not checked |
| 694 | `{"level": 28, "max_candles": 22, "n": 12, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 3,131.52 | 1.3 | -4.0 | 63.9 | 1,348.27 | 1.2 | -4.4 | 0.89 | 17920/9444 | not checked |

(50 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 820 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
