# linear_regression_residual_reversion: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 88 of optimization.log (2026-11-26T04:01:45Z); written at the checkpoint in iteration 363; backtest.py version `b3a0f0afae`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 10,122.96)

## Parameters

| parameter | value |
|---|---|
| max_candles | 11 |
| n | 60 |
| stop_atr | 2.75 |
| take_profit_atr | 4.0 |
| z | 2.25 |

```json
{
  "max_candles": 11,
  "n": 60,
  "stop_atr": 2.75,
  "take_profit_atr": 4.0,
  "z": 2.25
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 14,965.04 | 1,888.92 |
| return % | 149.65 | 18.89 |
| return %/year | 4.5 | 1.6 |
| gross profit | 29,226.74 | 10,178.06 |
| gross loss | 14,261.69 | 8,289.14 |
| trades | 105 | 61 |
| win rate % | 64.8 | 54.1 |
| avg win | 429.80 | 308.43 |
| avg loss | -385.45 | -296.04 |
| avg result / trade | 142.52 | 30.97 |
| largest single loss | -1,161.90 | -571.10 |
| largest loss % of equity | -6.14 | -5.64 |
| max drawdown | -2,681.67 | -1,720.54 |
| max drawdown % | -13.49 | -16.13 |
| profit factor | 2.05 | 1.23 |
| unusually bad trades | 4 | 2 |
| … threshold (% of equity) | 4.2 | 5.4 |
| time in market % | 16.9 | 16.5 |
| buy & hold return % | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.36 |
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
