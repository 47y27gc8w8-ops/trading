# rsi_centerline_momentum: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** NVDA (etf, 1d)
**Found at:** iteration 215 of optimization.log (2026-11-25T09:04:57Z); written at the checkpoint in iteration 464; backtest.py version `7e0177b6fd`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 11,909.65)
**Range warning:** take_profit_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| level | 59 |
| max_candles | 144 |
| n | 23 |
| stop_atr | 2.5 |
| take_profit_atr | 1.5 |

```json
{
  "level": 59,
  "max_candles": 144,
  "n": 23,
  "stop_atr": 2.5,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 24,854.08 | 5,592.17 |
| return % | 248.54 | 55.92 |
| return %/year | 8.2 | 4.2 |
| gross profit | 54,416.15 | 34,132.42 |
| gross loss | 29,562.07 | 28,540.25 |
| trades | 64 | 60 |
| win rate % | 75.0 | 71.7 |
| avg win | 1,133.67 | 793.78 |
| avg loss | -1,847.63 | -1,678.84 |
| avg result / trade | 388.34 | 93.20 |
| largest single loss | -3,840.05 | -3,148.60 |
| largest loss % of equity | -13.82 | -13.58 |
| max drawdown | -7,356.96 | -11,226.78 |
| max drawdown % | -35.78 | -44.78 |
| profit factor | 1.84 | 1.20 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 19.5 | 16.6 |
| time in market % | 14.2 | 15.8 |
| buy & hold return % | 476.60 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.50 |
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
