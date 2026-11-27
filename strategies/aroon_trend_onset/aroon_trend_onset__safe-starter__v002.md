# aroon_trend_onset: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** GLD (etf, 1d)
**Found at:** iteration 423 of optimization.log (2026-11-25T18:46:06Z); written at the checkpoint in iteration 941; backtest.py version `0f1046be1b`
**Replaces:** aroon_trend_onset__safe-starter__v001.md
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -634.03)

## Parameters

| parameter | value |
|---|---|
| level | 50.0 |
| max_bars | 48 |
| n | 20 |
| stop_atr | 0.75 |
| take_profit_atr | 4.0 |

```json
{
  "level": 50.0,
  "max_bars": 48,
  "n": 20,
  "stop_atr": 0.75,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,220.11 | 3,039.26 |
| return % | 22.20 | 30.39 |
| return %/year | 2.0 | 2.5 |
| gross profit | 4,266.32 | 5,655.58 |
| gross loss | 2,046.20 | 2,616.32 |
| trades | 21 | 34 |
| win rate % | 33.3 | 41.2 |
| avg win | 609.47 | 403.97 |
| avg loss | -146.16 | -130.82 |
| avg result / trade | 105.72 | 89.39 |
| largest single loss | -194.40 | -316.48 |
| largest loss % of equity | -1.94 | -2.33 |
| max drawdown | -882.73 | -684.12 |
| max drawdown % | -7.95 | -5.85 |
| profit factor | 2.08 | 2.16 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 2.3 | 2.0 |
| time in market % | 5.7 | 7.2 |
| buy & hold return % | 105.55 | 222.91 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.23 |
| period | 2005-11-30 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Aroon Trend Onset

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: GLD (base run); screening universe: `etf` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `AroonUp(n)` crosses above `level` AND `AroonDown(n) < 30`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `AroonUp(n) < AroonDown(n)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| n | Aroon length | 25 | 14–50 | 2 |
| level | AroonUp cross level | 70 | 60–90 | 2.5 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 96 | 48–192 | 12 |

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

## Open questions
- none (library conventions agreed across the library sessions and the user's absolute_momentum_monthly choices)

---
Backtest results don't guarantee future performance.
