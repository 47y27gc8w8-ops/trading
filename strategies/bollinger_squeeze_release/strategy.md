# Bollinger Squeeze Release

Source: original.md (120-strategy research library, with ../../EXECUTION.md and ../../INDICATORS.md
as binding conventions), formalized 2026-11-24. This file is the testable version.

## Idea
Volatility contraction precedes expansion: when the Bollinger Band width has just been unusually
narrow and price then closes above the upper band, buy the upside release of the squeeze.

## Market
- Symbols: ETHUSDT (Binance spot; the spec's ETH/USD on a single exchange)
- Timeframe: 4h bars (UTC, aligned to 00:00), built from Binance 1m bars
- Direction: long only, one position at a time

## Indicators (INDICATORS.md)
- BB(20, 2): mid = SMA(C, 20), upper/lower = mid ± 2 · Std(C, 20), population std (ddof = 0)
- BBWidth = 100 · (upper − lower) / mid
- ATR(14) = Wilder RMA of TR (alpha 1/14, SMA seed)
- Percentile: NumPy linear-interpolation 10th percentile of the preceding `lookback` values

## Buy trigger
At the close of bar t (all of):
- `BBWidth[t−1] <= 10th percentile of BBWidth[t−1−lookback … t−2]` (the `lookback` values preceding bar t−1)
- `C[t] > BB_upper(20, 2)[t]`
- entry veto: the signal exit `C[t] < SMA(20)[t]` is not already true (it can't be while C is above the upper band, but it's implemented anyway)
- the signal bar's ATR(14) is > 0 and the resulting stop is > 0, otherwise the signal is skipped

Order: buy at the open of bar t+1.

## Sell trigger
At entry, freeze E = actual entry fill and A = ATR(14) of the signal bar t. Close at the first of:
- **stop**: low ≤ S = E − stop_atr · A (intrabar, active from the entry bar). Fills at min(open, S) less slippage
- **target**: high ≥ T = E + take_profit_atr · A (resting limit). Fills at T exactly: commission only, no slippage
- if stop and target are touched in the same bar → stop first (conservative, no finer data used)
- **signal**: `C < SMA(20)` at a close → sell at the next open
- **time**: after `max_candles` completed held bars (the entry bar counts as 1) → sell at the next open

After an intrabar stop/target exit, the next signal may only come from a later, fully completed
flat bar. After an exit at an open, that bar's close may signal again (entry at the next open).

## Parameters
| name | meaning | description's value | range | step |
|---|---|---|---|---|
| lookback | preceding BBWidth window for the 10th percentile | 120 | 60–252 (hard 20–400) | 12 |
| stop_atr | stop distance in signal-bar ATRs | 2 | 1–4 (hard min 0.5) | 0.25 |
| take_profit_atr | target distance in signal-bar ATRs | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit in held bars | 48 | 24–96 (hard min 1) | 6 |

Fixed constants (the spec says unlisted numbers are fixed): BB 20 / 2, 10th percentile, ATR 14, exit SMA 20.
`risk_fraction` (0.005) isn't tuned: see Setup. Constraints: the spec lists none.
Grid: 17 × 13 × 10 × 13 = 28,730 sets.

## Setup
- Data: ETHUSDT 4h from 2017-08 (warm-up), trading from 2018-01-01 → 2026-11-23 (frozen)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, fractional units allowed
- Fees 0.10% per side, slippage 0.10% per market/stop fill (EXECUTION.md crypto: 10 bp commission,
  5 bp half-spread + 5 bp slippage); target limits pay commission only
- Warm-up: 450 bars of the symbol's own history before it may trade

## Assumptions
- ETH/USD → Binance ETHUSDT: the project's only crypto venue; USDT ≈ USD.
- Sizing 100% of equity instead of risk_fraction · equity / (E − S): the user's decision for library
  specs (2026-11-24), so results compare across the leaderboard. With the spec's 0.5% risk and a
  ~2 ATR stop, a position would be only ~10–25% of equity; returns and drawdowns here are therefore
  much larger than the spec's sizing would give.
- Participation cap (1% of 20-bar volume) is not modeled: 10k USD is far below 1% of ETH 4h volume.
- Signal exit, time exit and the final close use market fills with slippage; the target, as a resting limit, has none.
- Same-bar stop and target → stop first; this ambiguity is reported, not resolved with 1m data.

## Open questions
- none (the spec plus EXECUTION.md/INDICATORS.md cover the rules; sizing per the user's earlier choice)
