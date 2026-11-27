# donchian_channel_breakout: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 395 of optimization.log (2026-11-25T23:56:35Z); written at the checkpoint in iteration 838; backtest.py version `c132114b2c`
**Replaces:** donchian_channel_breakout__balanced__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 17,526.50)

## Parameters

| parameter | value |
|---|---|
| exit_n | 25 |
| max_candles | 42 |
| n | 65 |
| stop_atr | 1.25 |
| take_profit_atr | 4.5 |

```json
{
  "exit_n": 25,
  "max_candles": 42,
  "n": 65,
  "stop_atr": 1.25,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 31,705.32 | 2,503.92 |
| return % | 317.05 | 25.04 |
| return %/year | 29.4 | 8.0 |
| gross profit | 43,248.24 | 6,880.18 |
| gross loss | 11,542.93 | 4,376.25 |
| trades | 26 | 15 |
| win rate % | 53.9 | 33.3 |
| avg win | 3,089.16 | 1,376.04 |
| avg loss | -961.91 | -437.63 |
| avg result / trade | 1,219.44 | 166.93 |
| largest single loss | -1,658.05 | -577.79 |
| largest loss % of equity | -6.86 | -4.49 |
| max drawdown | -5,119.28 | -2,338.74 |
| max drawdown % | -33.92 | -16.51 |
| profit factor | 3.75 | 1.57 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 11.2 | 8.3 |
| time in market % | 16.9 | 14.7 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |
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
