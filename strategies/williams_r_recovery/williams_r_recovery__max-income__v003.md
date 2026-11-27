# williams_r_recovery: max-income v003

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 1189 of optimization.log (2026-11-25T23:22:03Z); written at the checkpoint in iteration 1190; backtest.py version `14edac6745`
**Replaces:** williams_r_recovery__max-income__v002.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 9,133.35)

## Parameters

| parameter | value |
|---|---|
| level | -87 |
| max_candles | 16 |
| n | 9 |
| stop_atr | 4.75 |
| take_profit_atr | 5.0 |

```json
{
  "level": -87,
  "max_candles": 16,
  "n": 9,
  "stop_atr": 4.75,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 12,793.54 | 3,157.10 |
| return % | 127.94 | 31.57 |
| return %/year | 5.4 | 2.5 |
| gross profit | 21,932.74 | 13,197.19 |
| gross loss | 9,139.20 | 10,040.09 |
| trades | 94 | 69 |
| win rate % | 78.7 | 71.0 |
| avg win | 296.39 | 269.33 |
| avg loss | -456.96 | -502.00 |
| avg result / trade | 136.10 | 45.76 |
| largest single loss | -1,682.08 | -1,640.67 |
| largest loss % of equity | -9.16 | -12.96 |
| max drawdown | -2,383.24 | -2,195.94 |
| max drawdown % | -14.99 | -16.62 |
| profit factor | 2.40 | 1.31 |
| unusually bad trades | 5 | 5 |
| … threshold (% of equity) | 4.7 | 5.8 |
| time in market % | 17.2 | 18.4 |
| buy & hold return % | 36.87 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.47 |
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
