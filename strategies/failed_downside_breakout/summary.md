# failed_downside_breakout: optimization summary

Updated 2026-11-26T00:51:44Z · backtest.py version `f82364249e` · 2,547 parameter sets tested with this version (2,547 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: IWM (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1493 | `{"max_candles": 28, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1494 | `{"max_candles": 24, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.33 |
| 1498 | `{"max_candles": 32, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1504 | `{"max_candles": 36, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1510 | `{"max_candles": 40, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1516 | `{"max_candles": 44, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1522 | `{"max_candles": 48, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1528 | `{"max_candles": 52, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1534 | `{"max_candles": 56, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1540 | `{"max_candles": 60, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1546 | `{"max_candles": 64, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1552 | `{"max_candles": 68, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1558 | `{"max_candles": 72, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1564 | `{"max_candles": 76, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1570 | `{"max_candles": 80, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1576 | `{"max_candles": 84, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1582 | `{"max_candles": 88, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1588 | `{"max_candles": 92, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.43 |
| 1594 | `{"max_candles": 96, "n": 10, "stop_atr": 2.25, "take_profit_atr": 2.0}` | 1,204.02 | 0.8 | -27.6 | 66.1 | 1,925.39 | 1.6 | -17.9 | 2.17 | 112/69 | 0.33 |
| 1955 | `{"max_candles": 24, "n": 10, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 765.67 | 0.5 | -27.4 | 65.8 | 1,460.29 | 1.3 | -17.2 | 2.57 | 111/68 | 0.40 |
| 1960 | `{"max_candles": 28, "n": 10, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 765.67 | 0.5 | -27.4 | 65.8 | 1,460.29 | 1.3 | -17.2 | 2.57 | 111/68 | 0.50 |
| 1965 | `{"max_candles": 32, "n": 10, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 765.67 | 0.5 | -27.4 | 65.8 | 1,460.29 | 1.3 | -17.2 | 2.57 | 111/68 | 0.50 |
| 1970 | `{"max_candles": 36, "n": 10, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 765.67 | 0.5 | -27.4 | 65.8 | 1,460.29 | 1.3 | -17.2 | 2.57 | 111/68 | 0.50 |
| 1975 | `{"max_candles": 40, "n": 10, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 765.67 | 0.5 | -27.4 | 65.8 | 1,460.29 | 1.3 | -17.2 | 2.57 | 111/68 | 0.50 |
| 1980 | `{"max_candles": 44, "n": 10, "stop_atr": 2.25, "take_profit_atr": 6.0}` | 765.67 | 0.5 | -27.4 | 65.8 | 1,460.29 | 1.3 | -17.2 | 2.57 | 111/68 | 0.50 |

(13 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

65 of 74 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ^VIX | 100% | 16.0 | 27.5 | 1.2 | 15.2 | 36.5 | 61 |
| 2 | XLU | 95% | 1.3 | 2.5 | 6.0 | 1.2 | -0.2 | 48 |
| 3 | XLE | 90% | 1.4 | 3.9 | 6.7 | 1.9 | 2.4 | 54 |
| 4 | VIG | 85% | 2.0 | 4.6 | 7.0 | 0.6 | 0.9 | 26 |
| 5 | XLV | 80% | 0.9 | 2.3 | 7.1 | 2.3 | 0.1 | 44 |
| 6 | RSP | 70% | 0.8 | 3.0 | 9.4 | 2.7 | 2.0 | 35 |
| 7 | VUG | 70% | 0.5 | 2.9 | 8.1 | 0.5 | 1.0 | 24 |
| 8 | LQD | 69% | 0.2 | 0.7 | 5.4 | 0.2 | -2.1 | 0 |
| 9 | GLD | 66% | 1.6 | 2.5 | 8.5 | 0.8 | 2.6 | 40 |
| 10 | ACWI | 54% | 1.1 | 5.5 | 4.7 | 4.6 | 0.9 | 0 |
| 11 | ^DJI | 52% | 0.0 | 1.2 | 7.5 | -0.8 | 0.3 | 13 |
| 12 | ^GSPC | 51% | 0.0 | 0.8 | 7.4 | 0.2 | 1.4 | 19 |
| 13 | EEM | 49% | 0.1 | 4.0 | 7.9 | -0.8 | 1.1 | 21 |
| 14 | ^RUT | 49% | -0.0 | 1.3 | 7.5 | 0.4 | 1.4 | 7 |
| 15 | TLT | 43% | -0.2 | 0.9 | 6.7 | -1.4 | -2.7 | 0 |
| 16 | XLB | 43% | -0.3 | 3.0 | 5.4 | 2.7 | 0.9 | 13 |
| 17 | VTI | 38% | -0.3 | 1.0 | 7.3 | -0.3 | 1.6 | 8 |
| 18 | CSSMI.SW | 36% | 0.4 | 3.2 | 3.3 | 0.8 | 1.0 | 16 |
| 19 | SPY | 36% | -0.2 | 1.1 | 9.3 | -0.3 | 3.0 | 22 |
| 20 | VEA | 34% | -0.4 | 3.9 | -0.3 | -0.8 | 2.8 | 21 |
| 21 | TQQQ | 31% | 9.4 | 15.6 | 58.3 | 5.7 | -6.0 | 0 |
| 22 | BND | 31% | 0.1 | 0.5 | 4.3 | 0.2 | -0.7 | 0 |
| 23 | GDX | 28% | -1.3 | 1.9 | -8.7 | -2.4 | 0.7 | 15 |
| 24 | IEF | 26% | -0.1 | 0.7 | 5.2 | -0.3 | -1.8 | 0 |
| 25 | VNQ | 26% | -0.7 | 2.2 | 8.5 | 1.0 | 1.1 | 10 |
| 26 | VXUS | 25% | 3.1 | 7.2 | 1.2 | 3.0 | 0.4 | 8 |
| 27 | VWO | 25% | -1.6 | 3.2 | 4.5 | -2.0 | 1.4 | 7 |
| 28 | VOO | 23% | 1.9 | 3.3 | 11.9 | 1.4 | 2.9 | 12 |
| 29 | VT | 23% | 0.2 | 2.3 | 11.4 | -2.4 | -0.0 | 6 |
| 30 | CSSPX.SW | 21% | 1.8 | 2.3 | 13.6 | 1.9 | 0.4 | 3 |
| 31 | CSNDX.SW | 18% | 1.8 | 4.0 | 18.0 | -0.0 | 1.0 | 5 |
| 32 | XLY | 18% | -1.9 | 1.5 | 7.4 | -3.5 | -1.8 | 3 |
| 33 | XLF | 18% | -2.6 | 2.2 | 1.5 | -3.1 | 2.9 | 11 |
| 34 | ^STOXX50E | 16% | -1.3 | 2.3 | -3.0 | -1.6 | -0.1 | 3 |
| 35 | ^SSMI | 15% | -1.0 | 0.2 | 5.9 | -1.9 | -0.1 | 4 |
| 36 | IWM | 13% | -0.9 | 0.8 | 7.5 | -2.6 | -2.9 | 0 |
| 37 | IVV | 13% | -1.1 | 1.2 | 4.6 | -1.5 | 2.8 | 8 |
| 38 | SLV | 13% | -2.2 | 1.5 | 2.0 | -3.5 | 6.9 | 8 |
| 39 | AGG | 11% | -0.4 | 0.1 | 4.0 | -0.5 | -0.1 | 0 |
| 40 | DIA | 11% | -0.8 | 0.5 | 6.2 | -0.1 | 2.0 | 7 |

(25 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [failed_downside_breakout__broad__max-income__v002.md](symbols/broad/failed_downside_breakout__broad__max-income__v002.md) | 8.6 | 6.7 | 6.7 | -18.9 | 71.0 | 4078/3384 |
| broad | balanced | [failed_downside_breakout__broad__balanced__v001.md](symbols/broad/failed_downside_breakout__broad__balanced__v001.md) | 2.1 | 2.8 | 2.1 | -8.3 | 65.9 | 1857/1525 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 2,547 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
