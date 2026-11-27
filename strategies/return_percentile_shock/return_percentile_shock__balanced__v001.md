# return_percentile_shock: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 27 of optimization.log (2026-11-25T10:55:22Z); written at the checkpoint in iteration 261; backtest.py version `d5c1e2fac8`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 24.14)
**Range warning:** rank is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 12 |
| n | 90 |
| rank | 1 |
| stop_atr | 3.5 |
| take_profit_atr | 4.0 |

```json
{
  "max_candles": 12,
  "n": 90,
  "rank": 1,
  "stop_atr": 3.5,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 835.79 | 659.56 |
| return % | 8.36 | 6.60 |
| return %/year | 0.5 | 0.6 |
| gross profit | 2,441.47 | 2,165.82 |
| gross loss | 1,605.68 | 1,506.26 |
| trades | 25 | 21 |
| win rate % | 60.0 | 71.4 |
| avg win | 162.76 | 144.39 |
| avg loss | -160.57 | -251.04 |
| avg result / trade | 33.43 | 31.41 |
| largest single loss | -495.31 | -465.65 |
| largest loss % of equity | -4.33 | -4.23 |
| max drawdown | -591.25 | -1,049.50 |
| max drawdown % | -5.17 | -9.52 |
| profit factor | 1.52 | 1.44 |
| unusually bad trades | 3 | 0 |
| … threshold (% of equity) | 2.0 | 4.6 |
| time in market % | 2.3 | 2.5 |
| buy & hold return % | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.18 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# return_percentile_shock: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
PR(ROC(1), n) < rank AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: ROC(3) > 1 (percentage points) OR C > SMA(5). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 100 | 50 | 250 | 10 | 10 |  |
| rank | 5.0 | 1.0 | 10.0 | 1.0 | 0.5 | 50.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol SPY (spec: SPY; ETF).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 400 bars per symbol.
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
