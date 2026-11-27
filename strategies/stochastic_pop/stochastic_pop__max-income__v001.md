# stochastic_pop: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 52 of optimization.log (2026-11-25T07:31:10Z); written at the checkpoint in iteration 35537; backtest.py version `c20fb5f59d`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 245.26)

## Parameters

| parameter | value |
|---|---|
| level | 78 |
| max_candles | 96 |
| stop_atr | 2.5 |
| take_profit_atr | 3.0 |

```json
{
  "level": 78,
  "max_candles": 96,
  "stop_atr": 2.5,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,143.00 | 3,701.11 |
| return % | 31.43 | 37.01 |
| return %/year | 1.7 | 2.9 |
| gross profit | 10,823.22 | 8,055.15 |
| gross loss | 7,680.22 | 4,354.04 |
| trades | 47 | 43 |
| win rate % | 46.8 | 48.8 |
| avg win | 491.96 | 383.58 |
| avg loss | -307.21 | -197.91 |
| avg result / trade | 66.87 | 86.07 |
| largest single loss | -829.42 | -458.77 |
| largest loss % of equity | -8.29 | -4.58 |
| max drawdown | -1,736.82 | -1,320.57 |
| max drawdown % | -13.01 | -12.49 |
| profit factor | 1.41 | 1.85 |
| unusually bad trades | 2 | 1 |
| … threshold (% of equity) | 4.1 | 3.5 |
| time in market % | 12.4 | 14.6 |
| buy & hold return % | 28.06 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.70 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# stochastic_pop: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
SlowK(14,3) crosses above level AND ADX(14) > 20 AND C > SMA(100).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: SlowK(14,3) < 50. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| level | 80.0 | 70.0 | 90.0 | 1.0 | 51.0 | 99.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 96 | 48 | 192 | 12 | 4 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol QQQ (spec: QQQ; ETF).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 200 bars per symbol.
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
