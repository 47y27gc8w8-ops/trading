# chaikin_oscillator_cross__broad: optimization summary

Updated 2026-11-25T17:27:41Z · backtest.py version `71317483c0` · 404 parameter sets tested with this version (404 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, CDW, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [chaikin_oscillator_cross__broad__max-income__v002.md](chaikin_oscillator_cross__broad__max-income__v002.md) | 404 | `{"max_bars": 42, "n": 10, "stop_atr": 4.75, "take_profit_atr": 7.5}` | long NESN.SW since 2026-10-15 00:00 @ 80.144039; long CFR.SW since 2026-11-02 00:00 @ 163.849143; long GIVN.SW since 2026-10-14 00:00 @ 3818.1451; long SREN.SW since 2026-11-24 00:00 @ 151.0453; long SOON.SW since 2026-10-12 00:00 @ 266.0798; long ARE since 2026-11-03 00:00 @ 42.172648; long AWK since 2026-10-23 00:00 @ 142.18748; long BAX since 2026-11-04 00:00 @ 26.247872; long BIIB since 2026-11-24 00:00 @ 259.907936; long CHRW since 2026-11-11 00:00 @ 129.088718; long CHTR since 2026-10-28 00:00 @ 104.961479; long CMG since 2026-10-30 00:00 @ 31.679501; long CMS since 2026-11-10 00:00 @ 69.320793; long KO since 2026-11-10 00:00 @ 96.678997; long CL since 2026-11-12 00:00 @ 98.929672; long CSGP since 2026-11-24 00:00 @ 30.209061; long DLTR since 2026-11-11 00:00 @ 139.921969; long DPZ since 2026-10-12 00:00 @ 310.463106; long DUK since 2026-11-19 00:00 @ 128.848641; long EIX since 2026-10-06 00:00 @ 53.614358; long ES since 2026-11-11 00:00 @ 69.26077; long FICO since 2026-11-09 00:00 @ 704.911422; long FE since 2026-11-05 00:00 @ 47.074872; long GIS since 2026-11-23 00:00 @ 34.790433; long HSIC since 2026-11-19 00:00 @ 85.225557; long HRL since 2026-11-19 00:00 @ 22.806839; long IFF since 2026-11-24 00:00 @ 82.634784; long MKC since 2026-11-24 00:00 @ 47.999396; long MGM since 2026-11-02 00:00 @ 30.239069; long NOC since 2026-11-12 00:00 @ 555.276518; long PCG since 2026-10-02 00:00 @ 12.343702; long PEG since 2026-10-07 00:00 @ 71.701504; long SJM since 2026-11-10 00:00 @ 132.166446; long TSCO since 2026-11-02 00:00 @ 34.460336; long WRB since 2026-11-04 00:00 @ 76.442924; long WMT since 2026-11-10 00:00 @ 125.697702; long WM since 2026-11-24 00:00 @ 241.36238; long WYNN since 2026-11-05 00:00 @ 81.953069; long YUM since 2026-11-20 00:00 @ 161.428419 |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 10,847.13 | 3,810.09 |
| return % | 108.47 | 38.10 |
| return %/year | 3.6 | 3.0 |
| gross profit | 88,711.45 | 38,173.90 |
| gross loss | 77,864.32 | 34,363.81 |
| trades | 105,613 | 68,775 |
| win rate % | 38.0 | 38.5 |
| avg win | 2.21 | 1.44 |
| avg loss | -1.19 | -0.81 |
| avg result / trade | 0.10 | 0.06 |
| largest single loss | -115.69 | -37.32 |
| largest loss % of equity | -14.04 | -27.73 |
| max drawdown | -6,315.48 | -2,363.80 |
| max drawdown % | -33.79 | -17.81 |
| profit factor | 1.14 | 1.11 |
| unusually bad trades | 14,425 | 9,133 |
| … threshold (% of equity) | 4.8 | 4.4 |
| time in market % | 41.3 | 48.1 |
| buy & hold return % | 1,824.49 | 466.47 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.85 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 1995 | 9.8 |
| 1996 | 5.9 |
| 1997 | 6.4 |
| 1998 | 5.8 |
| 1999 | 2.1 |
| 2000 | 6.8 |
| 2001 | 0.6 |
| 2002 | -12.0 |
| 2003 | 18.8 |
| 2004 | 9.6 |
| 2005 | 6.6 |
| 2006 | 2.8 |
| 2007 | -3.5 |
| 2008 | -20.4 |
| 2009 | 19.4 |
| 2010 | 9.2 |
| 2011 | -6.3 |
| 2012 | 7.4 |
| 2013 | 13.0 |
| 2014 | 8.5 |
| 2015 | -6.3 |
| 2016 (OOS) | 6.5 |
| 2017 (OOS) | 11.2 |
| 2018 (OOS) | -2.1 |
| 2019 (OOS) | 12.0 |
| 2020 (OOS) | 1.1 |
| 2021 (OOS) | 3.8 |
| 2022 (OOS) | -12.3 |
| 2023 (OOS) | 6.0 |
| 2024 (OOS) | 10.0 |
| 2025 (OOS) | -2.1 |
| 2026 (OOS) | 1.4 |

### Risk in plain language

- **max-income**: Risk looks high: the account fell up to 33.8% from a peak in-sample and 17.8% out-of-sample, and the worst single trade cost 27.7% of the account out-of-sample. About 38 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 30% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 335 | `{"max_bars": 42, "n": 7, "stop_atr": 4.75, "take_profit_atr": 8.5}` | 11,252.28 | 3.7 | -33.5 | 37.9 | 3,624.87 | 2.9 | -18.2 | 0.79 | 106765/69319 | not checked |
| 306 | `{"max_bars": 42, "n": 7, "stop_atr": 4.75, "take_profit_atr": 7.5}` | 10,786.31 | 3.5 | -33.4 | 37.9 | 3,568.00 | 2.8 | -18.0 | 0.80 | 106765/69319 | not checked |
| 339 | `{"max_bars": 42, "n": 7, "stop_atr": 5.75, "take_profit_atr": 7.5}` | 10,603.41 | 3.5 | -33.2 | 37.9 | 3,310.58 | 2.7 | -18.9 | 0.76 | 106689/69309 | not checked |
| 382 | `{"max_bars": 30, "n": 7, "stop_atr": 4.5, "take_profit_atr": 8.5}` | 10,427.48 | 3.5 | -31.5 | 38.1 | 3,545.69 | 2.8 | -17.8 | 0.82 | 106780/69320 | not checked |
| 393 | `{"max_bars": 24, "n": 9, "stop_atr": 4.75, "take_profit_atr": 8.5}` | 10,405.96 | 3.5 | -31.1 | 38.5 | 3,038.34 | 2.5 | -17.7 | 0.71 | 105694/68810 | not checked |
| 350 | `{"max_bars": 24, "n": 17, "stop_atr": 5.25, "take_profit_atr": 8.5}` | 8,336.58 | 2.9 | -30.5 | 38.7 | 2,549.80 | 2.1 | -16.7 | 0.72 | 98955/64513 | not checked |
| 394 | `{"max_bars": 30, "n": 19, "stop_atr": 5.25, "take_profit_atr": 8.5}` | 8,157.76 | 2.9 | -29.5 | 38.4 | 2,581.12 | 2.1 | -16.0 | 0.74 | 92986/60240 | not checked |
| 265 | `{"max_bars": 48, "n": 20, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 7,600.92 | 2.7 | -29.3 | 38.2 | 2,191.07 | 1.8 | -14.6 | 0.67 | 90143/58080 | not checked |
| 395 | `{"max_bars": 48, "n": 23, "stop_atr": 4.75, "take_profit_atr": 7.0}` | 7,272.46 | 2.6 | -29.1 | 38.1 | 2,256.58 | 1.9 | -14.0 | 0.72 | 83288/53085 | not checked |
| 336 | `{"max_bars": 24, "n": 19, "stop_atr": 4.75, "take_profit_atr": 6.5}` | 7,196.02 | 2.6 | -28.6 | 38.8 | 2,061.12 | 1.7 | -15.1 | 0.66 | 92997/60244 | not checked |
| 340 | `{"max_bars": 24, "n": 19, "stop_atr": 4.75, "take_profit_atr": 6.0}` | 7,166.55 | 2.6 | -28.4 | 38.8 | 1,972.30 | 1.7 | -14.9 | 0.64 | 92997/60244 | not checked |
| 180 | `{"max_bars": 78, "n": 26, "stop_atr": 3.25, "take_profit_atr": 6.0}` | 6,490.46 | 2.4 | -27.3 | 38.0 | 2,002.22 | 1.7 | -12.0 | 0.70 | 78772/49764 | not checked |
| 323 | `{"max_bars": 48, "n": 27, "stop_atr": 3.75, "take_profit_atr": 6.0}` | 6,341.86 | 2.4 | -26.5 | 38.1 | 1,830.38 | 1.6 | -12.5 | 0.66 | 77636/48951 | not checked |
| 119 | `{"max_bars": 24, "n": 22, "stop_atr": 2.5, "take_profit_atr": 5.5}` | 5,636.35 | 2.1 | -25.9 | 38.2 | 1,780.98 | 1.5 | -12.6 | 0.71 | 85261/54485 | not checked |
| 387 | `{"max_bars": 54, "n": 45, "stop_atr": 4.75, "take_profit_atr": 8.5}` | 5,411.08 | 2.1 | -24.4 | 37.9 | 1,521.38 | 1.3 | -12.6 | 0.63 | 70913/43679 | not checked |
| 269 | `{"max_bars": 42, "n": 28, "stop_atr": 3.25, "take_profit_atr": 4.5}` | 5,042.29 | 2.0 | -24.3 | 38.4 | 1,440.85 | 1.2 | -11.5 | 0.63 | 76678/48181 | not checked |
| 139 | `{"max_bars": 30, "n": 26, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 4,972.18 | 1.9 | -24.1 | 38.9 | 1,017.96 | 0.9 | -12.8 | 0.46 | 78771/49764 | not checked |
| 148 | `{"max_bars": 54, "n": 34, "stop_atr": 2.75, "take_profit_atr": 5.5}` | 4,645.93 | 1.8 | -23.9 | 37.7 | 1,536.90 | 1.3 | -10.4 | 0.72 | 73054/45400 | not checked |
| 102 | `{"max_bars": 90, "n": 30, "stop_atr": 3.0, "take_profit_atr": 4.5}` | 4,570.12 | 1.8 | -23.6 | 38.1 | 1,235.93 | 1.1 | -11.3 | 0.60 | 75132/46925 | not checked |
| 120 | `{"max_bars": 60, "n": 44, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 4,563.83 | 1.8 | -22.7 | 37.9 | 1,176.18 | 1.0 | -10.8 | 0.57 | 70939/43723 | not checked |
| 215 | `{"max_bars": 72, "n": 36, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 4,462.54 | 1.8 | -21.4 | 38.2 | 1,044.48 | 0.9 | -10.7 | 0.52 | 72322/44866 | not checked |
| 235 | `{"max_bars": 78, "n": 38, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 4,382.45 | 1.8 | -20.9 | 38.2 | 967.84 | 0.8 | -10.8 | 0.49 | 71738/44468 | not checked |
| 208 | `{"max_bars": 30, "n": 38, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 4,259.31 | 1.7 | -20.2 | 38.6 | 873.02 | 0.8 | -11.2 | 0.45 | 71735/44468 | not checked |
| 241 | `{"max_bars": 24, "n": 44, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 3,442.59 | 1.4 | -20.1 | 38.7 | 610.88 | 0.6 | -11.2 | 0.39 | 70936/43723 | not checked |
| 223 | `{"max_bars": 90, "n": 38, "stop_atr": 3.75, "take_profit_atr": 3.5}` | 3,356.99 | 1.4 | -19.9 | 39.0 | 446.75 | 0.4 | -11.0 | 0.29 | 71737/44468 | not checked |

(4 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 404 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
