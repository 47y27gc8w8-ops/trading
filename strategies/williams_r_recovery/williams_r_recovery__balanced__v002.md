# williams_r_recovery: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 596 of optimization.log (2026-11-25T05:42:45Z); written at the checkpoint in iteration 1039; backtest.py version `14edac6745`
**Replaces:** williams_r_recovery__balanced__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 5,380.53)

## Parameters

| parameter | value |
|---|---|
| level | -94 |
| max_candles | 24 |
| n | 26 |
| stop_atr | 2.0 |
| take_profit_atr | 6.0 |

```json
{
  "level": -94,
  "max_candles": 24,
  "n": 26,
  "stop_atr": 2.0,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 7,623.20 | 1,527.74 |
| return % | 76.23 | 15.28 |
| return %/year | 3.7 | 1.3 |
| gross profit | 11,863.20 | 7,246.54 |
| gross loss | 4,240.00 | 5,718.80 |
| trades | 33 | 27 |
| win rate % | 69.7 | 55.6 |
| avg win | 515.79 | 483.10 |
| avg loss | -424.00 | -476.57 |
| avg result / trade | 231.01 | 56.58 |
| largest single loss | -650.07 | -860.90 |
| largest loss % of equity | -4.80 | -8.80 |
| max drawdown | -939.33 | -2,824.82 |
| max drawdown % | -6.99 | -24.49 |
| profit factor | 2.80 | 1.27 |
| unusually bad trades | 0 | 2 |
| … threshold (% of equity) | 6.1 | 7.1 |
| time in market % | 8.7 | 7.7 |
| buy & hold return % | 36.87 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.35 |
| period | 2000-05-16 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# williams_r_recovery: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
WilliamsR(n) crosses above level AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: WilliamsR(n) > -20. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 14 | 7 | 28 | 1 | 2 |  |
| level | -80.0 | -90.0 | -70.0 | 1.0 | -99.0 | -21.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol QQQ (spec: QQQ; ETF).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 300 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `etf`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard; its "size for ~10% DD" column gives a risk-scaled size).
- Costs: library convention fee 0.05% + slippage 0.03% per fill (more conservative than the spec's 1 bp + 2 bp + 2 bp).
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder RSI/ATR with SMA seed, EMA with SMA seed, population std, PR excluding t).
- Adjusted closes are used for signals and fills (the project data has no separate raw execution series).

---
Backtest results don't guarantee future performance.
