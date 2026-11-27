# atr_volatility_expansion: optimization summary

Updated 2026-11-25T23:05:36Z · backtest.py version `29e151e2b0` · 8,191 parameter sets tested with this version (8,191 rows in results.csv in total) · last run ended: see base optimization.log

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

31 of 60 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | ADAUSDT | 92% | 10.6 | 24.0 | 45.0 | 3.1 | -5.8 | 9 |
| 2 | SOLUSDT | 84% | 20.3 | 93.0 | 214.4 | 32.2 | 1.7 | 3 |
| 3 | VETUSDT | 82% | 4.5 | 16.9 | 53.1 | 10.4 | -12.9 | 4 |
| 4 | FILUSDT | 79% | 7.6 | 27.3 | -67.5 | 18.6 | -27.2 | 0 |
| 5 | ETCUSDT | 75% | 11.3 | 45.8 | 34.4 | 10.5 | -11.1 | 4 |
| 6 | LTCUSDT | 75% | 4.9 | 18.6 | -8.6 | -3.3 | -9.1 | 27 |
| 7 | BNBUSDT | 72% | 6.1 | 17.2 | 74.8 | -0.7 | -24.0 | 0 |
| 8 | ETHUSDT | 70% | 3.6 | 26.6 | 13.4 | 6.0 | -1.4 | 6 |
| 9 | BTCUSDT | 69% | 2.1 | 20.2 | 27.1 | 7.0 | -19.5 | 0 |
| 10 | AVAXUSDT | 64% | 12.6 | 39.9 | 14.6 | 21.7 | -12.0 | 5 |
| 11 | DOGEUSDT | 64% | 2.0 | 32.9 | 156.4 | 7.6 | -4.1 | 8 |
| 12 | XLMUSDT | 57% | 3.5 | 17.9 | -11.6 | -7.3 | 3.0 | 7 |
| 13 | ICPUSDT | 54% | 24.5 | 46.5 | -41.6 | 24.4 | -17.0 | 1 |
| 14 | TRXUSDT | 54% | 0.1 | 35.3 | 54.0 | -1.7 | -9.3 | 5 |
| 15 | BCHUSDT | 49% | -0.0 | 11.2 | 2.9 | -2.6 | -8.8 | 3 |
| 16 | ZECUSDT | 49% | -0.0 | 16.4 | -11.3 | 2.9 | -13.2 | 18 |
| 17 | DASHUSDT | 48% | -0.1 | 4.7 | -20.4 | 2.8 | -25.9 | 15 |
| 18 | XRPUSDT | 43% | -0.7 | 10.4 | 5.0 | 8.6 | -6.9 | 8 |
| 19 | DOTUSDT | 26% | -2.9 | 5.2 | -20.7 | -0.6 | -11.2 | 7 |
| 20 | AAVEUSDT | 26% | -4.4 | 21.0 | -36.5 | -3.5 | 11.0 | 4 |
| 21 | NEARUSDT | 21% | -7.7 | 26.6 | -15.6 | -20.7 | -10.4 | 7 |
| 22 | LINKUSDT | 20% | -5.8 | 29.3 | 37.9 | 4.1 | -17.4 | 0 |
| 23 | UNIUSDT | 16% | -12.8 | 6.4 | -37.0 | -24.4 | -11.4 | 1 |
| 24 | JSTUSDT | 15% | -9.8 | 24.5 | 4.5 | -11.8 | -12.2 | 0 |
| 25 | INJUSDT | 15% | -10.2 | 25.2 | 44.0 | -7.4 | -17.4 | 0 |
| 26 | CAKEUSDT | 13% | -3.5 | 10.0 | -48.5 | -3.9 | 14.3 | 8 |
| 27 | SHIBUSDT | 3% | -13.3 | 1.5 | -41.9 | -26.6 | -13.1 | 2 |
| 28 | ALGOUSDT | 2% | -15.8 | 2.9 | -3.8 | -13.6 | -4.4 | 1 |
| 29 | ATOMUSDT | 0% | -12.6 | n/a | 36.8 | -18.3 | -20.4 | 0 |
| 30 | STXUSDT | 0% | -18.0 | n/a | 105.8 | -27.1 | -10.4 | 0 |
| 31 | HBARUSDT | 0% | -23.1 | n/a | 26.6 | -24.4 | 38.8 | 0 |

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [atr_volatility_expansion__broad__max-income__v001.md](symbols/broad/atr_volatility_expansion__broad__max-income__v001.md) | 3.2 | 3.7 | 3.2 | -6.9 | 40.1 | 715/591 |
| broad | balanced | [atr_volatility_expansion__broad__balanced__v002.md](symbols/broad/atr_volatility_expansion__broad__balanced__v002.md) | 1.8 | 2.3 | 1.8 | -4.5 | 48.9 | 563/449 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 8,191 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
