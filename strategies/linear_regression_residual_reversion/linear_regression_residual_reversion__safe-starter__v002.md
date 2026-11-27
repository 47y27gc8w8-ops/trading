# linear_regression_residual_reversion: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 971 of optimization.log (2026-11-26T04:02:04Z); written at the checkpoint in iteration 1476; backtest.py version `b3a0f0afae`
**Replaces:** linear_regression_residual_reversion__safe-starter__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 8,196.22)

## Parameters

| parameter | value |
|---|---|
| max_candles | 24 |
| n | 170 |
| stop_atr | 2.25 |
| take_profit_atr | 4.0 |
| z | 3.0 |

```json
{
  "max_candles": 24,
  "n": 170,
  "stop_atr": 2.25,
  "take_profit_atr": 4.0,
  "z": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 13,763.15 | 3,010.12 |
| return % | 137.63 | 30.10 |
| return %/year | 4.2 | 2.5 |
| gross profit | 19,073.83 | 8,383.79 |
| gross loss | 5,310.68 | 5,373.67 |
| trades | 37 | 22 |
| win rate % | 73.0 | 50.0 |
| avg win | 706.44 | 762.16 |
| avg loss | -531.07 | -488.52 |
| avg result / trade | 371.98 | 136.82 |
| largest single loss | -869.97 | -961.73 |
| largest loss % of equity | -4.40 | -8.95 |
| max drawdown | -1,371.21 | -2,530.46 |
| max drawdown % | -7.77 | -21.77 |
| profit factor | 3.59 | 1.56 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 6.7 | 7.0 |
| time in market % | 10.3 | 7.0 |
| buy & hold return % | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.58 |
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
