"""Storage budget report / check / prune (see src/common/budget.py and config `storage`).

  python -m src.tools.storage report   # usage per dataset
  python -m src.tools.storage check    # exit 0 ok, 1 >= 80 %, 2 >= 95 % of the budget
  python -m src.tools.storage prune    # rolling window for book ticks
"""
from __future__ import annotations

import sys

from src.common.budget import GB, prune_book, usage


def report(u: dict) -> str:
    lines = [f"data/ uses {u['total'] / GB:.1f} GB of {u['budget'] / GB:.0f} GB budget ({u['pct'] * 100:.1f}%), "
             f"disk free {u['disk_free'] / GB:.0f} GB"]
    for k, v in sorted(u["datasets"].items(), key=lambda kv: -kv[1]):
        lines.append(f"  {k:<20} {v / GB:9.2f} GB")
    lines.append(f"  (book ticks are capped at {u['book_max'] / GB:.0f} GB, oldest days pruned first)")
    return "\n".join(lines)


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    if cmd == "prune":
        removed = prune_book()
        print(f"pruned {len(removed)} book day(s): {', '.join(removed) or '-'}")
    u = usage()
    print(report(u))
    if cmd == "check":
        sys.exit(2 if u["pct"] >= 0.95 else 1 if u["pct"] >= 0.80 else 0)


if __name__ == "__main__":
    main()
