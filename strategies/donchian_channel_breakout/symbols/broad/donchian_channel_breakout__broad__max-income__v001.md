# donchian_channel_breakout__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 400 of optimization.log (2026-11-25T23:58:14Z); written at the checkpoint in iteration 475; backtest.py version `39d8ffecaf`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 19,557.81)
**Range warning:** stop_atr is at the max of its range, take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| exit_n | 10 |
| max_candles | 72 |
| n | 40 |
| stop_atr | 4.0 |
| take_profit_atr | 6.0 |

```json
{
  "exit_n": 10,
  "max_candles": 72,
  "n": 40,
  "stop_atr": 4.0,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 30,623.96 | 5,185.51 |
| return % | 306.24 | 51.86 |
| return %/year | 28.7 | 15.5 |
| gross profit | 69,591.48 | 18,748.35 |
| gross loss | 38,967.51 | 13,562.84 |
| trades | 504 | 352 |
| win rate % | 44.4 | 42.0 |
| avg win | 310.68 | 126.68 |
| avg loss | -139.17 | -66.48 |
| avg result / trade | 60.76 | 14.73 |
| largest single loss | -3,394.89 | -1,409.71 |
| largest loss % of equity | -28.16 | -25.37 |
| max drawdown | -14,919.75 | -3,586.17 |
| max drawdown % | -35.32 | -25.13 |
| profit factor | 1.79 | 1.38 |
| unusually bad trades | 21 | 15 |
| … threshold (% of equity) | 28.3 | 27.2 |
| time in market % | 14.3 | 18.4 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.54 |
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
