# range_box_breakout: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 992 of optimization.log (2026-11-25T10:33:42Z); written at the checkpoint in iteration 1493; backtest.py version `b039e0a41a`
**Replaces:** range_box_breakout__max-income__v001.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 148,901.32)

## Parameters

| parameter | value |
|---|---|
| max_candles | 24 |
| n | 19 |
| stop_atr | 4.0 |
| take_profit_atr | 4.5 |
| width | 6.75 |

```json
{
  "max_candles": 24,
  "n": 19,
  "stop_atr": 4.0,
  "take_profit_atr": 4.5,
  "width": 6.75
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 318,961.43 | 10,214.37 |
| return % | 3,189.61 | 102.14 |
| return %/year | 18.1 | 6.7 |
| gross profit | 588,207.66 | 40,172.55 |
| gross loss | 269,246.22 | 29,958.19 |
| trades | 129 | 81 |
| win rate % | 52.7 | 51.9 |
| avg win | 8,650.11 | 956.49 |
| avg loss | -4,413.87 | -768.16 |
| avg result / trade | 2,472.57 | 126.10 |
| largest single loss | -30,217.03 | -2,034.47 |
| largest loss % of equity | -8.32 | -10.11 |
| max drawdown | -59,594.65 | -5,945.15 |
| max drawdown % | -36.66 | -22.98 |
| profit factor | 2.19 | 1.34 |
| unusually bad trades | 11 | 5 |
| … threshold (% of equity) | 8.2 | 7.2 |
| time in market % | 27.0 | 37.7 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.37 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Range Box Breakout

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Buy the upside break of a tight n-bar box (box height small relative to ATR); exit below EMA(20).

## Market
- Symbols: AAPL (base run, spec's instrument); screening over the 516 US stocks from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- `(HH(H,n)[1] - LL(L,n)[1]) / ATR(14)[1] < width` AND `C > HH(H,n)[1]`
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
| n | box length | 10 | 5–30 | 1 |
| width | max box height in ATRs | 4.0 | 2.0–8.0 | 0.25 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 48 | 24–96 | 6 |

ATR(14) (Wilder) and the EMA(20) exit are fixed.

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
