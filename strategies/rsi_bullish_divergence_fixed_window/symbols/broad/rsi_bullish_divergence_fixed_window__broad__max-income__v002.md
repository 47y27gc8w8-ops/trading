# rsi_bullish_divergence_fixed_window__broad: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d)
**Found at:** iteration 1240 of optimization.log (2026-11-25T10:51:34Z); written at the checkpoint in iteration 1663; backtest.py version `32e35a6a14`
**Replaces:** rsi_bullish_divergence_fixed_window__broad__max-income__v001.md
**Robustness:** 9/9 one-step neighbours profitable in-sample (worst neighbour net 2,159.98)

## Parameters

| parameter | value |
|---|---|
| gap | 0 |
| max_candles | 34 |
| n | 14 |
| stop_atr | 5.0 |
| take_profit_atr | 5.0 |

```json
{
  "gap": 0,
  "max_candles": 34,
  "n": 14,
  "stop_atr": 5.0,
  "take_profit_atr": 5.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,503.85 | 1,430.91 |
| return % | 25.04 | 14.31 |
| return %/year | 1.4 | 1.2 |
| gross profit | 3,916.12 | 3,323.75 |
| gross loss | 1,412.28 | 1,892.84 |
| trades | 589 | 534 |
| win rate % | 75.9 | 70.0 |
| avg win | 8.76 | 8.89 |
| avg loss | -9.95 | -11.83 |
| avg result / trade | 4.25 | 2.68 |
| largest single loss | -41.71 | -158.20 |
| largest loss % of equity | -19.13 | -33.74 |
| max drawdown | -337.29 | -595.73 |
| max drawdown % | -2.74 | -5.00 |
| profit factor | 2.77 | 1.76 |
| unusually bad trades | 17 | 53 |
| … threshold (% of equity) | 8.4 | 6.1 |
| time in market % | 5.2 | 6.9 |
| buy & hold return % | 95.12 | 303.60 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.88 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# rsi_bullish_divergence_fixed_window: formalized rules

Source: `original.md` (120-strategy research library, plus `../../EXECUTION.md` and `../../INDICATORS.md`).

## Buy (evaluated at bar t's close, filled at bar t+1's open)
C < LL(C,n)[1] AND RSI(14) > LL(RSI(14),n)[1] + gap AND C > SMA(200).

Entry veto: no buy when the signal exit below is already true on the signal bar, or ATR(14) is not yet defined.

## Sell (OR conditions; the earliest executable exit wins)
- Signal exit: RSI(14) > 60. Filled at the next open.
- Stop loss: entry fill - stop_atr x ATR(14) of the signal bar, frozen at entry, active from the entry bar (intrabar on low; a gap below fills at the open less slippage). Entry skipped if ATR <= 0 or stop <= 0.
- Take profit: resting limit at entry fill + take_profit_atr x the same ATR; fills at its level, also on a favourable gap, no slippage. If stop and target are both touched in one bar, the stop is assumed.
- Time exit: after max_candles completed held bars (entry bar = 1), sell at the next open.
- After an intrabar stop/target exit, the next signal must come from a fully completed flat bar.

## Parameters
| parameter | start | min | max | step | hard_min | hard_max |
|---|---|---|---|---|---|---|
| n | 20 | 10 | 50 | 2 | 2 |  |
| gap | 5.0 | 2.0 | 15.0 | 1.0 | 0.0 |  |
| stop_atr | 2.0 | 1.0 | 4.0 | 0.25 | 0.25 |  |
| take_profit_atr | 3.0 | 1.5 | 6.0 | 0.5 | 0.5 |  |
| max_candles | 12 | 6 | 24 | 2 | 1 |  |

`risk_fraction` from the spec is not used (see assumptions). Every other numeric literal in the triggers is a fixed constant.

## Setup
- Data: Yahoo daily adjusted OHLCV (`data/etf/1d`), base symbol GLD (spec: GLD; ETF).
- In-sample 2000-01-01 to 2016-01-01 (excl.), out-of-sample 2016-01-01 to 2026-11-23. Warm-up 300 bars per symbol.
- Capital 10,000 USD, 100% of equity per trade, long only, one position per symbol.
- Costs: fee 0.05% per side, slippage 0.03% per market/stop fill.
- Screening universe: `etf`.

## Assumptions
- Sizing: 100% of equity per trade instead of the spec's risk_fraction sizing (user's library-wide choice, so results compare on the leaderboard; its "size for ~10% DD" column gives a risk-scaled size).
- Costs: library convention fee 0.05% + slippage 0.03% per fill (more conservative than the spec's 1 bp + 2 bp + 2 bp).
- In-sample/out-of-sample split at 2016-01-01: library convention for Yahoo strategies.
- Indicators follow INDICATORS.md (Wilder RSI/ATR with SMA seed, EMA with SMA seed, population std, PR excluding t).
- Adjusted closes are used for signals and fills (the project data has no separate raw execution series).
- With the spec's start values (n=20, gap=5) the buy condition never fires on GLD in-sample (0 trades); it fires 0-7 times over the whole history of SPY/QQQ/AAPL. The optimizer has to find smaller gaps/windows, or the broad basket has to supply the trades.

---
Backtest results don't guarantee future performance.
