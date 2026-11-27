# bullish_engulfing_trend: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 169 of optimization.log (2026-11-26T02:11:32Z); written at the checkpoint in iteration 51932; backtest.py version `d2ea6db0b5`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 1,588.85)

## Parameters

| parameter | value |
|---|---|
| max_candles | 28 |
| n | 110 |
| stop_atr | 1.0 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 28,
  "n": 110,
  "stop_atr": 1.0,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,983.46 | 859.30 |
| return % | 29.83 | 8.59 |
| return %/year | 1.6 | 0.8 |
| gross profit | 13,981.84 | 7,755.44 |
| gross loss | 10,998.38 | 6,896.14 |
| trades | 83 | 68 |
| win rate % | 45.8 | 47.1 |
| avg win | 367.94 | 242.36 |
| avg loss | -244.41 | -191.56 |
| avg result / trade | 35.95 | 12.64 |
| largest single loss | -738.49 | -450.72 |
| largest loss % of equity | -7.33 | -4.19 |
| max drawdown | -4,619.88 | -1,028.93 |
| max drawdown % | -38.29 | -9.96 |
| profit factor | 1.27 | 1.12 |
| unusually bad trades | 2 | 2 |
| … threshold (% of equity) | 5.1 | 3.6 |
| time in market % | 5.2 | 7.1 |
| buy & hold return % | 2,918.19 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.46 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# bullish_engulfing_trend: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
C[1] < O[1] AND C > O AND O <= C[1] AND C >= O[1] AND C > SMA(n)
(numeric bullish engulfing: a down bar followed by an up bar whose body covers it, in an uptrend).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: C < EMA(10). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 200 | 100 | 300 | 10 | 2 |  |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 48 | 24 | 96 | 4 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). EMA(10) and ATR(14) are fixed constants.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol AAPL (spec: AAPL; stock).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 300 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `stock`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard).
- Costs: library convention fee 0.05% + slippage 0.03% per fill.
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder ATR with SMA seed, EMA with SMA seed).
- Adjusted prices are used for signals and fills (no separate raw execution series).

---
Backtest results don't guarantee future performance.
