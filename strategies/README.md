# Strategies

Each folder is one strategy that improves through small, recorded experiments.

```
strategies/<name>/
  README.md          source, rules, known caveats
  strategy.py        positions(bars, params) -> target weights (and optional valid(params))
  config.json        universe, costs, in/out-of-sample split, current champion params + stats, mutation space
  experiments.jsonl  every experiment ever run, kept or discarded (append-only)
  EVOLUTION.md       readable report generated from experiments.jsonl
  rejected/<id>.patch  code changes that lost (kept for reference)
```

## Loop

```bash
scripts/evolve.sh sma_crossover --generations 20                 # random small param changes
scripts/evolve.sh sma_crossover --set fast=40 --note "idea"       # one hand-picked change
# edit strategies/sma_crossover/strategy.py, then:
scripts/evolve.sh sma_crossover --code-change --note "add volatility filter"
```

Each run backtests the candidate and compares it with the current champion:

- **better** (in-sample Sharpe up by at least `min_improvement`): it becomes the new champion in `config.json`
- **worse**: the champion stays. Param candidates are only logged. Code changes are saved to `rejected/<id>.patch` and reverted.

Either way the experiment is appended to `experiments.jsonl`, `EVOLUTION.md` is regenerated and the result is committed, so `git log -- strategies/<name>` shows how the strategy evolved.

## Avoiding fooling ourselves

- **Holdout:** decisions use only the in-sample window (before `oos_start`). The out-of-sample columns are never used to keep or discard a change. If in-sample Sharpe keeps rising while OOS falls, the strategy is being overfit, so stop evolving it.
- **No look-ahead:** weights decided at the close of day *t* earn day *t+1*'s return.
- **Costs:** `cost_bps` is charged per unit of turnover (crypto 15 bps, ETFs 5 bps).
- **Survivorship bias (crypto):** the universe is *today's* top 16 coins, so it leaves out the coins that died. Crypto results are therefore optimistic, especially for rotation strategies.
- **Multiple testing:** after hundreds of mutations, some will look good by chance. Treat a small improvement after many generations with suspicion.
- Long-only and unleveraged throughout (spot crypto / ETFs).

## Sources

- Trend following and MA crossovers: Faber (2007), *A Quantitative Approach to Tactical Asset Allocation*
- Time-series momentum: Moskowitz, Ooi & Pedersen (2012), [Quantpedia summary](https://quantpedia.com/strategies/time-series-momentum-effect/)
- Donchian breakout: the Turtle Traders rules (Dennis/Eckhardt, 1983)
- RSI(2): Connors & Alvarez (2008), *Short Term Trading Strategies That Work*, [MQL5 test](https://www.mql5.com/en/articles/17636)
- BTC MAX/MIN: Padysak & Vojtko (2022), [Quantpedia revisit](https://quantpedia.com/revisiting-trend-following-and-mean-reversion-strategies-in-bitcoin/)
- Cross-sectional momentum: Jegadeesh & Titman (1993); Liu, Tsyvinski & Wu (2022), *Common Risk Factors in Cryptocurrency*
