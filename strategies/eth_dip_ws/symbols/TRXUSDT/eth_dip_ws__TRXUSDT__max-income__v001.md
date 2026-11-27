# eth_dip_ws__TRXUSDT: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** TRXUSDT (crypto, 4h)
**Found at:** iteration 171 of optimization.log (2026-11-23T22:09:41Z); written at the checkpoint in iteration 303; backtest.py version `4087f933dc`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 17,438.19)
**Range warning:** rsi_n is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| entry | 34 |
| exit | 75 |
| rsi_n | 30 |
| stop_loss_pct | 14 |

```json
{
  "entry": 34,
  "exit": 75,
  "rsi_n": 30,
  "stop_loss_pct": 14
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.05% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 159,933.20 | 6,166.85 |
| return % | 1,599.33 | 61.67 |
| return %/year | 68.0 | 18.1 |
| gross profit | 261,642.39 | 9,825.84 |
| gross loss | 101,709.18 | 3,658.99 |
| trades | 28 | 7 |
| win rate % | 35.7 | 57.1 |
| avg win | 26,164.24 | 2,456.46 |
| avg loss | -5,650.51 | -1,219.66 |
| avg result / trade | 5,711.90 | 880.98 |
| largest single loss | -15,792.08 | -2,130.60 |
| largest loss % of equity | -14.21 | -14.21 |
| max drawdown | -73,731.00 | -4,366.91 |
| max drawdown % | -79.04 | -25.97 |
| profit factor | 2.57 | 2.69 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 28.4 | 28.4 |
| time in market % | 70.7 | 69.3 |
| buy & hold return % | 222.95 | 184.00 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |
| period | 2018-07-15 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

## Rules (strategy.md at the time of saving)

# ETH dip buying (RSI oversold on 4h)

Source: original.md (user's description, 2026-11-23). This file is the testable version.

## Idea
ETH overreacts on sell-offs on the 4-hour chart. Buy when RSI says it is oversold, sell when
RSI has recovered, and cap each trade's loss with a fixed stop.

## Market
- Symbols: ETHUSDT (Binance spot)
- Timeframe: 4h bars (UTC, 00/04/08/12/16/20), built from 1m bars
- Direction: long only, one position at a time

## Buy trigger
At the close of 4h bar t (using only bar t and earlier):
- `RSI(rsi_n) < entry` (Wilder RSI on closes)
Order: buy at the open of bar t+1. While a position is open, further buy signals are ignored.

## Sell trigger
Close the position at the first of:
- `RSI(rsi_n) > exit` at a 4h close → sell at the next open
- stop loss: price ≤ entry fill × (1 − stop_loss_pct/100), checked intrabar on the 4h low;
  a gap through the level fills at the open

No other exits (no target, trailing stop or time exit: the description has none).

## Parameters
| name | meaning | description's value | range | step |
|---|---|---|---|---|
| rsi_n | RSI length (bars) | 14 ("the usual setting") | 4–30 (hard min 2) | 2 |
| entry | buy below this RSI | 25 | 10–40 (hard 2–60) | 2 |
| exit | sell above this RSI | 55 | 35–80 (hard 20–95) | 5 |
| stop_loss_pct | stop below entry fill, % | 6 | 2–15 (hard min 1, 0 = off not allowed) | 1 |

Constraints: `exit > entry`, `stop_loss_pct > 0`. Grid ≈ 14 × 16 × 10 × 14 ≈ 31,000 sets.

## Setup
- Data: ETHUSDT 1m from 2018-03-05 → frozen end 2026-11-22 (last complete day)
- First tradable bar 2018-06-01 (≥ 200 4h bars of warm-up before it)
- In-sample (tuning): 2018-06-01 → 2023-12-31; out-of-sample (validation only): 2024-01-01 → 2026-11-22
- Capital 10,000 USD, 100% of equity per trade, fractional units allowed
- Fees 0.10% per side, slippage 0.05% per fill

## Assumptions
- RSI = Wilder's RSI (project helper `rsi`), the standard definition.
- "-6%" = stop 6% below the entry fill price, checked intrabar (not on the close).
- "back above 55" = the first 4h close with RSI > exit level; the sell fills at the next open.
- The stop is always on: the user wants it to protect the account, so 0 (= no stop) is not in the range.
- Capital, sizing, fees, slippage and IS/OOS split: skill defaults / repo precedent for crypto.
- Base symbol ETHUSDT as named; screening checks other Binance coins.

## Open questions
- None blocking. The user may want to confirm: stop intrabar vs. on a 4h close; full equity per trade.

---
Backtest results don't guarantee future performance.
