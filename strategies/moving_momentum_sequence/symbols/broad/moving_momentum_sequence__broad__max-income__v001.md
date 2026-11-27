# moving_momentum_sequence__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 41 of optimization.log (2026-11-25T23:47:28Z); written at the checkpoint in iteration 223; backtest.py version `d97ae6e4c4`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 63.90)

## Parameters

| parameter | value |
|---|---|
| max_candles | 108 |
| oversold | 18 |
| stop_atr | 2.25 |
| take_profit_atr | 4.0 |

```json
{
  "max_candles": 108,
  "oversold": 18,
  "stop_atr": 2.25,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 171.79 | 610.52 |
| return % | 1.72 | 6.11 |
| return %/year | 0.1 | 0.6 |
| gross profit | 1,130.46 | 1,569.17 |
| gross loss | 958.67 | 958.65 |
| trades | 865 | 743 |
| win rate % | 59.2 | 59.0 |
| avg win | 2.21 | 3.58 |
| avg loss | -2.72 | -3.14 |
| avg result / trade | 0.20 | 0.82 |
| largest single loss | -19.30 | -93.37 |
| largest loss % of equity | -10.42 | -26.22 |
| max drawdown | -138.07 | -200.86 |
| max drawdown % | -1.36 | -1.94 |
| profit factor | 1.18 | 1.64 |
| unusually bad trades | 102 | 86 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 0.9 | 1.9 |
| buy & hold return % | 97.45 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 6.88 |
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
