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
**INT-0002 — Government services are accessible to everyone** — `intent`, status `proposed`

> Services built from the Design System work for everyone, including disabled people and people using assistive technology such as screen readers, keyboards and voice control, meeting WCAG 2.2 level AA and the Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations 2018.

**source_ref**: accessibility
<!-- tl:end -->

<!-- tl:item INT-0003 -->
**INT-0003 — Components are used consistently and correctly across services** — `intent`, status `proposed`

> Teams reuse each component as intended, with consistent structure, content and wording, so users recognise and trust government services and can transfer what they learn from one service to the next instead of teams reinventing interface elements service by service.

**source_ref**: consistent-use
<!-- tl:end -->

<!-- tl:item INT-0004 -->
**INT-0004 — Components are proven by user research** — `intent`, status `proposed`

> Each component is shaped and validated by user research and testing, so services adopt solutions already shown to help people complete their task first time with fewer errors, rather than untested designs.

**source_ref**: proven-by-research
<!-- tl:end -->

## Button

<!-- tl:item UR-0001 -->
**UR-0001 — Button** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Button component to let users carry out an action, following its guidance on button text, variants, grouping, contrast and double-click prevention.

*Rationale:* Users need an unambiguous, prominent way to carry out an action such as starting an application, signing in, or paying, so the main call to action stands out and they always know what to do next.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: button
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('button#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | proposed | Buttons carry out an action |
| SR-0002 | system_requirement | proposed | Button text is sentence case and describes the action |
| SR-0003 | system_requirement | proposed | Primary action aligns to the left of the form |
| SR-0004 | system_requirement | proposed | Avoid multiple default buttons on a page |
| SR-0005 | system_requirement | proposed | Start buttons are links, not submit buttons |
| SR-0006 | system_requirement | proposed | Secondary buttons for secondary actions only |
| SR-0007 | system_requirement | proposed | Warning buttons only for serious destructive actions |
| SR-0008 | system_requirement | proposed | Precede a warning action with a confirmation step |
| SR-0009 | system_requirement | proposed | Do not rely on warning button colour alone |
| SR-0010 | system_requirement | proposed | Buttons on dark backgrounds meet contrast minimum |
| SR-0011 | system_requirement | proposed | Avoid disabled buttons |
| SR-0012 | system_requirement | proposed | Group buttons placed together |
| SR-0013 | system_requirement | proposed | Guard against accidental double submission |
| SR-0014 | system_requirement | proposed | Green start buttons improve click-through |
<!-- tl:end -->

## Error summary

<!-- tl:item UR-0002 -->
**UR-0002 — Error summary** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Error summary component at the top of a page to summarise validation errors, moving focus to it, linking each error to its answer and mirroring the inline error messages.

*Rationale:* When a user submits answers containing validation errors, they need every problem gathered and focused at the top of the page so they can find, understand, and fix each mistake rather than hunting for what went wrong.

*Derives from:* INT-0002, INT-0003

**source_ref**: error-summary
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('error-summary#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0015 | system_requirement | proposed | Show the error summary at the top of the page |
| SR-0016 | system_requirement | proposed | Show a summary and an inline message per error |
| SR-0017 | system_requirement | proposed | Always show the summary when there is an error |
| SR-0018 | system_requirement | proposed | Move keyboard focus to the error summary |
| SR-0019 | system_requirement | proposed | Use the heading 'There is a problem' |
| SR-0020 | system_requirement | proposed | Summary wording matches the inline messages |
| SR-0021 | system_requirement | proposed | Prefix the page title with 'Error:' |
| SR-0022 | system_requirement | proposed | Link single-field errors to the field |
| SR-0023 | system_requirement | proposed | Link multi-field errors to the first errored field |
| SR-0024 | system_requirement | proposed | Link option errors to the first option |
| SR-0025 | system_requirement | proposed | Place the summary above the h1 |
<!-- tl:end -->

## Date input

<!-- tl:item UR-0003 -->
**UR-0003 — Date input** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Date input component to help users enter a memorable date across day, month and year fields, grouped in a fieldset, with accessible labelling, autocomplete and specific error messages.

*Rationale:* Users entering a date they already know or can look up need to type the day, month and year directly, avoiding the friction of a calendar picker for dates that are memorable rather than chosen.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: date-input
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('date-input#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0026 | system_requirement | proposed | Use for dates users know or can look up |
| SR-0027 | system_requirement | proposed | Do not use for dates users will not know |
| SR-0028 | system_requirement | proposed | Group the three fields in a fieldset with a legend |
| SR-0029 | system_requirement | proposed | Set the legend as the page heading when one question per page |
| SR-0030 | system_requirement | proposed | Do not set the legend as the heading with multiple questions |
| SR-0031 | system_requirement | proposed | Hint text example dates are valid for the question |
| SR-0032 | system_requirement | proposed | Accept month names in full or abbreviated form |
| SR-0033 | system_requirement | proposed | Do not auto-tab between fields |
| SR-0034 | system_requirement | proposed | Set autocomplete attributes for a date of birth |
| SR-0035 | system_requirement | proposed | Highlight only the fields in error |
| SR-0036 | system_requirement | proposed | Show the highest-priority error first |
| SR-0037 | system_requirement | proposed | Use specific wording for each error state |
| SR-0038 | system_requirement | proposed | Accepting month names reduced errors |
<!-- tl:end -->

## Accordion

<!-- tl:item UR-0004 -->
**UR-0004 — Accordion** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Accordion component to let users show and hide sections of related content, only where research shows hiding content helps, with clear headings and keyboard support.

*Rationale:* When users benefit from an overview of related sections and want to reveal, hide, and compare only the parts relevant to them, this lets them control long or repeat-use content instead of scrolling through everything at once.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: accordion
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('accordion#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0039 | system_requirement | proposed | Use only where research shows it helps |
| SR-0040 | system_requirement | proposed | Do not hide content all users need |
| SR-0041 | system_requirement | proposed | Test the content without an accordion first |
| SR-0042 | system_requirement | proposed | Do not use to split up questions |
| SR-0043 | system_requirement | proposed | Do not nest accordions or hide-reveal components |
| SR-0044 | system_requirement | proposed | Give the accordion a unique id |
| SR-0045 | system_requirement | proposed | Show all content when JavaScript is unavailable |
| SR-0046 | system_requirement | proposed | Write clear, short heading button text |
| SR-0047 | system_requirement | proposed | Keep any summary line as short as possible |
| SR-0048 | system_requirement | proposed | Fit section heading levels into the page |
| SR-0049 | system_requirement | proposed | Do not disable sections |
| SR-0050 | system_requirement | proposed | Reworked in 2021 for accessibility |
<!-- tl:end -->

## Back link

<!-- tl:item UR-0005 -->
**UR-0005 — Back link** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Back link component to help users return to the previous page in a multi-page transaction, placed above the main content with clear text and sufficient contrast.

*Rationale:* Because browser back buttons can break services or go unnoticed, users in a multi-page transaction need a reliable in-page way to return to the previous step without losing their progress.

*Derives from:* INT-0002, INT-0003

**source_ref**: back-link
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('back-link#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0051 | system_requirement | proposed | Use to go back in a multi-page transaction |
| SR-0052 | system_requirement | proposed | Always include on question pages |
| SR-0053 | system_requirement | proposed | Do not combine with breadcrumbs |
| SR-0054 | system_requirement | proposed | Place the back link before the main element |
| SR-0055 | system_requirement | proposed | Return users to the page as they last saw it |
| SR-0056 | system_requirement | proposed | Work without JavaScript, or hide it |
| SR-0057 | system_requirement | proposed | Use descriptive text for complex journeys |
| SR-0058 | system_requirement | proposed | Back links on dark backgrounds meet contrast minimum |
<!-- tl:end -->

## Breadcrumbs

<!-- tl:item UR-0006 -->
**UR-0006 — Breadcrumbs** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Breadcrumbs component to help users understand where they are within a site's hierarchy and move between levels, placed above the main content.

*Rationale:* Users navigating a site with multiple hierarchical levels need to understand where they are and move up between levels, so they can orient themselves within the wider structure.

*Derives from:* INT-0002, INT-0003

**source_ref**: breadcrumbs
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('breadcrumbs#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0059 | system_requirement | proposed | Use to move between levels of a hierarchy |
| SR-0060 | system_requirement | proposed | Do not use for flat sites or linear journeys |
| SR-0061 | system_requirement | proposed | Place breadcrumbs before the main element |
| SR-0062 | system_requirement | proposed | Run from home to the current page's parent |
| SR-0063 | system_requirement | proposed | Optionally collapse long breadcrumbs on mobile |
| SR-0064 | system_requirement | proposed | Breadcrumbs on dark backgrounds meet contrast minimum |
<!-- tl:end -->

## Character count

<!-- tl:item UR-0007 -->
**UR-0007 — Character count** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Character count component to tell users how much text they can enter into a textarea with a limit, only where limiting is justified, with accessible live feedback.

*Rationale:* When a genuine legal or technical limit caps how much a user can enter, they need live feedback on characters or words remaining so they can write their full answer and then edit it down without being cut off unexpectedly.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: character-count
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('character-count#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0065 | system_requirement | proposed | Test the service without a character count first |
| SR-0066 | system_requirement | proposed | Raise a limit users keep hitting |
| SR-0067 | system_requirement | proposed | Do not block entry over the limit |
| SR-0068 | system_requirement | proposed | Show the count message below the textarea |
| SR-0069 | system_requirement | proposed | Show a static limit message without JavaScript |
| SR-0070 | system_requirement | proposed | Do not set the label as the heading with multiple questions |
| SR-0071 | system_requirement | proposed | Consider a word count for longer answers |
| SR-0072 | system_requirement | proposed | Set the limit higher than most users need |
| SR-0073 | system_requirement | proposed | Show an error above the field and the count below |
| SR-0074 | system_requirement | proposed | Tested with disabled users; announcement fixed |
<!-- tl:end -->

## Checkboxes

<!-- tl:item UR-0008 -->
**UR-0008 — Checkboxes** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Checkboxes component to let users select one or more options, grouped in a fieldset with an accessible legend, ordered and labelled to guidance.

*Rationale:* Users need to select one or more options from a list, or toggle a single option on or off, when a question genuinely allows multiple answers rather than a single mutually-exclusive choice.

*Derives from:* INT-0002, INT-0003

**source_ref**: checkboxes
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('checkboxes#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0075 | system_requirement | proposed | Use to select multiple options or toggle one |
| SR-0076 | system_requirement | proposed | Use radios for a single choice |
| SR-0077 | system_requirement | proposed | Position checkboxes to the left of labels |
| SR-0078 | system_requirement | proposed | Explain that multiple options can be selected |
| SR-0079 | system_requirement | proposed | Do not pre-select options |
| SR-0080 | system_requirement | proposed | Order options alphabetically by default |
| SR-0081 | system_requirement | proposed | Group checkboxes in a fieldset with a legend |
| SR-0082 | system_requirement | proposed | Set the legend as the heading for one question per page |
| SR-0083 | system_requirement | proposed | Keep item hints short and link-free |
| SR-0084 | system_requirement | proposed | Provide a 'none' option where valid |
| SR-0085 | system_requirement | proposed | Only conditionally reveal simple questions |
| SR-0086 | system_requirement | proposed | Conditional reveal is not always announced |
| SR-0087 | system_requirement | proposed | Use specific error messages |
<!-- tl:end -->

## Cookie banner

<!-- tl:item UR-0009 -->
**UR-0009 — Cookie banner** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Cookie banner component to let users accept or reject non-essential cookies, shown until a choice is made, with an accessible confirmation and a supporting cookies page.

*Rationale:* When a service sets non-essential cookies, users must be told about them and given a clear choice to accept or reject, so the service meets its data-protection obligations before storing anything on their device.

*Derives from:* INT-0002, INT-0003

**source_ref**: cookie-banner
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('cookie-banner#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0088 | system_requirement | proposed | Use when the service sets cookies |
| SR-0089 | system_requirement | proposed | Treat storage technologies as non-essential cookies |
| SR-0090 | system_requirement | proposed | Show the banner until the user decides |
| SR-0091 | system_requirement | proposed | Confirm the choice and remember it for a year |
| SR-0092 | system_requirement | proposed | Position the banner before the skip link |
| SR-0093 | system_requirement | proposed | Do not make the banner sticky |
| SR-0094 | system_requirement | proposed | Essential-only services still need a cookies page |
| SR-0095 | system_requirement | proposed | Support consent without JavaScript |
| SR-0096 | system_requirement | proposed | Move focus to the confirmation with assistive roles |
| SR-0097 | system_requirement | proposed | Name the service in the banner heading |
| SR-0098 | system_requirement | proposed | Keep cookie text short but accurate |
| SR-0099 | system_requirement | proposed | Provide a cookies page alongside the banner |
<!-- tl:end -->

## Details

<!-- tl:item UR-0010 -->
**UR-0010 — Details** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Details component to let users reveal more detailed information only if they need it, with short descriptive link text, for content only some users need.

*Rationale:* Users need a page to stay easy to scan when it holds information only some of them require, so less-important detail can be tucked away and revealed on demand rather than cluttering the page.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: details
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('details#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0100 | system_requirement | proposed | Use for information only some users need |
| SR-0101 | system_requirement | proposed | Do not hide information most users need |
| SR-0102 | system_requirement | proposed | Use for a single section of content |
| SR-0103 | system_requirement | proposed | Write short, descriptive link text |
| SR-0104 | system_requirement | proposed | Some users avoid the reveal link |
<!-- tl:end -->

## Error message

<!-- tl:item UR-0011 -->
**UR-0011 — Error message** — `user_requirement`, status `proposed`

> The service uses the GOV.UK Error message component to explain, next to each field, what went wrong and how to fix it, worded to match the error summary and following the plain-English error guidance.

*Rationale:* When a user's answer fails validation, they need a clear, specific message beside the field explaining what went wrong and how to fix it, so they can recover and correct their own input rather than being blocked.

*Derives from:* INT-0002, INT-0003

**source_ref**: error-message
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('error-message#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0105 | system_requirement | proposed | Show a message on each validation error |
| SR-0106 | system_requirement | proposed | Do not use for problems the user cannot fix |
| SR-0107 | system_requirement | proposed | Style and connect the message to its question |
| SR-0108 | system_requirement | proposed | Do not clear the user's answers |
| SR-0109 | system_requirement | proposed | Include a hidden 'Error:' prefix |
| SR-0110 | system_requirement | proposed | Summarise all errors at the top of the page |
| SR-0111 | system_requirement | proposed | Match the message to the question wording |
| SR-0112 | system_requirement | proposed | Write in plain, positive English |
| SR-0113 | system_requirement | proposed | Do not repeat an on-screen example |
| SR-0114 | system_requirement | proposed | Keep the field and summary messages identical |
| SR-0115 | system_requirement | proposed | Give a specific message per error state |
| SR-0116 | system_requirement | proposed | Use instructions and descriptions consistently |
| SR-0117 | system_requirement | proposed | Use the standard error message templates |
<!-- tl:end -->

## Exit this page

<!-- tl:item UR-0012 -->
**UR-0012 — Exit this page** — `user_requirement`, status `proposed`

> Exit this page gives users a way to quickly and safely leave a service, website or application when a page holds sensitive information that could put them at risk.

*Rationale:* So users who could be put at risk of abuse or retaliation by someone seeing sensitive pages, such as a victim escaping domestic abuse, can leave the service quickly and cover their tracks.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: exit-this-page
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('exit-this-page#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0118 | system_requirement | proposed | Pair with the Exit a page quickly pattern |
| SR-0119 | system_requirement | proposed | Use only for at-risk pages |
| SR-0120 | system_requirement | proposed | Apply to whole service or sensitive parts |
| SR-0121 | system_requirement | proposed | Do not use when risk is unlikely |
| SR-0122 | system_requirement | proposed | Position above the grid |
| SR-0123 | system_requirement | proposed | Choose a safe redirect destination |
| SR-0124 | system_requirement | proposed | Add the secondary skip link |
| SR-0125 | system_requirement | proposed | Decide how to handle session data |
| SR-0126 | system_requirement | proposed | Loading overlay clears the screen |
| SR-0127 | system_requirement | proposed | Support shift-key activation |
| SR-0128 | system_requirement | proposed | Offer discreet assistive-tech activation |
| SR-0129 | system_requirement | proposed | Grounded in lived-experience research |
| SR-0130 | system_requirement | proposed | Research with your own users first |
<!-- tl:end -->

## Fieldset

<!-- tl:item UR-0013 -->
**UR-0013 — Fieldset** — `user_requirement`, status `proposed`

> The fieldset component groups related form inputs so users understand the relationship between them.

*Rationale:* So users, especially screen reader users, understand that several separate form inputs are related and belong to a single question, such as the multiple text boxes making up an address.

*Derives from:* INT-0002, INT-0003

**source_ref**: fieldset
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('fieldset#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0131 | system_requirement | proposed | Use to group related inputs |
| SR-0132 | system_requirement | proposed | Reuse existing component fieldsets |
| SR-0133 | system_requirement | proposed | Legend must come first and describe the group |
| SR-0134 | system_requirement | proposed | Set the legend as the page heading for single questions |
| SR-0135 | system_requirement | proposed | Legend signals inputs are related |
| SR-0136 | system_requirement | proposed | Keep any legend help text short |
<!-- tl:end -->

## File upload

<!-- tl:item UR-0014 -->
**UR-0014 — File upload** — `user_requirement`, status `proposed`

> The file upload component helps users select and upload a file within a service.

*Rationale:* So users can reliably select and upload a file when providing that document is critical to delivering the service, with clear errors and drag-and-drop support that also works for assistive technology.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: file-upload
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('file-upload#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0137 | system_requirement | proposed | Ask for uploads only when critical |
| SR-0138 | system_requirement | proposed | Support choose-file and drag-and-drop |
| SR-0139 | system_requirement | proposed | Let users reuse uploaded files |
| SR-0140 | system_requirement | proposed | Follow error message guidance with specific errors |
| SR-0141 | system_requirement | proposed | Use the prescribed error wording |
| SR-0142 | system_requirement | proposed | Opt in to the improved component |
| SR-0143 | system_requirement | proposed | Keep changeable text short |
| SR-0144 | system_requirement | proposed | Keep required attributes on the original input |
| SR-0145 | system_requirement | proposed | Avoid the required attribute |
| SR-0146 | system_requirement | proposed | Improved component supports speech recognition |
| SR-0147 | system_requirement | proposed | Make the drop zone visible and responsive |
| SR-0148 | system_requirement | proposed | Interaction states refreshed for the brand |
| SR-0149 | system_requirement | proposed | Known gap in the earlier version |
<!-- tl:end -->

## GOV.UK footer

<!-- tl:item UR-0015 -->
**UR-0015 — GOV.UK footer** — `user_requirement`, status `proposed`

> The GOV.UK footer provides copyright, licensing and other information about a service and sits at the bottom of every page.

*Rationale:* So every page of a service clearly states who owns the copyright and under what licence content may be reused, and links users to privacy, accessibility, cookies and terms information.

*Derives from:* INT-0002, INT-0003

**source_ref**: footer
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('footer#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0150 | system_requirement | proposed | Use at the bottom of every page |
| SR-0151 | system_requirement | proposed | Add a copyright notice and coat of arms |
| SR-0152 | system_requirement | proposed | State the reuse licence |
| SR-0153 | system_requirement | proposed | Use standard footer link text |
| SR-0154 | system_requirement | proposed | Place help links consistently |
| SR-0155 | system_requirement | proposed | Add secondary navigation only for GOV.UK services |
| SR-0156 | system_requirement | proposed | Restrict the footer to GOV.UK services |
| SR-0157 | system_requirement | proposed | Use the refreshed branding |
<!-- tl:end -->

## GOV.UK header

<!-- tl:item UR-0016 -->
**UR-0016 — GOV.UK header** — `user_requirement`, status `proposed`

> The GOV.UK header tells users they are using a service on GOV.UK and gives access to GOV.UK-wide tools.

*Rationale:* So users trust they are in the right place on an official gov.uk service as they move around government websites, giving a consistent GOV.UK experience and access to GOV.UK-wide tools.

*Derives from:* INT-0003

**source_ref**: header
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('header#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0158 | system_requirement | proposed | Use only on GOV.UK domains |
| SR-0159 | system_requirement | proposed | Show on every page to maintain trust |
| SR-0160 | system_requirement | proposed | Do not use off GOV.UK domains |
| SR-0161 | system_requirement | proposed | Use the default header showing only logo and GOV.UK tools |
| SR-0162 | system_requirement | proposed | Do not show service name or navigation in the header |
| SR-0163 | system_requirement | proposed | Pair with service navigation for consistency |
| SR-0164 | system_requirement | proposed | Use the refreshed branding |
<!-- tl:end -->

## Inset text

<!-- tl:item UR-0017 -->
**UR-0017 — Inset text** — `user_requirement`, status `proposed`

> The inset text component differentiates a block of text from the surrounding content, such as quotes, examples or additional information.

*Rationale:* So a block of supporting text like a quote, example or extra note is visually differentiated from surrounding content, used sparingly since it is not reliable enough for very important information.

*Derives from:* INT-0003

**source_ref**: inset-text
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('inset-text#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0165 | system_requirement | proposed | Use to differentiate a block of text |
| SR-0166 | system_requirement | proposed | Do not use for very important information |
| SR-0167 | system_requirement | proposed | Use Warning text for critical content |
| SR-0168 | system_requirement | proposed | Use sparingly |
<!-- tl:end -->

## Notification banner

<!-- tl:item UR-0018 -->
**UR-0018 — Notification banner** — `user_requirement`, status `proposed`

> A notification banner tells the user about something they need to know that is not directly related to the page content, and a service uses it for service-wide problems, personal alerts, or the outcome of a completed action.

*Rationale:* Alerts users to something they need to know but that is not directly tied to the current task, such as a service-wide problem, an approaching deadline, or the outcome of a prior action, without cluttering the main content.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: notification-banner
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('notification-banner#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0169 | system_requirement | proposed | Use for information not directly relevant to the page task |
| SR-0170 | system_requirement | proposed | Use notification banners sparingly |
| SR-0171 | system_requirement | proposed | Put directly relevant information in the page content |
| SR-0172 | system_requirement | proposed | Do not use for validation errors |
| SR-0173 | system_requirement | proposed | Do not show alongside an error summary |
| SR-0174 | system_requirement | proposed | Position immediately before the page h1 |
| SR-0175 | system_requirement | proposed | Expose the banner as a labelled region |
| SR-0176 | system_requirement | proposed | Show only one notification banner per page |
| SR-0177 | system_requirement | proposed | Use h3 headings to structure content |
| SR-0178 | system_requirement | proposed | Use the neutral blue version for problems and elsewhere-events |
| SR-0179 | system_requirement | proposed | Use the green version to confirm an expected outcome |
| SR-0180 | system_requirement | proposed | Add role=alert so focus shifts on load |
| SR-0181 | system_requirement | proposed | Remove the green banner when moving to a new page |
| SR-0182 | system_requirement | proposed | Convey success meaning with a heading, not colour alone |
| SR-0183 | system_requirement | proposed | Use the same success heading consistently |
| SR-0184 | system_requirement | proposed | Open research questions |
<!-- tl:end -->

## Pagination

<!-- tl:item UR-0019 -->
**UR-0019 — Pagination** — `user_requirement`, status `proposed`

> Pagination helps users navigate forwards and backwards through a series of numbered pages, and a service uses it for collections such as search results or guidance split across multiple pages.

*Rationale:* Lets users navigate forwards and backwards through a series of numbered pages so that content split for performance or usability, like search results or multi-page guidance, stays fast to load and easy to move through.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: pagination
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('pagination#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0185 | system_requirement | proposed | Use when a single page loads too slowly or most users need only early pages |
| SR-0186 | system_requirement | proposed | Only paginate if it improves performance or usability |
| SR-0187 | system_requirement | proposed | Avoid infinite scroll |
| SR-0188 | system_requirement | proposed | Do not use for linear journeys |
| SR-0189 | system_requirement | proposed | Place pagination after the page content |
| SR-0190 | system_requirement | proposed | Do not show pagination for a single page |
| SR-0191 | system_requirement | proposed | Redirect to the first page for dead URLs |
| SR-0192 | system_requirement | proposed | Use block style for related content pages |
| SR-0193 | system_requirement | proposed | Use link labels for context |
| SR-0194 | system_requirement | proposed | Use list style for pages of items |
| SR-0195 | system_requirement | proposed | Show the page number in the page title |
| SR-0196 | system_requirement | proposed | Show pages appropriate to screen size |
| SR-0197 | system_requirement | proposed | Use ellipses for skipped pages |
| SR-0198 | system_requirement | proposed | Hide previous on first page and next on last page |
| SR-0199 | system_requirement | proposed | Apply filtering and sorting to the whole list |
| SR-0200 | system_requirement | proposed | Set defaults to reduce clicks |
| SR-0201 | system_requirement | proposed | Based on proven government components |
<!-- tl:end -->

## Panel

<!-- tl:item UR-0020 -->
**UR-0020 — Panel** — `user_requirement`, status `proposed`

> The panel component is a visible container used on confirmation or results pages to highlight important content, and a service uses it to confirm a completed transaction.

*Rationale:* Highlights that a transaction has been completed successfully on a confirmation or results page, giving users clear high-level reassurance and any reference they need once they finish.

*Derives from:* INT-0003

**source_ref**: panel
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('panel#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0202 | system_requirement | proposed | Use to display important information after a completed transaction |
| SR-0203 | system_requirement | proposed | Never use to highlight information in body content |
| SR-0204 | system_requirement | proposed | Keep panel text brief |
| SR-0205 | system_requirement | proposed | Use short words to stay readable at all sizes |
| SR-0206 | system_requirement | proposed | Use description text for detail |
<!-- tl:end -->

## Password input

<!-- tl:item UR-0021 -->
**UR-0021 — Password input** — `user_requirement`, status `proposed`

> The password input component helps users accessibly create and enter passwords, with an option to show what they have entered as plain text, and a service uses it whenever a password must be created or entered.

*Rationale:* Helps users create and enter passwords accessibly, letting them reveal what they typed to reduce errors and choose stronger, more unique passwords before submitting.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: password-input
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('password-input#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0207 | system_requirement | proposed | Use whenever a password is created or entered |
| SR-0208 | system_requirement | proposed | Do not use for non-password information |
| SR-0209 | system_requirement | proposed | Let users show their entry as plain text |
| SR-0210 | system_requirement | proposed | Do not reveal which credential was wrong |
| SR-0211 | system_requirement | proposed | Hide passwords by default |
| SR-0212 | system_requirement | proposed | Use distinct labels and toggles for multiple inputs |
| SR-0213 | system_requirement | proposed | Avoid a confirm password field |
| SR-0214 | system_requirement | proposed | Set input type to password on submit |
| SR-0215 | system_requirement | proposed | Use the autocomplete attribute |
| SR-0216 | system_requirement | proposed | Always allow copy and paste |
| SR-0217 | system_requirement | proposed | Support all characters and avoid restricting input |
| SR-0218 | system_requirement | proposed | Keep any restrictions identical and consistent |
| SR-0219 | system_requirement | proposed | Do not use maxlength to restrict length |
| SR-0220 | system_requirement | proposed | Disable spellcheck and autocapitalise |
| SR-0221 | system_requirement | proposed | Native show/hide tools can duplicate or mismatch |
| SR-0222 | system_requirement | proposed | Research decided against a second field |
<!-- tl:end -->

## Phase banner

<!-- tl:item UR-0022 -->
**UR-0022 — Phase banner** — `user_requirement`, status `proposed`

> The phase banner shows users a service is still being worked on, and a service.gov.uk service uses it to display its alpha or beta status until it passes a live assessment.

*Rationale:* Signals to users that a service is still being worked on in alpha or beta and invites feedback, as required for service.gov.uk domains until they pass a live assessment.

*Derives from:* INT-0003

**source_ref**: phase-banner
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('phase-banner#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0223 | system_requirement | proposed | Required on service.gov.uk until live assessment passed |
| SR-0224 | system_requirement | proposed | Use the alpha or beta banner to match the phase |
| SR-0225 | system_requirement | proposed | Show inside the header after navigation or GOV.UK header |
| SR-0226 | system_requirement | proposed | Show on all pages as a service-level message |
| SR-0227 | system_requirement | proposed | Include a feedback link |
| SR-0228 | system_requirement | proposed | Let users return to their place after feedback |
<!-- tl:end -->

## Radios

<!-- tl:item UR-0023 -->
**UR-0023 — Radios** — `user_requirement`, status `proposed`

> The radios component lets users select a single option from a list, and a service uses it when only one option can be chosen.

*Rationale:* Lets users select exactly one option from a list when the choices are mutually exclusive, making the single-answer constraint clear and preventing the confusion of allowing multiple selections.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: radios
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('radios#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0229 | system_requirement | proposed | Use when only one option can be selected |
| SR-0230 | system_requirement | proposed | Do not use when multiple selections are possible |
| SR-0231 | system_requirement | proposed | Position radios to the left of their labels |
| SR-0232 | system_requirement | proposed | Add a hint that only one option can be chosen |
| SR-0233 | system_requirement | proposed | Do not pre-select an option |
| SR-0234 | system_requirement | proposed | Include a 'None of the above' option when valid |
| SR-0235 | system_requirement | proposed | Order options alphabetically by default |
| SR-0236 | system_requirement | proposed | Group radios in a fieldset with a describing legend |
| SR-0237 | system_requirement | proposed | Set legend as page heading when asking one question |
| SR-0238 | system_requirement | proposed | Do not set legend as heading with multiple questions |
| SR-0239 | system_requirement | proposed | Only use inline radios for two short options |
| SR-0240 | system_requirement | proposed | Keep item hints to one short sentence with no links |
| SR-0241 | system_requirement | proposed | Separate a distinct option with a text divider |
| SR-0242 | system_requirement | proposed | Keep conditionally revealed questions simple |
| SR-0243 | system_requirement | proposed | Restrict conditional reveal to questions only |
| SR-0244 | system_requirement | proposed | Conditional reveal has a known notification gap |
| SR-0245 | system_requirement | proposed | Use smaller radios only when less prominence helps |
| SR-0246 | system_requirement | proposed | Show an error when no radio or revealed question is answered |
| SR-0247 | system_requirement | proposed | Word errors according to the option pattern |
| SR-0248 | system_requirement | proposed | Research found simple conditional reveals workable |
<!-- tl:end -->

## Select

<!-- tl:item UR-0024 -->
**UR-0024 — Select** — `user_requirement`, status `proposed`

> The select component helps users choose a single item from a long list, used only as a last resort in public-facing services because some users find selects hard to use.

*Rationale:* Offers a last-resort way to pick one option from a long list in public services, but should be avoided because research shows many users struggle to open, scroll, and choose within selects, so ask narrowing questions or use radios instead.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: select
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('select#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0249 | system_requirement | proposed | Use only as a last resort |
| SR-0250 | system_requirement | proposed | Reduce options before using select |
| SR-0251 | system_requirement | proposed | Pre-select only for settings |
| SR-0252 | system_requirement | proposed | Do not pre-select for questions |
| SR-0253 | system_requirement | proposed | Keep hint text short |
| SR-0254 | system_requirement | proposed | No links in hint text |
| SR-0255 | system_requirement | proposed | Show error when no option selected |
| SR-0256 | system_requirement | proposed | Avoid multiple selection |
| SR-0257 | system_requirement | proposed | Known usability struggles |
<!-- tl:end -->

## Service navigation

<!-- tl:item UR-0025 -->
**UR-0025 — Service navigation** — `user_requirement`, status `proposed`

> Service navigation helps users understand they are using your service and lets them navigate around it, showing the service name and optional navigation links.

*Rationale:* Reassures users that they are in the right place within a specific service and lets them move between its parts, giving a consistent experience that shows GOV.UK functions as one coherent website.

*Derives from:* INT-0002, INT-0003

**source_ref**: service-navigation
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('service-navigation#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0258 | system_requirement | proposed | Use to identify the service |
| SR-0259 | system_requirement | proposed | Pair with the GOV.UK header |
| SR-0260 | system_requirement | proposed | Show the service name |
| SR-0261 | system_requirement | proposed | Show navigation links |
| SR-0262 | system_requirement | proposed | Use slots for custom elements |
| SR-0263 | system_requirement | proposed | Keep aria-label accurate |
| SR-0264 | system_requirement | proposed | Retest slots on each update |
| SR-0265 | system_requirement | proposed | Use refreshed GOV.UK branding |
<!-- tl:end -->

## Skip link

<!-- tl:item UR-0026 -->
**UR-0026 — Skip link** — `user_requirement`, status `proposed`

> The skip link component helps keyboard-only users skip the top-level navigation and jump straight to the main content on a page.

*Rationale:* Lets keyboard-only users bypass repetitive top-level navigation links and jump straight to a page's main content, removing the burden of tabbing through the header on every page.

*Derives from:* INT-0002, INT-0003

**source_ref**: skip-link
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('skip-link#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0266 | system_requirement | proposed | Include on every GOV.UK page |
| SR-0267 | system_requirement | proposed | Place after the opening body tag |
| SR-0268 | system_requirement | proposed | Ignore the landmark warning |
| SR-0269 | system_requirement | proposed | Let users bypass navigation |
| SR-0270 | system_requirement | proposed | Hidden until keyboard activation |
<!-- tl:end -->

## Summary list

<!-- tl:item UR-0027 -->
**UR-0027 — Summary list** — `user_requirement`, status `proposed`

> A summary list summarises information as a list of key facts, such as a user's responses at the end of a form, with an optional summary card variant for grouping multiple lists.

*Rationale:* Presents information as key-and-value facts, such as metadata or a user's form answers at the end of a journey, so people can review and correct their responses before submitting.

*Derives from:* INT-0002, INT-0003

**source_ref**: summary-list
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('summary-list#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0271 | system_requirement | proposed | Use for a list of key facts |
| SR-0272 | system_requirement | proposed | Only for key-and-value information |
| SR-0273 | system_requirement | proposed | Do not use for tables or simple lists |
| SR-0274 | system_requirement | proposed | Structure each row as key and value |
| SR-0275 | system_requirement | proposed | Add structure to multiple lists |
| SR-0276 | system_requirement | proposed | Add visually hidden text to row actions |
| SR-0277 | system_requirement | proposed | Pre-populate when returning to answers |
| SR-0278 | system_requirement | proposed | Mark rows without actions |
| SR-0279 | system_requirement | proposed | Think carefully before removing borders |
| SR-0280 | system_requirement | proposed | Link to complete missing information |
| SR-0281 | system_requirement | proposed | Use summary cards for same-type lists |
| SR-0282 | system_requirement | proposed | Do not use cards for small amounts |
| SR-0283 | system_requirement | proposed | Give each card a unique title |
| SR-0284 | system_requirement | proposed | Write clear card action link text |
| SR-0285 | system_requirement | proposed | Limit card actions |
| SR-0286 | system_requirement | proposed | Confirm serious card actions |
<!-- tl:end -->

## Table

<!-- tl:item UR-0028 -->
**UR-0028 — Table** — `user_requirement`, status `proposed`

> The table component presents information in rows and columns to make it easier for users to compare and scan.

*Rationale:* Makes information easier to compare and scan by arranging related data into rows and columns, so users can read across shared attributes rather than hunting through prose.

*Derives from:* INT-0002, INT-0003

**source_ref**: table
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('table#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0287 | system_requirement | proposed | Use to compare information |
| SR-0288 | system_requirement | proposed | Never use for layout |
| SR-0289 | system_requirement | proposed | Describe the table with a caption |
| SR-0290 | system_requirement | proposed | Use headers with scope |
| SR-0291 | system_requirement | proposed | Right-align columns of numbers |
| SR-0292 | system_requirement | proposed | Reduce data in tables |
| SR-0293 | system_requirement | proposed | Only shrink text for lots of data |
<!-- tl:end -->

## Tabs

<!-- tl:item UR-0029 -->
**UR-0029 — Tabs** — `user_requirement`, status `proposed`

> The tabs component lets users quickly switch between related sections of content, displaying one clearly labelled section at a time.

*Rationale:* Lets regular or expert users quickly switch between clearly labelled related sections without viewing all at once, but is avoided when users must read in order or compare content, since tabs hide information many people miss.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: tabs
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('tabs#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0294 | system_requirement | proposed | Use for clearly separable sections |
| SR-0295 | system_requirement | proposed | Do not use for heavy or navigational content |
| SR-0296 | system_requirement | proposed | Do not use for ordered or comparison content |
| SR-0297 | system_requirement | proposed | Test content without tabs first |
| SR-0298 | system_requirement | proposed | Choose tabs versus accordion or details |
| SR-0299 | system_requirement | proposed | Provide a no-JavaScript fallback |
| SR-0300 | system_requirement | proposed | Use clear tab labels |
| SR-0301 | system_requirement | proposed | Order tabs by user need |
| SR-0302 | system_requirement | proposed | Do not disable tabs |
| SR-0303 | system_requirement | proposed | Avoid tabs wrapping onto multiple lines |
| SR-0304 | system_requirement | proposed | Add a heading to each tab's content |
| SR-0305 | system_requirement | proposed | Not yet tested with users |
<!-- tl:end -->

## Tag

<!-- tl:item UR-0030 -->
**UR-0030 — Tag** — `user_requirement`, status `proposed`

> As a service, I use the Tag component to show users the status of something, such as an item on a task list or a phase banner.

*Rationale:* Lets users see at a glance the current status of something that can hold more than one state, such as whether a task-list item is completed or a user is active, so they know where things stand without reading further.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: tag
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('tag#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0306 | system_requirement | proposed | Use when a thing can have more than one status |
| SR-0307 | system_requirement | proposed | Use tags only to indicate status |
| SR-0308 | system_requirement | proposed | Do not make tags interactive |
| SR-0309 | system_requirement | proposed | Name tags with adjectives |
| SR-0310 | system_requirement | proposed | Start with the fewest statuses |
| SR-0311 | system_requirement | proposed | A single status can be enough |
| SR-0312 | system_requirement | proposed | Do not convey information by colour alone |
| SR-0313 | system_requirement | proposed | Keep tag colour consistent across uses |
| SR-0314 | system_requirement | proposed | Use colour to distinguish or emphasise |
| SR-0315 | system_requirement | proposed | Tags no longer use uppercase text |
| SR-0316 | system_requirement | proposed | Tag styling changed to avoid looking like buttons |
<!-- tl:end -->

## Task list

<!-- tl:item UR-0031 -->
**UR-0031 — Task list** — `user_requirement`, status `proposed`

> As a service, I use the task list component to display all the tasks a user needs to do and let them see which are done and which remain.

*Rationale:* Gives users control over long, complex services they cannot or do not want to finish in one sitting, letting them choose their own order and clearly see which tasks are done and which remain.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: task-list
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('task-list#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0317 | system_requirement | proposed | Use to give control over long, complex services |
| SR-0318 | system_requirement | proposed | Only use with supporting evidence |
| SR-0319 | system_requirement | proposed | Try to simplify the service first |
| SR-0320 | system_requirement | proposed | Do not use for strictly ordered services |
| SR-0321 | system_requirement | proposed | Do not use to show users their answers |
| SR-0322 | system_requirement | proposed | Let users complete tasks in any order |
| SR-0323 | system_requirement | proposed | Status indicates whether a task can be started |
| SR-0324 | system_requirement | proposed | Only allow moving on when all tasks are completed |
| SR-0325 | system_requirement | proposed | Each task has a name and a status |
| SR-0326 | system_requirement | proposed | Link the whole task row |
| SR-0327 | system_requirement | proposed | Write clear, short task names in sentence case |
| SR-0328 | system_requirement | proposed | Split tasks that are hard to name concisely |
| SR-0329 | system_requirement | proposed | Keep hint text to one short sentence |
| SR-0330 | system_requirement | proposed | Do not put links in hint text |
| SR-0331 | system_requirement | proposed | Group tasks under clear headings |
| SR-0332 | system_requirement | proposed | Statuses use colour and a short descriptor |
| SR-0333 | system_requirement | proposed | Statuses redesigned and rows linked after feedback |
| SR-0334 | system_requirement | proposed | Statuses moved to sentence case for readability |
| SR-0335 | system_requirement | proposed | Component still needs user testing |
<!-- tl:end -->

## Textarea

<!-- tl:item UR-0032 -->
**UR-0032 — Textarea** — `user_requirement`, status `proposed`

> As a service, I use the textarea component to let users enter an amount of text that is longer than a single line.

*Rationale:* Lets users provide answers longer than a single line, giving space for detailed free-text information that would not fit in a standard single-line input field.

*Derives from:* INT-0002, INT-0003

**source_ref**: textarea
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('textarea#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0336 | system_requirement | proposed | Use for text longer than a single line |
| SR-0337 | system_requirement | proposed | Consider breaking up open-ended questions |
| SR-0338 | system_requirement | proposed | Do not use for single-line answers |
| SR-0339 | system_requirement | proposed | Always label the textarea |
| SR-0340 | system_requirement | proposed | Align labels above and use sentence case |
| SR-0341 | system_requirement | proposed | Size the textarea to expected input |
| SR-0342 | system_requirement | proposed | Do not disable copy and paste |
| SR-0343 | system_requirement | proposed | Label is not the page heading with multiple questions |
| SR-0344 | system_requirement | proposed | Limit character count with the right component |
| SR-0345 | system_requirement | proposed | Use specific error messages per state |
<!-- tl:end -->

## Text input

<!-- tl:item UR-0033 -->
**UR-0033 — Text input** — `user_requirement`, status `proposed`

> As a service, I use the text input component to let users enter text no longer than a single line, such as their name or phone number.

*Rationale:* Lets users enter short, single-line information such as a name or phone number, providing an appropriately sized field so they understand what is expected without spanning multiple lines.

*Derives from:* INT-0002, INT-0003, INT-0004

**source_ref**: text-input
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('text-input#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0346 | system_requirement | proposed | Use for single-line text |
| SR-0347 | system_requirement | proposed | Do not use for multi-line answers |
| SR-0348 | system_requirement | proposed | All inputs must have labels |
| SR-0349 | system_requirement | proposed | Align labels above and use sentence case |
| SR-0350 | system_requirement | proposed | Avoid placeholder text |
| SR-0351 | system_requirement | proposed | Use label as heading for one question per page |
| SR-0352 | system_requirement | proposed | Label is not the page heading with multiple questions |
| SR-0353 | system_requirement | proposed | Size inputs to the expected content |
| SR-0354 | system_requirement | proposed | Use hint text for widely relevant help |
| SR-0355 | system_requirement | proposed | Do not put links in hint text |
| SR-0356 | system_requirement | proposed | Do not use hint text for long explanations |
| SR-0357 | system_requirement | proposed | Set inputmode numeric for whole numbers |
| SR-0358 | system_requirement | proposed | Set inputmode decimal for decimals |
| SR-0359 | system_requirement | proposed | Avoid input type number |
| SR-0360 | system_requirement | proposed | Visually separate characters in codes |
| SR-0361 | system_requirement | proposed | Do not rely on prefixes or suffixes alone |
| SR-0362 | system_requirement | proposed | Position prefixes and suffixes outside the input |
| SR-0363 | system_requirement | proposed | Use the autocomplete attribute |
| SR-0364 | system_requirement | proposed | Do not disable copy and paste |
| SR-0365 | system_requirement | proposed | Avoid restricting input length |
| SR-0366 | system_requirement | proposed | Disable spellcheck where inappropriate |
| SR-0367 | system_requirement | proposed | Use specific error messages per state |
| SR-0368 | system_requirement | proposed | Support all characters the user needs |
| SR-0369 | system_requirement | proposed | Problems found with input type number |
| SR-0370 | system_requirement | proposed | Some users clicked on prefixes |
<!-- tl:end -->

## Warning text

<!-- tl:item UR-0034 -->
**UR-0034 — Warning text** — `user_requirement`, status `proposed`

> As a service, I use the warning text component to warn users about something important, such as legal consequences of an action or inaction.

*Rationale:* Draws users' attention to something genuinely important, such as the legal consequences of an action or inaction, so they do not overlook a critical warning before deciding what to do.

*Derives from:* INT-0002, INT-0003

**source_ref**: warning-text
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('warning-text#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0371 | system_requirement | proposed | Use to warn about something important |
| SR-0372 | system_requirement | proposed | Adapt the hidden text to context |
<!-- tl:end -->

## Generic header

<!-- tl:item UR-0035 -->
**UR-0035 — Generic header** — `user_requirement`, status `proposed`

> As a service, I use the Generic header component to tell users they are using a government service that is not part of the GOV.UK website.

*Rationale:* Signals to users that a public-facing government service sits outside the GOV.UK website, maintaining trust and consistency across journeys while ensuring non-GOV.UK services do not misuse GOV.UK branding.

*Derives from:* INT-0002, INT-0003

**source_ref**: generic-header
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('generic-header#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0373 | system_requirement | proposed | Use for public services not on GOV.UK |
| SR-0374 | system_requirement | proposed | Bring consistency across cross-government journeys |
| SR-0375 | system_requirement | proposed | Do not use GOV.UK branding in the header |
| SR-0376 | system_requirement | proposed | Do not use on gov.uk domains |
| SR-0377 | system_requirement | proposed | Replace the default header in the page template |
| SR-0378 | system_requirement | proposed | Display your own brand logo, link, and font |
| SR-0379 | system_requirement | proposed | Make the brand logo accessible and optimised |
| SR-0380 | system_requirement | proposed | Customise the homepage link |
| SR-0381 | system_requirement | proposed | Do not show navigation links in the header |
<!-- tl:end -->

