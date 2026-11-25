CONFIG = {
    "name": "rsi_dip_trend_filter",
    "asset_class": "crypto",
    "symbols": ["BTCUSDT"],           # spec: BTC/USD (ETH/USD = alternative, covered by screening)
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
    "n": 14, "buy": 30, "exit": 55,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 12,
}

SPACE = {
    "n": {"min": 7, "max": 21, "step": 1, "hard_min": 2},
    "buy": {"min": 20, "max": 40, "step": 2, "hard_min": 1, "hard_max": 99},
    "exit": {"min": 45, "max": 70, "step": 5, "hard_min": 1, "hard_max": 99},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 6, "max": 24, "step": 2, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return p["buy"] < p["exit"]


def buy_signal(df, p):
    c = df["close"]
    return (rsi_c(df, p["n"]) < p["buy"]) & (c > sma(c, 200))


def sell_signal(df, p):
    return rsi_c(df, p["n"]) > p["exit"]
