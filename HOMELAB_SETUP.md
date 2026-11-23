# Homelab Setup: Market Data Pipeline (Crypto, ETFs, yfinance)

Instructions for **Claude Code** running on an **Ubuntu Server** homelab.
Goal: install Docker and build a data pipeline that collects **free** historical and live
**1-minute bars** for crypto and ETFs. This is phase 1 of an automated trading project
(paper trading only, no broker, no exchange account, no API keys).

> Ask the user before any `sudo` step, and confirm each phase works before moving on.

---

## 0. Context and constraints

- **Paper trading only.** Orders are simulated locally. No broker or exchange API keys are needed.
- **Bar size:** 1 minute (1m). Also keep daily bars for long-horizon tests.
- **Open decisions (keep asking the user, don't guess):**
  1. Which coins and ETFs to trade → use the *placeholder* list in `config/symbols.yaml` for now.
  2. Virtual starting capital and base currency (CHF/USD).
  3. Which strategies to test first.
  4. Tiingo free account → postponed; don't use Tiingo yet.
- **Store all timestamps in UTC.**
- **Before any real-money trading:** remind the user to check Swiss tax rules
  (professional securities trader status, ESTV circular KS 36).

### Data sources

| Asset | History | Live | Account / key |
|---|---|---|---|
| Crypto | Binance public archive `data.binance.vision`: 1m klines, monthly/daily zip files, ~2017 → today | Binance public websocket `wss://data-stream.binance.vision:443/ws/<symbol>@kline_1m` | None |
| ETFs / indices | Yahoo Finance via `yfinance`: daily bars for decades | `yfinance` 1m bars, polled | None |

**Important limitation (yfinance minute data):** Yahoo only serves 1m bars for roughly the
**last 30 days**, at most about **7 days per request**. Longer intervals go further back
(2m–30m about 60 days, 1h about 730 days). There is **no free multi-year 1m ETF history**.
Strategy: download daily history once, then run a **collector that saves 1m bars every day**
so we build our own minute archive from now on. Verify these limits when implementing,
because yfinance changes often.

yfinance is unofficial and rate-limited. Always cache to disk, add backoff on HTTP 429, and
never re-download data we already have.

---

## 1. Install Docker (ask before running sudo)

Use Docker's official apt repository (not the `docker.io` snap):

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER   # user must log out and back in
```

Check: `docker run --rm hello-world` and `docker compose version`.

Also make sure the clock is synced (needed for correct timestamps):
`timedatectl` should show `System clock synchronized: yes`.

---

## 2. Project layout

Create in `~/trading`:

```
~/trading/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example            # no secrets needed yet
├── config/
│   └── symbols.yaml
├── data/                   # mounted volume, NOT in git
│   ├── raw/binance/        # downloaded zips (can be deleted after conversion)
│   ├── crypto/1m/          # Parquet, partitioned by symbol/year/month
│   ├── etf/1d/             # Parquet, one file per ticker
│   └── etf/1m/             # Parquet, partitioned by ticker/date
├── src/
│   ├── common/storage.py       # read/write Parquet, deduplicate, gap check
│   ├── collectors/
│   │   ├── binance_history.py  # backfill from data.binance.vision
│   │   ├── binance_live.py     # websocket → 1m bars
│   │   ├── yahoo_daily.py      # full daily history
│   │   └── yahoo_intraday.py   # 1m bars of last ~7 days, run daily
│   └── tools/check_data.py     # print coverage, gaps, row counts
└── logs/
```

Initialise a git repo, with `data/`, `logs/` and `.env` in `.gitignore`.

### `config/symbols.yaml` (placeholder, user hasn't decided yet)

```yaml
# PLACEHOLDER: replace when the user picks the asset universe
crypto:            # Binance spot pairs, quote = USDT
  - BTCUSDT
  - ETHUSDT
etf:               # Yahoo tickers
  - SPY            # US S&P 500 ETF (fine for data/backtests)
  - QQQ
  - CSSPX.SW       # iShares Core S&P 500 UCITS on SIX (tradable for Swiss residents)
  - ^GSPC          # S&P 500 index, long daily history
crypto_history_start: 2017-08
```

### `requirements.txt`

```
pandas
pyarrow
requests
websockets
yfinance
pyyaml
tenacity      # retries / backoff
```

### Docker

- `Dockerfile`: `python:3.12-slim`, install requirements, `WORKDIR /app`, copy `src/` and `config/`.
- `docker-compose.yml` services, all mounting `./data:/app/data` and `./logs:/app/logs`, `TZ=UTC`:
  - `binance-live`: `python -m src.collectors.binance_live`, `restart: unless-stopped`
  - `yahoo-intraday`: run on a schedule (see step 6)
  - one-off jobs run with `docker compose run --rm <service> ...`

---

## 3. Crypto history: Binance public archive

URL patterns (no account needed):

```
Monthly: https://data.binance.vision/data/spot/monthly/klines/<SYMBOL>/1m/<SYMBOL>-1m-<YYYY>-<MM>.zip
Daily:   https://data.binance.vision/data/spot/daily/klines/<SYMBOL>/1m/<SYMBOL>-1m-<YYYY-MM-DD>.zip
Checksum: same URL + ".CHECKSUM"  (SHA256)
```

`binance_history.py` must:
1. For each symbol, download all **monthly** files from `crypto_history_start` to last month,
   then **daily** files for the current month.
2. Verify the SHA256 checksum, and skip months already present in Parquet.
3. Parse the CSV (no header). Columns: `open_time, open, high, low, close, volume, close_time,
   quote_volume, trades, taker_buy_base, taker_buy_quote, ignore`.
   **Timestamp gotcha:** older files use milliseconds, newer spot files may use
   **microseconds**. Detect it by magnitude and convert to UTC datetime.
4. Write Parquet to `data/crypto/1m/symbol=<S>/year=<Y>/month=<M>/`.
5. Treat 404s as "no data" (pair not listed yet) and continue.

Check: `check_data.py` shows BTCUSDT 1m from 2017-08 to yesterday with a gap count.

## 4. Crypto live: Binance public websocket

`binance_live.py`:
- Connect to `wss://data-stream.binance.vision:443/stream?streams=btcusdt@kline_1m/ethusdt@kline_1m`
  (symbols lowercase, from config).
- Only store a bar when the kline's `x` (is closed) field is `true`.
- Append to the same Parquet layout (buffer, flush every few minutes), deduplicated on `open_time`.
- Reconnect with exponential backoff, and log disconnects.
- On startup, fill any gap since the last stored bar with the public REST endpoint
  `https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1m&startTime=...&limit=1000`
  (no key needed).

Check: after 10 minutes, new 1m bars appear and `check_data.py` shows no gap.

## 5. ETF daily history: yfinance

`yahoo_daily.py`:
- `yf.download(ticker, period="max", interval="1d", auto_adjust=False, actions=True)`.
  Keep both `Close` and `Adj Close`, plus dividends and splits.
- One ticker at a time, a few seconds of sleep between tickers, retry with backoff on rate limits.
- Save to `data/etf/1d/<ticker>.parquet`. On re-runs, only fetch the missing tail.

## 6. ETF minute bars: daily collector

`yahoo_intraday.py`:
- For each ticker: `yf.download(ticker, period="7d", interval="1m", prepost=False)`.
- Convert to UTC, merge into `data/etf/1m/ticker=<T>/date=<D>/`, deduplicated on timestamp.
- Run it **every day** after the US close (around 22:30 UTC) through a **systemd timer** or cron
  calling `docker compose run --rm yahoo-intraday`. If a run fails, the next run fills the gap
  (7-day window), but alert in the log after 5 days without success.
- On the first run, also save `period="30d"` in 7-day chunks to get as much history as possible.

## 7. Verification (`check_data.py`)

For every symbol, print: first and last timestamp, row count, number of gaps over 1 minute
during market hours (crypto: 24/7; ETFs: exchange hours only), and size on disk.
Run it at the end of setup and show the output to the user.

---

## 8. Done when

- [ ] Docker and the compose plugin are installed, and the clock is synced
- [ ] Crypto 1m history backfilled for the placeholder symbols
- [ ] `binance-live` container running and surviving a restart
- [ ] ETF daily history saved
- [ ] Daily ETF 1m collector scheduled and run once successfully
- [ ] `check_data.py` report shown to the user

## Next phases (don't build yet)

1. Backtesting engine on the stored Parquet data (fees and slippage included)
2. Paper-trading engine: live data → strategy → simulated orders → portfolio log
3. Risk limits and kill switch (max loss per day/trade/total), plus alerts
4. Real trading only after long paper results, **and after the Swiss tax check**
