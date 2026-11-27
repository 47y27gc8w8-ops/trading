# multi_horizon_roc_vote: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT (crypto, 1d)
**Found at:** iteration 928 of optimization.log (2026-11-26T00:05:38Z); written at the checkpoint in iteration 6253; backtest.py version `866a9ad9a7`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/6 one-step neighbours profitable in-sample (worst neighbour net -2,007.40)

## Parameters

| parameter | value |
|---|---|
| max_candles | 60 |
| stop_atr | 4.0 |
| take_profit_atr | 2.5 |
| votes | 4 |

```json
{
  "max_candles": 60,
  "stop_atr": 4.0,
  "take_profit_atr": 2.5,
  "votes": 4
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,867.42 | 882.02 |
| return % | 28.67 | 8.82 |
| return %/year | 4.7 | 3.0 |
| gross profit | 15,846.33 | 5,443.25 |
| gross loss | 12,978.90 | 4,561.23 |
| trades | 20 | 11 |
| win rate % | 65.0 | 63.6 |
| avg win | 1,218.95 | 777.61 |
| avg loss | -1,854.13 | -1,140.31 |
| avg result / trade | 143.37 | 80.18 |
| largest single loss | -3,063.87 | -1,865.30 |
| largest loss % of equity | -24.00 | -15.01 |
| max drawdown | -5,702.96 | -2,320.64 |
| max drawdown % | -38.92 | -18.51 |
| profit factor | 1.22 | 1.19 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 30.6 | 19.4 |
| time in market % | 17.9 | 26.4 |
| buy & hold return % | 547.53 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.64 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Multi-horizon ROC vote: testable rules

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
At least `votes` of ROC(21), ROC(63), ROC(126), ROC(252) are > 0, and that was not true on the previous bar.

## Signal exit
At most one of the four ROC values is > 0.

## Parameters
| name | start | range (step) | hard limits |
|---|---:|---|---|
| votes | 3 | 2–4 (1) | 2–4 |
| stop_atr | 2.0 | 1–4 (0.25) | ≥ 0.25 |
| take_profit_atr | 3.0 | 1.5–6 (0.5) | ≥ 0.5 |
| max_candles | 96 | 48–192 (12) | ≥ 1 |

## Assumptions
1. BTC/USD → Binance BTCUSDT, the project's only crypto venue.
2. 100%-equity sizing instead of risk_fraction (user's choice for library specs, keeps the leaderboard comparable).
3. EMA/RMA seeded with the SMA of the first n values (INDICATORS.md); 300-bar warm-up for every set so all runs start on the same day.
4. Search ranges = the spec's Min/Max; step sizes chosen for a daily grid.
5. ROC horizons 21/63/126/252 and the 'at most one' exit are fixed constants.

---
Backtest results don't guarantee future performance.
