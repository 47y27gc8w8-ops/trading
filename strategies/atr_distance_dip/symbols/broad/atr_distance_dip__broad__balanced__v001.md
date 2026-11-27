# atr_distance_dip__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 39 of optimization.log (2026-11-25T22:49:25Z); written at the checkpoint in iteration 225; backtest.py version `1e6b11acb4`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 428.80)
**Range warning:** max_candles is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| distance | 3.75 |
| max_candles | 6 |
| stop_atr | 3.0 |
| take_profit_atr | 5.0 |

```json
{
  "distance": 3.75,
  "max_candles": 6,
  "stop_atr": 3.0,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 822.06 | 776.04 |
| return % | 8.22 | 7.76 |
| return %/year | 1.3 | 2.6 |
| gross profit | 2,551.09 | 2,192.80 |
| gross loss | 1,729.03 | 1,416.76 |
| trades | 259 | 239 |
| win rate % | 61.0 | 58.2 |
| avg win | 16.15 | 15.78 |
| avg loss | -17.12 | -14.17 |
| avg result / trade | 3.17 | 3.25 |
| largest single loss | -109.52 | -58.29 |
| largest loss % of equity | -30.31 | -16.51 |
| max drawdown | -458.88 | -993.19 |
| max drawdown % | -4.26 | -9.59 |
| profit factor | 1.48 | 1.55 |
| unusually bad trades | 25 | 34 |
| … threshold (% of equity) | 6.2 | 5.3 |
| time in market % | 0.4 | 0.7 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.96 |
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
