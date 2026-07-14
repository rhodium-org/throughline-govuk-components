#!/usr/bin/env python3
"""Generate the GOV.UK Design System throughline source from a distilled data file.

Unlike ASVS, the GOV.UK Design System publishes no machine-readable clause export: the
guidance is prose on the component pages. The intellectual work — distilling each
component's usage rules, accessibility criteria and research findings into testable
clauses — lives in ``tools/components_data.py`` (one structured record per component).
This script is pure mechanics: it turns that data into throughline items and the
published spec skeleton.

One invariant makes re-running safe and faithful (mirroring the ASVS generator):

* **UIDs are permanent.** The mapping from a component/clause to a throughline UID is
  derived from the items already on disk, keyed by ``attrs.source_ref`` (which is unique
  per item: ``"button"`` for a component UR, ``"button#sentence-case"`` for a clause SR).
  A component/clause that has no item yet gets a freshly allocated UID, in data-file
  order, continuing from the highest number in use; a UID, once allocated, never moves.

Item *bodies* are regenerated from ``components_data.py`` on every run — the data file is
the single source of truth. To revise a clause, edit the data file and re-run; to retire
one, remove it from the data file and tombstone its item with ``tl delete``.

The **"why" spine** has three co-equal **root** intents — the outcomes the Design System
claims: accessibility (``INT-0002``), consistent use (``INT-0003``) and proven-by-research
(``INT-0004``). There is no single umbrella (``INT-0001`` was retired as a tombstone).
Each component ``user_requirement`` ``derives_from`` the outcome roots its clauses serve
and carries a ``rationale`` (the component's real *why*). Each clause
``system_requirement`` ``implements`` its component and ``serves`` the outcome root
matching its ``attrs.kind`` — so a clause's *why* is a first-class, traversable edge
rather than a flat tag.

The docs skeleton (``docs/spec.md``) is regenerated in full each run — a header plus, per
component, a ``tl:item`` block for its UR and a ``tl:table`` referencing its clauses.
``tl docs`` then injects the live graph content into those markers.

Usage:  python tools/generate.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

from components_data import COMPONENTS

REPO = Path(__file__).resolve().parent.parent
COMPONENTS_DIR = REPO / "components"      # user_requirement, prefix UR
REQS_DIR = REPO / "requirements"          # system_requirement, prefix SR
SPEC = REPO / "docs" / "spec.md"

# The three co-equal root intents (the outcomes the Design System claims). A clause's
# `attrs.kind` maps 1:1 to the outcome it serves; a component derives_from the union of
# the outcomes its clauses cover. KIND_ORDER fixes a stable link order.
OUTCOMES = {
    "accessibility": "INT-0002",   # works for everyone
    "usage": "INT-0003",           # consistent, correct use
    "research": "INT-0004",        # proven by user research
}
KIND_ORDER = ["accessibility", "usage", "research"]


def _scan_existing(dir_: Path) -> dict[str, str]:
    """Map source_ref -> UID for the items already on disk."""
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max_num(ref2uid: dict[str, str], prefix: str) -> int:
    nums = [int(u.split("-")[1]) for u in ref2uid.values() if u.startswith(prefix + "-")]
    return max(nums, default=0)


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=80),
        encoding="utf-8",
    )


def generate_items() -> tuple[dict[str, str], int, int]:
    """Allocate UIDs for any new components/clauses, then (re)write every item body from
    the data file. Returns (slug->ur_uid, urs_new, srs_new)."""
    ur_ref2uid = _scan_existing(COMPONENTS_DIR)
    sr_ref2uid = _scan_existing(REQS_DIR)
    next_ur = _max_num(ur_ref2uid, "UR") + 1
    next_sr = _max_num(sr_ref2uid, "SR") + 1

    slug2ur: dict[str, str] = {}
    urs_new = srs_new = 0

    for comp in COMPONENTS:
        slug = comp["slug"]
        ur_uid = ur_ref2uid.get(slug)
        if ur_uid is None:
            ur_uid = f"UR-{next_ur:04d}"
            next_ur += 1
            ur_ref2uid[slug] = ur_uid
            urs_new += 1
        slug2ur[slug] = ur_uid

        # A component derives_from the outcome roots its clauses serve (stable order).
        kinds = {c["kind"] for c in comp["clauses"]}
        outcomes = [OUTCOMES[k] for k in KIND_ORDER if k in kinds]
        _dump(COMPONENTS_DIR / f"{ur_uid}.yml", {
            "uid": ur_uid,
            "type": "user_requirement",
            "status": "approved",
            "title": comp["title"],
            "text": comp["ur_text"],
            "rationale": comp["rationale"],
            "links": [{"target": o, "type": "derives_from"} for o in outcomes],
            "attrs": {"source_ref": slug},
        })

        for clause in comp["clauses"]:
            ref = f"{slug}#{clause['anchor']}"
            sr_uid = sr_ref2uid.get(ref)
            if sr_uid is None:
                sr_uid = f"SR-{next_sr:04d}"
                next_sr += 1
                sr_ref2uid[ref] = sr_uid
                srs_new += 1
            attrs = {"source_ref": ref, "kind": clause["kind"]}
            if clause.get("wcag"):
                attrs["wcag"] = clause["wcag"]
            _dump(REQS_DIR / f"{sr_uid}.yml", {
                "uid": sr_uid,
                "type": "system_requirement",
                "status": "approved",
                "title": clause["title"],
                "text": clause["text"],
                "links": [
                    {"target": ur_uid, "type": "implements"},
                    {"target": OUTCOMES[clause["kind"]], "type": "serves"},
                ],
                "attrs": attrs,
            })

    return slug2ur, urs_new, srs_new


SPEC_HEADER = """\
# GOV.UK Design System components — throughline source

