# percent_b_money_flow__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d)
**Found at:** iteration 933 of optimization.log (2026-11-25T09:39:46Z); written at the checkpoint in iteration 1054; backtest.py version `0257c71e87`
**Replaces:** percent_b_money_flow__broad__balanced__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 370.33)

## Parameters

| parameter | value |
|---|---|
| b | 0.75 |
| max_candles | 90 |
| mfi | 90 |
| stop_atr | 4.25 |
| take_profit_atr | 5.0 |

```json
{
  "b": 0.75,
  "max_candles": 90,
  "mfi": 90,
  "stop_atr": 4.25,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 580.30 | 135.10 |
| return % | 5.80 | 1.35 |
| return %/year | 0.3 | 0.1 |
| gross profit | 2,692.66 | 2,314.65 |
| gross loss | 2,112.36 | 2,179.55 |
| trades | 933 | 786 |
| win rate % | 45.4 | 45.7 |
| avg win | 6.35 | 6.45 |
| avg loss | -4.15 | -5.10 |
| avg result / trade | 0.62 | 0.17 |
| largest single loss | -30.71 | -37.34 |
| largest loss % of equity | -10.99 | -18.82 |
| max drawdown | -356.18 | -532.28 |
| max drawdown % | -3.55 | -5.11 |
| profit factor | 1.27 | 1.06 |
| unusually bad trades | 105 | 90 |
| … threshold (% of equity) | 3.1 | 3.6 |
| time in market % | 4.8 | 7.8 |
| buy & hold return % | 116.56 | 305.41 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.44 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Percent B Money Flow

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Momentum confirmation: buy when price rides the upper Bollinger band (%B high) and money flow is strong at the same time; exit when either fades.

## Market
- Symbols: QQQ (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- (`PercentB(20,2) > b` AND `MFI(10) > mfi`) is true at t and was false at t-1
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `PercentB(20,2) < 0.5` OR `MFI(10) < 40` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| b | %B entry threshold | 0.8 | 0.7–1.0 | 0.05 |
| mfi | MFI entry threshold | 80 | 60–90 | 2 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

BB(20,2), MFI(10), exit levels 0.5 and 40 are fixed.

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
