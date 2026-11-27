# mfi_momentum_confirmation__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 397 of optimization.log (2026-11-26T04:53:21Z); written at the checkpoint in iteration 921; backtest.py version `1f39108d70`
**Replaces:** mfi_momentum_confirmation__broad__balanced__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 1,248.70)

## Parameters

| parameter | value |
|---|---|
| level | 90.0 |
| max_candles | 96 |
| stop_atr | 5.25 |
| take_profit_atr | 5.5 |

```json
{
  "level": 90.0,
  "max_candles": 96,
  "stop_atr": 5.25,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,976.03 | 687.16 |
| return % | 29.76 | 6.87 |
| return %/year | 4.5 | 2.3 |
| gross profit | 7,929.22 | 4,199.75 |
| gross loss | 4,953.19 | 3,512.59 |
| trades | 361 | 265 |
| win rate % | 45.4 | 43.0 |
| avg win | 48.35 | 36.84 |
| avg loss | -25.14 | -23.26 |
| avg result / trade | 8.24 | 2.59 |
| largest single loss | -117.87 | -107.06 |
| largest loss % of equity | -14.89 | -15.46 |
| max drawdown | -526.63 | -710.75 |
| max drawdown % | -4.11 | -6.53 |
| profit factor | 1.60 | 1.20 |
| unusually bad trades | 35 | 26 |
| … threshold (% of equity) | 10.5 | 10.7 |
| time in market % | 1.3 | 2.0 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Mfi Momentum Confirmation

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/mfi_momentum_confirmation.py.

## Idea
Money-flow momentum confirmed by a 20-bar high breakout.

## Market
- Base symbol: ETHUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: MFI(14) crosses above level and C > HH(H,20)[1]. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: MFI(14) < 50 at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| level | MFI cross level | 70 | 60–85 (2.5) |
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
