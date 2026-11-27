# three_down_closes__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 62 of optimization.log (2026-11-25T07:22:33Z); written at the checkpoint in iteration 244; backtest.py version `aece766218`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -212.92)

## Parameters

| parameter | value |
|---|---|
| max_candles | 12 |
| n | 3 |
| stop_atr | 3.0 |
| take_profit_atr | 3.5 |

```json
{
  "max_candles": 12,
  "n": 3,
  "stop_atr": 3.0,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,675.58 | 579.76 |
| return % | 16.76 | 5.80 |
| return %/year | 1.0 | 0.5 |
| gross profit | 6,283.82 | 6,497.70 |
| gross loss | 4,608.24 | 5,917.94 |
| trades | 4,106 | 4,592 |
| win rate % | 61.9 | 60.7 |
| avg win | 2.47 | 2.33 |
| avg loss | -2.95 | -3.28 |
| avg result / trade | 0.41 | 0.13 |
| largest single loss | -33.37 | -51.42 |
| largest loss % of equity | -9.27 | -17.78 |
| max drawdown | -381.65 | -808.37 |
| max drawdown % | -3.18 | -7.76 |
| profit factor | 1.36 | 1.10 |
| unusually bad trades | 379 | 559 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 5.8 | 9.0 |
| buy & hold return % | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.54 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# three_down_closes: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
The last n close-to-close returns are each negative AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: C > H[1]. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 3 | 2 | 5 | 1 | 1 | 10 |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol SPY (spec: SPY; ETF).
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
