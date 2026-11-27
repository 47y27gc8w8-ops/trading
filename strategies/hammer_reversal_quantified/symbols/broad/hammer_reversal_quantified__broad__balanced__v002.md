# hammer_reversal_quantified__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d)
**Found at:** iteration 251 of optimization.log (2026-11-26T02:21:19Z); written at the checkpoint in iteration 750; backtest.py version `afbd7797ed`
**Replaces:** hammer_reversal_quantified__broad__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 100.32)

## Parameters

| parameter | value |
|---|---|
| max_candles | 32 |
| ratio | 2.25 |
| stop_atr | 2.75 |
| take_profit_atr | 1.0 |

```json
{
  "max_candles": 32,
  "ratio": 2.25,
  "stop_atr": 2.75,
  "take_profit_atr": 1.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 366.95 | 85.39 |
| return % | 3.67 | 0.85 |
| return %/year | 0.2 | 0.1 |
| gross profit | 961.33 | 800.96 |
| gross loss | 594.39 | 715.58 |
| trades | 621 | 599 |
| win rate % | 73.4 | 71.8 |
| avg win | 2.11 | 1.86 |
| avg loss | -3.60 | -4.23 |
| avg result / trade | 0.59 | 0.14 |
| largest single loss | -14.62 | -43.13 |
| largest loss % of equity | -7.86 | -28.04 |
| max drawdown | -55.31 | -133.95 |
| max drawdown % | -0.55 | -1.33 |
| profit factor | 1.62 | 1.12 |
| unusually bad trades | 36 | 26 |
| … threshold (% of equity) | 3.7 | 4.5 |
| time in market % | 0.5 | 1.0 |
| buy & hold return % | 119.84 | 280.02 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.47 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Hammer Reversal Quantified

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
A quantified hammer candle (long lower wick, small upper wick, close in the upper part of the range) that makes a new 10-bar low inside a long-term uptrend: buy the rejection of lower prices, exit at the 10-day mean.

## Market
- Symbols: GLD (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): lower wick ≥ ratio × body AND upper wick ≤ body AND body/(H−L) ≥ 0.1 AND CLV01 > 0.65 AND `L < LL(L,10)[1]` AND `C > SMA(200)`; body = |C−O|, lower wick = min(O,C) − L, upper wick = H − max(O,C), CLV01 = (C−L)/(H−L); bars with H = L skipped.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C >= SMA(10)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| ratio | min lower-wick / body | 2 | 1.5–4 | 0.25 |
| stop_atr | stop distance, × signal-bar ATR(14) | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance, × the same ATR | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit after N completed held bars | 48 | 24–96 | 4 |

Constraints: none. `risk_fraction` (spec 0.005) is not used (see assumptions).

## Setup
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end)
- Each symbol trades only after 250 bars of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Position size = 100% of equity per trade, not the spec's risk_fraction sizing (user's choice for the library, so results compare on the leaderboard); risk_fraction is therefore not optimized.
- Costs: fee 0.05% per side, slippage 0.03% per fill (repo US ETF/stock defaults, library-wide convention), slightly above the spec's 5 bp scenario.
- Fills on adjusted prices (the project has no separate raw execution series).
- In-sample 1995-01-01 → 2016-01-01, out-of-sample 2016-01-01 → 2026-11-23 (repo precedent for ETF strategies; same split across the library).
- Indicators: EMA/RMA seeded with the SMA of the first n values, ATR = Wilder RMA of TR (INDICATORS.md).
- Screening universe: Yahoo ETFs (spec: ETF); listed instruments are alternatives, tested separately.
- 0.1, 0.65, LL(10), SMA(200) and the exit SMA(10) are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
