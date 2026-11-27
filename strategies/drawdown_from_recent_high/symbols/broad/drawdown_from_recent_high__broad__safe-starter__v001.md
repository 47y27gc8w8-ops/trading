# drawdown_from_recent_high__broad: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 844 of optimization.log (2026-11-26T00:05:14Z); written at the checkpoint in iteration 889; backtest.py version `721094815c`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 1,687.25)

## Parameters

| parameter | value |
|---|---|
| dip | 17 |
| max_candles | 12 |
| n | 7 |
| stop_atr | 2.0 |
| take_profit_atr | 0.5 |

```json
{
  "dip": 17,
  "max_candles": 12,
  "n": 7,
  "stop_atr": 2.0,
  "take_profit_atr": 0.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 5,097.94 | 776.18 |
| return % | 50.98 | 7.76 |
| return %/year | 7.7 | 2.6 |
| gross profit | 9,844.73 | 4,135.53 |
| gross loss | 4,746.79 | 3,359.35 |
| trades | 379 | 270 |
| win rate % | 84.2 | 79.6 |
| avg win | 30.86 | 19.24 |
| avg loss | -79.11 | -61.08 |
| avg result / trade | 13.45 | 2.87 |
| largest single loss | -247.49 | -148.84 |
| largest loss % of equity | -26.44 | -27.03 |
| max drawdown | -1,617.06 | -973.20 |
| max drawdown % | -12.65 | -8.60 |
| profit factor | 2.07 | 1.23 |
| unusually bad trades | 1 | 1 |
| … threshold (% of equity) | 36.3 | 37.4 |
| time in market % | 2.2 | 3.1 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.34 |
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
