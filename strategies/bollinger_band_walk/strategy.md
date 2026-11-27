# Bollinger Band Walk

Source: original.md (strategy library, committed 6946552; spec plus ../../EXECUTION.md and
../../INDICATORS.md). This file is the testable version, formalized 2026-11-24.

## Idea
When price "walks" the upper Bollinger band (several closes in a row above it) while the
20-day average is rising, a volatility-expansion breakout is under way: ride it until the
close falls back below the 10-day average, or a fixed ATR stop / target or time limit hits.

## Market
- Symbol: QQQ (base run; the spec's only named instrument). Screening tests the other ETFs in
  `config/symbols.yaml` (indices `^...` excluded, they aren't tradable).
- Timeframe: 1d exchange sessions, Yahoo daily adjusted bars.
- Direction: long only, one position at a time, no pyramiding, no leverage.

## Indicators (fixed literals, INDICATORS.md)
- BB_upper(20,2) = SMA(C,20) + 2·Std(C,20), population std (ddof 0), includes bar t.
- SMA(20)[5] = the 20-day SMA five completed bars ago.
- ATR(14) = Wilder RMA of TR, SMA seed.

## Buy trigger
At the close of bar t (completed bars only):
- `C[t-k] > BB_upper[t-k]` for every k = 0 … n−1 (each close above its own contemporaneous band)
- AND `SMA(20)[t] > SMA(20)[t-5]`
- AND not `C[t] < SMA(10)[t]` (entry veto: the signal exit must not already be true)
- AND ATR(14)[t] valid, > 0 and the resulting stop > 0 (otherwise skip).
Order: buy at the open of bar t+1. After an intrabar stop/target exit on bar x, the next signal
bar must be > x (one fully flat bar).

## Sell trigger
Freeze at entry: E = entry fill, A = ATR(14) of the signal bar t. The first of:
- signal exit: `C < SMA(10)` at a bar close → sell at the next open
- stop loss: low ≤ S = E − stop_atr·A, intrabar; a gap below S fills at the open (less slippage)
- take profit: resting limit at T = E + take_profit_atr·A; fills at T (also on a favorable gap), no slippage
- time exit: after `max_candles` completed held bars (entry bar = 1) → sell at the next open
Stop and target in the same bar → stop assumed. Stop/target active from the entry bar on.

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | closes in a row above the upper band | 3 | 2–5 (hard 1–10) | 1 |
| stop_atr | stop distance in signal-bar ATRs | 2 | 1–4 (hard min 0.25) | 0.25 |
| take_profit_atr | target distance in the same ATRs | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit, completed held daily bars | 48 | 24–96 (hard min 3) | 6 |

Not searched: `risk_fraction` (sizing, see assumptions); BB(20,2), SMA(20) slope lag 5, exit
SMA(10) and ATR(14) are fixed literals in the spec. Constraints: none given beyond positive
values. Grid: 4 × 13 × 10 × 13 = 6,760 sets.

## Setup
- Data: QQQ daily from 1999-03-10 (warm-up). Trading from 2000-01-01.
- In-sample (tuning): 2000-01-01 → 2015-12-31; out-of-sample (validation only): 2016-01-01 → 2026-11-23 (frozen end).
- Capital 10,000 USD, 100% of equity per trade, fractional shares.
- Costs: 0.05% fee per side, 0.03% slippage per market/stop fill (skill US-ETF defaults; the spec's
  1 bp commission + 4 bp half-spread/slippage totals about the same per round trip). The limit
  target pays the fee only.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction·equity/(E−S) sizing. This is
  the user's choice for this library (2026-11-24). Summaries report the position size that would
  have kept the worst drawdown near 10%. risk_fraction is therefore not optimized.
- Fills on Yahoo adjusted prices: the project has no separate raw execution series.
- Participation cap (1% of 20-day volume) ignored: 10k USD is far below it for these ETFs.
- Screening uses the same US-ETF costs for the Swiss/European listings (.SW/.L/.AS), which slightly
  understates their costs (~0.07% per round trip at ~2 trades per year).
- Cost stress tests (2×, 4×) and library-wide multiple-testing control are not run by the optimizer;
  noted as open validation steps for later.

## Open questions
- none (sizing answered by the user's 2026-11-24 library-wide choice)
