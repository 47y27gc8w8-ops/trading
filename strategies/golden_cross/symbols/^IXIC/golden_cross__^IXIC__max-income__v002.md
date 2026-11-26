# golden_cross__^IXIC: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** ^IXIC (etf, 1d)
**Found at:** iteration 954 of optimization.log (2026-11-26T02:12:58Z); written at the checkpoint in iteration 1421; backtest.py version `c9c614bfa8`
**Replaces:** golden_cross__^IXIC__max-income__v001.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 19,010.01)
**Range warning:** take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 10 |
| max_candles | 64 |
| slow | 270 |
| stop_atr | 4.0 |
| take_profit_atr | 10.5 |

```json
{
  "fast": 10,
  "max_candles": 64,
  "slow": 270,
  "stop_atr": 4.0,
  "take_profit_atr": 10.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 35,793.69 | 6,574.88 |
| return % | 357.94 | 65.75 |
| return %/year | 7.5 | 4.8 |
| gross profit | 37,311.86 | 7,347.62 |
| gross loss | 1,518.17 | 772.74 |
| trades | 20 | 9 |
| win rate % | 85.0 | 66.7 |
| avg win | 2,194.82 | 1,224.60 |
| avg loss | -506.06 | -257.58 |
| avg result / trade | 1,789.68 | 730.54 |
| largest single loss | -1,008.11 | -381.22 |
| largest loss % of equity | -2.64 | -3.81 |
| max drawdown | -2,786.66 | -761.67 |
| max drawdown % | -14.42 | -7.25 |
| profit factor | 24.58 | 9.51 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 2.2 | 4.5 |
| time in market % | 17.0 | 14.9 |
| buy & hold return % | 566.49 | 391.86 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.63 |
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
