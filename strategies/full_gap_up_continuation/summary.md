# full_gap_up_continuation: optimization summary

Updated 2026-11-27T12:55:22Z · backtest.py version `ed51168bca` · 681 parameter sets tested with this version (681 rows in results.csv in total) · last run ended: converged: no profile improved in the last 520 iterations at the smallest step size

## Setup

- Data: MSFT (etf, 5min bars)
- In-sample (tuning): 2016-03-01 → 2023-01-01; out-of-sample (validation only): 2023-01-01 → 2026-11-25
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

No variant passed all checks yet. See optimization.log for why candidates were rejected.

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

No eligible parameter sets yet.


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 681 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
