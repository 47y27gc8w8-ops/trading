# low_volume_pullback_rebound: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 37109 of optimization.log (2026-11-26T04:28:04Z); written at the checkpoint in iteration 48212; backtest.py version `834d5c61c2`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 38,042.12)

## Parameters

| parameter | value |
|---|---|
| fraction | 0.85 |
| max_candles | 32 |
| stop_atr | 2.5 |
| take_profit_atr | 7.0 |

```json
{
  "fraction": 0.85,
  "max_candles": 32,
  "stop_atr": 2.5,
  "take_profit_atr": 7.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 67,149.73 | 6,219.50 |
| return % | 671.50 | 62.19 |
| return %/year | 10.2 | 4.5 |
| gross profit | 140,297.89 | 18,678.55 |
| gross loss | 73,148.16 | 12,459.06 |
| trades | 113 | 55 |
| win rate % | 38.0 | 41.8 |
| avg win | 3,262.74 | 812.11 |
| avg loss | -1,044.97 | -389.35 |
| avg result / trade | 594.25 | 113.08 |
| largest single loss | -3,942.66 | -1,133.95 |
| largest loss % of equity | -4.56 | -8.45 |
| max drawdown | -18,628.08 | -2,841.35 |
| max drawdown % | -42.23 | -17.62 |
| profit factor | 1.92 | 1.50 |
| unusually bad trades | 8 | 7 |
| … threshold (% of equity) | 6.3 | 4.3 |
| time in market % | 21.7 | 26.6 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.44 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Low Volume Pullback Rebound

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
In an uptrend, a down day on very light volume is a weak pullback; buy when the next close takes out that day's high, exit when price loses the 20-day EMA.

## Market
- Symbols: AAPL (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's stock list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `C[1] < C[2]` AND `V[1] < fraction × SMA(V,20)[2]` AND `C > H[1]` AND `C > SMA(100)`.
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
| fraction | volume vs 20-bar baseline | 0.6 | 0.3–0.9 (hard 0.05–1) | 0.05 |
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
- Screening universe: Yahoo stocks (spec: stock); listed instruments are alternatives, tested separately.
- Symbols without volume (zero) never signal.
- SMA(V,20), SMA(100) and EMA(20) are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
