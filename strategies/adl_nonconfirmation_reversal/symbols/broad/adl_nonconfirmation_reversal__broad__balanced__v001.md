# adl_nonconfirmation_reversal__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 122 of optimization.log (2026-11-25T06:02:18Z); written at the checkpoint in iteration 272; backtest.py version `cdafece0cc`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 179.55)

## Parameters

| parameter | value |
|---|---|
| max_candles | 72 |
| n | 28 |
| stop_atr | 1.5 |
| take_profit_atr | 4.0 |

```json
{
  "max_candles": 72,
  "n": 28,
  "stop_atr": 1.5,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 281.65 | 391.61 |
| return % | 2.82 | 3.92 |
| return %/year | 0.2 | 0.3 |
| gross profit | 2,330.47 | 2,633.44 |
| gross loss | 2,048.82 | 2,241.83 |
| trades | 590 | 728 |
| win rate % | 45.9 | 48.4 |
| avg win | 8.60 | 7.48 |
| avg loss | -6.42 | -5.96 |
| avg result / trade | 0.48 | 0.54 |
| largest single loss | -27.48 | -56.93 |
| largest loss % of equity | -14.56 | -27.12 |
| max drawdown | -432.53 | -574.37 |
| max drawdown % | -4.29 | -5.52 |
| profit factor | 1.14 | 1.18 |
| unusually bad trades | 42 | 57 |
| … threshold (% of equity) | 5.5 | 5.0 |
| time in market % | 1.8 | 3.0 |
| buy & hold return % | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.06 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# ADL Non-confirmation Reversal

Source: original.md (120-strategy research library, staged 2026-11-24) plus the binding conventions in
../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version.

## Idea
Buy a fresh short-term closing low when the accumulation/distribution line refuses to make a new low
(volume-weighted buying under the surface) and the bar itself closes near its high. Exit on the
reversion back to the moving average, a fixed ATR target, an ATR stop, or a time limit.

## Market
- Symbol: XLI (Industrial Select Sector SPDR), Yahoo daily bars, split/dividend adjusted
- Timeframe: 1d (exchange sessions)
- Direction: long only, one position at a time

## Buy trigger
At the close of bar t (all three, plus the entry veto):
- `C[t] < min(C[t-n..t-1])` (new n-bar closing low, `LL(C,n)[1]`)
- `ADL[t] > min(ADL[t-n..t-1])` (`LL(ADL,n)[1]`), ADL = cumsum(((2C−H−L)/(H−L))·V), increment 0 if H = L
- `CLV01[t] > 0.7`, CLV01 = (C−L)/(H−L), 0.5 if H = L
- veto: not if the signal exit `C[t] >= SMA(C,n)` is already true (it can't be, given a new low; kept for fidelity)

Order: buy at the open of bar t+1. Freeze E = fill, A = ATR(14) (Wilder) of bar t.
Skip if A ≤ 0 or E − stop_atr·A ≤ 0.

## Sell trigger
First of (OR):
- time: after `max_candles` completed held bars (entry bar = 1) → sell at the next open
- stop: low ≤ S = E − stop_atr·A, active from the entry bar; a gap below S fills at the open; slippage applies
- target: high ≥ T = E + take_profit_atr·A; resting limit, fills at T (also on a favourable gap), no slippage
- signal: `C >= SMA(C,n)` at a close → sell at the next open
Stop is assumed first if stop and target are touched in the same bar.
Re-entry needs one completed flat bar: after an exit at an open, a signal on that same bar is allowed
(entry the next open); after an intrabar stop/target exit, the next signal can come from the following bar.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| n | lookback for the closing low, ADL low and exit SMA | 20 | 10–60 (hard min 3) | 2 |
| stop_atr | stop distance in ATR(14) | 2 | 1–4 (hard min 0.25) | 0.25 |
| take_profit_atr | target distance in ATR(14) | 3 | 1.5–6 (hard min 0.25) | 0.25 |
| max_candles | time exit, held bars | 48 | 24–96 (hard min 1) | 4 |

Fixed: CLV threshold 0.7, ATR length 14 (spec: literals not in the table are fixed; ATR(14) is not an
optimized parameter). No order constraints between parameters.
`risk_fraction` (0.005, range 0.001–0.01) is not optimized: see Assumptions.

## Setup
- Data: XLI 1998-12-22 → 2026-11-23 (end frozen); first tradable bar after 300 warm-up bars (2000-03-02)
- In-sample (tuning): 2000-01-01 → 2015-12-31; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per market/stop fill (target limit fills: fee only)

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction stop-distance sizing — the user's
  standing choice for library specs (2026-11-24), so results compare across the leaderboard. The
  summary's suggested position size plays the role of risk_fraction.
- The "20" in both `LL(…,20)` and `SMA(20)` is the single parameter `n` (spec: trigger text shows the start
  configuration of the named parameters; n is the only lookback).
- Costs: repo defaults for US ETFs (0.05% + 0.03%), about 1.6× the spec's base scenario (1 bp commission,
  2 bp half-spread, 2 bp slippage), i.e. between its 1× and 2× stress levels.
- Volume: Yahoo split-adjusted volume as delivered by the project loader.
- OOS start 2016-01-01: repo precedent for ETF strategies, keeps results comparable.
- Screening universe: the `etf` list in config/symbols.yaml without `^` indices (not tradable, no volume).

## Open questions
None asked. The spec is explicit about triggers; open points were decided above and logged.

---
Backtest results don't guarantee future performance.
