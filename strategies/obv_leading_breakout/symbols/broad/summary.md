# obv_leading_breakout__broad: optimization summary

Updated 2026-11-25T08:22:00Z · backtest.py version `fc935c84ec` · 525 parameter sets tested with this version (525 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [obv_leading_breakout__broad__max-income__v002.md](obv_leading_breakout__broad__max-income__v002.md) | 525 | `{"max_candles": 36, "n": 5, "stop_atr": 3.5, "take_profit_atr": 8.0}` | long ABBV since 2026-11-24 00:00 @ 291.267347; long AES since 2026-11-17 00:00 @ 14.934479; long LNT since 2026-11-24 00:00 @ 72.811838; long ALL since 2026-11-13 00:00 @ 269.620871; long AEE since 2026-11-24 00:00 @ 112.643784; long AEP since 2026-11-17 00:00 @ 128.608578; long AZO since 2026-11-13 00:00 @ 3261.81834; long BDX since 2026-11-24 00:00 @ 214.324273; long BRO since 2026-11-19 00:00 @ 72.26167; long CTAS since 2026-11-24 00:00 @ 223.387003; long CMS since 2026-11-19 00:00 @ 69.160741; long CPRT since 2026-11-24 00:00 @ 31.669498; long DPZ since 2026-11-17 00:00 @ 346.1038; long DHI since 2026-11-24 00:00 @ 146.784027; long DUK since 2026-11-06 00:00 @ 126.174479; long ERIE since 2026-11-17 00:00 @ 273.211944; long EG since 2026-11-23 00:00 @ 418.89562; long EVRG since 2026-11-24 00:00 @ 86.956079; long ES since 2026-11-12 00:00 @ 71.271375; long EXC since 2026-10-28 00:00 @ 44.713411; long FDS since 2026-11-24 00:00 @ 312.573755; long GPN since 2026-11-23 00:00 @ 93.0279; long KDP since 2026-11-24 00:00 @ 35.515653; long KIM since 2026-11-23 00:00 @ 25.357605; long LOW since 2026-11-24 00:00 @ 226.257859; long MRSH since 2026-11-24 00:00 @ 208.102405; long ORLY since 2026-11-16 00:00 @ 93.0279; long PNR since 2026-11-19 00:00 @ 68.160441; long PGR since 2026-11-13 00:00 @ 238.0714; long PHM since 2026-11-24 00:00 @ 126.417911; long STE since 2026-11-24 00:00 @ 255.706694; long TGT since 2026-11-19 00:00 @ 167.020092; long TYL since 2026-11-02 00:00 @ 389.966961; long VRSN since 2026-11-24 00:00 @ 314.044197; long WRB since 2026-11-02 00:00 @ 74.092221 |
| balanced | none | | | |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS |
|---|---|---|
| net profit | 6,942.00 | 1,151.31 |
| return % | 69.42 | 11.51 |
| return %/year | 2.5 | 1.0 |
| gross profit | 44,881.36 | 19,460.65 |
| gross loss | 37,939.36 | 18,309.35 |
| trades | 80,294 | 50,196 |
| win rate % | 38.5 | 38.6 |
| avg win | 1.45 | 1.00 |
| avg loss | -0.77 | -0.59 |
| avg result / trade | 0.09 | 0.02 |
| largest single loss | -259.31 | -36.52 |
| largest loss % of equity | -7.62 | -17.75 |
| max drawdown | -1,960.34 | -788.96 |
| max drawdown % | -14.51 | -6.84 |
| profit factor | 1.18 | 1.06 |
| unusually bad trades | 10,807 | 6,397 |
| … threshold (% of equity) | 3.6 | 3.6 |
| time in market % | 22.7 | 27.3 |
| buy & hold return % | 1,875.86 | 478.58 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.40 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income |
|---|---|
| 1995 | 5.3 |
| 1996 | 1.8 |
| 1997 | 4.3 |
| 1998 | 3.1 |
| 1999 | 2.3 |
| 2000 | 3.6 |
| 2001 | -4.2 |
| 2002 | -3.9 |
| 2003 | 9.3 |
| 2004 | 4.0 |
| 2005 | -0.8 |
| 2006 | 2.9 |
| 2007 | 0.0 |
| 2008 | -9.2 |
| 2009 | 13.9 |
| 2010 | 4.3 |
| 2011 | -3.4 |
| 2012 | 3.5 |
| 2013 | 11.3 |
| 2014 | 7.4 |
| 2015 | 0.8 |
| 2016 (OOS) | 1.4 |
| 2017 (OOS) | 8.9 |
| 2018 (OOS) | -0.4 |
| 2019 (OOS) | 3.2 |
| 2020 (OOS) | 6.9 |
| 2021 (OOS) | 7.0 |
| 2022 (OOS) | -2.2 |
| 2023 (OOS) | 6.3 |
| 2024 (OOS) | 9.9 |
| 2025 (OOS) | -4.2 |
| 2026 (OOS) | -3.5 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 14.5% from a peak in-sample and 6.8% out-of-sample, and the worst single trade cost 17.8% of the account out-of-sample. About 39 of every 100 trades won in-sample. Out-of-sample it earned 1.0% a year against 2.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 69% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 473 | `{"max_candles": 24, "n": 5, "stop_atr": 4.0, "take_profit_atr": 8.5}` | 7,083.59 | 2.6 | -14.4 | 38.6 | 1,166.32 | 1.0 | -7.0 | 0.40 | 80534/50410 | not checked |
| 445 | `{"max_candles": 24, "n": 5, "stop_atr": 3.5, "take_profit_atr": 8.5}` | 6,796.11 | 2.5 | -14.3 | 38.6 | 1,160.62 | 1.0 | -6.9 | 0.40 | 80557/50431 | not checked |
| 520 | `{"max_candles": 30, "n": 5, "stop_atr": 4.0, "take_profit_atr": 7.5}` | 6,718.72 | 2.5 | -14.2 | 38.6 | 1,132.91 | 1.0 | -7.0 | 0.40 | 80521/50331 | not checked |
| 502 | `{"max_candles": 30, "n": 5, "stop_atr": 3.75, "take_profit_atr": 7.5}` | 6,474.34 | 2.4 | -14.2 | 38.6 | 1,142.66 | 1.0 | -7.0 | 0.41 | 80532/50338 | not checked |
| 416 | `{"max_candles": 24, "n": 5, "stop_atr": 2.5, "take_profit_atr": 8.5}` | 5,904.65 | 2.2 | -14.1 | 38.4 | 1,155.56 | 1.0 | -6.8 | 0.45 | 80821/50599 | not checked |
| 465 | `{"max_candles": 24, "n": 5, "stop_atr": 2.25, "take_profit_atr": 8.5}` | 5,827.25 | 2.2 | -14.1 | 38.3 | 1,083.33 | 0.9 | -7.0 | 0.43 | 81017/50729 | not checked |
| 480 | `{"max_candles": 42, "n": 7, "stop_atr": 3.5, "take_profit_atr": 8.5}` | 5,614.12 | 2.1 | -13.6 | 39.6 | 1,474.39 | 1.3 | -5.8 | 0.59 | 70758/44055 | not checked |
| 509 | `{"max_candles": 24, "n": 7, "stop_atr": 3.75, "take_profit_atr": 8.5}` | 5,578.81 | 2.1 | -13.5 | 39.6 | 1,488.28 | 1.3 | -5.7 | 0.60 | 71159/44355 | not checked |
| 501 | `{"max_candles": 24, "n": 7, "stop_atr": 3.0, "take_profit_atr": 8.5}` | 5,509.90 | 2.1 | -13.5 | 39.6 | 1,464.95 | 1.3 | -5.7 | 0.60 | 71242/44416 | not checked |
| 438 | `{"max_candles": 36, "n": 7, "stop_atr": 4.0, "take_profit_atr": 7.5}` | 5,229.41 | 2.0 | -13.3 | 39.6 | 1,510.32 | 1.3 | -6.0 | 0.64 | 71056/44208 | not checked |
| 468 | `{"max_candles": 30, "n": 7, "stop_atr": 3.5, "take_profit_atr": 7.5}` | 5,090.89 | 2.0 | -13.2 | 39.6 | 1,486.46 | 1.3 | -5.9 | 0.65 | 71153/44293 | not checked |
| 450 | `{"max_candles": 48, "n": 7, "stop_atr": 2.25, "take_profit_atr": 7.5}` | 4,399.91 | 1.8 | -13.1 | 39.3 | 1,453.63 | 1.2 | -6.2 | 0.71 | 71536/44523 | not checked |
| 472 | `{"max_candles": 36, "n": 9, "stop_atr": 3.75, "take_profit_atr": 8.5}` | 3,980.29 | 1.6 | -12.8 | 40.1 | 1,383.17 | 1.2 | -5.6 | 0.74 | 64265/40322 | not checked |
| 461 | `{"max_candles": 36, "n": 9, "stop_atr": 4.0, "take_profit_atr": 7.5}` | 3,841.97 | 1.6 | -12.5 | 40.1 | 1,380.55 | 1.2 | -5.7 | 0.77 | 64542/40462 | not checked |
| 431 | `{"max_candles": 36, "n": 15, "stop_atr": 3.5, "take_profit_atr": 8.5}` | 3,574.91 | 1.5 | -11.2 | 40.6 | 1,022.91 | 0.9 | -5.2 | 0.61 | 54253/34567 | not checked |
| 443 | `{"max_candles": 24, "n": 21, "stop_atr": 3.5, "take_profit_atr": 8.5}` | 3,344.38 | 1.4 | -10.7 | 40.9 | 873.60 | 0.8 | -4.1 | 0.56 | 49430/31639 | not checked |
| 367 | `{"max_candles": 72, "n": 22, "stop_atr": 2.75, "take_profit_atr": 6.5}` | 3,094.18 | 1.3 | -10.7 | 40.8 | 772.03 | 0.7 | -4.2 | 0.54 | 49139/31425 | not checked |
| 359 | `{"max_candles": 72, "n": 24, "stop_atr": 2.75, "take_profit_atr": 6.5}` | 3,067.48 | 1.3 | -10.4 | 40.8 | 704.60 | 0.6 | -4.1 | 0.49 | 47921/30675 | not checked |
| 351 | `{"max_candles": 30, "n": 24, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 2,923.01 | 1.2 | -10.2 | 40.9 | 673.68 | 0.6 | -4.2 | 0.49 | 48059/30747 | not checked |
| 361 | `{"max_candles": 24, "n": 24, "stop_atr": 3.5, "take_profit_atr": 6.0}` | 2,909.27 | 1.2 | -10.2 | 40.9 | 685.36 | 0.6 | -4.2 | 0.50 | 48193/30848 | not checked |
| 457 | `{"max_candles": 24, "n": 31, "stop_atr": 4.0, "take_profit_atr": 8.0}` | 2,774.81 | 1.2 | -9.9 | 40.9 | 606.17 | 0.5 | -4.2 | 0.46 | 44403/28593 | not checked |
| 373 | `{"max_candles": 54, "n": 28, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 2,507.99 | 1.1 | -9.8 | 40.9 | 693.56 | 0.6 | -4.4 | 0.58 | 45595/29285 | not checked |
| 362 | `{"max_candles": 48, "n": 32, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 2,428.25 | 1.0 | -9.7 | 40.9 | 647.78 | 0.6 | -4.2 | 0.56 | 43966/28345 | not checked |
| 365 | `{"max_candles": 54, "n": 36, "stop_atr": 4.0, "take_profit_atr": 7.0}` | 2,082.89 | 0.9 | -9.6 | 40.9 | 580.53 | 0.5 | -4.2 | 0.57 | 42594/27545 | not checked |
| 146 | `{"max_candles": 60, "n": 30, "stop_atr": 3.5, "take_profit_atr": 5.0}` | 2,012.18 | 0.9 | -9.5 | 41.0 | 458.18 | 0.4 | -4.6 | 0.47 | 45915/29423 | not checked |

(8 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 525 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
