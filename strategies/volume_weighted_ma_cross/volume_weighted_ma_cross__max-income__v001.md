# volume_weighted_ma_cross: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** ETHUSDT (crypto, 4h)
**Found at:** iteration 231 of optimization.log (2026-11-26T05:03:19Z); written at the checkpoint in iteration 311; backtest.py version `fef9f45d7e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/9 one-step neighbours profitable in-sample (worst neighbour net -2,481.59)
**Range warning:** take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| fast | 18 |
| max_candles | 60 |
| slow | 55 |
| stop_atr | 2.5 |
| take_profit_atr | 6.0 |

```json
{
  "fast": 18,
  "max_candles": 60,
  "slow": 55,
  "stop_atr": 2.5,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 3,431.22 | 2,969.31 |
| return % | 34.31 | 29.69 |
| return %/year | 5.1 | 9.4 |
| gross profit | 34,830.41 | 17,970.18 |
| gross loss | 31,399.19 | 15,000.87 |
| trades | 77 | 44 |
| win rate % | 35.1 | 36.4 |
| avg win | 1,290.02 | 1,123.14 |
| avg loss | -627.98 | -535.75 |
| avg result / trade | 44.56 | 67.48 |
| largest single loss | -1,970.09 | -1,029.71 |
| largest loss % of equity | -10.75 | -6.57 |
| max drawdown | -8,484.27 | -4,494.00 |
| max drawdown % | -39.83 | -27.31 |
| profit factor | 1.11 | 1.20 |
| unusually bad trades | 5 | 0 |
| … threshold (% of equity) | 8.9 | 8.7 |
| time in market % | 14.3 | 13.6 |
| buy & hold return % | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.84 |
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
