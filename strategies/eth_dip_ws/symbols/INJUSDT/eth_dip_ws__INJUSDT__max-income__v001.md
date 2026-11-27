# eth_dip_ws__INJUSDT: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** INJUSDT (crypto, 4h)
**Found at:** iteration 55 of optimization.log (2026-11-23T22:08:35Z); written at the checkpoint in iteration 255; backtest.py version `291e45ac04`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 2,601.70)

## Parameters

| parameter | value |
|---|---|
| entry | 25 |
| exit | 60 |
| rsi_n | 16 |
| stop_loss_pct | 4 |

```json
{
  "entry": 25,
  "exit": 60,
  "rsi_n": 16,
  "stop_loss_pct": 4
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.05% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 10,052.81 | 4,280.34 |
| return % | 100.53 | 42.80 |
| return %/year | 25.1 | 13.1 |
| gross profit | 23,028.50 | 19,308.34 |
| gross loss | 12,975.69 | 15,028.00 |
| trades | 25 | 35 |
| win rate % | 24.0 | 25.7 |
| avg win | 3,838.08 | 2,145.37 |
| avg loss | -682.93 | -578.00 |
| avg result / trade | 402.11 | 122.30 |
| largest single loss | -887.82 | -794.97 |
| largest loss % of equity | -4.24 | -4.24 |
| max drawdown | -7,750.77 | -7,469.65 |
| max drawdown % | -39.71 | -35.44 |
| profit factor | 1.77 | 1.28 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 8.5 | 8.5 |
| time in market % | 6.8 | 8.8 |
| buy & hold return % | 2,283.51 | -82.56 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |
| period | 2020-11-23 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

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
