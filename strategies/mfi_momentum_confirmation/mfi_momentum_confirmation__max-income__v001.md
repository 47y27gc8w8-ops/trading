# mfi_momentum_confirmation: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** ETHUSDT (crypto, 4h)
**Found at:** iteration 16477 of optimization.log (2026-11-26T04:45:50Z); written at the checkpoint in iteration 36581; backtest.py version `bd5de2f5c1`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 5,675.90)

## Parameters

| parameter | value |
|---|---|
| level | 75.0 |
| max_candles | 33 |
| stop_atr | 2.5 |
| take_profit_atr | 6.5 |

```json
{
  "level": 75.0,
  "max_candles": 33,
  "stop_atr": 2.5,
  "take_profit_atr": 6.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 13,339.94 | 1,188.24 |
| return % | 133.40 | 11.88 |
| return %/year | 15.4 | 4.0 |
| gross profit | 51,005.71 | 12,027.06 |
| gross loss | 37,665.77 | 10,838.81 |
| trades | 80 | 40 |
| win rate % | 48.8 | 35.0 |
| avg win | 1,307.84 | 859.08 |
| avg loss | -918.68 | -416.88 |
| avg result / trade | 166.75 | 29.71 |
| largest single loss | -3,290.06 | -783.30 |
| largest loss % of equity | -10.83 | -5.38 |
| max drawdown | -10,024.44 | -4,533.90 |
| max drawdown % | -32.36 | -28.84 |
| profit factor | 1.35 | 1.11 |
| unusually bad trades | 9 | 0 |
| … threshold (% of equity) | 6.7 | 7.4 |
| time in market % | 8.8 | 8.6 |
| buy & hold return % | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Mfi Momentum Confirmation

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/mfi_momentum_confirmation.py.

## Idea
Money-flow momentum confirmed by a 20-bar high breakout.

## Market
- Base symbol: ETHUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: MFI(14) crosses above level and C > HH(H,20)[1]. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: MFI(14) < 50 at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| level | MFI cross level | 70 | 60–85 (2.5) |
| stop_atr | stop distance × ATR(14) | 2 | 1–4 (0.25) |
| take_profit_atr | target distance × ATR(14) | 3 | 1.5–6 (0.5) |
| max_candles | held bars before time exit | 48 | 24–96 (9) |

`risk_fraction` (spec 0.005) is not used: the user chose 100% of equity per trade (2026-11-24).

## Setup
- In-sample 2018-01-01 → 2024-01-01, out-of-sample 2024-01-01 → 2026-11-23 (frozen end)
- Warm-up: 1000 bars of each coin's own history before it may trade (≥ 5× the longest recursive period)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fee 0.10% per side, slippage 0.10% per fill (spec: 10 bp commission, 5 bp half-spread + 5 bp slippage)

## Assumptions
- Volume = Binance quote volume (USDT), the only volume the loader provides; the spec says base-unit volume. Ratios (RVOL, MFI, VWMA weights) are nearly unaffected.
- Prices from one venue (Binance spot USDT), as the spec requires a single exchange.

---
Backtest results don't guarantee future performance.
