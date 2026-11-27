# mfi_washout: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** MSFT (etf, 1d)
**Found at:** iteration 678 of optimization.log (2026-11-25T05:42:10Z); written at the checkpoint in iteration 1179; backtest.py version `9fc21f0042`
**Replaces:** mfi_washout__max-income__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 11,072.30)

## Parameters

| parameter | value |
|---|---|
| level | 34 |
| max_candles | 36 |
| n | 15 |
| stop_atr | 3.0 |
| take_profit_atr | 4.0 |

```json
{
  "level": 34,
  "max_candles": 36,
  "n": 15,
  "stop_atr": 3.0,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 20,288.64 | 7,206.53 |
| return % | 202.89 | 72.07 |
| return %/year | 5.4 | 5.1 |
| gross profit | 43,235.37 | 15,025.31 |
| gross loss | 22,946.74 | 7,818.78 |
| trades | 50 | 30 |
| win rate % | 72.0 | 70.0 |
| avg win | 1,200.98 | 715.49 |
| avg loss | -1,639.05 | -868.75 |
| avg result / trade | 405.77 | 240.22 |
| largest single loss | -3,449.36 | -1,904.41 |
| largest loss % of equity | -12.56 | -9.16 |
| max drawdown | -6,340.30 | -3,977.92 |
| max drawdown % | -19.80 | -19.09 |
| profit factor | 1.88 | 1.92 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 10.8 | 11.6 |
| time in market % | 13.9 | 16.7 |
| buy & hold return % | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.94 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# MFI Washout

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Buy a money-flow washout recovery (MFI crossing back above an oversold level) while the long-term trend is up; sell once money flow is strong again.

## Market
- Symbols: MSFT (base run, spec's instrument); screening over the 516 US stocks from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `MFI(n)` crosses above `level` (MFI[t] > level and MFI[t-1] <= level) AND `C > SMA(200)`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `MFI(n) > 65` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | MFI length | 14 | 7–28 | 1 |
| level | MFI cross level | 20 | 10–30 | 2 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 12 | 6–24 | 2 |

SMA(200) trend filter and the exit level 65 are fixed constants in the spec.

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
