#!/usr/bin/env python3
"""Heartbeat watchdog for the paper bots, plus a "back up after reboot" e-mail.

Runs every 2 minutes from the user crontab (standard library only, no sudo):
  */2 * * * * /usr/bin/python3 /home/luca/trading/scripts/brokers/watchdog.py >> /home/luca/trading/logs/brokers/watchdog.log 2>&1

1. Hung bots: systemd's Restart=always only reacts when a bot process EXITS. A bot whose unit is
   active but whose heartbeat is older than STALE_MIN minutes is hung: its container is stopped,
   and systemd starts a fresh one 15 s later. At most one restart per bot per COOLDOWN_MIN.
2. Units that are enabled but not active (failed, hit a start limit) can't be started without
   sudo: they are reported in the events table once an hour (and show up in the daily report).
3. After a reboot: once every bot has a heartbeat newer than the boot (or BOOT_WAIT_MIN passed),
   one e-mail says how many bots came back by themselves. Sent through msmtp like the daily
   report; the recipient is the `from` address in ~/.msmtprc (or BROKER_REPORT_TO).
"""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import time
from datetime import datetime, timezone
from email.message import EmailMessage
from email.utils import formatdate
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "data" / "brokers" / "brokers.db"
STATE = ROOT / "data" / "brokers" / "watchdog_state.json"
STALE_MIN = float(os.environ.get("BROKER_WATCHDOG_STALE_MIN", 10))   # env override for tests
COOLDOWN_MIN, BOOT_WAIT_MIN = 20, 15


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def age_min(iso: str | None) -> float:
    if not iso:
        return 1e9
    t = datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - t).total_seconds() / 60


def boot_time() -> int:
    for line in Path("/proc/stat").read_text().splitlines():
        if line.startswith("btime "):
            return int(line.split()[1])
    return 0


def unit_state(bot: str) -> tuple[str, str]:
    r = subprocess.run(["systemctl", "show", f"broker@{bot}.service", "-p", "ActiveState", "-p", "UnitFileState", "--value"],
                       capture_output=True, text=True, timeout=20)
    vals = (r.stdout.split("\n") + ["", ""])[:2]
    return vals[0], vals[1]   # ActiveState, UnitFileState


def log_event(con, bot: str, level: str, kind: str, msg: str, data: dict | None = None) -> None:
    ts = now_iso()
    with con:
        con.execute("INSERT INTO events(bot_id, ts, level, kind, message) VALUES (?,?,?,?,?)", (bot, ts, level, kind, msg))
        if data is not None:
            con.execute("INSERT INTO journal(bot_id, ts, kind, data) VALUES (?,?,?,?)", (bot, ts, "watchdog", json.dumps(data)))
    print(f"{ts} {bot}: {msg}", flush=True)


def recipient() -> str | None:
    if os.environ.get("BROKER_REPORT_TO"):
        return os.environ["BROKER_REPORT_TO"]
    rc = Path.home() / ".msmtprc"
    for line in rc.read_text().splitlines() if rc.exists() else []:   # only the non-secret `from` line
        p = line.split()
        if len(p) >= 2 and p[0] == "from":
            return p[1]
    return None


def mail(subject: str, body: str) -> None:
    to = recipient()
    if not to:
        print("no recipient for the reboot mail", flush=True)
        return
    m = EmailMessage()
    m["From"], m["To"], m["Subject"], m["Date"] = f"Trading Homelab <{to}>", to, subject, formatdate(localtime=True)
    m.set_content(body)
    subprocess.run(["msmtp", to], input=m.as_bytes(), check=True, timeout=120)


def main() -> None:
    if not DB.exists():
        return
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    con = sqlite3.connect(DB, timeout=30)
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT bot_id, status, heartbeat FROM state ORDER BY bot_id").fetchall()
    restarts = state.setdefault("restarts", {})
    reported = state.setdefault("unit_reported", {})
    units = {}
    for r in rows:
        bot = r["bot_id"]
        active, enabled = unit_state(bot)
        units[bot] = (active, enabled)
        if enabled != "enabled":
            continue                                   # removed or disabled on purpose: leave it alone
        if active != "active":
            if time.time() - reported.get(bot, 0) > 3600 and active not in ("activating", "reloading"):
                log_event(con, bot, "error", "watchdog", f"unit broker@{bot} is {active} (needs: sudo systemctl restart broker@{bot})")
                reported[bot] = time.time()
            continue
        stale = age_min(r["heartbeat"])
        if r["status"] != "stopped" and stale > STALE_MIN and time.time() - restarts.get(bot, 0) > COOLDOWN_MIN * 60:
            subprocess.run(["docker", "stop", "-t", "30", f"broker-{bot}"], capture_output=True, timeout=90)
            restarts[bot] = time.time()
            log_event(con, bot, "error", "watchdog", f"no heartbeat for {stale:.0f} min: container restarted",
                      {"action": "restart", "heartbeat": r["heartbeat"], "stale_min": round(stale, 1), "status": r["status"]})

    # reboot notice: once per boot, after the bots had time to come back
    bt = boot_time()
    if bt and state.get("boot_notified") != bt:
        boot_iso = datetime.fromtimestamp(bt, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        if state.get("boot_seen") is None:             # first run ever: just remember this boot
            state["boot_notified"] = bt
        else:
            fresh = [r["bot_id"] for r in rows if r["heartbeat"] and r["heartbeat"] > boot_iso]
            waited = (time.time() - bt) / 60
            if len(fresh) == len(rows) or waited > BOOT_WAIT_MIN:
                missing = sorted(set(r["bot_id"] for r in rows) - set(fresh))
                local = datetime.fromtimestamp(bt).astimezone().strftime("%d.%m.%Y %H:%M %Z")
                body = (f"h0melab restarted at {local}.\n\n{len(fresh)} of {len(rows)} paper bots came back up by themselves"
                        f" ({waited:.0f} min after boot).\n"
                        + (f"\nNot back yet: {', '.join(missing)}\nCheck: systemctl list-units 'broker@*'\n" if missing else "")
                        + "\nDashboard: http://h0melab:3000/brokers\nPaper trading only.")
                try:
                    mail(f"h0melab rebooted: {len(fresh)}/{len(rows)} paper bots back up", body)
                    state["boot_notified"] = bt
                    print(f"{now_iso()} reboot mail sent ({len(fresh)}/{len(rows)} up)", flush=True)
                except Exception as ex:  # noqa: BLE001
                    print(f"{now_iso()} reboot mail failed: {ex}", flush=True)
        state["boot_seen"] = bt
    STATE.write_text(json.dumps(state))


if __name__ == "__main__":
    main()
