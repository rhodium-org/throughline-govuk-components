#!/usr/bin/env python3
"""Generate the GOV.UK Design System throughline source from a distilled data file.

Unlike ASVS, the GOV.UK Design System publishes no machine-readable clause export: the
guidance is prose on the component pages. The intellectual work — distilling each
component's usage rules, accessibility criteria and research findings into testable
clauses — lives in ``tools/components_data.py`` (one structured record per component).
This script is pure mechanics: it turns that data into throughline items and the
published spec skeleton.

Two invariants make re-running safe and faithful (mirroring the ASVS generator):

* **UIDs are permanent.** The mapping from a component/clause to a throughline UID is
  derived from the items already on disk, keyed by ``attrs.source_ref`` (which is unique
  per item: ``"button"`` for a component UR, ``"button#sentence-case"`` for a clause SR).
  Existing items are never rewritten; only components/clauses that have no item yet get a
  freshly allocated UID, in data-file order, continuing from the highest number in use.
* **Additive only.** Editing a clause's text in the data file does not rewrite an item
  that already exists (it is matched and skipped). To revise published text, edit the
  item YAML directly; to retire a clause, tombstone the item with ``tl delete``.

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
INTENT = "INT-0001"


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
    """Create any missing UR/SR items. Returns (slug->ur_uid, urs_written, srs_written)."""
    ur_ref2uid = _scan_existing(COMPONENTS_DIR)
    sr_ref2uid = _scan_existing(REQS_DIR)
    next_ur = _max_num(ur_ref2uid, "UR") + 1
    next_sr = _max_num(sr_ref2uid, "SR") + 1

    slug2ur: dict[str, str] = {}
    urs_written = srs_written = 0

    for comp in COMPONENTS:
        slug = comp["slug"]
        if slug in ur_ref2uid:
            ur_uid = ur_ref2uid[slug]
        else:
            ur_uid = f"UR-{next_ur:04d}"
            next_ur += 1
            ur_ref2uid[slug] = ur_uid
            _dump(COMPONENTS_DIR / f"{ur_uid}.yml", {
                "uid": ur_uid,
                "type": "user_requirement",
                "status": "approved",
                "title": comp["title"],
                "text": comp["ur_text"],
                "links": [{"target": INTENT, "type": "derives_from"}],
                "attrs": {"source_ref": slug},
            })
            urs_written += 1
        slug2ur[slug] = ur_uid

        for clause in comp["clauses"]:
            ref = f"{slug}#{clause['anchor']}"
            if ref in sr_ref2uid:
                continue
            sr_uid = f"SR-{next_sr:04d}"
            next_sr += 1
            sr_ref2uid[ref] = sr_uid
            attrs = {"source_ref": ref, "kind": clause["kind"]}
            if clause.get("wcag"):
                attrs["wcag"] = clause["wcag"]
            _dump(REQS_DIR / f"{sr_uid}.yml", {
                "uid": sr_uid,
                "type": "system_requirement",
                "status": "approved",
                "title": clause["title"],
                "text": clause["text"],
                "links": [{"target": ur_uid, "type": "implements"}],
                "attrs": attrs,
            })
            srs_written += 1

    return slug2ur, urs_written, srs_written


SPEC_HEADER = """\
# GOV.UK Design System components — throughline source

This document is generated from the graph. The prose between `tl:item` / `tl:table`
markers is injected by `tl docs` — edit the YAML items, not the injected regions.

Each component is a `user_requirement` grouping the standard; each usage rule,
accessibility acceptance criterion or do-and-don't is a `system_requirement` that
`implements` its component. The component's native anchor lives in `attrs.source_ref`
(`"button"`, `"button#sentence-case"`); the facet in `attrs.kind`
(`usage` / `accessibility` / `research`); any WCAG success criterion in `attrs.wcag`.

## Purpose

<!-- tl:item INT-0001 -->
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
    total_sr = len(list(REQS_DIR.glob("*.yml")))
    total_ur = len(list(COMPONENTS_DIR.glob("*.yml")))
    print(f"components: {urs} new URs written, {total_ur} total")
    print(f"clauses: {srs} new SRs written, {total_sr} total")
    print(f"spec: {SPEC} regenerated for {len(COMPONENTS)} components")
    print("next: run `tl docs` to inject content, then `tl check --strict`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
