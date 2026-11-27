# percent_b_money_flow: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 185 of optimization.log (2026-11-25T09:33:01Z); written at the checkpoint in iteration 285; backtest.py version `87997ef64b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 712.70)
**Range warning:** take_profit_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| b | 0.8 |
| max_candles | 30 |
| mfi | 88 |
| stop_atr | 2.5 |
| take_profit_atr | 1.5 |

```json
{
  "b": 0.8,
  "max_candles": 30,
  "mfi": 88,
  "stop_atr": 2.5,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,017.07 | 786.98 |
| return % | 20.17 | 7.87 |
| return %/year | 1.1 | 0.7 |
| gross profit | 6,239.04 | 3,320.40 |
| gross loss | 4,221.97 | 2,533.42 |
| trades | 39 | 26 |
| win rate % | 61.5 | 73.1 |
| avg win | 259.96 | 174.76 |
| avg loss | -281.46 | -361.92 |
| avg result / trade | 51.72 | 30.27 |
| largest single loss | -889.20 | -548.82 |
| largest loss % of equity | -7.24 | -4.92 |
| max drawdown | -1,925.96 | -972.58 |
| max drawdown % | -15.57 | -8.44 |
| profit factor | 1.48 | 1.31 |
| unusually bad trades | 6 | 0 |
| … threshold (% of equity) | 3.2 | 7.0 |
| time in market % | 6.7 | 4.9 |
| buy & hold return % | 117.30 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.62 |
| period | 1999-08-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

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
