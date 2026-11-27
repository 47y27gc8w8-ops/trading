# stochastic_oversold_cross__broad: optimization summary

Updated 2026-11-25T09:04:22Z · backtest.py version `d915a51720` · 448 parameter sets tested with this version (448 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [stochastic_oversold_cross__broad__max-income__v002.md](stochastic_oversold_cross__broad__max-income__v002.md) | 448 | `{"level": 32, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 4.0}` | long UBSG.SW since 2026-11-24 00:00 @ 38.0114; long SREN.SW since 2026-11-13 00:00 @ 153.0459; long LOGN.SW since 2026-11-05 00:00 @ 82.144639; long SAP since 2026-11-24 00:00 @ 203.461014; long ACN since 2026-11-24 00:00 @ 223.507034; long LNT since 2026-11-24 00:00 @ 72.811838; long ALL since 2026-11-12 00:00 @ 267.930361; long AMCR since 2026-11-18 00:00 @ 43.14294; long AME since 2026-11-10 00:00 @ 236.080798; long AMGN since 2026-11-24 00:00 @ 452.315647; long APH since 2026-10-27 00:00 @ 76.372903; long APA since 2026-11-10 00:00 @ 43.863153; long BMY since 2026-11-24 00:00 @ 59.917972; long CCL since 2026-11-24 00:00 @ 27.638288; long CRL since 2026-11-24 00:00 @ 332.559729; long CVX since 2026-11-11 00:00 @ 210.634554; long CTAS since 2026-11-24 00:00 @ 223.387003; long CTSH since 2026-11-06 00:00 @ 64.792392; long COP since 2026-11-11 00:00 @ 135.578893; long DE since 2026-11-24 00:00 @ 634.270241; long DXCM since 2026-11-13 00:00 @ 82.034605; long ECL since 2026-11-24 00:00 @ 304.791422; long EMR since 2026-11-24 00:00 @ 156.807023; long EOG since 2026-11-10 00:00 @ 147.134123; long EFX since 2026-11-24 00:00 @ 179.813923; long EL since 2026-11-24 00:00 @ 103.561058; long EXPE since 2026-11-12 00:00 @ 261.161926; long EXPD since 2026-11-11 00:00 @ 190.307075; long XOM since 2026-11-11 00:00 @ 164.153409; long IT since 2026-11-13 00:00 @ 194.368291; long GM since 2026-11-24 00:00 @ 81.234362; long GPC since 2026-10-26 00:00 @ 123.056903; long GPN since 2026-11-23 00:00 @ 93.0279; long GL since 2026-10-30 00:00 @ 162.208652; long DOC since 2026-11-24 00:00 @ 19.965987; long HPQ since 2026-11-06 00:00 @ 29.458836; long ITW since 2026-11-24 00:00 @ 279.343788; long ILMN since 2026-11-10 00:00 @ 217.825323; long IFF since 2026-11-19 00:00 @ 79.483837; long JCI since 2026-11-10 00:00 @ 140.712199; long KDP since 2026-11-24 00:00 @ 35.515653; long LIN since 2026-11-24 00:00 @ 515.724678; long MRK since 2026-10-30 00:00 @ 149.594868; long MCO since 2026-11-24 00:00 @ 480.184021; long NDAQ since 2026-11-24 00:00 @ 105.171541; long NTAP since 2026-11-11 00:00 @ 183.945166; long NSC since 2026-11-12 00:00 @ 333.730094; long NUE since 2026-11-11 00:00 @ 260.078; long NXPI since 2026-11-24 00:00 @ 246.373893; long OXY since 2026-11-11 00:00 @ 57.277176; long OKE since 2026-11-11 00:00 @ 88.396514; long PKG since 2026-11-24 00:00 @ 236.540942; long PANW since 2026-10-22 00:00 @ 356.686961; long PM since 2026-11-16 00:00 @ 200.06; long PFG since 2026-11-24 00:00 @ 107.452224; long PHM since 2026-11-24 00:00 @ 126.417911; long RL since 2026-11-24 00:00 @ 386.095805; long RMD since 2026-11-05 00:00 @ 244.68466; long RVTY since 2026-11-20 00:00 @ 150.975272; long SPGI since 2026-11-24 00:00 @ 451.1353; long STT since 2026-11-24 00:00 @ 160.048; long STLD since 2026-11-11 00:00 @ 239.171736; long SNPS since 2026-10-27 00:00 @ 458.1374; long TRGP since 2026-11-11 00:00 @ 287.026084; long TDY since 2026-11-10 00:00 @ 634.080182; long TRV since 2026-11-12 00:00 @ 405.1215; long VLO since 2026-11-02 00:00 @ 392.797797; long VRSN since 2026-11-23 00:00 @ 309.692886; long VRTX since 2026-11-24 00:00 @ 542.402662; long WAT since 2026-11-20 00:00 @ 454.486311; long WDAY since 2026-11-13 00:00 @ 193.738097; long ZBRA since 2026-11-12 00:00 @ 324.027172 |
| balanced | [stochastic_oversold_cross__broad__balanced__v001.md](stochastic_oversold_cross__broad__balanced__v001.md) | 328 | `{"level": 20, "max_candles": 14, "stop_atr": 4.5, "take_profit_atr": 6.0}` | long UBSG.SW since 2026-11-24 00:00 @ 38.0114; long SREN.SW since 2026-11-24 00:00 @ 151.0453; long LOGN.SW since 2026-11-05 00:00 @ 82.144639; long SAP since 2026-11-24 00:00 @ 203.461014; long ACN since 2026-11-24 00:00 @ 223.507034; long AMCR since 2026-11-18 00:00 @ 43.14294; long AMGN since 2026-11-24 00:00 @ 452.315647; long APA since 2026-11-10 00:00 @ 43.863153; long BMY since 2026-11-24 00:00 @ 59.917972; long CCL since 2026-11-24 00:00 @ 27.638288; long CVX since 2026-11-11 00:00 @ 210.634554; long CTSH since 2026-11-23 00:00 @ 58.347501; long COP since 2026-11-11 00:00 @ 135.578893; long DE since 2026-11-24 00:00 @ 634.270241; long ECL since 2026-11-24 00:00 @ 304.791422; long EMR since 2026-11-24 00:00 @ 156.807023; long EOG since 2026-11-10 00:00 @ 147.134123; long EFX since 2026-11-24 00:00 @ 179.813923; long EL since 2026-11-24 00:00 @ 103.561058; long EXPE since 2026-11-12 00:00 @ 261.161926; long EXPD since 2026-11-11 00:00 @ 190.307075; long XOM since 2026-11-11 00:00 @ 164.153409; long IT since 2026-11-13 00:00 @ 194.368291; long GM since 2026-11-24 00:00 @ 81.234362; long GPN since 2026-11-23 00:00 @ 93.0279; long ITW since 2026-11-24 00:00 @ 279.343788; long ILMN since 2026-11-10 00:00 @ 217.825323; long IFF since 2026-11-19 00:00 @ 79.483837; long JCI since 2026-11-10 00:00 @ 140.712199; long KDP since 2026-11-24 00:00 @ 35.515653; long MPC since 2026-11-10 00:00 @ 377.191751; long MRK since 2026-11-24 00:00 @ 135.885755; long MCO since 2026-11-24 00:00 @ 480.184021; long NDAQ since 2026-11-24 00:00 @ 105.171541; long NTAP since 2026-11-11 00:00 @ 183.945166; long NUE since 2026-11-11 00:00 @ 260.078; long OXY since 2026-11-11 00:00 @ 57.277176; long OKE since 2026-11-11 00:00 @ 88.396514; long PKG since 2026-11-24 00:00 @ 236.540942; long PANW since 2026-11-19 00:00 @ 355.916741; long PSX since 2026-11-10 00:00 @ 245.126543; long PFG since 2026-11-24 00:00 @ 107.452224; long PHM since 2026-11-24 00:00 @ 126.417911; long RL since 2026-11-24 00:00 @ 386.095805; long RVTY since 2026-11-20 00:00 @ 150.975272; long SPGI since 2026-11-24 00:00 @ 451.1353; long STT since 2026-11-24 00:00 @ 160.048; long STLD since 2026-11-11 00:00 @ 239.171736; long WDAY since 2026-11-13 00:00 @ 193.738097; long ZBRA since 2026-11-12 00:00 @ 324.027172 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 4,694.43 | 2,869.90 | 3,025.55 | 1,315.02 |
| return % | 46.94 | 28.70 | 30.26 | 13.15 |
| return %/year | 2.4 | 2.3 | 1.7 | 1.1 |
| gross profit | 17,900.62 | 12,399.61 | 9,650.30 | 6,290.63 |
| gross loss | 13,206.19 | 9,529.71 | 6,624.74 | 4,975.60 |
| trades | 22,612 | 16,648 | 13,330 | 10,117 |
| win rate % | 68.2 | 67.0 | 61.4 | 58.7 |
| avg win | 1.16 | 1.11 | 1.18 | 1.06 |
| avg loss | -1.84 | -1.73 | -1.29 | -1.19 |
| avg result / trade | 0.21 | 0.17 | 0.23 | 0.13 |
| largest single loss | -22.85 | -20.42 | -15.30 | -10.90 |
| largest loss % of equity | -31.45 | -29.08 | -19.85 | -17.02 |
| max drawdown | -925.03 | -651.36 | -296.26 | -465.23 |
| max drawdown % | -7.78 | -5.69 | -2.50 | -4.34 |
| profit factor | 1.35 | 1.30 | 1.46 | 1.26 |
| unusually bad trades | 874 | 452 | 1,166 | 966 |
| … threshold (% of equity) | 12.9 | 12.9 | 7.7 | 7.5 |
| time in market % | 14.8 | 16.5 | 7.6 | 8.7 |
| buy & hold return % | 705.33 | 470.05 | 705.33 | 470.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.96 |  | 0.68 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 3.2 | 2.8 |
| 2001 | -1.5 | 0.0 |
| 2002 | -3.4 | -1.2 |
| 2003 | 8.1 | 4.9 |
| 2004 | 3.5 | 2.0 |
| 2005 | 2.0 | 0.7 |
| 2006 | 2.2 | 0.7 |
| 2007 | 3.4 | 1.8 |
| 2008 | -6.9 | -2.3 |
| 2009 | 9.8 | 5.8 |
| 2010 | 4.8 | 3.0 |
| 2011 | 2.1 | 1.5 |
| 2012 | 1.6 | 0.6 |
| 2013 | 7.0 | 4.0 |
| 2014 | 2.3 | 1.3 |
| 2015 | 1.9 | 1.3 |
| 2016 (OOS) | 0.5 | 0.7 |
| 2017 (OOS) | 5.2 | 2.3 |
| 2018 (OOS) | 2.5 | 1.7 |
| 2019 (OOS) | 4.0 | 1.7 |
| 2020 (OOS) | 2.0 | 0.3 |
| 2021 (OOS) | 6.3 | 2.9 |
| 2022 (OOS) | -2.5 | -1.3 |
| 2023 (OOS) | 2.3 | 1.9 |
| 2024 (OOS) | 3.5 | 2.4 |
| 2025 (OOS) | 0.5 | 0.8 |
| 2026 (OOS) | 1.3 | -0.6 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 7.8% from a peak in-sample and 5.7% out-of-sample, and the worst single trade cost 29.1% of the account out-of-sample. About 68 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 2.5% from a peak in-sample and 4.3% out-of-sample, and the worst single trade cost 17.0% of the account out-of-sample. About 61 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 440 | `{"level": 33, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 4,757.94 | 2.5 | -7.9 | 68.3 | 2,998.52 | 2.4 | -5.9 | 0.99 | 23280/17135 | not checked |
| 445 | `{"level": 32, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 4,694.43 | 2.4 | -7.8 | 68.2 | 2,869.90 | 2.3 | -5.7 | 0.96 | 22612/16648 | 1.00 |
| 439 | `{"level": 31, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 4.0}` | 4,666.17 | 2.4 | -7.6 | 68.2 | 2,739.72 | 2.2 | -5.5 | 0.93 | 21929/16139 | not checked |
| 391 | `{"level": 27, "max_candles": 24, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 4,663.10 | 2.4 | -6.2 | 68.3 | 2,717.82 | 2.2 | -5.7 | 0.92 | 18814/13913 | not checked |
| 393 | `{"level": 25, "max_candles": 24, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 4,651.03 | 2.4 | -5.3 | 68.6 | 2,547.99 | 2.1 | -5.5 | 0.87 | 17206/12802 | not checked |
| 394 | `{"level": 25, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 4,554.63 | 2.4 | -5.1 | 68.4 | 2,501.97 | 2.1 | -5.3 | 0.87 | 17344/12897 | not checked |
| 371 | `{"level": 24, "max_candles": 24, "stop_atr": 4.25, "take_profit_atr": 7.0}` | 4,413.95 | 2.3 | -5.1 | 68.4 | 2,402.93 | 2.0 | -5.3 | 0.87 | 16369/12212 | not checked |
| 374 | `{"level": 25, "max_candles": 24, "stop_atr": 3.75, "take_profit_atr": 6.5}` | 4,365.48 | 2.3 | -4.9 | 67.8 | 2,456.07 | 2.0 | -5.0 | 0.89 | 17496/13030 | not checked |
| 413 | `{"level": 24, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 4,337.34 | 2.3 | -4.9 | 68.2 | 2,352.19 | 2.0 | -5.1 | 0.86 | 16491/12296 | not checked |
| 331 | `{"level": 25, "max_candles": 24, "stop_atr": 3.25, "take_profit_atr": 7.0}` | 4,190.95 | 2.2 | -4.7 | 66.4 | 2,364.78 | 2.0 | -4.6 | 0.89 | 17956/13360 | not checked |
| 432 | `{"level": 24, "max_candles": 24, "stop_atr": 3.75, "take_profit_atr": 7.0}` | 4,164.43 | 2.2 | -4.6 | 67.6 | 2,313.98 | 1.9 | -4.8 | 0.88 | 16625/12419 | not checked |
| 401 | `{"level": 22, "max_candles": 24, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 4,070.58 | 2.2 | -4.5 | 68.3 | 2,207.49 | 1.9 | -4.6 | 0.86 | 14754/11045 | not checked |
| 366 | `{"level": 25, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 4,017.15 | 2.1 | -4.0 | 63.6 | 1,903.10 | 1.6 | -5.2 | 0.76 | 18019/13436 | not checked |
| 367 | `{"level": 25, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 3,984.39 | 2.1 | -4.0 | 63.6 | 1,860.00 | 1.6 | -5.2 | 0.74 | 18026/13437 | not checked |
| 398 | `{"level": 25, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 3,976.99 | 2.1 | -4.0 | 63.6 | 1,880.15 | 1.6 | -5.2 | 0.76 | 18022/13436 | not checked |
| 389 | `{"level": 24, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 3,830.94 | 2.0 | -3.9 | 63.3 | 1,793.20 | 1.5 | -5.0 | 0.75 | 17094/12777 | not checked |
| 388 | `{"level": 24, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 5.0}` | 3,794.73 | 2.0 | -3.9 | 63.4 | 1,760.18 | 1.5 | -5.0 | 0.74 | 17099/12778 | not checked |
| 207 | `{"level": 25, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 3,781.62 | 2.0 | -3.8 | 63.8 | 1,720.55 | 1.5 | -4.6 | 0.72 | 18042/13448 | not checked |
| 358 | `{"level": 22, "max_candles": 16, "stop_atr": 4.5, "take_profit_atr": 5.0}` | 3,713.51 | 2.0 | -3.6 | 63.6 | 1,715.17 | 1.5 | -4.8 | 0.73 | 15110/11325 | not checked |
| 119 | `{"level": 21, "max_candles": 18, "stop_atr": 4.5, "take_profit_atr": 6.0}` | 3,701.61 | 2.0 | -3.5 | 65.2 | 1,912.11 | 1.6 | -4.7 | 0.81 | 13979/10552 | not checked |
| 400 | `{"level": 21, "max_candles": 16, "stop_atr": 4.5, "take_profit_atr": 6.5}` | 3,594.57 | 1.9 | -3.0 | 63.4 | 1,732.23 | 1.5 | -4.7 | 0.76 | 14138/10674 | not checked |
| 122 | `{"level": 20, "max_candles": 16, "stop_atr": 4.5, "take_profit_atr": 6.0}` | 3,390.15 | 1.8 | -2.8 | 63.3 | 1,574.49 | 1.4 | -4.4 | 0.73 | 13167/9987 | 1.00 |
| 128 | `{"level": 20, "max_candles": 16, "stop_atr": 4.5, "take_profit_atr": 5.5}` | 3,370.37 | 1.8 | -2.8 | 63.4 | 1,566.95 | 1.4 | -4.3 | 0.74 | 13167/9987 | not checked |
| 127 | `{"level": 20, "max_candles": 16, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 3,209.03 | 1.8 | -2.7 | 62.9 | 1,537.79 | 1.3 | -3.9 | 0.75 | 13318/10112 | not checked |
| 285 | `{"level": 20, "max_candles": 16, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 3,157.31 | 1.7 | -2.7 | 63.3 | 1,402.57 | 1.2 | -3.5 | 0.70 | 13273/10060 | not checked |

(14 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 448 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
