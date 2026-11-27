# trix_zero_trend__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 1d)
**Found at:** iteration 209 of optimization.log (2026-11-26T00:34:24Z); written at the checkpoint in iteration 413; backtest.py version `a6e29e3860`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 4,798.30)

## Parameters

| parameter | value |
|---|---|
| max_candles | 132 |
| n | 13 |
| stop_atr | 2.75 |
| take_profit_atr | 3.5 |

```json
{
  "max_candles": 132,
  "n": 13,
  "stop_atr": 2.75,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 5,959.75 | 1,052.07 |
| return % | 59.60 | 10.52 |
| return %/year | 8.8 | 3.5 |
| gross profit | 11,992.67 | 6,248.14 |
| gross loss | 6,032.93 | 5,196.07 |
| trades | 219 | 211 |
| win rate % | 56.2 | 46.5 |
| avg win | 97.50 | 63.76 |
| avg loss | -62.84 | -45.98 |
| avg result / trade | 27.21 | 4.99 |
| largest single loss | -390.58 | -166.54 |
| largest loss % of equity | -24.37 | -33.70 |
| max drawdown | -1,188.46 | -1,925.80 |
| max drawdown % | -7.70 | -15.90 |
| profit factor | 1.99 | 1.20 |
| unusually bad trades | 5 | 8 |
| … threshold (% of equity) | 25.1 | 22.7 |
| time in market % | 5.5 | 8.9 |
| buy & hold return % | 368.58 | 81.24 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.40 |
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
