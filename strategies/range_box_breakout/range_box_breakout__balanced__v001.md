# range_box_breakout: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 336 of optimization.log (2026-11-25T10:33:25Z); written at the checkpoint in iteration 471; backtest.py version `b039e0a41a`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 20,391.69)
**Range warning:** take_profit_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 42 |
| n | 20 |
| stop_atr | 2.0 |
| take_profit_atr | 1.5 |
| width | 6.75 |

```json
{
  "max_candles": 42,
  "n": 20,
  "stop_atr": 2.0,
  "take_profit_atr": 1.5,
  "width": 6.75
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 37,540.81 | 6,827.08 |
| return % | 375.41 | 68.27 |
| return %/year | 7.7 | 4.9 |
| gross profit | 102,542.84 | 27,583.58 |
| gross loss | 65,002.04 | 20,756.50 |
| trades | 181 | 112 |
| win rate % | 66.8 | 64.3 |
| avg win | 847.46 | 383.11 |
| avg loss | -1,083.37 | -518.91 |
| avg result / trade | 207.41 | 60.96 |
| largest single loss | -4,185.47 | -1,139.93 |
| largest loss % of equity | -8.32 | -7.40 |
| max drawdown | -5,599.74 | -2,599.62 |
| max drawdown % | -35.31 | -17.23 |
| profit factor | 1.58 | 1.33 |
| unusually bad trades | 3 | 2 |
| … threshold (% of equity) | 11.0 | 7.2 |
| time in market % | 16.3 | 21.6 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.64 |
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
