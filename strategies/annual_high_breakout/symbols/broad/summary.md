# annual_high_breakout__broad: optimization summary

Updated 2026-11-25T20:10:00Z · backtest.py version `bb63cca92b` · 1,026 parameter sets tested with this version (1,026 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [annual_high_breakout__broad__max-income__v002.md](annual_high_breakout__broad__max-income__v002.md) | 1025 | `{"max_bars": 138, "n": 132, "stop_atr": 6.75, "take_profit_atr": 10.5}` | long RO.SW since 2026-10-16 00:00 @ 380.914228; long LONN.SW since 2026-10-16 00:00 @ 602.580744; long GIVN.SW since 2026-10-14 00:00 @ 3818.1451; long SCMN.SW since 2026-11-06 00:00 @ 725.71765; long SLHN.SW since 2026-11-05 00:00 @ 987.096028; long KNIN.SW since 2026-11-06 00:00 @ 237.871343; long SGSN.SW since 2026-10-22 00:00 @ 100.380103; long MMM since 2026-11-05 00:00 @ 193.833158; long AES since 2026-11-18 00:00 @ 15.024506; long MO since 2026-10-30 00:00 @ 78.163441; long AWK since 2026-11-05 00:00 @ 150.042584; long AMGN since 2026-11-05 00:00 @ 481.354945; long AJG since 2026-11-02 00:00 @ 274.782422; long AIZ since 2026-11-05 00:00 @ 313.333962; long ADP since 2026-10-23 00:00 @ 307.082087; long BDX since 2026-11-05 00:00 @ 208.0624; long BRK-B since 2026-11-05 00:00 @ 584.405249; long BIIB since 2026-09-24 00:00 @ 226.868043; long BR since 2026-11-05 00:00 @ 192.117616; long BF-B since 2026-11-05 00:00 @ 31.219362; long CAH since 2026-11-06 00:00 @ 265.659661; long COR since 2026-11-05 00:00 @ 359.29795; long CRL since 2026-10-22 00:00 @ 341.532422; long CVX since 2026-11-02 00:00 @ 230.65435; long CHD since 2026-10-23 00:00 @ 107.694692; long ED since 2026-11-06 00:00 @ 119.072497; long CPAY since 2026-11-06 00:00 @ 437.911333; long DG since 2026-11-05 00:00 @ 143.092918; long DLTR since 2026-11-05 00:00 @ 144.613378; long ECL since 2026-11-05 00:00 @ 318.945661; long EW since 2026-11-05 00:00 @ 100.700199; long GILD since 2026-11-02 00:00 @ 169.900961; long GPN since 2026-11-02 00:00 @ 97.459229; long HCA since 2026-11-05 00:00 @ 515.234541; long IDXX since 2026-11-03 00:00 @ 662.458688; long ICE since 2026-11-02 00:00 @ 168.53054; long JKHY since 2026-11-05 00:00 @ 180.464127; long KDP since 2026-10-16 00:00 @ 34.420323; long LH since 2026-10-29 00:00 @ 356.046784; long LLY since 2026-10-30 00:00 @ 1427.526139; long LMT since 2026-10-27 00:00 @ 627.098046; long MAR since 2026-11-03 00:00 @ 416.809567; long MCK since 2026-11-05 00:00 @ 1086.165718; long MDT since 2026-10-16 00:00 @ 95.858751; long MTD since 2026-09-23 00:00 @ 1485.015317; long MSI since 2026-11-06 00:00 @ 513.61406; long MSCI since 2026-11-05 00:00 @ 678.063715; long NDAQ since 2026-10-23 00:00 @ 102.730807; long PPG since 2026-11-05 00:00 @ 127.28229; long PG since 2026-10-16 00:00 @ 156.759578; long PRU since 2026-11-05 00:00 @ 128.0384; long PTC since 2026-10-06 00:00 @ 193.0579; long PSA since 2026-11-05 00:00 @ 345.083505; long REGN since 2026-11-02 00:00 @ 926.553871; long RSG since 2026-11-02 00:00 @ 244.653376; long RMD since 2026-10-23 00:00 @ 251.208531; long ROP since 2026-10-23 00:00 @ 440.132; long SWK since 2026-11-05 00:00 @ 118.115426; long STE since 2026-11-05 00:00 @ 251.76071; long TMO since 2026-09-17 00:00 @ 656.947025; long TYL since 2026-11-03 00:00 @ 397.169103; long ULTA since 2026-10-23 00:00 @ 631.139297; long UHS since 2026-11-05 00:00 @ 200.06; long VRSN since 2026-11-04 00:00 @ 312.341502; long VTRS since 2026-11-12 00:00 @ 21.056314; long GWW since 2026-11-05 00:00 @ 1479.632738; long DIS since 2026-11-05 00:00 @ 119.905964; long WST since 2026-10-28 00:00 @ 396.819174; long ZBH since 2026-11-05 00:00 @ 111.0333 |
| balanced | [annual_high_breakout__broad__balanced__v002.md](annual_high_breakout__broad__balanced__v002.md) | 1026 | `{"max_bars": 102, "n": 192, "stop_atr": 4.75, "take_profit_atr": 5.5}` | long RO.SW since 2026-10-16 00:00 @ 380.914228; long LONN.SW since 2026-10-16 00:00 @ 602.580744; long GIVN.SW since 2026-10-14 00:00 @ 3818.1451; long SCMN.SW since 2026-11-06 00:00 @ 725.71765; long SLHN.SW since 2026-11-05 00:00 @ 987.096028; long KNIN.SW since 2026-11-06 00:00 @ 237.871343; long SGSN.SW since 2026-10-22 00:00 @ 100.380103; long MMM since 2026-11-05 00:00 @ 193.833158; long MO since 2026-10-30 00:00 @ 78.163441; long AWK since 2026-11-05 00:00 @ 150.042584; long AMGN since 2026-11-05 00:00 @ 481.354945; long AJG since 2026-11-02 00:00 @ 274.782422; long AIZ since 2026-11-05 00:00 @ 313.333962; long ADP since 2026-10-23 00:00 @ 307.082087; long BDX since 2026-11-05 00:00 @ 208.0624; long BRK-B since 2026-11-05 00:00 @ 584.405249; long CAH since 2026-11-06 00:00 @ 265.659661; long CRL since 2026-10-22 00:00 @ 341.532422; long CHD since 2026-10-23 00:00 @ 107.694692; long ED since 2026-11-06 00:00 @ 119.072497; long CPAY since 2026-11-06 00:00 @ 437.911333; long DLTR since 2026-11-05 00:00 @ 144.613378; long ECL since 2026-11-05 00:00 @ 318.945661; long EW since 2026-11-05 00:00 @ 100.700199; long GILD since 2026-11-02 00:00 @ 169.900961; long GPN since 2026-11-02 00:00 @ 97.459229; long IDXX since 2026-11-05 00:00 @ 702.2106; long KDP since 2026-10-16 00:00 @ 34.420323; long LH since 2026-10-29 00:00 @ 356.046784; long LLY since 2026-10-30 00:00 @ 1427.526139; long MAR since 2026-11-03 00:00 @ 416.809567; long MCK since 2026-11-05 00:00 @ 1086.165718; long MSI since 2026-11-06 00:00 @ 513.61406; long MSCI since 2026-11-05 00:00 @ 678.063715; long NDAQ since 2026-10-23 00:00 @ 102.730807; long PG since 2026-10-23 00:00 @ 164.0492; long PRU since 2026-11-05 00:00 @ 128.0384; long PTC since 2026-10-06 00:00 @ 193.0579; long PSA since 2026-11-05 00:00 @ 345.083505; long REGN since 2026-11-02 00:00 @ 926.553871; long RSG since 2026-11-02 00:00 @ 244.653376; long SWK since 2026-11-05 00:00 @ 118.115426; long TMO since 2026-09-17 00:00 @ 656.947025; long TYL since 2026-11-06 00:00 @ 415.89472; long VRSN since 2026-11-04 00:00 @ 312.341502; long VTRS since 2026-11-12 00:00 @ 21.056314; long GWW since 2026-11-05 00:00 @ 1479.632738; long DIS since 2026-11-05 00:00 @ 119.905964; long WST since 2026-10-28 00:00 @ 396.819174; long ZBH since 2026-11-05 00:00 @ 111.0333 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 11,199.20 | 2,590.86 | 5,730.11 | 1,921.40 |
| return % | 111.99 | 25.91 | 57.30 | 19.21 |
| return %/year | 3.6 | 2.1 | 2.2 | 1.6 |
| gross profit | 26,522.06 | 7,912.08 | 18,096.74 | 6,643.71 |
| gross loss | 15,322.86 | 5,321.23 | 12,366.62 | 4,722.31 |
| trades | 10,770 | 5,717 | 11,209 | 5,736 |
| win rate % | 44.1 | 43.7 | 46.1 | 46.3 |
| avg win | 5.59 | 3.16 | 3.50 | 2.50 |
| avg loss | -2.54 | -1.65 | -2.05 | -1.53 |
| avg result / trade | 1.04 | 0.45 | 0.51 | 0.33 |
| largest single loss | -698.27 | -50.65 | -119.61 | -27.45 |
| largest loss % of equity | -37.76 | -20.77 | -20.91 | -13.70 |
| max drawdown | -1,396.93 | -481.96 | -568.92 | -341.99 |
| max drawdown % | -8.33 | -3.93 | -4.05 | -2.86 |
| profit factor | 1.73 | 1.49 | 1.46 | 1.41 |
| unusually bad trades | 941 | 449 | 782 | 330 |
| … threshold (% of equity) | 11.2 | 10.7 | 11.8 | 11.3 |
| time in market % | 18.3 | 18.3 | 13.8 | 13.5 |
| buy & hold return % | 1,772.23 | 471.27 | 1,772.23 | 471.27 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.59 |  | 0.75 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 6.2 | 4.8 |
| 1996 | 2.2 | 1.6 |
| 1997 | 5.5 | 4.5 |
| 1998 | 4.1 | 2.3 |
| 1999 | 5.3 | 4.0 |
| 2000 | 3.0 | 3.7 |
| 2001 | -3.0 | -1.8 |
| 2002 | -2.0 | -1.5 |
| 2003 | 9.2 | 6.3 |
| 2004 | 8.0 | 4.1 |
| 2005 | 8.1 | 2.8 |
| 2006 | -0.2 | 2.5 |
| 2007 | 4.5 | 0.7 |
| 2008 | -4.7 | -2.8 |
| 2009 | 4.3 | 2.7 |
| 2010 | 1.7 | 0.6 |
| 2011 | 4.3 | 1.3 |
| 2012 | 8.4 | 2.1 |
| 2013 | 7.6 | 6.2 |
| 2014 | 4.3 | 1.8 |
| 2015 | 0.8 | 0.4 |
| 2016 (OOS) | 1.8 | 1.7 |
| 2017 (OOS) | 7.9 | 5.9 |
| 2018 (OOS) | 1.8 | -1.1 |
| 2019 (OOS) | -0.9 | 0.9 |
| 2020 (OOS) | 1.2 | 3.2 |
| 2021 (OOS) | 2.4 | 2.1 |
| 2022 (OOS) | -0.5 | -1.3 |
| 2023 (OOS) | 0.5 | 0.4 |
| 2024 (OOS) | 7.4 | 5.2 |
| 2025 (OOS) | -0.4 | 0.2 |
| 2026 (OOS) | 2.1 | 1.9 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 8.3% from a peak in-sample and 3.9% out-of-sample, and the worst single trade cost 20.8% of the account out-of-sample. About 44 of every 100 trades won in-sample. Out-of-sample it earned 2.1% a year against 3.6% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 4.0% from a peak in-sample and 2.9% out-of-sample, and the worst single trade cost 13.7% of the account out-of-sample. About 46 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

### Range warnings

- max-income: `take_profit_atr` = 10.5 is at the max of its range (3 automatic extension(s) used, limit 3). The optimum may lie outside; widen SPACE in backtest.py if the value still makes sense.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 945 | `{"max_bars": 138, "n": 132, "stop_atr": 7.0, "take_profit_atr": 10.5}` | 11,270.67 | 3.7 | -8.3 | 44.1 | 2,594.48 | 2.1 | -3.9 | 0.58 | 10768/5716 | not checked |
| 949 | `{"max_bars": 138, "n": 132, "stop_atr": 6.75, "take_profit_atr": 10.5}` | 11,199.20 | 3.6 | -8.3 | 44.1 | 2,590.86 | 2.1 | -3.9 | 0.59 | 10770/5717 | 1.00 |
| 1006 | `{"max_bars": 132, "n": 132, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 10,870.45 | 3.6 | -7.0 | 43.4 | 2,589.72 | 2.1 | -3.9 | 0.60 | 10844/5745 | not checked |
| 972 | `{"max_bars": 138, "n": 138, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 10,502.75 | 3.5 | -6.9 | 42.4 | 2,462.08 | 2.0 | -3.8 | 0.59 | 10800/5717 | not checked |
| 1004 | `{"max_bars": 132, "n": 138, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 10,395.35 | 3.5 | -6.9 | 42.5 | 2,434.39 | 2.0 | -3.8 | 0.59 | 10805/5719 | not checked |
| 1024 | `{"max_bars": 144, "n": 144, "stop_atr": 4.0, "take_profit_atr": 10.5}` | 10,190.06 | 3.4 | -6.5 | 42.3 | 2,437.74 | 2.0 | -3.8 | 0.59 | 10663/5649 | not checked |
| 985 | `{"max_bars": 132, "n": 144, "stop_atr": 5.25, "take_profit_atr": 10.5}` | 10,030.22 | 3.4 | -6.5 | 43.6 | 2,488.53 | 2.1 | -3.8 | 0.61 | 10529/5591 | not checked |
| 1016 | `{"max_bars": 132, "n": 144, "stop_atr": 5.0, "take_profit_atr": 10.5}` | 9,844.08 | 3.3 | -6.4 | 43.5 | 2,507.38 | 2.1 | -3.8 | 0.63 | 10544/5597 | not checked |
| 962 | `{"max_bars": 126, "n": 144, "stop_atr": 4.75, "take_profit_atr": 10.5}` | 9,330.03 | 3.2 | -6.4 | 43.3 | 2,552.47 | 2.1 | -3.8 | 0.66 | 10571/5604 | not checked |
| 996 | `{"max_bars": 126, "n": 150, "stop_atr": 5.0, "take_profit_atr": 10.5}` | 9,207.87 | 3.2 | -6.2 | 43.5 | 2,495.00 | 2.1 | -3.8 | 0.66 | 10434/5541 | not checked |
| 961 | `{"max_bars": 138, "n": 162, "stop_atr": 7.0, "take_profit_atr": 10.5}` | 8,796.95 | 3.0 | -5.7 | 44.2 | 2,628.05 | 2.2 | -3.8 | 0.71 | 10165/5402 | not checked |
| 987 | `{"max_bars": 132, "n": 162, "stop_atr": 6.75, "take_profit_atr": 10.5}` | 8,664.70 | 3.0 | -5.7 | 44.2 | 2,597.70 | 2.1 | -3.8 | 0.71 | 10172/5405 | not checked |
| 997 | `{"max_bars": 138, "n": 174, "stop_atr": 7.0, "take_profit_atr": 10.5}` | 8,620.90 | 3.0 | -5.5 | 44.3 | 2,425.79 | 2.0 | -3.9 | 0.67 | 9965/5296 | not checked |
| 928 | `{"max_bars": 144, "n": 186, "stop_atr": 5.25, "take_profit_atr": 10.5}` | 8,279.63 | 2.9 | -5.5 | 43.9 | 2,290.62 | 1.9 | -3.7 | 0.66 | 9818/5205 | not checked |
| 931 | `{"max_bars": 138, "n": 156, "stop_atr": 6.75, "take_profit_atr": 9.5}` | 8,050.91 | 2.9 | -5.4 | 44.3 | 2,337.51 | 1.9 | -3.9 | 0.68 | 10433/5535 | not checked |
| 906 | `{"max_bars": 138, "n": 174, "stop_atr": 5.5, "take_profit_atr": 10.0}` | 7,607.78 | 2.7 | -5.4 | 44.0 | 2,318.42 | 1.9 | -3.7 | 0.71 | 10065/5347 | not checked |
| 908 | `{"max_bars": 84, "n": 174, "stop_atr": 5.25, "take_profit_atr": 9.5}` | 7,571.43 | 2.7 | -5.2 | 44.6 | 2,166.40 | 1.8 | -3.7 | 0.67 | 10307/5445 | not checked |
| 937 | `{"max_bars": 138, "n": 186, "stop_atr": 6.75, "take_profit_atr": 9.5}` | 7,307.28 | 2.6 | -5.2 | 44.5 | 2,080.75 | 1.8 | -3.9 | 0.66 | 9951/5269 | not checked |
| 936 | `{"max_bars": 162, "n": 186, "stop_atr": 5.25, "take_profit_atr": 9.5}` | 7,170.77 | 2.6 | -5.0 | 44.1 | 2,034.95 | 1.7 | -3.7 | 0.66 | 9979/5287 | not checked |
| 939 | `{"max_bars": 84, "n": 198, "stop_atr": 5.25, "take_profit_atr": 8.5}` | 6,568.86 | 2.4 | -4.9 | 44.7 | 2,005.47 | 1.7 | -3.5 | 0.69 | 10158/5282 | not checked |
| 680 | `{"max_bars": 102, "n": 174, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 6,112.10 | 2.3 | -4.5 | 46.5 | 1,992.38 | 1.7 | -3.0 | 0.73 | 11483/5919 | not checked |
| 635 | `{"max_bars": 102, "n": 180, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 6,022.24 | 2.3 | -4.3 | 46.5 | 1,871.52 | 1.6 | -2.9 | 0.70 | 11373/5854 | not checked |
| 695 | `{"max_bars": 102, "n": 186, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 6,010.78 | 2.3 | -4.2 | 46.5 | 1,848.12 | 1.6 | -2.9 | 0.69 | 11274/5798 | not checked |
| 827 | `{"max_bars": 102, "n": 186, "stop_atr": 4.75, "take_profit_atr": 5.5}` | 5,897.68 | 2.2 | -4.2 | 46.1 | 1,883.36 | 1.6 | -2.8 | 0.72 | 11312/5806 | not checked |
| 776 | `{"max_bars": 102, "n": 192, "stop_atr": 5.25, "take_profit_atr": 5.5}` | 5,826.86 | 2.2 | -4.1 | 46.6 | 1,885.82 | 1.6 | -2.9 | 0.72 | 11171/5728 | not checked |

(21 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 1,026 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
