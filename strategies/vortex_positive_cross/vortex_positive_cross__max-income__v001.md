# vortex_positive_cross: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** IWM (etf, 1d)
**Found at:** iteration 811 of optimization.log (2026-11-25T22:44:47Z); written at the checkpoint in iteration 35545; backtest.py version `0b2fd9cffe`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 6,495.87)

## Parameters

| parameter | value |
|---|---|
| max_candles | 120 |
| n | 20 |
| stop_atr | 2.0 |
| take_profit_atr | 5.0 |

```json
{
  "max_candles": 120,
  "n": 20,
  "stop_atr": 2.0,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 11,810.94 | 4,677.00 |
| return % | 118.11 | 46.77 |
| return %/year | 5.4 | 3.6 |
| gross profit | 25,708.99 | 13,295.51 |
| gross loss | 13,898.05 | 8,618.52 |
| trades | 97 | 84 |
| win rate % | 49.5 | 45.2 |
| avg win | 535.60 | 349.88 |
| avg loss | -283.63 | -187.36 |
| avg result / trade | 121.76 | 55.68 |
| largest single loss | -996.45 | -677.28 |
| largest loss % of equity | -5.73 | -5.30 |
| max drawdown | -1,864.81 | -2,455.28 |
| max drawdown % | -12.58 | -19.04 |
| profit factor | 1.85 | 1.54 |
| unusually bad trades | 4 | 10 |
| … threshold (% of equity) | 3.5 | 2.7 |
| time in market % | 30.6 | 30.9 |
| buy & hold return % | 204.74 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.66 |
| period | 2001-03-14 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# vortex_positive_cross: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
VIplus(n) crosses above VIminus(n) AND C > SMA(100).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: VIplus(n) < VIminus(n). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 14 | 10 | 30 | 1 | 2 |  |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 96 | 48 | 192 | 12 | 4 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol IWM (spec: IWM; ETF).
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
