# cmf_accumulation_cross: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** XLF (etf, 1d)
**Found at:** iteration 803 of optimization.log (2026-11-25T15:43:34Z); written at the checkpoint in iteration 957; backtest.py version `5ae30db648`
**Replaces:** cmf_accumulation_cross__balanced__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 515.97)

## Parameters

| parameter | value |
|---|---|
| level | 0.09 |
| max_bars | 96 |
| n | 26 |
| stop_atr | 2.25 |
| take_profit_atr | 5.0 |

```json
{
  "level": 0.09,
  "max_bars": 96,
  "n": 26,
  "stop_atr": 2.25,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 6,675.90 | 2,201.01 |
| return % | 66.76 | 22.01 |
| return %/year | 3.2 | 1.8 |
| gross profit | 18,117.27 | 9,135.78 |
| gross loss | 11,441.37 | 6,934.77 |
| trades | 67 | 44 |
| win rate % | 50.8 | 40.9 |
| avg win | 532.86 | 507.54 |
| avg loss | -346.71 | -266.72 |
| avg result / trade | 99.64 | 50.02 |
| largest single loss | -817.11 | -556.86 |
| largest loss % of equity | -4.87 | -4.53 |
| max drawdown | -2,301.73 | -3,027.01 |
| max drawdown % | -17.12 | -24.42 |
| profit factor | 1.58 | 1.32 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 4.5 | 4.9 |
| time in market % | 25.9 | 26.5 |
| buy & hold return % | 41.29 | 257.92 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.58 |
| period | 1999-08-12 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Cmf Accumulation Cross

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: XLF (base run); screening universe: `etf` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `CMF(n)` crosses above `level` AND `C > SMA(100)`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `CMF(n) < 0` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| n | CMF length | 20 | 10–40 | 2 |
| level | CMF cross level | 0.10 | 0–0.25 | 0.01 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 48 | 24–96 | 6 |

Constraints: none beyond positive exits. All other numbers in the triggers are fixed constants of the spec.

## Setup
- In-sample (tuning): 1995-01-01 (or the symbol's first bar after 160 warm-up bars) → 2016-01-01
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
