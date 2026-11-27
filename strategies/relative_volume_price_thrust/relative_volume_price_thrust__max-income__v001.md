# relative_volume_price_thrust: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** NVDA (etf, 1d)
**Found at:** iteration 18680 of optimization.log (2026-11-25T11:10:27Z); written at the checkpoint in iteration 27088; backtest.py version `e55a16e3a2`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 10,067.16)

## Parameters

| parameter | value |
|---|---|
| max_candles | 96 |
| rvol | 1.25 |
| stop_atr | 1.75 |
| take_profit_atr | 5.0 |

```json
{
  "max_candles": 96,
  "rvol": 1.25,
  "stop_atr": 1.75,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 29,510.70 | 19,497.54 |
| return % | 295.11 | 194.98 |
| return %/year | 9.0 | 10.4 |
| gross profit | 71,939.75 | 35,536.44 |
| gross loss | 42,429.05 | 16,038.91 |
| trades | 66 | 40 |
| win rate % | 45.5 | 42.5 |
| avg win | 2,397.99 | 2,090.38 |
| avg loss | -1,178.58 | -697.34 |
| avg result / trade | 447.13 | 487.44 |
| largest single loss | -3,150.77 | -1,574.14 |
| largest loss % of equity | -12.86 | -5.07 |
| max drawdown | -9,728.43 | -5,402.15 |
| max drawdown % | -45.07 | -24.82 |
| profit factor | 1.70 | 2.22 |
| unusually bad trades | 4 | 1 |
| … threshold (% of equity) | 8.8 | 8.7 |
| time in market % | 13.1 | 12.7 |
| buy & hold return % | 790.82 | 20,904.13 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.17 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# relative_volume_price_thrust: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
V / SMA(V,20)[1] > rvol AND C > HH(H,10)[1] AND CLV01 > 0.8.

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: C < EMA(10). Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| rvol | 2.0 | 1.5 | 4.0 | 0.25 | 1.0 |  |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 48 | 24 | 96 | 6 | 2 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol NVDA (spec: NVDA; stock).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 100 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `stock`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard; its "size for ~10% DD" column gives a risk-scaled size).
- Costs: library convention fee 0.05% + slippage 0.03% per fill (more conservative than the spec's 1 bp + 2 bp + 2 bp).
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder RSI/ATR with SMA seed, EMA with SMA seed, population std, PR excluding t).
- Adjusted closes are used for signals and fills (the project data has no separate raw execution series).
- `V/SMA(V,20)[1]` is read as today's volume divided by the 20-bar volume average ending yesterday (baseline excludes t), matching EXECUTION.md's 'preceding' convention.

---
Backtest results don't guarantee future performance.
