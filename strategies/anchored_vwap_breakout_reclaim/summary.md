# anchored_vwap_breakout_reclaim: optimization summary

Updated 2026-11-24T22:53:33Z · backtest.py version `90ad32a171` · 21,963 parameter sets tested with this version (21,963 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 1h bars)
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
| 1 | SHIBUSDT | 100% | 11.1 | 26.4 | 6.3 | 13.5 | -19.5 | 0 |
| 2 | ETCUSDT | 69% | 1.4 | 6.9 | 6.8 | -0.6 | -8.1 | 0 |
| 3 | LINKUSDT | 44% | -0.3 | 6.3 | 107.0 | -2.1 | -18.6 | 0 |
| 4 | DOGEUSDT | 39% | -1.0 | 5.0 | 113.9 | -1.0 | 0.2 | 1 |
| 5 | ICPUSDT | 33% | -3.2 | 5.4 | -58.9 | -4.9 | -13.2 | 0 |
| 6 | TRXUSDT | 18% | -2.6 | 4.4 | 20.3 | -3.9 | -8.5 | 0 |
| 7 | JSTUSDT | 13% | -3.4 | 1.6 | -15.0 | -7.7 | -14.1 | 0 |
| 8 | HBARUSDT | 7% | -6.3 | 6.5 | 22.1 | -9.0 | -17.2 | 0 |
| 9 | BTCUSDT | 0% | -5.1 | n/a | 20.6 | -8.7 | -12.8 | 0 |
| 10 | AAVEUSDT | 0% | -5.9 | n/a | 50.3 | -11.6 | -15.1 | 0 |
| 11 | XRPUSDT | 0% | -6.2 | n/a | -2.2 | -13.0 | 3.2 | 0 |
| 12 | XLMUSDT | 0% | -6.5 | n/a | -10.0 | -10.0 | -8.2 | 0 |
| 13 | ETHUSDT | 0% | -8.4 | n/a | 20.8 | -10.8 | -5.8 | 0 |
| 14 | ADAUSDT | 0% | -9.5 | n/a | 8.5 | -11.1 | -14.6 | 0 |
| 15 | RAYUSDT | 0% | -9.9 | n/a | -52.3 | -13.3 | -21.5 | 0 |
| 16 | BCHUSDT | 0% | -9.9 | n/a | 5.9 | -8.3 | -1.7 | 0 |
| 17 | UNIUSDT | 0% | -10.2 | n/a | 19.5 | -19.7 | -7.5 | 0 |
| 18 | FILUSDT | 0% | -10.2 | n/a | -37.6 | -18.2 | -6.0 | 0 |
| 19 | ALGOUSDT | 0% | -10.4 | n/a | -29.2 | -16.8 | -15.4 | 0 |
| 20 | STXUSDT | 0% | -11.5 | n/a | 61.7 | -14.3 | -21.9 | 0 |
| 21 | ZECUSDT | 0% | -13.6 | n/a | -18.9 | -15.4 | -14.9 | 0 |
| 22 | LTCUSDT | 0% | -13.8 | n/a | -17.1 | -15.9 | -21.3 | 0 |
| 23 | QNTUSDT | 0% | -14.1 | n/a | -4.1 | -20.3 | -19.7 | 0 |
| 24 | VETUSDT | 0% | -14.7 | n/a | 25.4 | -19.2 | -10.8 | 0 |
| 25 | DASHUSDT | 0% | -15.2 | n/a | -24.4 | -20.2 | -7.6 | 0 |
| 26 | DOTUSDT | 0% | -15.5 | n/a | 16.7 | -16.6 | -10.1 | 0 |
| 27 | ATOMUSDT | 0% | -16.5 | n/a | 21.2 | -21.0 | -10.0 | 0 |
| 28 | BNBUSDT | 0% | -17.3 | n/a | 82.1 | -22.1 | -11.5 | 0 |
| 29 | NEARUSDT | 0% | -17.7 | n/a | 72.3 | -19.4 | -10.6 | 0 |
| 30 | INJUSDT | 0% | -18.6 | n/a | 242.5 | -26.0 | -10.9 | 0 |
| 31 | CAKEUSDT | 0% | -19.8 | n/a | -34.5 | -24.7 | -7.2 | 0 |
| 32 | AVAXUSDT | 0% | -20.3 | n/a | 103.3 | -26.0 | -17.8 | 0 |
| 33 | SOLUSDT | 0% | -25.1 | n/a | 177.6 | -28.0 | -14.4 | 0 |

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

Searching 21,963 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
