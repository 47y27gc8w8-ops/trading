"""Storage budget for ./data (config: storage.budget_gb, default 750 GB).

- usage(): bytes per dataset
- allow_backfill(): False at >= 95 % of the budget (backfills stop cleanly)
- prune_book(): book-ticker recording is a rolling window: oldest days are deleted
  while it is above storage.book_max_gb, or while the whole project is above 90 %.
"""
from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path

from src.common.storage import DATA, load_config

log = logging.getLogger("budget")
GB = 1024 ** 3
BOOK = DATA / "crypto" / "book"
DATASETS = {
    "crypto 1m": DATA / "crypto" / "1m", "crypto trades": DATA / "crypto" / "trades", "crypto book": BOOK,
    "quotes 30s": DATA / "quotes", "yahoo (etf/stock)": DATA / "etf", "raw downloads": DATA / "raw",
}


def settings() -> dict:
    s = load_config().get("storage", {}) or {}
    return {"budget_gb": float(s.get("budget_gb", 750)), "book_max_gb": float(s.get("book_max_gb", 300))}


def dir_bytes(path: Path) -> int:
    total = 0
    if not path.exists():
        return 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                total += os.lstat(os.path.join(root, f)).st_size
            except OSError:
                pass
    return total


def usage() -> dict:
    per = {k: dir_bytes(p) for k, p in DATASETS.items()}
    total = dir_bytes(DATA)
    per["other"] = max(0, total - sum(per.values()))
    s = settings()
    return {"total": total, "datasets": per, "budget": int(s["budget_gb"] * GB), "book_max": int(s["book_max_gb"] * GB),
            "pct": total / (s["budget_gb"] * GB), "disk_free": shutil.disk_usage(DATA).free}


def allow_backfill(limit: float = 0.95) -> bool:
    u = usage()
    if u["pct"] >= limit:
        log.error("storage budget: %.1f GB of %.0f GB used (%.0f%%) - backfill stopped",
                  u["total"] / GB, u["budget"] / GB, u["pct"] * 100)
        return False
    return True


def prune_book(project_target: float = 0.90) -> list[str]:
    """Delete the oldest book-ticker days until both limits hold. Never touches other datasets."""
    removed = []
    days = sorted(p for p in BOOK.glob("date=*") if p.is_dir())
    if not days:
        return removed
    u = usage()
    book, total = u["datasets"]["crypto book"], u["total"]
    while len(days) > 1 and (book > u["book_max"] or total > project_target * u["budget"]):
        d = days.pop(0)
        size = dir_bytes(d)
        shutil.rmtree(d)
        book -= size
        total -= size
        removed.append(d.name)
        log.warning("pruned book ticks %s (%.1f GB)", d.name, size / GB)
    return removed
