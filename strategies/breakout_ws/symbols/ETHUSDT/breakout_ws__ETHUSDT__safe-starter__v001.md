# breakout_ws__ETHUSDT: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** ETHUSDT (crypto, 1d)
**Found at:** iteration 615 of optimization.log (2026-11-23T22:07:31Z); written at the checkpoint in iteration 1583; backtest.py version `330d161090`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 3/3 one-step neighbours profitable in-sample (worst neighbour net 18,204.26)

## Parameters

| parameter | value |
|---|---|
| entry_n | 59 |
| exit_n | 3 |

```json
{
  "entry_n": 59,
  "exit_n": 3
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 23,514.75 | 2,789.43 |
| return % | 235.15 | 27.89 |
| return %/year | 22.4 | 8.9 |
| gross profit | 46,101.64 | 9,023.68 |
| gross loss | 22,586.89 | 6,234.25 |
| trades | 29 | 13 |
| win rate % | 44.8 | 53.9 |
| avg win | 3,546.28 | 1,289.10 |
| avg loss | -1,411.68 | -1,039.04 |
| avg result / trade | 810.85 | 214.57 |
| largest single loss | -4,077.07 | -2,141.62 |
| largest loss % of equity | -20.10 | -13.45 |
| max drawdown | -14,379.50 | -4,783.95 |
| max drawdown % | -35.11 | -27.22 |
| profit factor | 2.04 | 1.45 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 10.9 | 14.5 |
| time in market % | 16.4 | 18.0 |
| buy & hold return % | 211.30 | -24.43 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.40 |
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
