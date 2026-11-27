# cross_market_trend_confirmation__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 60 of optimization.log (2026-11-25T13:55:33Z); written at the checkpoint in iteration 231; backtest.py version `951e834614`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 963.55)
**Range warning:** take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_bars | 66 |
| n | 46 |
| stop_atr | 1.25 |
| take_profit_atr | 6.0 |

```json
{
  "max_bars": 66,
  "n": 46,
  "stop_atr": 1.25,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,033.04 | 1,169.05 |
| return % | 10.33 | 11.69 |
| return %/year | 0.5 | 1.0 |
| gross profit | 4,953.14 | 5,956.16 |
| gross loss | 3,920.10 | 4,787.11 |
| trades | 2,112 | 2,649 |
| win rate % | 29.9 | 31.3 |
| avg win | 7.84 | 7.18 |
| avg loss | -2.65 | -2.63 |
| avg result / trade | 0.49 | 0.44 |
| largest single loss | -15.15 | -33.64 |
| largest loss % of equity | -8.44 | -8.35 |
| max drawdown | -899.63 | -547.10 |
| max drawdown % | -7.53 | -4.98 |
| profit factor | 1.26 | 1.24 |
| unusually bad trades | 227 | 284 |
| … threshold (% of equity) | 2.1 | 2.1 |
| time in market % | 6.7 | 16.7 |
| buy & hold return % | 100.07 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.17 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Cross Market Trend Confirmation

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: QQQ (base run); screening universe: `etf` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `C` crosses above `EMA(n)` AND `SOXX C > SMA(SOXX, 100)` AND `SOXX ROC(21) > ROC(21)` (traded symbol)
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `C < EMA(n)` OR `SOXX C < SMA(SOXX, 100)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| n | EMA length on the traded symbol | 20 | 10–50 | 2 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 48 | 24–96 | 6 |

Constraints: none beyond positive exits. All other numbers in the triggers are fixed constants of the spec.

## Setup
- In-sample (tuning): 1995-01-01 (or the symbol's first bar after 260 warm-up bars) → 2016-01-01
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
- SOXX is the fixed reference for every screened symbol: the spec names it; screening asks which other symbols the same semiconductor-confirmation rule suits.
- SOXX closes are aligned to the traded symbol's dates without forward fill; a missing SOXX bar means no signal (EXECUTION.md). SOXX history starts 2001, so earlier bars never signal.

## Open questions
- none (library conventions agreed across the library sessions and the user's absolute_momentum_monthly choices)

---
Backtest results don't guarantee future performance.
