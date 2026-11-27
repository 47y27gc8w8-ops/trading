# Anchored VWAP breakout reclaim: testable rules

Source: `original.md` (library spec) plus `../../EXECUTION.md` and `../../INDICATORS.md`.
Implemented in `backtest.py` (adapted copy of `strategies/backtest.py`).

## Setup
- Market: Binance spot BTCUSDT (spec: BTC/USD spot), 1h bars built from 1m data, UTC.
- Periods: trading from 2018-01-01; in-sample 2018-01-01 → 2023-12-31; out-of-sample
  2024-01-01 → 2026-11-23 (end frozen at setup). 400-bar warm-up per symbol.
- Capital 10,000 USD, 100% of equity per trade (user's choice for library specs; the spec's
  risk_fraction sizing is not used), long only, one position per symbol.
- Costs (EXECUTION.md crypto): commission 0.10% per side; market and stop fills move 0.10%
  against us (5 bp half-spread + 5 bp slippage); the take-profit limit fills exactly at its
  price with commission only.

## Buy (signal at the close of bar t, fill at the open of t+1)
All of:
1. Breakout at bar t-2: C[t-2] > max(H[t-2-n] … H[t-3]) (highest high of the n bars before it).
2. Anchor the VWAP at bar t-2: AVWAP(j) = Σ TP·V / Σ V over bars t-2…j, TP = (H+L+C)/3.
3. C[t-1] < AVWAP(t-1).
4. C[t] > AVWAP(t) and C[t] > O[t].
5. ATR(14)[t] > 0 and the stop level below is > 0.
Entry veto (sell condition already true) can't occur: rule 4 excludes it.

## Sell (whichever comes first)
- Time exit: at the open after `max_candles` completed held bars (entry bar counts as 1).
- Stop: E − stop_atr × ATR(14)[t], E = entry fill, frozen. Intrabar on the low; a gap below
  fills at the open.
- Target: E + take_profit_atr × ATR(14)[t], frozen, resting limit.
- If stop and target are touched in the same bar, the stop is assumed.
- Signal exit: a close below the VWAP anchored at the entry's breakout bar (t-2), still
  accumulating from that anchor; fills at the next open.
- Re-entry needs one fully completed flat bar after the exit.

## Parameters
| name | start | range (step) | hard limits |
|---|---:|---|---|
| n | 48 | 24–168 (12) | ≥ 2 |
| stop_atr | 2.0 | 1.0–4.0 (0.25) | ≥ 0.25 |
| take_profit_atr | 3.0 | 1.5–6.0 (0.5) | ≥ 0.5 |
| max_candles | 48 | 24–96 (6) | ≥ 1 |

ATR(14) is fixed (Wilder RMA, SMA seed), not optimized.

## Assumptions
1. Volume: the project's bars carry quote volume Q (USDT). Base volume is approximated per
   1h bar as Q/TP, so the VWAP is Σ Q / Σ (Q/TP). Within one hour the error is negligible.
2. BTC/USD → Binance BTCUSDT (the only crypto venue in the project).
3. 100%-equity sizing instead of risk_fraction (user's choice, keeps the leaderboard comparable).
4. Search ranges = the spec's Min/Max, with step sizes chosen for a 1h grid.
