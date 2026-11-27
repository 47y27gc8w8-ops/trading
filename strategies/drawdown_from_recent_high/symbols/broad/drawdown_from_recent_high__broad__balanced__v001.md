# drawdown_from_recent_high__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 232 of optimization.log (2026-11-26T00:03:31Z); written at the checkpoint in iteration 233; backtest.py version `721094815c`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/8 one-step neighbours profitable in-sample (worst neighbour net -2,374.27)

## Parameters

| parameter | value |
|---|---|
| dip | 14 |
| max_candles | 10 |
| n | 10 |
| stop_atr | 2.75 |
| take_profit_atr | 1.5 |

```json
{
  "dip": 14,
  "max_candles": 10,
  "n": 10,
  "stop_atr": 2.75,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 43.74 | 652.63 |
| return % | 0.44 | 6.53 |
| return %/year | 0.1 | 2.2 |
| gross profit | 10,166.24 | 7,553.16 |
| gross loss | 10,122.50 | 6,900.52 |
| trades | 507 | 436 |
| win rate % | 63.1 | 65.8 |
| avg win | 31.77 | 26.32 |
| avg loss | -54.13 | -46.31 |
| avg result / trade | 0.09 | 1.50 |
| largest single loss | -375.09 | -253.75 |
| largest loss % of equity | -40.36 | -31.27 |
| max drawdown | -3,335.74 | -1,734.30 |
| max drawdown % | -26.99 | -14.78 |
| profit factor | 1.00 | 1.09 |
| unusually bad trades | 37 | 47 |
| … threshold (% of equity) | 24.8 | 16.9 |
| time in market % | 5.0 | 8.6 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 27.62 |
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
