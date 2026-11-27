"""Common base of every paper bot: simulated fills, CHF accounting, SQLite, logging, main loop.

Only the strategy differs between bots (see engine.Strategy). PAPER ONLY: a "fill" is a row in
SQLite priced at the latest public market price; nothing is ever sent to a broker or exchange.

Cycle (every 60 s for crypto, every 120 s for ETFs while NYSE is open):
  1. update bars (stored history + live tail) and run the strategy's simulation,
  2. compare the simulated open positions with the bot's paper positions; a change must be seen
     in two consecutive cycles before it is traded (guards against a data blip),
  3. sell what the strategy no longer holds, then buy new positions at the strategy's weight of
     the bot's current equity (0.1 % fee and 0.05 % slippage on every fill),
  4. write equity + heartbeat.
ETF bots idle outside NYSE hours (no data calls; equity is still recorded every minute).
Every decision is also written to the structured journal (src/brokers/journal.py) for later analysis.
A failing data source is retried with backoff (market.retry), then the cycle is skipped and
the next one waits longer (up to 15 min); the process never exits because of a data error.
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import logging
import logging.handlers
import signal
import sys
import time
import traceback
from datetime import datetime, timezone

from src.brokers import db, journal, market
from src.brokers.engine import Strategy
from src.brokers.market import DataError

FX_TTL = 15 * 60
MIN_TRADE_CHF = 5.0


def setup_logging(bot_id: str) -> logging.Logger:
    d = db.ROOT / "logs" / "brokers"
    d.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)sZ %(levelname)s %(name)s: %(message)s", "%Y-%m-%dT%H:%M:%S")
    fmt.converter = time.gmtime
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    for h in (logging.StreamHandler(sys.stdout),
              logging.handlers.RotatingFileHandler(d / f"{bot_id}.log", maxBytes=5_000_000, backupCount=5)):
        h.setFormatter(fmt)
        root.addHandler(h)
    for noisy in ("yfinance", "urllib3", "peewee", "ccxt"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    return logging.getLogger(f"brokers.{bot_id}")


class Bot:
    def __init__(self, cfg: dict, bot: dict):
        self.id = bot["id"]
        self.cfg, self.bot = cfg, bot
        self.log = setup_logging(self.id)
        self.fee = float(cfg.get("fee_pct", 0.10)) / 100
        self.slip = float(cfg.get("slippage_pct", 0.05)) / 100
        self.start_balance = float(cfg.get("start_balance_chf", 10_000))
        self.strategy = Strategy(bot["strategy"], bot.get("params") or {}, bot["symbols"])
        self.crypto = self.strategy.asset_class == "crypto"
        self.con = db.connect()
        self.fx, self.fx_at = None, 0.0
        self.pending: dict | None = None      # target signature seen once, awaiting confirmation
        self.fail_streak = 0
        self.stop = False
        self.last_bar: dict[str, str] = {}     # last completed bar per symbol (journal snapshots)
        self.sim_seen: set | None = None      # closed simulated trades already journaled
        self.market_open: bool | None = None
        self.stats = self._new_stats()
        self._register()
        market.on_retry = lambda what, err, k, wait: self.journal(
            "retry", {"source": what, "error": err, "attempt": k, "wait_s": wait})
        self.journal("start", {"strategy": bot["strategy"], "profile": bot.get("profile"), "params": bot.get("params"),
                               "symbols": bot["symbols"], "asset_class": self.strategy.asset_class,
                               "timeframe": self.strategy.timeframe, "per_symbol_sizing": self.strategy.per_symbol,
                               "fee_pct": self.fee * 100, "slippage_pct": self.slip * 100, "code": self._code_hashes()})

    # ------------------------------------------------------------------ db ---
    def _register(self) -> None:
        b, s = self.bot, self.strategy
        with self.con:
            self.con.execute(
                "INSERT INTO bots(id, strategy, profile, asset_class, timeframe, symbols, params, variant_file, backtest,"
                " start_balance, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
                " ON CONFLICT(id) DO UPDATE SET strategy=excluded.strategy, profile=excluded.profile,"
                " asset_class=excluded.asset_class, timeframe=excluded.timeframe, symbols=excluded.symbols,"
                " params=excluded.params, variant_file=excluded.variant_file, backtest=excluded.backtest",
                (self.id, b["strategy"], b.get("profile"), s.asset_class, s.timeframe, json.dumps(b["symbols"]),
                 json.dumps(b.get("params") or {}), b.get("variant_file"), json.dumps(b.get("backtest") or {}),
                 self.start_balance, db.now_iso()))
            self.con.execute(
                "INSERT INTO state(bot_id, cash, status, message, started_at, heartbeat) VALUES (?,?,?,?,?,?)"
                " ON CONFLICT(bot_id) DO UPDATE SET status=excluded.status, message=excluded.message,"
                " started_at=excluded.started_at, heartbeat=excluded.heartbeat",
                (self.id, self.start_balance, "starting", "starting", db.now_iso(), db.now_iso()))
            row = self.con.execute("SELECT fx_usdchf FROM state WHERE bot_id=?", (self.id,)).fetchone()
            self.fx = row["fx_usdchf"] if row else None
        self.event("info", "start", f"started ({self.strategy.asset_class} {self.strategy.timeframe}, "
                                    f"{len(self.bot['symbols'])} symbols)")

    def event(self, level: str, kind: str, msg: str) -> None:
        getattr(self.log, "error" if level == "error" else level)(msg)
        with self.con:
            self.con.execute("INSERT INTO events(bot_id, ts, level, kind, message) VALUES (?,?,?,?,?)",
                             (self.id, db.now_iso(), level, kind, msg[:2000]))

    def journal(self, kind: str, data: dict) -> None:
        try:
            journal.write(self.con, self.id, db.now_iso(), kind, data)
        except Exception:  # noqa: BLE001 - the journal must never stop trading
            self.log.exception("journal write failed (%s)", kind)

    def _code_hashes(self) -> dict:
        h = lambda paths: hashlib.sha1(b"".join(p.read_bytes() for p in paths)).hexdigest()[:12]  # noqa: E731
        return {"strategy": h([self.strategy.path]), "brokers": h(sorted((db.ROOT / "src" / "brokers").glob("*.py")))}

    @staticmethod
    def _new_stats() -> dict:
        return {"hour": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H"), "ok": 0, "failed": 0, "idle": 0,
                "data_ms": [], "sim_ms": []}

    def _stats_tick(self, outcome: str, data_ms: float | None = None, sim_ms: float | None = None) -> None:
        hour = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H")
        st = self.stats
        if hour != st["hour"]:
            ms = lambda xs: {"avg": round(sum(xs) / len(xs)), "max": round(max(xs))} if xs else None  # noqa: E731
            self.journal("stats", {"hour": st["hour"], "ok": st["ok"], "failed": st["failed"], "idle": st["idle"],
                                   "data_ms": ms(st["data_ms"]), "sim_ms": ms(st["sim_ms"])})
            self.stats = st = self._new_stats()
        st[outcome] += 1
        if data_ms is not None:
            st["data_ms"].append(data_ms)
            st["sim_ms"].append(sim_ms)

    def cash(self) -> float:
        return float(self.con.execute("SELECT cash FROM state WHERE bot_id=?", (self.id,)).fetchone()["cash"])

    def positions(self) -> dict[str, dict]:
        rows = self.con.execute("SELECT * FROM positions WHERE bot_id=?", (self.id,)).fetchall()
        return {r["symbol"]: dict(r) for r in rows}

    def equity(self, prices: dict[str, float] | None = None) -> float:
        fx = self.fx or 0.0
        value = 0.0
        for s, p in self.positions().items():
            px = (prices or {}).get(s) or p["last_price_usd"] or p["avg_price_usd"]
            value += p["qty"] * px * fx
        return self.cash() + value

    def set_status(self, status: str, message: str) -> None:
        with self.con:
            self.con.execute("UPDATE state SET status=?, message=?, heartbeat=?, fx_usdchf=? WHERE bot_id=?",
                             (status, message[:500], db.now_iso(), self.fx, self.id))

    def record_equity(self, prices: dict[str, float] | None = None) -> float:
        eq = self.equity(prices)
        ts = datetime.now(timezone.utc).replace(second=0).strftime("%Y-%m-%dT%H:%M:%SZ")  # one row per minute
        with self.con:
            if prices:
                for s, px in prices.items():
                    self.con.execute("UPDATE positions SET last_price_usd=? WHERE bot_id=? AND symbol=?", (px, self.id, s))
            self.con.execute("INSERT OR REPLACE INTO equity(bot_id, ts, equity, cash) VALUES (?,?,?,?)",
                             (self.id, ts, eq, self.cash()))
            self.con.execute("UPDATE state SET peak = max(coalesce(peak, ?), ?) WHERE bot_id=?", (self.start_balance, eq, self.id))
            self.con.execute("UPDATE state SET max_dd = min(coalesce(max_dd, 0), ? / peak - 1) WHERE bot_id=?", (eq, self.id))
        return eq

    # --------------------------------------------------------------- fills ---
    def fill(self, symbol: str, side: str, qty: float, ref_px: float, reason: str, sim_entry: str | None = None,
             sim_price: float | None = None, sim_time: str | None = None, adopt: bool = False) -> None:
        """Simulated fill: price moves against us by the slippage, fee on the notional, all in CHF."""
        px = ref_px * (1 + self.slip) if side == "buy" else ref_px * (1 - self.slip)
        notional = qty * px * self.fx
        fee = notional * self.fee
        pos = self.positions().get(symbol)
        now = db.now_iso()
        pnl = None
        with self.con:
            if side == "buy":
                self.con.execute("UPDATE state SET cash = cash - ? WHERE bot_id=?", (notional + fee, self.id))
                if pos:
                    q = pos["qty"] + qty
                    self.con.execute("UPDATE positions SET qty=?, avg_price_usd=?, cost=cost+?, sim_entry=?, last_price_usd=?"
                                     " WHERE bot_id=? AND symbol=?",
                                     (q, (pos["avg_price_usd"] * pos["qty"] + px * qty) / q, notional + fee, sim_entry,
                                      ref_px, self.id, symbol))
                else:
                    self.con.execute("INSERT INTO positions(bot_id, symbol, qty, avg_price_usd, cost, sim_entry, opened_at,"
                                     " last_price_usd) VALUES (?,?,?,?,?,?,?,?)",
                                     (self.id, symbol, qty, px, notional + fee, sim_entry, now, ref_px))
            else:
                frac = min(1.0, qty / pos["qty"])
                cost_part = pos["cost"] * frac
                pnl = notional - fee - cost_part
                self.con.execute("UPDATE state SET cash = cash + ? WHERE bot_id=?", (notional - fee, self.id))
                if frac >= 0.999999:
                    self.con.execute("DELETE FROM positions WHERE bot_id=? AND symbol=?", (self.id, symbol))
                else:
                    self.con.execute("UPDATE positions SET qty=qty-?, cost=cost-?, last_price_usd=? WHERE bot_id=? AND symbol=?",
                                     (qty, cost_part, ref_px, self.id, symbol))
            cur = self.con.execute("INSERT INTO trades(bot_id, ts, symbol, side, qty, price_usd, ref_price_usd, fx_usdchf,"
                                   " notional, fee, pnl, reason) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                                   (self.id, now, symbol, side, qty, px, ref_px, self.fx, notional, fee, pnl, reason))
        shortfall = delay = None
        if sim_price:
            shortfall = ((px / sim_price - 1) if side == "buy" else (sim_price / px - 1)) * 1e4
        if sim_time:
            try:
                delay = (datetime.now(timezone.utc) - datetime.fromisoformat(sim_time)).total_seconds()
            except ValueError:
                pass
        self.journal("fill", {"trade_id": cur.lastrowid, "symbol": symbol, "side": side, "qty": qty, "ref_price": ref_px,
                              "fill_price": px, "sim_price": sim_price, "sim_time": sim_time, "shortfall_bps": shortfall,
                              "delay_s": delay, "adopt": adopt, "fx": self.fx, "notional_chf": notional, "fee_chf": fee,
                              "pnl_chf": pnl, "reason": reason})
        self.log.info("PAPER %s %s %.8g @ %.6g USD (%.2f CHF, fee %.2f%s) - %s", side.upper(), symbol, qty, px, notional,
                      fee, f", P&L {pnl:+.2f}" if pnl is not None else "", reason)

    # ------------------------------------------------------------- trading ---
    def refresh_fx(self) -> None:
        if self.fx is None or time.time() - self.fx_at > FX_TTL:
            try:
                self.fx, self.fx_at = market.usdchf(), time.time()
            except DataError as ex:
                if self.fx is None:
                    raise
                self.event("warning", "data", f"USDCHF refresh failed, keeping {self.fx:.4f}: {ex}")
                self.fx_at = time.time()

    def rebalance(self, targets: dict[str, dict], last_exit: dict[str, dict], prices: dict[str, float]) -> None:
        held = self.positions()
        sig = {s: t["sim_entry"] for s, t in targets.items()}
        mine = {s: p["sim_entry"] for s, p in held.items()}
        if sig == mine:
            if self.pending is not None:
                self.journal("target_dropped", {"pending": self.pending, "held": mine})
            self.pending = None
            return
        if self.pending != sig:          # first sighting: wait one cycle to confirm
            if self.pending is not None:
                self.journal("target_dropped", {"pending": self.pending, "now": sig, "held": mine})
            self.pending = sig
            self.journal("target_seen", {"held": mine, "target": sig,
                                         "weights": {s: round(t["weight"], 4) for s, t in targets.items()}})
            self.log.info("target change seen, confirming next cycle: held=%s target=%s", mine, sig)
            return
        self.journal("target_confirmed", {"held": mine, "target": sig})
        self.pending = None
        # 1. exits and changed entries (the strategy re-entered or re-weighted): sell first
        for s, p in held.items():
            if s not in targets or targets[s]["sim_entry"] != p["sim_entry"]:
                sim = next((c for c in reversed(self.strategy.sim_closed)
                            if c["symbol"] == s and c["entry_time"] == p["sim_entry"]), None)
                why = (sim or last_exit.get(s) or {}).get("reason", "signal") if s not in targets \
                    else "strategy re-entered / re-weighted"
                self.fill(s, "sell", p["qty"], prices[s], f"exit: {why}",
                          sim_price=sim["exit_price"] if sim else None, sim_time=sim["exit_time"] if sim else None)
        # 2. entries at the strategy's weight of the bot's equity
        eq = self.equity(prices)
        first = not held and not self.con.execute("SELECT 1 FROM trades WHERE bot_id=? LIMIT 1", (self.id,)).fetchone()
        for s, t in sorted(targets.items(), key=lambda kv: -kv[1]["weight"]):
            if s in self.positions():
                continue
            cash = self.cash()
            want = min(t["weight"] * eq, cash / (1 + self.fee))
            if want < MIN_TRADE_CHF:
                continue
            ref = prices[s]
            qty = want / (ref * (1 + self.slip) * self.fx)
            since = t["sim_entry"][:16]
            self.fill(s, "buy", qty, ref, f"{'adopt' if first else 'entry'}: strategy long since {since} UTC, "
                                         f"weight {t['weight']:.1%}", t["sim_entry"],
                      sim_price=t.get("sim_entry_price"), sim_time=t["sim_entry"], adopt=first)

    def _journal_cycle(self, targets: dict[str, dict], eq: float) -> None:
        # shadow record: trades the strategy's own simulation closed since the last cycle
        keys = {(c["symbol"], c["entry_time"], c["exit_time"]) for c in self.strategy.sim_closed}
        if self.sim_seen is not None:
            for c in self.strategy.sim_closed:
                if (c["symbol"], c["entry_time"], c["exit_time"]) not in self.sim_seen:
                    self.journal("sim_trade", c)
        self.sim_seen = keys
        # snapshot whenever a bar completed (and at start)
        bars = self.strategy.closed_bars()
        last = {s: b["t"] for s, b in bars.items()}
        if last != self.last_bar:
            changed = [s for s in last if self.last_bar.get(s) != last[s]]
            self.journal("snapshot", {
                "first": not self.last_bar, "changed": changed, "bars": bars,
                "signals": self.strategy.closed_bar_signals(),
                "sim_open": {s: {"since": t["sim_entry"], "entry": t.get("sim_entry_price"), "weight": round(t["weight"], 4)}
                             for s, t in targets.items()},
                "held": {s: {"qty": p["qty"], "avg_usd": p["avg_price_usd"], "cost_chf": p["cost"], "since": p["opened_at"]}
                         for s, p in self.positions().items()},
                "equity": eq, "cash": self.cash(), "fx": self.fx})
            self.last_bar = last

    def cycle(self) -> str:
        if not self.crypto:
            is_open = market.nyse_open()
            if is_open != self.market_open:
                self.journal("market", {"nyse_open": is_open})
                self.market_open = is_open
            if not is_open:
                self.refresh_fx()
                self.record_equity()
                self.set_status("idle", "NYSE closed: idling")
                return "idle"
        self.refresh_fx()
        t0 = time.time()
        self.strategy.update_bars()
        t1 = time.time()
        targets, last_exit = self.strategy.targets()
        t2 = time.time()
        prices = self.strategy.prices()
        self.rebalance(targets, last_exit, prices)
        eq = self.record_equity(prices)
        self._journal_cycle(targets, eq)
        self._cycle_ms = ((t1 - t0) * 1000, (t2 - t1) * 1000)
        held = ", ".join(sorted(self.positions())) or "flat"
        self.set_status("running", f"equity {eq:,.2f} CHF; holding {held}")
        return "ok"

    def run(self) -> None:
        signal.signal(signal.SIGTERM, lambda *_: setattr(self, "stop", True))
        signal.signal(signal.SIGINT, lambda *_: setattr(self, "stop", True))
        while not self.stop:
            t0 = time.time()
            try:
                state = self.cycle()
                self.fail_streak = 0
                wait = 60 if (self.crypto or state == "idle") else 120
                if state == "idle":
                    self._stats_tick("idle")
                else:
                    self._stats_tick("ok", *getattr(self, "_cycle_ms", (None, None)))
            except Exception as ex:  # noqa: BLE001 - a bot must never die on a bad cycle
                self.fail_streak += 1
                wait = min(900, 60 * 2 ** (self.fail_streak - 1))
                kind = "data" if isinstance(ex, DataError) else "error"
                self.event("error", kind, f"cycle failed ({type(ex).__name__}: {str(ex)[:500]}); retry in {wait}s")
                self.journal("error", {"type": type(ex).__name__, "message": str(ex)[:1000], "data_error": kind == "data",
                                       "fail_streak": self.fail_streak, "retry_in_s": wait,
                                       "traceback": traceback.format_exc()[-4000:]})
                self._stats_tick("failed")
                if not isinstance(ex, DataError):
                    self.log.exception("traceback")
                try:
                    self.record_equity()
                    self.set_status("error", f"{type(ex).__name__}: {str(ex)[:300]}")
                except Exception:  # noqa: BLE001
                    self.log.exception("could not record status")
            beat = time.time()
            while not self.stop and time.time() - t0 < wait:
                time.sleep(1)
                if time.time() - beat >= 60:   # alive while waiting/backing off: the watchdog only restarts hung bots
                    beat = time.time()
                    try:
                        with self.con:
                            self.con.execute("UPDATE state SET heartbeat=? WHERE bot_id=?", (db.now_iso(), self.id))
                    except Exception:  # noqa: BLE001
                        self.log.exception("heartbeat failed")
        self.event("info", "stop", "stopped (SIGTERM)")
        self.set_status("stopped", "stopped")


def single_instance(bot_id: str):
    """flock so two copies of the same bot can never trade the same account."""
    p = db.ROOT / "data" / "brokers" / f".{bot_id}.lock"
    p.parent.mkdir(parents=True, exist_ok=True)
    fh = open(p, "w")
    try:
        fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit(f"bot {bot_id} is already running")
    return fh
