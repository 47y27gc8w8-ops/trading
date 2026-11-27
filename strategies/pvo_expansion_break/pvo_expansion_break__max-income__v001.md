# pvo_expansion_break: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** IWM (etf, 1d)
**Found at:** iteration 45 of optimization.log (2026-11-25T10:15:41Z); written at the checkpoint in iteration 43962; backtest.py version `4a6c2ff343`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 2,070.53)

## Parameters

| parameter | value |
|---|---|
| level | 2 |
| max_candles | 42 |
| stop_atr | 2.75 |
| take_profit_atr | 2.5 |

```json
{
  "level": 2,
  "max_candles": 42,
  "stop_atr": 2.75,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,929.02 | 496.46 |
| return % | 29.29 | 4.96 |
| return %/year | 1.7 | 0.5 |
| gross profit | 5,691.12 | 3,252.51 |
| gross loss | 2,762.10 | 2,756.05 |
| trades | 22 | 19 |
| win rate % | 54.5 | 47.4 |
| avg win | 474.26 | 361.39 |
| avg loss | -276.21 | -275.60 |
| avg result / trade | 133.14 | 26.13 |
| largest single loss | -443.75 | -442.80 |
| largest loss % of equity | -3.51 | -4.38 |
| max drawdown | -1,492.65 | -1,149.84 |
| max drawdown % | -11.45 | -9.89 |
| profit factor | 2.06 | 1.18 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 4.4 | 5.3 |
| time in market % | 6.8 | 7.2 |
| buy & hold return % | 177.00 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |
| period | 2000-12-29 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# PVO Expansion Break

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
A breakout to a new 20-bar high confirmed by a volume surge (PVO crossing up) tends to follow through.

## Market
- Symbols: IWM (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `PVO(12,26)` crosses above `level` AND `C > HH(H, 20)[1]`
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
| level | PVO cross level, % | 10 | 0–25 | 1 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

PVO(12,26), the 20-bar high and the EMA(20) exit are fixed.

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 150 bars of its own history (indicator warm-up, ≥ 5× the longest recursive period)
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
