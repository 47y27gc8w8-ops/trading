# eth_dip_ws__INJUSDT: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** INJUSDT (crypto, 4h)
**Found at:** iteration 280 of optimization.log (2026-11-23T22:08:43Z); written at the checkpoint in iteration 836; backtest.py version `291e45ac04`
**Replaces:** eth_dip_ws__INJUSDT__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,368.74)

## Parameters

| parameter | value |
|---|---|
| entry | 30 |
| exit | 40 |
| rsi_n | 24 |
| stop_loss_pct | 6 |

```json
{
  "entry": 30,
  "exit": 40,
  "rsi_n": 24,
  "stop_loss_pct": 6
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.05% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 16,406.34 | 15,716.08 |
| return % | 164.06 | 157.16 |
| return %/year | 36.8 | 38.6 |
| gross profit | 26,746.56 | 25,142.72 |
| gross loss | 10,340.22 | 9,426.64 |
| trades | 23 | 26 |
| win rate % | 52.2 | 61.5 |
| avg win | 2,228.88 | 1,571.42 |
| avg loss | -940.02 | -942.66 |
| avg result / trade | 713.32 | 604.46 |
| largest single loss | -1,478.96 | -1,488.22 |
| largest loss % of equity | -6.23 | -6.23 |
| max drawdown | -3,755.70 | -2,854.18 |
| max drawdown % | -22.82 | -22.86 |
| profit factor | 2.59 | 2.67 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 12.5 | 12.5 |
| time in market % | 2.1 | 3.0 |
| buy & hold return % | 2,283.51 | -82.56 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.05 |
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
