# bullish_engulfing_trend: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 52019 of optimization.log (2026-11-26T02:28:28Z); written at the checkpoint in iteration 52474; backtest.py version `d2ea6db0b5`
**Replaces:** bullish_engulfing_trend__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 3,818.03)

## Parameters

| parameter | value |
|---|---|
| max_candles | 52 |
| n | 110 |
| stop_atr | 0.5 |
| take_profit_atr | 6.5 |

```json
{
  "max_candles": 52,
  "n": 110,
  "stop_atr": 0.5,
  "take_profit_atr": 6.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 10,411.53 | 3,651.77 |
| return % | 104.12 | 36.52 |
| return %/year | 4.6 | 2.9 |
| gross profit | 20,075.79 | 9,948.73 |
| gross loss | 9,664.27 | 6,296.96 |
| trades | 77 | 63 |
| win rate % | 24.7 | 30.2 |
| avg win | 1,056.62 | 523.62 |
| avg loss | -166.63 | -143.11 |
| avg result / trade | 135.21 | 57.96 |
| largest single loss | -353.02 | -578.75 |
| largest loss % of equity | -3.53 | -4.19 |
| max drawdown | -4,203.17 | -1,824.04 |
| max drawdown % | -40.16 | -11.79 |
| profit factor | 2.08 | 1.58 |
| unusually bad trades | 2 | 1 |
| … threshold (% of equity) | 3.2 | 2.1 |
| time in market % | 8.2 | 10.3 |
| buy & hold return % | 2,918.19 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.64 |
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
