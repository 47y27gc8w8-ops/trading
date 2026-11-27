# return_percentile_shock: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 679 of optimization.log (2026-11-25T10:55:34Z); written at the checkpoint in iteration 957; backtest.py version `d5c1e2fac8`
**Replaces:** return_percentile_shock__max-income__v001.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 2,355.97)

## Parameters

| parameter | value |
|---|---|
| max_candles | 8 |
| n | 10 |
| rank | 8 |
| stop_atr | 5.0 |
| take_profit_atr | 2.0 |

```json
{
  "max_candles": 8,
  "n": 10,
  "rank": 8,
  "stop_atr": 5.0,
  "take_profit_atr": 2.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,216.66 | 4,369.63 |
| return % | 32.17 | 43.70 |
| return %/year | 1.8 | 3.4 |
| gross profit | 12,516.65 | 11,481.59 |
| gross loss | 9,300.00 | 7,111.95 |
| trades | 193 | 159 |
| win rate % | 64.8 | 66.7 |
| avg win | 100.13 | 108.32 |
| avg loss | -136.76 | -134.19 |
| avg result / trade | 16.67 | 27.48 |
| largest single loss | -803.25 | -574.21 |
| largest loss % of equity | -6.53 | -4.22 |
| max drawdown | -1,409.83 | -1,520.59 |
| max drawdown % | -11.16 | -12.15 |
| profit factor | 1.35 | 1.61 |
| unusually bad trades | 13 | 10 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 15.9 | 16.9 |
| buy & hold return % | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.93 |
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
