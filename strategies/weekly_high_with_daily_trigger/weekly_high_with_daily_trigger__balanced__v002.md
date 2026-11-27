# weekly_high_with_daily_trigger: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 39098 of optimization.log (2026-11-26T00:46:53Z); written at the checkpoint in iteration 39628; backtest.py version `d0055b4125`
**Replaces:** weekly_high_with_daily_trigger__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 34,518.48)

## Parameters

| parameter | value |
|---|---|
| max_candles | 36 |
| stop_atr | 1.25 |
| take_profit_atr | 8.0 |
| weeks | 6 |

```json
{
  "max_candles": 36,
  "stop_atr": 1.25,
  "take_profit_atr": 8.0,
  "weeks": 6
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 65,232.44 | 3,617.64 |
| return % | 652.32 | 36.18 |
| return %/year | 43.9 | 11.3 |
| gross profit | 92,809.77 | 9,257.76 |
| gross loss | 27,577.33 | 5,640.12 |
| trades | 31 | 17 |
| win rate % | 48.4 | 35.3 |
| avg win | 6,187.32 | 1,542.96 |
| avg loss | -1,723.58 | -512.74 |
| avg result / trade | 2,104.27 | 212.80 |
| largest single loss | -3,405.72 | -687.09 |
| largest loss % of equity | -7.93 | -6.09 |
| max drawdown | -10,441.25 | -3,898.90 |
| max drawdown % | -21.38 | -24.51 |
| profit factor | 3.37 | 1.64 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 10.4 | 7.8 |
| time in market % | 22.4 | 19.8 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Weekly high with daily trigger: testable rules

Source: `original.md` (library spec) plus `../../EXECUTION.md` and `../../INDICATORS.md`.
Implemented in `backtest.py` (adapted copy of `strategies/backtest.py`).

## Setup
- Market: Binance spot BTCUSDT (spec: BTC/USD spot), daily bars built from 1m data (00:00 UTC).
- Periods: trading from 2018-01-01 after a 300-bar warm-up (first tradable day 2018-06-13 for BTC);
  in-sample → 2023-12-31; out-of-sample 2024-01-01 → 2026-11-23 (end frozen at setup).
- Capital 10,000 USD, 100% of equity per trade (user's choice for library specs; the spec's
  risk_fraction sizing is not used), long only, one position per symbol.
- Costs (EXECUTION.md crypto): commission 0.10% per side; market and stop fills 0.10% adverse
  (5 bp half-spread + 5 bp slippage); the take-profit limit fills exactly at its price, commission only.

## Exits common to the library (whichever comes first)
- Time exit at the open after `max_candles` completed held bars (entry bar counts as 1).
- Stop E − stop_atr × ATR(14) of the signal bar, E = entry fill, frozen; intrabar on the low,
  a gap below fills at the open.
- Target E + take_profit_atr × the same ATR, frozen resting limit.
- Stop assumed first when both are touched in one bar.
- The strategy's signal exit (below) on the close, filled at the next open.
- Entry veto: no entry when the signal exit is already true on the signal bar.
- Re-entry only after one fully completed flat bar. ATR(14) = Wilder RMA, fixed.

## Buy (signal at the close of bar t, fill at the open of t+1)
C crosses above the highest high of the `weeks` completed UTC weeks before the week of the bar (C > WH and C[1] ≤ WH[1]), and C > SMA(50).

## Signal exit
C < the lowest low of the 2 completed UTC weeks before the week of the bar.

## Parameters
| name | start | range (step) | hard limits |
|---|---:|---|---|
| weeks | 12 | 4–26 (1) | ≥ 1 |
| stop_atr | 2.0 | 1–4 (0.25) | ≥ 0.25 |
| take_profit_atr | 3.0 | 1.5–6 (0.5) | ≥ 0.5 |
| max_candles | 48 | 24–96 (6) | ≥ 1 |

## Assumptions
1. BTC/USD → Binance BTCUSDT, the project's only crypto venue.
2. 100%-equity sizing instead of risk_fraction (user's choice for library specs, keeps the leaderboard comparable).
3. EMA/RMA seeded with the SMA of the first n values (INDICATORS.md); 300-bar warm-up for every set so all runs start on the same day.
4. Search ranges = the spec's Min/Max; step sizes chosen for a daily grid.
5. Weeks run Monday 00:00 UTC → next Monday, built from the daily bars. 'Preceding completed weeks' = weeks that ended before the week containing the evaluated day; the current week is never included, even on its Sunday close.
6. SMA(50) and the 2-week exit are fixed constants.

---
Backtest results don't guarantee future performance.
