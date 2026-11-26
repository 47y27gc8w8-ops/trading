# kst_cycle_confirmation: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 39612 of optimization.log (2026-11-26T03:00:59Z); written at the checkpoint in iteration 40146; backtest.py version `c6a1335e0b`
**Replaces:** kst_cycle_confirmation__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 3,229.35)

## Parameters

| parameter | value |
|---|---|
| max_candles | 88 |
| signal | 21 |
| stop_atr | 3.5 |
| take_profit_atr | 5.0 |

```json
{
  "max_candles": 88,
  "signal": 21,
  "stop_atr": 3.5,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,953.70 | 1,410.90 |
| return % | 49.54 | 14.11 |
| return %/year | 1.9 | 1.2 |
| gross profit | 9,474.98 | 5,787.25 |
| gross loss | 4,521.28 | 4,376.35 |
| trades | 48 | 36 |
| win rate % | 56.2 | 55.6 |
| avg win | 350.93 | 289.36 |
| avg loss | -215.30 | -273.52 |
| avg result / trade | 103.20 | 39.19 |
| largest single loss | -590.64 | -792.97 |
| largest loss % of equity | -4.26 | -6.88 |
| max drawdown | -1,000.18 | -1,059.56 |
| max drawdown % | -7.25 | -9.09 |
| profit factor | 2.10 | 1.32 |
| unusually bad trades | 3 | 6 |
| … threshold (% of equity) | 2.9 | 2.6 |
| time in market % | 14.9 | 20.0 |
| buy & hold return % | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.63 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# KST Cycle Confirmation

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Pring's Know Sure Thing: buy when the KST crosses above its signal line while KST is positive (momentum cycle turning up in a bullish regime); exit when it falls below the signal.

## Market
- Symbols: SPY (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `KST` crosses above `SMA(KST, signal)` AND `KST > 0`; KST = SMA(ROC10,10) + 2·SMA(ROC15,10) + 3·SMA(ROC20,10) + 4·SMA(ROC30,15).
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `KST < SMA(KST, signal)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| signal | KST signal-line SMA | 9 | 5–15 | 1 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 96 | 48–192 | 8 |

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
- KST ROC/SMA lengths fixed as in INDICATORS.md.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
