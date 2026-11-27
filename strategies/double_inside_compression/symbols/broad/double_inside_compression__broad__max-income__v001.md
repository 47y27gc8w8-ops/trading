# double_inside_compression__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d)
**Found at:** iteration 119 of optimization.log (2026-11-25T22:44:50Z); written at the checkpoint in iteration 2484; backtest.py version `4b76847a81`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/5 one-step neighbours profitable in-sample (worst neighbour net 46.98)

## Parameters

| parameter | value |
|---|---|
| max_candles | 72 |
| stop_atr | 4.0 |
| take_profit_atr | 4.0 |

```json
{
  "max_candles": 72,
  "stop_atr": 4.0,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 53.24 | 6.28 |
| return % | 0.53 | 0.06 |
| return %/year | 0.0 | 0.0 |
| gross profit | 300.49 | 180.82 |
| gross loss | 247.25 | 174.54 |
| trades | 146 | 133 |
| win rate % | 37.0 | 42.1 |
| avg win | 5.56 | 3.23 |
| avg loss | -2.69 | -2.27 |
| avg result / trade | 0.36 | 0.05 |
| largest single loss | -14.33 | -8.33 |
| largest loss % of equity | -9.31 | -5.67 |
| max drawdown | -52.50 | -61.16 |
| max drawdown % | -0.52 | -0.61 |
| profit factor | 1.22 | 1.04 |
| unusually bad trades | 21 | 16 |
| … threshold (% of equity) | 2.7 | 2.3 |
| time in market % | 0.3 | 0.5 |
| buy & hold return % | 131.76 | 280.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.33 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Double Inside Compression

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Two consecutive inside bars (a volatility squeeze) followed by a close above the range of the bar that started it: buy the breakout of the compression, exit when price loses its short EMA.

## Market
- Symbols: QQQ (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `H[1] < H[2] < H[3]` AND `L[1] > L[2] > L[3]` AND `C > H[3]`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C < EMA(10)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 100 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- The spec has no tunable signal parameter: only the exits are optimized; EMA(10) is a fixed constant.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
