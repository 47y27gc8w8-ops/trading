CONFIG = {
    "name": "ema_price_reclaim",
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
    "n": 100,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 96,
}

SPACE = {
    "n": {"min": 50, "max": 200, "step": 10, "hard_min": 2},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 48, "max": 192, "step": 18, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def buy_signal(df, p):
    c = df["close"]
    e = ema(c, p["n"])
    return cross_above(c, e) & (e > e.shift(5))


def sell_signal(df, p):
    return df["close"] < ema(df["close"], p["n"])
