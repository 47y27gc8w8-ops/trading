# elder_impulse_onset: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** MSFT (etf, 1d)
**Found at:** iteration 819 of optimization.log (2026-11-25T23:27:51Z); written at the checkpoint in iteration 862; backtest.py version `10a8dc4c3f`
**Replaces:** elder_impulse_onset__balanced__v001.md
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -4,003.76)

## Parameters

| parameter | value |
|---|---|
| max_candles | 160 |
| n | 25 |
| stop_atr | 3.75 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 160,
  "n": 25,
  "stop_atr": 3.75,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,095.36 | 693.78 |
| return % | 40.95 | 6.94 |
| return %/year | 1.6 | 0.6 |
| gross profit | 59,437.21 | 26,120.37 |
| gross loss | 55,341.86 | 25,426.59 |
| trades | 266 | 183 |
| win rate % | 49.6 | 50.8 |
| avg win | 450.28 | 280.86 |
| avg loss | -413.00 | -282.52 |
| avg result / trade | 15.40 | 3.79 |
| largest single loss | -1,654.18 | -1,003.37 |
| largest loss % of equity | -10.02 | -8.18 |
| max drawdown | -11,101.03 | -4,113.24 |
| max drawdown % | -57.19 | -33.52 |
| profit factor | 1.07 | 1.03 |
| unusually bad trades | 25 | 9 |
| … threshold (% of equity) | 5.0 | 4.9 |
| time in market % | 26.9 | 35.5 |
| buy & hold return % | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.38 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Elder Impulse Onset

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Elder impulse system: buy the first bar where both the EMA slope and the MACD histogram turn up together (inertia + momentum) above the 100-day trend; exit when both turn down.

## Market
- Symbols: MSFT (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's stock list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `EMA(n) > EMA(n)[1]` AND `MACDhist(12,26,9) > MACDhist[1]`, while that conjunction was false on the preceding bar, AND `C > SMA(100)`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `EMA(n) < EMA(n)[1]` AND `MACDhist < MACDhist[1]` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | impulse EMA length | 13 | 8–26 | 1 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 96 | 48–192 | 8 |

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
- Screening universe: Yahoo stocks (spec: stock); listed instruments are alternatives, tested separately.
- Base symbol MSFT (spec lists MSFT, AAPL as alternatives; AAPL is covered by the stock screen).
- MACD(12,26,9) and SMA(100) are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
