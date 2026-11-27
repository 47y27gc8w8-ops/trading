# golden_cross_ws__QQQ: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 462 of optimization.log (2026-11-23T22:09:09Z); written at the checkpoint in iteration 1739; backtest.py version `7fe33695ff`
**Replaces:** golden_cross_ws__QQQ__safe-starter__v001.md
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 2,346.58)

## Parameters

| parameter | value |
|---|---|
| fast | 55 |
| slow | 230 |
| trailing_stop_pct | 6 |

```json
{
  "fast": 55,
  "slow": 230,
  "trailing_stop_pct": 6
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,115.52 | 2,423.51 |
| return % | 41.16 | 24.24 |
| return %/year | 2.2 | 2.0 |
| gross profit | 4,987.32 | 2,849.12 |
| gross loss | 871.79 | 425.61 |
| trades | 9 | 4 |
| win rate % | 44.4 | 50.0 |
| avg win | 1,246.83 | 1,424.56 |
| avg loss | -174.36 | -212.80 |
| avg result / trade | 457.28 | 605.88 |
| largest single loss | -364.79 | -228.05 |
| largest loss % of equity | -3.39 | -2.33 |
| max drawdown | -1,277.22 | -1,004.66 |
| max drawdown % | -10.61 | -9.62 |
| profit factor | 5.72 | 6.69 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 2.8 | 4.3 |
| time in market % | 15.4 | 9.1 |
| buy & hold return % | 36.87 | 499.73 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.91 |
| period | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

## Rules (strategy.md at the time of saving)

# Golden cross (SPY)

Source: original.md (user's description, 2026-11-23). This file is the testable version.

## Idea
Be long the S&P 500 while its medium-term trend (50-day average) is above its long-term trend
(200-day average), and be in cash otherwise, to sit out the big bear markets. Optionally protect
open gains with a trailing stop.

## Market
- Symbols: SPY (Yahoo daily, dividend/split adjusted)
- Timeframe: 1d bars
- Direction: long only, one position at a time

## Buy trigger
At the close of day t, using only day t and earlier:
- `SMA(close, fast)[t] > SMA(close, slow)[t]` AND `SMA(close, fast)[t-1] <= SMA(close, slow)[t-1]`
  (the fast average crosses above the slow one: "the 50 day goes above the 200 day")
Order: buy at the open of day t+1.

## Sell trigger
Close the position at the first of:
- death cross: `SMA(close, fast) < SMA(close, slow)` at a close → sell at the next open
  ("get out when it crosses back")
- trailing stop (only if `trailing_stop_pct` > 0): price falls `trailing_stop_pct` % below the
  highest high since entry, checked intrabar (gaps fill at the open)

After a trailing-stop exit the strategy waits for the next golden cross (the buy trigger is the
cross itself, as written). See open questions.

## Parameters
| name | meaning | description's value | range | step |
|---|---|---|---|---|
| fast | fast SMA length (days) | 50 | 10–150 | 5 |
| slow | slow SMA length (days) | 200 | 100–300 | 10 |
| trailing_stop_pct | trailing stop % below highest high since entry, 0 = off | not given ("maybe… not sure how much") → 0 | 0–25 | 1 |

Constraint: `fast < slow`. Grid: 29 × 21 × 26 ≈ 15,800 sets (minus invalid ones).

## Setup
- Data: SPY daily 1993-01-29 → 2026-11-20 (end frozen at setup: last complete bar)
- Trading from 1995-01-01 (earlier bars only warm up the SMAs, up to 300 days)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-20
- Capital 10,000 USD, 100% of equity per trade, fractional units allowed
- Fees 0.05% per side, slippage 0.03% per fill (US ETF defaults)
- Optimizer settings changed for this strategy: `min_trades_is` 5 (default 20), `min_trades_oos` 2
  (default 5), `balanced_min_win_rate` 40 (default 45), because a 50/200 golden cross on SPY trades
  only every ~2 years (9 in-sample trades in 21 years with the defaults), so the defaults would
  reject the strategy as written.

## Assumptions
- "S&P ETF" = SPY (the largest, oldest S&P 500 ETF, data since 1993; IVV/VOO are equivalent but shorter).
- "50 day / 200 day" = simple moving averages of the daily close (the standard golden-cross definition).
- "crosses back" = the 50-day SMA closes below the 200-day SMA.
- Trailing stop measured from the highest high since entry; 0 (off) allowed because the user wasn't sure they want one.
- Signals on the close, fills at the next open (no same-bar execution).
- Out-of-sample split 2016-01-01 (repo precedent for ETF strategies).

## Open questions (user unavailable; defaults used)
1. After a trailing-stop exit, should it buy again while the 50-day is still above the 200-day
   (e.g. once price makes a new high), or only at the next fresh golden cross? Default: only at
   the next golden cross (literal reading). This can leave the strategy in cash for years after a stop.
2. SMA or EMA? Default: SMA.

---
Backtest results don't guarantee future performance.
