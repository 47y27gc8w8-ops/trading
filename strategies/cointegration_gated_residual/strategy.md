# Cointegration-gated residual (formalized)

Source: `original.md` (library spec), EXECUTION.md "Pair execution" / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_pairs.py`; rule = `signals()`, execution = `_simulate_pair()`).

> **Borrow cost is an assumption (0.25 %/yr), not historical data.** The spec says to disable
> this strategy without borrow/carry history; the user chose to run it with a labelled assumption.

## Rule
- **Spec buy trigger:** At each month-end fit log(A)=alpha+beta*log(B) on preceding 252 bars; require beta>0 and Engle-Granger cointegration p<0.05. Freeze model and residual mean/std for next month. Enter long A/short B ratio 1:beta when residual z<-2.
- **Spec exit:** Signal/rebalance exit: Frozen residual z>=0 or <=-4; close at next month-end before refitting.
- **Formal:** At each month-end t fit log(A) = alpha + beta log(B) on t-n..t-1; if beta > 0 and the Engle-Granger p-value < p, freeze alpha, beta and the residual mean/std for bars t .. next month-end - 1. Frozen residual z < -2 -> long A / short B with dollar ratio 1:beta; exit z >= 0 or z <= -4; positions are closed at the next month-end (force) before refitting.
- **Fills:** decided at bar t's close, both legs filled at the next synchronized open (both need a bar).
- **Protective exits (OR):** per-leg hard stop leg_stop_pct (long below, short above its entry fill;
  a stop forces the other leg out); net pair P&L incl. fees and borrow <= -pair_stop_pct % of entry
  gross at a close -> next open; time exit after max_candles held bars (entry bar = 1) -> next open.

## Setup
| | |
|---|---|
| Legs | GLD / IAU |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2007-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, gross pair notional 100 % of equity |
| Costs | fee 0.05 % + slippage 0.03 % per fill, both legs |
| Borrow (short leg) | **0.25 %/yr, assumed** |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 252 |
| `p` | 0.05 |
| `pair_stop_pct` | 5.0 |
| `leg_stop_pct` | 8.0 |
| `max_candles` | 40 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 126, "max": 504, "step": 21, "hard_min": 42, "hard_max": 756} |
| `p` | {"min": 0.01, "max": 0.1, "step": 0.01, "hard_min": 0.001, "hard_max": 0.5} |
| `pair_stop_pct` | {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.5, "hard_max": 30.0} |
| `leg_stop_pct` | {"min": 4.0, "max": 15.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0} |
| `max_candles` | {"min": 10, "max": 80, "step": 5, "hard_min": 2, "hard_max": 252} |

## Assumptions
- Engle-Granger p-value computed in numpy exactly as statsmodels coint(trend='c', maxlag=1, autolag=None) (OLS, ADF on residuals without constant with 1 lag, MacKinnon N=2 'c' p-value constants copied from statsmodels 0.14.4); statsmodels isn't in the backtest image. Formation = the n bars before the month-end bar; the model is frozen from that month-end bar until the next one, where open positions are closed (forced) before refitting. Entry z -2 and stop z -4 are fixed constants.
- BORROW COST ASSUMED (user decision 2026-11-27): the spec says to disable pairs without historical borrow/carry data; there is none, so the short leg pays a constant labelled fee (CONFIG borrow_fee_pct_yr: 0.25 %/yr for these easy-to-borrow ETFs/large caps, 3 %/yr for crypto margin) on its market value per calendar day; stress runs at higher fees are logged after the optimization. Borrow recalls and margin calls are not modelled.
- short proceeds earn 0 % and the long leg is paid from the sleeve (no margin interest): conservative carry; total-return (adjusted) closes on both legs, so the short leg pays the dividends it is short (dividend-in-lieu).
- gross notional G = 100 % of sleeve equity at entry (equal dollars: G/2 each; ratio 1:beta: long G/(1+beta), short beta*G/(1+beta)); quantities frozen at entry.
- same-bar ambiguity: if a leg's stop is touched intrabar, that leg fills at its stop and the other leg at its worst bar extreme (long: low, short: high); if both legs touch, the long leg is assumed first. Gaps through a stop fill both legs at the open.
- no new entry on a bar where a position was closed, and no entry when the exit condition (or a forced window end) is true on the signal bar.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), both legs, entry and exit.
- IAU, EWA, EWC and VDE were not in the project; their Yahoo daily history was fetched on 2026-11-27 (src.collectors.yahoo_daily.update, full history) without adding them to config/symbols.yaml, so the nightly job doesn't refresh them.
