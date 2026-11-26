# keltner_upper_breakout__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d)
**Found at:** iteration 141 of optimization.log (2026-11-26T02:36:44Z); written at the checkpoint in iteration 243; backtest.py version `ee08b24994`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/7 one-step neighbours profitable in-sample (worst neighbour net -147.89)
**Range warning:** k is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 3.0 |
| max_candles | 72 |
| stop_atr | 2.25 |
| take_profit_atr | 2.5 |

```json
{
  "k": 3.0,
  "max_candles": 72,
  "stop_atr": 2.25,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 52.61 | 10.93 |
| return % | 0.53 | 0.11 |
| return %/year | 0.0 | 0.0 |
| gross profit | 2,835.56 | 3,319.61 |
| gross loss | 2,782.95 | 3,308.67 |
| trades | 1,316 | 1,629 |
| win rate % | 47.8 | 47.4 |
| avg win | 4.51 | 4.30 |
| avg loss | -4.05 | -3.86 |
| avg result / trade | 0.04 | 0.01 |
| largest single loss | -24.27 | -28.55 |
| largest loss % of equity | -14.73 | -18.27 |
| max drawdown | -349.77 | -552.95 |
| max drawdown % | -3.40 | -5.46 |
| profit factor | 1.02 | 1.00 |
| unusually bad trades | 78 | 124 |
| … threshold (% of equity) | 4.3 | 4.1 |
| time in market % | 3.5 | 8.2 |
| buy & hold return % | 127.68 | 280.36 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.50 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Keltner Upper Breakout

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Volatility breakout: buy when the close breaks above the upper Keltner channel while the 20-day EMA is rising; exit when price falls back below the EMA.

## Market
- Symbols: GLD (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `C` crosses above `KC_upper(20,10,k) = EMA(20) + k × ATR(10)` AND `EMA(20) > EMA(20)[5]`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C < EMA(20)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| k | Keltner ATR multiplier | 2 | 1–3 | 0.25 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 150 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- EMA(20), ATR(10) and the 5-bar slope lag are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
