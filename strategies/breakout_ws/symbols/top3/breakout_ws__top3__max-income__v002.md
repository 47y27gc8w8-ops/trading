# breakout_ws__top3: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** ETHUSDT, ETCUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 360 of optimization.log (2026-11-23T22:10:03Z); written at the checkpoint in iteration 1378; backtest.py version `5f036785d9`
**Replaces:** breakout_ws__top3__max-income__v001.md
**Robustness:** 4/4 one-step neighbours profitable in-sample (worst neighbour net 91,656.82)

## Parameters

| parameter | value |
|---|---|
| entry_n | 38 |
| exit_n | 8 |

```json
{
  "entry_n": 38,
  "exit_n": 8
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 136,142.03 | 5,347.43 |
| return % | 1,361.42 | 53.47 |
| return %/year | 56.4 | 16.0 |
| gross profit | 189,100.03 | 11,908.22 |
| gross loss | 52,958.00 | 6,560.79 |
| trades | 59 | 28 |
| win rate % | 52.5 | 42.9 |
| avg win | 6,100.00 | 992.35 |
| avg loss | -1,891.36 | -410.05 |
| avg result / trade | 2,307.49 | 190.98 |
| largest single loss | -19,210.69 | -862.94 |
| largest loss % of equity | -23.53 | -12.92 |
| max drawdown | -66,067.37 | -8,290.14 |
| max drawdown % | -45.44 | -38.16 |
| profit factor | 3.57 | 1.81 |
| unusually bad trades | 5 | 0 |
| … threshold (% of equity) | 18.1 | 19.3 |
| time in market % | 26.9 | 19.1 |
| buy & hold return % | 265.38 | -61.67 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |
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
