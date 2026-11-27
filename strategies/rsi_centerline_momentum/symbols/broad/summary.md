# rsi_centerline_momentum__broad: optimization summary

Updated 2026-11-25T10:11:37Z · backtest.py version `ef016b6df4` · 334 parameter sets tested with this version (334 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [rsi_centerline_momentum__broad__max-income__v001.md](rsi_centerline_momentum__broad__max-income__v001.md) | 333 | `{"level": 53, "max_candles": 60, "n": 25, "stop_atr": 4.0, "take_profit_atr": 6.0}` | long NOVN.SW since 2026-10-15 00:00 @ 123.79713; long ZURN.SW since 2026-10-16 00:00 @ 611.1833; long CFR.SW since 2026-11-11 00:00 @ 176.0528; long SIKA.SW since 2026-10-21 00:00 @ 183.154936; long SREN.SW since 2026-11-24 00:00 @ 151.0453; long GEBN.SW since 2026-10-16 00:00 @ 553.365972; long SLHN.SW since 2026-10-19 00:00 @ 921.476372; long KNIN.SW since 2026-11-12 00:00 @ 234.970464; long MMM since 2026-11-24 00:00 @ 183.815123; long ABT since 2026-10-16 00:00 @ 105.681697; long AFL since 2026-10-15 00:00 @ 119.462563; long A since 2026-11-19 00:00 @ 176.883051; long APD since 2026-10-15 00:00 @ 294.768397; long ALL since 2026-11-11 00:00 @ 258.317462; long AMZN since 2026-11-05 00:00 @ 271.511422; long AEP since 2026-10-19 00:00 @ 126.395544; long AIG since 2026-10-09 00:00 @ 77.353201; long AMT since 2026-10-12 00:00 @ 182.304675; long AMGN since 2026-11-24 00:00 @ 452.315647; long APA since 2026-09-24 00:00 @ 44.129883; long AAPL since 2026-11-05 00:00 @ 353.727399; long ADSK since 2026-10-16 00:00 @ 248.09441; long AVY since 2026-09-03 00:00 @ 175.182544; long BALL since 2026-10-16 00:00 @ 63.379009; long BAX since 2026-11-04 00:00 @ 26.247872; long BLK since 2026-10-16 00:00 @ 1128.238394; long BRO since 2026-10-16 00:00 @ 68.596083; long BXP since 2026-11-05 00:00 @ 66.469932; long CCL since 2026-11-19 00:00 @ 28.778631; long COR since 2026-10-09 00:00 @ 318.992131; long CRL since 2026-11-09 00:00 @ 343.543034; long COP since 2026-11-16 00:00 @ 140.152034; long CSX since 2026-10-23 00:00 @ 51.575469; long DHR since 2026-09-16 00:00 @ 209.361864; long DRI since 2026-10-16 00:00 @ 215.634678; long DAL since 2026-11-03 00:00 @ 83.935177; long DG since 2026-10-30 00:00 @ 132.359703; long D since 2026-10-23 00:00 @ 65.289578; long DHI since 2026-10-23 00:00 @ 145.857708; long EBAY since 2026-09-18 00:00 @ 111.523445; long ECL since 2026-11-24 00:00 @ 304.791422; long EOG since 2026-10-09 00:00 @ 147.33318; long EXPD since 2026-11-13 00:00 @ 196.55895; long FDS since 2026-10-09 00:00 @ 289.376796; long FRT since 2026-11-04 00:00 @ 112.53375; long FDX since 2026-10-28 00:00 @ 306.802004; long FERG since 2026-11-10 00:00 @ 257.737003; long FISV since 2026-11-24 00:00 @ 57.007099; long BEN since 2026-11-05 00:00 @ 34.110228; long GE since 2026-11-05 00:00 @ 328.658566; long GEN since 2026-10-30 00:00 @ 28.510871; long GIS since 2026-11-23 00:00 @ 34.790433; long HIG since 2026-10-19 00:00 @ 134.200252; long HCA since 2026-11-24 00:00 @ 479.513806; long DOC since 2026-11-05 00:00 @ 20.262862; long HSIC since 2026-11-05 00:00 @ 89.706904; long HRL since 2026-11-05 00:00 @ 23.0069; long IDXX since 2026-11-03 00:00 @ 662.458688; long ITW since 2026-10-21 00:00 @ 275.732689; long INCY since 2026-11-02 00:00 @ 119.055703; long J since 2026-10-23 00:00 @ 144.933466; long JNJ since 2026-10-23 00:00 @ 265.899753; long KDP since 2026-11-24 00:00 @ 35.515653; long KMB since 2026-10-16 00:00 @ 104.741412; long LIN since 2026-10-07 00:00 @ 490.687171; long LYV since 2026-10-30 00:00 @ 178.283465; long LMT since 2026-11-10 00:00 @ 587.286118; long L since 2026-10-19 00:00 @ 109.702899; long MA since 2026-11-24 00:00 @ 635.23049; long MDT since 2026-10-13 00:00 @ 92.377703; long MDLZ since 2026-10-13 00:00 @ 62.268675; long MSCI since 2026-11-24 00:00 @ 624.887422; long NDAQ since 2026-11-24 00:00 @ 105.171541; long NXPI since 2026-10-27 00:00 @ 247.444206; long ORLY since 2026-11-03 00:00 @ 90.847246; long OMC since 2026-10-16 00:00 @ 81.824543; long PAYX since 2026-10-21 00:00 @ 110.656593; long PNW since 2026-11-19 00:00 @ 103.691102; long PPG since 2026-10-28 00:00 @ 118.531633; long PGR since 2026-10-09 00:00 @ 217.56525; long PRU since 2026-10-23 00:00 @ 116.825038; long PHM since 2026-10-30 00:00 @ 125.877748; long RL since 2026-10-06 00:00 @ 367.250157; long REG since 2026-11-03 00:00 @ 75.572668; long RMD since 2026-09-16 00:00 @ 227.626875; long RVTY since 2026-11-09 00:00 @ 157.487234; long RCL since 2026-10-07 00:00 @ 285.095513; long RTX since 2026-10-27 00:00 @ 196.594455; long SPGI since 2026-11-24 00:00 @ 451.1353; long SHW since 2026-10-16 00:00 @ 337.42149; long SJM since 2026-10-16 00:00 @ 125.630528; long LUV since 2026-11-03 00:00 @ 44.203256; long SBUX since 2026-10-23 00:00 @ 100.81477; long TTWO since 2026-11-11 00:00 @ 227.558252; long TRGP since 2026-11-13 00:00 @ 300.100013; long TGT since 2026-11-03 00:00 @ 157.131037; long TRV since 2026-11-23 00:00 @ 393.598055; long ULTA since 2026-11-24 00:00 @ 632.019566; long UNP since 2026-10-15 00:00 @ 290.087; long UPS since 2026-10-28 00:00 @ 103.883434; long UHS since 2026-11-05 00:00 @ 200.06; long VTR since 2026-11-05 00:00 @ 90.016995; long VRSN since 2026-11-19 00:00 @ 306.631971; long VRSK since 2026-10-16 00:00 @ 189.826935; long VZ since 2026-11-12 00:00 @ 46.974087; long VRTX since 2026-10-22 00:00 @ 527.338147; long V since 2026-11-24 00:00 @ 409.1227; long VMRK since 2026-10-23 00:00 @ 63.809138; long VMC since 2026-11-24 00:00 @ 280.594163; long WRB since 2026-10-09 00:00 @ 71.961584; long WM since 2026-10-16 00:00 @ 224.847433; long WAT since 2026-11-19 00:00 @ 469.310764; long WELL since 2026-10-16 00:00 @ 236.485689; long WST since 2026-11-24 00:00 @ 398.549522; long WTW since 2026-10-19 00:00 @ 313.654066 |
| balanced | [rsi_centerline_momentum__broad__balanced__v001.md](rsi_centerline_momentum__broad__balanced__v001.md) | 334 | `{"level": 64, "max_candles": 60, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.5}` | long NESN.SW since 2026-11-05 00:00 @ 86.325893; long RO.SW since 2026-10-27 00:00 @ 403.1209; long ZURN.SW since 2026-11-05 00:00 @ 640.592144; long LONN.SW since 2026-10-21 00:00 @ 624.1872; long GIVN.SW since 2026-10-14 00:00 @ 3818.1451; long SREN.SW since 2026-10-16 00:00 @ 149.344793; long SCMN.SW since 2026-11-05 00:00 @ 700.21; long SLHN.SW since 2026-11-05 00:00 @ 987.096028; long KNIN.SW since 2026-09-23 00:00 @ 230.069; long SOON.SW since 2026-11-17 00:00 @ 289.0867; long SGSN.SW since 2026-10-22 00:00 @ 100.380103; long MMM since 2026-11-05 00:00 @ 193.833158; long AOS since 2026-11-05 00:00 @ 67.300183; long AES since 2026-11-17 00:00 @ 14.934479; long A since 2026-10-06 00:00 @ 172.821835; long MO since 2026-10-19 00:00 @ 74.272275; long AEE since 2026-11-10 00:00 @ 113.404014; long AIG since 2026-10-23 00:00 @ 82.434727; long AWK since 2026-11-03 00:00 @ 145.170424; long AMGN since 2026-11-02 00:00 @ 460.906911; long ACGL since 2026-11-03 00:00 @ 109.342791; long AJG since 2026-11-05 00:00 @ 289.0867; long AIZ since 2026-11-05 00:00 @ 313.333962; long AVY since 2026-11-05 00:00 @ 193.317973; long BALL since 2026-10-23 00:00 @ 65.51965; long BDX since 2026-11-23 00:00 @ 213.243947; long TECH since 2026-10-06 00:00 @ 72.522035; long BIIB since 2026-10-23 00:00 @ 251.755497; long BR since 2026-10-23 00:00 @ 184.855443; long CCL since 2026-11-03 00:00 @ 30.155445; long CBOE since 2026-11-11 00:00 @ 363.539022; long CB since 2026-11-05 00:00 @ 378.993669; long CHD since 2026-11-11 00:00 @ 110.55764; long CINF since 2026-11-05 00:00 @ 193.598055; long CTAS since 2026-10-21 00:00 @ 215.630857; long CLX since 2026-11-10 00:00 @ 105.0315; long CME since 2026-10-23 00:00 @ 305.151516; long CL since 2026-10-23 00:00 @ 96.959079; long ED since 2026-10-23 00:00 @ 115.170597; long STZ since 2026-11-05 00:00 @ 146.884048; long CCI since 2026-10-27 00:00 @ 86.52595; long DRI since 2026-11-19 00:00 @ 236.450919; long DLTR since 2026-11-05 00:00 @ 144.613378; long DD since 2026-11-04 00:00 @ 155.286577; long EBAY since 2026-10-16 00:00 @ 123.977184; long ECL since 2026-11-02 00:00 @ 306.081787; long EW since 2026-11-05 00:00 @ 100.700199; long ERIE since 2026-11-06 00:00 @ 280.043979; long EG since 2026-10-23 00:00 @ 407.302147; long EVRG since 2026-11-16 00:00 @ 88.897328; long EXR since 2026-11-02 00:00 @ 151.745507; long FDS since 2026-10-23 00:00 @ 327.86832; long FERG since 2026-11-12 00:00 @ 265.361766; long FISV since 2026-11-04 00:00 @ 60.068014; long GILD since 2026-10-30 00:00 @ 170.301075; long HCA since 2026-10-15 00:00 @ 475.1425; long HD since 2026-11-05 00:00 @ 360.808222; long HST since 2026-10-21 00:00 @ 24.90747; long IDXX since 2026-11-03 00:00 @ 662.458688; long ICE since 2026-11-12 00:00 @ 181.434419; long JKHY since 2026-11-05 00:00 @ 180.464127; long KDP since 2026-11-02 00:00 @ 36.040808; long KIM since 2026-11-03 00:00 @ 24.967487; long KR since 2026-10-23 00:00 @ 67.476602; long LH since 2026-10-29 00:00 @ 356.046784; long LLY since 2026-10-30 00:00 @ 1427.526139; long LMT since 2026-10-26 00:00 @ 613.554006; long LOW since 2026-11-05 00:00 @ 233.580048; long MRSH since 2026-10-23 00:00 @ 198.479524; long MAS since 2026-11-03 00:00 @ 82.767756; long MA since 2026-10-30 00:00 @ 642.622722; long MCD since 2026-11-05 00:00 @ 281.0843; long MTD since 2026-11-09 00:00 @ 1744.323189; long MSI since 2026-11-24 00:00 @ 529.138674; long MSCI since 2026-11-03 00:00 @ 633.989589; long NDAQ since 2026-10-23 00:00 @ 102.730807; long NI since 2026-11-05 00:00 @ 45.933774; long PNW since 2026-10-23 00:00 @ 105.475855; long PPG since 2026-11-03 00:00 @ 124.607368; long PG since 2026-11-10 00:00 @ 169.230747; long PTC since 2026-10-06 00:00 @ 193.0579; long PSA since 2026-11-03 00:00 @ 331.289359; long DGX since 2026-11-10 00:00 @ 258.737602; long REGN since 2026-11-02 00:00 @ 926.553871; long RSG since 2026-10-23 00:00 @ 241.742499; long RVTY since 2026-10-16 00:00 @ 154.417611; long RCL since 2026-11-05 00:00 @ 334.120195; long SPGI since 2026-11-02 00:00 @ 466.759981; long SPG since 2026-11-05 00:00 @ 230.069; long SWK since 2026-11-16 00:00 @ 113.213954; long STE since 2026-11-05 00:00 @ 251.76071; long TMO since 2026-10-06 00:00 @ 683.554981; long TRV since 2026-10-21 00:00 @ 396.61895; long TYL since 2026-10-23 00:00 @ 391.767489; long TSN since 2026-11-05 00:00 @ 60.748219; long ULTA since 2026-10-16 00:00 @ 611.1833; long UPS since 2026-11-05 00:00 @ 112.468926; long VTRS since 2026-11-09 00:00 @ 20.116034; long V since 2026-11-12 00:00 @ 429.468798; long VMC since 2026-11-05 00:00 @ 299.088717; long WRB since 2026-10-19 00:00 @ 74.642389; long GWW since 2026-11-05 00:00 @ 1479.632738; long WMT since 2026-11-02 00:00 @ 124.137228; long DIS since 2026-11-05 00:00 @ 119.905964; long WM since 2026-10-23 00:00 @ 238.321475; long WEC since 2026-11-02 00:00 @ 114.74626; long WST since 2026-11-16 00:00 @ 417.155108; long YUM since 2026-11-05 00:00 @ 167.020092; long ZBH since 2026-11-05 00:00 @ 111.0333 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 9,238.69 | 5,419.93 | 4,685.19 | 3,143.92 |
| return % | 92.39 | 54.20 | 46.85 | 31.44 |
| return %/year | 4.2 | 4.1 | 2.4 | 2.5 |
| gross profit | 31,628.69 | 21,353.02 | 16,694.43 | 11,685.01 |
| gross loss | 22,390.00 | 15,933.09 | 12,009.24 | 8,541.09 |
| trades | 21,706 | 16,423 | 11,830 | 9,432 |
| win rate % | 42.4 | 41.4 | 55.0 | 54.0 |
| avg win | 3.43 | 3.14 | 2.56 | 2.30 |
| avg loss | -1.79 | -1.66 | -2.26 | -1.97 |
| avg result / trade | 0.43 | 0.33 | 0.40 | 0.33 |
| largest single loss | -104.04 | -26.10 | -59.59 | -56.20 |
| largest loss % of equity | -13.51 | -29.95 | -27.39 | -28.34 |
| max drawdown | -1,908.39 | -1,336.69 | -862.43 | -563.69 |
| max drawdown % | -13.44 | -8.99 | -6.72 | -4.56 |
| profit factor | 1.41 | 1.34 | 1.39 | 1.37 |
| unusually bad trades | 1,493 | 866 | 451 | 190 |
| … threshold (% of equity) | 10.2 | 10.2 | 14.2 | 14.1 |
| time in market % | 32.7 | 34.2 | 18.9 | 21.7 |
| buy & hold return % | 705.33 | 470.05 | 705.33 | 470.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.97 |  | 1.04 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 5.1 | 4.0 |
| 2001 | -2.3 | -3.0 |
| 2002 | -4.1 | -1.1 |
| 2003 | 16.1 | 10.1 |
| 2004 | 6.3 | 5.6 |
| 2005 | 5.4 | 1.1 |
| 2006 | 5.2 | 5.1 |
| 2007 | 3.2 | 2.2 |
| 2008 | -9.6 | -3.5 |
| 2009 | 15.9 | 6.4 |
| 2010 | 5.4 | 1.4 |
| 2011 | -1.1 | 0.6 |
| 2012 | 4.5 | 1.3 |
| 2013 | 15.6 | 9.4 |
| 2014 | 5.4 | 1.4 |
| 2015 | -0.3 | -1.0 |
| 2016 (OOS) | 2.8 | 1.1 |
| 2017 (OOS) | 9.5 | 7.3 |
| 2018 (OOS) | -0.8 | -0.1 |
| 2019 (OOS) | 9.3 | 3.8 |
| 2020 (OOS) | 10.0 | 2.6 |
| 2021 (OOS) | 12.1 | 7.5 |
| 2022 (OOS) | -7.5 | -3.6 |
| 2023 (OOS) | 5.1 | 0.9 |
| 2024 (OOS) | 3.0 | 4.5 |
| 2025 (OOS) | -0.7 | 1.9 |
| 2026 (OOS) | 1.0 | 4.7 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 13.4% from a peak in-sample and 9.0% out-of-sample, and the worst single trade cost 29.9% of the account out-of-sample. About 42 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 74% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 6.7% from a peak in-sample and 4.6% out-of-sample, and the worst single trade cost 28.3% of the account out-of-sample. About 55 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 168 | `{"level": 54, "max_candles": 60, "n": 25, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,556.86 | 4.3 | -14.0 | 43.4 | 5,765.60 | 4.3 | -9.4 | 1.00 | 21493/16305 | not checked |
| 173 | `{"level": 53, "max_candles": 60, "n": 25, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 9,238.69 | 4.2 | -13.4 | 42.4 | 5,419.93 | 4.1 | -9.0 | 0.97 | 21706/16423 | 1.00 |
| 166 | `{"level": 53, "max_candles": 60, "n": 26, "stop_atr": 4.0, "take_profit_atr": 6.0}` | 8,894.16 | 4.1 | -13.3 | 43.1 | 5,596.78 | 4.2 | -9.0 | 1.03 | 21164/15992 | not checked |
| 170 | `{"level": 53, "max_candles": 60, "n": 25, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 8,422.71 | 3.9 | -13.2 | 42.9 | 5,389.58 | 4.0 | -8.8 | 1.04 | 22060/16669 | not checked |
| 243 | `{"level": 57, "max_candles": 84, "n": 18, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 8,418.34 | 3.9 | -13.2 | 40.9 | 5,363.98 | 4.0 | -8.0 | 1.03 | 24270/18550 | not checked |
| 273 | `{"level": 59, "max_candles": 156, "n": 18, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 7,240.48 | 3.5 | -12.2 | 43.2 | 4,580.19 | 3.5 | -7.3 | 1.02 | 23773/18166 | not checked |
| 290 | `{"level": 58, "max_candles": 156, "n": 23, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 7,161.46 | 3.4 | -11.6 | 53.3 | 3,958.62 | 3.1 | -7.0 | 0.91 | 23439/18004 | not checked |
| 213 | `{"level": 61, "max_candles": 72, "n": 23, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 6,751.00 | 3.3 | -10.4 | 48.4 | 4,620.89 | 3.5 | -6.8 | 1.08 | 18774/14652 | not checked |
| 292 | `{"level": 62, "max_candles": 156, "n": 23, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 6,524.44 | 3.2 | -9.9 | 51.9 | 4,006.33 | 3.1 | -6.3 | 0.98 | 18055/14134 | not checked |
| 196 | `{"level": 60, "max_candles": 120, "n": 24, "stop_atr": 2.25, "take_profit_atr": 5.5}` | 6,318.95 | 3.1 | -9.8 | 37.8 | 4,323.58 | 3.4 | -6.8 | 1.08 | 19853/15572 | not checked |
| 142 | `{"level": 59, "max_candles": 216, "n": 25, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 5,582.98 | 2.8 | -9.2 | 63.0 | 2,824.10 | 2.3 | -5.9 | 0.82 | 24928/19025 | not checked |
| 251 | `{"level": 63, "max_candles": 60, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 5,384.59 | 2.7 | -7.5 | 55.1 | 3,388.71 | 2.7 | -5.4 | 1.00 | 13297/10603 | not checked |
| 255 | `{"level": 64, "max_candles": 60, "n": 28, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 4,864.85 | 2.5 | -7.1 | 53.4 | 3,208.38 | 2.6 | -4.6 | 1.03 | 11407/9144 | not checked |
| 257 | `{"level": 64, "max_candles": 72, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,731.88 | 2.5 | -6.9 | 53.9 | 3,160.95 | 2.6 | -4.7 | 1.04 | 11747/9359 | not checked |
| 258 | `{"level": 64, "max_candles": 60, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,685.19 | 2.4 | -6.7 | 55.0 | 3,143.92 | 2.5 | -4.6 | 1.04 | 11830/9432 | 1.00 |
| 253 | `{"level": 64, "max_candles": 60, "n": 28, "stop_atr": 3.75, "take_profit_atr": 4.5}` | 4,382.59 | 2.3 | -6.5 | 54.0 | 2,919.22 | 2.4 | -4.7 | 1.03 | 11888/9496 | not checked |
| 254 | `{"level": 64, "max_candles": 60, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 4,156.90 | 2.2 | -6.5 | 57.1 | 2,890.07 | 2.4 | -4.5 | 1.07 | 12314/9831 | not checked |
| 256 | `{"level": 64, "max_candles": 48, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,073.59 | 2.2 | -6.0 | 55.6 | 2,768.96 | 2.3 | -4.9 | 1.05 | 12045/9633 | not checked |
| 252 | `{"level": 65, "max_candles": 60, "n": 28, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 3,640.47 | 2.0 | -5.8 | 54.7 | 2,662.35 | 2.2 | -4.3 | 1.12 | 10316/8362 | not checked |
| 301 | `{"level": 65, "max_candles": 156, "n": 27, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 3,412.91 | 1.9 | -5.7 | 58.2 | 2,501.35 | 2.1 | -4.4 | 1.12 | 11751/9469 | not checked |
| 324 | `{"level": 64, "max_candles": 48, "n": 24, "stop_atr": 1.75, "take_profit_atr": 4.0}` | 1,565.18 | 0.9 | -5.5 | 36.9 | 1,078.19 | 0.9 | -4.5 | 1.04 | 17380/13813 | not checked |
| 191 | `{"level": 64, "max_candles": 84, "n": 26, "stop_atr": 2.0, "take_profit_atr": 3.0}` | 1,234.44 | 0.7 | -5.0 | 44.9 | 699.68 | 0.6 | -4.0 | 0.85 | 16489/13100 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 334 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
