# drawdown_from_recent_high: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 28 of optimization.log (2026-11-26T00:02:18Z); written at the checkpoint in iteration 235; backtest.py version `378b9dfe9b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/10 one-step neighbours profitable in-sample (worst neighbour net -435.12)

## Parameters

| parameter | value |
|---|---|
| dip | 13 |
| max_candles | 10 |
| n | 50 |
| stop_atr | 2.25 |
| take_profit_atr | 5.5 |

```json
{
  "dip": 13,
  "max_candles": 10,
  "n": 50,
  "stop_atr": 2.25,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,373.67 | 1,830.79 |
| return % | 23.74 | 18.31 |
| return %/year | 3.9 | 6.0 |
| gross profit | 9,762.94 | 6,612.06 |
| gross loss | 7,389.27 | 4,781.27 |
| trades | 30 | 15 |
| win rate % | 70.0 | 66.7 |
| avg win | 464.90 | 661.21 |
| avg loss | -821.03 | -956.25 |
| avg result / trade | 79.12 | 122.05 |
| largest single loss | -2,391.10 | -1,353.44 |
| largest loss % of equity | -17.86 | -11.15 |
| max drawdown | -5,406.38 | -2,046.64 |
| max drawdown % | -40.22 | -15.42 |
| profit factor | 1.32 | 1.38 |
| unusually bad trades | 3 | 0 |
| … threshold (% of equity) | 11.6 | 14.3 |
| time in market % | 8.3 | 6.7 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.53 |
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
