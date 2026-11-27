# relative_volume_price_thrust__broad: optimization summary

Updated 2026-11-25T12:14:24Z · backtest.py version `99a560110d` · 467 parameter sets tested with this version (467 rows in results.csv in total) · last run ended: time budget used

## Setup

- Data: NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, CDW, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [relative_volume_price_thrust__broad__max-income__v001.md](relative_volume_price_thrust__broad__max-income__v001.md) | 279 | `{"max_candles": 90, "rvol": 1.75, "stop_atr": 3.75, "take_profit_atr": 5.5}` | long DUK since 2026-11-05 00:00 @ 130.905644; long STE since 2026-11-05 00:00 @ 251.76071 |
| balanced | [relative_volume_price_thrust__broad__balanced__v002.md](relative_volume_price_thrust__broad__balanced__v002.md) | 467 | `{"max_candles": 36, "rvol": 3.75, "stop_atr": 2.5, "take_profit_atr": 3.0}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 471.92 | 215.50 | 270.64 | 58.21 |
| return % | 4.72 | 2.15 | 2.71 | 0.58 |
| return %/year | 0.3 | 0.2 | 0.2 | 0.1 |
| gross profit | 6,422.90 | 3,107.27 | 1,116.54 | 332.60 |
| gross loss | 5,950.98 | 2,891.77 | 845.90 | 274.39 |
| trades | 12,015 | 6,675 | 1,605 | 638 |
| win rate % | 39.5 | 38.9 | 46.2 | 46.7 |
| avg win | 1.35 | 1.20 | 1.50 | 1.12 |
| avg loss | -0.82 | -0.71 | -0.98 | -0.81 |
| avg result / trade | 0.04 | 0.03 | 0.17 | 0.09 |
| largest single loss | -19.43 | -10.82 | -6.36 | -6.79 |
| largest loss % of equity | -13.78 | -20.89 | -30.21 | -33.78 |
| max drawdown | -341.42 | -201.26 | -26.61 | -22.77 |
| max drawdown % | -3.25 | -1.97 | -0.26 | -0.23 |
| profit factor | 1.08 | 1.07 | 1.32 | 1.21 |
| unusually bad trades | 1,280 | 651 | 135 | 42 |
| … threshold (% of equity) | 5.6 | 5.4 | 7.6 | 6.8 |
| time in market % | 5.8 | 5.0 | 0.7 | 0.5 |
| buy & hold return % | 726.23 | 466.47 | 726.23 | 466.47 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.69 |  | 0.29 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | 1.4 | 0.5 |
| 2001 | -0.6 | 0.3 |
| 2002 | -0.9 | -0.0 |
| 2003 | 2.1 | 0.6 |
| 2004 | 2.2 | 0.3 |
| 2005 | 0.2 | 0.2 |
| 2006 | 0.2 | 0.2 |
| 2007 | -0.0 | -0.0 |
| 2008 | -1.8 | -0.0 |
| 2009 | 0.4 | 0.2 |
| 2010 | 0.3 | -0.1 |
| 2011 | -0.5 | 0.0 |
| 2012 | 0.7 | 0.3 |
| 2013 | 2.4 | 0.2 |
| 2014 | -0.2 | 0.1 |
| 2015 | -1.0 | 0.0 |
| 2016 (OOS) | 0.8 | 0.0 |
| 2017 (OOS) | 0.6 | 0.1 |
| 2018 (OOS) | -0.7 | -0.1 |
| 2019 (OOS) | 0.4 | 0.1 |
| 2020 (OOS) | -0.8 | 0.0 |
| 2021 (OOS) | 0.8 | 0.0 |
| 2022 (OOS) | -0.6 | -0.0 |
| 2023 (OOS) | 1.3 | 0.1 |
| 2024 (OOS) | 0.6 | 0.2 |
| 2025 (OOS) | 0.4 | 0.1 |
| 2026 (OOS) | 0.0 | -0.1 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 3.2% from a peak in-sample and 2.0% out-of-sample, and the worst single trade cost 20.9% of the account out-of-sample. About 40 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 0.3% from a peak in-sample and 0.2% out-of-sample, and the worst single trade cost 33.8% of the account out-of-sample. About 46 of every 100 trades won in-sample. Out-of-sample it earned 0.1% a year against 0.2% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 187 | `{"max_candles": 90, "rvol": 1.75, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 484.78 | 0.3 | -3.3 | 39.5 | 216.27 | 0.2 | -2.0 | 0.67 | 12015/6675 | not checked |
| 385 | `{"max_candles": 72, "rvol": 1.75, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 484.78 | 0.3 | -3.3 | 39.5 | 216.27 | 0.2 | -2.0 | 0.67 | 12015/6675 | not checked |
| 398 | `{"max_candles": 78, "rvol": 1.75, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 484.78 | 0.3 | -3.3 | 39.5 | 216.27 | 0.2 | -2.0 | 0.67 | 12015/6675 | not checked |
| 403 | `{"max_candles": 96, "rvol": 1.75, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 484.78 | 0.3 | -3.3 | 39.5 | 216.27 | 0.2 | -2.0 | 0.67 | 12015/6675 | not checked |
| 404 | `{"max_candles": 84, "rvol": 1.75, "stop_atr": 4.0, "take_profit_atr": 5.5}` | 484.78 | 0.3 | -3.3 | 39.5 | 216.27 | 0.2 | -2.0 | 0.67 | 12015/6675 | not checked |
| 190 | `{"max_candles": 84, "rvol": 1.75, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 471.92 | 0.3 | -3.2 | 39.5 | 215.50 | 0.2 | -2.0 | 0.69 | 12015/6675 | not checked |
| 191 | `{"max_candles": 96, "rvol": 1.75, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 471.92 | 0.3 | -3.2 | 39.5 | 215.50 | 0.2 | -2.0 | 0.69 | 12015/6675 | not checked |
| 192 | `{"max_candles": 90, "rvol": 1.75, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 471.92 | 0.3 | -3.2 | 39.5 | 215.50 | 0.2 | -2.0 | 0.69 | 12015/6675 | 1.00 |
| 295 | `{"max_candles": 78, "rvol": 1.75, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 471.92 | 0.3 | -3.2 | 39.5 | 215.50 | 0.2 | -2.0 | 0.69 | 12015/6675 | not checked |
| 377 | `{"max_candles": 72, "rvol": 1.75, "stop_atr": 3.75, "take_profit_atr": 5.5}` | 471.92 | 0.3 | -3.2 | 39.5 | 215.50 | 0.2 | -2.0 | 0.69 | 12015/6675 | not checked |
| 186 | `{"max_candles": 90, "rvol": 1.75, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 471.19 | 0.3 | -3.2 | 39.5 | 226.95 | 0.2 | -1.9 | 0.72 | 12015/6675 | not checked |
| 375 | `{"max_candles": 96, "rvol": 1.75, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 471.19 | 0.3 | -3.2 | 39.5 | 226.95 | 0.2 | -1.9 | 0.72 | 12015/6675 | not checked |
| 299 | `{"max_candles": 48, "rvol": 1.75, "stop_atr": 4.0, "take_profit_atr": 4.5}` | 446.36 | 0.3 | -3.1 | 39.6 | 162.15 | 0.1 | -1.9 | 0.56 | 12079/6697 | not checked |
| 305 | `{"max_candles": 84, "rvol": 2.5, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 437.17 | 0.3 | -1.2 | 40.5 | 230.13 | 0.2 | -0.5 | 0.78 | 4791/2243 | not checked |
| 259 | `{"max_candles": 78, "rvol": 2.5, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 411.98 | 0.2 | -1.1 | 41.3 | 199.14 | 0.2 | -0.4 | 0.72 | 4817/2253 | not checked |
| 224 | `{"max_candles": 60, "rvol": 2.5, "stop_atr": 4.0, "take_profit_atr": 3.0}` | 375.91 | 0.2 | -1.0 | 41.9 | 150.76 | 0.1 | -0.5 | 0.61 | 4834/2257 | not checked |
| 35 | `{"max_candles": 72, "rvol": 3.25, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 356.24 | 0.2 | -0.7 | 42.2 | 136.78 | 0.1 | -0.2 | 0.55 | 2361/982 | not checked |
| 48 | `{"max_candles": 72, "rvol": 3.75, "stop_atr": 3.25, "take_profit_atr": 5.5}` | 353.47 | 0.2 | -0.6 | 45.1 | 89.44 | 0.1 | -0.2 | 0.36 | 1598/638 | not checked |
| 36 | `{"max_candles": 72, "rvol": 3.75, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 352.78 | 0.2 | -0.5 | 45.1 | 90.72 | 0.1 | -0.2 | 0.36 | 1598/638 | 1.00 |
| 51 | `{"max_candles": 66, "rvol": 3.75, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 352.78 | 0.2 | -0.5 | 45.1 | 90.72 | 0.1 | -0.2 | 0.36 | 1598/638 | not checked |
| 52 | `{"max_candles": 78, "rvol": 3.75, "stop_atr": 3.5, "take_profit_atr": 5.5}` | 352.78 | 0.2 | -0.5 | 45.1 | 90.72 | 0.1 | -0.2 | 0.36 | 1598/638 | not checked |
| 16 | `{"max_candles": 72, "rvol": 3.75, "stop_atr": 3.5, "take_profit_atr": 4.5}` | 311.69 | 0.2 | -0.5 | 45.2 | 92.60 | 0.1 | -0.2 | 0.42 | 1598/638 | not checked |
| 162 | `{"max_candles": 36, "rvol": 3.75, "stop_atr": 4.0, "take_profit_atr": 3.5}` | 294.03 | 0.2 | -0.4 | 45.9 | 87.71 | 0.1 | -0.2 | 0.44 | 1602/638 | not checked |
| 352 | `{"max_candles": 36, "rvol": 3.75, "stop_atr": 3.0, "take_profit_atr": 3.0}` | 289.04 | 0.2 | -0.3 | 46.6 | 68.08 | 0.1 | -0.2 | 0.33 | 1605/638 | not checked |
| 315 | `{"max_candles": 36, "rvol": 3.75, "stop_atr": 2.75, "take_profit_atr": 3.0}` | 277.62 | 0.2 | -0.3 | 46.4 | 71.07 | 0.1 | -0.2 | 0.41 | 1605/638 | not checked |

(4 more on the front, see results.csv)

## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 467 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
