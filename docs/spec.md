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
**INT-0002 — Government services are accessible to everyone** — `intent`, status `approved`

> Services built from the Design System work for everyone, including disabled people and people using assistive technology such as screen readers, keyboards and voice control, meeting WCAG 2.2 level AA and the Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations 2018.

**source_ref**: accessibility
<!-- tl:end -->

<!-- tl:item INT-0003 -->
**INT-0003 — Components are used consistently and correctly across services** — `intent`, status `approved`

> Teams reuse each component as intended, with consistent structure, content and wording, so users recognise and trust government services and can transfer what they learn from one service to the next instead of teams reinventing interface elements service by service.

**source_ref**: consistent-use
<!-- tl:end -->

<!-- tl:item INT-0004 -->
**INT-0004 — Components are proven by user research** — `intent`, status `approved`

> Each component is shaped and validated by user research and testing, so services adopt solutions already shown to help people complete their task first time with fewer errors, rather than untested designs.

**source_ref**: proven-by-research
<!-- tl:end -->

## Button

<!-- tl:item UR-0001 -->
**UR-0001 — Button** — `user_requirement`, status `approved`

> The service uses the GOV.UK Button component to let users carry out an action, following its guidance on button text, variants, grouping, contrast and double-click prevention.

*Rationale:* Users need an unambiguous, prominent way to carry out an action such as starting an application, signing in, or paying, so the main call to action stands out and they always know what to do next.

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

*Rationale:* When a user submits answers containing validation errors, they need every problem gathered and focused at the top of the page so they can find, understand, and fix each mistake rather than hunting for what went wrong.

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

*Rationale:* Users entering a date they already know or can look up need to type the day, month and year directly, avoiding the friction of a calendar picker for dates that are memorable rather than chosen.

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

*Rationale:* When users benefit from an overview of related sections and want to reveal, hide, and compare only the parts relevant to them, this lets them control long or repeat-use content instead of scrolling through everything at once.

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

*Rationale:* Because browser back buttons can break services or go unnoticed, users in a multi-page transaction need a reliable in-page way to return to the previous step without losing their progress.

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

*Rationale:* Users navigating a site with multiple hierarchical levels need to understand where they are and move up between levels, so they can orient themselves within the wider structure.

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

*Rationale:* When a genuine legal or technical limit caps how much a user can enter, they need live feedback on characters or words remaining so they can write their full answer and then edit it down without being cut off unexpectedly.

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

## Checkboxes

<!-- tl:item UR-0008 -->
**UR-0008 — Checkboxes** — `user_requirement`, status `approved`

> The service uses the GOV.UK Checkboxes component to let users select one or more options, grouped in a fieldset with an accessible legend, ordered and labelled to guidance.

*Rationale:* Users need to select one or more options from a list, or toggle a single option on or off, when a question genuinely allows multiple answers rather than a single mutually-exclusive choice.

