# volume_climax_rejection__broad: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 855 of optimization.log (2026-11-26T05:02:57Z); written at the checkpoint in iteration 889; backtest.py version `9a6709b1fe`
**Replaces:** volume_climax_rejection__broad__max-income__v001.md
**Robustness:** 7/8 one-step neighbours profitable in-sample (worst neighbour net -290.00)

## Parameters

| parameter | value |
|---|---|
| max_candles | 6 |
| rvol | 2.5 |
| stop_atr | 4.5 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 6,
  "rvol": 2.5,
  "stop_atr": 4.5,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,288.86 | 913.84 |
| return % | 12.89 | 9.14 |
| return %/year | 2.1 | 3.1 |
| gross profit | 2,402.99 | 2,384.18 |
| gross loss | 1,114.13 | 1,470.33 |
| trades | 231 | 272 |
| win rate % | 61.9 | 71.3 |
| avg win | 16.80 | 12.29 |
| avg loss | -12.66 | -18.85 |
| avg result / trade | 5.58 | 3.36 |
| largest single loss | -68.65 | -78.41 |
| largest loss % of equity | -16.39 | -20.88 |
| max drawdown | -276.47 | -974.35 |
| max drawdown % | -2.54 | -9.41 |
| profit factor | 2.16 | 1.62 |
| unusually bad trades | 21 | 24 |
| … threshold (% of equity) | 4.8 | 5.8 |
| time in market % | 0.2 | 0.6 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.48 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Volume Climax Rejection

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/volume_climax_rejection.py.

## Idea
Capitulation reversal: volume spike to a new 20-bar low, close near the high.

## Market
- Base symbol: BTCUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: V > rvol × SMA(V,20)[1], L < LL(L,20)[1], CLV01 > 0.75 and C > O. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C ≥ SMA(20) at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| rvol | volume multiple | 3 | 2–5 (0.25) |
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
