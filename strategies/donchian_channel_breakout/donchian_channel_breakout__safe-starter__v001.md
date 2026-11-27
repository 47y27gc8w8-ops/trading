# donchian_channel_breakout: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 57 of optimization.log (2026-11-25T23:56:30Z); written at the checkpoint in iteration 272; backtest.py version `c132114b2c`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 12,397.88)

## Parameters

| parameter | value |
|---|---|
| exit_n | 20 |
| max_candles | 72 |
| n | 60 |
| stop_atr | 1.75 |
| take_profit_atr | 4.5 |

```json
{
  "exit_n": 20,
  "max_candles": 72,
  "n": 60,
  "stop_atr": 1.75,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 26,463.40 | 2,356.12 |
| return % | 264.63 | 23.56 |
| return %/year | 26.2 | 7.6 |
| gross profit | 44,531.79 | 7,541.98 |
| gross loss | 18,068.40 | 5,185.85 |
| trades | 27 | 15 |
| win rate % | 55.6 | 40.0 |
| avg win | 2,968.79 | 1,257.00 |
| avg loss | -1,505.70 | -576.21 |
| avg result / trade | 980.13 | 157.07 |
| largest single loss | -2,781.00 | -712.18 |
| largest loss % of equity | -9.49 | -7.67 |
| max drawdown | -8,169.00 | -2,559.39 |
| max drawdown % | -25.09 | -18.06 |
| profit factor | 2.46 | 1.45 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 15.9 | 10.7 |
| time in market % | 21.2 | 21.4 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |
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
