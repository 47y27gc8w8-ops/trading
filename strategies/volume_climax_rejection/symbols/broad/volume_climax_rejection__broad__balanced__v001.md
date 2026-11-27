# volume_climax_rejection__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 90 of optimization.log (2026-11-26T04:59:33Z); written at the checkpoint in iteration 272; backtest.py version `9a6709b1fe`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 147.20)
**Range warning:** max_candles is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 24 |
| rvol | 4.25 |
| stop_atr | 1.25 |
| take_profit_atr | 1.5 |

```json
{
  "max_candles": 24,
  "rvol": 4.25,
  "stop_atr": 1.25,
  "take_profit_atr": 1.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 246.87 | 95.41 |
| return % | 2.47 | 0.95 |
| return %/year | 0.4 | 0.3 |
| gross profit | 389.23 | 389.82 |
| gross loss | 142.37 | 294.41 |
| trades | 31 | 34 |
| win rate % | 71.0 | 50.0 |
| avg win | 17.69 | 22.93 |
| avg loss | -15.82 | -17.32 |
| avg result / trade | 7.96 | 2.81 |
| largest single loss | -30.51 | -26.46 |
| largest loss % of equity | -9.46 | -8.20 |
| max drawdown | -57.27 | -130.24 |
| max drawdown % | -0.57 | -1.27 |
| profit factor | 2.73 | 1.32 |
| unusually bad trades | 1 | 0 |
| … threshold (% of equity) | 8.3 | 12.6 |
| time in market % | 0.0 | 0.1 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.81 |
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
