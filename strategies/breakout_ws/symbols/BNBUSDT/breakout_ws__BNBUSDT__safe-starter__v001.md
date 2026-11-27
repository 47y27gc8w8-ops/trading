# breakout_ws__BNBUSDT: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BNBUSDT (crypto, 1d)
**Found at:** iteration 321 of optimization.log (2026-11-23T22:09:10Z); written at the checkpoint in iteration 1590; backtest.py version `777b99fc80`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/4 one-step neighbours profitable in-sample (worst neighbour net 378,601.81)

## Parameters

| parameter | value |
|---|---|
| entry_n | 36 |
| exit_n | 13 |

```json
{
  "entry_n": 36,
  "exit_n": 13
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 401,479.48 | 9,035.52 |
| return % | 4,014.79 | 90.36 |
| return %/year | 89.4 | 24.9 |
| gross profit | 546,761.89 | 18,131.69 |
| gross loss | 145,282.42 | 9,096.17 |
| trades | 20 | 9 |
| win rate % | 50.0 | 44.4 |
| avg win | 54,676.19 | 4,532.92 |
| avg loss | -14,528.24 | -1,819.23 |
| avg result / trade | 20,073.97 | 1,003.95 |
| largest single loss | -57,661.08 | -4,104.76 |
| largest loss % of equity | -12.63 | -17.53 |
| max drawdown | -207,184.75 | -15,245.51 |
| max drawdown % | -37.30 | -49.39 |
| profit factor | 3.76 | 1.99 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 15.8 | 16.2 |
| time in market % | 38.3 | 48.0 |
| buy & hold return % | 2,992.03 | 79.41 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |
| period | 2018-03-06 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

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
