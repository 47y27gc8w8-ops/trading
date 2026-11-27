# golden_cross_bl: golden cross on SPY

**Source idea** (golden_cross.txt): "golden cross on the s&p etf. Buy when the 50 day goes above the 200 day, get out when it crosses back. Maybe a trailing stop too? Not sure how much."

## Rules as interpreted
- Symbol: SPY, daily bars adjusted for dividends and splits (project Yahoo data, 1993 to 2026-11-20).
- Buy at the next open after the day the fast MA closes above the slow MA (the cross day only, `entry=cross`).
- Sell at the next open after the day the fast MA closes below the slow MA (death cross).
- Optional trailing stop: exit when the price falls `trailing_stop_pct` % below the highest high since entry. With `entry=cross`, a stopped-out trade waits for the **next** golden cross before buying again.
- Extras tested: EMA instead of SMA, a % band against whipsaws, and `entry=trend` (re-enter any day fast > slow and close > fast MA).
- Long-only, 100 % in or out, no leverage. Costs: 0 commission, 0.02 % slippage per fill.
- In-sample 1994 to 2015 (all decisions); out-of-sample 2016 to 2026-11-20 (only reported).

## Files
- `backtest.py`: copy of `strategies/backtest.py` with this strategy plugged in (`--period is|oos|all|live`, `--params`, `--trades`).
- `optimize.py`: grid search over 3,264 combos, ranked by in-sample Sharpe averaged over neighbouring fast/slow values (robustness).
- `results_is.csv`: every combo, in-sample. `summary.json`: baseline, picks, OOS, buy & hold.

Run: `docker compose run --rm -T backtest python strategies/golden_cross_bl/optimize.py` (~40 s)

## Results (Sharpe / CAGR / max drawdown)
| variant | params | in-sample 1994-2015 | out-of-sample 2016-2026 |
|---|---|---|---|
| SPY buy & hold | | 0.54 / 8.9 % / -55 % | 0.82 / 13.8 % / -34 % |
| your idea, as written | SMA 50/200 | 0.79 / 10.0 % / -19 % | 0.65 / 9.0 % / -34 % |
| your idea + 12 % trailing stop | SMA 50/200, trail 12 | 0.80 / 8.5 % / -17 % | 0.93 / 10.8 % / -16 % |
| **recommended (robust pick)** | EMA 80/100, trail 15 | 0.86 / 10.7 % / -16 % | 0.88 / 10.5 % / -20 % |
| best single IS combo | EMA 20/150, 1 % band, trail 15 | 0.87 / 10.7 % / -15 % | 0.98 / 11.8 % / -17 % |

## Caveats
- Only 8 to 10 trades in 22 years in-sample (5 to 6 out-of-sample). Every number here rests on a handful of trades, so differences of 0.05 Sharpe are noise.
- 3,264 combos were tried; the winner's in-sample edge over 50/200 is partly selection luck. The OOS check is one period with ~5 trades.
- In the 2016-2026 bull market, every variant made less than buy & hold (13.8 % a year). The strategy's value is the smaller drawdown (-16 to -20 % vs -34 %), not higher return.
- With a trailing stop and cross-only entry, you can sit in cash for a long time after a stop-out (e.g. the 50/200 + 12 % stop variant is flat right now).
