# triple_ema_alignment: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** QQQ (etf, 1d)
**Found at:** iteration 227 of optimization.log (2026-11-25T07:09:23Z); written at the checkpoint in iteration 333; backtest.py version `861ff684f9`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 10/11 one-step neighbours profitable in-sample (worst neighbour net -195.20)
**Range warning:** fast is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 3 |
| max_candles | 120 |
| mid | 10 |
| slow | 15 |
| stop_atr | 2.75 |
| take_profit_atr | 4.5 |

```json
{
  "fast": 3,
  "max_candles": 120,
  "mid": 10,
  "slow": 15,
  "stop_atr": 2.75,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,015.09 | 3,492.18 |
| return % | 30.15 | 34.92 |
| return %/year | 1.7 | 2.8 |
| gross profit | 18,719.53 | 12,479.19 |
| gross loss | 15,704.45 | 8,987.01 |
| trades | 106 | 65 |
| win rate % | 32.1 | 41.5 |
| avg win | 550.57 | 462.19 |
| avg loss | -218.12 | -236.50 |
| avg result / trade | 28.44 | 53.73 |
| largest single loss | -613.18 | -600.81 |
| largest loss % of equity | -5.66 | -4.65 |
| max drawdown | -2,944.08 | -2,918.86 |
| max drawdown % | -19.25 | -18.10 |
| profit factor | 1.19 | 1.39 |
| unusually bad trades | 9 | 5 |
| … threshold (% of equity) | 3.2 | 3.4 |
| time in market % | 22.9 | 21.6 |
| buy & hold return % | 28.06 | 541.70 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.68 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# triple_ema_alignment: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
EMA(fast) crosses above EMA(mid) AND EMA(mid) > EMA(slow).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: EMA(fast) < EMA(mid). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| fast | 5 | 3 | 7 | 1 | 2 |  |
| mid | 8 | 8 | 12 | 1 | 3 |  |
| slow | 13 | 13 | 30 | 1 | 4 |  |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 96 | 48 | 192 | 12 | 4 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol QQQ (spec: QQQ, liquid large-cap stocks).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 200 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `yahoo`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard; its "size for ~10% DD" column gives a risk-scaled size).
- Costs: library convention fee 0.05% + slippage 0.03% per fill (more conservative than the spec's 1 bp + 2 bp + 2 bp).
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder RSI/ATR with SMA seed, EMA with SMA seed, population std, PR excluding t).
- Adjusted closes are used for signals and fills (the project data has no separate raw execution series).
- Spec ranges give mid min = 8 and slow min = 13 (= start values); the order constraint fast < mid < slow is enforced in valid().

---
Backtest results don't guarantee future performance.
