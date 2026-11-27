CONFIG = {
    "name": "three_bar_momentum_thrust",
    "asset_class": "crypto",
    "symbols": ["SOLUSDT"],           # spec: SOL/USD
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
    "roc": 4.0,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 48,
}

SPACE = {
    "roc": {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.0},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 24, "max": 96, "step": 9, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def buy_signal(df, p):
    c, o = df["close"], df["open"]
    up = c > o
    _, _, adx = dmi(df, 14)
    return (up & up.shift(1, fill_value=False) & up.shift(2, fill_value=False)
            & (c > c.shift(1)) & (c.shift(1) > c.shift(2)) & (roc(c, 3) > p["roc"]) & (adx > 20))


def sell_signal(df, p):
    return df["close"] < df["low"].shift(1)
