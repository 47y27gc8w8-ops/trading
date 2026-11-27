# keltner_upper_breakout: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** GLD (etf, 1d)
**Found at:** iteration 22385 of optimization.log (2026-11-26T02:34:05Z); written at the checkpoint in iteration 22887; backtest.py version `dcee56cb53`
**Replaces:** keltner_upper_breakout__balanced__v001.md
**Robustness:** 5/6 one-step neighbours profitable in-sample (worst neighbour net -70.82)

## Parameters

| parameter | value |
|---|---|
| k | 0.75 |
| max_candles | 8 |
| stop_atr | 1.0 |
| take_profit_atr | 6.0 |

```json
{
  "k": 0.75,
  "max_candles": 8,
  "stop_atr": 1.0,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 6,291.05 | 1,371.71 |
| return % | 62.91 | 13.72 |
| return %/year | 4.8 | 1.2 |
| gross profit | 18,070.02 | 10,917.01 |
| gross loss | 11,778.97 | 9,545.30 |
| trades | 99 | 118 |
| win rate % | 46.5 | 39.0 |
| avg win | 392.83 | 237.33 |
| avg loss | -222.24 | -132.57 |
| avg result / trade | 63.55 | 11.62 |
| largest single loss | -515.84 | -435.42 |
| largest loss % of equity | -4.26 | -3.60 |
| max drawdown | -1,830.80 | -2,215.51 |
| max drawdown % | -10.39 | -20.50 |
| profit factor | 1.53 | 1.14 |
| unusually bad trades | 3 | 5 |
| … threshold (% of equity) | 3.0 | 2.6 |
| time in market % | 18.6 | 20.1 |
| buy & hold return % | 130.80 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.25 |
| period | 2005-06-24 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Keltner Upper Breakout

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Volatility breakout: buy when the close breaks above the upper Keltner channel while the 20-day EMA is rising; exit when price falls back below the EMA.

## Market
- Symbols: GLD (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `C` crosses above `KC_upper(20,10,k) = EMA(20) + k × ATR(10)` AND `EMA(20) > EMA(20)[5]`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C < EMA(20)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| k | Keltner ATR multiplier | 2 | 1–3 | 0.25 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 150 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- EMA(20), ATR(10) and the 5-bar slope lag are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
