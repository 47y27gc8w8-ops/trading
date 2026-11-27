# range_box_breakout__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, CDW, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d)
**Found at:** iteration 328 of optimization.log (2026-11-25T11:11:52Z); written at the checkpoint in iteration 492; backtest.py version `4af220afd6`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 669.55)

## Parameters

| parameter | value |
|---|---|
| max_candles | 72 |
| n | 28 |
| stop_atr | 2.75 |
| take_profit_atr | 2.0 |
| width | 4.5 |

```json
{
  "max_candles": 72,
  "n": 28,
  "stop_atr": 2.75,
  "take_profit_atr": 2.0,
  "width": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,045.28 | 448.97 |
| return % | 10.45 | 4.49 |
| return %/year | 0.5 | 0.4 |
| gross profit | 11,654.07 | 6,090.34 |
| gross loss | 10,608.79 | 5,641.38 |
| trades | 21,961 | 12,761 |
| win rate % | 48.0 | 48.6 |
| avg win | 1.11 | 0.98 |
| avg loss | -0.93 | -0.86 |
| avg result / trade | 0.05 | 0.04 |
| largest single loss | -12.68 | -7.25 |
| largest loss % of equity | -17.67 | -21.22 |
| max drawdown | -681.14 | -193.56 |
| max drawdown % | -6.27 | -1.84 |
| profit factor | 1.10 | 1.08 |
| unusually bad trades | 1,701 | 735 |
| … threshold (% of equity) | 6.6 | 6.6 |
| time in market % | 6.9 | 7.7 |
| buy & hold return % | 1,897.80 | 476.79 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.85 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Range Box Breakout

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Buy the upside break of a tight n-bar box (box height small relative to ATR); exit below EMA(20).

## Market
- Symbols: AAPL (base run, spec's instrument); screening over the 516 US stocks from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `(HH(H,n)[1] - LL(L,n)[1]) / ATR(14)[1] < width` AND `C > HH(H,n)[1]`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `C < EMA(20)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | box length | 10 | 5–30 | 1 |
| width | max box height in ATRs | 4.0 | 2.0–8.0 | 0.25 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

ATR(14) (Wilder) and the EMA(20) exit are fixed.

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 100 bars of its own history (indicator warm-up, ≥ 5× the longest recursive period)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- ETF/US-stock costs 0.05% fee per side + 0.03% slippage per fill (library convention, user-approved in absolute_momentum_monthly; above the spec's 5 bp)

## Assumptions
- 100% of equity per trade instead of the spec's risk_fraction sizing: user's choice for the library (leaderboard comparability); summary.md shows the size that keeps drawdowns near 10%.
- Fills on adjusted prices (the project has no separate raw execution series).
- Costs: see Setup.
- A target fills at its level even on a favorable gap (spec: conservative), stops at the open on a gap.
- Library conventions agreed across the parallel library sessions: IS to 2016-01-01, ETF costs, ATR exits frozen at the signal bar, entry veto, max_candles as the time exit.

## Open questions
- none (library-wide questions answered by the user in the absolute_momentum_monthly setup)

---
Backtest results don't guarantee future performance.
