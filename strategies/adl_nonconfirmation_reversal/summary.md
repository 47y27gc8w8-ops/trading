# adl_nonconfirmation_reversal: optimization summary

Updated 2026-11-25T06:09:15Z · backtest.py version `268c407cee` · 122,018 parameter sets tested with this version (122,018 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: XLI (etf, 1d bars)
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
| 1 | DBC | 36% | 0.5 | 3.0 | -6.5 | 2.4 | 0.9 | 13 |
| 2 | EFA | 25% | 2.3 | 4.0 | 7.2 | 1.6 | 0.2 | 2 |
| 3 | USO | 23% | -2.5 | 4.4 | -16.6 | -0.5 | 1.6 | 11 |
| 4 | VWO | 21% | 1.3 | 2.3 | 2.2 | 2.2 | 1.2 | 9 |
| 5 | SOXX | 20% | -0.2 | 3.3 | 8.8 | -0.3 | -1.1 | 1 |
| 6 | XLU | 10% | 1.8 | 0.7 | 7.3 | 0.8 | 0.2 | 2 |
| 7 | VEA | 7% | 1.2 | 1.8 | 4.3 | -0.1 | 0.8 | 1 |
| 8 | XLP | 7% | 0.1 | 0.6 | 8.4 | 0.2 | 1.4 | 4 |
| 9 | TIP | 7% | 0.0 | 0.3 | 3.7 | 0.0 | -0.1 | 0 |
| 10 | IVV | 7% | -0.2 | 0.8 | 5.8 | -0.2 | -1.3 | 2 |
| 11 | XLV | 5% | 0.0 | 1.3 | 7.6 | 1.1 | 2.6 | 3 |
| 12 | XLK | 5% | -0.4 | 0.2 | -0.6 | -0.1 | 0.5 | 3 |
| 13 | VT | 3% | 1.2 | 0.6 | 8.7 | 1.4 | -0.5 | 2 |
| 14 | XLF | 3% | -0.9 | 1.0 | 3.0 | -2.5 | -0.7 | 1 |
| 15 | SMH | 2% | -0.2 | 0.9 | 1.4 | -0.5 | 0.9 | 1 |
| 16 | SLV | 2% | -1.6 | 0.0 | 0.4 | -3.9 | -2.3 | 1 |
| 17 | CSNDX.SW | 0% | 5.5 | n/a | 16.5 | 4.5 | 1.1 | 0 |
| 18 | TQQQ | 0% | 3.8 | n/a | 42.8 | 4.0 | 2.1 | 0 |
| 19 | VWRL.SW | 0% | 2.7 | n/a | 7.8 | 6.0 | 0.3 | 0 |
| 20 | CSSPX.SW | 0% | 2.1 | n/a | 12.0 | 0.3 | 2.4 | 0 |
| 21 | GDX | 0% | 1.5 | n/a | -11.2 | 0.3 | 1.4 | 0 |
| 22 | VXUS | 0% | 1.1 | n/a | 3.9 | 0.8 | 0.3 | 0 |
| 23 | VOO | 0% | 1.0 | n/a | 14.9 | 0.5 | -0.4 | 0 |
| 24 | USMV | 0% | 1.0 | n/a | 14.8 | 1.4 | -0.0 | 0 |
| 25 | VNQ | 0% | 0.8 | n/a | 7.4 | 0.8 | -0.5 | 0 |
| 26 | IWDA.AS | 0% | 0.8 | n/a | 13.0 | 0.5 | 0.1 | 0 |
| 27 | ACWI | 0% | 0.7 | n/a | 9.4 | 1.0 | -0.4 | 0 |
| 28 | SCHD | 0% | 0.7 | n/a | 13.3 | -0.8 | 1.1 | 0 |
| 29 | VUG | 0% | 0.4 | n/a | 8.7 | 1.2 | 1.1 | 0 |
| 30 | VIG | 0% | 0.1 | n/a | 6.0 | -0.3 | 0.3 | 0 |
| 31 | BND | 0% | 0.1 | n/a | 4.3 | 0.1 | -0.4 | 0 |
| 32 | VTI | 0% | 0.0 | n/a | 9.1 | -0.2 | -1.6 | 0 |
| 33 | SPY | 0% | 0.0 | n/a | 3.9 | -0.2 | -1.1 | 0 |
| 34 | SHY | 0% | -0.0 | n/a | 2.1 | -0.0 | -0.2 | 0 |
| 35 | CSSMI.SW | 0% | -0.1 | n/a | 12.0 | 1.2 | 0.6 | 0 |
| 36 | CSPX.L | 0% | -0.1 | n/a | 16.3 | -0.2 | -0.5 | 0 |
| 37 | GLD | 0% | -0.2 | n/a | 6.2 | -1.1 | 0.3 | 0 |
| 38 | IEF | 0% | -0.2 | n/a | 5.1 | -0.2 | -0.2 | 0 |
| 39 | AGG | 0% | -0.3 | n/a | 4.1 | -0.3 | -0.1 | 0 |
| 40 | QQQ | 0% | -0.3 | n/a | 2.0 | 1.5 | 1.5 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [adl_nonconfirmation_reversal__broad__max-income__v002.md](symbols/broad/adl_nonconfirmation_reversal__broad__max-income__v002.md) | 0.2 | 0.1 | 0.1 | -6.3 | 50.7 | 615/791 |
| broad | balanced | [adl_nonconfirmation_reversal__broad__balanced__v001.md](symbols/broad/adl_nonconfirmation_reversal__broad__balanced__v001.md) | 0.2 | 0.3 | 0.2 | -5.5 | 45.9 | 590/728 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 122,018 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
