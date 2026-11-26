# golden_cross__top3: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** ^IXIC, SOXX, SMH (etf, 1d)
**Found at:** iteration 568 of optimization.log (2026-11-26T02:14:06Z); written at the checkpoint in iteration 582; backtest.py version `58457d9bf2`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 3,562.01)
**Range warning:** fast is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 20 |
| max_candles | 128 |
| slow | 280 |
| stop_atr | 2.0 |
| take_profit_atr | 6.0 |

```json
{
  "fast": 20,
  "max_candles": 128,
  "slow": 280,
  "stop_atr": 2.0,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 5,520.60 | 3,924.19 |
| return % | 55.21 | 39.24 |
| return %/year | 2.1 | 3.1 |
| gross profit | 8,279.41 | 5,325.78 |
| gross loss | 2,758.81 | 1,401.58 |
| trades | 37 | 21 |
| win rate % | 56.8 | 42.9 |
| avg win | 394.26 | 591.75 |
| avg loss | -172.43 | -116.80 |
| avg result / trade | 149.21 | 186.87 |
| largest single loss | -319.73 | -265.99 |
| largest loss % of equity | -4.93 | -6.95 |
| max drawdown | -976.25 | -791.42 |
| max drawdown % | -6.13 | -7.86 |
| profit factor | 3.00 | 3.80 |
| unusually bad trades | 1 | 1 |
| … threshold (% of equity) | 7.7 | 6.5 |
| time in market % | 6.0 | 7.6 |
| buy & hold return % | 256.65 | 1,237.80 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.46 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

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
