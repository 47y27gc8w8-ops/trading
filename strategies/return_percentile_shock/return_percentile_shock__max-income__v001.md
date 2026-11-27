# return_percentile_shock: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 83 of optimization.log (2026-11-25T10:55:23Z); written at the checkpoint in iteration 260; backtest.py version `d5c1e2fac8`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/10 one-step neighbours profitable in-sample (worst neighbour net -484.54)

## Parameters

| parameter | value |
|---|---|
| max_candles | 8 |
| n | 130 |
| rank | 2 |
| stop_atr | 3.5 |
| take_profit_atr | 3.5 |

```json
{
  "max_candles": 8,
  "n": 130,
  "rank": 2,
  "stop_atr": 3.5,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,040.49 | 1,163.29 |
| return % | 10.40 | 11.63 |
| return %/year | 0.6 | 1.0 |
| gross profit | 4,061.92 | 4,247.16 |
| gross loss | 3,021.44 | 3,083.87 |
| trades | 48 | 40 |
| win rate % | 66.7 | 70.0 |
| avg win | 126.94 | 151.68 |
| avg loss | -188.84 | -256.99 |
| avg result / trade | 21.68 | 29.08 |
| largest single loss | -517.73 | -653.36 |
| largest loss % of equity | -4.61 | -5.53 |
| max drawdown | -1,034.03 | -737.92 |
| max drawdown % | -8.91 | -6.20 |
| profit factor | 1.34 | 1.38 |
| unusually bad trades | 4 | 3 |
| … threshold (% of equity) | 2.5 | 3.8 |
| time in market % | 4.5 | 4.6 |
| buy & hold return % | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.65 |
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
