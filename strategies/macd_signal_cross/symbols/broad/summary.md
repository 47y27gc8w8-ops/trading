# macd_signal_cross__broad: optimization summary

Updated 2026-11-26T06:53:38Z · backtest.py version `33b128069d` · 458 parameter sets tested with this version (458 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [macd_signal_cross__broad__max-income__v002.md](macd_signal_cross__broad__max-income__v002.md) | 457 | `{"max_candles": 80, "signal": 20, "stop_atr": 4.0, "take_profit_atr": 6.5}` | long CFR.SW since 2026-11-06 00:00 @ 169.450814; long LOGN.SW since 2026-11-20 00:00 @ 84.165241; long AES since 2026-11-17 00:00 @ 14.934479; long BAX since 2026-11-24 00:00 @ 26.317892; long DRI since 2026-10-15 00:00 @ 211.973577; long DXCM since 2026-11-24 00:00 @ 81.744517; long ESS since 2026-11-06 00:00 @ 267.130103; long FRT since 2026-11-25 00:00 @ 113.193952; long FTNT since 2026-11-25 00:00 @ 128.82863; long DOC since 2026-10-23 00:00 @ 19.357203; long INCY since 2026-11-25 00:00 @ 123.707099; long IVZ since 2026-11-10 00:00 @ 28.730069; long JKHY since 2026-11-25 00:00 @ 178.563548; long LYV since 2026-10-06 00:00 @ 169.510845; long PANW since 2026-11-24 00:00 @ 349.1047; long SYY since 2026-11-24 00:00 @ 80.044003; long TGT since 2026-11-03 00:00 @ 157.131037; long WMT since 2026-11-25 00:00 @ 132.667794; long YUM since 2026-11-24 00:00 @ 165.949764; long ZBH since 2026-11-25 00:00 @ 108.732607 |
| balanced | [macd_signal_cross__broad__balanced__v002.md](macd_signal_cross__broad__balanced__v002.md) | 458 | `{"max_candles": 64, "signal": 18, "stop_atr": 3.75, "take_profit_atr": 2.0}` | long LOGN.SW since 2026-11-19 00:00 @ 86.0258; long AON since 2026-11-25 00:00 @ 344.913441; long BAX since 2026-11-24 00:00 @ 26.317892; long CPRT since 2026-11-25 00:00 @ 32.549763; long DXCM since 2026-11-13 00:00 @ 82.034605; long DLTR since 2026-11-25 00:00 @ 155.509133; long ESS since 2026-11-09 00:00 @ 274.182236; long FTNT since 2026-11-25 00:00 @ 128.82863; long DOC since 2026-11-24 00:00 @ 19.965987; long INCY since 2026-11-25 00:00 @ 123.707099; long IVZ since 2026-11-10 00:00 @ 28.730069; long LYV since 2026-11-24 00:00 @ 180.644173; long OMC since 2026-11-25 00:00 @ 88.876653; long PANW since 2026-11-23 00:00 @ 361.928553; long REGN since 2026-11-25 00:00 @ 985.2955; long SYY since 2026-11-24 00:00 @ 80.044003; long WTW since 2026-11-25 00:00 @ 350.094987; long YUM since 2026-11-25 00:00 @ 167.0501; long ZBH since 2026-11-25 00:00 @ 108.732607 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 6,815.63 | 2,973.45 | 2,420.08 | 1,292.31 |
| return % | 68.16 | 29.73 | 24.20 | 12.92 |
| return %/year | 2.5 | 2.4 | 1.0 | 1.1 |
| gross profit | 35,228.95 | 16,479.71 | 23,643.62 | 12,390.69 |
| gross loss | 28,413.31 | 13,506.26 | 21,223.54 | 11,098.38 |
| trades | 44,467 | 25,444 | 46,070 | 26,364 |
| win rate % | 38.8 | 39.2 | 46.7 | 47.6 |
| avg win | 2.04 | 1.65 | 1.10 | 0.99 |
| avg loss | -1.04 | -0.87 | -0.86 | -0.80 |
| avg result / trade | 0.15 | 0.12 | 0.05 | 0.05 |
| largest single loss | -54.72 | -39.95 | -19.78 | -20.29 |
| largest loss % of equity | -44.41 | -34.83 | -20.02 | -15.99 |
| max drawdown | -1,356.93 | -702.21 | -857.32 | -492.82 |
| max drawdown % | -9.48 | -5.38 | -7.41 | -4.33 |
| profit factor | 1.24 | 1.22 | 1.11 | 1.12 |
| unusually bad trades | 5,187 | 2,876 | 4,448 | 2,458 |
| … threshold (% of equity) | 5.3 | 5.3 | 5.5 | 5.5 |
| time in market % | 22.5 | 25.2 | 12.6 | 14.0 |
| buy & hold return % | 1,777.75 | 470.42 | 1,777.75 | 470.42 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.96 |  | 1.08 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 5.3 | 2.7 |
| 1996 | 3.1 | 1.2 |
| 1997 | 7.5 | 2.7 |
| 1998 | 3.3 | -0.1 |
| 1999 | 2.9 | 0.4 |
| 2000 | 1.2 | 0.9 |
| 2001 | -2.0 | -0.5 |
| 2002 | -4.2 | -2.6 |
| 2003 | 6.5 | 3.8 |
| 2004 | 6.3 | 2.6 |
| 2005 | 2.8 | 1.4 |
| 2006 | 0.4 | -0.0 |
| 2007 | 1.4 | 1.2 |
| 2008 | -5.2 | -4.6 |
| 2009 | 5.6 | 3.6 |
| 2010 | 5.4 | 2.9 |
| 2011 | -2.1 | -0.2 |
| 2012 | 0.6 | -0.0 |
| 2013 | 11.8 | 6.6 |
| 2014 | 5.1 | 2.8 |
| 2015 | -1.5 | -2.3 |
| 2016 (OOS) | 1.3 | -0.2 |
| 2017 (OOS) | 5.9 | 3.3 |
| 2018 (OOS) | -2.2 | -1.4 |
| 2019 (OOS) | 3.9 | 3.1 |
| 2020 (OOS) | 4.9 | 2.9 |
| 2021 (OOS) | 10.7 | 5.5 |
| 2022 (OOS) | -2.6 | -2.5 |
| 2023 (OOS) | 1.8 | -0.6 |
| 2024 (OOS) | 5.0 | 3.1 |
| 2025 (OOS) | -3.3 | -2.1 |
| 2026 (OOS) | 2.2 | 1.0 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 9.5% from a peak in-sample and 5.4% out-of-sample, and the worst single trade cost 34.8% of the account out-of-sample. About 39 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 7.4% from a peak in-sample and 4.3% out-of-sample, and the worst single trade cost 16.0% of the account out-of-sample. About 47 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 447 | `{"max_candles": 80, "signal": 19, "stop_atr": 4.0, "take_profit_atr": 6.5}` | 6,824.98 | 2.5 | -9.2 | 38.9 | 2,897.22 | 2.4 | -5.6 | 0.94 | 45210/25895 | not checked |
| 440 | `{"max_candles": 104, "signal": 20, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,036.23 | 2.0 | -9.0 | 39.5 | 2,274.75 | 1.9 | -4.8 | 0.97 | 44467/25444 | not checked |
| 441 | `{"max_candles": 80, "signal": 20, "stop_atr": 3.5, "take_profit_atr": 4.0}` | 5,036.23 | 2.0 | -9.0 | 39.5 | 2,274.75 | 1.9 | -4.8 | 0.97 | 44467/25444 | not checked |
| 402 | `{"max_candles": 104, "signal": 20, "stop_atr": 3.75, "take_profit_atr": 4.0}` | 5,009.24 | 1.9 | -9.0 | 39.5 | 2,314.07 | 1.9 | -4.7 | 0.99 | 44467/25444 | not checked |
| 439 | `{"max_candles": 96, "signal": 20, "stop_atr": 3.5, "take_profit_atr": 3.5}` | 4,577.25 | 1.8 | -8.8 | 40.1 | 1,950.96 | 1.6 | -4.4 | 0.91 | 44467/25444 | not checked |
| 443 | `{"max_candles": 88, "signal": 20, "stop_atr": 3.5, "take_profit_atr": 3.5}` | 4,577.25 | 1.8 | -8.8 | 40.1 | 1,950.96 | 1.6 | -4.4 | 0.91 | 44467/25444 | not checked |
| 431 | `{"max_candles": 104, "signal": 19, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 4,555.35 | 1.8 | -8.6 | 40.1 | 1,882.58 | 1.6 | -4.5 | 0.89 | 45210/25895 | not checked |
| 421 | `{"max_candles": 104, "signal": 19, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 3,922.11 | 1.6 | -8.4 | 41.2 | 1,720.15 | 1.5 | -4.4 | 0.93 | 45210/25895 | not checked |
| 423 | `{"max_candles": 80, "signal": 19, "stop_atr": 3.5, "take_profit_atr": 2.5}` | 3,382.78 | 1.4 | -8.0 | 43.3 | 1,499.61 | 1.3 | -4.1 | 0.92 | 45210/25895 | not checked |
| 411 | `{"max_candles": 104, "signal": 20, "stop_atr": 4.0, "take_profit_atr": 2.5}` | 3,276.49 | 1.4 | -8.0 | 43.3 | 1,604.54 | 1.4 | -4.1 | 1.01 | 44467/25444 | not checked |
| 445 | `{"max_candles": 64, "signal": 19, "stop_atr": 4.0, "take_profit_atr": 2.0}` | 2,465.08 | 1.1 | -7.2 | 46.9 | 1,237.81 | 1.1 | -3.9 | 1.02 | 45210/25895 | not checked |
| 403 | `{"max_candles": 104, "signal": 20, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 1,591.02 | 0.7 | -6.4 | 52.9 | 890.79 | 0.8 | -3.3 | 1.11 | 44467/25444 | not checked |
| 415 | `{"max_candles": 88, "signal": 18, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,474.33 | 0.7 | -6.3 | 52.6 | 870.08 | 0.8 | -4.1 | 1.17 | 46070/26364 | not checked |
| 195 | `{"max_candles": 176, "signal": 13, "stop_atr": 1.0, "take_profit_atr": 2.0}` | 351.37 | 0.2 | -6.3 | 36.2 | 282.63 | 0.3 | -3.0 | 1.62 | 51418/29354 | not checked |

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 458 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
