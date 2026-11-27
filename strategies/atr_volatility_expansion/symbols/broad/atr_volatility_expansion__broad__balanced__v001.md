# atr_volatility_expansion__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 69 of optimization.log (2026-11-25T22:59:47Z); written at the checkpoint in iteration 215; backtest.py version `2d6341ae0f`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 682.06)
**Range warning:** max_candles is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 3.0 |
| max_candles | 96 |
| stop_atr | 3.25 |
| take_profit_atr | 2.5 |

```json
{
  "k": 3.0,
  "max_candles": 96,
  "stop_atr": 3.25,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,336.23 | 1,065.11 |
| return % | 13.36 | 10.65 |
| return %/year | 2.1 | 3.6 |
| gross profit | 8,132.07 | 5,565.48 |
| gross loss | 6,795.84 | 4,500.37 |
| trades | 734 | 604 |
| win rate % | 48.8 | 44.4 |
| avg win | 22.72 | 20.77 |
| avg loss | -18.07 | -13.39 |
| avg result / trade | 1.82 | 1.76 |
| largest single loss | -85.22 | -72.41 |
| largest loss % of equity | -22.73 | -24.60 |
| max drawdown | -449.82 | -551.36 |
| max drawdown % | -4.00 | -4.90 |
| profit factor | 1.20 | 1.24 |
| unusually bad trades | 60 | 52 |
| … threshold (% of equity) | 8.9 | 6.7 |
| time in market % | 1.0 | 1.9 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.66 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Atr Volatility Expansion

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/atr_volatility_expansion.py.

## Idea
Breakout on a wide-range bullish bar that closes near its high.

## Market
- Base symbol: BTCUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: TR > k × ATR(14)[1], C > H[1], C > O and CLV01 > 0.8. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C < EMA(10) at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| k | range expansion multiple | 2 | 1.5–3 (0.25) |
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
