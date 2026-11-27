# bollinger_squeeze_release: optimization summary

Updated 2026-11-25T02:46:19Z · backtest.py version `2587de07d6` · 28,730 parameter sets tested with this version (28,730 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: ETHUSDT (crypto, 4h bars)
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
| 1 | ETHUSDT | 98% | 14.0 | 34.4 | 20.8 | 8.5 | -16.0 | 0 |
| 2 | RAYUSDT | 95% | 15.5 | 36.7 | -62.0 | 24.1 | -27.0 | 0 |
| 3 | ZECUSDT | 84% | 4.6 | 25.2 | -21.5 | 1.4 | -1.2 | 0 |
| 4 | AVAXUSDT | 75% | 4.6 | 22.6 | 115.7 | -0.7 | -10.2 | 23 |
| 5 | LINKUSDT | 70% | 2.8 | 11.6 | 103.3 | 4.1 | -16.5 | 0 |
| 6 | ADAUSDT | 66% | 1.7 | 15.2 | 29.6 | 0.4 | -7.3 | 0 |
| 7 | ETCUSDT | 64% | 1.7 | 8.6 | 11.6 | -0.8 | -15.1 | 0 |
| 8 | BNBUSDT | 62% | 1.7 | 13.2 | 66.8 | 8.0 | -3.9 | 3 |
| 9 | TRXUSDT | 59% | 0.6 | 15.3 | 34.4 | 3.8 | -6.1 | 0 |
| 10 | JSTUSDT | 56% | 1.0 | 15.5 | 6.7 | 12.7 | 1.1 | 13 |
| 11 | BTCUSDT | 49% | -0.1 | 11.3 | 20.6 | -2.7 | -16.4 | 0 |
| 12 | NEARUSDT | 44% | -1.9 | 17.0 | 45.2 | -4.9 | -6.3 | 8 |
| 13 | INJUSDT | 36% | -2.7 | 27.9 | 100.7 | -4.3 | -22.2 | 0 |
| 14 | FILUSDT | 26% | -4.1 | 13.9 | -30.9 | 7.5 | -9.1 | 1 |
| 15 | SOLUSDT | 25% | -5.5 | 26.2 | 248.9 | -9.8 | -17.4 | 0 |
| 16 | QNTUSDT | 25% | -7.3 | 15.4 | -27.4 | -9.7 | -3.8 | 2 |
| 17 | VETUSDT | 23% | -8.8 | 9.4 | 20.1 | -10.8 | -10.2 | 0 |
| 18 | XLMUSDT | 13% | -4.9 | 4.4 | -9.0 | -8.3 | -14.3 | 0 |
| 19 | LTCUSDT | 13% | -5.3 | 7.3 | -16.9 | 3.5 | -6.0 | 0 |
| 20 | HBARUSDT | 10% | -10.0 | 13.8 | 38.1 | -5.6 | 0.7 | 0 |
| 21 | DASHUSDT | 8% | -9.1 | 7.3 | -28.3 | -6.7 | -14.3 | 1 |
| 22 | AAVEUSDT | 7% | -7.7 | 4.2 | 9.9 | -8.3 | -6.7 | 0 |
| 23 | UNIUSDT | 7% | -9.0 | 2.5 | 23.4 | -10.0 | -0.7 | 1 |
| 24 | XRPUSDT | 3% | -7.9 | 2.3 | 4.3 | -9.3 | -15.4 | 0 |
| 25 | DOGEUSDT | 3% | -8.2 | 5.4 | 125.7 | -4.0 | -10.3 | 0 |
| 26 | ALGOUSDT | 2% | -8.5 | 3.3 | -9.9 | -7.3 | 6.8 | 1 |
| 27 | ATOMUSDT | 2% | -13.0 | 1.0 | 21.9 | -17.9 | 2.0 | 0 |
| 28 | SHIBUSDT | 2% | -18.3 | 3.8 | 21.1 | -18.6 | 0.4 | 1 |
| 29 | DOTUSDT | 0% | -10.1 | n/a | 24.1 | -7.9 | -3.5 | 0 |
| 30 | BCHUSDT | 0% | -11.3 | n/a | -12.8 | -6.1 | -11.5 | 0 |
| 31 | STXUSDT | 0% | -16.6 | n/a | 101.4 | -20.8 | -30.0 | 0 |
| 32 | ICPUSDT | 0% | -19.0 | n/a | -38.6 | -18.0 | -2.2 | 0 |
| 33 | CAKEUSDT | 0% | -22.1 | n/a | -59.2 | -24.8 | -11.1 | 0 |

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

Searching 28,730 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
