# trix_zero_trend__broad: safe-starter v003

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 1548 of optimization.log (2026-11-26T00:56:50Z); written at the checkpoint in iteration 1549; backtest.py version `a6e29e3860`
**Replaces:** trix_zero_trend__broad__safe-starter__v002.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,655.98)

## Parameters

| parameter | value |
|---|---|
| max_candles | 108 |
| n | 33 |
| stop_atr | 2.5 |
| take_profit_atr | 4.0 |

```json
{
  "max_candles": 108,
  "n": 33,
  "stop_atr": 2.5,
  "take_profit_atr": 4.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,045.60 | 866.10 |
| return % | 30.46 | 8.66 |
| return %/year | 4.9 | 2.9 |
| gross profit | 10,009.12 | 4,919.48 |
| gross loss | 6,963.52 | 4,053.38 |
| trades | 201 | 139 |
| win rate % | 46.3 | 46.0 |
| avg win | 107.62 | 76.87 |
| avg loss | -64.48 | -54.05 |
| avg result / trade | 15.15 | 6.23 |
| largest single loss | -213.19 | -123.31 |
| largest loss % of equity | -14.88 | -36.47 |
| max drawdown | -3,062.36 | -1,716.14 |
| max drawdown % | -20.83 | -14.77 |
| profit factor | 1.44 | 1.21 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 33.5 | 30.3 |
| time in market % | 6.5 | 8.9 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.59 |
| period | 2018-06-13 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# TRIX zero-line trend: testable rules

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
TRIX(n) crosses above zero (TRIX > 0 and TRIX[1] ≤ 0) and C > SMA(100).

## Signal exit
TRIX(n) < 0.

## Parameters
| name | start | range (step) | hard limits |
|---|---:|---|---|
| n | 15 | 9–30 (1) | ≥ 2 |
| stop_atr | 2.0 | 1–4 (0.25) | ≥ 0.25 |
| take_profit_atr | 3.0 | 1.5–6 (0.5) | ≥ 0.5 |
| max_candles | 96 | 48–192 (12) | ≥ 1 |

## Assumptions
1. BTC/USD → Binance BTCUSDT, the project's only crypto venue.
2. 100%-equity sizing instead of risk_fraction (user's choice for library specs, keeps the leaderboard comparable).
3. EMA/RMA seeded with the SMA of the first n values (INDICATORS.md); 300-bar warm-up for every set so all runs start on the same day.
4. Search ranges = the spec's Min/Max; step sizes chosen for a daily grid.
5. TRIX(n) = 100 × one-bar ROC of EMA(EMA(EMA(C, n), n), n). SMA(100) is a fixed constant.

---
Backtest results don't guarantee future performance.
