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
**INT-0001 — GOV.UK services are consistent, accessible and usable by everyone** — `intent`, status `approved`

> The GOV.UK Design System exists so that government services are built from components and patterns that are proven to be consistent, accessible and usable — letting teams reuse tested solutions with documented usage and accessibility guidance rather than reinventing interface elements service by service.

**source_ref**: GOV.UK Design System
<!-- tl:end -->

## Button

<!-- tl:item UR-0001 -->
**UR-0001 — Button** — `user_requirement`, status `approved`

> The service uses the GOV.UK Button component to let users carry out an action, following its guidance on button text, variants, grouping, contrast and double-click prevention.

**source_ref**: button
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('button#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Buttons carry out an action |
| SR-0002 | system_requirement | approved | Button text is sentence case and describes the action |
| SR-0003 | system_requirement | approved | Primary action aligns to the left of the form |
| SR-0004 | system_requirement | approved | Avoid multiple default buttons on a page |
| SR-0005 | system_requirement | approved | Start buttons are links, not submit buttons |
| SR-0006 | system_requirement | approved | Secondary buttons for secondary actions only |
| SR-0007 | system_requirement | approved | Warning buttons only for serious destructive actions |
| SR-0008 | system_requirement | approved | Precede a warning action with a confirmation step |
| SR-0009 | system_requirement | approved | Do not rely on warning button colour alone |
| SR-0010 | system_requirement | approved | Buttons on dark backgrounds meet contrast minimum |
| SR-0011 | system_requirement | approved | Avoid disabled buttons |
| SR-0012 | system_requirement | approved | Group buttons placed together |
| SR-0013 | system_requirement | approved | Guard against accidental double submission |
| SR-0014 | system_requirement | approved | Green start buttons improve click-through |
<!-- tl:end -->

## Error summary

<!-- tl:item UR-0002 -->
**UR-0002 — Error summary** — `user_requirement`, status `approved`

> The service uses the GOV.UK Error summary component at the top of a page to summarise validation errors, moving focus to it, linking each error to its answer and mirroring the inline error messages.

**source_ref**: error-summary
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('error-summary#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0015 | system_requirement | approved | Show the error summary at the top of the page |
| SR-0016 | system_requirement | approved | Show a summary and an inline message per error |
| SR-0017 | system_requirement | approved | Always show the summary when there is an error |
| SR-0018 | system_requirement | approved | Move keyboard focus to the error summary |
| SR-0019 | system_requirement | approved | Use the heading 'There is a problem' |
| SR-0020 | system_requirement | approved | Summary wording matches the inline messages |
| SR-0021 | system_requirement | approved | Prefix the page title with 'Error:' |
| SR-0022 | system_requirement | approved | Link single-field errors to the field |
| SR-0023 | system_requirement | approved | Link multi-field errors to the first errored field |
| SR-0024 | system_requirement | approved | Link option errors to the first option |
| SR-0025 | system_requirement | approved | Place the summary above the h1 |
<!-- tl:end -->

## Date input

<!-- tl:item UR-0003 -->
**UR-0003 — Date input** — `user_requirement`, status `approved`

> The service uses the GOV.UK Date input component to help users enter a memorable date across day, month and year fields, grouped in a fieldset, with accessible labelling, autocomplete and specific error messages.

**source_ref**: date-input
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('date-input#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0026 | system_requirement | approved | Use for dates users know or can look up |
| SR-0027 | system_requirement | approved | Do not use for dates users will not know |
| SR-0028 | system_requirement | approved | Group the three fields in a fieldset with a legend |
| SR-0029 | system_requirement | approved | Set the legend as the page heading when one question per page |
| SR-0030 | system_requirement | approved | Do not set the legend as the heading with multiple questions |
| SR-0031 | system_requirement | approved | Hint text example dates are valid for the question |
| SR-0032 | system_requirement | approved | Accept month names in full or abbreviated form |
| SR-0033 | system_requirement | approved | Do not auto-tab between fields |
| SR-0034 | system_requirement | approved | Set autocomplete attributes for a date of birth |
| SR-0035 | system_requirement | approved | Highlight only the fields in error |
| SR-0036 | system_requirement | approved | Show the highest-priority error first |
| SR-0037 | system_requirement | approved | Use specific wording for each error state |
| SR-0038 | system_requirement | approved | Accepting month names reduced errors |
<!-- tl:end -->

## Accordion

<!-- tl:item UR-0004 -->
**UR-0004 — Accordion** — `user_requirement`, status `approved`

> The service uses the GOV.UK Accordion component to let users show and hide sections of related content, only where research shows hiding content helps, with clear headings and keyboard support.

**source_ref**: accordion
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('accordion#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0039 | system_requirement | approved | Use only where research shows it helps |
| SR-0040 | system_requirement | approved | Do not hide content all users need |
| SR-0041 | system_requirement | approved | Test the content without an accordion first |
| SR-0042 | system_requirement | approved | Do not use to split up questions |
| SR-0043 | system_requirement | approved | Do not nest accordions or hide-reveal components |
| SR-0044 | system_requirement | approved | Give the accordion a unique id |
| SR-0045 | system_requirement | approved | Show all content when JavaScript is unavailable |
| SR-0046 | system_requirement | approved | Write clear, short heading button text |
| SR-0047 | system_requirement | approved | Keep any summary line as short as possible |
| SR-0048 | system_requirement | approved | Fit section heading levels into the page |
| SR-0049 | system_requirement | approved | Do not disable sections |
| SR-0050 | system_requirement | approved | Reworked in 2021 for accessibility |
<!-- tl:end -->

## Back link

<!-- tl:item UR-0005 -->
**UR-0005 — Back link** — `user_requirement`, status `approved`

> The service uses the GOV.UK Back link component to help users return to the previous page in a multi-page transaction, placed above the main content with clear text and sufficient contrast.

**source_ref**: back-link
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('back-link#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0051 | system_requirement | approved | Use to go back in a multi-page transaction |
| SR-0052 | system_requirement | approved | Always include on question pages |
| SR-0053 | system_requirement | approved | Do not combine with breadcrumbs |
| SR-0054 | system_requirement | approved | Place the back link before the main element |
| SR-0055 | system_requirement | approved | Return users to the page as they last saw it |
| SR-0056 | system_requirement | approved | Work without JavaScript, or hide it |
| SR-0057 | system_requirement | approved | Use descriptive text for complex journeys |
| SR-0058 | system_requirement | approved | Back links on dark backgrounds meet contrast minimum |
<!-- tl:end -->

## Breadcrumbs

<!-- tl:item UR-0006 -->
**UR-0006 — Breadcrumbs** — `user_requirement`, status `approved`

> The service uses the GOV.UK Breadcrumbs component to help users understand where they are within a site's hierarchy and move between levels, placed above the main content.

**source_ref**: breadcrumbs
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('breadcrumbs#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0059 | system_requirement | approved | Use to move between levels of a hierarchy |
| SR-0060 | system_requirement | approved | Do not use for flat sites or linear journeys |
| SR-0061 | system_requirement | approved | Place breadcrumbs before the main element |
| SR-0062 | system_requirement | approved | Run from home to the current page's parent |
| SR-0063 | system_requirement | approved | Optionally collapse long breadcrumbs on mobile |
| SR-0064 | system_requirement | approved | Breadcrumbs on dark backgrounds meet contrast minimum |
<!-- tl:end -->

## Character count

<!-- tl:item UR-0007 -->
**UR-0007 — Character count** — `user_requirement`, status `approved`

> The service uses the GOV.UK Character count component to tell users how much text they can enter into a textarea with a limit, only where limiting is justified, with accessible live feedback.

**source_ref**: character-count
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('character-count#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0065 | system_requirement | approved | Test the service without a character count first |
| SR-0066 | system_requirement | approved | Raise a limit users keep hitting |
| SR-0067 | system_requirement | approved | Do not block entry over the limit |
| SR-0068 | system_requirement | approved | Show the count message below the textarea |
| SR-0069 | system_requirement | approved | Show a static limit message without JavaScript |
| SR-0070 | system_requirement | approved | Do not set the label as the heading with multiple questions |
| SR-0071 | system_requirement | approved | Consider a word count for longer answers |
| SR-0072 | system_requirement | approved | Set the limit higher than most users need |
| SR-0073 | system_requirement | approved | Show an error above the field and the count below |
| SR-0074 | system_requirement | approved | Tested with disabled users; announcement fixed |
<!-- tl:end -->

