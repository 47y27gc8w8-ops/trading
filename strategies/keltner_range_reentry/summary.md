# keltner_range_reentry: optimization summary

Updated 2026-11-26T06:15:36Z · backtest.py version `cd417ff39f` · 9,100 parameter sets tested with this version (9,100 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 1h bars)
- In-sample (tuning): 2018-01-01 → 2024-01-01; out-of-sample (validation only): 2024-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.1% per side, slippage 0.1% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

33 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | STXUSDT | 15% | -0.3 | 3.0 | 88.6 | -8.0 | 2.3 | 1 |
| 2 | JSTUSDT | 13% | -0.6 | 2.3 | 1.9 | -2.6 | -5.2 | 0 |
| 3 | VETUSDT | 13% | -1.3 | 3.2 | 21.6 | 0.7 | -13.4 | 1 |
| 4 | INJUSDT | 13% | -2.0 | 7.1 | 115.0 | -12.3 | -0.9 | 1 |
| 5 | QNTUSDT | 11% | -0.9 | 4.4 | -26.0 | -5.9 | -7.8 | 0 |
| 6 | ETCUSDT | 8% | -3.4 | 2.7 | 11.2 | -6.2 | -0.7 | 5 |
| 7 | AVAXUSDT | 5% | -0.5 | 4.5 | 107.0 | 1.2 | -1.3 | 2 |
| 8 | NEARUSDT | 5% | -4.0 | 2.1 | 52.8 | -7.6 | -7.3 | 0 |
| 9 | BCHUSDT | 3% | -1.4 | 0.7 | -9.5 | 0.7 | -6.0 | 0 |
| 10 | SHIBUSDT | 3% | -3.4 | 0.6 | 11.7 | -3.0 | -7.0 | 0 |
| 11 | SOLUSDT | 2% | -0.2 | 2.9 | 211.6 | -5.5 | -5.5 | 0 |
| 12 | AAVEUSDT | 2% | -0.7 | 1.9 | 7.2 | -4.6 | -2.8 | 0 |
| 13 | ZECUSDT | 2% | -1.4 | 3.2 | -18.6 | -3.3 | -11.6 | 1 |
| 14 | RAYUSDT | 0% | -0.0 | n/a | -59.6 | -17.6 | -6.7 | 0 |
| 15 | ETHUSDT | 0% | -1.4 | n/a | 20.8 | -6.5 | -4.7 | 0 |
| 16 | ICPUSDT | 0% | -1.6 | n/a | -35.4 | -5.7 | -6.9 | 0 |
| 17 | LTCUSDT | 0% | -1.7 | n/a | -16.7 | -11.6 | -0.9 | 0 |
| 18 | BTCUSDT | 0% | -2.0 | n/a | 20.6 | -5.3 | -3.6 | 0 |
| 19 | ADAUSDT | 0% | -2.2 | n/a | 27.0 | -7.5 | -7.7 | 0 |
| 20 | LINKUSDT | 0% | -2.4 | n/a | 104.9 | -13.0 | -7.3 | 0 |
| 21 | XRPUSDT | 0% | -2.7 | n/a | 4.9 | -4.2 | -6.5 | 0 |
| 22 | XLMUSDT | 0% | -2.7 | n/a | -12.6 | -12.9 | -5.1 | 0 |
| 23 | DOTUSDT | 0% | -2.7 | n/a | 23.9 | -11.5 | -3.6 | 0 |
| 24 | ATOMUSDT | 0% | -2.9 | n/a | 15.4 | -10.6 | -3.7 | 0 |
| 25 | FILUSDT | 0% | -3.0 | n/a | -37.4 | -8.1 | 2.4 | 0 |
| 26 | DASHUSDT | 0% | -3.4 | n/a | -30.4 | -4.9 | -9.6 | 0 |
| 27 | TRXUSDT | 0% | -4.0 | n/a | 35.9 | -3.4 | -4.3 | 0 |
| 28 | DOGEUSDT | 0% | -4.2 | n/a | 130.1 | -13.2 | -1.8 | 0 |
| 29 | UNIUSDT | 0% | -4.7 | n/a | 27.7 | -9.4 | -4.7 | 0 |
| 30 | BNBUSDT | 0% | -4.8 | n/a | 58.2 | -8.9 | -7.4 | 0 |
| 31 | ALGOUSDT | 0% | -4.9 | n/a | -19.9 | -12.8 | -1.2 | 0 |
| 32 | HBARUSDT | 0% | -5.2 | n/a | 36.2 | -11.0 | -4.6 | 0 |
| 33 | CAKEUSDT | 0% | -6.2 | n/a | -52.3 | -8.0 | -5.4 | 0 |

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

Searching 9,100 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
