# bollinger_band_walk__broad: optimization summary

Updated 2026-11-24T22:56:40Z · backtest.py version `413bbd6bc7` · 6,760 parameter sets tested with this version (6,760 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: SPY, VOO, IVV, VTI, QQQ, DIA, IWM, RSP, VEA, VWO, EFA, EEM, VXUS, ACWI, VT, XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU, XLB, SMH, SOXX, TLT, IEF, SHY, AGG, BND, LQD, HYG, TIP, GLD, SLV, USO, DBC, GDX, VIG, SCHD, MTUM, QUAL, USMV, VNQ, VUG, VTV, TQQQ, SQQQ, CSSPX.SW, CSNDX.SW, CSSMI.SW, VWRL.SW, IWDA.AS, CSPX.L (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.

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
