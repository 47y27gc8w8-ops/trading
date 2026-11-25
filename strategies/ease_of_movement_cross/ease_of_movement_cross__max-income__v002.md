# ease_of_movement_cross: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** GLD (etf, 1d)
**Found at:** iteration 406 of optimization.log (2026-11-25T23:07:54Z); written at the checkpoint in iteration 808; backtest.py version `cd6d51b443`
**Replaces:** ease_of_movement_cross__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 2,464.30)

## Parameters

| parameter | value |
|---|---|
| max_candles | 44 |
| n | 23 |
| stop_atr | 1.75 |
| take_profit_atr | 6.5 |

```json
{
  "max_candles": 44,
  "n": 23,
  "stop_atr": 1.75,
  "take_profit_atr": 6.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 7,981.31 | 3,924.82 |
| return % | 79.81 | 39.25 |
| return %/year | 5.8 | 3.1 |
| gross profit | 16,685.65 | 10,757.52 |
| gross loss | 8,704.34 | 6,832.69 |
| trades | 62 | 82 |
| win rate % | 43.5 | 36.6 |
| avg win | 617.99 | 358.58 |
| avg loss | -248.70 | -131.40 |
| avg result / trade | 128.73 | 47.86 |
| largest single loss | -751.21 | -370.27 |
| largest loss % of equity | -4.82 | -3.96 |
| max drawdown | -3,010.44 | -1,549.10 |
| max drawdown % | -14.62 | -15.32 |
| profit factor | 1.92 | 1.57 |
| unusually bad trades | 1 | 3 |
| … threshold (% of equity) | 3.4 | 2.7 |
| time in market % | 23.1 | 23.7 |
| buy & hold return % | 128.41 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.53 |
| period | 2005-09-06 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Ease Of Movement Cross

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Ease of Movement (price change per unit of volume) turns positive on average while price is above its 100-day trend: buy easy upward movement, exit when its average turns negative.

## Market
- Symbols: GLD (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `SMA(EOM, n)` crosses above 0 AND `C > SMA(100)`; EOM = ((H+L)/2 − (H[1]+L[1])/2) × (H−L) / V, bars with V = 0 skipped.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `SMA(EOM, n) < 0` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | EOM smoothing length | 14 | 7–28 | 1 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

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
- SMA(100) trend filter is a fixed constant (not in the spec's parameter table).

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
