# drawdown_from_recent_high: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 741 of optimization.log (2026-11-26T00:02:28Z); written at the checkpoint in iteration 1268; backtest.py version `378b9dfe9b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 633.09)

## Parameters

| parameter | value |
|---|---|
| dip | 13 |
| max_candles | 2 |
| n | 12 |
| stop_atr | 3.5 |
| take_profit_atr | 4.5 |

```json
{
  "dip": 13,
  "max_candles": 2,
  "n": 12,
  "stop_atr": 3.5,
  "take_profit_atr": 4.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,295.41 | 1,235.02 |
| return % | 32.95 | 12.35 |
| return %/year | 5.3 | 4.1 |
| gross profit | 7,953.69 | 1,418.37 |
| gross loss | 4,658.27 | 183.35 |
| trades | 29 | 5 |
| win rate % | 62.1 | 60.0 |
| avg win | 441.87 | 472.79 |
| avg loss | -423.48 | -91.67 |
| avg result / trade | 113.63 | 247.00 |
| largest single loss | -930.66 | -151.24 |
| largest loss % of equity | -7.27 | -1.33 |
| max drawdown | -2,682.81 | -279.18 |
| max drawdown % | -20.91 | -2.44 |
| profit factor | 1.71 | 7.74 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 8.2 | 2.0 |
| time in market % | 2.7 | 0.8 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.78 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Drawdown from recent high: testable rules

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
100 × (C / HH(C, n) − 1) < −dip and C > SMA(200).

## Signal exit
C ≥ EMA(20).

## Parameters
| name | start | range (step) | hard limits |
|---|---:|---|---|
| n | 20 | 10–60 (5) | ≥ 2 |
| dip | 8 | 4–15 (1) | 0.5–90 |
| stop_atr | 2.0 | 1–4 (0.25) | ≥ 0.25 |
| take_profit_atr | 3.0 | 1.5–6 (0.5) | ≥ 0.5 |
| max_candles | 12 | 6–24 (2) | ≥ 1 |

## Assumptions
1. BTC/USD → Binance BTCUSDT, the project's only crypto venue.
2. 100%-equity sizing instead of risk_fraction (user's choice for library specs, keeps the leaderboard comparable).
3. EMA/RMA seeded with the SMA of the first n values (INDICATORS.md); 300-bar warm-up for every set so all runs start on the same day.
4. Search ranges = the spec's Min/Max; step sizes chosen for a daily grid.
5. SMA(200) and EMA(20) are fixed constants (not in the spec's parameter table).

---
Backtest results don't guarantee future performance.
