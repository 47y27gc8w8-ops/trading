"""Paper-trading bots ("brokers"): one bot per strategy variant, all sharing src/brokers/base.py.

PAPER ONLY. Nothing in this package can place a real order: there are no broker or exchange
accounts, no API keys, and market data comes from public endpoints (Binance klines via ccxt,
Yahoo Finance via yfinance). Fills are simulated against the latest price.
"""
