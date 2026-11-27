# donchian_channel_breakout__broad: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 1248 of optimization.log (2026-11-26T00:01:42Z); written at the checkpoint in iteration 1370; backtest.py version `39d8ffecaf`
**Replaces:** donchian_channel_breakout__broad__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 44,366.82)

## Parameters

| parameter | value |
|---|---|
| exit_n | 20 |
| max_candles | 37 |
| n | 22 |
| stop_atr | 3.25 |
| take_profit_atr | 7.0 |

```json
{
  "exit_n": 20,
  "max_candles": 37,
  "n": 22,
  "stop_atr": 3.25,
  "take_profit_atr": 7.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 71,619.90 | 4,930.08 |
| return % | 716.20 | 49.30 |
| return %/year | 46.0 | 14.8 |
| gross profit | 131,153.98 | 22,730.70 |
| gross loss | 59,534.08 | 17,800.62 |
| trades | 606 | 463 |
| win rate % | 49.3 | 41.0 |
| avg win | 438.64 | 119.64 |
| avg loss | -193.92 | -65.20 |
| avg result / trade | 118.18 | 10.65 |
| largest single loss | -3,881.89 | -1,196.30 |
| largest loss % of equity | -14.62 | -25.68 |
| max drawdown | -14,840.11 | -5,034.49 |
| max drawdown % | -21.14 | -38.61 |
| profit factor | 2.20 | 1.28 |
| unusually bad trades | 7 | 5 |
| … threshold (% of equity) | 32.0 | 31.2 |
| time in market % | 21.3 | 30.9 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.32 |
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