**source_ref**: checkboxes
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('checkboxes#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0075 | system_requirement | approved | Use to select multiple options or toggle one |
| SR-0076 | system_requirement | approved | Use radios for a single choice |
| SR-0077 | system_requirement | approved | Position checkboxes to the left of labels |
| SR-0078 | system_requirement | approved | Explain that multiple options can be selected |
| SR-0079 | system_requirement | approved | Do not pre-select options |
| SR-0080 | system_requirement | approved | Order options alphabetically by default |
| SR-0081 | system_requirement | approved | Group checkboxes in a fieldset with a legend |
| SR-0082 | system_requirement | approved | Set the legend as the heading for one question per page |
| SR-0083 | system_requirement | approved | Keep item hints short and link-free |
| SR-0084 | system_requirement | approved | Provide a 'none' option where valid |
| SR-0085 | system_requirement | approved | Only conditionally reveal simple questions |
| SR-0086 | system_requirement | approved | Conditional reveal is not always announced |
| SR-0087 | system_requirement | approved | Use specific error messages |
<!-- tl:end -->

## Cookie banner

<!-- tl:item UR-0009 -->
**UR-0009 — Cookie banner** — `user_requirement`, status `approved`

> The service uses the GOV.UK Cookie banner component to let users accept or reject non-essential cookies, shown until a choice is made, with an accessible confirmation and a supporting cookies page.

*Rationale:* When a service sets non-essential cookies, users must be told about them and given a clear choice to accept or reject, so the service meets its data-protection obligations before storing anything on their device.

**source_ref**: cookie-banner
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('cookie-banner#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0088 | system_requirement | approved | Use when the service sets cookies |
| SR-0089 | system_requirement | approved | Treat storage technologies as non-essential cookies |
| SR-0090 | system_requirement | approved | Show the banner until the user decides |
| SR-0091 | system_requirement | approved | Confirm the choice and remember it for a year |
| SR-0092 | system_requirement | approved | Position the banner before the skip link |
| SR-0093 | system_requirement | approved | Do not make the banner sticky |
| SR-0094 | system_requirement | approved | Essential-only services still need a cookies page |
| SR-0095 | system_requirement | approved | Support consent without JavaScript |
| SR-0096 | system_requirement | approved | Move focus to the confirmation with assistive roles |
| SR-0097 | system_requirement | approved | Name the service in the banner heading |
| SR-0098 | system_requirement | approved | Keep cookie text short but accurate |
| SR-0099 | system_requirement | approved | Provide a cookies page alongside the banner |
<!-- tl:end -->

## Details

<!-- tl:item UR-0010 -->
**UR-0010 — Details** — `user_requirement`, status `approved`

> The service uses the GOV.UK Details component to let users reveal more detailed information only if they need it, with short descriptive link text, for content only some users need.

*Rationale:* Users need a page to stay easy to scan when it holds information only some of them require, so less-important detail can be tucked away and revealed on demand rather than cluttering the page.

**source_ref**: details
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('details#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0100 | system_requirement | approved | Use for information only some users need |
| SR-0101 | system_requirement | approved | Do not hide information most users need |
| SR-0102 | system_requirement | approved | Use for a single section of content |
| SR-0103 | system_requirement | approved | Write short, descriptive link text |
| SR-0104 | system_requirement | approved | Some users avoid the reveal link |
<!-- tl:end -->

## Error message

<!-- tl:item UR-0011 -->
**UR-0011 — Error message** — `user_requirement`, status `approved`

> The service uses the GOV.UK Error message component to explain, next to each field, what went wrong and how to fix it, worded to match the error summary and following the plain-English error guidance.

*Rationale:* When a user's answer fails validation, they need a clear, specific message beside the field explaining what went wrong and how to fix it, so they can recover and correct their own input rather than being blocked.

**source_ref**: error-message
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('error-message#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0105 | system_requirement | approved | Show a message on each validation error |
| SR-0106 | system_requirement | approved | Do not use for problems the user cannot fix |
| SR-0107 | system_requirement | approved | Style and connect the message to its question |
| SR-0108 | system_requirement | approved | Do not clear the user's answers |
| SR-0109 | system_requirement | approved | Include a hidden 'Error:' prefix |
| SR-0110 | system_requirement | approved | Summarise all errors at the top of the page |
| SR-0111 | system_requirement | approved | Match the message to the question wording |
| SR-0112 | system_requirement | approved | Write in plain, positive English |
| SR-0113 | system_requirement | approved | Do not repeat an on-screen example |
| SR-0114 | system_requirement | approved | Keep the field and summary messages identical |
| SR-0115 | system_requirement | approved | Give a specific message per error state |
| SR-0116 | system_requirement | approved | Use instructions and descriptions consistently |
| SR-0117 | system_requirement | approved | Use the standard error message templates |
<!-- tl:end -->

## Exit this page

<!-- tl:item UR-0012 -->
**UR-0012 — Exit this page** — `user_requirement`, status `approved`

> Exit this page gives users a way to quickly and safely leave a service, website or application when a page holds sensitive information that could put them at risk.

*Rationale:* So users who could be put at risk of abuse or retaliation by someone seeing sensitive pages, such as a victim escaping domestic abuse, can leave the service quickly and cover their tracks.

**source_ref**: exit-this-page
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('exit-this-page#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0118 | system_requirement | approved | Pair with the Exit a page quickly pattern |
| SR-0119 | system_requirement | approved | Use only for at-risk pages |
| SR-0120 | system_requirement | approved | Apply to whole service or sensitive parts |
| SR-0121 | system_requirement | approved | Do not use when risk is unlikely |
| SR-0122 | system_requirement | approved | Position above the grid |
| SR-0123 | system_requirement | approved | Choose a safe redirect destination |
| SR-0124 | system_requirement | approved | Add the secondary skip link |
| SR-0125 | system_requirement | approved | Decide how to handle session data |
| SR-0126 | system_requirement | approved | Loading overlay clears the screen |
| SR-0127 | system_requirement | approved | Support shift-key activation |
| SR-0128 | system_requirement | approved | Offer discreet assistive-tech activation |
| SR-0129 | system_requirement | approved | Grounded in lived-experience research |
| SR-0130 | system_requirement | approved | Research with your own users first |
<!-- tl:end -->

## Fieldset

<!-- tl:item UR-0013 -->
**UR-0013 — Fieldset** — `user_requirement`, status `approved`

> The fieldset component groups related form inputs so users understand the relationship between them.

*Rationale:* So users, especially screen reader users, understand that several separate form inputs are related and belong to a single question, such as the multiple text boxes making up an address.

**source_ref**: fieldset
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('fieldset#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0131 | system_requirement | approved | Use to group related inputs |
| SR-0132 | system_requirement | approved | Reuse existing component fieldsets |
| SR-0133 | system_requirement | approved | Legend must come first and describe the group |
| SR-0134 | system_requirement | approved | Set the legend as the page heading for single questions |
| SR-0135 | system_requirement | approved | Legend signals inputs are related |
| SR-0136 | system_requirement | approved | Keep any legend help text short |
<!-- tl:end -->

## File upload

<!-- tl:item UR-0014 -->
**UR-0014 — File upload** — `user_requirement`, status `approved`

> The file upload component helps users select and upload a file within a service.

*Rationale:* So users can reliably select and upload a file when providing that document is critical to delivering the service, with clear errors and drag-and-drop support that also works for assistive technology.

**source_ref**: file-upload
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('file-upload#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0137 | system_requirement | approved | Ask for uploads only when critical |
| SR-0138 | system_requirement | approved | Support choose-file and drag-and-drop |
| SR-0139 | system_requirement | approved | Let users reuse uploaded files |
| SR-0140 | system_requirement | approved | Follow error message guidance with specific errors |
| SR-0141 | system_requirement | approved | Use the prescribed error wording |
| SR-0142 | system_requirement | approved | Opt in to the improved component |
| SR-0143 | system_requirement | approved | Keep changeable text short |
| SR-0144 | system_requirement | approved | Keep required attributes on the original input |
| SR-0145 | system_requirement | approved | Avoid the required attribute |
| SR-0146 | system_requirement | approved | Improved component supports speech recognition |
| SR-0147 | system_requirement | approved | Make the drop zone visible and responsive |
| SR-0148 | system_requirement | approved | Interaction states refreshed for the brand |
| SR-0149 | system_requirement | approved | Known gap in the earlier version |
<!-- tl:end -->

## GOV.UK footer

<!-- tl:item UR-0015 -->
**UR-0015 — GOV.UK footer** — `user_requirement`, status `approved`

> The GOV.UK footer provides copyright, licensing and other information about a service and sits at the bottom of every page.

*Rationale:* So every page of a service clearly states who owns the copyright and under what licence content may be reused, and links users to privacy, accessibility, cookies and terms information.

**source_ref**: footer
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('footer#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0150 | system_requirement | approved | Use at the bottom of every page |
| SR-0151 | system_requirement | approved | Add a copyright notice and coat of arms |
| SR-0152 | system_requirement | approved | State the reuse licence |
| SR-0153 | system_requirement | approved | Use standard footer link text |
| SR-0154 | system_requirement | approved | Place help links consistently |
| SR-0155 | system_requirement | approved | Add secondary navigation only for GOV.UK services |
| SR-0156 | system_requirement | approved | Restrict the footer to GOV.UK services |
| SR-0157 | system_requirement | approved | Use the refreshed branding |
<!-- tl:end -->

## GOV.UK header

<!-- tl:item UR-0016 -->
**UR-0016 — GOV.UK header** — `user_requirement`, status `approved`

> The GOV.UK header tells users they are using a service on GOV.UK and gives access to GOV.UK-wide tools.

*Rationale:* So users trust they are in the right place on an official gov.uk service as they move around government websites, giving a consistent GOV.UK experience and access to GOV.UK-wide tools.

**source_ref**: header
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('header#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0158 | system_requirement | approved | Use only on GOV.UK domains |
| SR-0159 | system_requirement | approved | Show on every page to maintain trust |
| SR-0160 | system_requirement | approved | Do not use off GOV.UK domains |
| SR-0161 | system_requirement | approved | Use the default header showing only logo and GOV.UK tools |
| SR-0162 | system_requirement | approved | Do not show service name or navigation in the header |
| SR-0163 | system_requirement | approved | Pair with service navigation for consistency |
| SR-0164 | system_requirement | approved | Use the refreshed branding |
<!-- tl:end -->

## Inset text

<!-- tl:item UR-0017 -->
**UR-0017 — Inset text** — `user_requirement`, status `approved`

> The inset text component differentiates a block of text from the surrounding content, such as quotes, examples or additional information.

*Rationale:* So a block of supporting text like a quote, example or extra note is visually differentiated from surrounding content, used sparingly since it is not reliable enough for very important information.

**source_ref**: inset-text
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('inset-text#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0165 | system_requirement | approved | Use to differentiate a block of text |
| SR-0166 | system_requirement | approved | Do not use for very important information |
| SR-0167 | system_requirement | approved | Use Warning text for critical content |
| SR-0168 | system_requirement | approved | Use sparingly |
<!-- tl:end -->

## Notification banner

<!-- tl:item UR-0018 -->
**UR-0018 — Notification banner** — `user_requirement`, status `approved`

> A notification banner tells the user about something they need to know that is not directly related to the page content, and a service uses it for service-wide problems, personal alerts, or the outcome of a completed action.

*Rationale:* Alerts users to something they need to know but that is not directly tied to the current task, such as a service-wide problem, an approaching deadline, or the outcome of a prior action, without cluttering the main content.

**source_ref**: notification-banner
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('notification-banner#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0169 | system_requirement | approved | Use for information not directly relevant to the page task |
| SR-0170 | system_requirement | approved | Use notification banners sparingly |
| SR-0171 | system_requirement | approved | Put directly relevant information in the page content |
| SR-0172 | system_requirement | approved | Do not use for validation errors |
| SR-0173 | system_requirement | approved | Do not show alongside an error summary |
| SR-0174 | system_requirement | approved | Position immediately before the page h1 |
| SR-0175 | system_requirement | approved | Expose the banner as a labelled region |
| SR-0176 | system_requirement | approved | Show only one notification banner per page |
| SR-0177 | system_requirement | approved | Use h3 headings to structure content |
| SR-0178 | system_requirement | approved | Use the neutral blue version for problems and elsewhere-events |
| SR-0179 | system_requirement | approved | Use the green version to confirm an expected outcome |
| SR-0180 | system_requirement | approved | Add role=alert so focus shifts on load |
| SR-0181 | system_requirement | approved | Remove the green banner when moving to a new page |
| SR-0182 | system_requirement | approved | Convey success meaning with a heading, not colour alone |
| SR-0183 | system_requirement | approved | Use the same success heading consistently |
| SR-0184 | system_requirement | approved | Open research questions |
<!-- tl:end -->

## Pagination

<!-- tl:item UR-0019 -->
**UR-0019 — Pagination** — `user_requirement`, status `approved`

> Pagination helps users navigate forwards and backwards through a series of numbered pages, and a service uses it for collections such as search results or guidance split across multiple pages.

*Rationale:* Lets users navigate forwards and backwards through a series of numbered pages so that content split for performance or usability, like search results or multi-page guidance, stays fast to load and easy to move through.

**source_ref**: pagination
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('pagination#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0185 | system_requirement | approved | Use when a single page loads too slowly or most users need only early pages |
| SR-0186 | system_requirement | approved | Only paginate if it improves performance or usability |
| SR-0187 | system_requirement | approved | Avoid infinite scroll |
| SR-0188 | system_requirement | approved | Do not use for linear journeys |
| SR-0189 | system_requirement | approved | Place pagination after the page content |
| SR-0190 | system_requirement | approved | Do not show pagination for a single page |
| SR-0191 | system_requirement | approved | Redirect to the first page for dead URLs |
| SR-0192 | system_requirement | approved | Use block style for related content pages |
| SR-0193 | system_requirement | approved | Use link labels for context |
| SR-0194 | system_requirement | approved | Use list style for pages of items |
| SR-0195 | system_requirement | approved | Show the page number in the page title |
| SR-0196 | system_requirement | approved | Show pages appropriate to screen size |
| SR-0197 | system_requirement | approved | Use ellipses for skipped pages |
| SR-0198 | system_requirement | approved | Hide previous on first page and next on last page |
| SR-0199 | system_requirement | approved | Apply filtering and sorting to the whole list |
| SR-0200 | system_requirement | approved | Set defaults to reduce clicks |
| SR-0201 | system_requirement | approved | Based on proven government components |
<!-- tl:end -->

## Panel

<!-- tl:item UR-0020 -->
**UR-0020 — Panel** — `user_requirement`, status `approved`

> The panel component is a visible container used on confirmation or results pages to highlight important content, and a service uses it to confirm a completed transaction.

*Rationale:* Highlights that a transaction has been completed successfully on a confirmation or results page, giving users clear high-level reassurance and any reference they need once they finish.

**source_ref**: panel
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('panel#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0202 | system_requirement | approved | Use to display important information after a completed transaction |
| SR-0203 | system_requirement | approved | Never use to highlight information in body content |
| SR-0204 | system_requirement | approved | Keep panel text brief |
| SR-0205 | system_requirement | approved | Use short words to stay readable at all sizes |
| SR-0206 | system_requirement | approved | Use description text for detail |
<!-- tl:end -->

## Password input

<!-- tl:item UR-0021 -->
**UR-0021 — Password input** — `user_requirement`, status `approved`

> The password input component helps users accessibly create and enter passwords, with an option to show what they have entered as plain text, and a service uses it whenever a password must be created or entered.

*Rationale:* Helps users create and enter passwords accessibly, letting them reveal what they typed to reduce errors and choose stronger, more unique passwords before submitting.

**source_ref**: password-input
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('password-input#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0207 | system_requirement | approved | Use whenever a password is created or entered |
| SR-0208 | system_requirement | approved | Do not use for non-password information |
| SR-0209 | system_requirement | approved | Let users show their entry as plain text |
| SR-0210 | system_requirement | approved | Do not reveal which credential was wrong |
| SR-0211 | system_requirement | approved | Hide passwords by default |
| SR-0212 | system_requirement | approved | Use distinct labels and toggles for multiple inputs |
| SR-0213 | system_requirement | approved | Avoid a confirm password field |
| SR-0214 | system_requirement | approved | Set input type to password on submit |
| SR-0215 | system_requirement | approved | Use the autocomplete attribute |
| SR-0216 | system_requirement | approved | Always allow copy and paste |
| SR-0217 | system_requirement | approved | Support all characters and avoid restricting input |
| SR-0218 | system_requirement | approved | Keep any restrictions identical and consistent |
| SR-0219 | system_requirement | approved | Do not use maxlength to restrict length |
| SR-0220 | system_requirement | approved | Disable spellcheck and autocapitalise |
| SR-0221 | system_requirement | approved | Native show/hide tools can duplicate or mismatch |
| SR-0222 | system_requirement | approved | Research decided against a second field |
<!-- tl:end -->

## Phase banner

<!-- tl:item UR-0022 -->
**UR-0022 — Phase banner** — `user_requirement`, status `approved`

> The phase banner shows users a service is still being worked on, and a service.gov.uk service uses it to display its alpha or beta status until it passes a live assessment.

*Rationale:* Signals to users that a service is still being worked on in alpha or beta and invites feedback, as required for service.gov.uk domains until they pass a live assessment.

**source_ref**: phase-banner
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('phase-banner#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0223 | system_requirement | approved | Required on service.gov.uk until live assessment passed |
| SR-0224 | system_requirement | approved | Use the alpha or beta banner to match the phase |
| SR-0225 | system_requirement | approved | Show inside the header after navigation or GOV.UK header |
| SR-0226 | system_requirement | approved | Show on all pages as a service-level message |
| SR-0227 | system_requirement | approved | Include a feedback link |
| SR-0228 | system_requirement | approved | Let users return to their place after feedback |
<!-- tl:end -->

## Radios

<!-- tl:item UR-0023 -->
**UR-0023 — Radios** — `user_requirement`, status `approved`

> The radios component lets users select a single option from a list, and a service uses it when only one option can be chosen.

*Rationale:* Lets users select exactly one option from a list when the choices are mutually exclusive, making the single-answer constraint clear and preventing the confusion of allowing multiple selections.

**source_ref**: radios
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('radios#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0229 | system_requirement | approved | Use when only one option can be selected |
| SR-0230 | system_requirement | approved | Do not use when multiple selections are possible |
| SR-0231 | system_requirement | approved | Position radios to the left of their labels |
| SR-0232 | system_requirement | approved | Add a hint that only one option can be chosen |
| SR-0233 | system_requirement | approved | Do not pre-select an option |
| SR-0234 | system_requirement | approved | Include a 'None of the above' option when valid |
| SR-0235 | system_requirement | approved | Order options alphabetically by default |
| SR-0236 | system_requirement | approved | Group radios in a fieldset with a describing legend |
| SR-0237 | system_requirement | approved | Set legend as page heading when asking one question |
| SR-0238 | system_requirement | approved | Do not set legend as heading with multiple questions |
| SR-0239 | system_requirement | approved | Only use inline radios for two short options |
| SR-0240 | system_requirement | approved | Keep item hints to one short sentence with no links |
| SR-0241 | system_requirement | approved | Separate a distinct option with a text divider |
| SR-0242 | system_requirement | approved | Keep conditionally revealed questions simple |
| SR-0243 | system_requirement | approved | Restrict conditional reveal to questions only |
| SR-0244 | system_requirement | approved | Conditional reveal has a known notification gap |
| SR-0245 | system_requirement | approved | Use smaller radios only when less prominence helps |
| SR-0246 | system_requirement | approved | Show an error when no radio or revealed question is answered |
| SR-0247 | system_requirement | approved | Word errors according to the option pattern |
| SR-0248 | system_requirement | approved | Research found simple conditional reveals workable |
<!-- tl:end -->

## Select

<!-- tl:item UR-0024 -->
**UR-0024 — Select** — `user_requirement`, status `approved`

> The select component helps users choose a single item from a long list, used only as a last resort in public-facing services because some users find selects hard to use.

*Rationale:* Offers a last-resort way to pick one option from a long list in public services, but should be avoided because research shows many users struggle to open, scroll, and choose within selects, so ask narrowing questions or use radios instead.

**source_ref**: select
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('select#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0249 | system_requirement | approved | Use only as a last resort |
| SR-0250 | system_requirement | approved | Reduce options before using select |
| SR-0251 | system_requirement | approved | Pre-select only for settings |
| SR-0252 | system_requirement | approved | Do not pre-select for questions |
| SR-0253 | system_requirement | approved | Keep hint text short |
| SR-0254 | system_requirement | approved | No links in hint text |
| SR-0255 | system_requirement | approved | Show error when no option selected |
| SR-0256 | system_requirement | approved | Avoid multiple selection |
| SR-0257 | system_requirement | approved | Known usability struggles |
<!-- tl:end -->

## Service navigation

<!-- tl:item UR-0025 -->
**UR-0025 — Service navigation** — `user_requirement`, status `approved`

> Service navigation helps users understand they are using your service and lets them navigate around it, showing the service name and optional navigation links.

*Rationale:* Reassures users that they are in the right place within a specific service and lets them move between its parts, giving a consistent experience that shows GOV.UK functions as one coherent website.

**source_ref**: service-navigation
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('service-navigation#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0258 | system_requirement | approved | Use to identify the service |
| SR-0259 | system_requirement | approved | Pair with the GOV.UK header |
| SR-0260 | system_requirement | approved | Show the service name |
| SR-0261 | system_requirement | approved | Show navigation links |
| SR-0262 | system_requirement | approved | Use slots for custom elements |
| SR-0263 | system_requirement | approved | Keep aria-label accurate |
| SR-0264 | system_requirement | approved | Retest slots on each update |
| SR-0265 | system_requirement | approved | Use refreshed GOV.UK branding |
<!-- tl:end -->

## Skip link

<!-- tl:item UR-0026 -->
**UR-0026 — Skip link** — `user_requirement`, status `approved`

> The skip link component helps keyboard-only users skip the top-level navigation and jump straight to the main content on a page.

*Rationale:* Lets keyboard-only users bypass repetitive top-level navigation links and jump straight to a page's main content, removing the burden of tabbing through the header on every page.

**source_ref**: skip-link
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('skip-link#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0266 | system_requirement | approved | Include on every GOV.UK page |
| SR-0267 | system_requirement | approved | Place after the opening body tag |
| SR-0268 | system_requirement | approved | Ignore the landmark warning |
| SR-0269 | system_requirement | approved | Let users bypass navigation |
| SR-0270 | system_requirement | approved | Hidden until keyboard activation |
<!-- tl:end -->

## Summary list

<!-- tl:item UR-0027 -->
**UR-0027 — Summary list** — `user_requirement`, status `approved`

> A summary list summarises information as a list of key facts, such as a user's responses at the end of a form, with an optional summary card variant for grouping multiple lists.

*Rationale:* Presents information as key-and-value facts, such as metadata or a user's form answers at the end of a journey, so people can review and correct their responses before submitting.

**source_ref**: summary-list
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('summary-list#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0271 | system_requirement | approved | Use for a list of key facts |
| SR-0272 | system_requirement | approved | Only for key-and-value information |
| SR-0273 | system_requirement | approved | Do not use for tables or simple lists |
| SR-0274 | system_requirement | approved | Structure each row as key and value |
| SR-0275 | system_requirement | approved | Add structure to multiple lists |
| SR-0276 | system_requirement | approved | Add visually hidden text to row actions |
| SR-0277 | system_requirement | approved | Pre-populate when returning to answers |
| SR-0278 | system_requirement | approved | Mark rows without actions |
| SR-0279 | system_requirement | approved | Think carefully before removing borders |
| SR-0280 | system_requirement | approved | Link to complete missing information |
| SR-0281 | system_requirement | approved | Use summary cards for same-type lists |
| SR-0282 | system_requirement | approved | Do not use cards for small amounts |
| SR-0283 | system_requirement | approved | Give each card a unique title |
| SR-0284 | system_requirement | approved | Write clear card action link text |
| SR-0285 | system_requirement | approved | Limit card actions |
| SR-0286 | system_requirement | approved | Confirm serious card actions |
<!-- tl:end -->

## Table

<!-- tl:item UR-0028 -->
**UR-0028 — Table** — `user_requirement`, status `approved`

> The table component presents information in rows and columns to make it easier for users to compare and scan.

*Rationale:* Makes information easier to compare and scan by arranging related data into rows and columns, so users can read across shared attributes rather than hunting through prose.

**source_ref**: table
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('table#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0287 | system_requirement | approved | Use to compare information |
| SR-0288 | system_requirement | approved | Never use for layout |
| SR-0289 | system_requirement | approved | Describe the table with a caption |
| SR-0290 | system_requirement | approved | Use headers with scope |
| SR-0291 | system_requirement | approved | Right-align columns of numbers |
| SR-0292 | system_requirement | approved | Reduce data in tables |
| SR-0293 | system_requirement | approved | Only shrink text for lots of data |
<!-- tl:end -->

## Tabs

<!-- tl:item UR-0029 -->
**UR-0029 — Tabs** — `user_requirement`, status `approved`

> The tabs component lets users quickly switch between related sections of content, displaying one clearly labelled section at a time.

*Rationale:* Lets regular or expert users quickly switch between clearly labelled related sections without viewing all at once, but is avoided when users must read in order or compare content, since tabs hide information many people miss.

**source_ref**: tabs
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('tabs#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0294 | system_requirement | approved | Use for clearly separable sections |
| SR-0295 | system_requirement | approved | Do not use for heavy or navigational content |
| SR-0296 | system_requirement | approved | Do not use for ordered or comparison content |
| SR-0297 | system_requirement | approved | Test content without tabs first |
| SR-0298 | system_requirement | approved | Choose tabs versus accordion or details |
| SR-0299 | system_requirement | approved | Provide a no-JavaScript fallback |
| SR-0300 | system_requirement | approved | Use clear tab labels |
| SR-0301 | system_requirement | approved | Order tabs by user need |
| SR-0302 | system_requirement | approved | Do not disable tabs |
| SR-0303 | system_requirement | approved | Avoid tabs wrapping onto multiple lines |
| SR-0304 | system_requirement | approved | Add a heading to each tab's content |
| SR-0305 | system_requirement | approved | Not yet tested with users |
<!-- tl:end -->

## Tag

<!-- tl:item UR-0030 -->
**UR-0030 — Tag** — `user_requirement`, status `approved`

> As a service, I use the Tag component to show users the status of something, such as an item on a task list or a phase banner.

*Rationale:* Lets users see at a glance the current status of something that can hold more than one state, such as whether a task-list item is completed or a user is active, so they know where things stand without reading further.

**source_ref**: tag
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('tag#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0306 | system_requirement | approved | Use when a thing can have more than one status |
| SR-0307 | system_requirement | approved | Use tags only to indicate status |
| SR-0308 | system_requirement | approved | Do not make tags interactive |
| SR-0309 | system_requirement | approved | Name tags with adjectives |
| SR-0310 | system_requirement | approved | Start with the fewest statuses |
| SR-0311 | system_requirement | approved | A single status can be enough |
| SR-0312 | system_requirement | approved | Do not convey information by colour alone |
| SR-0313 | system_requirement | approved | Keep tag colour consistent across uses |
| SR-0314 | system_requirement | approved | Use colour to distinguish or emphasise |
| SR-0315 | system_requirement | approved | Tags no longer use uppercase text |
| SR-0316 | system_requirement | approved | Tag styling changed to avoid looking like buttons |
<!-- tl:end -->

## Task list

<!-- tl:item UR-0031 -->
**UR-0031 — Task list** — `user_requirement`, status `approved`

> As a service, I use the task list component to display all the tasks a user needs to do and let them see which are done and which remain.

*Rationale:* Gives users control over long, complex services they cannot or do not want to finish in one sitting, letting them choose their own order and clearly see which tasks are done and which remain.

**source_ref**: task-list
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('task-list#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0317 | system_requirement | approved | Use to give control over long, complex services |
| SR-0318 | system_requirement | approved | Only use with supporting evidence |
| SR-0319 | system_requirement | approved | Try to simplify the service first |
| SR-0320 | system_requirement | approved | Do not use for strictly ordered services |
| SR-0321 | system_requirement | approved | Do not use to show users their answers |
| SR-0322 | system_requirement | approved | Let users complete tasks in any order |
| SR-0323 | system_requirement | approved | Status indicates whether a task can be started |
| SR-0324 | system_requirement | approved | Only allow moving on when all tasks are completed |
| SR-0325 | system_requirement | approved | Each task has a name and a status |
| SR-0326 | system_requirement | approved | Link the whole task row |
| SR-0327 | system_requirement | approved | Write clear, short task names in sentence case |
| SR-0328 | system_requirement | approved | Split tasks that are hard to name concisely |
| SR-0329 | system_requirement | approved | Keep hint text to one short sentence |
| SR-0330 | system_requirement | approved | Do not put links in hint text |
| SR-0331 | system_requirement | approved | Group tasks under clear headings |
| SR-0332 | system_requirement | approved | Statuses use colour and a short descriptor |
| SR-0333 | system_requirement | approved | Statuses redesigned and rows linked after feedback |
| SR-0334 | system_requirement | approved | Statuses moved to sentence case for readability |
| SR-0335 | system_requirement | approved | Component still needs user testing |
<!-- tl:end -->

## Textarea

<!-- tl:item UR-0032 -->
**UR-0032 — Textarea** — `user_requirement`, status `approved`

> As a service, I use the textarea component to let users enter an amount of text that is longer than a single line.

*Rationale:* Lets users provide answers longer than a single line, giving space for detailed free-text information that would not fit in a standard single-line input field.

**source_ref**: textarea
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('textarea#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0336 | system_requirement | approved | Use for text longer than a single line |
| SR-0337 | system_requirement | approved | Consider breaking up open-ended questions |
| SR-0338 | system_requirement | approved | Do not use for single-line answers |
| SR-0339 | system_requirement | approved | Always label the textarea |
| SR-0340 | system_requirement | approved | Align labels above and use sentence case |
| SR-0341 | system_requirement | approved | Size the textarea to expected input |
| SR-0342 | system_requirement | approved | Do not disable copy and paste |
| SR-0343 | system_requirement | approved | Label is not the page heading with multiple questions |
| SR-0344 | system_requirement | approved | Limit character count with the right component |
| SR-0345 | system_requirement | approved | Use specific error messages per state |
<!-- tl:end -->

## Text input

<!-- tl:item UR-0033 -->
**UR-0033 — Text input** — `user_requirement`, status `approved`

> As a service, I use the text input component to let users enter text no longer than a single line, such as their name or phone number.

*Rationale:* Lets users enter short, single-line information such as a name or phone number, providing an appropriately sized field so they understand what is expected without spanning multiple lines.

**source_ref**: text-input
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('text-input#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0346 | system_requirement | approved | Use for single-line text |
| SR-0347 | system_requirement | approved | Do not use for multi-line answers |
| SR-0348 | system_requirement | approved | All inputs must have labels |
| SR-0349 | system_requirement | approved | Align labels above and use sentence case |
| SR-0350 | system_requirement | approved | Avoid placeholder text |
| SR-0351 | system_requirement | approved | Use label as heading for one question per page |
| SR-0352 | system_requirement | approved | Label is not the page heading with multiple questions |
| SR-0353 | system_requirement | approved | Size inputs to the expected content |
| SR-0354 | system_requirement | approved | Use hint text for widely relevant help |
| SR-0355 | system_requirement | approved | Do not put links in hint text |
| SR-0356 | system_requirement | approved | Do not use hint text for long explanations |
| SR-0357 | system_requirement | approved | Set inputmode numeric for whole numbers |
| SR-0358 | system_requirement | approved | Set inputmode decimal for decimals |
| SR-0359 | system_requirement | approved | Avoid input type number |
| SR-0360 | system_requirement | approved | Visually separate characters in codes |
| SR-0361 | system_requirement | approved | Do not rely on prefixes or suffixes alone |
| SR-0362 | system_requirement | approved | Position prefixes and suffixes outside the input |
| SR-0363 | system_requirement | approved | Use the autocomplete attribute |
| SR-0364 | system_requirement | approved | Do not disable copy and paste |
| SR-0365 | system_requirement | approved | Avoid restricting input length |
| SR-0366 | system_requirement | approved | Disable spellcheck where inappropriate |
| SR-0367 | system_requirement | approved | Use specific error messages per state |
| SR-0368 | system_requirement | approved | Support all characters the user needs |
| SR-0369 | system_requirement | approved | Problems found with input type number |
| SR-0370 | system_requirement | approved | Some users clicked on prefixes |
<!-- tl:end -->

## Warning text

<!-- tl:item UR-0034 -->
**UR-0034 — Warning text** — `user_requirement`, status `approved`

> As a service, I use the warning text component to warn users about something important, such as legal consequences of an action or inaction.

*Rationale:* Draws users' attention to something genuinely important, such as the legal consequences of an action or inaction, so they do not overlook a critical warning before deciding what to do.

**source_ref**: warning-text
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('warning-text#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0371 | system_requirement | approved | Use to warn about something important |
| SR-0372 | system_requirement | approved | Adapt the hidden text to context |
<!-- tl:end -->

## Generic header

<!-- tl:item UR-0035 -->
**UR-0035 — Generic header** — `user_requirement`, status `approved`

> As a service, I use the Generic header component to tell users they are using a government service that is not part of the GOV.UK website.

*Rationale:* Signals to users that a public-facing government service sits outside the GOV.UK website, maintaining trust and consistency across journeys while ensuring non-GOV.UK services do not misuse GOV.UK branding.

**source_ref**: generic-header
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('generic-header#') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0373 | system_requirement | approved | Use for public services not on GOV.UK |
| SR-0374 | system_requirement | approved | Bring consistency across cross-government journeys |
| SR-0375 | system_requirement | approved | Do not use GOV.UK branding in the header |
| SR-0376 | system_requirement | approved | Do not use on gov.uk domains |
| SR-0377 | system_requirement | approved | Replace the default header in the page template |
| SR-0378 | system_requirement | approved | Display your own brand logo, link, and font |
| SR-0379 | system_requirement | approved | Make the brand logo accessible and optimised |
| SR-0380 | system_requirement | approved | Customise the homepage link |
| SR-0381 | system_requirement | approved | Do not show navigation links in the header |
<!-- tl:end -->

