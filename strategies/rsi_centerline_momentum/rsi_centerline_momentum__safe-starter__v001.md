# rsi_centerline_momentum: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** NVDA (etf, 1d)
**Found at:** iteration 262 of optimization.log (2026-11-25T09:04:58Z); written at the checkpoint in iteration 465; backtest.py version `7e0177b6fd`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/9 one-step neighbours profitable in-sample (worst neighbour net -304.50)

## Parameters

| parameter | value |
|---|---|
| level | 63 |
| max_candles | 192 |
| n | 25 |
| stop_atr | 1.75 |
| take_profit_atr | 4.0 |

```json
{
  "level": 63,
  "max_candles": 192,
  "n": 25,
  "stop_atr": 1.75,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 21,240.18 | 52,759.13 |
| return % | 212.40 | 527.59 |
| return %/year | 7.5 | 18.4 |
| gross profit | 48,265.92 | 101,337.23 |
| gross loss | 27,025.74 | 48,578.10 |
| trades | 40 | 44 |
| win rate % | 47.5 | 56.8 |
| avg win | 2,540.31 | 4,053.49 |
| avg loss | -1,286.94 | -2,556.74 |
| avg result / trade | 531.00 | 1,199.07 |
| largest single loss | -2,880.36 | -5,842.50 |
| largest loss % of equity | -9.03 | -7.07 |
| max drawdown | -6,568.86 | -20,405.37 |
| max drawdown % | -30.33 | -24.54 |
| profit factor | 1.79 | 2.09 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 12.2 | 11.8 |
| time in market % | 15.5 | 19.1 |
| buy & hold return % | 476.60 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.45 |
| period | 2000-03-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# rsi_centerline_momentum: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
RSI(n) crosses above level AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: RSI(n) < 45 (fixed literal; the spec's trigger text uses the same RSI). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 14 | 7 | 28 | 1 | 2 |  |
| level | 55.0 | 50.0 | 65.0 | 1.0 | 46.0 | 95.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 96 | 48 | 192 | 12 | 4 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol NVDA (spec: NVDA; stock).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 300 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `stock`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard; its "size for ~10% DD" column gives a risk-scaled size).
- Costs: library convention fee 0.05% + slippage 0.03% per fill (more conservative than the spec's 1 bp + 2 bp + 2 bp).
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder RSI/ATR with SMA seed, EMA with SMA seed, population std, PR excluding t).
- Adjusted closes are used for signals and fills (the project data has no separate raw execution series).

---
Backtest results don't guarantee future performance.
