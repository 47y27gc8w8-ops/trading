# rsi_bullish_divergence_fixed_window: optimization summary

Updated 2026-11-25T10:55:20Z · backtest.py version `d1dd83e399` · 61,587 parameter sets tested with this version (61,587 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: GLD (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | XLU | 0% | 0.2 | n/a | 7.3 | 0.5 | -0.2 | 0 |
| 2 | SPY | 0% | 0.0 | n/a | 3.9 | 0.3 | 0.8 | 0 |
| 3 | VOO | 0% | 0.0 | n/a | 14.9 | 1.0 | 1.0 | 0 |
| 4 | IVV | 0% | 0.0 | n/a | 5.8 | 0.3 | 0.8 | 0 |
| 5 | VTI | 0% | 0.0 | n/a | 9.1 | 0.0 | 0.5 | 0 |
| 6 | QQQ | 0% | 0.0 | n/a | 2.0 | 0.7 | -0.3 | 0 |
| 7 | DIA | 0% | 0.0 | n/a | 4.9 | -0.1 | 0.5 | 0 |
| 8 | IWM | 0% | 0.0 | n/a | 7.4 | 0.0 | -0.3 | 0 |
| 9 | RSP | 0% | 0.0 | n/a | 8.8 | -0.2 | 0.0 | 0 |
| 10 | VEA | 0% | 0.0 | n/a | 4.3 | 0.0 | 0.6 | 0 |
| 11 | VWO | 0% | 0.0 | n/a | 2.2 | -0.9 | 0.0 | 0 |
| 12 | EFA | 0% | 0.0 | n/a | 7.2 | -0.4 | 0.1 | 0 |
| 13 | EEM | 0% | 0.0 | n/a | 7.6 | -0.3 | -0.2 | 0 |
| 14 | VXUS | 0% | 0.0 | n/a | 3.9 | 0.0 | 0.7 | 0 |
| 15 | ACWI | 0% | 0.0 | n/a | 9.4 | 0.0 | 0.5 | 0 |
| 16 | VT | 0% | 0.0 | n/a | 8.7 | 0.0 | 0.3 | 0 |
| 17 | XLK | 0% | 0.0 | n/a | -0.6 | 1.1 | 0.0 | 0 |
| 18 | XLF | 0% | 0.0 | n/a | 3.0 | 0.6 | 0.5 | 0 |
| 19 | XLE | 0% | 0.0 | n/a | 7.1 | 0.8 | 0.4 | 0 |
| 20 | XLV | 0% | 0.0 | n/a | 7.6 | 0.0 | 0.4 | 0 |
| 21 | XLY | 0% | 0.0 | n/a | 8.6 | 0.1 | 0.4 | 0 |
| 22 | XLP | 0% | 0.0 | n/a | 8.4 | 0.4 | 0.1 | 0 |
| 23 | XLI | 0% | 0.0 | n/a | 6.6 | 0.0 | 0.6 | 0 |
| 24 | XLB | 0% | 0.0 | n/a | 7.3 | 0.0 | 1.0 | 0 |
| 25 | SMH | 0% | 0.0 | n/a | 1.4 | 0.0 | -0.9 | 0 |
| 26 | SOXX | 0% | 0.0 | n/a | 8.8 | 0.4 | 0.0 | 0 |
| 27 | TLT | 0% | 0.0 | n/a | 6.9 | -0.1 | 0.0 | 0 |
| 28 | IEF | 0% | 0.0 | n/a | 5.1 | -0.2 | -0.1 | 0 |
| 29 | SHY | 0% | 0.0 | n/a | 2.1 | -0.0 | -0.0 | 0 |
| 30 | AGG | 0% | 0.0 | n/a | 4.1 | 0.0 | 0.0 | 0 |
| 31 | BND | 0% | 0.0 | n/a | 4.3 | 0.0 | 0.1 | 0 |
| 32 | LQD | 0% | 0.0 | n/a | 5.1 | -0.3 | -0.1 | 0 |
| 33 | HYG | 0% | 0.0 | n/a | 5.1 | 0.2 | 0.0 | 0 |
| 34 | TIP | 0% | 0.0 | n/a | 3.7 | 0.0 | 0.0 | 0 |
| 35 | GLD | 0% | 0.0 | n/a | 6.2 | 0.0 | 0.0 | 0 |
| 36 | SLV | 0% | 0.0 | n/a | 0.4 | 0.0 | 0.3 | 0 |
| 37 | USO | 0% | 0.0 | n/a | -16.6 | -2.0 | -0.3 | 0 |
| 38 | DBC | 0% | 0.0 | n/a | -6.5 | 0.0 | 0.0 | 0 |
| 39 | GDX | 0% | 0.0 | n/a | -11.2 | 0.0 | -0.2 | 0 |
| 40 | VIG | 0% | 0.0 | n/a | 6.0 | 0.4 | 0.5 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [rsi_bullish_divergence_fixed_window__broad__max-income__v002.md](symbols/broad/rsi_bullish_divergence_fixed_window__broad__max-income__v002.md) | 1.4 | 1.2 | 1.2 | -5.0 | 75.9 | 589/534 |
| broad | balanced | [rsi_bullish_divergence_fixed_window__broad__balanced__v002.md](symbols/broad/rsi_bullish_divergence_fixed_window__broad__balanced__v002.md) | 0.9 | 1.1 | 0.9 | -2.9 | 74.4 | 309/312 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 61,587 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
