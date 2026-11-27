# adx_directional_break: optimization summary

Updated 2026-11-25T06:08:29Z · backtest.py version `39b59077e3` · 35,490 parameter sets tested with this version (35,490 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: BTCUSDT (crypto, 4h bars)
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
| 1 | AVAXUSDT | 44% | 3.1 | 53.4 | 102.0 | -6.9 | -9.8 | 0 |
| 2 | ATOMUSDT | 44% | 0.9 | 18.0 | 14.0 | 16.0 | -4.9 | 1 |
| 3 | FILUSDT | 36% | 2.6 | 14.7 | -36.9 | 13.0 | -16.6 | 2 |
| 4 | JSTUSDT | 34% | 1.2 | 34.0 | -7.0 | 5.9 | 14.5 | 16 |
| 5 | ADAUSDT | 34% | -2.4 | 8.3 | 17.0 | -8.9 | -19.9 | 0 |
| 6 | STXUSDT | 26% | -5.7 | 32.1 | 89.0 | -10.3 | -0.8 | 0 |
| 7 | ICPUSDT | 25% | -7.6 | 6.5 | -43.7 | 1.4 | -13.9 | 0 |
| 8 | ALGOUSDT | 21% | -3.9 | 23.5 | -19.7 | 12.2 | 1.1 | 5 |
| 9 | ETCUSDT | 20% | -2.8 | 4.1 | 5.1 | -5.5 | -2.2 | 6 |
| 10 | INJUSDT | 18% | -3.1 | 25.8 | 178.1 | -4.5 | -33.6 | 0 |
| 11 | LTCUSDT | 16% | -6.0 | 7.4 | -17.7 | -8.3 | -9.3 | 0 |
| 12 | XLMUSDT | 15% | -3.9 | 7.1 | -8.1 | -3.2 | -11.9 | 3 |
| 13 | DASHUSDT | 13% | -3.9 | 5.3 | -23.5 | -12.1 | 3.0 | 4 |
| 14 | BNBUSDT | 10% | -7.5 | 3.1 | 82.1 | -5.8 | -13.9 | 0 |
| 15 | CAKEUSDT | 8% | -6.7 | 4.0 | -38.2 | -13.6 | -1.7 | 2 |
| 16 | BCHUSDT | 7% | -4.0 | 3.8 | 5.9 | -3.2 | -22.5 | 0 |
| 17 | AAVEUSDT | 7% | -5.1 | 1.2 | 13.2 | -0.9 | 22.6 | 4 |
| 18 | LINKUSDT | 7% | -5.9 | 11.8 | 102.7 | -11.8 | 11.0 | 0 |
| 19 | DOTUSDT | 7% | -6.8 | 6.0 | 19.0 | -8.4 | -10.7 | 0 |
| 20 | ETHUSDT | 7% | -7.8 | 3.7 | 20.8 | -14.7 | -23.2 | 0 |
| 21 | VETUSDT | 7% | -7.8 | 2.0 | 14.4 | -11.0 | -21.8 | 4 |
| 22 | ZECUSDT | 5% | -7.7 | 2.1 | -18.2 | -4.7 | 21.8 | 1 |
| 23 | SHIBUSDT | 3% | -9.1 | 1.1 | 24.0 | -6.3 | -23.5 | 0 |
| 24 | NEARUSDT | 3% | -11.4 | 1.3 | 59.7 | -9.9 | -14.9 | 0 |
| 25 | HBARUSDT | 3% | -12.1 | 1.7 | 25.2 | -8.4 | -18.0 | 0 |
| 26 | BTCUSDT | 2% | -5.5 | 0.6 | 20.6 | -7.9 | -12.1 | 0 |
| 27 | XRPUSDT | 2% | -7.6 | 1.2 | -1.8 | -13.1 | -18.4 | 0 |
| 28 | DOGEUSDT | 2% | -9.8 | 0.1 | 117.4 | -16.4 | -12.8 | 0 |
| 29 | SOLUSDT | 2% | -11.7 | 4.8 | 186.2 | -3.1 | -10.3 | 0 |
| 30 | UNIUSDT | 2% | -15.4 | 3.5 | 30.5 | -21.4 | -10.0 | 0 |
| 31 | TRXUSDT | 0% | -12.8 | n/a | 23.9 | -12.3 | -4.9 | 0 |
| 32 | QNTUSDT | 0% | -17.7 | n/a | -12.4 | -27.6 | -14.6 | 0 |
| 33 | RAYUSDT | 0% | -18.7 | n/a | -66.9 | -22.7 | -3.4 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| SOLUSDT | none passed | | | | | | | |
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 35,490 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
