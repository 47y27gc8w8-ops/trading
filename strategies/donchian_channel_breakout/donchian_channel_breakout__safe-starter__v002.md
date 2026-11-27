# donchian_channel_breakout: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 344 of optimization.log (2026-11-25T23:56:34Z); written at the checkpoint in iteration 839; backtest.py version `c132114b2c`
**Replaces:** donchian_channel_breakout__safe-starter__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 10,282.60)

## Parameters

| parameter | value |
|---|---|
| exit_n | 15 |
| max_candles | 36 |
| n | 45 |
| stop_atr | 1.5 |
| take_profit_atr | 5.0 |

```json
{
  "exit_n": 15,
  "max_candles": 36,
  "n": 45,
  "stop_atr": 1.5,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 14,551.39 | 3,344.95 |
| return % | 145.51 | 33.45 |
| return %/year | 17.6 | 10.5 |
| gross profit | 32,513.78 | 8,349.70 |
| gross loss | 17,962.39 | 5,004.75 |
| trades | 36 | 16 |
| win rate % | 38.9 | 43.8 |
| avg win | 2,322.41 | 1,192.81 |
| avg loss | -816.47 | -556.08 |
| avg result / trade | 404.21 | 209.06 |
| largest single loss | -1,598.51 | -647.76 |
| largest loss % of equity | -8.17 | -4.63 |
| max drawdown | -4,687.72 | -2,977.53 |
| max drawdown % | -21.38 | -19.86 |
| profit factor | 1.81 | 1.67 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 11.6 | 10.5 |
| time in market % | 21.1 | 18.4 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.60 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Donchian channel breakout: testable rules

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
C > HH(H, n)[1] and C[1] <= HH(H, n)[2] (close crosses above the highest high of the n preceding bars).

## Signal exit
C < LL(L, exit_n)[1] (close below the lowest low of the exit_n preceding bars).

## Parameters
| name | start | range (step) | hard limits |
|---|---:|---|---|
| n | 55 | 20–100 (5) | ≥ 2 |
| exit_n | 20 | 5–40 (5) | ≥ 1, < n |
| stop_atr | 2.0 | 1–4 (0.25) | ≥ 0.25 |
| take_profit_atr | 3.0 | 1.5–6 (0.5) | ≥ 0.5 |
| max_candles | 48 | 24–96 (6) | ≥ 1 |

## Assumptions
1. BTC/USD → Binance BTCUSDT, the project's only crypto venue.
2. 100%-equity sizing instead of risk_fraction (user's choice for library specs, keeps the leaderboard comparable).
3. EMA/RMA seeded with the SMA of the first n values (INDICATORS.md); 300-bar warm-up for every set so all runs start on the same day.
4. Search ranges = the spec's Min/Max; step sizes chosen for a daily grid.
5. Constraint exit_n < n (spec).

---
Backtest results don't guarantee future performance.
