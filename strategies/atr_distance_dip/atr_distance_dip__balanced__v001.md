# atr_distance_dip: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** ETHUSDT (crypto, 4h)
**Found at:** iteration 18305 of optimization.log (2026-11-25T22:48:11Z); written at the checkpoint in iteration 20811; backtest.py version `841fa309ff`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 753.58)

## Parameters

| parameter | value |
|---|---|
| distance | 3.5 |
| max_candles | 14 |
| stop_atr | 4.25 |
| take_profit_atr | 2.5 |

```json
{
  "distance": 3.5,
  "max_candles": 14,
  "stop_atr": 4.25,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,015.22 | 434.21 |
| return % | 30.15 | 4.34 |
| return %/year | 4.6 | 1.5 |
| gross profit | 5,505.57 | 3,764.53 |
| gross loss | 2,490.36 | 3,330.32 |
| trades | 20 | 16 |
| win rate % | 55.0 | 62.5 |
| avg win | 500.51 | 376.45 |
| avg loss | -276.71 | -555.05 |
| avg result / trade | 150.76 | 27.14 |
| largest single loss | -817.26 | -1,288.87 |
| largest loss % of equity | -6.17 | -10.81 |
| max drawdown | -3,297.49 | -1,740.71 |
| max drawdown % | -28.45 | -14.42 |
| profit factor | 2.21 | 1.13 |
| unusually bad trades | 4 | 1 |
| … threshold (% of equity) | 2.2 | 8.5 |
| time in market % | 1.8 | 2.5 |
| buy & hold return % | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.33 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Atr Distance Dip

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/atr_distance_dip.py.

## Idea
Dip buying in an uptrend: price stretched below EMA(50) in ATR units.

## Market
- Base symbol: ETHUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: (C − EMA(50)) / ATR(14) < −distance and EMA(50) > EMA(200). Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C ≥ EMA(20) at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| distance | stretch in ATRs | 2 | 1–4 (0.25) |
| stop_atr | stop distance × ATR(14) | 2 | 1–4 (0.25) |
| take_profit_atr | target distance × ATR(14) | 3 | 1.5–6 (0.5) |
| max_candles | held bars before time exit | 12 | 6–24 (2) |

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
