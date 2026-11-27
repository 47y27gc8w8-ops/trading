# macd_signal_cross: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 1776 of optimization.log (2026-11-26T05:34:32Z); written at the checkpoint in iteration 27271; backtest.py version `1299a2cc4b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 84,383.18)

## Parameters

| parameter | value |
|---|---|
| max_candles | 48 |
| signal | 5 |
| stop_atr | 1.75 |
| take_profit_atr | 5.5 |

```json
{
  "max_candles": 48,
  "signal": 5,
  "stop_atr": 1.75,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 115,213.47 | 29,459.03 |
| return % | 1,152.13 | 294.59 |
| return %/year | 12.8 | 13.4 |
| gross profit | 229,468.30 | 57,632.99 |
| gross loss | 114,254.83 | 28,173.96 |
| trades | 177 | 104 |
| win rate % | 44.1 | 51.9 |
| avg win | 2,941.90 | 1,067.28 |
| avg loss | -1,154.09 | -563.48 |
| avg result / trade | 650.92 | 283.26 |
| largest single loss | -8,374.59 | -3,973.17 |
| largest loss % of equity | -7.80 | -9.03 |
| max drawdown | -15,168.32 | -6,775.58 |
| max drawdown % | -55.90 | -14.84 |
| profit factor | 2.01 | 2.05 |
| unusually bad trades | 10 | 7 |
| … threshold (% of equity) | 6.2 | 3.3 |
| time in market % | 26.0 | 33.3 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.05 |
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
