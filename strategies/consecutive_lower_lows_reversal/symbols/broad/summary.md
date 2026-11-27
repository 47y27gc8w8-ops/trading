# consecutive_lower_lows_reversal__broad: optimization summary

Updated 2026-11-25T15:06:48Z · backtest.py version `be254b3860` · 641 parameter sets tested with this version (641 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [consecutive_lower_lows_reversal__broad__max-income__v002.md](consecutive_lower_lows_reversal__broad__max-income__v002.md) | 640 | `{"max_bars": 34, "n": 1, "stop_atr": 7.0, "take_profit_atr": 3.5}` | long UBSG.SW since 2026-11-11 00:00 @ 40.872259; long SIKA.SW since 2026-11-24 00:00 @ 186.505932; long GIVN.SW since 2026-11-12 00:00 @ 4101.23; long HOLN.SW since 2026-11-17 00:00 @ 74.702404; long SREN.SW since 2026-11-11 00:00 @ 150.045; long GEBN.SW since 2026-11-24 00:00 @ 585.1755; long KNIN.SW since 2026-11-12 00:00 @ 234.970464; long SGSN.SW since 2026-11-05 00:00 @ 104.231257; long SAP since 2026-11-10 00:00 @ 236.480927; long MMM since 2026-11-10 00:00 @ 187.89635; long AMD since 2026-11-19 00:00 @ 542.332634; long A since 2026-11-24 00:00 @ 187.016095; long APD since 2026-11-10 00:00 @ 310.022972; long LNT since 2026-11-10 00:00 @ 73.161941; long AMZN since 2026-11-19 00:00 @ 272.641766; long AEP since 2026-11-10 00:00 @ 126.217854; long AMT since 2026-11-23 00:00 @ 184.53534; long AWK since 2026-11-23 00:00 @ 147.134123; long AMP since 2026-11-10 00:00 @ 534.470291; long AMGN since 2026-11-10 00:00 @ 463.164559; long APH since 2026-11-24 00:00 @ 76.112823; long ADI since 2026-11-10 00:00 @ 388.816622; long AON since 2026-11-23 00:00 @ 331.0993; long APA since 2026-11-12 00:00 @ 47.194154; long ACGL since 2026-11-23 00:00 @ 107.542255; long ATO since 2026-11-12 00:00 @ 177.423206; long ADSK since 2026-11-24 00:00 @ 254.946456; long AZO since 2026-11-13 00:00 @ 3261.81834; long AVY since 2026-11-10 00:00 @ 187.546252; long BALL since 2026-11-10 00:00 @ 66.429927; long TECH since 2026-11-24 00:00 @ 72.78183; long BLK since 2026-11-24 00:00 @ 1135.3405; long BX since 2026-11-10 00:00 @ 123.0369; long BNY since 2026-11-24 00:00 @ 145.0435; long BXP since 2026-11-17 00:00 @ 63.589071; long CDNS since 2026-11-05 00:00 @ 322.136621; long CNC since 2026-11-12 00:00 @ 70.771225; long CRL since 2026-11-09 00:00 @ 343.543034; long CVX since 2026-11-12 00:00 @ 213.293273; long CB since 2026-11-23 00:00 @ 369.730881; long CHD since 2026-11-23 00:00 @ 109.522845; long CI since 2026-11-11 00:00 @ 300.82023; long CTAS since 2026-11-12 00:00 @ 229.593074; long CSCO since 2026-10-22 00:00 @ 106.802028; long KO since 2026-11-23 00:00 @ 94.628378; long CTSH since 2026-11-05 00:00 @ 66.792588; long CL since 2026-11-23 00:00 @ 95.228557; long COP since 2026-11-12 00:00 @ 137.785037; long STZ since 2026-11-23 00:00 @ 140.042; long CPRT since 2026-11-10 00:00 @ 32.189654; long COST since 2026-11-23 00:00 @ 1090.467057; long CVS since 2026-11-04 00:00 @ 85.325593; long DHR since 2026-11-05 00:00 @ 237.521232; long DE since 2026-11-24 00:00 @ 634.270241; long DXCM since 2026-11-13 00:00 @ 82.034605; long DG since 2026-11-17 00:00 @ 135.270565; long DOV since 2026-11-10 00:00 @ 211.703491; long DUK since 2026-11-23 00:00 @ 128.688589; long ETN since 2026-10-22 00:00 @ 378.910376; long EBAY since 2026-11-19 00:00 @ 121.436422; long ECL since 2026-11-10 00:00 @ 305.781709; long EW since 2026-11-24 00:00 @ 104.961479; long EMR since 2026-11-05 00:00 @ 166.514439; long EFX since 2026-11-12 00:00 @ 189.456814; long ESS since 2026-11-19 00:00 @ 272.451706; long EL since 2026-11-24 00:00 @ 103.561058; long EXPD since 2026-11-10 00:00 @ 188.306475; long XOM since 2026-11-12 00:00 @ 167.244829; long FDS since 2026-11-12 00:00 @ 337.87132; long FRT since 2026-11-10 00:00 @ 113.113926; long FDX since 2026-11-10 00:00 @ 318.465506; long FERG since 2026-11-24 00:00 @ 250.655176; long FITB since 2026-11-10 00:00 @ 54.536356; long BEN since 2026-11-24 00:00 @ 33.249974; long GRMN since 2026-11-24 00:00 @ 275.982764; long IT since 2026-11-12 00:00 @ 194.0582; long GEN since 2026-11-12 00:00 @ 30.483321; long GD since 2026-11-10 00:00 @ 362.018577; long GM since 2026-11-10 00:00 @ 88.836641; long GPC since 2026-10-23 00:00 @ 125.697702; long GILD since 2026-11-10 00:00 @ 170.201039; long GPN since 2026-11-23 00:00 @ 93.0279; long HIG since 2026-11-11 00:00 @ 136.410906; long HCA since 2026-11-23 00:00 @ 474.132187; long HSIC since 2026-11-19 00:00 @ 85.225557; long HD since 2026-11-10 00:00 @ 349.60485; long HST since 2026-11-10 00:00 @ 25.217562; long HPQ since 2026-11-05 00:00 @ 30.009; long IBM since 2026-11-05 00:00 @ 254.238881; long ITW since 2026-11-10 00:00 @ 286.305867; long ILMN since 2026-11-04 00:00 @ 241.0723; long INCY since 2026-11-10 00:00 @ 120.616176; long IFF since 2026-11-10 00:00 @ 83.455029; long IVZ since 2026-11-24 00:00 @ 28.0084; long JKHY since 2026-11-11 00:00 @ 173.121928; long J since 2026-11-10 00:00 @ 155.646686; long JPM since 2026-11-10 00:00 @ 344.063179; long KDP since 2026-11-23 00:00 @ 34.720412; long KEY since 2026-11-10 00:00 @ 21.486444; long KIM since 2026-11-17 00:00 @ 25.827746; long KKR since 2026-11-11 00:00 @ 100.82; long LEN since 2026-11-10 00:00 @ 89.966984; long LIN since 2026-11-24 00:00 @ 515.724678; long LYV since 2026-11-24 00:00 @ 180.644173; long LMT since 2026-11-10 00:00 @ 587.286118; long MPC since 2026-11-10 00:00 @ 377.191751; long MAS since 2026-11-10 00:00 @ 85.165541; long MRK since 2026-11-10 00:00 @ 148.444514; long MTD since 2026-11-24 00:00 @ 1731.049188; long MSFT since 2026-11-10 00:00 @ 542.095673; long MDLZ since 2026-11-23 00:00 @ 65.579666; long MPWR since 2026-11-24 00:00 @ 1281.3843; long MCO since 2026-11-10 00:00 @ 509.827868; long NTAP since 2026-10-22 00:00 @ 214.194244; long NDSN since 2026-11-03 00:00 @ 328.998664; long NSC since 2026-11-10 00:00 @ 326.397878; long NUE since 2026-11-12 00:00 @ 263.0789; long NXPI since 2026-11-24 00:00 @ 246.373893; long OXY since 2026-11-02 00:00 @ 62.708806; long OMC since 2026-11-19 00:00 @ 87.686302; long OKE since 2026-11-11 00:00 @ 88.396514; long PFE since 2026-11-12 00:00 @ 29.758925; long PSX since 2026-11-10 00:00 @ 245.126543; long PNC since 2026-11-10 00:00 @ 232.309677; long PPG since 2026-11-10 00:00 @ 123.987182; long PPL since 2026-11-06 00:00 @ 36.260875; long PFG since 2026-11-10 00:00 @ 115.584668; long PG since 2026-11-23 00:00 @ 167.57026; long PGR since 2026-11-23 00:00 @ 229.198744; long PRU since 2026-11-10 00:00 @ 122.606771; long PHM since 2026-11-10 00:00 @ 133.810135; long RL since 2026-11-24 00:00 @ 386.095805; long RJF since 2026-11-10 00:00 @ 168.640573; long REG since 2026-11-11 00:00 @ 76.462934; long REGN since 2026-11-10 00:00 @ 914.682465; long RF since 2026-11-10 00:00 @ 29.0087; long RVTY since 2026-11-04 00:00 @ 167.740309; long ROP since 2026-11-12 00:00 @ 482.434696; long ROST since 2026-11-10 00:00 @ 237.0711; long RCL since 2026-11-19 00:00 @ 319.385796; long RTX since 2026-11-10 00:00 @ 195.478357; long SPGI since 2026-11-10 00:00 @ 470.761181; long CRM since 2026-11-05 00:00 @ 229.128716; long SHW since 2026-11-10 00:00 @ 355.306054; long SJM since 2026-11-23 00:00 @ 131.229359; long SWK since 2026-11-10 00:00 @ 116.815033; long SBUX since 2026-11-17 00:00 @ 107.652289; long STT since 2026-11-24 00:00 @ 160.048; long TROW since 2026-11-10 00:00 @ 110.553153; long TRGP since 2026-11-11 00:00 @ 287.026084; long TEL since 2026-11-10 00:00 @ 217.58897; long TSLA since 2026-11-19 00:00 @ 390.026977; long TXN since 2026-11-10 00:00 @ 288.986664; long TT since 2026-10-22 00:00 @ 467.200116; long TRV since 2026-11-13 00:00 @ 406.862012; long TFC since 2026-11-10 00:00 @ 50.028229; long TYL since 2026-11-12 00:00 @ 429.258744; long USB since 2026-11-10 00:00 @ 60.918272; long UNP since 2026-11-10 00:00 @ 297.709281; long UAL since 2026-11-24 00:00 @ 106.541955; long UPS since 2026-11-10 00:00 @ 108.831681; long URI since 2026-11-10 00:00 @ 1125.447518; long UHS since 2026-11-10 00:00 @ 198.589558; long VLO since 2026-11-02 00:00 @ 392.797797; long VZ since 2026-11-23 00:00 @ 46.283881; long VRTX since 2026-11-10 00:00 @ 547.134062; long VMC since 2026-11-10 00:00 @ 287.596263; long WRB since 2026-11-23 00:00 @ 77.603276; long WAB since 2026-11-24 00:00 @ 281.594463; long WAT since 2026-11-10 00:00 @ 470.141; long WFC since 2026-11-10 00:00 @ 85.855751; long WELL since 2026-11-19 00:00 @ 245.343585; long WSM since 2026-11-10 00:00 @ 258.467532; long WDAY since 2026-11-05 00:00 @ 204.841433; long ZBRA since 2026-11-12 00:00 @ 324.027172; long ZBH since 2026-11-10 00:00 @ 108.522545 |
| balanced | [consecutive_lower_lows_reversal__broad__balanced__v002.md](consecutive_lower_lows_reversal__broad__balanced__v002.md) | 641 | `{"max_bars": 32, "n": 2, "stop_atr": 6.75, "take_profit_atr": 2.5}` | long UBSG.SW since 2026-11-24 00:00 @ 38.0114; long SIKA.SW since 2026-11-24 00:00 @ 186.505932; long SREN.SW since 2026-11-11 00:00 @ 150.045; long GEBN.SW since 2026-11-24 00:00 @ 585.1755; long KNIN.SW since 2026-11-12 00:00 @ 234.970464; long SGSN.SW since 2026-11-05 00:00 @ 104.231257; long MMM since 2026-11-10 00:00 @ 187.89635; long AMD since 2026-11-19 00:00 @ 542.332634; long APD since 2026-11-10 00:00 @ 310.022972; long AMZN since 2026-11-19 00:00 @ 272.641766; long AMT since 2026-11-23 00:00 @ 184.53534; long AWK since 2026-11-23 00:00 @ 147.134123; long AMGN since 2026-11-10 00:00 @ 463.164559; long ADI since 2026-11-10 00:00 @ 388.816622; long AON since 2026-11-23 00:00 @ 331.0993; long ACGL since 2026-11-23 00:00 @ 107.542255; long ADSK since 2026-11-24 00:00 @ 254.946456; long AZO since 2026-11-13 00:00 @ 3261.81834; long AVY since 2026-11-10 00:00 @ 187.546252; long BLK since 2026-11-24 00:00 @ 1135.3405; long BX since 2026-11-10 00:00 @ 123.0369; long BNY since 2026-11-24 00:00 @ 145.0435; long CDNS since 2026-11-10 00:00 @ 330.289059; long CNC since 2026-11-12 00:00 @ 70.771225; long CRL since 2026-11-09 00:00 @ 343.543034; long CVX since 2026-11-12 00:00 @ 213.293273; long CB since 2026-11-23 00:00 @ 369.730881; long CHD since 2026-11-23 00:00 @ 109.522845; long CI since 2026-11-11 00:00 @ 300.82023; long CSCO since 2026-10-22 00:00 @ 106.802028; long KO since 2026-11-23 00:00 @ 94.628378; long CTSH since 2026-11-11 00:00 @ 63.96644; long CL since 2026-11-23 00:00 @ 95.228557; long COP since 2026-11-12 00:00 @ 137.785037; long STZ since 2026-11-23 00:00 @ 140.042; long CPRT since 2026-11-10 00:00 @ 32.189654; long COST since 2026-11-23 00:00 @ 1090.467057; long DHR since 2026-11-05 00:00 @ 237.521232; long DE since 2026-11-24 00:00 @ 634.270241; long DXCM since 2026-11-13 00:00 @ 82.034605; long DG since 2026-11-17 00:00 @ 135.270565; long DOV since 2026-11-10 00:00 @ 211.703491; long DUK since 2026-11-23 00:00 @ 128.688589; long EBAY since 2026-11-19 00:00 @ 121.436422; long ECL since 2026-11-10 00:00 @ 305.781709; long EMR since 2026-11-24 00:00 @ 156.807023; long EL since 2026-11-24 00:00 @ 103.561058; long EXPD since 2026-11-10 00:00 @ 188.306475; long XOM since 2026-11-12 00:00 @ 167.244829; long FDS since 2026-11-12 00:00 @ 337.87132; long FDX since 2026-11-10 00:00 @ 318.465506; long FERG since 2026-11-24 00:00 @ 250.655176; long FITB since 2026-11-10 00:00 @ 54.536356; long BEN since 2026-11-24 00:00 @ 33.249974; long GRMN since 2026-11-24 00:00 @ 275.982764; long GEN since 2026-11-12 00:00 @ 30.483321; long GD since 2026-11-10 00:00 @ 362.018577; long GM since 2026-11-10 00:00 @ 88.836641; long GPC since 2026-10-23 00:00 @ 125.697702; long GILD since 2026-11-10 00:00 @ 170.201039; long GPN since 2026-11-23 00:00 @ 93.0279; long HIG since 2026-11-11 00:00 @ 136.410906; long HCA since 2026-11-23 00:00 @ 474.132187; long HSIC since 2026-11-19 00:00 @ 85.225557; long HST since 2026-11-10 00:00 @ 25.217562; long HPQ since 2026-11-12 00:00 @ 29.198758; long IBM since 2026-11-05 00:00 @ 254.238881; long ITW since 2026-11-10 00:00 @ 286.305867; long ILMN since 2026-11-04 00:00 @ 241.0723; long IFF since 2026-11-24 00:00 @ 82.634784; long IVZ since 2026-11-24 00:00 @ 28.0084; long JBL since 2026-10-12 00:00 @ 303.665535; long JKHY since 2026-11-11 00:00 @ 173.121928; long J since 2026-11-10 00:00 @ 155.646686; long JPM since 2026-11-10 00:00 @ 344.063179; long KDP since 2026-11-23 00:00 @ 34.720412; long KEY since 2026-11-10 00:00 @ 21.486444; long LMT since 2026-11-10 00:00 @ 587.286118; long MPC since 2026-11-10 00:00 @ 377.191751; long MAS since 2026-11-10 00:00 @ 85.165541; long MSFT since 2026-11-10 00:00 @ 542.095673; long MDLZ since 2026-11-23 00:00 @ 65.579666; long MCO since 2026-11-10 00:00 @ 509.827868; long NTAP since 2026-11-24 00:00 @ 167.360191; long NDSN since 2026-11-10 00:00 @ 320.976269; long NSC since 2026-11-10 00:00 @ 326.397878; long NUE since 2026-11-24 00:00 @ 244.923461; long OXY since 2026-11-11 00:00 @ 57.277176; long OKE since 2026-11-11 00:00 @ 88.396514; long PSX since 2026-11-10 00:00 @ 245.126543; long PNC since 2026-11-10 00:00 @ 232.309677; long PPG since 2026-11-10 00:00 @ 123.987182; long PFG since 2026-11-10 00:00 @ 115.584668; long PG since 2026-11-23 00:00 @ 167.57026; long PGR since 2026-11-23 00:00 @ 229.198744; long PHM since 2026-11-23 00:00 @ 125.647684; long RL since 2026-11-24 00:00 @ 386.095805; long RJF since 2026-11-10 00:00 @ 168.640573; long REG since 2026-11-11 00:00 @ 76.462934; long REGN since 2026-11-10 00:00 @ 914.682465; long RF since 2026-11-10 00:00 @ 29.0087; long RVTY since 2026-11-04 00:00 @ 167.740309; long ROP since 2026-11-12 00:00 @ 482.434696; long ROST since 2026-11-10 00:00 @ 237.0711; long RCL since 2026-11-19 00:00 @ 319.385796; long RTX since 2026-11-10 00:00 @ 195.478357; long SPGI since 2026-11-10 00:00 @ 470.761181; long CRM since 2026-11-05 00:00 @ 229.128716; long SHW since 2026-11-10 00:00 @ 355.306054; long SJM since 2026-11-23 00:00 @ 131.229359; long SWK since 2026-11-24 00:00 @ 109.352796; long SBUX since 2026-11-17 00:00 @ 107.652289; long STT since 2026-11-24 00:00 @ 160.048; long TRGP since 2026-11-11 00:00 @ 287.026084; long TEL since 2026-11-10 00:00 @ 217.58897; long TSLA since 2026-11-19 00:00 @ 390.026977; long TXN since 2026-11-10 00:00 @ 288.986664; long TT since 2026-10-27 00:00 @ 461.788489; long TRV since 2026-11-23 00:00 @ 393.598055; long TFC since 2026-11-10 00:00 @ 50.028229; long TYL since 2026-11-12 00:00 @ 429.258744; long USB since 2026-11-10 00:00 @ 60.918272; long UNP since 2026-11-10 00:00 @ 297.709281; long UAL since 2026-11-24 00:00 @ 106.541955; long URI since 2026-11-10 00:00 @ 1125.447518; long VLO since 2026-11-02 00:00 @ 392.797797; long VZ since 2026-11-23 00:00 @ 46.283881; long VRTX since 2026-11-24 00:00 @ 542.402662; long VMC since 2026-11-10 00:00 @ 287.596263; long WAB since 2026-11-24 00:00 @ 281.594463; long WAT since 2026-11-10 00:00 @ 470.141; long WFC since 2026-11-10 00:00 @ 85.855751; long WSM since 2026-11-10 00:00 @ 258.467532 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 7,662.77 | 2,400.93 | 5,468.80 | 1,351.65 |
| return % | 76.63 | 24.01 | 54.69 | 13.52 |
| return %/year | 2.8 | 2.0 | 2.1 | 1.2 |
| gross profit | 31,693.26 | 14,102.07 | 21,860.00 | 9,816.47 |
| gross loss | 24,030.48 | 11,701.13 | 16,391.20 | 8,464.82 |
| trades | 57,821 | 34,550 | 41,954 | 24,826 |
| win rate % | 73.3 | 72.1 | 73.6 | 71.9 |
| avg win | 0.75 | 0.57 | 0.71 | 0.55 |
| avg loss | -1.56 | -1.21 | -1.48 | -1.21 |
| avg result / trade | 0.13 | 0.07 | 0.13 | 0.05 |
| largest single loss | -99.97 | -21.68 | -54.01 | -13.53 |
| largest loss % of equity | -64.79 | -35.31 | -54.24 | -42.52 |
| max drawdown | -1,328.86 | -1,424.10 | -880.44 | -1,178.48 |
| max drawdown % | -9.03 | -12.17 | -6.60 | -10.47 |
| profit factor | 1.32 | 1.21 | 1.33 | 1.16 |
| unusually bad trades | 5,161 | 3,134 | 3,708 | 2,266 |
| … threshold (% of equity) | 4.5 | 4.7 | 5.0 | 5.2 |
| time in market % | 18.3 | 21.0 | 13.5 | 15.6 |
| buy & hold return % | 1,777.05 | 470.05 | 1,777.05 | 470.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.73 |  | 0.56 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 5.4 | 3.6 |
| 1996 | 3.4 | 2.4 |
| 1997 | 3.9 | 2.6 |
| 1998 | 2.3 | 1.4 |
| 1999 | 3.4 | 2.4 |
| 2000 | 4.7 | 4.2 |
| 2001 | -1.9 | -0.8 |
| 2002 | -5.0 | -4.1 |
| 2003 | 9.9 | 7.2 |
| 2004 | 3.2 | 2.9 |
| 2005 | 1.7 | 1.8 |
| 2006 | 3.9 | 2.7 |
| 2007 | 4.6 | 3.0 |
| 2008 | -8.1 | -5.8 |
| 2009 | 10.1 | 8.6 |
| 2010 | 2.4 | 1.4 |
| 2011 | 1.1 | 1.2 |
| 2012 | 4.5 | 3.2 |
| 2013 | 6.2 | 4.9 |
| 2014 | 2.1 | 1.4 |
| 2015 | 1.1 | 0.8 |
| 2016 (OOS) | 1.7 | 1.9 |
| 2017 (OOS) | 5.0 | 3.6 |
| 2018 (OOS) | 2.4 | 1.3 |
| 2019 (OOS) | 5.8 | 4.2 |
| 2020 (OOS) | -3.8 | -5.2 |
| 2021 (OOS) | 6.9 | 4.8 |
| 2022 (OOS) | -4.4 | -3.5 |
| 2023 (OOS) | 3.4 | 2.4 |
| 2024 (OOS) | 3.5 | 2.2 |
| 2025 (OOS) | 1.5 | 0.9 |
| 2026 (OOS) | 2.1 | 1.2 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.0% from a peak in-sample and 12.2% out-of-sample, and the worst single trade cost 35.3% of the account out-of-sample. About 73 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 82% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 6.6% from a peak in-sample and 10.5% out-of-sample, and the worst single trade cost 42.5% of the account out-of-sample. About 74 of every 100 trades won in-sample. Out-of-sample it earned 1.2% a year against 2.1% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 96% per trade would have kept the worst drawdown near 10% (rough estimate).

### Range warnings

- max-income: `stop_atr` = 7.0 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 541 | `{"max_bars": 40, "n": 1, "stop_atr": 7.0, "take_profit_atr": 4.5}` | 7,714.81 | 2.8 | -9.2 | 73.3 | 2,510.53 | 2.1 | -12.3 | 0.75 | 57701/34489 | not checked |
| 477 | `{"max_bars": 34, "n": 1, "stop_atr": 7.0, "take_profit_atr": 4.5}` | 7,704.95 | 2.8 | -9.2 | 73.3 | 2,443.85 | 2.0 | -12.4 | 0.74 | 57812/34542 | not checked |
| 479 | `{"max_bars": 30, "n": 1, "stop_atr": 7.0, "take_profit_atr": 4.5}` | 7,704.71 | 2.8 | -9.1 | 73.2 | 2,339.80 | 1.9 | -12.3 | 0.71 | 57942/34630 | not checked |
| 540 | `{"max_bars": 30, "n": 1, "stop_atr": 7.0, "take_profit_atr": 5.5}` | 7,702.03 | 2.8 | -9.0 | 73.2 | 2,355.58 | 2.0 | -12.4 | 0.71 | 57939/34627 | not checked |
| 425 | `{"max_bars": 34, "n": 1, "stop_atr": 7.0, "take_profit_atr": 3.5}` | 7,662.77 | 2.8 | -9.0 | 73.3 | 2,400.93 | 2.0 | -12.2 | 0.73 | 57821/34550 | 1.00 |
| 562 | `{"max_bars": 30, "n": 1, "stop_atr": 7.0, "take_profit_atr": 3.5}` | 7,656.02 | 2.7 | -8.9 | 73.2 | 2,297.10 | 1.9 | -12.1 | 0.70 | 57951/34638 | not checked |
| 490 | `{"max_bars": 30, "n": 1, "stop_atr": 7.0, "take_profit_atr": 3.0}` | 7,624.94 | 2.7 | -8.8 | 73.3 | 2,268.74 | 1.9 | -12.0 | 0.69 | 57971/34660 | not checked |
| 580 | `{"max_bars": 28, "n": 1, "stop_atr": 7.0, "take_profit_atr": 3.5}` | 7,427.04 | 2.7 | -8.7 | 73.2 | 2,276.83 | 1.9 | -12.1 | 0.71 | 58068/34710 | not checked |
| 489 | `{"max_bars": 28, "n": 1, "stop_atr": 7.0, "take_profit_atr": 3.0}` | 7,405.70 | 2.7 | -8.6 | 73.2 | 2,250.57 | 1.9 | -12.0 | 0.70 | 58088/34732 | not checked |
| 430 | `{"max_bars": 28, "n": 1, "stop_atr": 7.0, "take_profit_atr": 2.5}` | 7,102.77 | 2.6 | -8.4 | 73.3 | 2,109.52 | 1.8 | -11.8 | 0.68 | 58135/34768 | not checked |
| 405 | `{"max_bars": 28, "n": 1, "stop_atr": 7.0, "take_profit_atr": 2.0}` | 6,750.98 | 2.5 | -8.4 | 73.5 | 2,037.96 | 1.7 | -11.3 | 0.69 | 58323/34894 | not checked |
| 534 | `{"max_bars": 16, "n": 1, "stop_atr": 6.5, "take_profit_atr": 4.5}` | 6,326.42 | 2.4 | -8.1 | 71.7 | 1,586.92 | 1.4 | -11.6 | 0.58 | 60584/36115 | not checked |
| 486 | `{"max_bars": 38, "n": 2, "stop_atr": 7.0, "take_profit_atr": 4.5}` | 5,839.29 | 2.2 | -7.1 | 73.5 | 1,582.37 | 1.4 | -11.2 | 0.61 | 41788/24717 | not checked |
| 513 | `{"max_bars": 40, "n": 2, "stop_atr": 7.0, "take_profit_atr": 4.5}` | 5,831.14 | 2.2 | -7.1 | 73.5 | 1,579.87 | 1.4 | -11.2 | 0.61 | 41778/24709 | not checked |
| 638 | `{"max_bars": 42, "n": 2, "stop_atr": 6.75, "take_profit_atr": 4.5}` | 5,795.61 | 2.2 | -6.9 | 73.5 | 1,542.27 | 1.3 | -11.0 | 0.60 | 41826/24738 | not checked |
| 550 | `{"max_bars": 36, "n": 2, "stop_atr": 7.0, "take_profit_atr": 3.0}` | 5,763.23 | 2.2 | -6.9 | 73.6 | 1,507.86 | 1.3 | -10.8 | 0.59 | 41827/24739 | not checked |
| 470 | `{"max_bars": 34, "n": 2, "stop_atr": 7.0, "take_profit_atr": 3.0}` | 5,758.75 | 2.2 | -6.9 | 73.6 | 1,496.89 | 1.3 | -10.8 | 0.59 | 41846/24752 | not checked |
| 452 | `{"max_bars": 42, "n": 2, "stop_atr": 6.75, "take_profit_atr": 3.5}` | 5,757.65 | 2.2 | -6.8 | 73.5 | 1,513.02 | 1.3 | -10.8 | 0.59 | 41834/24744 | not checked |
| 590 | `{"max_bars": 34, "n": 2, "stop_atr": 6.75, "take_profit_atr": 3.0}` | 5,710.08 | 2.2 | -6.7 | 73.5 | 1,466.73 | 1.3 | -10.7 | 0.58 | 41893/24784 | not checked |
| 412 | `{"max_bars": 32, "n": 2, "stop_atr": 6.75, "take_profit_atr": 3.0}` | 5,661.13 | 2.2 | -6.7 | 73.5 | 1,443.11 | 1.2 | -10.7 | 0.58 | 41917/24803 | not checked |
| 414 | `{"max_bars": 34, "n": 2, "stop_atr": 6.75, "take_profit_atr": 2.5}` | 5,514.68 | 2.1 | -6.6 | 73.6 | 1,376.64 | 1.2 | -10.5 | 0.56 | 41931/24807 | not checked |
| 415 | `{"max_bars": 32, "n": 2, "stop_atr": 6.75, "take_profit_atr": 2.5}` | 5,468.80 | 2.1 | -6.6 | 73.6 | 1,351.65 | 1.2 | -10.5 | 0.56 | 41954/24826 | 1.00 |
| 491 | `{"max_bars": 32, "n": 2, "stop_atr": 6.25, "take_profit_atr": 3.0}` | 5,391.09 | 2.1 | -6.6 | 73.5 | 1,424.64 | 1.2 | -10.1 | 0.59 | 42003/24858 | not checked |
| 505 | `{"max_bars": 32, "n": 2, "stop_atr": 6.0, "take_profit_atr": 3.0}` | 5,289.47 | 2.0 | -6.5 | 73.5 | 1,381.40 | 1.2 | -9.7 | 0.59 | 42061/24894 | not checked |
| 359 | `{"max_bars": 28, "n": 2, "stop_atr": 5.5, "take_profit_atr": 3.0}` | 4,875.85 | 1.9 | -6.4 | 73.4 | 1,334.29 | 1.2 | -9.2 | 0.61 | 42295/25037 | not checked |

(17 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 641 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
