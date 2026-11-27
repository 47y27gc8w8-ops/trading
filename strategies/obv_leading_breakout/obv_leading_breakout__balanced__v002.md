# obv_leading_breakout: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 324 of optimization.log (2026-11-25T07:17:30Z); written at the checkpoint in iteration 1078; backtest.py version `685cc94aa3`
**Replaces:** obv_leading_breakout__balanced__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 8,269.66)

## Parameters

| parameter | value |
|---|---|
| max_candles | 36 |
| n | 58 |
| stop_atr | 1.25 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 36,
  "n": 58,
  "stop_atr": 1.25,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 13,320.44 | 2,488.17 |
| return % | 133.20 | 24.88 |
| return %/year | 4.1 | 2.1 |
| gross profit | 46,889.43 | 10,819.22 |
| gross loss | 33,568.99 | 8,331.05 |
| trades | 134 | 74 |
| win rate % | 53.7 | 51.4 |
| avg win | 651.24 | 284.72 |
| avg loss | -541.44 | -231.42 |
| avg result / trade | 99.41 | 33.62 |
| largest single loss | -1,045.27 | -514.42 |
| largest loss % of equity | -8.27 | -4.38 |
| max drawdown | -2,781.73 | -1,261.64 |
| max drawdown % | -21.97 | -10.68 |
| profit factor | 1.40 | 1.30 |
| unusually bad trades | 3 | 1 |
| … threshold (% of equity) | 6.7 | 4.3 |
| time in market % | 6.5 | 8.4 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.50 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# OBV Leading Breakout

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Volume leads price: buy when OBV makes an n-bar high before price does (price still below its n-bar high) in an uptrend.

## Market
- Symbols: AAPL (base run, spec's instrument); screening over the 516 US stocks from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `OBV > HH(OBV, n)[1]` AND `C < HH(H, n)[1]` AND `C > SMA(100)`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: `OBV < SMA(OBV, 10)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | breakout lookback | 20 | 10–60 | 2 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

SMA(100) trend filter and the SMA(OBV,10) exit are fixed. OBV starts at 0 on the symbol's first bar (only differences matter).

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
