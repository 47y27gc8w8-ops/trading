# bollinger_keltner_compression_release__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 3117 of optimization.log (2026-11-25T23:32:28Z); written at the checkpoint in iteration 3118; backtest.py version `f9522f49d9`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/8 one-step neighbours profitable in-sample (worst neighbour net -1,171.13)

## Parameters

| parameter | value |
|---|---|
| k | 1.7 |
| max_candles | 33 |
| stop_atr | 3.0 |
| take_profit_atr | 5.5 |

```json
{
  "k": 1.7,
  "max_candles": 33,
  "stop_atr": 3.0,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 184.63 | 1,059.20 |
| return % | 1.85 | 10.59 |
| return %/year | 0.3 | 3.5 |
| gross profit | 24,554.23 | 13,277.78 |
| gross loss | 24,369.59 | 12,218.58 |
| trades | 2,120 | 1,424 |
| win rate % | 31.0 | 34.5 |
| avg win | 37.37 | 27.04 |
| avg loss | -16.66 | -13.10 |
| avg result / trade | 0.09 | 0.74 |
| largest single loss | -122.09 | -70.52 |
| largest loss % of equity | -14.21 | -8.81 |
| max drawdown | -4,954.11 | -2,495.65 |
| max drawdown % | -33.26 | -18.41 |
| profit factor | 1.01 | 1.09 |
| unusually bad trades | 194 | 108 |
| … threshold (% of equity) | 7.6 | 6.1 |
| time in market % | 5.7 | 8.4 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 11.42 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Bollinger Keltner Compression Release

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/bollinger_keltner_compression_release.py.

## Idea
Squeeze release: Bollinger Bands leave the Keltner Channel upward after a compression.

## Market
- Base symbol: BTCUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: on t−1 BB(20,2) fully inside KC(20,10,k); now not fully inside, C > BB_upper(20,2) and ROC(10) > 0. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C < EMA(20) at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| k | Keltner multiplier | 1.5 | 1–2 (0.1) |
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
- 'Fully inside' = BB_upper ≤ KC_upper and BB_lower ≥ KC_lower.

---
Backtest results don't guarantee future performance.
