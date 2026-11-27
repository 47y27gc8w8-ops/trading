# ppo_percentage_trend: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** XLK (etf, 1d)
**Found at:** iteration 80 of optimization.log (2026-11-25T09:40:47Z); written at the checkpoint in iteration 30467; backtest.py version `56ab330998`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,522.84)

## Parameters

| parameter | value |
|---|---|
| max_candles | 96 |
| stop_atr | 1.25 |
| take_profit_atr | 5.0 |
| threshold | 1.0 |

```json
{
  "max_candles": 96,
  "stop_atr": 1.25,
  "take_profit_atr": 5.0,
  "threshold": 1.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 7,857.37 | 6,868.67 |
| return % | 78.57 | 68.69 |
| return %/year | 3.9 | 4.9 |
| gross profit | 12,538.52 | 8,987.98 |
| gross loss | 4,681.15 | 2,119.31 |
| trades | 25 | 14 |
| win rate % | 48.0 | 57.1 |
| avg win | 1,044.88 | 1,123.50 |
| avg loss | -360.09 | -353.22 |
| avg result / trade | 314.29 | 490.62 |
| largest single loss | -493.01 | -552.49 |
| largest loss % of equity | -2.84 | -3.48 |
| max drawdown | -1,456.09 | -1,050.69 |
| max drawdown % | -9.42 | -6.48 |
| profit factor | 2.68 | 4.24 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 4.3 | 4.9 |
| time in market % | 15.3 | 13.2 |
| buy & hold return % | 38.82 | 767.30 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.25 |
| period | 2000-12-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# PPO Percentage Trend

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Slow trend following on the percentage price oscillator: buy when PPO(20,100) rises through a positive threshold, sell when it turns negative.

## Market
- Symbols: XLK (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `PPO(20,100)` crosses above `threshold`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `PPO(20,100) < 0` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| threshold | PPO entry level, % | 1.0 | 0.0–3.0 | 0.25 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 96 | 48–192 | 12 |

PPO periods 20/100 and the exit level 0 are fixed. XLI (spec's second instrument) is covered by screening.

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 500 bars of its own history (indicator warm-up, ≥ 5× the longest recursive period)
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
