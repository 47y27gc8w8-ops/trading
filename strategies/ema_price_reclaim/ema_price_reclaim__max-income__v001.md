# ema_price_reclaim: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT (crypto, 4h)
**Found at:** iteration 24456 of optimization.log (2026-11-26T02:39:22Z); written at the checkpoint in iteration 26460; backtest.py version `2f1c7c7526`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -164.24)

## Parameters

| parameter | value |
|---|---|
| max_candles | 48 |
| n | 140 |
| stop_atr | 0.75 |
| take_profit_atr | 5.5 |

```json
{
  "max_candles": 48,
  "n": 140,
  "stop_atr": 0.75,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 6,621.05 | 779.68 |
| return % | 66.21 | 7.80 |
| return %/year | 9.0 | 2.6 |
| gross profit | 18,549.77 | 3,864.15 |
| gross loss | 11,928.72 | 3,084.47 |
| trades | 81 | 31 |
| win rate % | 21.0 | 19.4 |
| avg win | 1,091.16 | 644.03 |
| avg loss | -186.39 | -123.38 |
| avg result / trade | 81.74 | 25.15 |
| largest single loss | -514.56 | -205.05 |
| largest loss % of equity | -4.38 | -1.76 |
| max drawdown | -3,285.85 | -2,502.36 |
| max drawdown % | -25.76 | -19.44 |
| profit factor | 1.55 | 1.25 |
| unusually bad trades | 7 | 0 |
| … threshold (% of equity) | 2.7 | 2.1 |
| time in market % | 5.3 | 5.7 |
| buy & hold return % | 313.33 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.29 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Ema Price Reclaim

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/ema_price_reclaim.py.

## Idea
Close reclaims a rising EMA.

## Market
- Base symbol: BTCUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: C crosses above EMA(n) and EMA(n) > EMA(n)[5]. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C < EMA(n) at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| n | EMA length | 100 | 50–200 (10) |
| stop_atr | stop distance × ATR(14) | 2 | 1–4 (0.25) |
| take_profit_atr | target distance × ATR(14) | 3 | 1.5–6 (0.5) |
| max_candles | held bars before time exit | 96 | 48–192 (18) |

`risk_fraction` (spec 0.005) is not used: the user chose 100% of equity per trade (2026-11-24).

## Setup
- In-sample 2018-01-01 → 2024-01-01, out-of-sample 2024-01-01 → 2026-11-23 (frozen end)
- Warm-up: 1000 bars of each coin's own history before it may trade (≥ 5× the longest recursive period)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fee 0.10% per side, slippage 0.10% per fill (spec: 10 bp commission, 5 bp half-spread + 5 bp slippage)

## Assumptions
- Volume = Binance quote volume (USDT), the only volume the loader provides; the spec says base-unit volume. Ratios (RVOL, MFI, VWMA weights) are nearly unaffected.
- Prices from one venue (Binance spot USDT), as the spec requires a single exchange.
- Spec lists BTC and ETH: BTC is the base run, the rest comes from screening.

---
Backtest results don't guarantee future performance.
