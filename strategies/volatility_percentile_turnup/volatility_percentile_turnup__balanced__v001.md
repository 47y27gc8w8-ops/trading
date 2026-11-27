# volatility_percentile_turnup: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 3559 of optimization.log (2026-11-25T05:47:20Z); written at the checkpoint in iteration 35572; backtest.py version `27cc240f83`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/8 one-step neighbours profitable in-sample (worst neighbour net -181.08)

## Parameters

| parameter | value |
|---|---|
| max_candles | 36 |
| n | 190 |
| stop_atr | 2.75 |
| take_profit_atr | 5.0 |

```json
{
  "max_candles": 36,
  "n": 190,
  "stop_atr": 2.75,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 267.07 | 118.25 |
| return % | 2.67 | 1.18 |
| return %/year | 0.2 | 0.1 |
| gross profit | 3,195.03 | 2,901.94 |
| gross loss | 2,927.95 | 2,783.69 |
| trades | 33 | 30 |
| win rate % | 48.5 | 36.7 |
| avg win | 199.69 | 263.81 |
| avg loss | -172.23 | -146.51 |
| avg result / trade | 8.09 | 3.94 |
| largest single loss | -370.10 | -405.20 |
| largest loss % of equity | -3.65 | -4.03 |
| max drawdown | -1,560.23 | -1,364.20 |
| max drawdown % | -14.53 | -12.67 |
| profit factor | 1.09 | 1.04 |
| unusually bad trades | 2 | 1 |
| … threshold (% of equity) | 2.9 | 3.2 |
| time in market % | 11.9 | 15.2 |
| buy & hold return % | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.69 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# volatility_percentile_turnup: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
PR(ATR(14)/C, n)[1] < 15 AND ATR(14) > ATR(14)[1] AND C > HH(H,10)[1].

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: C < EMA(20). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 100 | 50 | 250 | 10 | 10 |  |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 48 | 24 | 96 | 6 | 2 |  |

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
