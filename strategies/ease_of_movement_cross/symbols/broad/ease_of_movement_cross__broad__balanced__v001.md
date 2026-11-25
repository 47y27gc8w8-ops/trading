# ease_of_movement_cross__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d)
**Found at:** iteration 226 of optimization.log (2026-11-25T23:11:46Z); written at the checkpoint in iteration 376; backtest.py version `66df47bf4f`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 361.88)
**Range warning:** max_candles is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 24 |
| n | 19 |
| stop_atr | 1.75 |
| take_profit_atr | 2.0 |

```json
{
  "max_candles": 24,
  "n": 19,
  "stop_atr": 1.75,
  "take_profit_atr": 2.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 728.35 | 281.87 |
| return % | 7.28 | 2.82 |
| return %/year | 0.3 | 0.3 |
| gross profit | 7,682.84 | 7,887.76 |
| gross loss | 6,954.49 | 7,605.89 |
| trades | 5,039 | 5,212 |
| win rate % | 46.9 | 45.3 |
| avg win | 3.25 | 3.34 |
| avg loss | -2.60 | -2.67 |
| avg result / trade | 0.14 | 0.05 |
| largest single loss | -20.68 | -36.73 |
| largest loss % of equity | -13.03 | -9.81 |
| max drawdown | -567.73 | -713.09 |
| max drawdown % | -5.53 | -6.53 |
| profit factor | 1.10 | 1.04 |
| unusually bad trades | 436 | 500 |
| … threshold (% of equity) | 2.6 | 2.5 |
| time in market % | 7.3 | 14.4 |
| buy & hold return % | 124.13 | 280.02 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.77 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Ease Of Movement Cross

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
Ease of Movement (price change per unit of volume) turns positive on average while price is above its 100-day trend: buy easy upward movement, exit when its average turns negative.

## Market
- Symbols: GLD (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `SMA(EOM, n)` crosses above 0 AND `C > SMA(100)`; EOM = ((H+L)/2 − (H[1]+L[1])/2) × (H−L) / V, bars with V = 0 skipped.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `SMA(EOM, n) < 0` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | EOM smoothing length | 14 | 7–28 | 1 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 200 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- SMA(100) trend filter is a fixed constant (not in the spec's parameter table).

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
