# Time-series momentum, volatility-targeted

**Idea:** An asset's own past return predicts its next return (Moskowitz, Ooi & Pedersen 2012). Sizing by inverse volatility keeps risk roughly constant.

**Rules:** For each coin, if the `lookback`-day return is > 0, hold `min(1, target_vol / realised_vol(vol_window))` of its 1/N sleeve. Otherwise hold cash. Positions are rebalanced daily.

**Data:** 16 Binance USDT pairs, daily (UTC). In-sample before 2024, out-of-sample from 2024. Costs are 15 bps.

**Caveats:** Survivorship bias, because the universe is today's top coins. The daily vol resizing creates turnover.
