# market_residual_stock_rebound: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 1289 of optimization.log (2026-11-26T06:54:29Z); written at the checkpoint in iteration 1774; backtest.py version `6f443a3d30`
**Replaces:** market_residual_stock_rebound__max-income__v001.md
**Robustness:** 8/9 one-step neighbours profitable in-sample (worst neighbour net -855.49)

## Parameters

| parameter | value |
|---|---|
| max_candles | 56 |
| n | 63 |
| stop_atr | 2.25 |
| take_profit_atr | 0.5 |
| z | 1.75 |

```json
{
  "max_candles": 56,
  "n": 63,
  "stop_atr": 2.25,
  "take_profit_atr": 0.5,
  "z": 1.75
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,798.05 | 1,219.45 |
| return % | 37.98 | 12.19 |
| return %/year | 1.6 | 1.1 |
| gross profit | 11,978.52 | 5,679.95 |
| gross loss | 8,180.46 | 4,460.50 |
| trades | 80 | 62 |
| win rate % | 76.2 | 80.7 |
| avg win | 196.37 | 113.60 |
| avg loss | -430.55 | -371.71 |
| avg result / trade | 47.48 | 19.67 |
| largest single loss | -1,149.18 | -575.62 |
| largest loss % of equity | -11.32 | -5.12 |
| max drawdown | -1,815.15 | -1,437.46 |
| max drawdown % | -17.88 | -13.55 |
| profit factor | 1.46 | 1.27 |
| unusually bad trades | 3 | 0 |
| … threshold (% of equity) | 5.7 | 7.8 |
| time in market % | 2.6 | 2.5 |
| buy & hold return % | 8,135.28 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.68 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Market Residual Stock Rebound

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Regress the stock's daily return on SPY's over the preceding n days; when today's stock-specific (residual) return is more than z standard deviations below normal while both the stock and SPY are above their 200-day SMA, buy the idiosyncratic dip and exit on a close above the 5-day SMA.

## Market
- Symbols: AAPL (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's stock list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): OLS `r = alpha + beta × r_SPY` on the preceding n daily returns (excluding t); `(r_t − alpha − beta·r_SPY,t) / sqrt(SSE/n) < −z` AND `C > SMA(200)` AND `SPY C > SMA(200)` (SPY aligned by date, no forward fill).
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C > SMA(5)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | regression window, bars | 126 | 63–252 (hard 21–315) | 21 |
| z | entry deviation, residual std units | 2 | 1.5–3 | 0.25 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 330 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo stocks (spec: stock); listed instruments are alternatives, tested separately.
- Reference is SPY for every traded symbol (screening other stocks keeps SPY as the market).
- SPY's SMA(200) is computed on SPY closes aligned to the traded symbol's dates; a missing SPY bar gives no signal.
- Returns are simple daily returns of adjusted closes.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
