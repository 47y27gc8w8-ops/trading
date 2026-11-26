# golden_cross__SOXX: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SOXX (etf, 1d)
**Found at:** iteration 199 of optimization.log (2026-11-26T02:13:09Z); written at the checkpoint in iteration 421; backtest.py version `d48a95163b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,130.09)
**Range warning:** stop_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 35 |
| max_candles | 96 |
| slow | 200 |
| stop_atr | 1.0 |
| take_profit_atr | 10.0 |

```json
{
  "fast": 35,
  "max_candles": 96,
  "slow": 200,
  "stop_atr": 1.0,
  "take_profit_atr": 10.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 12,442.15 | 4,817.40 |
| return % | 124.42 | 48.17 |
| return %/year | 6.5 | 3.7 |
| gross profit | 14,442.65 | 5,533.29 |
| gross loss | 2,000.50 | 715.89 |
| trades | 10 | 5 |
| win rate % | 40.0 | 40.0 |
| avg win | 3,610.66 | 2,766.65 |
| avg loss | -333.42 | -238.63 |
| avg result / trade | 1,244.21 | 963.48 |
| largest single loss | -414.71 | -363.49 |
| largest loss % of equity | -1.99 | -3.77 |
| max drawdown | -1,370.28 | -1,026.81 |
| max drawdown % | -9.21 | -9.82 |
| profit factor | 7.22 | 7.73 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 3.9 | 3.9 |
| time in market % | 10.2 | 6.5 |
| buy & hold return % | 179.81 | 1,491.27 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.57 |
| period | 2003-02-20 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Golden Cross

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Classic trend following: buy when the fast SMA crosses above the slow SMA, sell on the death cross, with an ATR stop, ATR target and time cap.

## Market
- Symbols: SPY (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `SMA(fast)` crosses above `SMA(slow)`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `SMA(fast)` crosses below `SMA(slow)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| fast | fast SMA | 50 | 20–80 | 5 |
| slow | slow SMA | 200 | 120–300 (hard max 380) | 10 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 96 | 48–192 | 8 |

Constraints: `fast < slow`. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 400 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- Base symbol SPY (spec lists SPY, VTI; VTI is covered by the ETF screen).
- Folder name golden_cross is the library spec; the older golden_cross_ws/_bl folders are separate experiments.
- A cross is a one-bar event, so after an ATR stop/target/time exit the strategy waits for the next golden cross (literal reading of the spec).

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
