# connors_composite_oversold: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** IWM (etf, 1d)
**Found at:** iteration 113 of optimization.log (2026-11-25T15:34:29Z); written at the checkpoint in iteration 447; backtest.py version `6203944f74`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 4,230.79)

## Parameters

| parameter | value |
|---|---|
| buy | 11 |
| exit | 80.0 |
| max_bars | 18 |
| stop_atr | 2.0 |
| take_profit_atr | 3.0 |

```json
{
  "buy": 11,
  "exit": 80.0,
  "max_bars": 18,
  "stop_atr": 2.0,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 6,333.38 | 5,585.89 |
| return % | 63.33 | 55.86 |
| return %/year | 3.4 | 4.2 |
| gross profit | 9,974.83 | 7,882.20 |
| gross loss | 3,641.45 | 2,296.31 |
| trades | 39 | 30 |
| win rate % | 74.4 | 76.7 |
| avg win | 343.96 | 342.70 |
| avg loss | -364.15 | -328.04 |
| avg result / trade | 162.39 | 186.20 |
| largest single loss | -510.88 | -558.37 |
| largest loss % of equity | -3.60 | -3.47 |
| max drawdown | -879.74 | -1,027.42 |
| max drawdown % | -6.16 | -9.45 |
| profit factor | 2.74 | 3.43 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 6.1 | 5.9 |
| time in market % | 6.8 | 7.0 |
| buy & hold return % | 166.10 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.21 |
| period | 2001-06-08 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Connors Composite Oversold

Source: original.md (library spec, 2026-11-24) plus ../../EXECUTION.md and ../../INDICATORS.md. This file is the testable version; backtest.py implements it.

## Market
- Symbols: IWM (base run); screening universe: `etf` (Yahoo daily, adjusted)
- Timeframe: 1d bars
- Direction: long only, one position per symbol at a time, 100% of equity

## Buy trigger
At the close of bar t (only bar t and earlier):
- `ConnorsRSI(3, 2, 100) < buy` AND `C > SMA(200)`
- veto: not when the sell trigger's close-based condition is also true at t
Order: buy at the open of bar t+1.

## Sell trigger
Close the position at the first of:
- `ConnorsRSI(3, 2, 100) > exit` at a close → sell at the next open
- stop: low ≤ E − stop_atr × A (intrabar; gap below → fill at the open)
- target: high ≥ E + take_profit_atr × A (intrabar; fills at the target)
- time: after max_bars held bars (entry bar = 1) → sell at the next open

E = entry fill, A = ATR(14) of the signal bar, both frozen at entry. If stop and target touch in the same bar, the stop is assumed.

## Parameters
| name | meaning | spec start | range | step |
|---|---|---|---|---|
| buy | entry level | 10 | 5–20 | 1 |
| exit | exit level | 70 | 55–90 | 2.5 |
| stop_atr | stop distance in signal-bar ATR(14) | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance in the same ATR | 3 | 1.5–6 | 0.5 |
| max_bars | time exit (spec: max_candles) | 12 | 6–24 | 2 |

Constraints: `exit > buy`. All other numbers in the triggers are fixed constants of the spec.

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
