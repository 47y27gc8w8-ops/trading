# atr_distance_dip__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 348 of optimization.log (2026-11-25T22:50:56Z); written at the checkpoint in iteration 887; backtest.py version `1e6b11acb4`
**Replaces:** atr_distance_dip__broad__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 291.74)

## Parameters

| parameter | value |
|---|---|
| distance | 4.5 |
| max_candles | 6 |
| stop_atr | 4.25 |
| take_profit_atr | 2.5 |

```json
{
  "distance": 4.5,
  "max_candles": 6,
  "stop_atr": 4.25,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 618.59 | 997.36 |
| return % | 6.19 | 9.97 |
| return %/year | 1.0 | 3.3 |
| gross profit | 903.50 | 1,254.44 |
| gross loss | 284.91 | 257.08 |
| trades | 75 | 82 |
| win rate % | 66.7 | 70.7 |
| avg win | 18.07 | 21.63 |
| avg loss | -11.40 | -10.71 |
| avg result / trade | 8.25 | 12.16 |
| largest single loss | -91.81 | -40.08 |
| largest loss % of equity | -27.45 | -10.74 |
| max drawdown | -123.73 | -351.44 |
| max drawdown % | -1.20 | -3.48 |
| profit factor | 3.17 | 4.88 |
| unusually bad trades | 5 | 6 |
| … threshold (% of equity) | 3.0 | 4.2 |
| time in market % | 0.1 | 0.2 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 3.27 |
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
