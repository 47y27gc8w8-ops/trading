CONFIG = {
    "name": "inside_bar_breakout",
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
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 48,
}

SPACE = {
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 24, "max": 96, "step": 9, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def buy_signal(df, p):
    h, l = df["high"], df["low"]
    return (h.shift(1) < h.shift(2)) & (l.shift(1) > l.shift(2)) & (df["close"] > h.shift(2))


def sell_signal(df, p):
    # spec: "C < L[2]", read literally as a rolling condition (not frozen at the mother bar)
    return df["close"] < df["low"].shift(2)
