# ADX Directional Break

Source: original.md (strategy library, committed 6946552; spec plus ../../EXECUTION.md and
../../INDICATORS.md). This file is the testable version, formalized 2026-11-24.

## Idea
Buy when buyers take over directional control (DI+ crosses above DI−) while the market is
already trending strongly (ADX above a threshold). Get out when sellers regain control, or at a
fixed ATR stop / target, or after a maximum holding time.

## Market
- Symbols: BTCUSDT (base run), SOLUSDT (spec's alternative target, separate run). Binance spot,
  USDT quote = the single preselected venue. Screening tests the other coins.
- Timeframe: 4h bars, UTC-aligned (00:00, 04:00, ...), built from Binance 1m bars.
- Direction: long only, one position per symbol at a time, no pyramiding, no leverage.

## Indicators (period 14 fixed, INDICATORS.md)
- TR = max(H−L, |H−C[1]|, |L−C[1]|); ATR = RMA(TR,14). RMA = Wilder (alpha 1/14), SMA seed.
- +DM = H−H[1] if it is > L[1]−L and > 0, else 0; −DM symmetric.
- DI+ = 100·RMA(+DM,14)/ATR, DI− likewise; DX = 100·|DI+ − DI−|/(DI+ + DI−); ADX = RMA(DX,14).
  Zero denominators give 0.

## Buy trigger
At the close of bar t (completed bars only):
- `DI+[t] > DI−[t]` AND `DI+[t−1] <= DI−[t−1]` (cross above) AND `ADX[t] > adx`
- and ATR[t] valid, > 0, and the resulting stop > 0 (otherwise skip).
Order: buy at the open of bar t+1. Entry veto (exit already true) can't occur: the cross implies DI+ > DI−.
After an intrabar stop/target exit on bar x, the next signal bar must be > x (one fully flat bar).

## Sell trigger
Freeze at entry: E = entry fill, A = ATR(14) of the signal bar t. The first of:
- signal exit: `DI+ < DI−` at a bar close → sell at the next open
- stop loss: low ≤ S = E − stop_atr·A, intrabar; a gap below S fills at the open (less slippage)
- take profit: resting limit at T = E + take_profit_atr·A; fills at T (also on a favorable gap), no slippage
- time exit: after `max_candles` completed held bars (entry bar = 1) → sell at the next open
Stop and target in the same bar → stop assumed. Stop/target active from the entry bar on.

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| adx | minimum ADX(14) at the signal bar | 25 | 15–35 (hard 5–60) | 1 |
| stop_atr | stop distance in signal-bar ATRs | 2 | 1–4 (hard min 0.25) | 0.25 |
| take_profit_atr | target distance in the same ATRs | 3 | 1.5–6 (hard min 0.5) | 0.5 |
| max_candles | time exit, completed held 4h bars | 96 | 48–192 (hard min 6) | 12 |

Not searched: `risk_fraction` (sizing, see assumptions); DI/ADX/ATR period 14 (fixed literal in
the spec). Constraints: none given beyond positive values. Grid: 21 × 13 × 10 × 13 = 35,490 sets.

## Setup
- Data: BTCUSDT 4h from 2017-08 (warm-up), SOLUSDT from 2020-08. Trading from 2018-01-01.
- In-sample (tuning): 2018-01-01 → 2023-12-31; out-of-sample (validation only): 2024-01-01 → 2026-11-23 (frozen end).
- Capital 10,000 USD, 100% of equity per trade, fractional units.
- Costs (EXECUTION.md crypto scenario): commission 0.10% per side; half-spread 5 bps + slippage
  5 bps = 0.10% adverse on every market/stop fill; the limit target pays commission only.

## Assumptions
- Binance spot USDT pairs stand in for "BTC/USD, SOL/USD": the only crypto venue in the project.
- Sizing: 100% of equity per trade instead of the spec's risk_fraction·equity/(E−S) sizing. This is
  the user's choice for this library (2026-11-24). Summaries report the position size that would
  have kept the worst drawdown near 10%. risk_fraction is therefore not optimized.
- Participation cap (1% of 20-bar volume) ignored: 10k USD on BTC/SOL is far below it.
- 4h buckets on UTC epoch boundaries; the last incomplete bucket is dropped by the loader.
- Cost stress tests (2×, 4×) and library-wide multiple-testing control are not run by the optimizer;
  noted as open validation steps for later.

## Open questions
- none (sizing answered by the user's 2026-11-24 library-wide choice)
