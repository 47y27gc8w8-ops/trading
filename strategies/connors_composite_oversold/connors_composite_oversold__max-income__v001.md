# connors_composite_oversold: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** IWM (etf, 1d)
**Found at:** iteration 426 of optimization.log (2026-11-25T15:34:34Z); written at the checkpoint in iteration 446; backtest.py version `6203944f74`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 10,369.52)
**Range warning:** max_bars is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| buy | 16 |
| exit | 85.0 |
| max_bars | 6 |
| stop_atr | 3.25 |
| take_profit_atr | 3.0 |

```json
{
  "buy": 16,
  "exit": 85.0,
  "max_bars": 6,
  "stop_atr": 3.25,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 15,403.17 | 8,911.61 |
| return % | 154.03 | 89.12 |
| return %/year | 6.6 | 6.0 |
| gross profit | 29,302.54 | 16,039.34 |
| gross loss | 13,899.37 | 7,127.73 |
| trades | 102 | 69 |
| win rate % | 67.7 | 68.1 |
| avg win | 424.67 | 341.26 |
| avg loss | -421.19 | -323.99 |
| avg result / trade | 151.01 | 129.15 |
| largest single loss | -1,250.70 | -1,055.87 |
| largest loss % of equity | -5.77 | -6.03 |
| max drawdown | -3,222.89 | -2,171.07 |
| max drawdown % | -14.29 | -19.20 |
| profit factor | 2.11 | 2.25 |
| unusually bad trades | 9 | 4 |
| … threshold (% of equity) | 3.1 | 4.7 |
| time in market % | 15.3 | 13.2 |
| buy & hold return % | 166.10 | 175.35 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.91 |
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
