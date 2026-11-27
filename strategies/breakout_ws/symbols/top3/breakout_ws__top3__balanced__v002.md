# breakout_ws__top3: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** ETHUSDT, ETCUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 212 of optimization.log (2026-11-23T22:09:53Z); written at the checkpoint in iteration 1379; backtest.py version `5f036785d9`
**Replaces:** breakout_ws__top3__balanced__v001.md
**Robustness:** 3/3 one-step neighbours profitable in-sample (worst neighbour net 82,345.66)

## Parameters

| parameter | value |
|---|---|
| entry_n | 32 |
| exit_n | 2 |

```json
{
  "entry_n": 32,
  "exit_n": 2
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 93,609.50 | 4,114.89 |
| return % | 936.09 | 41.15 |
| return %/year | 47.7 | 12.7 |
| gross profit | 155,163.81 | 10,412.48 |
| gross loss | 61,554.31 | 6,297.59 |
| trades | 99 | 38 |
| win rate % | 49.5 | 44.7 |
| avg win | 3,166.61 | 612.50 |
| avg loss | -1,231.09 | -299.89 |
| avg result / trade | 945.55 | 108.29 |
| largest single loss | -10,775.86 | -703.91 |
| largest loss % of equity | -20.53 | -9.86 |
| max drawdown | -38,970.13 | -2,877.25 |
| max drawdown % | -33.47 | -16.93 |
| profit factor | 2.52 | 1.65 |
| unusually bad trades | 9 | 1 |
| … threshold (% of equity) | 12.0 | 12.5 |
| time in market % | 15.1 | 11.1 |
| buy & hold return % | 265.38 | -61.67 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

## Rules (strategy.md at the time of saving)

# Breakout (Donchian channel, long only)

Source: original.md (user's description, 2026-11-23). This file is the testable version.

## Idea
Buy strength: when a coin closes above its recent highest high it may be starting a trend;
ride it until it closes below its recent lowest low. The user expects it to work only on
coins that trend a lot, so the main question is *which* coins.

## Market
- Symbols: base run on BTCUSDT (assumption, see below); screening over the crypto universe
  (Binance USDT pairs) picks the coins for per-symbol and basket runs
- Timeframe: 1d bars (UTC), built from Binance 1m data
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of day t (only day t and earlier are used):
- `close[t] > max(high[t-entry_n] … high[t-1])` (highest high of the previous `entry_n` days, today excluded)
Order: buy at the open of day t+1 (only when flat).

## Sell trigger
Close the position when:
- `close[t] < min(low[t-exit_n] … low[t-1])` (lowest low of the previous `exit_n` days, today excluded) → sell at the next open
No stop loss, target, trailing stop or time exit (the description has none).

## Parameters
| name | meaning | description's value | range | step |
|---|---|---|---|---|
| entry_n | breakout channel length (days) | 20 | 5–60 (may widen to 110) | 1 |
| exit_n | exit channel length (days) | 10 | 3–30 (may widen to 110) | 1 |

Constraints: none between the two lengths (the description sets none). Grid: 56 × 28 = 1,568 sets.

## Setup
- Data: Binance daily bars; trading from 2018-01-01 (or a coin's 120th day) → 2026-11-22 (frozen)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, fractional units allowed
- Fees 0.10% per side, slippage 0.10% per fill

## Assumptions
- Base symbol BTCUSDT: the description names no coin; BTC is the most liquid with the longest history.
- "Previous 20 days" excludes the current day (otherwise a close can never exceed a high that includes itself).
- Highs/lows (not closes) define the channel, as written.
- Slippage 0.10% (smaller-coin value) for every symbol, since the screen includes smaller coins.
- Optimizer gates adapted to a slow trend follower: min_trades_is 12 (≈ 4 trades/yr, coins listed
  2019–2021 have only 2–5 IS years), balanced_min_win_rate 35 (trend followers usually win 35–45%).
- Budget: the user asked for ~10 minutes in total; all stages are scaled down to fit.

## Open questions
- None blocking. Could ask: should "previous 20 days" include today (no, impossible as written)?
  Fees/slippage different from 0.10%/0.10%?

---
Backtest results don't guarantee future performance.
