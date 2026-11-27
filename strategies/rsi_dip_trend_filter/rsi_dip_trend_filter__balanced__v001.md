# rsi_dip_trend_filter: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT (crypto, 4h)
**Found at:** iteration 757 of optimization.log (2026-11-24T22:14:36Z); written at the checkpoint in iteration 758; backtest.py version `028e59b880`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/12 one-step neighbours profitable in-sample (worst neighbour net -1,673.93)

## Parameters

| parameter | value |
|---|---|
| buy | 34 |
| exit | 65 |
| max_candles | 14 |
| n | 19 |
| stop_atr | 1.75 |
| take_profit_atr | 3.5 |

```json
{
  "buy": 34,
  "exit": 65,
  "max_candles": 14,
  "n": 19,
  "stop_atr": 1.75,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 880.77 | 243.41 |
| return % | 8.81 | 2.43 |
| return %/year | 1.4 | 0.8 |
| gross profit | 4,632.84 | 1,201.92 |
| gross loss | 3,752.07 | 958.50 |
| trades | 20 | 8 |
| win rate % | 45.0 | 50.0 |
| avg win | 514.76 | 300.48 |
| avg loss | -341.10 | -239.63 |
| avg result / trade | 44.04 | 30.43 |
| largest single loss | -631.79 | -309.31 |
| largest loss % of equity | -6.32 | -3.06 |
| max drawdown | -2,253.33 | -1,371.00 |
| max drawdown % | -22.35 | -12.77 |
| profit factor | 1.24 | 1.25 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 7.1 | 4.6 |
| time in market % | 1.3 | 0.9 |
| buy & hold return % | 313.33 | 44.90 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.58 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Rsi Dip Trend Filter

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/rsi_dip_trend_filter.py.

## Idea
RSI oversold dip above the 200-bar SMA.

## Market
- Base symbol: BTCUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: RSI(n) < buy and C > SMA(200). Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: RSI(n) > exit at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| n | RSI length | 14 | 7–21 (1) |
| buy | oversold level | 30 | 20–40 (2) |
| exit | exit level | 55 | 45–70 (5) |
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
- Spec lists BTC and ETH as alternatives: BTC is the base run, ETH and the rest come from screening.
- buy < exit enforced.

---
Backtest results don't guarantee future performance.
