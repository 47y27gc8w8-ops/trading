# weekly_high_with_daily_trigger__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 304 of optimization.log (2026-11-26T00:47:55Z); written at the checkpoint in iteration 395; backtest.py version `1d79bb9b82`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 27,041.42)
**Range warning:** stop_atr is at the max of its range, take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 48 |
| stop_atr | 4.0 |
| take_profit_atr | 6.0 |
| weeks | 7 |

```json
{
  "max_candles": 48,
  "stop_atr": 4.0,
  "take_profit_atr": 6.0,
  "weeks": 7
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 33,927.70 | 2,813.67 |
| return % | 339.28 | 28.14 |
| return %/year | 30.6 | 8.9 |
| gross profit | 65,897.17 | 13,746.11 |
| gross loss | 31,969.47 | 10,932.44 |
| trades | 413 | 289 |
| win rate % | 51.1 | 43.2 |
| avg win | 312.31 | 109.97 |
| avg loss | -158.26 | -66.66 |
| avg result / trade | 82.15 | 9.74 |
| largest single loss | -1,269.20 | -986.70 |
| largest loss % of equity | -36.30 | -31.54 |
| max drawdown | -16,972.44 | -3,173.12 |
| max drawdown % | -38.85 | -24.66 |
| profit factor | 2.06 | 1.26 |
| unusually bad trades | 18 | 11 |
| … threshold (% of equity) | 33.0 | 31.0 |
| time in market % | 14.3 | 19.6 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |
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
