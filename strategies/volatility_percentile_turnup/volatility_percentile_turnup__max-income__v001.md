# volatility_percentile_turnup: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 739 of optimization.log (2026-11-25T05:46:27Z); written at the checkpoint in iteration 35571; backtest.py version `27cc240f83`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/8 one-step neighbours profitable in-sample (worst neighbour net -547.45)

## Parameters

| parameter | value |
|---|---|
| max_candles | 90 |
| n | 120 |
| stop_atr | 3.5 |
| take_profit_atr | 3.0 |

```json
{
  "max_candles": 90,
  "n": 120,
  "stop_atr": 3.5,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 733.06 | 149.72 |
| return % | 7.33 | 1.50 |
| return %/year | 0.4 | 0.1 |
| gross profit | 4,712.26 | 3,299.28 |
| gross loss | 3,979.20 | 3,149.56 |
| trades | 41 | 36 |
| win rate % | 43.9 | 41.7 |
| avg win | 261.79 | 219.95 |
| avg loss | -173.01 | -149.98 |
| avg result / trade | 17.88 | 4.16 |
| largest single loss | -500.83 | -398.72 |
| largest loss % of equity | -5.09 | -4.03 |
| max drawdown | -1,549.39 | -1,503.19 |
| max drawdown % | -14.63 | -13.66 |
| profit factor | 1.18 | 1.05 |
| unusually bad trades | 3 | 1 |
| … threshold (% of equity) | 2.9 | 3.1 |
| time in market % | 12.3 | 13.6 |
| buy & hold return % | 85.02 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.32 |
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
