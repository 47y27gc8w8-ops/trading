# Cross-sectional crypto momentum (rotation)

**Idea:** Winners keep winning relative to losers (Jegadeesh & Titman 1993). In crypto, Liu, Tsyvinski & Wu (2022) find strong momentum. Rotate into the strongest coins and go to cash in bear markets.

**Rules:** Every `rebalance` days, rank coins with at least `min_history` days of data by their `lookback` return and hold the `top_k` coins in equal weight. If BTC is below SMA(`regime_sma`), hold cash (`regime_sma` = 0 disables the filter).

**Data:** 16 Binance USDT pairs, daily. In-sample before 2024, out-of-sample from 2024. Costs are 15 bps.

**Caveats:** This is the strategy most exposed to **survivorship bias**: today's top 16 includes coins that 10x'd, and it leaves out the ones that died. Expect live results to be worse.
