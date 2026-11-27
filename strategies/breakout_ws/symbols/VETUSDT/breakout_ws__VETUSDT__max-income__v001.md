# breakout_ws__VETUSDT: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** VETUSDT (crypto, 1d)
**Found at:** iteration 552 of optimization.log (2026-11-23T22:08:48Z); written at the checkpoint in iteration 1580; backtest.py version `850733bcef`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/4 one-step neighbours profitable in-sample (worst neighbour net 252,177.65)

## Parameters

| parameter | value |
|---|---|
| entry_n | 30 |
| exit_n | 9 |

```json
{
  "entry_n": 30,
  "exit_n": 9
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 402,189.90 | 10,307.58 |
| return % | 4,021.90 | 103.08 |
| return %/year | 107.2 | 27.8 |
| gross profit | 617,192.32 | 18,659.67 |
| gross loss | 215,002.43 | 8,352.09 |
| trades | 20 | 8 |
| win rate % | 55.0 | 37.5 |
| avg win | 56,108.39 | 6,219.89 |
| avg loss | -23,889.16 | -1,670.42 |
| avg result / trade | 20,109.49 | 1,288.45 |
| largest single loss | -89,631.88 | -2,136.49 |
| largest loss % of equity | -23.53 | -12.92 |
| max drawdown | -253,341.32 | -15,351.54 |
| max drawdown % | -50.33 | -54.03 |
| profit factor | 2.87 | 2.23 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 18.4 | 23.2 |
| time in market % | 36.2 | 16.6 |
| buy & hold return % | 484.67 | -86.53 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |
| period | 2018-11-22 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

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