This document is generated from the graph. The prose between `tl:item` / `tl:table`
markers is injected by `tl docs` — edit the YAML items, not the injected regions.

The "why" spine has three co-equal **root** intents — the outcomes the Design System
claims. Each component is a `user_requirement` that `derives_from` the outcome roots its
clauses serve, carrying a `rationale` for its own existence; each usage rule,
accessibility acceptance criterion or do-and-don't is a `system_requirement` that
`implements` its component and `serves` the outcome root matching its `attrs.kind`
(`accessibility` → INT-0002, `usage` → INT-0003, `research` → INT-0004). The component's
native anchor lives in `attrs.source_ref` (`"button"`, `"button#sentence-case"`); any
WCAG success criterion in `attrs.wcag`.

## Outcomes — the roots

<!-- tl:item INT-0002 -->
<!-- tl:end -->

<!-- tl:item INT-0003 -->
<!-- tl:end -->

<!-- tl:item INT-0004 -->
<!-- tl:end -->
"""


def generate_spec(slug2ur: dict[str, str]) -> None:
    parts = [SPEC_HEADER]
    for comp in COMPONENTS:
        slug = comp["slug"]
        parts.append(f"## {comp['title']}\n")
        parts.append(f"<!-- tl:item {slug2ur[slug]} -->\n<!-- tl:end -->\n")
        flt = (
            "type == 'system_requirement' and "
            f"attrs.get('source_ref').startswith('{slug}#')"
        )
        parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    slug2ur, urs, srs = generate_items()
    generate_spec(slug2ur)
    total_sr = len(list(REQS_DIR.glob("SR-*.yml")))
    total_ur = len(list(COMPONENTS_DIR.glob("UR-*.yml")))
    print(f"components: {urs} new URs written, {total_ur} total")
    print(f"clauses: {srs} new SRs written, {total_sr} total")
    print(f"spec: {SPEC} regenerated for {len(COMPONENTS)} components")
    print("next: run `tl docs` to inject content, then `tl check --strict`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
