# stochastic_pop__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 760 of optimization.log (2026-11-25T07:45:51Z); written at the checkpoint in iteration 790; backtest.py version `e9a1993ec3`
**Replaces:** stochastic_pop__broad__balanced__v001.md
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -162.58)

## Parameters

| parameter | value |
|---|---|
| level | 72 |
| max_candles | 24 |
| stop_atr | 4.25 |
| take_profit_atr | 2.5 |

```json
{
  "level": 72,
  "max_candles": 24,
  "stop_atr": 4.25,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 82.56 | 400.67 |
| return % | 0.83 | 4.01 |
| return %/year | 0.1 | 0.4 |
| gross profit | 3,872.36 | 4,325.43 |
| gross loss | 3,789.80 | 3,924.77 |
| trades | 1,658 | 1,695 |
| win rate % | 46.3 | 48.0 |
| avg win | 5.05 | 5.31 |
| avg loss | -4.25 | -4.45 |
| avg result / trade | 0.05 | 0.24 |
| largest single loss | -34.45 | -43.90 |
| largest loss % of equity | -16.70 | -31.93 |
| max drawdown | -353.38 | -350.18 |
| max drawdown % | -3.39 | -3.43 |
| profit factor | 1.02 | 1.10 |
| unusually bad trades | 147 | 200 |
| … threshold (% of equity) | 3.6 | 3.2 |
| time in market % | 7.2 | 10.3 |
| buy & hold return % | 89.54 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 7.20 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# stochastic_pop: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
SlowK(14,3) crosses above level AND ADX(14) > 20 AND C > SMA(100).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: SlowK(14,3) < 50. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| level | 80.0 | 70.0 | 90.0 | 1.0 | 51.0 | 99.0 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 96 | 48 | 192 | 12 | 4 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol QQQ (spec: QQQ; ETF).
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
