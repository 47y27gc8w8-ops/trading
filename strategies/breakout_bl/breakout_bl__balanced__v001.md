# breakout_bl: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SOLUSDT, VETUSDT, ADAUSDT, HBARUSDT, BTCUSDT, DOGEUSDT, BNBUSDT, AVAXUSDT, SHIBUSDT, DOTUSDT, NEARUSDT, UNIUSDT, ALGOUSDT, RAYUSDT, ETHUSDT, ETCUSDT, TRXUSDT, NEXOUSDT, LINKUSDT, XRPUSDT, STXUSDT, XLMUSDT, JSTUSDT, DASHUSDT, AAVEUSDT, QNTUSDT, FILUSDT, ZECUSDT, CAKEUSDT, BCHUSDT, INJUSDT, ATOMUSDT, LTCUSDT, APTUSDT, ICPUSDT (crypto, 1d)
**Found at:** iteration 160 of optimization.log (2026-11-24T22:58:10Z); written at the checkpoint in iteration 1594; backtest.py version `3f84a6b068`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/4 one-step neighbours profitable in-sample (worst neighbour net 33,180.13)

## Parameters

| parameter | value |
|---|---|
| entry_n | 57 |
| exit_n | 5 |

```json
{
  "entry_n": 57,
  "exit_n": 5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 42,228.38 | 6,528.96 |
| return % | 422.28 | 65.29 |
| return %/year | 31.7 | 19.0 |
| gross profit | 61,215.26 | 14,210.75 |
| gross loss | 18,986.88 | 7,681.79 |
| trades | 441 | 311 |
| win rate % | 43.3 | 40.2 |
| avg win | 320.50 | 113.69 |
| avg loss | -75.95 | -41.30 |
| avg result / trade | 95.76 | 20.99 |
| largest single loss | -1,031.84 | -287.68 |
| largest loss % of equity | -20.53 | -15.88 |
| max drawdown | -7,442.80 | -4,532.62 |
| max drawdown % | -19.44 | -25.74 |
| profit factor | 3.22 | 1.85 |
| unusually bad trades | 23 | 18 |
| … threshold (% of equity) | 20.5 | 19.8 |
| time in market % | 11.0 | 13.1 |
| buy & hold return % | 502.60 | 61.42 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.60 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

## Rules (strategy.md at the time of saving)

# Breakout (Donchian channel, long only), broad-basket variant

Source: original.md (the user's breakout description; byte copy of strategies/breakout_ws/original.md,
since the file the earlier study names, breakout.md, no longer exists). This file is the testable version.
README.md, log.md and results/ hold an earlier standalone study of the same rules (2026-11-23); this
file describes the skill-optimizer run that started 2026-11-24.

## Idea
Buy strength: when a coin closes above its recent highest high it may be starting a trend;
ride it until it closes below its recent lowest low. The user expects it to work only on
coins that trend a lot. The earlier study found that choosing coins by past results did not
pick the next period's winners, so this folder starts from a broad basket.

## Market
- Symbols: base run on the 35-coin basket in backtest.py CONFIG (every Binance USDT pair with
  ≥ 1.5 years and ≥ 8 trades of 2018–2024 history; a history filter, not a performance filter).
  Screening over the crypto universe defines the "broad" basket and tests ranking persistence.
- Timeframe: 1d bars (UTC), built from Binance 1m data
- Direction: long only, one position per coin, capital split equally between the coins

## Buy trigger
At the close of day t (only day t and earlier are used):
- `close[t] > max(high[t-entry_n] … high[t-1])` (highest high of the previous `entry_n` days, today excluded)
Order: buy at the open of day t+1 (only when flat in that coin).

## Sell trigger
- `close[t] < min(low[t-exit_n] … low[t-1])` (lowest low of the previous `exit_n` days, today excluded) → sell at the next open
No stop loss, target, trailing stop, trend filter or time exit (the description has none).

## Parameters
| name | meaning | description's value | range | step |
|---|---|---|---|---|
| entry_n | breakout channel length (days) | 20 | 5–60 (may widen to 110) | 1 |
| exit_n | exit channel length (days) | 10 | 3–30 (may widen to 110) | 1 |

Constraints: none between the two lengths. Grid: 56 × 28 = 1,568 sets.

## Setup
- Data: Binance daily bars; trading from 2018-01-01 (or a coin's 120th day) → 2026-11-22 (frozen)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, each coin's share 100% invested while in a trade, fractional units allowed
- Fees 0.10% per side, slippage 0.10% per fill

## Assumptions
- Base symbols = the earlier study's 35-coin basket: the description names no coin, and that study's
  walk-forward test showed past-result coin selection doesn't persist.
- "Previous 20 days" excludes the current day (otherwise a close can never exceed a high that includes itself).
- Highs/lows (not closes) define the channel, as written.
- The earlier study's extras (trend_sma, trailing_stop_pct) and its `exit_n ≤ 1.5 × entry_n` constraint
  are dropped: not in the description.
- Split moved from 2025-01-01 to 2024-01-01: repo precedent for crypto, ~33% OOS, comparable to breakout_ws.
- Slippage 0.10% (smaller-coin value) for every coin, since the basket includes smaller coins.
- Optimizer gates for a slow trend follower: min_trades_is 12, balanced_min_win_rate 35 (same as breakout_ws).

---
Backtest results don't guarantee future performance.
