# macd_signal_cross__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH (etf, 1d)
**Found at:** iteration 379 of optimization.log (2026-11-26T06:42:20Z); written at the checkpoint in iteration 458; backtest.py version `33b128069d`
**Replaces:** macd_signal_cross__broad__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,466.94)

## Parameters

| parameter | value |
|---|---|
| max_candles | 64 |
| signal | 18 |
| stop_atr | 3.75 |
| take_profit_atr | 2.0 |

```json
{
  "max_candles": 64,
  "signal": 18,
  "stop_atr": 3.75,
  "take_profit_atr": 2.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,420.08 | 1,292.31 |
| return % | 24.20 | 12.92 |
| return %/year | 1.0 | 1.1 |
| gross profit | 23,643.62 | 12,390.69 |
| gross loss | 21,223.54 | 11,098.38 |
| trades | 46,070 | 26,364 |
| win rate % | 46.7 | 47.6 |
| avg win | 1.10 | 0.99 |
| avg loss | -0.86 | -0.80 |
| avg result / trade | 0.05 | 0.05 |
| largest single loss | -19.78 | -20.29 |
| largest loss % of equity | -20.02 | -15.99 |
| max drawdown | -857.32 | -492.82 |
| max drawdown % | -7.41 | -4.33 |
| profit factor | 1.11 | 1.12 |
| unusually bad trades | 4,448 | 2,458 |
| … threshold (% of equity) | 5.5 | 5.5 |
| time in market % | 12.6 | 14.0 |
| buy & hold return % | 1,777.75 | 470.42 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.08 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# MACD Signal Cross

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Buy MACD(12,26) crossing above its signal line while price is above the 200-day SMA; exit on the cross back below.

## Market
- Symbols: AAPL (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's stock list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `MACD(12,26)` crosses above `EMA(MACD, signal)` AND `C > SMA(200)`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `MACD(12,26)` crosses below `EMA(MACD, signal)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| signal | MACD signal EMA | 9 | 5–15 | 1 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 96 | 48–192 | 8 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 250 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo stocks (spec: stock); listed instruments are alternatives, tested separately.
- Base symbol AAPL (spec lists AAPL, MSFT; MSFT is covered by the stock screen).
- MACD 12/26 and SMA(200) are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
