CONFIG = {
    "name": "stochrsi_reset",
    "asset_class": "crypto",
    "symbols": ["BTCUSDT"],           # spec: BTC/USD
    "timeframe": "4h",              # spec signal timeframe, built per coin from Binance 1m bars (UTC)
    "start": "2018-01-01",
    "oos_start": "2024-01-01",      # repo precedent for crypto strategies
    "end": "2026-11-23",            # frozen at setup: last complete UTC day
    "capital": 10_000.0,
    "position_pct": 1.0,            # user's choice: 100% of equity (spec's risk_fraction sizing not used)
    "fee_pct": 0.10,                # spec: 10 bp commission per side
    "slippage_pct": 0.10,           # spec: 5 bp half-spread + 5 bp adverse slippage per fill
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 1000,             # >= 5x the longest recursive indicator period (EXECUTION.md warm-up)
}

PARAMS = {
    "n": 14, "level": 0.2,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 12,
}

SPACE = {
    "n": {"min": 7, "max": 28, "step": 1, "hard_min": 2},
    "level": {"min": 0.1, "max": 0.3, "step": 0.025, "hard_min": 0.0, "hard_max": 0.75},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 6, "max": 24, "step": 2, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def buy_signal(df, p):
    # assumption: the spec's single lookback n applies to StochRSI(n) and its RSI(n) filter
    c = df["close"]
    return cross_above(stoch_rsi(df, p["n"]), p["level"]) & (rsi_c(df, p["n"]) > 40) & (c > ema(c, 200))


def sell_signal(df, p):
    return stoch_rsi(df, p["n"]) > 0.8
