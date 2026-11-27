# tsi_signal_momentum: optimization summary

Updated 2026-11-25T07:09:16Z · backtest.py version `05e7d2b6e7` · 21,994 parameter sets tested with this version (21,994 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2216 | `{"max_candles": 60, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2217 | `{"max_candles": 48, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.14 |
| 2223 | `{"max_candles": 72, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2230 | `{"max_candles": 84, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2235 | `{"max_candles": 96, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2242 | `{"max_candles": 108, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2249 | `{"max_candles": 120, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2256 | `{"max_candles": 132, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2261 | `{"max_candles": 144, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2268 | `{"max_candles": 156, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2273 | `{"max_candles": 168, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2280 | `{"max_candles": 180, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.25 |
| 2287 | `{"max_candles": 192, "signal": 4, "stop_atr": 1.25, "take_profit_atr": 2.5}` | 395.64 | 0.2 | -20.2 | 37.3 | 2,134.19 | 1.8 | -13.2 | 7.46 | 110/84 | 0.14 |

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | HYG | 100% | 1.5 | 4.1 | 5.0 | 2.1 | -0.5 | 11 |
| 2 | EFA | 87% | 0.4 | 2.6 | 6.0 | 0.6 | -3.1 | 0 |
| 3 | GLD | 85% | 2.5 | 5.7 | 8.3 | 1.0 | 0.3 | 18 |
| 4 | XLU | 84% | 0.5 | 2.0 | 6.4 | 0.7 | -1.4 | 5 |
| 5 | SLV | 79% | 2.1 | 5.8 | -0.7 | 1.2 | 1.4 | 48 |
| 6 | VNQ | 79% | 0.8 | 2.9 | 7.6 | 2.5 | -1.1 | 0 |
| 7 | DBC | 74% | 1.0 | 3.6 | -5.8 | 1.1 | 1.9 | 33 |
| 8 | VWO | 56% | 0.1 | 1.8 | 3.3 | 0.3 | -2.7 | 1 |
| 9 | IWDA.AS | 54% | 0.0 | 3.1 | 13.5 | -1.2 | 2.3 | 28 |
| 10 | SOXX | 48% | -0.1 | 2.4 | 3.7 | -0.2 | 2.7 | 19 |
| 11 | IEF | 39% | -0.1 | 0.8 | 5.0 | -0.8 | -0.5 | 3 |
| 12 | VEA | 39% | -0.2 | 1.6 | 0.0 | -0.2 | -3.0 | 0 |
| 13 | GDX | 31% | -1.4 | 5.7 | -10.5 | 1.0 | 2.8 | 5 |
| 14 | VOO | 28% | -0.6 | 1.8 | 13.1 | -0.6 | -0.2 | 7 |
| 15 | VT | 28% | -0.7 | 1.6 | 11.9 | -0.5 | -1.1 | 0 |
| 16 | EEM | 26% | -0.5 | 2.2 | 6.4 | -2.4 | -3.5 | 0 |
| 17 | XLB | 20% | -1.3 | 0.9 | 5.6 | 0.0 | -0.9 | 1 |
| 18 | AGG | 15% | -0.3 | 0.3 | 4.2 | -0.4 | -0.4 | 6 |
| 19 | XLE | 15% | -1.3 | 0.8 | 6.9 | -1.1 | 1.3 | 1 |
| 20 | CSSPX.SW | 13% | -1.0 | 1.6 | 11.6 | -0.8 | 0.8 | 8 |
| 21 | CSNDX.SW | 13% | -1.7 | 1.1 | 16.8 | -1.1 | -0.6 | 0 |
| 22 | DIA | 10% | -0.9 | 0.5 | 4.9 | -0.2 | -0.7 | 0 |
| 23 | TLT | 8% | -0.6 | 0.2 | 6.2 | -1.7 | -0.2 | 3 |
| 24 | ACWI | 7% | -1.7 | 0.8 | 10.8 | -0.7 | -0.8 | 0 |
| 25 | SMH | 7% | -2.2 | 1.3 | 2.1 | -2.1 | 0.3 | 3 |
| 26 | VTI | 3% | -1.1 | 0.5 | 7.1 | -0.5 | -0.1 | 2 |
| 27 | IWM | 3% | -1.2 | 0.1 | 7.8 | -0.8 | -0.8 | 0 |
| 28 | USO | 3% | -1.8 | 0.4 | -14.7 | -2.3 | 3.3 | 2 |
| 29 | SCHD | 3% | -1.8 | 0.5 | 12.4 | -2.6 | 1.1 | 2 |
| 30 | CSPX.L | 3% | -2.1 | 0.4 | 12.1 | -1.4 | 4.2 | 2 |
| 31 | IVV | 2% | -1.2 | 0.1 | 5.3 | -0.7 | -0.1 | 1 |
| 32 | SPY | 2% | -1.2 | 0.0 | 3.9 | -1.3 | 0.2 | 1 |
| 33 | VUG | 2% | -1.4 | 0.2 | 8.3 | -0.9 | 0.5 | 1 |
| 34 | TQQQ | 2% | -5.0 | 0.9 | 45.7 | -6.6 | -3.9 | 0 |
| 35 | SHY | 0% | -0.6 | n/a | 2.1 | -0.6 | -0.8 | 0 |
| 36 | BND | 0% | -0.8 | n/a | 3.8 | -1.0 | -0.5 | 0 |
| 37 | VXUS | 0% | -0.8 | n/a | 4.5 | -3.1 | -0.5 | 0 |
| 38 | LQD | 0% | -1.1 | n/a | 4.9 | -0.9 | -0.7 | 0 |
| 39 | TIP | 0% | -1.1 | n/a | 3.8 | -1.1 | -0.8 | 0 |
| 40 | QQQ | 0% | -1.6 | n/a | 1.6 | -1.6 | -0.8 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 21,994 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
