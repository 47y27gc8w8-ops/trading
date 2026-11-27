# regression_channel_breakout: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 604 of optimization.log (2026-11-25T11:40:42Z); written at the checkpoint in iteration 982; backtest.py version `0e3504779a`
**Replaces:** regression_channel_breakout__safe-starter__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 7,348.21)

## Parameters

| parameter | value |
|---|---|
| k | 1.5 |
| max_candles | 36 |
| n | 75 |
| stop_atr | 3.5 |
| take_profit_atr | 2.0 |

```json
{
  "k": 1.5,
  "max_candles": 36,
  "n": 75,
  "stop_atr": 3.5,
  "take_profit_atr": 2.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 12,302.60 | 2,987.85 |
| return % | 123.03 | 29.88 |
| return %/year | 5.0 | 2.4 |
| gross profit | 17,654.57 | 8,635.83 |
| gross loss | 5,351.97 | 5,647.97 |
| trades | 47 | 47 |
| win rate % | 70.2 | 70.2 |
| avg win | 534.99 | 261.69 |
| avg loss | -382.28 | -403.43 |
| avg result / trade | 261.76 | 63.57 |
| largest single loss | -619.20 | -819.23 |
| largest loss % of equity | -2.58 | -6.40 |
| max drawdown | -1,709.41 | -1,892.32 |
| max drawdown % | -7.12 | -13.06 |
| profit factor | 3.30 | 1.53 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 4.1 | 6.1 |
| time in market % | 10.5 | 13.2 |
| buy & hold return % | 98.28 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.48 |
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
