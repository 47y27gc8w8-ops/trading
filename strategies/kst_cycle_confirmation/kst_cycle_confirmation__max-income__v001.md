# kst_cycle_confirmation: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 27714 of optimization.log (2026-11-26T02:56:59Z); written at the checkpoint in iteration 39564; backtest.py version `c6a1335e0b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 2,985.49)

## Parameters

| parameter | value |
|---|---|
| max_candles | 160 |
| signal | 17 |
| stop_atr | 3.5 |
| take_profit_atr | 4.5 |

```json
{
  "max_candles": 160,
  "signal": 17,
  "stop_atr": 3.5,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,129.91 | 1,482.99 |
| return % | 41.30 | 14.83 |
| return %/year | 1.7 | 1.3 |
| gross profit | 10,329.70 | 5,665.15 |
| gross loss | 6,199.79 | 4,182.16 |
| trades | 58 | 38 |
| win rate % | 58.6 | 55.3 |
| avg win | 303.81 | 269.77 |
| avg loss | -258.32 | -246.01 |
| avg result / trade | 71.21 | 39.03 |
| largest single loss | -724.62 | -763.03 |
| largest loss % of equity | -5.02 | -6.88 |
| max drawdown | -2,839.37 | -1,308.26 |
| max drawdown % | -19.36 | -11.28 |
| profit factor | 1.67 | 1.35 |
| unusually bad trades | 4 | 5 |
| … threshold (% of equity) | 2.9 | 2.7 |
| time in market % | 14.9 | 19.1 |
| buy & hold return % | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.77 |
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
