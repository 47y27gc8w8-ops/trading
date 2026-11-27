# eth_dip_ws: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** ETHUSDT (crypto, 4h)
**Found at:** iteration 276 of optimization.log (2026-11-23T22:06:35Z); written at the checkpoint in iteration 277; backtest.py version `d7da2db029`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/6 one-step neighbours profitable in-sample (worst neighbour net -7,101.11)

## Parameters

| parameter | value |
|---|---|
| entry | 32 |
| exit | 80 |
| rsi_n | 30 |
| stop_loss_pct | 13 |

```json
{
  "entry": 32,
  "exit": 80,
  "rsi_n": 30,
  "stop_loss_pct": 13
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.05% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,123.90 | 1,072.11 |
| return % | 21.24 | 10.72 |
| return %/year | 3.5 | 3.6 |
| gross profit | 17,121.93 | 14,102.79 |
| gross loss | 14,998.04 | 13,030.68 |
| trades | 29 | 12 |
| win rate % | 17.2 | 33.3 |
| avg win | 3,424.39 | 3,525.70 |
| avg loss | -624.92 | -1,628.84 |
| avg result / trade | 73.24 | 89.34 |
| largest single loss | -1,321.72 | -1,912.96 |
| largest loss % of equity | -13.22 | -13.22 |
| max drawdown | -27,214.18 | -19,677.92 |
| max drawdown % | -90.88 | -66.93 |
| profit factor | 1.14 | 1.08 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 26.4 | 26.4 |
| time in market % | 82.2 | 82.1 |
| buy & hold return % | 294.92 | -24.43 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.02 |
| period | 2018-06-01 → 2023-12-31 | 2024-01-01 → 2026-11-22 |

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
