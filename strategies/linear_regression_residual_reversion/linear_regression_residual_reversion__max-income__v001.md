# linear_regression_residual_reversion: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 150 of optimization.log (2026-11-26T04:01:46Z); written at the checkpoint in iteration 362; backtest.py version `b3a0f0afae`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 7,918.64)
**Range warning:** n is at the max of its range, z is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 14 |
| n | 120 |
| stop_atr | 2.75 |
| take_profit_atr | 4.0 |
| z | 1.5 |

```json
{
  "max_candles": 14,
  "n": 120,
  "stop_atr": 2.75,
  "take_profit_atr": 4.0,
  "z": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 24,993.71 | 3,035.75 |
| return % | 249.94 | 30.36 |
| return %/year | 6.2 | 2.5 |
| gross profit | 55,483.09 | 16,156.18 |
| gross loss | 30,489.38 | 13,120.42 |
| trades | 120 | 75 |
| win rate % | 69.2 | 60.0 |
| avg win | 668.47 | 359.03 |
| avg loss | -824.04 | -437.35 |
| avg result / trade | 208.28 | 40.48 |
| largest single loss | -2,630.15 | -1,137.37 |
| largest loss % of equity | -7.21 | -10.21 |
| max drawdown | -5,960.04 | -3,683.18 |
| max drawdown % | -19.20 | -28.37 |
| profit factor | 1.82 | 1.23 |
| unusually bad trades | 1 | 2 |
| … threshold (% of equity) | 6.6 | 6.8 |
| time in market % | 22.2 | 24.4 |
| buy & hold return % | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.40 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Linear Regression Residual Reversion

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Fit a log-price trend line on the preceding n bars; when today's close sits more than z residual standard deviations below the line of an up-sloping trend, buy the dip and exit when price is back on the line.

## Market
- Symbols: SPY (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): OLS of log(C) on time 0..n−1 over the preceding n bars (t−n…t−1, excluding t); residual = log(C_t) − line extrapolated to index n; `residual / sqrt(SSE/n) < −z` AND slope > 0.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `log(C_t) >= ` the next-bar extrapolated line refitted on the preceding n bars (residual ≥ 0) at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | regression window | 60 | 30–120 (hard 10–180) | 5 |
| z | entry deviation, residual std units | 2 | 1.5–3 | 0.25 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 12 | 6–24 | 1 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 200 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- Residual std is the population std of the formation residuals, sqrt(SSE/n) (INDICATORS.md).

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
