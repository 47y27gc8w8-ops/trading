# weekly_high_with_daily_trigger: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 194 of optimization.log (2026-11-26T00:36:37Z); written at the checkpoint in iteration 38911; backtest.py version `d0055b4125`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 18,723.06)

## Parameters

| parameter | value |
|---|---|
| max_candles | 36 |
| stop_atr | 1.75 |
| take_profit_atr | 6.0 |
| weeks | 8 |

```json
{
  "max_candles": 36,
  "stop_atr": 1.75,
  "take_profit_atr": 6.0,
  "weeks": 8
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 26,030.46 | 2,108.13 |
| return % | 260.30 | 21.08 |
| return %/year | 26.0 | 6.8 |
| gross profit | 47,248.23 | 6,647.29 |
| gross loss | 21,217.77 | 4,539.16 |
| trades | 27 | 14 |
| win rate % | 55.6 | 42.9 |
| avg win | 3,149.88 | 1,107.88 |
| avg loss | -1,768.15 | -567.40 |
| avg result / trade | 964.09 | 150.58 |
| largest single loss | -2,864.34 | -709.92 |
| largest loss % of equity | -10.98 | -5.26 |
| max drawdown | -6,958.28 | -3,540.85 |
| max drawdown % | -35.66 | -23.31 |
| profit factor | 2.23 | 1.46 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 16.5 | 10.2 |
| time in market % | 23.5 | 22.9 |
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
