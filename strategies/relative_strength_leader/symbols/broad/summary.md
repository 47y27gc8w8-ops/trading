# relative_strength_leader__broad: optimization summary

Updated 2026-11-25T13:28:43Z · backtest.py version `406b88edda` · 468 parameter sets tested with this version (468 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [relative_strength_leader__broad__max-income__v002.md](relative_strength_leader__broad__max-income__v002.md) | 468 | `{"max_candles": 156, "n": 75, "stop_atr": 4.75, "take_profit_atr": 10.5}` | long SIKA.SW since 2026-06-15 00:00 @ 160.048; long MMM since 2026-10-30 00:00 @ 177.307684; long ABT since 2026-11-02 00:00 @ 106.922066; long AES since 2026-10-30 00:00 @ 14.874461; long AFL since 2026-10-23 00:00 @ 122.100699; long APD since 2026-10-19 00:00 @ 299.659878; long ALL since 2026-10-30 00:00 @ 261.138316; long MO since 2026-10-09 00:00 @ 71.451429; long AMZN since 2026-11-05 00:00 @ 271.511422; long AMCR since 2026-11-17 00:00 @ 43.423023; long AEE since 2026-10-23 00:00 @ 108.862651; long AIG since 2026-10-16 00:00 @ 79.363798; long AMT since 2026-10-12 00:00 @ 182.304675; long AWK since 2026-10-23 00:00 @ 142.18748; long AMGN since 2026-10-08 00:00 @ 407.737974; long APH since 2026-11-24 00:00 @ 76.112823; long ADI since 2026-11-24 00:00 @ 328.0984; long APA since 2026-08-11 00:00 @ 40.29813; long AAPL since 2026-08-31 00:00 @ 319.453155; long ACGL since 2026-10-19 00:00 @ 100.800228; long AJG since 2026-10-19 00:00 @ 252.195631; long AIZ since 2026-10-19 00:00 @ 281.414386; long ADP since 2026-10-09 00:00 @ 271.181336; long AVY since 2026-10-15 00:00 @ 174.862441; long BALL since 2026-10-16 00:00 @ 63.379009; long BAX since 2026-11-04 00:00 @ 26.247872; long BBY since 2026-10-14 00:00 @ 87.126128; long TECH since 2026-11-02 00:00 @ 72.611964; long BIIB since 2026-08-13 00:00 @ 213.04389; long BLK since 2026-10-16 00:00 @ 1128.238394; long BNY since 2026-11-06 00:00 @ 146.583955; long BRO since 2026-11-02 00:00 @ 68.995189; long BF-B since 2026-10-15 00:00 @ 28.638588; long BXP since 2026-11-16 00:00 @ 63.869153; long CAH since 2026-10-14 00:00 @ 240.972264; long CBOE since 2026-10-09 00:00 @ 301.59045; long COR since 2026-10-09 00:00 @ 318.992131; long CVX since 2026-08-11 00:00 @ 191.040739; long CB since 2026-10-15 00:00 @ 356.186811; long CHD since 2026-10-15 00:00 @ 103.973859; long CINF since 2026-10-23 00:00 @ 178.333483; long CTAS since 2026-10-09 00:00 @ 200.331301; long KO since 2026-10-13 00:00 @ 90.587166; long CTSH since 2026-11-23 00:00 @ 58.347501; long CL since 2026-10-15 00:00 @ 93.753179; long COP since 2026-08-11 00:00 @ 121.176012; long ED since 2026-10-15 00:00 @ 110.633273; long CPAY since 2026-11-02 00:00 @ 403.931141; long COST since 2026-10-15 00:00 @ 996.935953; long CSX since 2026-10-23 00:00 @ 51.575469; long DRI since 2026-10-16 00:00 @ 215.634678; long DAL since 2026-11-03 00:00 @ 83.935177; long DXCM since 2026-11-23 00:00 @ 81.374403; long DG since 2026-10-30 00:00 @ 132.359703; long DLTR since 2026-10-29 00:00 @ 128.438514; long D since 2026-11-02 00:00 @ 66.740017; long DUK since 2026-10-23 00:00 @ 124.408972; long EBAY since 2026-10-09 00:00 @ 112.283675; long ECL since 2026-10-14 00:00 @ 284.715394; long EW since 2026-10-23 00:00 @ 90.137034; long EMR since 2026-09-23 00:00 @ 152.490386; long EOG since 2026-11-06 00:00 @ 145.513642; long ESS since 2026-11-16 00:00 @ 275.882728; long EL since 2026-10-05 00:00 @ 94.0282; long EG since 2026-10-16 00:00 @ 380.534139; long EVRG since 2026-10-23 00:00 @ 84.056675; long EXR since 2026-10-23 00:00 @ 143.703102; long FDS since 2026-10-09 00:00 @ 289.376796; long FAST since 2026-10-09 00:00 @ 50.250421; long BEN since 2026-11-05 00:00 @ 34.110228; long GRMN since 2026-11-05 00:00 @ 294.548329; long GEN since 2026-10-30 00:00 @ 28.510871; long GPN since 2026-11-02 00:00 @ 97.459229; long DOC since 2026-11-06 00:00 @ 19.765247; long HSIC since 2026-11-19 00:00 @ 85.225557; long HST since 2026-10-16 00:00 @ 23.967187; long HUM since 2026-10-12 00:00 @ 433.779041; long IEX since 2026-10-26 00:00 @ 231.0693; long ITW since 2026-10-30 00:00 @ 283.685086; long INCY since 2026-11-05 00:00 @ 123.997187; long ICE since 2026-10-30 00:00 @ 166.729997; long IFF since 2026-11-23 00:00 @ 80.364098; long JKHY since 2026-10-23 00:00 @ 160.668181; long J since 2026-10-22 00:00 @ 142.812835; long JNJ since 2026-10-23 00:00 @ 265.899753; long KDP since 2026-10-13 00:00 @ 33.069919; long KMB since 2026-10-19 00:00 @ 104.441327; long KIM since 2026-10-30 00:00 @ 24.557364; long LH since 2026-10-15 00:00 @ 321.696486; long LLY since 2026-10-15 00:00 @ 1233.913097; long LIN since 2026-10-19 00:00 @ 498.119392; long LYV since 2026-10-30 00:00 @ 178.283465; long MAR since 2026-10-13 00:00 @ 370.874645; long MRSH since 2026-10-16 00:00 @ 187.656286; long MAS since 2026-10-21 00:00 @ 74.686293; long MDT since 2026-10-13 00:00 @ 92.377703; long MET since 2026-10-09 00:00 @ 97.55294; long MSFT since 2026-07-31 00:00 @ 448.422956; long MDLZ since 2026-10-30 00:00 @ 65.0195; long MPWR since 2026-11-24 00:00 @ 1281.3843; long MCO since 2026-10-30 00:00 @ 491.003386; long MSCI since 2026-10-21 00:00 @ 588.529389; long NDAQ since 2026-10-21 00:00 @ 95.28858; long NDSN since 2026-07-23 00:00 @ 288.270972; long NUE since 2026-11-17 00:00 @ 256.726989; long OMC since 2026-11-02 00:00 @ 82.674797; long PKG since 2026-10-23 00:00 @ 247.304165; long PANW since 2026-11-20 00:00 @ 359.147721; long PAYX since 2026-11-03 00:00 @ 113.474034; long PFE since 2026-08-07 00:00 @ 25.850424; long PNW since 2026-10-15 00:00 @ 102.679558; long PPG since 2026-10-28 00:00 @ 118.531633; long PFG since 2026-10-30 00:00 @ 113.994187; long PG since 2026-10-09 00:00 @ 149.624654; long PGR since 2026-10-19 00:00 @ 217.005084; long PRU since 2026-11-03 00:00 @ 118.345491; long PSA since 2026-10-23 00:00 @ 310.093; long DGX since 2026-10-15 00:00 @ 235.920761; long REGN since 2026-10-15 00:00 @ 801.753643; long RSG since 2026-10-15 00:00 @ 228.918661; long RMD since 2026-10-08 00:00 @ 225.232794; long RCL since 2026-10-28 00:00 @ 295.688686; long SPGI since 2026-10-19 00:00 @ 423.346967; long SHW since 2026-11-02 00:00 @ 340.176039; long SPG since 2026-10-30 00:00 @ 218.255459; long SWKS since 2026-09-03 00:00 @ 71.171347; long SJM since 2026-10-15 00:00 @ 123.974235; long SO since 2026-10-23 00:00 @ 92.947143; long SWK since 2026-10-21 00:00 @ 95.26857; long SBUX since 2026-10-27 00:00 @ 101.948417; long STE since 2026-10-23 00:00 @ 230.251043; long TRGP since 2026-11-11 00:00 @ 287.026084; long TGT since 2026-11-02 00:00 @ 154.091521; long TRV since 2026-10-14 00:00 @ 370.621163; long UNP since 2026-10-23 00:00 @ 296.839025; long UPS since 2026-10-28 00:00 @ 103.883434; long VRSN since 2026-10-02 00:00 @ 287.140282; long VRSK since 2026-10-16 00:00 @ 189.826935; long VRTX since 2026-10-22 00:00 @ 527.338147; long VTRS since 2026-10-15 00:00 @ 17.755325; long WRB since 2026-10-30 00:00 @ 74.52235; long GWW since 2026-10-21 00:00 @ 1334.999723; long DIS since 2026-10-09 00:00 @ 107.252167; long WM since 2026-10-19 00:00 @ 224.607355; long WAT since 2026-05-29 00:00 @ 367.350162; long WEC since 2026-10-23 00:00 @ 111.164473; long WELL since 2026-11-02 00:00 @ 233.923769; long WST since 2026-09-15 00:00 @ 354.902973; long WTW since 2026-10-23 00:00 @ 330.819217; long ZBH since 2026-10-23 00:00 @ 98.399514 |
| balanced | [relative_strength_leader__broad__balanced__v001.md](relative_strength_leader__broad__balanced__v001.md) | 309 | `{"max_candles": 132, "n": 30, "stop_atr": 3.25, "take_profit_atr": 1.5}` | long LOGN.SW since 2026-11-13 00:00 @ 84.145239; long AMZN since 2026-11-04 00:00 @ 264.899453; long AMCR since 2026-11-17 00:00 @ 43.423023; long APH since 2026-11-24 00:00 @ 76.112823; long AAPL since 2026-11-05 00:00 @ 353.727399; long DXCM since 2026-11-16 00:00 @ 83.485037; long ESS since 2026-11-05 00:00 @ 274.542329; long EXPD since 2026-11-12 00:00 @ 195.788715; long GRMN since 2026-11-05 00:00 @ 294.548329; long GPC since 2026-11-19 00:00 @ 122.666786; long GPN since 2026-11-23 00:00 @ 93.0279; long HSIC since 2026-11-05 00:00 @ 89.706904; long HPQ since 2026-11-23 00:00 @ 28.868659; long INCY since 2026-11-02 00:00 @ 119.055703; long MPWR since 2026-11-24 00:00 @ 1281.3843; long NDSN since 2026-11-10 00:00 @ 320.976269; long NUE since 2026-11-17 00:00 @ 256.726989; long PANW since 2026-11-20 00:00 @ 359.147721; long RMD since 2026-11-05 00:00 @ 244.68466; long RVTY since 2026-11-19 00:00 @ 154.296275; long TSLA since 2026-11-24 00:00 @ 384.005182; long TXN since 2026-11-24 00:00 @ 277.423198; long UHS since 2026-11-23 00:00 @ 178.103418 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 6,583.85 | 3,256.20 | 945.51 | 256.84 |
| return % | 65.84 | 32.56 | 9.46 | 2.57 |
| return %/year | 3.2 | 2.6 | 0.6 | 0.2 |
| gross profit | 20,826.62 | 14,138.44 | 15,626.52 | 10,813.59 |
| gross loss | 14,242.76 | 10,882.24 | 14,681.01 | 10,556.75 |
| trades | 32,740 | 25,865 | 53,428 | 40,331 |
| win rate % | 35.0 | 33.5 | 46.3 | 46.0 |
| avg win | 1.82 | 1.63 | 0.63 | 0.58 |
| avg loss | -0.67 | -0.63 | -0.51 | -0.48 |
| avg result / trade | 0.20 | 0.13 | 0.02 | 0.01 |
| largest single loss | -20.01 | -16.43 | -12.86 | -11.38 |
| largest loss % of equity | -26.70 | -24.26 | -43.22 | -50.04 |
| max drawdown | -910.30 | -846.31 | -396.10 | -441.06 |
| max drawdown % | -7.20 | -6.66 | -3.95 | -4.15 |
| profit factor | 1.46 | 1.30 | 1.06 | 1.02 |
| unusually bad trades | 4,827 | 3,896 | 6,472 | 4,771 |
| … threshold (% of equity) | 3.5 | 3.5 | 3.3 | 3.2 |
| time in market % | 23.5 | 25.4 | 9.4 | 10.0 |
| buy & hold return % | 705.33 | 470.05 | 705.33 | 470.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.82 |  | 0.40 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 2.8 | 0.1 |
| 2001 | -2.3 | -0.9 |
| 2002 | -2.5 | -2.4 |
| 2003 | 10.0 | 4.3 |
| 2004 | 5.2 | 2.2 |
| 2005 | 3.5 | -0.6 |
| 2006 | 3.8 | 0.4 |
| 2007 | 2.0 | 0.5 |
| 2008 | -4.3 | -2.3 |
| 2009 | 8.1 | 3.4 |
| 2010 | 5.8 | 1.0 |
| 2011 | -0.2 | -0.3 |
| 2012 | 4.8 | 1.0 |
| 2013 | 12.1 | 3.7 |
| 2014 | 5.2 | 0.2 |
| 2015 | -1.1 | -0.9 |
| 2016 (OOS) | 2.2 | 0.2 |
| 2017 (OOS) | 6.1 | 1.3 |
| 2018 (OOS) | -1.0 | -1.1 |
| 2019 (OOS) | 5.2 | 2.2 |
| 2020 (OOS) | 2.1 | 0.5 |
| 2021 (OOS) | 9.1 | 2.8 |
| 2022 (OOS) | -4.4 | -1.9 |
| 2023 (OOS) | 2.4 | -0.7 |
| 2024 (OOS) | 5.5 | 0.1 |
| 2025 (OOS) | 0.2 | -1.0 |
| 2026 (OOS) | 0.3 | -0.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 7.2% from a peak in-sample and 6.7% out-of-sample, and the worst single trade cost 24.3% of the account out-of-sample. About 35 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.0% from a peak in-sample and 4.2% out-of-sample, and the worst single trade cost 50.0% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 0.2% a year against 0.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 404 | `{"max_candles": 156, "n": 70, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 6,774.41 | 3.3 | -7.2 | 35.1 | 3,327.30 | 2.7 | -6.7 | 0.81 | 33939/26522 | not checked |
| 455 | `{"max_candles": 156, "n": 70, "stop_atr": 5.25, "take_profit_atr": 10.0}` | 6,587.37 | 3.2 | -7.1 | 35.2 | 3,192.22 | 2.6 | -6.5 | 0.80 | 33938/26522 | not checked |
| 458 | `{"max_candles": 180, "n": 75, "stop_atr": 5.25, "take_profit_atr": 10.0}` | 6,467.41 | 3.2 | -6.9 | 35.0 | 3,185.02 | 2.6 | -6.4 | 0.81 | 32739/25865 | not checked |
| 448 | `{"max_candles": 144, "n": 75, "stop_atr": 5.25, "take_profit_atr": 10.0}` | 6,453.66 | 3.2 | -6.9 | 35.0 | 3,182.71 | 2.6 | -6.4 | 0.81 | 32739/25865 | not checked |
| 437 | `{"max_candles": 120, "n": 75, "stop_atr": 5.25, "take_profit_atr": 10.0}` | 6,448.04 | 3.2 | -6.8 | 35.0 | 3,183.26 | 2.6 | -6.3 | 0.81 | 32739/25865 | not checked |
| 419 | `{"max_candles": 192, "n": 70, "stop_atr": 5.75, "take_profit_atr": 8.5}` | 6,026.18 | 3.0 | -6.6 | 35.3 | 3,005.65 | 2.4 | -6.0 | 0.82 | 33937/26522 | not checked |
| 460 | `{"max_candles": 132, "n": 80, "stop_atr": 5.25, "take_profit_atr": 8.5}` | 5,819.80 | 2.9 | -6.4 | 35.2 | 2,815.92 | 2.3 | -6.1 | 0.79 | 31581/25251 | not checked |
| 451 | `{"max_candles": 156, "n": 85, "stop_atr": 4.25, "take_profit_atr": 8.5}` | 5,464.43 | 2.8 | -6.3 | 34.8 | 2,955.59 | 2.4 | -5.7 | 0.87 | 30732/24813 | not checked |
| 431 | `{"max_candles": 120, "n": 75, "stop_atr": 3.75, "take_profit_atr": 8.0}` | 5,403.61 | 2.7 | -6.3 | 35.0 | 2,835.15 | 2.3 | -5.8 | 0.85 | 32740/25865 | not checked |
| 436 | `{"max_candles": 156, "n": 75, "stop_atr": 4.75, "take_profit_atr": 7.5}` | 5,276.74 | 2.7 | -6.2 | 35.2 | 2,579.72 | 2.1 | -5.8 | 0.79 | 32740/25865 | not checked |
| 421 | `{"max_candles": 120, "n": 85, "stop_atr": 4.75, "take_profit_atr": 8.0}` | 5,252.68 | 2.7 | -6.0 | 34.9 | 2,842.07 | 2.3 | -5.8 | 0.87 | 30732/24813 | not checked |
| 462 | `{"max_candles": 144, "n": 85, "stop_atr": 5.25, "take_profit_atr": 7.5}` | 4,982.39 | 2.6 | -5.9 | 35.0 | 2,700.64 | 2.2 | -5.5 | 0.87 | 30731/24813 | not checked |
| 348 | `{"max_candles": 84, "n": 75, "stop_atr": 3.75, "take_profit_atr": 7.0}` | 4,897.59 | 2.5 | -5.8 | 35.2 | 2,490.32 | 2.1 | -5.5 | 0.82 | 32740/25865 | not checked |
| 434 | `{"max_candles": 72, "n": 75, "stop_atr": 5.75, "take_profit_atr": 6.0}` | 4,494.67 | 2.4 | -5.2 | 35.7 | 2,137.36 | 1.8 | -5.5 | 0.77 | 32738/25865 | not checked |
| 443 | `{"max_candles": 168, "n": 75, "stop_atr": 5.75, "take_profit_atr": 5.0}` | 3,800.54 | 2.0 | -5.2 | 36.3 | 1,873.15 | 1.6 | -5.0 | 0.78 | 32738/25865 | not checked |
| 442 | `{"max_candles": 84, "n": 90, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 3,537.76 | 1.9 | -5.1 | 35.5 | 2,012.33 | 1.7 | -5.2 | 0.89 | 29964/24251 | not checked |
| 156 | `{"max_candles": 84, "n": 90, "stop_atr": 2.5, "take_profit_atr": 5.0}` | 2,979.29 | 1.6 | -5.0 | 35.3 | 1,792.51 | 1.5 | -4.5 | 0.93 | 29964/24251 | not checked |
| 294 | `{"max_candles": 120, "n": 90, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 2,731.68 | 1.5 | -4.9 | 36.1 | 1,664.66 | 1.4 | -4.6 | 0.93 | 29964/24251 | not checked |
| 357 | `{"max_candles": 144, "n": 85, "stop_atr": 3.0, "take_profit_atr": 4.0}` | 2,548.51 | 1.4 | -4.7 | 36.8 | 1,453.65 | 1.2 | -4.1 | 0.87 | 30732/24813 | not checked |
| 256 | `{"max_candles": 168, "n": 75, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 2,446.64 | 1.4 | -4.7 | 37.8 | 1,158.25 | 1.0 | -4.3 | 0.73 | 32740/25865 | not checked |
| 215 | `{"max_candles": 60, "n": 75, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 2,436.90 | 1.4 | -4.6 | 37.8 | 1,164.86 | 1.0 | -4.1 | 0.74 | 32740/25865 | not checked |
| 255 | `{"max_candles": 120, "n": 85, "stop_atr": 3.0, "take_profit_atr": 3.5}` | 2,242.96 | 1.3 | -4.6 | 37.6 | 1,159.67 | 1.0 | -3.9 | 0.80 | 30732/24813 | not checked |
| 293 | `{"max_candles": 156, "n": 95, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 2,095.78 | 1.2 | -4.6 | 37.6 | 907.87 | 0.8 | -4.3 | 0.67 | 29150/23989 | not checked |
| 262 | `{"max_candles": 180, "n": 90, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 2,079.13 | 1.2 | -4.4 | 37.5 | 1,077.91 | 0.9 | -4.1 | 0.79 | 29964/24251 | not checked |
| 146 | `{"max_candles": 144, "n": 95, "stop_atr": 3.5, "take_profit_atr": 3.0}` | 1,608.97 | 0.9 | -4.3 | 38.5 | 681.26 | 0.6 | -3.6 | 0.65 | 29150/23989 | not checked |

(9 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 468 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
