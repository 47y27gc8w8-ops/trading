# three_down_closes: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 381 of optimization.log (2026-11-25T07:19:39Z); written at the checkpoint in iteration 6428; backtest.py version `1d9e1ab953`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/7 one-step neighbours profitable in-sample (worst neighbour net -461.11)

## Parameters

| parameter | value |
|---|---|
| max_candles | 8 |
| n | 3 |
| stop_atr | 4.0 |
| take_profit_atr | 3.5 |

```json
{
  "max_candles": 8,
  "n": 3,
  "stop_atr": 4.0,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,304.63 | 788.48 |
| return % | 43.05 | 7.88 |
| return %/year | 2.3 | 0.7 |
| gross profit | 9,442.69 | 6,839.11 |
| gross loss | 5,138.07 | 6,050.63 |
| trades | 119 | 104 |
| win rate % | 69.8 | 67.3 |
| avg win | 113.77 | 97.70 |
| avg loss | -142.72 | -177.96 |
| avg result / trade | 36.17 | 7.58 |
| largest single loss | -712.74 | -725.43 |
| largest loss % of equity | -5.25 | -6.30 |
| max drawdown | -1,007.39 | -1,817.79 |
| max drawdown % | -8.03 | -16.57 |
| profit factor | 1.84 | 1.13 |
| unusually bad trades | 6 | 11 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 9.7 | 11.4 |
| buy & hold return % | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.31 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# three_down_closes: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
The last n close-to-close returns are each negative AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: C > H[1]. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 3 | 2 | 5 | 1 | 1 | 10 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol SPY (spec: SPY; ETF).
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
