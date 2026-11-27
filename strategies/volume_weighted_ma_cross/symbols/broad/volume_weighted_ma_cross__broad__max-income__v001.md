# volume_weighted_ma_cross__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 68 of optimization.log (2026-11-26T05:04:57Z); written at the checkpoint in iteration 284; backtest.py version `92af7b89e5`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 3,668.26)

## Parameters

| parameter | value |
|---|---|
| fast | 10 |
| max_candles | 87 |
| slow | 70 |
| stop_atr | 2.0 |
| take_profit_atr | 10.5 |

```json
{
  "fast": 10,
  "max_candles": 87,
  "slow": 70,
  "stop_atr": 2.0,
  "take_profit_atr": 10.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 11,562.10 | 1,666.46 |
| return % | 115.62 | 16.66 |
| return %/year | 13.9 | 5.5 |
| gross profit | 44,875.40 | 16,585.46 |
| gross loss | 33,313.30 | 14,919.00 |
| trades | 1,913 | 1,372 |
| win rate % | 26.9 | 26.5 |
| avg win | 87.31 | 45.69 |
| avg loss | -23.81 | -14.79 |
| avg result / trade | 6.04 | 1.21 |
| largest single loss | -229.16 | -216.89 |
| largest loss % of equity | -8.76 | -15.64 |
| max drawdown | -5,424.86 | -2,899.54 |
| max drawdown % | -26.59 | -24.34 |
| profit factor | 1.35 | 1.11 |
| unusually bad trades | 79 | 39 |
| … threshold (% of equity) | 9.3 | 8.4 |
| time in market % | 11.3 | 15.5 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.39 |
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
