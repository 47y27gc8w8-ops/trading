# obv_leading_breakout: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 464 of optimization.log (2026-11-25T07:17:33Z); written at the checkpoint in iteration 1079; backtest.py version `685cc94aa3`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 8,944.43)

## Parameters

| parameter | value |
|---|---|
| max_candles | 78 |
| n | 50 |
| stop_atr | 1.0 |
| take_profit_atr | 2.0 |

```json
{
  "max_candles": 78,
  "n": 50,
  "stop_atr": 1.0,
  "take_profit_atr": 2.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 13,084.59 | 2,766.13 |
| return % | 130.85 | 27.66 |
| return %/year | 4.1 | 2.3 |
| gross profit | 48,768.93 | 11,341.41 |
| gross loss | 35,684.34 | 8,575.29 |
| trades | 141 | 71 |
| win rate % | 45.4 | 42.2 |
| avg win | 762.01 | 378.05 |
| avg loss | -463.43 | -209.15 |
| avg result / trade | 92.80 | 38.96 |
| largest single loss | -1,219.34 | -445.19 |
| largest loss % of equity | -5.23 | -3.53 |
| max drawdown | -4,222.91 | -1,488.56 |
| max drawdown % | -28.83 | -11.81 |
| profit factor | 1.37 | 1.32 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 6.3 | 3.8 |
| time in market % | 7.7 | 8.3 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.56 |
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
