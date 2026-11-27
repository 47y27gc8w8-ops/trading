# Low-correlation momentum selection (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end sort positive ROC(126) assets descending by ROC(126); greedily select up to 3, admitting each only if its 126-day daily-return correlation with every earlier selected asset is < 0.6; equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets not in the newly selected group.
- **Formal:** Positive ROC(126) assets sorted descending; greedily admit up to k, each only if its 126-day daily-return correlation with every already selected asset is < corr (undefined correlations are skipped, INDICATORS.md); equal weight.
- **Decision / fill:** at the close of the last daily bar of each complete month; orders fill at the
  next daily open. Sells and trims first, then buys to target; buys scale down if cash is short.
  Weights sum to at most 100 %; the rest is cash (0 %).
- **Protective stop:** every holding, stop_loss_pct below its average cost; gap below -> open,
  otherwise intrabar at the stop. On additions the stop never loosens:
  new stop = max(old, E_new x (1 - stop_loss_pct/100)).
- **Time exit:** after max_candles held daily bars, sell at the next open (age survives trims/additions).
- A stopped or timed-out holding can only return at a later month-end decision.

## Setup
| | |
|---|---|
| Universe | DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2004-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | defaults |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `k` | 3 |
| `corr` | 0.6 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 2, "max": 5, "step": 1, "hard_min": 1, "hard_max": 8} |
| `corr` | {"min": 0.3, "max": 0.9, "step": 0.05, "hard_min": 0.0, "hard_max": 1.0} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- correlation pairs with fewer than 3 common returns or zero variance are skipped (not blocking), per INDICATORS.md 'skips undefined correlations'. ROC and correlation windows stay 126.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).
