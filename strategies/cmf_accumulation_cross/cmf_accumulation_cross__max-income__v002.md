# cmf_accumulation_cross: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** XLF (etf, 1d)
**Found at:** iteration 443 of optimization.log (2026-11-25T15:43:26Z); written at the checkpoint in iteration 956; backtest.py version `5ae30db648`
**Replaces:** cmf_accumulation_cross__max-income__v001.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 714.27)

## Parameters

| parameter | value |
|---|---|
| level | 0.07 |
| max_bars | 48 |
| n | 28 |
| stop_atr | 1.0 |
| take_profit_atr | 3.0 |

```json
{
  "level": 0.07,
  "max_bars": 48,
  "n": 28,
  "stop_atr": 1.0,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 7,055.15 | 2,399.80 |
| return % | 70.55 | 24.00 |
| return %/year | 3.3 | 2.0 |
| gross profit | 19,444.92 | 8,605.18 |
| gross loss | 12,389.78 | 6,205.39 |
| trades | 77 | 53 |
| win rate % | 40.3 | 37.7 |
| avg win | 627.26 | 430.26 |
| avg loss | -269.34 | -188.04 |
| avg result / trade | 91.63 | 45.28 |
| largest single loss | -1,060.81 | -337.97 |
| largest loss % of equity | -6.17 | -2.68 |
| max drawdown | -1,912.25 | -2,960.86 |
| max drawdown % | -10.08 | -20.39 |
| profit factor | 1.57 | 1.39 |
| unusually bad trades | 5 | 0 |
| … threshold (% of equity) | 2.7 | 3.4 |
| time in market % | 11.7 | 13.2 |
| buy & hold return % | 41.29 | 257.92 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.60 |
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
