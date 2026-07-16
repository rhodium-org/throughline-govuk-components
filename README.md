# throughline-govuk-components

The **GOV.UK Design System component library** expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/rhodium-org/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its clauses as `govuk:SR-0003`.

## Status

A grounded graph of
<!-- tl:count type == 'user_requirement' -->
35
<!-- tl:end --> component requirements and
<!-- tl:count type == 'system_requirement' -->
381
<!-- tl:end --> distilled clauses, published to [`docs/spec.md`](docs/spec.md):

- **Three co-equal root intents** — the outcomes the Design System actually claims:
  `INT-0002` accessibility, `INT-0003` consistent use, `INT-0004` proven by research
  (all `normative: false`). There is no single umbrella intent — a source gets as many
  roots as it has genuine *why*s.
- Each **component** is a `user_requirement` that `derives_from` the specific outcome
  roots its clauses serve, and carries a `rationale` — its own reason for existing.
- Each **usage rule / accessibility acceptance criterion / do-and-don't** is a
  `system_requirement` that `implements` its component UR **and** `serves` the outcome
  root matching its `kind` — so a clause's *why* is a traversable edge, not a flat tag.

The counts above are rendered from the live graph by the `tl:count` directive, so they
cannot drift.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0001`…), immutable and never the
  component's name. The component's native anchor lives in `attrs.source_ref`
  (`"date-input"`, or `"date-input#accessibility"` for a facet).
- **Every clause carries a `kind`** — `usage`, `accessibility`, or `research` — so the
  facets of a component's guidance stay separable. `kind` also selects the outcome root
  the clause `serves` (`accessibility` → `INT-0002`, `usage` → `INT-0003`, `research` →
  `INT-0004`). Where a rule cites a WCAG success criterion, it is recorded in `attrs.wcag`.
- **The *why* is first-class, not a tag.** Rather than every component hanging off one
  bland root, components ground to the outcome roots they serve and every item carries a
  `rationale`. Queries like "which clauses serve accessibility?" become graph traversals
  that roll up through composition, instead of attribute filters.
- **Guidance is re-expressed as testable clauses**, not copied verbatim. Prescriptive
  guidance ("associate each input with a visible label") becomes a clause; pure
  rationale prose ("why this matters") does not, unless it encodes a testable
  expectation.
- **Components are independent.** A component's clauses ground only to that component's
  UR; where two components have a documented relationship (error summary and error
  message), their URs may `relates`, but grounding stays within each component.

## Composing it

In a consuming throughline project's `throughline.toml`:

```toml
[[sources]]
namespace = "govuk"
path = "vendor/throughline-govuk-components"   # or a pinned checkout
```

Then reference a clause from your own items:

```yaml
links:
- target: govuk:SR-0003          # a GOV.UK date-input accessibility criterion
  type: satisfies
```

`tl-compose check` resolves the reference; bare `tl check` fails fast and points you at
`tl-compose`.

## Local checks

```sh
pip install throughline
tl check --strict     # the graph must stay sound
tl docs --check       # README.md and docs/spec.md must match the graph
```

## Provenance

The GOV.UK Design System is produced by the Government Digital Service. Its guidance
content is © Crown copyright, published under the
[Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/);
`govuk-frontend` component code is MIT. The distilled guidance text remains Crown
copyright. See [NOTICE](NOTICE) and https://design-system.service.gov.uk/. This
repository is Apache-2.0 for its structure and tooling.
