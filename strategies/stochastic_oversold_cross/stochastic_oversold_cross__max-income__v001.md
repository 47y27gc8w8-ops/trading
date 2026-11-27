# stochastic_oversold_cross: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** AAPL (etf, 1d)
**Found at:** iteration 36825 of optimization.log (2026-11-25T07:56:15Z); written at the checkpoint in iteration 40377; backtest.py version `1fce26ee1e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 21,975.17)

## Parameters

| parameter | value |
|---|---|
| level | 26 |
| max_candles | 20 |
| stop_atr | 4.25 |
| take_profit_atr | 7.0 |

```json
{
  "level": 26,
  "max_candles": 20,
  "stop_atr": 4.25,
  "take_profit_atr": 7.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 29,080.35 | 2,985.00 |
| return % | 290.80 | 29.85 |
| return %/year | 8.9 | 2.4 |
| gross profit | 51,147.04 | 11,273.37 |
| gross loss | 22,066.69 | 8,288.37 |
| trades | 48 | 35 |
| win rate % | 79.2 | 74.3 |
| avg win | 1,345.97 | 433.59 |
| avg loss | -2,206.67 | -920.93 |
| avg result / trade | 605.84 | 85.29 |
| largest single loss | -7,132.59 | -2,063.25 |
| largest loss % of equity | -22.74 | -15.96 |
| max drawdown | -8,772.70 | -3,788.23 |
| max drawdown % | -27.56 | -27.35 |
| profit factor | 2.32 | 1.36 |
| unusually bad trades | 1 | 1 |
| … threshold (% of equity) | 14.0 | 15.2 |
| time in market % | 14.6 | 15.4 |
| buy & hold return % | 2,918.19 | 1,414.11 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# stochastic_oversold_cross: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
SlowK(14,3) crosses above SlowD(14,3,3) AND SlowK < level AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: SlowK(14,3) > 80. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| level | 25.0 | 15.0 | 35.0 | 1.0 | 1.0 | 79.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol AAPL (spec: AAPL; stock).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 300 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `stock`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard; its "size for ~10% DD" column gives a risk-scaled size).
- Costs: library convention fee 0.05% + slippage 0.03% per fill (more conservative than the spec's 1 bp + 2 bp + 2 bp).
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder RSI/ATR with SMA seed, EMA with SMA seed, population std, PR excluding t).
- Adjusted closes are used for signals and fills (the project data has no separate raw execution series).

---
Backtest results don't guarantee future performance.
