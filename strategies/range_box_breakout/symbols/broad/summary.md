# range_box_breakout__broad: optimization summary

Updated 2026-11-25T11:39:57Z · backtest.py version `4af220afd6` · 543 parameter sets tested with this version (543 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, CDW, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [range_box_breakout__broad__max-income__v002.md](range_box_breakout__broad__max-income__v002.md) | 543 | `{"max_candles": 54, "n": 2, "stop_atr": 3.75, "take_profit_atr": 7.0, "width": 5.25}` | long MMM since 2026-11-24 00:00 @ 183.815123; long AFL since 2026-11-11 00:00 @ 125.366005; long ALL since 2026-11-12 00:00 @ 267.930361; long AEE since 2026-11-16 00:00 @ 115.484632; long AWK since 2026-11-17 00:00 @ 149.434816; long AON since 2026-11-17 00:00 @ 340.102; long ACGL since 2026-11-05 00:00 @ 112.413711; long AIZ since 2026-11-12 00:00 @ 326.297872; long T since 2026-11-23 00:00 @ 22.066617; long AZO since 2026-10-12 00:00 @ 2921.576161; long BAX since 2026-11-24 00:00 @ 26.317892; long BDX since 2026-11-10 00:00 @ 213.994172; long BRK-B since 2026-11-03 00:00 @ 554.386237; long TECH since 2026-11-24 00:00 @ 72.78183; long BIIB since 2026-11-24 00:00 @ 259.907936; long BRO since 2026-11-02 00:00 @ 68.995189; long CAH since 2026-11-05 00:00 @ 274.622371; long CBOE since 2026-11-11 00:00 @ 363.539022; long CHTR since 2026-11-02 00:00 @ 112.203649; long CMG since 2026-10-30 00:00 @ 31.679501; long CB since 2026-11-11 00:00 @ 366.269852; long CHD since 2026-10-30 00:00 @ 110.028946; long CINF since 2026-11-11 00:00 @ 188.476524; long CLX since 2026-11-11 00:00 @ 104.921466; long CMS since 2026-10-07 00:00 @ 64.564606; long CL since 2026-11-05 00:00 @ 100.03; long CMCSA since 2026-10-30 00:00 @ 22.876862; long ED since 2026-11-03 00:00 @ 116.788944; long COST since 2026-11-05 00:00 @ 1071.311287; long DPZ since 2026-10-19 00:00 @ 304.721394; long DTE since 2026-10-22 00:00 @ 130.099016; long DUK since 2026-11-03 00:00 @ 125.738062; long ECL since 2026-11-24 00:00 @ 304.791422; long EIX since 2026-10-12 00:00 @ 55.576669; long EW since 2026-11-10 00:00 @ 104.281275; long EVRG since 2026-11-24 00:00 @ 86.956079; long ES since 2026-10-23 00:00 @ 67.870353; long EXC since 2026-10-13 00:00 @ 42.612778; long EXR since 2026-11-05 00:00 @ 162.218649; long FE since 2026-10-08 00:00 @ 44.143216; long GEN since 2026-10-30 00:00 @ 28.510871; long GIS since 2026-11-16 00:00 @ 34.850452; long GILD since 2026-10-15 00:00 @ 156.436916; long GPN since 2026-11-23 00:00 @ 93.0279; long HIG since 2026-11-11 00:00 @ 136.410906; long DOC since 2026-11-24 00:00 @ 19.965987; long HSY since 2026-11-03 00:00 @ 168.108418; long HRL since 2026-11-23 00:00 @ 23.096927; long HUBB since 2026-11-24 00:00 @ 428.468498; long IDXX since 2026-11-05 00:00 @ 702.2106; long JKHY since 2026-11-12 00:00 @ 177.473224; long LH since 2026-11-24 00:00 @ 370.491119; long LIN since 2026-11-24 00:00 @ 515.724678; long MRSH since 2026-10-30 00:00 @ 202.010582; long MKC since 2026-11-23 00:00 @ 46.694004; long MDT since 2026-10-13 00:00 @ 92.377703; long MGM since 2026-11-02 00:00 @ 30.239069; long MDLZ since 2026-11-02 00:00 @ 65.239567; long MSI since 2026-11-12 00:00 @ 536.010731; long NRG since 2026-11-24 00:00 @ 95.798728; long ORLY since 2026-11-13 00:00 @ 92.097621; long PANW since 2026-11-20 00:00 @ 359.147721; long PNR since 2026-10-30 00:00 @ 66.029805; long PCG since 2026-11-17 00:00 @ 13.544062; long PG since 2026-10-30 00:00 @ 164.669381; long PTC since 2026-10-12 00:00 @ 194.928456; long PEG since 2026-10-23 00:00 @ 72.571768; long DGX since 2026-10-16 00:00 @ 239.741899; long RL since 2026-11-24 00:00 @ 386.095805; long REGN since 2026-11-12 00:00 @ 971.601505; long RSG since 2026-11-02 00:00 @ 244.653376; long ROL since 2026-11-17 00:00 @ 38.681599; long SHW since 2026-11-24 00:00 @ 347.754289; long SJM since 2026-10-14 00:00 @ 120.998856; long SO since 2026-11-17 00:00 @ 93.728107; long STE since 2026-11-06 00:00 @ 247.450788; long TGT since 2026-11-02 00:00 @ 154.091521; long TJX since 2026-11-19 00:00 @ 138.631573; long TSCO since 2026-10-30 00:00 @ 34.500349; long TSN since 2026-11-17 00:00 @ 63.028901; long UAL since 2026-11-24 00:00 @ 106.541955; long VZ since 2026-11-02 00:00 @ 44.043208; long VRTX since 2026-11-24 00:00 @ 542.402662; long VMC since 2026-11-24 00:00 @ 280.594163; long WRB since 2026-11-02 00:00 @ 74.092221; long WMT since 2026-11-03 00:00 @ 126.728009; long DIS since 2026-10-30 00:00 @ 111.853546; long WM since 2026-11-12 00:00 @ 243.873143; long WEC since 2026-11-02 00:00 @ 114.74626; long WTW since 2026-10-16 00:00 @ 313.133921; long WYNN since 2026-11-24 00:00 @ 82.834841; long YUM since 2026-11-05 00:00 @ 167.020092; long ZBH since 2026-11-24 00:00 @ 105.681697 |
| balanced | [range_box_breakout__broad__balanced__v001.md](range_box_breakout__broad__balanced__v001.md) | 492 | `{"max_candles": 72, "n": 28, "stop_atr": 2.75, "take_profit_atr": 2.0, "width": 4.5}` | long AES since 2026-11-18 00:00 @ 15.024506; long PCG since 2026-11-20 00:00 @ 14.054215 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 14,111.79 | 5,483.42 | 1,045.28 | 448.97 |
| return % | 141.12 | 54.83 | 10.45 | 4.49 |
| return %/year | 4.3 | 4.1 | 0.5 | 0.4 |
| gross profit | 102,511.45 | 40,762.68 | 11,654.07 | 6,090.34 |
| gross loss | 88,399.66 | 35,279.26 | 10,608.79 | 5,641.38 |
| trades | 112,438 | 66,461 | 21,961 | 12,761 |
| win rate % | 32.4 | 32.5 | 48.0 | 48.6 |
| avg win | 2.81 | 1.89 | 1.11 | 0.98 |
| avg loss | -1.16 | -0.79 | -0.93 | -0.86 |
| avg result / trade | 0.13 | 0.08 | 0.05 | 0.04 |
| largest single loss | -178.52 | -52.84 | -12.68 | -7.25 |
| largest loss % of equity | -62.39 | -14.96 | -17.67 | -21.22 |
| max drawdown | -7,035.28 | -1,854.56 | -681.14 | -193.56 |
| max drawdown % | -33.05 | -12.41 | -6.27 | -1.84 |
| profit factor | 1.16 | 1.16 | 1.10 | 1.08 |
| unusually bad trades | 14,470 | 8,319 | 1,701 | 735 |
| … threshold (% of equity) | 4.1 | 4.0 | 6.6 | 6.6 |
| time in market % | 43.2 | 51.0 | 6.9 | 7.7 |
| buy & hold return % | 1,897.80 | 476.79 | 1,897.80 | 476.79 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.96 |  | 0.85 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 9.6 | 1.2 |
| 1996 | 6.0 | 1.0 |
| 1997 | 8.8 | 1.1 |
| 1998 | 8.6 | 0.5 |
| 1999 | 11.1 | 0.5 |
| 2000 | -3.1 | -0.4 |
| 2001 | -1.1 | -1.0 |
| 2002 | -6.0 | -0.8 |
| 2003 | 16.8 | 2.2 |
| 2004 | 15.7 | 1.4 |
| 2005 | 3.7 | 0.7 |
| 2006 | 6.0 | 1.2 |
| 2007 | -2.4 | -0.7 |
| 2008 | -22.9 | -2.9 |
| 2009 | 25.6 | 1.9 |
| 2010 | 10.3 | 1.5 |
| 2011 | -9.5 | -0.4 |
| 2012 | 5.0 | 0.3 |
| 2013 | 16.6 | 2.5 |
| 2014 | 7.5 | 0.6 |
| 2015 | -4.9 | -0.3 |
| 2016 (OOS) | 13.6 | 0.5 |
| 2017 (OOS) | 11.2 | 1.5 |
| 2018 (OOS) | -2.2 | -0.6 |
| 2019 (OOS) | 19.7 | 0.9 |
| 2020 (OOS) | 16.6 | 1.3 |
| 2021 (OOS) | 9.7 | 1.5 |
| 2022 (OOS) | -6.2 | -0.2 |
| 2023 (OOS) | 26.5 | -0.3 |
| 2024 (OOS) | 28.7 | 0.8 |
| 2025 (OOS) | -11.3 | -0.7 |
| 2026 (OOS) | 6.6 | -0.0 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 33.0% from a peak in-sample and 12.4% out-of-sample, and the worst single trade cost 15.0% of the account out-of-sample. About 32 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks low: the account fell up to 6.3% from a peak in-sample and 1.8% out-of-sample, and the worst single trade cost 21.2% of the account out-of-sample. About 48 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 529 | `{"max_candles": 54, "n": 2, "stop_atr": 3.5, "take_profit_atr": 7.0, "width": 5.25}` | 14,185.09 | 4.3 | -32.9 | 32.4 | 5,511.86 | 4.1 | -12.4 | 0.96 | 112464/66475 | not checked |
| 531 | `{"max_candles": 54, "n": 2, "stop_atr": 3.75, "take_profit_atr": 6.5, "width": 5.25}` | 14,014.87 | 4.3 | -32.8 | 32.5 | 5,007.93 | 3.8 | -12.2 | 0.89 | 113439/67111 | not checked |
| 526 | `{"max_candles": 54, "n": 3, "stop_atr": 3.75, "take_profit_atr": 7.0, "width": 5.25}` | 13,536.79 | 4.2 | -31.4 | 32.9 | 5,484.78 | 4.1 | -11.5 | 0.99 | 102723/60887 | not checked |
| 501 | `{"max_candles": 60, "n": 3, "stop_atr": 3.75, "take_profit_atr": 5.5, "width": 5.25}` | 12,080.21 | 3.9 | -30.4 | 33.1 | 4,610.18 | 3.5 | -11.5 | 0.92 | 106143/63069 | not checked |
| 519 | `{"max_candles": 78, "n": 6, "stop_atr": 4.0, "take_profit_atr": 6.5, "width": 5.5}` | 8,845.14 | 3.1 | -28.3 | 34.0 | 4,579.18 | 3.5 | -10.3 | 1.15 | 83642/50004 | not checked |
| 468 | `{"max_candles": 90, "n": 7, "stop_atr": 3.0, "take_profit_atr": 5.0, "width": 6.75}` | 7,352.57 | 2.7 | -26.4 | 34.7 | 3,895.74 | 3.1 | -10.3 | 1.15 | 81968/49450 | not checked |
| 521 | `{"max_candles": 42, "n": 10, "stop_atr": 2.75, "take_profit_atr": 6.5, "width": 4.0}` | 6,969.27 | 2.5 | -23.0 | 35.3 | 4,192.97 | 3.3 | -8.9 | 1.28 | 64425/38878 | not checked |
| 522 | `{"max_candles": 48, "n": 14, "stop_atr": 3.25, "take_profit_atr": 6.0, "width": 5.75}` | 6,527.18 | 2.4 | -20.9 | 36.6 | 3,939.93 | 3.1 | -8.5 | 1.28 | 56071/34021 | not checked |
| 467 | `{"max_candles": 36, "n": 14, "stop_atr": 3.25, "take_profit_atr": 6.0, "width": 5.75}` | 6,403.64 | 2.4 | -20.7 | 36.6 | 4,023.50 | 3.2 | -8.3 | 1.32 | 56430/34280 | not checked |
| 408 | `{"max_candles": 96, "n": 13, "stop_atr": 3.0, "take_profit_atr": 4.5, "width": 8.0}` | 5,575.32 | 2.1 | -20.6 | 36.9 | 3,593.02 | 2.9 | -9.0 | 1.34 | 62496/38134 | not checked |
| 160 | `{"max_candles": 90, "n": 12, "stop_atr": 3.0, "take_profit_atr": 4.5, "width": 4.5}` | 5,193.95 | 2.0 | -20.6 | 36.4 | 3,229.97 | 2.6 | -7.9 | 1.29 | 61866/37636 | not checked |
| 469 | `{"max_candles": 54, "n": 15, "stop_atr": 3.25, "take_profit_atr": 4.5, "width": 7.5}` | 5,170.97 | 2.0 | -18.1 | 37.3 | 3,397.90 | 2.7 | -7.9 | 1.35 | 58060/35331 | not checked |
| 154 | `{"max_candles": 48, "n": 19, "stop_atr": 4.0, "take_profit_atr": 4.5, "width": 6.75}` | 5,143.64 | 2.0 | -16.7 | 38.1 | 3,159.70 | 2.5 | -7.4 | 1.27 | 50407/30588 | not checked |
| 150 | `{"max_candles": 48, "n": 19, "stop_atr": 4.0, "take_profit_atr": 4.5, "width": 5.25}` | 4,972.96 | 1.9 | -16.1 | 38.1 | 2,835.12 | 2.3 | -6.7 | 1.20 | 47024/28484 | not checked |
| 247 | `{"max_candles": 54, "n": 27, "stop_atr": 4.0, "take_profit_atr": 5.5, "width": 7.5}` | 4,502.42 | 1.8 | -13.4 | 38.5 | 3,163.17 | 2.6 | -7.7 | 1.43 | 40824/24410 | not checked |
| 455 | `{"max_candles": 90, "n": 26, "stop_atr": 2.5, "take_profit_atr": 5.5, "width": 5.5}` | 3,589.37 | 1.5 | -12.5 | 38.3 | 2,496.09 | 2.1 | -6.2 | 1.41 | 36242/21657 | not checked |
| 219 | `{"max_candles": 42, "n": 26, "stop_atr": 2.5, "take_profit_atr": 5.0, "width": 5.5}` | 3,246.93 | 1.4 | -12.2 | 38.3 | 2,289.14 | 1.9 | -6.1 | 1.42 | 36454/21795 | not checked |
| 412 | `{"max_candles": 78, "n": 30, "stop_atr": 4.0, "take_profit_atr": 5.0, "width": 5.25}` | 3,045.46 | 1.3 | -10.0 | 38.8 | 1,650.81 | 1.4 | -5.6 | 1.11 | 27678/16368 | not checked |
| 494 | `{"max_candles": 72, "n": 28, "stop_atr": 2.75, "take_profit_atr": 3.0, "width": 4.5}` | 1,733.87 | 0.8 | -7.0 | 41.2 | 687.21 | 0.6 | -2.4 | 0.80 | 21782/12685 | not checked |
| 325 | `{"max_candles": 72, "n": 28, "stop_atr": 2.75, "take_profit_atr": 2.5, "width": 4.5}` | 1,490.70 | 0.7 | -6.7 | 43.6 | 622.74 | 0.6 | -2.1 | 0.85 | 21835/12718 | not checked |
| 239 | `{"max_candles": 30, "n": 27, "stop_atr": 3.75, "take_profit_atr": 4.0, "width": 4.0}` | 1,416.50 | 0.6 | -5.9 | 39.2 | 743.90 | 0.7 | -2.1 | 1.05 | 15155/8782 | not checked |
| 169 | `{"max_candles": 24, "n": 20, "stop_atr": 4.0, "take_profit_atr": 4.5, "width": 3.25}` | 1,017.89 | 0.5 | -5.5 | 37.3 | 572.44 | 0.5 | -1.9 | 1.11 | 15313/8794 | not checked |
| 430 | `{"max_candles": 96, "n": 28, "stop_atr": 2.75, "take_profit_atr": 5.0, "width": 3.75}` | 991.36 | 0.5 | -4.5 | 38.4 | 521.02 | 0.5 | -1.6 | 1.04 | 9417/5487 | not checked |
| 277 | `{"max_candles": 60, "n": 13, "stop_atr": 2.0, "take_profit_atr": 5.0, "width": 2.25}` | 597.78 | 0.3 | -4.3 | 35.4 | 119.70 | 0.1 | -1.4 | 0.39 | 9308/5400 | not checked |
| 237 | `{"max_candles": 96, "n": 29, "stop_atr": 2.25, "take_profit_atr": 4.0, "width": 3.5}` | 534.69 | 0.2 | -2.1 | 38.9 | 189.83 | 0.2 | -1.0 | 0.68 | 5134/2900 | not checked |

(3 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 543 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
