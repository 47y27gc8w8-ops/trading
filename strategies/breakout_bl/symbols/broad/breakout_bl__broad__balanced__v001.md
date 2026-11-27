# breakout_bl__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, QNTUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT, RAYUSDT (crypto, 1d)
**Found at:** iteration 1013 of optimization.log (2026-11-24T23:07:53Z); written at the checkpoint in iteration 1585; backtest.py version `f778b38de9`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/4 one-step neighbours profitable in-sample (worst neighbour net 89,094.18)

## Parameters

| parameter | value |
|---|---|
| entry_n | 27 |
| exit_n | 8 |

```json
{
  "entry_n": 27,
  "exit_n": 8
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 91,362.70 | 11,832.48 |
| return % | 913.63 | 118.32 |
| return %/year | 47.1 | 31.0 |
| gross profit | 131,950.10 | 25,470.85 |
| gross loss | 40,587.40 | 13,638.37 |
| trades | 543 | 420 |
| win rate % | 45.1 | 35.5 |
| avg win | 538.57 | 170.95 |
| avg loss | -136.20 | -50.33 |
| avg result / trade | 168.26 | 28.17 |
| largest single loss | -2,156.24 | -472.54 |
| largest loss % of equity | -20.05 | -10.89 |
| max drawdown | -25,091.61 | -6,991.64 |
| max drawdown % | -34.16 | -34.30 |
| profit factor | 3.25 | 1.87 |
| unusually bad trades | 34 | 30 |
| … threshold (% of equity) | 21.3 | 20.6 |
| time in market % | 19.7 | 25.6 |
| buy & hold return % | 534.56 | 68.80 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.66 |
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
