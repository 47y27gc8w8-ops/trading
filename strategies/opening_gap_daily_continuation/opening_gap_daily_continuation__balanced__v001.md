# opening_gap_daily_continuation: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** NVDA (etf, 1d)
**Found at:** iteration 134 of optimization.log (2026-11-25T08:22:23Z); written at the checkpoint in iteration 31768; backtest.py version `2da54abf60`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 30,312.42)

## Parameters

| parameter | value |
|---|---|
| gap | 2.25 |
| max_candles | 36 |
| stop_atr | 3.0 |
| take_profit_atr | 5.5 |

```json
{
  "gap": 2.25,
  "max_candles": 36,
  "stop_atr": 3.0,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 38,804.72 | 10,236.06 |
| return % | 388.05 | 102.36 |
| return %/year | 10.1 | 6.7 |
| gross profit | 60,606.17 | 13,687.15 |
| gross loss | 21,801.44 | 3,451.09 |
| trades | 23 | 16 |
| win rate % | 52.2 | 50.0 |
| avg win | 5,050.51 | 1,710.89 |
| avg loss | -1,981.95 | -431.39 |
| avg result / trade | 1,687.16 | 639.75 |
| largest single loss | -5,950.50 | -826.32 |
| largest loss % of equity | -21.28 | -3.92 |
| max drawdown | -12,477.47 | -2,102.13 |
| max drawdown % | -38.35 | -13.16 |
| profit factor | 2.78 | 3.97 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 7.0 | 5.1 |
| time in market % | 6.1 | 5.8 |
| buy & hold return % | 2,340.06 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.67 |
| period | 1999-06-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Opening Gap Daily Continuation

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
A day that gaps above the prior high and holds (closes above its open) on heavy volume tends to continue; buy next session, exit below EMA(10).

## Market
- Symbols: NVDA (base run, spec's instrument); screening over the 516 US stocks from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `O > H[1] * (1 + gap/100)` AND `C > O` AND `V > 1.5 * SMA(V, 20)[1]`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `C < EMA(10)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| gap | gap above prior high, % | 1.0 | 0.5–3.0 | 0.25 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

Volume multiple 1.5 and EMA(10) exit are fixed. Entry is the next session's open (completed-gap-day signal).

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
