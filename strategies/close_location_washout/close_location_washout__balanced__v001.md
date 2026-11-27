# close_location_washout: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** IWM (etf, 1d)
**Found at:** iteration 132 of optimization.log (2026-11-25T16:00:01Z); written at the checkpoint in iteration 27352; backtest.py version `58d6d19b6c`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 2,014.37)

## Parameters

| parameter | value |
|---|---|
| clv | 0.05 |
| max_bars | 22 |
| stop_atr | 2.0 |
| take_profit_atr | 5.5 |

```json
{
  "clv": 0.05,
  "max_bars": 22,
  "stop_atr": 2.0,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,730.56 | 591.93 |
| return % | 27.31 | 5.92 |
| return %/year | 1.7 | 0.5 |
| gross profit | 7,460.12 | 3,598.95 |
| gross loss | 4,729.57 | 3,007.02 |
| trades | 92 | 41 |
| win rate % | 68.5 | 63.4 |
| avg win | 118.41 | 138.42 |
| avg loss | -163.09 | -200.47 |
| avg result / trade | 29.68 | 14.44 |
| largest single loss | -436.21 | -546.28 |
| largest loss % of equity | -3.64 | -5.04 |
| max drawdown | -845.63 | -1,230.68 |
| max drawdown % | -7.47 | -10.85 |
| profit factor | 1.58 | 1.20 |
| unusually bad trades | 10 | 5 |
| … threshold (% of equity) | 2.0 | 2.1 |
| time in market % | 5.2 | 3.1 |
| buy & hold return % | 166.10 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.32 |
| period | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Close Location Washout

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: IWM (base run); screening universe: `etf` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `CLV01 < clv` AND `ROC(1) < −1` (%) AND `C > SMA(200)`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `CLV01 > 0.8` OR `C > SMA(5)` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| clv | max close location (0–1) | 0.10 | 0.05–0.25 | 0.01 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 12 | 6–24 | 2 |

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
