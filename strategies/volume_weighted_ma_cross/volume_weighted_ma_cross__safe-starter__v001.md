# volume_weighted_ma_cross: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** ETHUSDT (crypto, 4h)
**Found at:** iteration 1440 of optimization.log (2026-11-26T05:03:53Z); written at the checkpoint in iteration 1941; backtest.py version `fef9f45d7e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 14,428.54)
**Range warning:** take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 11 |
| max_candles | 96 |
| slow | 70 |
| stop_atr | 1.25 |
| take_profit_atr | 10.5 |

```json
{
  "fast": 11,
  "max_candles": 96,
  "slow": 70,
  "stop_atr": 1.25,
  "take_profit_atr": 10.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 66,309.86 | 3,275.29 |
| return % | 663.10 | 32.75 |
| return %/year | 41.0 | 10.3 |
| gross profit | 130,853.68 | 16,652.42 |
| gross loss | 64,543.82 | 13,377.14 |
| trades | 78 | 49 |
| win rate % | 30.8 | 20.4 |
| avg win | 5,452.24 | 1,665.24 |
| avg loss | -1,195.26 | -343.00 |
| avg result / trade | 850.13 | 66.84 |
| largest single loss | -3,736.40 | -730.41 |
| largest loss % of equity | -4.83 | -4.00 |
| max drawdown | -21,994.69 | -6,642.91 |
| max drawdown % | -25.39 | -33.35 |
| profit factor | 2.03 | 1.25 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 5.4 | 4.4 |
| time in market % | 13.2 | 13.3 |
| buy & hold return % | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.25 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Volume Weighted Ma Cross

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/volume_weighted_ma_cross.py.

## Idea
VWMA crossover on above-average volume.

## Market
- Base symbol: ETHUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: VWMA(fast) crosses above VWMA(slow) and V > SMA(V,20)[1]. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: VWMA(fast) < VWMA(slow) at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| fast | fast VWMA | 10 | 5–20 (1) |
| slow | slow VWMA | 30 | 25–60 (5) |
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
- fast < slow enforced.

---
Backtest results don't guarantee future performance.
