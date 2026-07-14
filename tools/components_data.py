"""Distilled GOV.UK Design System component guidance — the source of truth for the graph.

Each record is one component: its `user_requirement` (slug, title, ur_text) and the
clauses distilled from its guidance page into `system_requirement`s. A clause is a
*testable* statement re-expressing prescriptive guidance — usage rules, accessibility
acceptance criteria, do-and-don'ts, and research findings that encode an expectation.
Pure rationale prose ("why this matters") is not modelled.

Clause fields:
  anchor  kebab id, unique within the component -> attrs.source_ref = "<slug>#<anchor>"
  kind    "usage" | "accessibility" | "research"
  title   concise label
  text    the rule as a testable statement
  wcag    optional WCAG 2.2 success criterion the rule cites (e.g. "1.4.3")

Authoritative source: https://design-system.service.gov.uk/components/ (Crown copyright,
Open Government Licence v3.0). Distilled faithfully; not copied verbatim.
"""

COMPONENTS = [
    {
        "slug": "button",
        "title": "Button",
        "ur_text": "The service uses the GOV.UK Button component to let users carry "
                   "out an action, following its guidance on button text, variants, "
                   "grouping, contrast and double-click prevention.",
        "clauses": [
            {
                "anchor": "carry-out-an-action",
                "kind": "usage",
                "title": "Buttons carry out an action",
                "text": "Use the button component to help users carry out an action, "
                        "such as starting an application or saving their information.",
            },
            {
                "anchor": "sentence-case-text",
                "kind": "usage",
                "title": "Button text is sentence case and describes the action",
                "text": "Write button text in sentence case, describing the action it "
                        "performs (for example 'Start now', 'Save and continue').",
            },
            {
                "anchor": "align-left",
                "kind": "usage",
                "title": "Primary action aligns to the left of the form",
                "text": "Align the primary action button to the left edge of the form.",
            },
            {
                "anchor": "one-default-per-page",
                "kind": "usage",
                "title": "Avoid multiple default buttons on a page",
                "text": "Use a default button for the main call to action, and avoid "
                        "more than one default button on a single page so users can "
                        "tell what to do next.",
            },
            {
                "anchor": "start-button-is-a-link",
                "kind": "usage",
                "title": "Start buttons are links, not submit buttons",
                "text": "Use a start button for the main call to action on a service's "
                        "start page; because it does not submit form data, implement it "
                        "as a link tag rather than a button tag.",
            },
            {
                "anchor": "secondary-for-secondary-actions",
                "kind": "usage",
                "title": "Secondary buttons for secondary actions only",
                "text": "Use secondary buttons only for secondary calls to action, and "
                        "simplify the page rather than adding many secondary buttons.",
            },
            {
                "anchor": "warning-sparingly",
                "kind": "usage",
                "title": "Warning buttons only for serious destructive actions",
                "text": "Use warning buttons only for actions with serious destructive "
                        "consequences that cannot be easily undone, and use them very "
                        "sparingly.",
            },
            {
                "anchor": "warning-confirmation-step",
                "kind": "usage",
                "title": "Precede a warning action with a confirmation step",
                "text": "When an action needs a warning button, include an additional "
                        "step that asks the user to confirm, using another button style "
                        "for the initial action and the warning button for the final "
                        "confirmation.",
            },
            {
                "anchor": "warning-not-colour-alone",
                "kind": "accessibility",
                "title": "Do not rely on warning button colour alone",
                "text": "Do not rely on the red colour of a warning button to convey the "
                        "seriousness of the action; the surrounding context and the "
                        "button text must make clear what will happen, because not all "
                        "users can see or interpret the colour.",
            },
            {
                "anchor": "inverse-contrast",
                "kind": "accessibility",
                "title": "Buttons on dark backgrounds meet contrast minimum",
                "text": "When using the inverse button on a dark background, ensure the "
                        "button and its background colour have a contrast ratio of at "
                        "least 4.5:1.",
                "wcag": "1.4.3",
            },
            {
                "anchor": "avoid-disabled",
                "kind": "accessibility",
                "title": "Avoid disabled buttons",
                "text": "Avoid disabled buttons because they have poor contrast and can "
                        "confuse users; use one only where research shows it makes the "
                        "interface easier to understand.",
            },
            {
                "anchor": "group-related-buttons",
                "kind": "usage",
                "title": "Group buttons placed together",
                "text": "Use a button group when two or more buttons are placed "
                        "together so they and any adjacent links align.",
            },
            {
                "anchor": "prevent-double-click",
                "kind": "usage",
                "title": "Guard against accidental double submission",
                "text": "Where research shows users send information twice, set "
                        "data-prevent-double-click to true to ignore the second click "
                        "for users with JavaScript, and also protect against duplicate "
                        "submission server-side.",
            },
            {
                "anchor": "green-start-buttons",
                "kind": "research",
                "title": "Green start buttons improve click-through",
                "text": "Testing on GOV.UK showed that using green as the colour of "
                        "start buttons improved click-through rates.",
            },
        ],
    },
    {
        "slug": "error-summary",
        "title": "Error summary",
        "ur_text": "The service uses the GOV.UK Error summary component at the top of a "
                   "page to summarise validation errors, moving focus to it, linking "
                   "each error to its answer and mirroring the inline error messages.",
        "clauses": [
            {
                "anchor": "top-of-page",
                "kind": "usage",
                "title": "Show the error summary at the top of the page",
                "text": "Show the error summary at the top of the page to summarise any "
                        "errors the user has made.",
            },
            {
                "anchor": "summary-and-inline-message",
                "kind": "usage",
                "title": "Show a summary and an inline message per error",
                "text": "When a user makes an error, show both an error summary and an "
                        "error message next to each answer that contains an error.",
            },
            {
                "anchor": "always-when-error",
                "kind": "usage",
                "title": "Always show the summary when there is an error",
                "text": "Always show an error summary when there is a validation error, "
                        "even if there is only one error.",
            },
            {
                "anchor": "move-focus",
                "kind": "accessibility",
                "title": "Move keyboard focus to the error summary",
                "text": "Move keyboard focus to the error summary when it appears so "
                        "assistive technology users are taken to it (the govuk-frontend "
                        "JavaScript does this).",
            },
            {
                "anchor": "there-is-a-problem-heading",
                "kind": "usage",
                "title": "Use the heading 'There is a problem'",
                "text": "Include the heading 'There is a problem' in the error summary.",
            },
            {
                "anchor": "wording-matches-inline",
                "kind": "usage",
                "title": "Summary wording matches the inline messages",
                "text": "Word the error messages in the summary the same as the messages "
                        "shown next to the inputs with errors.",
            },
            {
                "anchor": "error-prefix-title",
                "kind": "accessibility",
                "title": "Prefix the page title with 'Error:'",
                "text": "Follow the validation pattern by adding 'Error:' to the start "
                        "of the page title so screen readers announce the error state "
                        "as soon as possible.",
            },
            {
                "anchor": "link-single-field",
                "kind": "accessibility",
                "title": "Link single-field errors to the field",
                "text": "For a question answered in a single field (file upload, select, "
                        "textarea, text input or character count), link the summary "
                        "error to that field.",
            },
            {
                "anchor": "link-multiple-fields",
                "kind": "accessibility",
                "title": "Link multi-field errors to the first errored field",
                "text": "For a question answered across multiple fields such as a date "
                        "input, link the summary error to the first field that contains "
                        "an error, or to the first field if the errored field is "
                        "unknown.",
            },
            {
                "anchor": "link-radios-checkboxes",
                "kind": "accessibility",
                "title": "Link option errors to the first option",
                "text": "For a question answered by selecting radios or checkboxes, link "
                        "the summary error to the first radio or checkbox.",
            },
            {
                "anchor": "placement",
                "kind": "usage",
                "title": "Place the summary above the h1",
                "text": "Put the error summary at the top of the main container; if the "
                        "page has breadcrumbs or a back link, place it below those but "
                        "above the page heading.",
            },
        ],
    },
    {
        "slug": "date-input",
        "title": "Date input",
        "ur_text": "The service uses the GOV.UK Date input component to help users enter "
                   "a memorable date across day, month and year fields, grouped in a "
                   "fieldset, with accessible labelling, autocomplete and specific "
                   "error messages.",
        "clauses": [
            {
                "anchor": "memorable-date",
                "kind": "usage",
                "title": "Use for dates users know or can look up",
                "text": "Use the date input component when asking for a date the user "
                        "will already know, or can look up without using a calendar.",
            },
            {
                "anchor": "not-for-unknown-dates",
                "kind": "usage",
                "title": "Do not use for dates users will not know",
                "text": "Do not use the date input component if users are unlikely to "
                        "know the exact date being asked about.",
            },
            {
                "anchor": "fieldset-legend",
                "kind": "accessibility",
                "title": "Group the three fields in a fieldset with a legend",
                "text": "Group the day, month and year fields in a fieldset with a "
                        "legend that describes them, usually phrased as a question.",
            },
            {
                "anchor": "legend-as-heading-single",
                "kind": "accessibility",
                "title": "Set the legend as the page heading when one question per page",
                "text": "When asking one question per page, set the legend as the page "
                        "heading so screen reader users hear it only once.",
            },
            {
                "anchor": "legend-not-heading-multiple",
                "kind": "accessibility",
                "title": "Do not set the legend as the heading with multiple questions",
                "text": "When asking more than one question on the page, do not set the "
                        "legend as the page heading.",
            },
            {
                "anchor": "valid-example-dates",
                "kind": "usage",
                "title": "Hint text example dates are valid for the question",
                "text": "Make sure any example dates used in hint text are valid for the "
                        "question being asked.",
            },
            {
                "anchor": "accept-month-names",
                "kind": "usage",
                "title": "Accept month names in full or abbreviated form",
                "text": "Accept month names written in full or abbreviated form (for "
                        "example 'january' or 'jan') as some users enter months this "
                        "way.",
            },
            {
                "anchor": "no-auto-tab",
                "kind": "accessibility",
                "title": "Do not auto-tab between fields",
                "text": "Never automatically move focus between the day, month and year "
                        "fields, because it is confusing and can clash with normal "
                        "keyboard controls.",
            },
            {
                "anchor": "autocomplete-dob",
                "kind": "accessibility",
                "title": "Set autocomplete attributes for a date of birth",
                "text": "When asking for a date of birth, set the autocomplete attribute "
                        "on the three fields to bday-day, bday-month and bday-year so "
                        "browsers can autofill a previously entered value.",
                "wcag": "1.3.5",
            },
            {
                "anchor": "error-highlight-scope",
                "kind": "usage",
                "title": "Highlight only the fields in error",
                "text": "When the whole date is in error, style all three fields; when "
                        "only one field is in error, style just that field and state in "
                        "the message which field has the error.",
            },
            {
                "anchor": "error-priority",
                "kind": "usage",
                "title": "Show the highest-priority error first",
                "text": "When there is more than one error, show the highest-priority "
                        "message, in order: missing or incomplete information; then "
                        "information that cannot be correct; then information that fails "
                        "validation for another reason.",
            },
            {
                "anchor": "error-specific-wording",
                "kind": "usage",
                "title": "Use specific wording for each error state",
                "text": "Give specific error messages for specific error states — for "
                        "example 'Enter your date of birth' when nothing is entered, "
                        "'Date of birth must include a month' when incomplete, and "
                        "'Date of birth must be a real date' when the date cannot be "
                        "correct.",
            },
            {
                "anchor": "accept-month-names-research",
                "kind": "research",
                "title": "Accepting month names reduced errors",
                "text": "On the Apply for teacher training service, hundreds of users "
                        "entered months as full or abbreviated names and got errors; "
                        "accepting month names dropped the error rate dramatically and "
                        "may help users with dyscalculia.",
            },
        ],
    },
    {
        "slug": "accordion",
        "title": "Accordion",
        "ur_text": "The service uses the GOV.UK Accordion component to let users show "
                   "and hide sections of related content, only where research shows "
                   "hiding content helps, with clear headings and keyboard support.",
        "clauses": [
            {
                "anchor": "only-with-evidence",
                "kind": "usage",
                "title": "Use only where research shows it helps",
                "text": "Use an accordion only where there is evidence it helps users "
                        "to see an overview of related sections and choose which to "
                        "reveal; test with users before deciding to use one.",
            },
            {
                "anchor": "not-for-essential-content",
                "kind": "usage",
                "title": "Do not hide content all users need",
                "text": "Do not use an accordion for content that all users need to "
                        "see, because accordions hide content and not all users notice "
                        "or understand them.",
            },
            {
                "anchor": "test-without-first",
                "kind": "usage",
                "title": "Test the content without an accordion first",
                "text": "Test the content without an accordion first; well-written and "
                        "structured content can remove the need for one.",
            },
            {
                "anchor": "not-for-questions",
                "kind": "usage",
                "title": "Do not use to split up questions",
                "text": "Do not use accordions to split up a series of questions; use "
                        "separate pages instead.",
            },
            {
                "anchor": "no-nesting",
                "kind": "usage",
                "title": "Do not nest accordions or hide-reveal components",
                "text": "Do not put accordions within accordions, or nest the accordion, "
                        "tabs and details components within one another.",
            },
            {
                "anchor": "unique-id",
                "kind": "usage",
                "title": "Give the accordion a unique id",
                "text": "When using HTML, give the govuk-accordion div a unique id "
                        "across the service's domain so the expanded state persists.",
            },
            {
                "anchor": "works-without-js",
                "kind": "accessibility",
                "title": "Show all content when JavaScript is unavailable",
                "text": "When JavaScript is not available, show all the content with the "
                        "section labels as headings.",
            },
            {
                "anchor": "clear-button-text",
                "kind": "accessibility",
                "title": "Write clear, short heading button text",
                "text": "Write each section heading button in sentence case, describing "
                        "the content it reveals and keeping it short, because long "
                        "button text is hard for screen reader users to navigate.",
            },
            {
                "anchor": "short-summary-line",
                "kind": "usage",
                "title": "Keep any summary line as short as possible",
                "text": "Add a summary line only if it is needed and keep it as short as "
                        "possible, as it lengthens the button text.",
            },
            {
                "anchor": "heading-level-fits",
                "kind": "accessibility",
                "title": "Fit section heading levels into the page",
                "text": "Section headings render as h2; change their heading level where "
                        "needed so they fit the other headings on the page.",
            },
            {
                "anchor": "no-disabled-sections",
                "kind": "usage",
                "title": "Do not disable sections",
                "text": "Do not disable sections; remove an empty section, or explain "
                        "why there is no content when the section is opened.",
            },
            {
                "anchor": "keyboard-accessible-research",
                "kind": "research",
                "title": "Reworked in 2021 for accessibility",
                "text": "The component was updated in December 2021 so it is fully "
                        "keyboard operable and its buttons and section labels are not "
                        "mistaken for links.",
            },
        ],
    },
    {
        "slug": "back-link",
        "title": "Back link",
        "ur_text": "The service uses the GOV.UK Back link component to help users return "
                   "to the previous page in a multi-page transaction, placed above the "
                   "main content with clear text and sufficient contrast.",
        "clauses": [
            {
                "anchor": "multi-page-transaction",
                "kind": "usage",
                "title": "Use to go back in a multi-page transaction",
                "text": "Use the back link to help users go back to the previous page in "
                        "a multi-page transaction.",
            },
            {
                "anchor": "always-on-question-pages",
                "kind": "usage",
                "title": "Always include on question pages",
                "text": "Always include the back link on question pages in the service.",
            },
            {
                "anchor": "not-with-breadcrumbs",
                "kind": "usage",
                "title": "Do not combine with breadcrumbs",
                "text": "Never use the back link together with the breadcrumbs "
                        "component.",
            },
            {
                "anchor": "place-above-main",
                "kind": "accessibility",
                "title": "Place the back link before the main element",
                "text": "Place the back link at the top of the page, before the main "
                        "element, so the 'Skip to main content' link skips it along "
                        "with other navigation links.",
            },
            {
                "anchor": "returns-to-previous-state",
                "kind": "usage",
                "title": "Return users to the page as they last saw it",
                "text": "Make sure the back link takes users to the previous page in the "
                        "state they last saw it.",
            },
            {
                "anchor": "works-without-js",
                "kind": "usage",
                "title": "Work without JavaScript, or hide it",
                "text": "Where possible ensure the back link works without JavaScript; "
                        "if that is not possible, hide it when JavaScript is "
                        "unavailable.",
            },
            {
                "anchor": "descriptive-text-when-complex",
                "kind": "usage",
                "title": "Use descriptive text for complex journeys",
                "text": "Use the default 'Back' text for simple journeys, but use "
                        "descriptive text such as 'Go back to [page]' where it would "
                        "otherwise be unclear what the user is going back to.",
            },
            {
                "anchor": "inverse-contrast",
                "kind": "accessibility",
                "title": "Back links on dark backgrounds meet contrast minimum",
                "text": "When using the inverse back link on a dark background, ensure "
                        "the background has a contrast ratio of at least 4.5:1 with "
                        "white.",
                "wcag": "1.4.3",
            },
        ],
    },
    {
        "slug": "breadcrumbs",
        "title": "Breadcrumbs",
        "ur_text": "The service uses the GOV.UK Breadcrumbs component to help users "
                   "understand where they are within a site's hierarchy and move "
                   "between levels, placed above the main content.",
        "clauses": [
            {
                "anchor": "for-hierarchy",
                "kind": "usage",
                "title": "Use to move between levels of a hierarchy",
                "text": "Use breadcrumbs to help users understand where they are and "
                        "move between the multiple levels of a website.",
            },
            {
                "anchor": "not-for-flat-or-linear",
                "kind": "usage",
                "title": "Do not use for flat sites or linear journeys",
                "text": "Do not use breadcrumbs on websites with a flat structure, or to "
                        "show progress through a linear journey or transaction.",
            },
            {
                "anchor": "place-above-main",
                "kind": "accessibility",
                "title": "Place breadcrumbs before the main element",
                "text": "Place breadcrumbs at the top of the page, before the main "
                        "element, so the 'Skip to main content' link skips them along "
                        "with other navigation links.",
            },
            {
                "anchor": "home-to-parent",
                "kind": "usage",
                "title": "Run from home to the current page's parent",
                "text": "Start breadcrumbs with the home page and end with the parent "
                        "section of the current page.",
            },
            {
                "anchor": "collapse-on-mobile",
                "kind": "usage",
                "title": "Optionally collapse long breadcrumbs on mobile",
                "text": "For long breadcrumbs, configure the component to show only the "
                        "first and last items on mobile devices.",
            },
            {
                "anchor": "inverse-contrast",
                "kind": "accessibility",
                "title": "Breadcrumbs on dark backgrounds meet contrast minimum",
                "text": "When using the inverse breadcrumbs on a dark background, ensure "
                        "the background has a contrast ratio of at least 4.5:1 with "
                        "white.",
                "wcag": "1.4.3",
            },
        ],
    },
    {
        "slug": "character-count",
        "title": "Character count",
        "ur_text": "The service uses the GOV.UK Character count component to tell users "
                   "how much text they can enter into a textarea with a limit, only "
                   "where limiting is justified, with accessible live feedback.",
        "clauses": [
            {
                "anchor": "test-without-first",
                "kind": "usage",
                "title": "Test the service without a character count first",
                "text": "Test the service without a character count first, and use one "
                        "only where there is a good reason to limit the number of "
                        "characters, such as evidence of over-entry or a legal or "
                        "technical limit.",
            },
            {
                "anchor": "raise-limit-not-count",
                "kind": "usage",
                "title": "Raise a limit users keep hitting",
                "text": "If users keep hitting the backend character limit, increase the "
                        "limit rather than adding a character count.",
            },
            {
                "anchor": "does-not-restrict",
                "kind": "usage",
                "title": "Do not block entry over the limit",
                "text": "Do not stop users entering more than the limit; let them enter "
                        "their full answer and tell them when they have entered too "
                        "many characters so they can edit it down.",
            },
            {
                "anchor": "message-below-textarea",
                "kind": "usage",
                "title": "Show the count message below the textarea",
                "text": "Show the count message below the textarea so it is separate "
                        "from hint text and error messages and remains visible on "
                        "scroll.",
            },
            {
                "anchor": "static-message-without-js",
                "kind": "accessibility",
                "title": "Show a static limit message without JavaScript",
                "text": "When JavaScript is not available, show a static message telling "
                        "users how many characters they can enter in place of the live "
                        "count.",
            },
            {
                "anchor": "label-not-heading-multiple",
                "kind": "accessibility",
                "title": "Do not set the label as the heading with multiple questions",
                "text": "When asking more than one question on the page, do not set the "
                        "textarea label as the page heading.",
            },
            {
                "anchor": "consider-word-count",
                "kind": "usage",
                "title": "Consider a word count for longer answers",
                "text": "Consider showing a word count instead of a character count "
                        "where the question requires a longer answer.",
            },
            {
                "anchor": "generous-limit",
                "kind": "usage",
                "title": "Set the limit higher than most users need",
                "text": "Set the limit higher than most users will need, informed by "
                        "user research and data analysis; use the threshold option to "
                        "reveal the count only near a limit users are unlikely to "
                        "reach.",
            },
            {
                "anchor": "error-above-and-count-below",
                "kind": "usage",
                "title": "Show an error above the field and the count below",
                "text": "When a user tries to send too many characters, show an error "
                        "message above the field as well as the count message below it, "
                        "with specific wording for each error state (for example 'Enter "
                        "a summary', 'Summary must be 400 characters or less').",
            },
            {
                "anchor": "tested-with-disabled-research",
                "kind": "research",
                "title": "Tested with disabled users; announcement fixed",
                "text": "The component was developed and tested in 2017 with 17 users "
                        "including people with disabilities, and updated in 2022 to stop "
                        "some screen readers announcing the count twice.",
            },
        ],
    },
]
