CONFIG = {
    "name": "macd_zero_cross",
    "asset_class": "crypto",
    "symbols": ["ETHUSDT"],           # spec: ETH/USD
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
    "fast": 12, "slow": 26,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 96,
}

SPACE = {
    "fast": {"min": 6, "max": 18, "step": 1, "hard_min": 2},
    "slow": {"min": 20, "max": 50, "step": 2, "hard_min": 3},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 48, "max": 192, "step": 18, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return p["fast"] < p["slow"]


def _macd(df, p):
    return _memo(("macd", id(df), int(p["fast"]), int(p["slow"])),
                 lambda: ema(df["close"], p["fast"]) - ema(df["close"], p["slow"]))


def buy_signal(df, p):
    return cross_above(_macd(df, p), 0.0)


def sell_signal(df, p):
    return _macd(df, p) < 0
