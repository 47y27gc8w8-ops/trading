"""Run one paper bot:  python -m src.brokers.run --bot <id>   (ids in config/brokers.yaml)

PAPER ONLY: simulated fills in data/brokers/brokers.db, public market data, no exchange keys.
"""
from __future__ import annotations

import argparse
import sys

import yaml

from src.brokers import db
from src.brokers.base import Bot, single_instance

CONFIG = db.ROOT / "config" / "brokers.yaml"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--bot", help="bot id from config/brokers.yaml")
    ap.add_argument("--list", action="store_true", help="print the bot ids and exit")
    a = ap.parse_args()
    cfg = yaml.safe_load(open(CONFIG))
    bots = {b["id"]: b for b in cfg["bots"]}
    if a.list or not a.bot:
        print("\n".join(bots))
        return
    if a.bot not in bots:
        sys.exit(f"unknown bot {a.bot!r}; known: {', '.join(bots)}")
    _lock = single_instance(a.bot)  # noqa: F841 - held for the process lifetime
    Bot(cfg, bots[a.bot]).run()


if __name__ == "__main__":
    main()
