# williams_r_recovery__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 281 of optimization.log (2026-11-25T05:45:14Z); written at the checkpoint in iteration 504; backtest.py version `43bffb3ba4`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 100% of one-step neighbours profitable in-sample (earlier run)
**Range warning:** level is at the min of its range, stop_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| level | -90 |
| max_candles | 16 |
| n | 10 |
| stop_atr | 4.0 |
| take_profit_atr | 4.0 |

```json
{
  "level": -90,
  "max_candles": 16,
  "n": 10,
  "stop_atr": 4.0,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,242.10 | 1,773.16 |
| return % | 32.42 | 17.73 |
| return %/year | 1.8 | 1.5 |
| gross profit | 8,132.72 | 8,365.68 |
| gross loss | 4,890.61 | 6,592.52 |
| trades | 2,723 | 2,949 |
| win rate % | 71.8 | 68.7 |
| avg win | 4.16 | 4.13 |
| avg loss | -6.36 | -7.15 |
| avg result / trade | 1.19 | 0.60 |
| largest single loss | -48.07 | -111.15 |
| largest loss % of equity | -24.25 | -37.66 |
| max drawdown | -524.52 | -789.03 |
| max drawdown % | -4.39 | -6.66 |
| profit factor | 1.66 | 1.27 |
| unusually bad trades | 275 | 243 |
| … threshold (% of equity) | 3.3 | 4.4 |
| time in market % | 9.5 | 14.1 |
| buy & hold return % | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.85 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# williams_r_recovery: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
WilliamsR(n) crosses above level AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: WilliamsR(n) > -20. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 14 | 7 | 28 | 1 | 2 |  |
| level | -80.0 | -90.0 | -70.0 | 1.0 | -99.0 | -21.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol QQQ (spec: QQQ; ETF).
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
