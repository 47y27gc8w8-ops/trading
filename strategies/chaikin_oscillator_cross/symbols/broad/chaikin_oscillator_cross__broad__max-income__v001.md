# chaikin_oscillator_cross__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** NESN.SW, NOVN.SW, RO.SW, UBSG.SW, ZURN.SW, ABBN.SW, CFR.SW, SIKA.SW, LONN.SW, GIVN.SW, HOLN.SW, SREN.SW, PGHN.SW, SCMN.SW, GEBN.SW, SLHN.SW, LOGN.SW, KNIN.SW, SOON.SW, SGSN.SW, ASML, TSM, SAP, NVO, MSTR, MELI, MMM, AOS, ABT, ABBV, ACN, ADBE, AMD, AES, AFL, A, APD, AKAM, ALB, ARE, ALGN, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AEE, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, AON, APA, APO, AAPL, AMAT, APTV, ACGL, ADM, AJG, AIZ, T, ATO, ADSK, ADP, AZO, AVY, AXON, BKR, BALL, BAC, BAX, BDX, BRK-B, BBY, TECH, BIIB, BLK, BX, BNY, BA, BKNG, BSX, BMY, AVGO, BR, BRO, BF-B, BG, BXP, CHRW, CDNS, CPT, COF, CAH, CCL, CASY, CAT, CBOE, CBRE, CDW, COR, CNC, CNP, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CIEN, CI, CINF, CTAS, CSCO, C, CLX, CME, CMS, KO, CTSH, COHR, CL, CMCSA, FIX, COP, ED, STZ, COO, CPRT, GLW, CPAY, CSGP, COST, CRH, CCI, CSX, CMI, CVS, DHR, DRI, DVA, DECK, DE, DAL, DVN, DXCM, FANG, DLR, DG, DLTR, D, DPZ, DOV, DHI, DTE, DUK, DD, ETN, EBAY, ECHO, ECL, EIX, EW, ELV, EME, EMR, ETR, EOG, EQT, EFX, EQIX, ERIE, ESS, EL, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FERG, FIS, FITB, FSLR, FE, FISV, FLEX, F, FTNT, BEN, FCX, GRMN, IT, GE, GEN, GNRC, GD, GIS, GM, GPC, GILD, GPN, GL, GS, HAL, HIG, HAS, HCA, DOC, HSIC, HSY, HD, HON, HRL, HST, HPQ, HUBB, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, PODD, INTC, IBKR, ICE, IFF, IP, INTU, ISRG, IVZ, IQV, IRM, JBHT, JBL, JKHY, J, JNJ, JCI, JPM, KDP, KEY, KMB, KIM, KMI, KKR, KLAC, KR, LHX, LH, LRCX, LVS, LDOS, LEN, LII, LLY, LIN, LYV, LMT, L, LOW, LULU, LYB, MTB, MPC, MAR, MRSH, MLM, MRVL, MAS, MA, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, PCAR, PKG, PANW, PH, PAYX, PNR, PEP, PFE, PCG, PM, PSX, PNW, PNC, PPG, PPL, PFG, PG, PGR, PLD, PRU, PTC, PEG, PSA, PHM, QCOM, PWR, DGX, RL, RJF, O, REG, REGN, RF, RSG, RMD, RVTY, ROK, ROL, ROP, ROST, RCL, RTX, SPGI, CRM, SBAC, SLB, STX, SRE, NOW, SHW, SPG, SKYD, SWKS, SJM, SW, SNA, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SMCI, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TER, TSLA, TXN, TPL, TXT, TMO, TJX, TKO, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VTRS, V, VMRK, VMC, WRB, GWW, WAB, WMT, DIS, WM, WAT, WEC, WFC, WELL, WST, WDC, WY, WSM, WMB, WTW, WDAY, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZTS (etf, 1d)
**Found at:** iteration 175 of optimization.log (2026-11-25T16:48:26Z); written at the checkpoint in iteration 263; backtest.py version `71317483c0`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 7,850.25)
**Range warning:** stop_atr is at the max of its range, take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_bars | 48 |
| n | 16 |
| stop_atr | 4.0 |
| take_profit_atr | 6.0 |

```json
{
  "max_bars": 48,
  "n": 16,
  "stop_atr": 4.0,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 8,972.62 | 3,229.32 |
| return % | 89.73 | 32.29 |
| return %/year | 3.1 | 2.6 |
| gross profit | 80,736.94 | 35,356.35 |
| gross loss | 71,764.31 | 32,127.03 |
| trades | 101,787 | 66,447 |
| win rate % | 38.1 | 38.5 |
| avg win | 2.08 | 1.38 |
| avg loss | -1.14 | -0.79 |
| avg result / trade | 0.09 | 0.05 |
| largest single loss | -88.88 | -33.04 |
| largest loss % of equity | -14.04 | -24.02 |
| max drawdown | -5,838.36 | -2,077.17 |
| max drawdown % | -32.66 | -15.63 |
| profit factor | 1.12 | 1.10 |
| unusually bad trades | 13,850 | 8,789 |
| … threshold (% of equity) | 4.9 | 4.4 |
| time in market % | 38.3 | 44.5 |
| buy & hold return % | 1,824.49 | 466.47 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.84 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Chaikin Oscillator Cross

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: MSFT (base run); screening universe: `stock` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `ChaikinOsc(3, 10)` crosses above 0 AND `ADL > SMA(ADL, n)`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `ChaikinOsc(3, 10) < 0` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| n | ADL trend SMA length | 20 | 10–50 | 2 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 48 | 24–96 | 6 |

Constraints: none beyond positive exits. All other numbers in the triggers are fixed constants of the spec.

## Setup
- In-sample (tuning): 1995-01-01 (or the symbol's first bar after 120 warm-up bars) → 2016-01-01
- Out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Sizing: 100% of equity per trade (user's choice for the library, 2026-11-24, so results compare across the leaderboard); the spec's risk_fraction is not used or tuned.
- Costs: fee 0.05%/side + slippage 0.03%/fill, the US ETF/stock convention of the user-approved absolute_momentum_monthly setup (above the spec's 1 bp + 2 bp + 2 bp). Exits at the target are charged slippage too (slightly conservative vs a limit order).
- Bars: Yahoo daily, dividend/split adjusted OHLC (the project has no separate raw execution series), used for signals and fills.
- ATR(14) is Wilder's RMA of true range with an SMA seed; stop and target are frozen at entry from the signal bar's ATR, never move, and are checked intrabar (stop first when both touch). A gap through the stop fills at the open; a target fills at the target price.
- max_candles is the template's max_bars (entry bar counts as 1; exit at the next open after bar N).
- Entry veto: no entry when the strategy's own close-based exit is true on the signal bar. After an intrabar stop/target exit, the next entry needs a signal from the following bar on (one fully flat bar).
- Base symbol = the first listed candidate; the others (and the rest of the universe) are covered by screening, since the spec calls the listed instruments alternatives, not a basket.
- Period: in-sample 1995-01-01 (or the symbol's first warmed-up bar) to 2016-01-01, out-of-sample to 2026-11-23 (frozen): repo precedent for ETF strategies.

## Open questions
- none (library conventions agreed across the library sessions and the user's absolute_momentum_monthly choices)

---
Backtest results don't guarantee future performance.
