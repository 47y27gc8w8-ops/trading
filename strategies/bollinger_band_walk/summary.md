# bollinger_band_walk: optimization summary

Updated 2026-11-24T22:56:40Z · backtest.py version `952b79552a` · 6,760 parameter sets tested with this version (6,760 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: QQQ (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

## Screening: where does the strategy work? (in-sample ranking)

55 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | TLT | 48% | 0.7 | 1.7 | 6.7 | 1.2 | -0.7 | 0 |
| 2 | GLD | 46% | 1.2 | 3.2 | 8.5 | 1.5 | 1.0 | 27 |
| 3 | IEF | 36% | 0.3 | 0.5 | 5.2 | 0.2 | -0.6 | 0 |
| 4 | LQD | 31% | -0.2 | 0.6 | 5.4 | 0.1 | -0.3 | 5 |
| 5 | AGG | 30% | 0.1 | 0.4 | 4.0 | 0.0 | -0.2 | 2 |
| 6 | HYG | 26% | 0.5 | 2.5 | 4.8 | 0.5 | 0.3 | 12 |
| 7 | XLU | 20% | 0.2 | 0.4 | 6.4 | 0.1 | -0.7 | 0 |
| 8 | XLY | 20% | -0.3 | 0.5 | 7.2 | 0.3 | 0.6 | 12 |
| 9 | SLV | 20% | -0.3 | 1.9 | 2.0 | -0.9 | 0.4 | 11 |
| 10 | DIA | 16% | -0.1 | 0.3 | 4.9 | -0.4 | 0.1 | 1 |
| 11 | EEM | 8% | -0.6 | 0.3 | 7.9 | -1.2 | -0.2 | 0 |
| 12 | USO | 3% | 0.6 | 0.2 | -17.2 | 1.3 | -0.9 | 0 |
| 13 | BND | 3% | 0.0 | 0.1 | 4.3 | -0.1 | 0.0 | 0 |
| 14 | EFA | 2% | -0.3 | 0.4 | 5.8 | -0.0 | 1.0 | 1 |
| 15 | VNQ | 2% | -0.4 | 0.3 | 8.5 | -0.5 | -0.0 | 0 |
| 16 | TQQQ | 2% | -1.0 | 0.6 | 58.3 | -0.3 | 0.1 | 0 |
| 17 | MTUM | 0% | 0.8 | n/a | 15.5 | 1.2 | -0.2 | 0 |
| 18 | CSSMI.SW | 0% | 0.3 | n/a | 3.3 | 0.6 | 0.2 | 0 |
| 19 | CSNDX.SW | 0% | 0.1 | n/a | 18.0 | -0.1 | -1.2 | 0 |
| 20 | VXUS | 0% | 0.0 | n/a | 1.2 | -0.0 | 1.8 | 0 |
| 21 | CSPX.L | 0% | -0.1 | n/a | 11.3 | 0.9 | 4.0 | 0 |
| 22 | SCHD | 0% | -0.2 | n/a | 12.3 | -0.2 | 0.8 | 0 |
| 23 | CSSPX.SW | 0% | -0.2 | n/a | 13.6 | 0.4 | -0.1 | 0 |
| 24 | VOO | 0% | -0.2 | n/a | 11.9 | -0.4 | -0.3 | 0 |
| 25 | XLK | 0% | -0.2 | n/a | -0.5 | -1.0 | 0.0 | 0 |
| 26 | TIP | 0% | -0.2 | n/a | 4.2 | -0.3 | -0.9 | 0 |
| 27 | SHY | 0% | -0.3 | n/a | 2.1 | -0.3 | -0.4 | 0 |
| 28 | IWM | 0% | -0.3 | n/a | 7.5 | -0.4 | 1.0 | 0 |
| 29 | VTV | 0% | -0.4 | n/a | 7.2 | -1.0 | 0.4 | 0 |
| 30 | IVV | 0% | -0.4 | n/a | 4.6 | -0.6 | -0.3 | 0 |
| 31 | USMV | 0% | -0.4 | n/a | 13.5 | 0.4 | 0.4 | 0 |
| 32 | XLF | 0% | -0.4 | n/a | 2.1 | -0.1 | -1.5 | 0 |
| 33 | XLI | 0% | -0.5 | n/a | 5.6 | -0.8 | 1.3 | 0 |
| 34 | XLP | 0% | -0.5 | n/a | 7.4 | -0.6 | -0.0 | 0 |
| 35 | VUG | 0% | -0.6 | n/a | 8.1 | -0.8 | -0.7 | 0 |
| 36 | QUAL | 0% | -0.6 | n/a | 9.0 | -0.7 | 0.9 | 0 |
| 37 | VTI | 0% | -0.6 | n/a | 7.3 | -1.1 | -0.2 | 0 |
| 38 | SPY | 0% | -0.7 | n/a | 3.9 | -1.2 | -0.3 | 0 |
| 39 | SMH | 0% | -0.7 | n/a | -0.3 | -0.9 | -3.5 | 0 |
| 40 | VIG | 0% | -0.7 | n/a | 7.0 | -0.9 | 0.1 | 0 |

(15 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | none passed | | | | | | | |


## Analyst notes

<!-- analyst-notes:start -->
**Verdict (2026-11-25): no tradable variant.** The band walk as specified loses money on the
named market and across ETFs as a group.

- **QQQ (base):** all 6,760 grid sets tested; none profitable in-sample (2000–2015). Best ≈ −0.01%/yr
  on 5 trades; the spec defaults lost −0.9%/yr IS (25 trades, PF 0.45) and −0.2%/yr OOS. Buy & hold
  QQQ made +1.6%/yr IS and far more OOS, and the strategy is in the market only ~4–7% of the time.
- **Broad basket (55 ETFs, one shared parameter set):** full grid tested; none profitable in-sample.
  The best set (n 5, stop 1.5 ATR, target 2 ATR) lost −0.06%/yr IS over 148 trades, profit factor 0.65.
  With many trades behind it, this is the most trustworthy result, and it is negative.
- **Why it fails:** three or more closes above the upper band already price in the move. The exit
  (close < SMA(10)) usually triggers within ~7 bars, after a pullback. Many small signal-exit
  losses outweigh the occasional 3-ATR target. max_candles almost never binds, so it barely matters.
- **Where it might work:** only defensive or trend-persistent assets showed some profitable sample
  sets: TLT 48%, GLD 46% (27 sets passing every gate in the screen sample), IEF 36%. Ranking
  persistence was **NOT PERSISTENT** (rank corr 0.07), so a good look on one symbol did not predict
  its later results. Targeting GLD would most likely be picking luck. A GLD-only run is possible
  but would be low confidence and was not run.
- **Range warnings:** none relevant. No set was profitable, so no best sat on a range edge.
- **Paper trading:** none recommended. Ideas outside this spec, for the user to decide (not built in):
  a looser exit (e.g. close < SMA(20) or a trailing ATR stop) so walks can run longer, or n = 1–2
  with a trend filter. Either would be a new strategy variant, not an optimization of this one.
<!-- analyst-notes:end -->

---

Searching 6,760 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
