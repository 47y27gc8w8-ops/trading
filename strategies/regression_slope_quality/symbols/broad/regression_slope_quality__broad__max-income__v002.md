# regression_slope_quality__broad: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ (etf, 1d)
**Found at:** iteration 753 of optimization.log (2026-11-25T11:53:59Z); written at the checkpoint in iteration 1254; backtest.py version `67a06b638d`
**Replaces:** regression_slope_quality__broad__max-income__v001.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 2,600.33)

## Parameters

| parameter | value |
|---|---|
| max_candles | 156 |
| n | 110 |
| r2 | 0.44 |
| stop_atr | 4.25 |
| take_profit_atr | 10.5 |

```json
{
  "max_candles": 156,
  "n": 110,
  "r2": 0.44,
  "stop_atr": 4.25,
  "take_profit_atr": 10.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,968.41 | 2,849.38 |
| return % | 39.68 | 28.49 |
| return %/year | 1.6 | 2.3 |
| gross profit | 7,061.71 | 6,346.00 |
| gross loss | 3,093.30 | 3,496.62 |
| trades | 545 | 556 |
| win rate % | 50.3 | 46.0 |
| avg win | 25.77 | 24.79 |
| avg loss | -11.41 | -11.66 |
| avg result / trade | 7.28 | 5.12 |
| largest single loss | -39.45 | -210.42 |
| largest loss % of equity | -11.57 | -24.53 |
| max drawdown | -1,131.70 | -748.94 |
| max drawdown % | -7.96 | -6.89 |
| profit factor | 2.28 | 1.81 |
| unusually bad trades | 34 | 26 |
| … threshold (% of equity) | 8.2 | 8.2 |
| time in market % | 15.1 | 24.0 |
| buy & hold return % | 114.15 | 305.61 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.46 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Regression Slope Quality

Source: original.md (research-library spec, 2026-11-24). This file is the testable version.
EXECUTION.md and INDICATORS.md (repo root) apply: indicator formulas follow INDICATORS.md.

## Idea
Buy when an up-trend becomes clean (log-price regression R2 rises through a threshold with a positive slope); exit when the slope turns or the fit falls apart.

## Market
- Symbols: SPY (base run, spec's instrument); screening over the 56 US ETFs from config/symbols.yaml
  (without `^` indices, `.SW` and other non-US listings: other currency and costs)
- Data: Yahoo daily bars, adjusted for dividends and splits
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (only bar t and earlier):
- OLS of log(C) over the n bars ending at t: slope > 0 AND `R2` crosses above `r2`
- not vetoed: the signal exit below is not already true on bar t
Order: buy at the open of bar t+1. Skipped if ATR(14) of bar t is ≤ 0 / missing or the stop would be ≤ 0.

## Sell trigger
First of:
- signal exit: slope <= 0 OR `R2 < 0.2` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A → fill at that level (at the open if it gaps below), E = entry fill, A = Wilder ATR(14) of the signal bar, both frozen
- target: high ≥ E + take_profit_atr × A → fill at the target level
- time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- stop is assumed before target when one bar touches both; after a stop/target exit one fully flat bar must complete before a new signal counts

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | regression window | 60 | 30–120 | 5 |
| r2 | R2 entry threshold | 0.6 | 0.4–0.8 | 0.02 |
| stop_atr | stop = entry fill − stop_atr × ATR(14) of the signal bar | 2 | 1–4 (hard ≥ 0.5) | 0.25 |
| take_profit_atr | target = entry fill + take_profit_atr × the same ATR | 3 | 1.5–6 (hard ≥ 0.5) | 0.5 |
| max_candles | time exit after this many completed held bars | 96 | 48–192 | 12 |

The R2 exit level 0.2 is fixed. GLD (spec's second instrument) is covered by screening.

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
