# chaikin_oscillator_cross: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** MSFT (etf, 1d)
**Found at:** iteration 122 of optimization.log (2026-11-25T16:22:19Z); written at the checkpoint in iteration 225; backtest.py version `7f972f2d22`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,917.35)

## Parameters

| parameter | value |
|---|---|
| max_bars | 48 |
| n | 12 |
| stop_atr | 3.25 |
| take_profit_atr | 5.5 |

```json
{
  "max_bars": 48,
  "n": 12,
  "stop_atr": 3.25,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 4,753.71 | 3,751.68 |
| return % | 47.54 | 37.52 |
| return %/year | 1.9 | 3.0 |
| gross profit | 94,787.64 | 32,604.23 |
| gross loss | 90,033.93 | 28,852.55 |
| trades | 282 | 141 |
| win rate % | 32.6 | 42.5 |
| avg win | 1,030.30 | 543.40 |
| avg loss | -473.86 | -356.20 |
| avg result / trade | 16.86 | 26.61 |
| largest single loss | -3,280.22 | -1,130.08 |
| largest loss % of equity | -12.25 | -6.85 |
| max drawdown | -21,485.51 | -9,133.70 |
| max drawdown % | -73.87 | -53.34 |
| profit factor | 1.05 | 1.13 |
| unusually bad trades | 35 | 19 |
| … threshold (% of equity) | 4.7 | 4.5 |
| time in market % | 43.4 | 53.0 |
| buy & hold return % | 1,968.97 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.59 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Chaikin Oscillator Cross

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: MSFT (base run); screening universe: `stock` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `ChaikinOsc(3, 10)` crosses above 0 AND `ADL > SMA(ADL, n)`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `ChaikinOsc(3, 10) < 0` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| n | ADL trend SMA length | 20 | 10–50 | 2 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 48 | 24–96 | 6 |

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
