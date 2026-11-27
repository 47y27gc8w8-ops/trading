# golden_cross_ws__XLY: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** XLY (etf, 1d)
**Found at:** iteration 360 of optimization.log (2026-11-23T22:09:58Z); written at the checkpoint in iteration 879; backtest.py version `30de6bbbac`
**Replaces:** golden_cross_ws__XLY__safe-starter__v001.md
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 1,436.53)

## Parameters

| parameter | value |
|---|---|
| fast | 100 |
| slow | 220 |
| trailing_stop_pct | 8 |

```json
{
  "fast": 100,
  "slow": 220,
  "trailing_stop_pct": 8
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,731.52 | 2,504.82 |
| return % | 47.32 | 25.05 |
| return %/year | 2.5 | 2.1 |
| gross profit | 6,373.94 | 3,505.26 |
| gross loss | 1,642.42 | 1,000.45 |
| trades | 11 | 6 |
| win rate % | 63.6 | 33.3 |
| avg win | 910.56 | 1,752.63 |
| avg loss | -410.61 | -250.11 |
| avg result / trade | 430.14 | 417.47 |
| largest single loss | -507.97 | -523.16 |
| largest loss % of equity | -4.50 | -3.92 |
| max drawdown | -2,103.28 | -2,020.16 |
| max drawdown % | -17.15 | -14.00 |
| profit factor | 3.88 | 3.50 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 7.1 | 3.6 |
| time in market % | 22.3 | 22.1 |
| buy & hold return % | 268.77 | 228.26 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.84 |
| period | 2000-03-02 → 2015-12-31 | 2016-01-04 → 2026-11-20 |

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
