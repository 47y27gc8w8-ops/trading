# mfi_momentum_confirmation__broad: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 78 of optimization.log (2026-11-26T04:52:01Z); written at the checkpoint in iteration 251; backtest.py version `1f39108d70`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/5 one-step neighbours profitable in-sample (worst neighbour net 584.52)
**Range warning:** stop_atr is at the max of its range, max_candles is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| level | 85.0 |
| max_candles | 24 |
| stop_atr | 4.0 |
| take_profit_atr | 3.5 |

```json
{
  "level": 85.0,
  "max_candles": 24,
  "stop_atr": 4.0,
  "take_profit_atr": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,441.70 | 1,465.57 |
| return % | 14.42 | 14.66 |
| return %/year | 2.3 | 4.8 |
| gross profit | 12,246.42 | 7,635.65 |
| gross loss | 10,804.72 | 6,170.08 |
| trades | 811 | 581 |
| win rate % | 46.7 | 49.6 |
| avg win | 32.31 | 26.51 |
| avg loss | -25.01 | -21.06 |
| avg result / trade | 1.78 | 2.52 |
| largest single loss | -187.55 | -88.13 |
| largest loss % of equity | -14.82 | -17.07 |
| max drawdown | -1,420.93 | -855.21 |
| max drawdown % | -11.35 | -7.34 |
| profit factor | 1.13 | 1.24 |
| unusually bad trades | 80 | 41 |
| … threshold (% of equity) | 10.3 | 10.3 |
| time in market % | 2.3 | 3.3 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.10 |
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
