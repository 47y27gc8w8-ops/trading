# bollinger_lower_band_reentry__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 63 of optimization.log (2026-11-25T17:46:14Z); written at the checkpoint in iteration 229; backtest.py version `1ca8bee48e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -52.86)

## Parameters

| parameter | value |
|---|---|
| k | 2.9 |
| max_bars | 16 |
| stop_atr | 3.75 |
| take_profit_atr | 3.5 |

```json
{
  "k": 2.9,
  "max_bars": 16,
  "stop_atr": 3.75,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 135.27 | 441.61 |
| return % | 1.35 | 4.42 |
| return %/year | 0.1 | 0.4 |
| gross profit | 1,065.07 | 1,282.58 |
| gross loss | 929.81 | 840.97 |
| trades | 339 | 430 |
| win rate % | 69.0 | 73.0 |
| avg win | 4.55 | 4.08 |
| avg loss | -8.86 | -7.25 |
| avg result / trade | 0.40 | 1.03 |
| largest single loss | -37.13 | -38.64 |
| largest loss % of equity | -17.93 | -21.36 |
| max drawdown | -440.77 | -332.15 |
| max drawdown % | -4.35 | -3.27 |
| profit factor | 1.15 | 1.52 |
| unusually bad trades | 26 | 10 |
| … threshold (% of equity) | 7.2 | 7.6 |
| time in market % | 1.1 | 2.3 |
| buy & hold return % | 108.03 | 303.57 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 6.67 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Bollinger Lower Band Reentry

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: SPY (base run); screening universe: `etf` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `C[1] < BB_lower(20, k)[1]` AND `C > BB_lower(20, k)` (cross back above) AND `ADX(14) < 25`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `C >= SMA(20)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| k | band width in std | 2 | 1.5–3 | 0.1 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 12 | 6–24 | 2 |

Constraints: none beyond positive exits. All other numbers in the triggers are fixed constants of the spec.

## Setup
- In-sample (tuning): 1995-01-01 (or the symbol's first bar after 120 warm-up bars) → 2016-01-01
- Out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill

## Assumptions
- Sizing: 100% of equity per trade (user's choice for the library, 2026-11-24, so results compare across the leaderboard); the spec's risk_fraction is not used or tuned.
- Costs: fee 0.05%/side + slippage 0.03%/fill, the US ETF/stock convention of the user-approved absolute_momentum_monthly setup (above the spec's 1 bp + 2 bp + 2 bp). Exits at the target are charged slippage too (slightly conservative vs a limit order).
- Bars: Yahoo daily, dividend/split adjusted OHLC (the project has no separate raw execution series), used for signals and fills.
- ATR(14) is Wilder's RMA of true range with an SMA seed; stop and target are frozen at entry from the signal bar's ATR, never move, and are checked intrabar (stop first when both touch). A gap through the stop fills at the open; a target fills at the target price.
- max_candles is the template's max_bars (entry bar counts as 1; exit at the next open after bar N).
- Entry veto: no entry when the strategy's own close-based exit is true on the signal bar. After an intrabar stop/target exit, the next entry needs a signal from the following bar on (one fully flat bar).
- Base symbol = the first listed candidate; the others (and the rest of the universe) are covered by screening, since the spec calls the listed instruments alternatives, not a basket.
- Period: in-sample 1995-01-01 (or the symbol's first warmed-up bar) to 2016-01-01, out-of-sample to 2026-11-23 (frozen): repo precedent for ETF strategies.

## Open questions
- none (library conventions agreed across the library sessions and the user's absolute_momentum_monthly choices)

---
Backtest results don't guarantee future performance.
