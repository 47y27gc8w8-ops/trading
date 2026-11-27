# negative_volume_index_trend__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, VNQ, VUG, VTV (etf, 1d)
**Found at:** iteration 52 of optimization.log (2026-11-25T05:54:19Z); written at the checkpoint in iteration 227; backtest.py version `c28f56dfaf`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 296.83)

## Parameters

| parameter | value |
|---|---|
| max_candles | 66 |
| n | 110 |
| stop_atr | 3.75 |
| take_profit_atr | 4.5 |

```json
{
  "max_candles": 66,
  "n": 110,
  "stop_atr": 3.75,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 470.68 | 268.76 |
| return % | 4.71 | 2.69 |
| return %/year | 0.3 | 0.2 |
| gross profit | 1,719.71 | 2,005.02 |
| gross loss | 1,249.03 | 1,736.26 |
| trades | 424 | 563 |
| win rate % | 41.8 | 42.5 |
| avg win | 9.72 | 8.39 |
| avg loss | -5.06 | -5.36 |
| avg result / trade | 1.11 | 0.48 |
| largest single loss | -25.20 | -47.82 |
| largest loss % of equity | -9.83 | -16.12 |
| max drawdown | -190.11 | -275.02 |
| max drawdown % | -1.79 | -2.66 |
| profit factor | 1.38 | 1.16 |
| unusually bad trades | 70 | 101 |
| … threshold (% of equity) | 2.3 | 2.2 |
| time in market % | 3.7 | 7.3 |
| buy & hold return % | 64.23 | 277.57 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.89 |
| period | 1999-01-07 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Negative Volume Index Trend

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Follow the 'smart money' Negative Volume Index: hold while NVI is above its long EMA and price is above SMA(200).

## Market
- Symbols: SPY (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `NVI` crosses above `EMA(NVI, n)` AND `C > SMA(200)`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `NVI < EMA(NVI, n)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | NVI EMA length | 255 | 100–300 | 10 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

SMA(200) is fixed. NVI starts at 1000 on the symbol's first bar and only moves on bars with lower volume than the bar before.

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 1500 bars of its own history (indicator warm-up, ≥ 5× the longest recursive period)
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
