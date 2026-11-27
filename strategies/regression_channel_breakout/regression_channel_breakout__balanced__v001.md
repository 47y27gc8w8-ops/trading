# regression_channel_breakout: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 447 of optimization.log (2026-11-25T11:40:40Z); written at the checkpoint in iteration 466; backtest.py version `0e3504779a`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 2,996.87)
**Range warning:** take_profit_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 1.8 |
| max_candles | 42 |
| n | 70 |
| stop_atr | 3.75 |
| take_profit_atr | 1.5 |

```json
{
  "k": 1.8,
  "max_candles": 42,
  "n": 70,
  "stop_atr": 3.75,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 5,686.23 | 1,366.84 |
| return % | 56.86 | 13.67 |
| return %/year | 2.8 | 1.2 |
| gross profit | 8,033.51 | 4,567.05 |
| gross loss | 2,347.28 | 3,200.22 |
| trades | 35 | 36 |
| win rate % | 80.0 | 75.0 |
| avg win | 286.91 | 169.15 |
| avg loss | -335.33 | -355.58 |
| avg result / trade | 162.46 | 37.97 |
| largest single loss | -557.21 | -655.91 |
| largest loss % of equity | -4.49 | -6.01 |
| max drawdown | -678.00 | -1,262.98 |
| max drawdown % | -6.33 | -11.58 |
| profit factor | 3.42 | 1.43 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 4.1 | 7.1 |
| time in market % | 7.1 | 8.4 |
| buy & hold return % | 98.28 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.42 |
| period | 1999-09-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Regression Channel Breakout

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Buy when price breaks above the upper edge of a rising log-price regression channel fitted on the preceding n bars.

## Market
- Symbols: QQQ (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- OLS of log(C) on time over bars t-n..t-1 (excl. t): `log(C[t]) > fit extrapolated to t + k * residual std` AND slope > 0
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
| n | regression window | 60 | 30–120 | 5 |
| k | channel width in residual stds | 2.0 | 1.0–3.0 | 0.1 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

EMA(20) exit is fixed.

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 130 bars of its own history (indicator warm-up, ≥ 5× the longest recursive period)
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
