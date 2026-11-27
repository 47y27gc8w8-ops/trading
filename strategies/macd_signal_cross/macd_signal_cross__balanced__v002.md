# macd_signal_cross: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 27428 of optimization.log (2026-11-26T05:47:15Z); written at the checkpoint in iteration 27799; backtest.py version `1299a2cc4b`
**Replaces:** macd_signal_cross__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 11,300.89)

## Parameters

| parameter | value |
|---|---|
| max_candles | 112 |
| signal | 4 |
| stop_atr | 1.5 |
| take_profit_atr | 2.0 |

```json
{
  "max_candles": 112,
  "signal": 4,
  "stop_atr": 1.5,
  "take_profit_atr": 2.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 38,641.32 | 17,227.26 |
| return % | 386.41 | 172.27 |
| return %/year | 7.8 | 9.6 |
| gross profit | 92,879.74 | 38,290.29 |
| gross loss | 54,238.42 | 21,063.04 |
| trades | 195 | 117 |
| win rate % | 47.7 | 57.3 |
| avg win | 998.71 | 571.50 |
| avg loss | -531.75 | -421.26 |
| avg result / trade | 198.16 | 147.24 |
| largest single loss | -2,118.85 | -2,627.17 |
| largest loss % of equity | -5.51 | -9.03 |
| max drawdown | -5,019.25 | -4,787.43 |
| max drawdown % | -34.96 | -19.29 |
| profit factor | 1.71 | 1.82 |
| unusually bad trades | 9 | 6 |
| … threshold (% of equity) | 5.6 | 3.7 |
| time in market % | 16.4 | 17.1 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.23 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# MACD Signal Cross

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Buy MACD(12,26) crossing above its signal line while price is above the 200-day SMA; exit on the cross back below.

## Market
- Symbols: AAPL (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's stock list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `MACD(12,26)` crosses above `EMA(MACD, signal)` AND `C > SMA(200)`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `MACD(12,26)` crosses below `EMA(MACD, signal)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| signal | MACD signal EMA | 9 | 5–15 | 1 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 96 | 48–192 | 8 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 250 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo stocks (spec: stock); listed instruments are alternatives, tested separately.
- Base symbol AAPL (spec lists AAPL, MSFT; MSFT is covered by the stock screen).
- MACD 12/26 and SMA(200) are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
