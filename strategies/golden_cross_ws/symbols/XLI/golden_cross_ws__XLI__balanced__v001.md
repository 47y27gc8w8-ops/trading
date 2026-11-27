# golden_cross_ws__XLI: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** XLI (etf, 1d)
**Found at:** iteration 98 of optimization.log (2026-11-23T22:10:24Z); written at the checkpoint in iteration 190; backtest.py version `0a1eb1d80a`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/5 one-step neighbours profitable in-sample (worst neighbour net 14,476.24)
**Range warning:** fast is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 10 |
| slow | 250 |
| trailing_stop_pct | 15 |

```json
{
  "fast": 10,
  "slow": 250,
  "trailing_stop_pct": 15
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 19,077.82 | 15,614.15 |
| return % | 190.78 | 156.14 |
| return %/year | 7.0 | 9.0 |
| gross profit | 22,366.44 | 17,391.65 |
| gross loss | 3,288.62 | 1,777.50 |
| trades | 15 | 9 |
| win rate % | 53.3 | 55.6 |
| avg win | 2,795.81 | 3,478.33 |
| avg loss | -469.80 | -444.37 |
| avg result / trade | 1,271.85 | 1,734.91 |
| largest single loss | -878.53 | -733.34 |
| largest loss % of equity | -2.93 | -4.06 |
| max drawdown | -4,394.90 | -3,468.46 |
| max drawdown % | -23.37 | -16.42 |
| profit factor | 6.80 | 9.78 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 5.2 | 5.2 |
| time in market % | 69.0 | 82.4 |
| buy & hold return % | 174.01 | 261.19 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.29 |
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
