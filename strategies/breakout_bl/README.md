# breakout_bl: 20-day breakout / 10-day breakdown (from breakout.md)

## Rules (as written in breakout.md, made exact)
- **Buy** when the daily close is above the highest high of the previous 20 days (today's bar not included).
- **Sell** when the daily close is below the lowest low of the previous 10 days.
- Signals are taken at the daily close (UTC, Binance USDT pairs). Orders fill at the next day's open. Long only, one position per coin, and each coin gets an equal share of the capital.
- Costs: 0.10 % fee plus 0.05 % slippage on each side.
- The tuning added two optional extras that are off by default: `trend_sma` (only buy above an SMA) and `trailing_stop_pct`.

## Split
- **In-sample** 2018-01-01 .. 2024-12-31. All choices of coins and parameters were made on this window only.
- **Out-of-sample** 2025-01-01 .. 2026-11-22. These numbers are reported but were never used to choose anything.

## Files
| file | what |
|---|---|
| `backtest.py` | trade-level backtest (copied from `strategies/backtest.py`, reads the shared bar cache without writing to it) |
| `optimize.py` | screens each coin with the original rules, selects coins, tunes one shared parameter set on them, then tunes per coin |
| `walkforward.py` | checks whether picking coins by their results over the past 3 years picks next year's winners |
| `tune_broad.py` | tunes one shared parameter set on all eligible coins |
| `results/` | `screen.csv`, `tune_grid.csv`, `per_coin.csv`, `summary.json`, `walkforward_*.csv`, `tune_grid_broad.csv`, `tune_broad.json` |
| `log.md` | timestamped run log |

To run (inside the backtest container):
```
docker compose run --rm -T backtest python strategies/breakout_bl/optimize.py --budget-min 10
docker compose run --rm -T backtest python strategies/breakout_bl/walkforward.py --tag original
docker compose run --rm -T backtest python strategies/breakout_bl/tune_broad.py
docker compose run --rm -T backtest python strategies/breakout_bl/backtest.py --period oos [--params '{"entry_n":30,"exit_n":5}']
```

## Findings (2026-11-23, about 1.5 min of compute in total)
1. **Screen.** 60 coins have daily bars. 35 of them have enough in-sample history (at least 1.5 years and 8 trades). 16 passed the in-sample filter: Sharpe ≥ 0.8, profit factor ≥ 1.3, and a smaller drawdown than buy & hold. They are SOL, VET, ADA, HBAR, BTC, DOGE, BNB, AVAX, SHIB, DOT, NEAR, UNI, ALGO, RAY, ETH and ETC.
2. **The screened coins did not keep working.** With the original 20/10 rules:

   | basket | IS Sharpe | OOS Sharpe | OOS return | OOS buy & hold | OOS max DD |
   |---|---|---|---|---|---|
   | 16 selected | 1.39 | **-0.38** | -22.5 % | -67.9 % | -41.8 % |
   | 19 rejected | 0.44 | **1.05** | +88.7 % | +36.6 % | -31.4 % |
   | all 35 eligible | 1.20 | 0.68 | +37.9 % | -11.2 % | -27.7 % |

3. **Walk-forward check** (`results/walkforward_original.csv`): for each year from 2021 to 2026, coins were picked using only the 3 years before. Coins with a good trailing breakout record beat the other coins in 4 of 6 years, but the average Sharpe difference was **0.00**. Picking the coins that trended most cleanly (top third by efficiency ratio) was **worse**: it won in only 1 of 6 years and lost 0.58 Sharpe on average. Within one window, trendiness and breakout Sharpe are correlated (Spearman 0.51 in-sample). That only describes the past. It does not tell you which coins will trend next.
4. **Tuning.**
   - On the 16 selected coins, the best shared set was 20/5 with SMA50. In-sample Sharpe rose from 1.39 to 1.53, but out-of-sample it stayed at -0.37.
   - Tuning each coin separately (`per_coin.csv`) did not fix the coins that failed out-of-sample.
   - On all 35 coins, the best smoothed in-sample sets used a faster exit (exit_n = 5). Best shared set: 30/5. Compared with the original 20/10:

   | set | IS Sharpe | IS max DD | OOS Sharpe | OOS return | OOS max DD |
   |---|---|---|---|---|---|
   | original 20/10 | 1.20 | -41.9 % | **0.68** | **+37.9 %** | -27.7 % |
   | 30/5 | 1.37 | -25.5 % | 0.57 | +20.2 % | **-18.5 %** |
   | 20/5 + SMA50 | 1.35 | -32.0 % | 0.44 | +14.6 % | -20.4 % |

   Tuning roughly halved drawdowns, both in- and out-of-sample. It did not improve out-of-sample return or Sharpe.
5. **Concentration.** Most coins lost money out-of-sample on their own: 2025-26 was a bear market for most alts. The basket was positive mainly because of a few big trends: ZEC (the strategy made +359 %/yr on it), JST, TRX and DASH. All four failed the in-sample screen. This is normal for trend following, and it is the reason to stay broad.

## Recommendation
- Run the rules on the **broad basket of established coins**, not a list chosen from past results.
- Use **20/10** for higher return, or **30/5** for a smaller drawdown.
- Treat the coin list as a liquidity and history filter, not as a performance filter.

## Caveats
- **Survivorship.** The universe is coins that exist on Binance today. Delisted coins are missing, so results look better than reality.
- **Short out-of-sample window.** Two mostly bearish years, and about 10 trades per coin.
- **Sizing.** Each coin's slice is fully invested whenever it is in a trade, with no volatility sizing.
