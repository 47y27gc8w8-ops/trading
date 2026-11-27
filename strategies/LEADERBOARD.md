# Strategy leaderboard

Updated 2026-11-27T13:52:50Z. 44 saved variants from optimizer-managed strategies.

Conservative %/yr = the lower of in-sample and out-of-sample yearly return; DD = the worse max drawdown of the two periods. Choosing between strategies with these numbers uses the out-of-sample period, so treat paper trading as the real test. Backtest results don't guarantee future performance.

⚠ low confidence = a single-symbol variant of a strategy whose screen ranking was not persistent in-sample (a good first half didn't predict a good second half), so the symbol may have been picked by luck. Prefer that strategy's broad basket.

## Best variant per symbol (or basket) and profile

| symbols | max-income | balanced | safe-starter |
|---|---|---|---|
| BTCUSDT,ETHUSDT,LTCUSDT,SOLUSDT | crypto_equal_weight_rebalance · 14.2%/yr · DD -70.9% | – | crypto_equal_weight_rebalance · 9.6%/yr · DD -58.2% |
| EFA,IEF,SPY | dual_momentum_allocation · 6.2%/yr · DD -27.6% | dual_momentum_allocation · 7.5%/yr · DD -24.6% | dual_momentum_allocation · 6.2%/yr · DD -27.6% |
| EWA,EWC | half_life_filtered_pairs · 0.2%/yr · DD -14.1% | half_life_filtered_pairs · 0.2%/yr · DD -12.0% | – |
| IEF,SPY | drawdown_defensive_switch · 10.4%/yr · DD -22.5% | drawdown_defensive_switch · 7.0%/yr · DD -25.4% | drawdown_defensive_switch · 8.2%/yr · DD -13.3% |
| KO,PEP | ratio_zscore_pairs · 0.2%/yr · DD -11.1% | ratio_zscore_pairs · 0.2%/yr · DD -11.1% | – |
| SPY | single_etf_volatility_target · 8.1%/yr · DD -25.4% | single_etf_volatility_target · 2.1%/yr · DD -5.0% | single_etf_volatility_target · 2.1%/yr · DD -5.4% |
| SPY,TLT | stock_bond_paired_switch · 5.2%/yr · DD -23.3% | stock_bond_paired_switch · 5.5%/yr · DD -29.8% | stock_bond_paired_switch · 5.7%/yr · DD -27.5% |
| base: basket of 11 | high_proximity_leader_rotation · 5.4%/yr · DD -38.5% | sector_roc_rotation · 7.1%/yr · DD -20.3% | sector_roc_rotation · 5.3%/yr · DD -16.6% |
| base: basket of 8 | downside_risk_weighted_momentum · 8.9%/yr · DD -25.7% | multi_horizon_rank_rotation · 8.8%/yr · DD -23.5% | low_correlation_momentum_selection · 8.9%/yr · DD -26.1% |

## All variants

| strategy | symbols | profile | IS %/yr | OOS %/yr | conservative %/yr | worst DD % | size for ~10% DD | win % IS/OOS | trades IS/OOS | signal now | file |
|---|---|---|---|---|---|---|---|---|---|---|---|
| crypto_equal_weight_rebalance | BTCUSDT,ETHUSDT,LTCUSDT,SOLUSDT | max-income | 46.2 | 14.2 | 14.2 | -70.9 | 14% | 32/34 | 139/70 | flat | [crypto_equal_weight_rebalance__max-income__v001.md](crypto_equal_weight_rebalance/crypto_equal_weight_rebalance__max-income__v001.md) |
| drawdown_defensive_switch | IEF,SPY | max-income | 10.4 | 13.2 | 10.4 | -22.5 | 44% | 65/67 | 17/15 | long SPY | [drawdown_defensive_switch__max-income__v002.md](drawdown_defensive_switch/drawdown_defensive_switch__max-income__v002.md) |
| crypto_equal_weight_rebalance | BTCUSDT,ETHUSDT,LTCUSDT,SOLUSDT | safe-starter | 38.1 | 9.6 | 9.6 | -58.2 | 17% | 30/41 | 180/90 | flat | [crypto_equal_weight_rebalance__safe-starter__v001.md](crypto_equal_weight_rebalance/crypto_equal_weight_rebalance__safe-starter__v001.md) |
| low_correlation_momentum_selection | base: basket of 8 | safe-starter | 8.9 | 9.2 | 8.9 | -26.1 | 38% | 47/53 | 116/102 | long DBC | [low_correlation_momentum_selection__safe-starter__v002.md](low_correlation_momentum_selection/low_correlation_momentum_selection__safe-starter__v002.md) |
| downside_risk_weighted_momentum | base: basket of 8 | max-income | 11.4 | 8.9 | 8.9 | -25.7 | 39% | 62/60 | 99/89 | long DBC, EFA, SPY | [downside_risk_weighted_momentum__max-income__v001.md](downside_risk_weighted_momentum/downside_risk_weighted_momentum__max-income__v001.md) |
| multi_horizon_rank_rotation | base: basket of 8 | balanced | 9.7 | 8.8 | 8.8 | -23.5 | 42% | 55/45 | 109/111 | long DBC, SPY, VNQ | [multi_horizon_rank_rotation__balanced__v001.md](multi_horizon_rank_rotation/multi_horizon_rank_rotation__balanced__v001.md) |
| vol_adjusted_momentum_rotation | base: basket of 8 | max-income | 11.2 | 8.3 | 8.3 | -25.8 | 39% | 59/54 | 129/127 | long DBC, TLT | [vol_adjusted_momentum_rotation__max-income__v001.md](vol_adjusted_momentum_rotation/vol_adjusted_momentum_rotation__max-income__v001.md) |
| drawdown_defensive_switch | IEF,SPY | safe-starter | 8.2 | 9.0 | 8.2 | -13.3 | 75% | 77/68 | 26/22 | long SPY | [drawdown_defensive_switch__safe-starter__v001.md](drawdown_defensive_switch/drawdown_defensive_switch__safe-starter__v001.md) |
| single_etf_volatility_target | SPY | max-income | 10.8 | 8.1 | 8.1 | -25.4 | 39% | 69/67 | 16/12 | long SPY | [single_etf_volatility_target__max-income__v002.md](single_etf_volatility_target/single_etf_volatility_target__max-income__v002.md) |
| trend_equal_weight_global | base: basket of 8 | max-income | 9.1 | 7.8 | 7.8 | -22.1 | 45% | 48/45 | 118/120 | long DBC, SPY | [trend_equal_weight_global__max-income__v001.md](trend_equal_weight_global/trend_equal_weight_global__max-income__v001.md) |
| multi_horizon_rank_rotation | base: basket of 8 | max-income | 13.1 | 7.7 | 7.7 | -26.2 | 38% | 58/52 | 115/122 | long DBC, EFA, SPY | [multi_horizon_rank_rotation__max-income__v001.md](multi_horizon_rank_rotation/multi_horizon_rank_rotation__max-income__v001.md) |
| inverse_volatility_trend_basket | base: basket of 8 | balanced | 7.7 | 7.7 | 7.7 | -21.7 | 46% | 47/46 | 88/93 | long DBC, SPY, VNQ | [inverse_volatility_trend_basket__balanced__v002.md](inverse_volatility_trend_basket/inverse_volatility_trend_basket__balanced__v002.md) |
| dual_momentum_allocation | EFA,IEF,SPY | balanced | 12.2 | 7.5 | 7.5 | -24.6 | 41% | 67/69 | 18/26 | long EFA | [dual_momentum_allocation__balanced__v001.md](dual_momentum_allocation/dual_momentum_allocation__balanced__v001.md) |
| sector_roc_rotation | base: basket of 11 | balanced | 9.0 | 7.1 | 7.1 | -20.3 | 49% | 68/54 | 160/179 | long XLB, XLE, XLF, XLP, XLRE, XLV | [sector_roc_rotation__balanced__v002.md](sector_roc_rotation/sector_roc_rotation__balanced__v002.md) |
| inverse_volatility_trend_basket | base: basket of 8 | max-income | 8.0 | 7.0 | 7.0 | -26.0 | 38% | 45/46 | 96/101 | long DBC, EFA, SPY, VNQ | [inverse_volatility_trend_basket__max-income__v002.md](inverse_volatility_trend_basket/inverse_volatility_trend_basket__max-income__v002.md) |
| drawdown_defensive_switch | IEF,SPY | balanced | 9.9 | 7.0 | 7.0 | -25.4 | 39% | 76/62 | 25/24 | long SPY | [drawdown_defensive_switch__balanced__v002.md](drawdown_defensive_switch/drawdown_defensive_switch__balanced__v002.md) |
| trend_equal_weight_global | base: basket of 8 | balanced | 8.7 | 6.9 | 6.9 | -26.2 | 38% | 46/46 | 101/104 | long DBC, EFA, SPY, VNQ | [trend_equal_weight_global__balanced__v001.md](trend_equal_weight_global/trend_equal_weight_global__balanced__v001.md) |
| low_correlation_momentum_selection | base: basket of 8 | max-income | 12.8 | 6.6 | 6.6 | -24.7 | 41% | 61/47 | 85/90 | long DBC | [low_correlation_momentum_selection__max-income__v001.md](low_correlation_momentum_selection/low_correlation_momentum_selection__max-income__v001.md) |
| dual_momentum_allocation | EFA,IEF,SPY | max-income | 12.5 | 6.2 | 6.2 | -27.6 | 36% | 65/70 | 20/27 | long EFA | [dual_momentum_allocation__max-income__v001.md](dual_momentum_allocation/dual_momentum_allocation__max-income__v001.md) |
| dual_momentum_allocation | EFA,IEF,SPY | safe-starter | 12.5 | 6.2 | 6.2 | -27.6 | 36% | 65/70 | 20/27 | long EFA | [dual_momentum_allocation__safe-starter__v001.md](dual_momentum_allocation/dual_momentum_allocation__safe-starter__v001.md) |
| low_correlation_momentum_selection | base: basket of 8 | balanced | 12.0 | 6.1 | 6.1 | -24.7 | 41% | 62/47 | 84/89 | long DBC | [low_correlation_momentum_selection__balanced__v001.md](low_correlation_momentum_selection/low_correlation_momentum_selection__balanced__v001.md) |
| stock_bond_paired_switch | SPY,TLT | safe-starter | 5.7 | 8.3 | 5.7 | -27.5 | 36% | 62/50 | 24/18 | long SPY | [stock_bond_paired_switch__safe-starter__v001.md](stock_bond_paired_switch/stock_bond_paired_switch__safe-starter__v001.md) |
| high_proximity_leader_rotation | base: basket of 11 | balanced | 5.5 | 8.5 | 5.5 | -38.2 | 26% | 59/60 | 235/205 | long XLB, XLE, XLF, XLP, XLV | [high_proximity_leader_rotation__balanced__v002.md](high_proximity_leader_rotation/high_proximity_leader_rotation__balanced__v002.md) |
| stock_bond_paired_switch | SPY,TLT | balanced | 6.2 | 5.5 | 5.5 | -29.8 | 34% | 57/48 | 46/42 | long TLT | [stock_bond_paired_switch__balanced__v001.md](stock_bond_paired_switch/stock_bond_paired_switch__balanced__v001.md) |
| high_proximity_leader_rotation | base: basket of 11 | max-income | 5.4 | 9.5 | 5.4 | -38.5 | 26% | 59/57 | 202/185 | long XLB, XLE, XLF, XLP, XLV | [high_proximity_leader_rotation__max-income__v002.md](high_proximity_leader_rotation/high_proximity_leader_rotation__max-income__v002.md) |
| consistent_winner_rotation | base: basket of 11 | max-income | 5.3 | 9.8 | 5.3 | -35.6 | 28% | 51/52 | 165/152 | long XLE, XLF, XLP, XLV | [consistent_winner_rotation__max-income__v002.md](consistent_winner_rotation/consistent_winner_rotation__max-income__v002.md) |
| consistent_winner_rotation | base: basket of 11 | balanced | 5.3 | 9.4 | 5.3 | -35.6 | 28% | 51/52 | 165/151 | long XLE, XLF, XLP, XLV | [consistent_winner_rotation__balanced__v002.md](consistent_winner_rotation/consistent_winner_rotation__balanced__v002.md) |
| sector_roc_rotation | base: basket of 11 | safe-starter | 5.3 | 5.7 | 5.3 | -16.6 | 60% | 29/27 | 325/310 | long XLB, XLE, XLF, XLP, XLU, XLV | [sector_roc_rotation__safe-starter__v002.md](sector_roc_rotation/sector_roc_rotation__safe-starter__v002.md) |
| stock_bond_paired_switch | SPY,TLT | max-income | 10.0 | 5.2 | 5.2 | -23.3 | 43% | 61/52 | 28/31 | long SPY | [stock_bond_paired_switch__max-income__v001.md](stock_bond_paired_switch/stock_bond_paired_switch__max-income__v001.md) |
| vol_adjusted_momentum_rotation | base: basket of 8 | balanced | 10.2 | 5.2 | 5.2 | -27.0 | 37% | 64/53 | 103/90 | long DBC, EFA, SPY, VNQ | [vol_adjusted_momentum_rotation__balanced__v001.md](vol_adjusted_momentum_rotation/vol_adjusted_momentum_rotation__balanced__v001.md) |
| monthly_loser_rebound_basket | base: basket of 11 | max-income | 5.2 | 8.6 | 5.2 | -34.3 | 29% | 65/63 | 320/294 | long XLB, XLF, XLK, XLRE, XLY | [monthly_loser_rebound_basket__max-income__v001.md](monthly_loser_rebound_basket/monthly_loser_rebound_basket__max-income__v001.md) |
| monthly_loser_rebound_basket | base: basket of 11 | balanced | 5.0 | 8.7 | 5.0 | -38.9 | 26% | 65/62 | 313/292 | long XLB, XLF, XLK, XLRE, XLY | [monthly_loser_rebound_basket__balanced__v001.md](monthly_loser_rebound_basket/monthly_loser_rebound_basket__balanced__v001.md) |
| equal_risk_contribution_trend | base: basket of 8 | balanced | 6.2 | 4.8 | 4.8 | -26.0 | 38% | 48/41 | 126/128 | long DBC, EFA, SPY, VNQ | [equal_risk_contribution_trend__balanced__v002.md](equal_risk_contribution_trend/equal_risk_contribution_trend__balanced__v002.md) |
| sector_roc_rotation | base: basket of 11 | max-income | 11.5 | 4.5 | 4.5 | -29.2 | 34% | 63/49 | 59/49 | long XLE | [sector_roc_rotation__max-income__v002.md](sector_roc_rotation/sector_roc_rotation__max-income__v002.md) |
| equal_risk_contribution_trend | base: basket of 8 | max-income | 6.5 | 4.4 | 4.4 | -30.1 | 33% | 44/41 | 102/107 | long DBC, EFA, SPY, VNQ | [equal_risk_contribution_trend__max-income__v001.md](equal_risk_contribution_trend/equal_risk_contribution_trend__max-income__v001.md) |
| minimum_variance_trend_basket | base: basket of 8 | max-income | 5.7 | 3.5 | 3.5 | -28.5 | 35% | 51/43 | 81/103 | long DBC, EFA, SPY, VNQ | [minimum_variance_trend_basket__max-income__v001.md](minimum_variance_trend_basket/minimum_variance_trend_basket__max-income__v001.md) |
| minimum_variance_trend_basket | base: basket of 8 | balanced | 5.6 | 3.4 | 3.4 | -32.4 | 31% | 51/47 | 84/106 | long DBC, EFA, SPY, VNQ | [minimum_variance_trend_basket__balanced__v001.md](minimum_variance_trend_basket/minimum_variance_trend_basket__balanced__v001.md) |
| downside_risk_weighted_momentum | base: basket of 8 | balanced | 7.8 | 3.0 | 3.0 | -28.0 | 36% | 57/44 | 77/68 | long DBC, EEM, EFA, SPY, VNQ | [downside_risk_weighted_momentum__balanced__v002.md](downside_risk_weighted_momentum/downside_risk_weighted_momentum__balanced__v002.md) |
| single_etf_volatility_target | SPY | safe-starter | 2.1 | 2.2 | 2.1 | -5.4 | 100% | 79/46 | 19/13 | long SPY | [single_etf_volatility_target__safe-starter__v002.md](single_etf_volatility_target/single_etf_volatility_target__safe-starter__v002.md) |
| single_etf_volatility_target | SPY | balanced | 2.2 | 2.1 | 2.1 | -5.0 | 100% | 72/50 | 25/16 | long SPY | [single_etf_volatility_target__balanced__v002.md](single_etf_volatility_target/single_etf_volatility_target__balanced__v002.md) |
| half_life_filtered_pairs | EWA,EWC | max-income | 0.8 | 0.2 | 0.2 | -14.1 | 71% | 61/58 | 57/36 | flat | [half_life_filtered_pairs__max-income__v002.md](half_life_filtered_pairs/half_life_filtered_pairs__max-income__v002.md) |
| half_life_filtered_pairs | EWA,EWC | balanced | 0.7 | 0.2 | 0.2 | -12.0 | 84% | 64/58 | 55/36 | flat | [half_life_filtered_pairs__balanced__v001.md](half_life_filtered_pairs/half_life_filtered_pairs__balanced__v001.md) |
| ratio_zscore_pairs | KO,PEP | max-income | 0.7 | 0.2 | 0.2 | -11.1 | 90% | 70/58 | 23/33 | flat | [ratio_zscore_pairs__max-income__v002.md](ratio_zscore_pairs/ratio_zscore_pairs__max-income__v002.md) |
| ratio_zscore_pairs | KO,PEP | balanced | 0.7 | 0.2 | 0.2 | -11.1 | 90% | 70/58 | 23/33 | flat | [ratio_zscore_pairs__balanced__v002.md](ratio_zscore_pairs/ratio_zscore_pairs__balanced__v002.md) |
