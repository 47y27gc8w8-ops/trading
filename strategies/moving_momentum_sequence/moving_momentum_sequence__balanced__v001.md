# moving_momentum_sequence: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 61 of optimization.log (2026-11-25T23:42:29Z); written at the checkpoint in iteration 18616; backtest.py version `0abd94298e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -919.76)

## Parameters

| parameter | value |
|---|---|
| max_candles | 108 |
| oversold | 16 |
| stop_atr | 2.0 |
| take_profit_atr | 4.5 |

```json
{
  "max_candles": 108,
  "oversold": 16,
  "stop_atr": 2.0,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 668.26 | 1,177.09 |
| return % | 6.68 | 11.77 |
| return %/year | 0.3 | 1.0 |
| gross profit | 1,478.48 | 1,212.95 |
| gross loss | 810.22 | 35.86 |
| trades | 23 | 7 |
| win rate % | 60.9 | 85.7 |
| avg win | 105.61 | 202.16 |
| avg loss | -90.02 | -35.86 |
| avg result / trade | 29.05 | 168.16 |
| largest single loss | -308.22 | -35.86 |
| largest loss % of equity | -2.81 | -0.32 |
| max drawdown | -386.05 | -151.02 |
| max drawdown % | -3.77 | -1.42 |
| profit factor | 1.82 | 33.82 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 1.4 | 0.5 |
| buy & hold return % | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 3.32 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Moving Momentum Sequence

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
In an uptrend (SMA20 > SMA150), buy when MACD momentum turns up shortly after a stochastic oversold dip; sell when the trend flips or the stochastic is overbought.

## Market
- Symbols: SPY (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `SMA(20) > SMA(150)` AND `min(SlowK(14,3)` over bars t-5..t-1`) < oversold` AND `MACDhist(12,26,9)` crosses above 0
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `SMA(20) < SMA(150)` OR `SlowK(14,3) > 80` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| oversold | stochastic oversold level | 20 | 10–30 | 2 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 96 | 48–192 | 12 |

SMA 20/150, SlowK(14,3), MACD(12,26,9) and the overbought exit 80 are fixed constants.

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 250 bars of its own history (indicator warm-up, ≥ 5× the longest recursive period)
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
