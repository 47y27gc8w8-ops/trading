# market_residual_stock_rebound__broad: optimization summary

Updated 2026-11-26T07:57:04Z · backtest.py version `72cfa30140` · 615 parameter sets tested with this version (615 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [market_residual_stock_rebound__broad__max-income__v002.md](market_residual_stock_rebound__broad__max-income__v002.md) | 614 | `{"max_candles": 28, "n": 63, "stop_atr": 5.75, "take_profit_atr": 4.0, "z": 0.5}` | long AMD since 2026-11-16 00:00 @ 503.601047; long MO since 2026-11-18 00:00 @ 76.963084; long AXP since 2026-11-12 00:00 @ 324.727394; long CNC since 2026-11-19 00:00 @ 67.660291; long STZ since 2026-11-18 00:00 @ 142.492732; long ELV since 2026-11-19 00:00 @ 402.35068; long EOG since 2026-11-19 00:00 @ 152.195639; long EQIX since 2026-11-16 00:00 @ 1036.478263; long XOM since 2026-11-19 00:00 @ 161.378401; long FAST since 2026-11-18 00:00 @ 54.416322; long FDX since 2026-11-18 00:00 @ 317.605263; long HAS since 2026-11-16 00:00 @ 120.469565; long JPM since 2026-11-17 00:00 @ 333.670078; long MPC since 2026-11-17 00:00 @ 406.668389; long MDT since 2026-11-19 00:00 @ 100.53015; long MNST since 2026-11-18 00:00 @ 44.133235; long NEM since 2026-11-11 00:00 @ 120.005992; long NTRS since 2026-11-18 00:00 @ 172.181644; long OXY since 2026-11-17 00:00 @ 57.817339; long OKE since 2026-11-17 00:00 @ 88.456529; long PM since 2026-11-17 00:00 @ 194.748409; long PSX since 2026-11-19 00:00 @ 246.183834; long PNW since 2026-11-17 00:00 @ 105.471634; long STLD since 2026-11-16 00:00 @ 229.348783; long UNP since 2026-11-18 00:00 @ 297.35917; long VLO since 2026-11-18 00:00 @ 359.364221; long VTR since 2026-11-13 00:00 @ 89.976982; long GWW since 2026-11-18 00:00 @ 1456.4368; long WST since 2026-11-18 00:00 @ 413.013882 |
| balanced | [market_residual_stock_rebound__broad__balanced__v002.md](market_residual_stock_rebound__broad__balanced__v002.md) | 615 | `{"max_candles": 28, "n": 84, "stop_atr": 4.5, "take_profit_atr": 4.0, "z": 1.25}` | long AMD since 2026-11-16 00:00 @ 503.601047; long MO since 2026-11-18 00:00 @ 76.963084; long CNC since 2026-11-19 00:00 @ 67.660291; long ELV since 2026-11-19 00:00 @ 402.35068; long EOG since 2026-11-19 00:00 @ 152.195639; long XOM since 2026-11-19 00:00 @ 161.378401; long JPM since 2026-11-18 00:00 @ 327.618245; long MPC since 2026-11-17 00:00 @ 406.668389; long MNST since 2026-11-18 00:00 @ 44.133235; long OXY since 2026-11-17 00:00 @ 57.817339; long OKE since 2026-11-17 00:00 @ 88.456529; long PSX since 2026-11-19 00:00 @ 246.183834; long PNW since 2026-11-18 00:00 @ 102.410711; long STLD since 2026-11-16 00:00 @ 229.348783; long UNP since 2026-11-18 00:00 @ 297.35917; long VLO since 2026-11-19 00:00 @ 340.946024; long WST since 2026-11-19 00:00 @ 407.202111 |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 6,840.76 | 1,691.64 | 3,671.29 | 824.33 |
| return % | 68.41 | 16.92 | 36.71 | 8.24 |
| return %/year | 2.5 | 1.4 | 1.5 | 0.7 |
| gross profit | 44,185.68 | 20,144.96 | 20,171.29 | 10,165.80 |
| gross loss | 37,344.92 | 18,453.32 | 16,500.00 | 9,341.47 |
| trades | 123,228 | 78,432 | 57,999 | 38,088 |
| win rate % | 63.0 | 63.3 | 62.9 | 62.4 |
| avg win | 0.57 | 0.41 | 0.55 | 0.43 |
| avg loss | -0.82 | -0.64 | -0.77 | -0.65 |
| avg result / trade | 0.06 | 0.02 | 0.06 | 0.02 |
| largest single loss | -89.09 | -40.41 | -32.27 | -15.22 |
| largest loss % of equity | -31.78 | -23.75 | -23.36 | -27.24 |
| max drawdown | -1,095.03 | -981.04 | -419.28 | -556.92 |
| max drawdown % | -6.89 | -9.12 | -3.17 | -5.43 |
| profit factor | 1.18 | 1.09 | 1.22 | 1.09 |
| unusually bad trades | 13,639 | 8,670 | 6,161 | 4,088 |
| … threshold (% of equity) | 2.7 | 2.8 | 3.1 | 3.3 |
| time in market % | 16.9 | 20.9 | 8.5 | 11.1 |
| buy & hold return % | 1,774.45 | 471.20 | 1,774.45 | 471.20 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.58 |  | 0.49 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 5.4 | 4.5 |
| 1996 | 1.7 | 1.6 |
| 1997 | 8.1 | 4.9 |
| 1998 | 2.8 | 1.0 |
| 1999 | 4.0 | 2.3 |
| 2000 | 3.9 | 4.2 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.4 | -0.0 |
| 2003 | 8.4 | 4.9 |
| 2004 | 0.9 | 0.8 |
| 2005 | 1.5 | 0.8 |
| 2006 | 1.9 | 0.5 |
| 2007 | 0.8 | 0.3 |
| 2008 | -1.0 | -0.2 |
| 2009 | 4.6 | 1.6 |
| 2010 | -0.2 | -0.4 |
| 2011 | -1.3 | -0.9 |
| 2012 | 2.5 | 1.5 |
| 2013 | 8.6 | 3.6 |
| 2014 | -0.2 | -0.3 |
| 2015 | 0.8 | 1.1 |
| 2016 (OOS) | 0.9 | -0.1 |
| 2017 (OOS) | 4.8 | 1.3 |
| 2018 (OOS) | -6.7 | -3.5 |
| 2019 (OOS) | 1.2 | 0.5 |
| 2020 (OOS) | 4.7 | 2.0 |
| 2021 (OOS) | 7.8 | 4.8 |
| 2022 (OOS) | -4.1 | -2.6 |
| 2023 (OOS) | 2.3 | 1.1 |
| 2024 (OOS) | 3.9 | 1.1 |
| 2025 (OOS) | 3.2 | 1.6 |
| 2026 (OOS) | 0.2 | 0.7 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 6.9% from a peak in-sample and 9.1% out-of-sample, and the worst single trade cost 23.8% of the account out-of-sample. About 63 of every 100 trades won in-sample. Out-of-sample it earned 1.4% a year against 2.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.2% from a peak in-sample and 5.4% out-of-sample, and the worst single trade cost 27.2% of the account out-of-sample. About 63 of every 100 trades won in-sample. Out-of-sample it earned 0.7% a year against 1.5% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 569 | `{"max_candles": 24, "n": 21, "stop_atr": 6.75, "take_profit_atr": 3.5, "z": 0.5}` | 7,167.58 | 2.6 | -7.2 | 62.9 | 2,017.22 | 1.7 | -9.1 | 0.65 | 126838/81079 | not checked |
| 610 | `{"max_candles": 24, "n": 21, "stop_atr": 5.75, "take_profit_atr": 3.5, "z": 0.5}` | 6,944.07 | 2.5 | -6.7 | 62.9 | 1,906.66 | 1.6 | -9.2 | 0.64 | 126996/81200 | not checked |
| 611 | `{"max_candles": 28, "n": 42, "stop_atr": 5.75, "take_profit_atr": 3.5, "z": 0.5}` | 6,675.42 | 2.5 | -6.6 | 62.9 | 1,797.21 | 1.5 | -9.2 | 0.62 | 124486/79522 | not checked |
| 603 | `{"max_candles": 28, "n": 21, "stop_atr": 6.25, "take_profit_atr": 4.0, "z": 0.75}` | 6,629.01 | 2.5 | -6.6 | 63.1 | 1,789.47 | 1.5 | -8.5 | 0.62 | 111248/71588 | not checked |
| 594 | `{"max_candles": 28, "n": 21, "stop_atr": 5.75, "take_profit_atr": 4.0, "z": 0.75}` | 6,536.39 | 2.4 | -6.3 | 63.1 | 1,752.84 | 1.5 | -8.4 | 0.62 | 111322/71650 | not checked |
| 537 | `{"max_candles": 28, "n": 63, "stop_atr": 5.75, "take_profit_atr": 3.5, "z": 0.75}` | 6,408.08 | 2.4 | -5.7 | 63.2 | 1,386.99 | 1.2 | -8.2 | 0.50 | 103149/65988 | not checked |
| 533 | `{"max_candles": 28, "n": 84, "stop_atr": 5.75, "take_profit_atr": 4.0, "z": 0.75}` | 6,120.74 | 2.3 | -5.5 | 63.2 | 1,418.94 | 1.2 | -8.2 | 0.54 | 101518/64826 | not checked |
| 607 | `{"max_candles": 44, "n": 21, "stop_atr": 5.25, "take_profit_atr": 5.0, "z": 1.0}` | 5,715.92 | 2.2 | -5.1 | 63.3 | 1,383.51 | 1.2 | -7.7 | 0.55 | 93062/60645 | not checked |
| 565 | `{"max_candles": 28, "n": 21, "stop_atr": 5.0, "take_profit_atr": 5.0, "z": 1.0}` | 5,549.62 | 2.1 | -5.0 | 63.3 | 1,395.62 | 1.2 | -7.7 | 0.57 | 93108/60693 | not checked |
| 514 | `{"max_candles": 28, "n": 84, "stop_atr": 4.75, "take_profit_atr": 3.5, "z": 1.0}` | 5,117.80 | 2.0 | -4.4 | 63.2 | 1,143.33 | 1.0 | -6.5 | 0.50 | 78905/50905 | not checked |
| 446 | `{"max_candles": 28, "n": 84, "stop_atr": 4.5, "take_profit_atr": 3.5, "z": 1.0}` | 4,889.41 | 1.9 | -4.2 | 63.2 | 1,119.74 | 1.0 | -6.5 | 0.51 | 78982/50954 | not checked |
| 516 | `{"max_candles": 48, "n": 105, "stop_atr": 4.75, "take_profit_atr": 4.0, "z": 1.0}` | 4,735.17 | 1.9 | -4.1 | 63.2 | 1,146.30 | 1.0 | -6.4 | 0.54 | 76990/49567 | not checked |
| 460 | `{"max_candles": 28, "n": 84, "stop_atr": 4.75, "take_profit_atr": 4.0, "z": 1.25}` | 3,850.05 | 1.6 | -3.2 | 62.9 | 837.32 | 0.7 | -5.5 | 0.47 | 57956/38061 | not checked |
| 461 | `{"max_candles": 28, "n": 84, "stop_atr": 4.5, "take_profit_atr": 3.5, "z": 1.25}` | 3,672.57 | 1.5 | -3.1 | 62.9 | 819.33 | 0.7 | -5.4 | 0.49 | 58001/38090 | not checked |
| 459 | `{"max_candles": 28, "n": 84, "stop_atr": 4.25, "take_profit_atr": 4.0, "z": 1.25}` | 3,491.96 | 1.4 | -3.0 | 62.9 | 790.73 | 0.7 | -5.3 | 0.49 | 58055/38113 | not checked |
| 585 | `{"max_candles": 28, "n": 84, "stop_atr": 4.75, "take_profit_atr": 3.5, "z": 1.5}` | 2,600.90 | 1.1 | -2.7 | 62.6 | 746.93 | 0.7 | -4.8 | 0.59 | 41107/27811 | not checked |
| 458 | `{"max_candles": 28, "n": 84, "stop_atr": 4.5, "take_profit_atr": 4.0, "z": 1.5}` | 2,509.36 | 1.1 | -2.5 | 62.6 | 742.54 | 0.7 | -4.7 | 0.62 | 41133/27826 | not checked |
| 509 | `{"max_candles": 28, "n": 84, "stop_atr": 4.5, "take_profit_atr": 3.0, "z": 1.5}` | 2,491.67 | 1.1 | -2.5 | 62.6 | 731.33 | 0.7 | -4.7 | 0.61 | 41136/27831 | not checked |
| 511 | `{"max_candles": 48, "n": 84, "stop_atr": 4.25, "take_profit_atr": 4.0, "z": 1.5}` | 2,403.54 | 1.0 | -2.5 | 62.6 | 714.52 | 0.6 | -4.7 | 0.62 | 41165/27845 | not checked |
| 160 | `{"max_candles": 48, "n": 84, "stop_atr": 4.0, "take_profit_atr": 3.5, "z": 1.5}` | 2,312.98 | 1.0 | -2.3 | 62.6 | 682.13 | 0.6 | -4.7 | 0.61 | 41195/27868 | 1.00 |
| 175 | `{"max_candles": 44, "n": 84, "stop_atr": 4.0, "take_profit_atr": 3.5, "z": 1.5}` | 2,312.98 | 1.0 | -2.3 | 62.6 | 682.13 | 0.6 | -4.7 | 0.61 | 41195/27868 | not checked |
| 176 | `{"max_candles": 52, "n": 84, "stop_atr": 4.0, "take_profit_atr": 3.5, "z": 1.5}` | 2,312.98 | 1.0 | -2.3 | 62.6 | 682.13 | 0.6 | -4.7 | 0.61 | 41195/27868 | not checked |
| 172 | `{"max_candles": 48, "n": 84, "stop_atr": 3.75, "take_profit_atr": 3.5, "z": 1.5}` | 2,162.91 | 0.9 | -2.3 | 62.6 | 662.30 | 0.6 | -4.7 | 0.63 | 41239/27889 | not checked |
| 503 | `{"max_candles": 28, "n": 84, "stop_atr": 4.75, "take_profit_atr": 4.0, "z": 1.75}` | 1,792.59 | 0.8 | -2.3 | 62.3 | 547.03 | 0.5 | -3.6 | 0.62 | 28689/20120 | not checked |
| 171 | `{"max_candles": 48, "n": 84, "stop_atr": 4.0, "take_profit_atr": 3.5, "z": 1.75}` | 1,599.42 | 0.7 | -2.0 | 62.2 | 475.40 | 0.4 | -3.7 | 0.61 | 28738/20146 | not checked |

(6 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 615 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
