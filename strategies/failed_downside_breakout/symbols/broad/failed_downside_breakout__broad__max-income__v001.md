# failed_downside_breakout__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L, ^GSPC, ^IXIC, ^DJI, ^RUT, ^VIX, ^SSMI, ^STOXX50E, ^GDAXI, ^N225, ^FTSE (etf, 1d)
**Found at:** iteration 265 of optimization.log (2026-11-26T00:42:11Z); written at the checkpoint in iteration 293; backtest.py version `af30724b73`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 20,443.46)
**Range warning:** take_profit_atr is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 52 |
| n | 12 |
| stop_atr | 3.25 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 52,
  "n": 12,
  "stop_atr": 3.25,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 31,251.93 | 12,251.85 |
| return % | 312.52 | 122.52 |
| return %/year | 7.0 | 7.6 |
| gross profit | 49,747.11 | 23,176.39 |
| gross loss | 18,495.17 | 10,924.54 |
| trades | 4,290 | 3,585 |
| win rate % | 68.7 | 69.9 |
| avg win | 16.87 | 9.24 |
| avg loss | -13.78 | -10.13 |
| avg result / trade | 7.28 | 3.42 |
| largest single loss | -1,875.83 | -1,455.70 |
| largest loss % of equity | -5.70 | -11.81 |
| max drawdown | -7,242.11 | -3,237.09 |
| max drawdown % | -16.93 | -15.16 |
| profit factor | 2.69 | 2.12 |
| unusually bad trades | 210 | 134 |
| … threshold (% of equity) | 8.1 | 7.2 |
| time in market % | 7.0 | 10.7 |
| buy & hold return % | 131.76 | 280.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.09 |
| period | 1995-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Failed Downside Breakout

Source: original.md (research-library spec, 2026-11). This file is the testable version.
Conventions from ../../EXECUTION.md and ../../INDICATORS.md apply.

## Idea
A bar that undercuts the prior n-bar low but closes back above it and above its open is a failed breakdown (bear trap): buy the reversal, exit when price regains the 20-day mean.

## Market
- Symbols: IWM (base run, Yahoo daily, adjusted for dividends and splits); screening over the project's ETF list
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time

## Buy trigger
At the close of bar t (bar t and earlier only): `L < LL(L, n)[1]` AND `C > LL(L, n)[1]` AND `C > O`.
Entry veto: no entry when the sell condition is already true on the signal bar.
Entry is skipped if the signal bar's ATR(14) ≤ 0 / missing or the stop would be ≤ 0.
Order: buy at the open of bar t+1.

## Sell trigger
First of (E = entry fill, A = ATR(14) of the signal bar, both frozen at entry):
- Signal exit: `C >= SMA(20)` at a close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after max_candles completed held bars (entry bar = 1) → sell at the next open
- Stop and target touched in the same bar → stop assumed.
- After a stop/target exit the next signal may come from the following bar on (one fully flat bar).

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | prior-low lookback | 20 | 10–60 | 2 |
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
- The exit SMA(20) stays fixed at 20 when n varies: the spec's n is the signal lookback, and literals outside the parameter table are fixed constants.

## Open questions
- none (sizing and costs follow the user's library-wide choices)

---
Backtest results don't guarantee future performance.
