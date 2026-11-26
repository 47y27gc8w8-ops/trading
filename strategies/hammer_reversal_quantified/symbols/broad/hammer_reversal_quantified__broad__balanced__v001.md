# hammer_reversal_quantified__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d)
**Found at:** iteration 88 of optimization.log (2026-11-26T02:20:16Z); written at the checkpoint in iteration 236; backtest.py version `afbd7797ed`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 163.29)
**Range warning:** take_profit_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 76 |
| ratio | 3.25 |
| stop_atr | 2.0 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 76,
  "ratio": 3.25,
  "stop_atr": 2.0,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 217.54 | 35.88 |
| return % | 2.18 | 0.36 |
| return %/year | 0.1 | 0.0 |
| gross profit | 572.46 | 513.38 |
| gross loss | 354.92 | 477.50 |
| trades | 339 | 353 |
| win rate % | 68.1 | 67.1 |
| avg win | 2.48 | 2.17 |
| avg loss | -3.29 | -4.12 |
| avg result / trade | 0.64 | 0.10 |
| largest single loss | -11.14 | -43.13 |
| largest loss % of equity | -5.76 | -28.04 |
| max drawdown | -46.89 | -107.52 |
| max drawdown % | -0.46 | -1.07 |
| profit factor | 1.61 | 1.07 |
| unusually bad trades | 8 | 12 |
| … threshold (% of equity) | 4.5 | 4.3 |
| time in market % | 0.3 | 0.7 |
| buy & hold return % | 119.84 | 280.02 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.30 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Hammer Reversal Quantified

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
A quantified hammer candle (long lower wick, small upper wick, close in the upper part of the range) that makes a new 10-bar low inside a long-term uptrend: buy the rejection of lower prices, exit at the 10-day mean.

## Market
- Symbols: GLD (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): lower wick ≥ ratio × body AND upper wick ≤ body AND body/(H−L) ≥ 0.1 AND CLV01 > 0.65 AND `L < LL(L,10)[1]` AND `C > SMA(200)`; body = |C−O|, lower wick = min(O,C) − L, upper wick = H − max(O,C), CLV01 = (C−L)/(H−L); bars with H = L skipped.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C >= SMA(10)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| ratio | min lower-wick / body | 2 | 1.5–4 | 0.25 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

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
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- 0.1, 0.65, LL(10), SMA(200) and the exit SMA(10) are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
