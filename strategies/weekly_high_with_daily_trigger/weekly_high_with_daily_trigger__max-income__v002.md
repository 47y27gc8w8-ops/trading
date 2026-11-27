# weekly_high_with_daily_trigger: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 39088 of optimization.log (2026-11-26T00:46:53Z); written at the checkpoint in iteration 39627; backtest.py version `d0055b4125`
**Replaces:** weekly_high_with_daily_trigger__max-income__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 41,298.34)

## Parameters

| parameter | value |
|---|---|
| max_candles | 36 |
| stop_atr | 1.75 |
| take_profit_atr | 8.5 |
| weeks | 6 |

```json
{
  "max_candles": 36,
  "stop_atr": 1.75,
  "take_profit_atr": 8.5,
  "weeks": 6
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 88,696.64 | 4,331.17 |
| return % | 886.97 | 43.31 |
| return %/year | 51.1 | 13.2 |
| gross profit | 126,230.57 | 9,542.91 |
| gross loss | 37,533.93 | 5,211.74 |
| trades | 27 | 15 |
| win rate % | 59.3 | 46.7 |
| avg win | 7,889.41 | 1,363.27 |
| avg loss | -3,412.18 | -651.47 |
| avg result / trade | 3,285.06 | 288.74 |
| largest single loss | -6,275.92 | -810.20 |
| largest loss % of equity | -9.49 | -5.35 |
| max drawdown | -17,649.84 | -3,695.54 |
| max drawdown % | -30.68 | -21.32 |
| profit factor | 3.36 | 1.83 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 14.8 | 10.3 |
| time in market % | 26.2 | 26.5 |
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
