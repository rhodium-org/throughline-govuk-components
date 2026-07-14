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
    {
        "slug": "checkboxes",
        "title": "Checkboxes",
        "ur_text": "The service uses the GOV.UK Checkboxes component to let users select "
                   "one or more options, grouped in a fieldset with an accessible "
                   "legend, ordered and labelled to guidance.",
        "clauses": [
            {
                "anchor": "for-multiple-selection",
                "kind": "usage",
                "title": "Use to select multiple options or toggle one",
                "text": "Use checkboxes to let users select multiple options from a "
                        "list, or toggle a single option on or off.",
            },
            {
                "anchor": "not-for-single-choice",
                "kind": "usage",
                "title": "Use radios for a single choice",
                "text": "Do not use checkboxes if users can only choose one option from "
                        "a selection; use the radios component instead.",
            },
            {
                "anchor": "boxes-left-of-labels",
                "kind": "accessibility",
                "title": "Position checkboxes to the left of labels",
                "text": "Always position checkboxes to the left of their labels so they "
                        "are easier to find, especially for screen magnifier users.",
            },
            {
                "anchor": "hint-select-all",
                "kind": "usage",
                "title": "Explain that multiple options can be selected",
                "text": "Do not assume users know they can select more than one option; "
                        "where needed add a hint such as 'Select all that apply'.",
            },
            {
                "anchor": "no-preselection",
                "kind": "usage",
                "title": "Do not pre-select options",
                "text": "Do not pre-select checkbox options, as users may then miss the "
                        "question or submit the wrong answer.",
            },
            {
                "anchor": "order-alphabetically",
                "kind": "usage",
                "title": "Order options alphabetically by default",
                "text": "Order checkbox options alphabetically by default, or from most "
                        "to least common where that is more helpful.",
            },
            {
                "anchor": "fieldset-legend",
                "kind": "accessibility",
                "title": "Group checkboxes in a fieldset with a legend",
                "text": "Group checkboxes in a fieldset with a legend that describes "
                        "them, usually phrased as a question.",
            },
            {
                "anchor": "legend-heading-single",
                "kind": "accessibility",
                "title": "Set the legend as the heading for one question per page",
                "text": "When asking one question per page, set the legend as the page "
                        "heading so screen reader users hear it only once; when asking "
                        "more than one question, do not.",
            },
            {
                "anchor": "hint-single-sentence",
                "kind": "accessibility",
                "title": "Keep item hints short and link-free",
                "text": "Keep each checkbox item hint to a single short sentence without "
                        "full stops, and do not put links in hint text, because screen "
                        "readers read the whole hint and do not flag links.",
            },
            {
                "anchor": "none-option",
                "kind": "usage",
                "title": "Provide a 'none' option where valid",
                "text": "Where 'none' is a valid answer, provide a 'none' checkbox shown "
                        "last, separated by an 'or' divider, labelled to repeat the key "
                        "part of the question, with exclusive behaviour that unchecks "
                        "the other options.",
            },
            {
                "anchor": "conditional-reveal-simple",
                "kind": "usage",
                "title": "Only conditionally reveal simple questions",
                "text": "Only conditionally reveal questions — never non-question "
                        "content — and keep a revealed question simple, moving anything "
                        "complex to the next page.",
            },
            {
                "anchor": "conditional-reveal-notify",
                "kind": "accessibility",
                "title": "Conditional reveal is not always announced",
                "text": "Users are not always notified when a conditionally revealed "
                        "question is shown or hidden, so keep revealed questions simple; "
                        "this is a known failure of the component.",
                "wcag": "4.1.2",
            },
            {
                "anchor": "error-messages",
                "kind": "usage",
                "title": "Use specific error messages",
                "text": "Follow the error message guidance and use specific wording for "
                        "each error state, for example 'Select your nationality or "
                        "nationalities' when nothing is selected.",
            },
        ],
    },
    {
        "slug": "cookie-banner",
        "title": "Cookie banner",
        "ur_text": "The service uses the GOV.UK Cookie banner component to let users "
                   "accept or reject non-essential cookies, shown until a choice is "
                   "made, with an accessible confirmation and a supporting cookies "
                   "page.",
        "clauses": [
            {
                "anchor": "when-cookies-set",
                "kind": "usage",
                "title": "Use when the service sets cookies",
                "text": "Use a cookie banner if the service sets any cookies; tell users "
                        "about the cookies set and let them accept or reject any that "
                        "are not essential.",
            },
            {
                "anchor": "non-essential-scope",
                "kind": "usage",
                "title": "Treat storage technologies as non-essential cookies",
                "text": "Treat HTML5 local storage, service workers and any other "
                        "technology that stores files on the user's device as "
                        "non-essential cookies requiring consent.",
            },
            {
                "anchor": "show-until-choice",
                "kind": "usage",
                "title": "Show the banner until the user decides",
                "text": "Show the cookie banner on every visit until the user accepts or "
                        "rejects cookies, or saves their preferences on the cookies "
                        "page.",
            },
            {
                "anchor": "confirmation-and-persist",
                "kind": "usage",
                "title": "Confirm the choice and remember it for a year",
                "text": "Once the user accepts or rejects, hide the message, show a "
                        "confirmation with a 'hide' button, and save the preference in a "
                        "cookie for one year; do not show the banner again or set "
                        "non-essential cookies the user did not accept.",
            },
            {
                "anchor": "position-before-skip-link",
                "kind": "accessibility",
                "title": "Position the banner before the skip link",
                "text": "Position the cookie banner after the opening body tag and "
                        "before the 'skip to main content' link.",
            },
            {
                "anchor": "not-sticky",
                "kind": "accessibility",
                "title": "Do not make the banner sticky",
                "text": "Do not fix the cookie banner to the top of the page, so it "
                        "cannot cover or obscure content that has focus.",
                "wcag": "2.4.11",
            },
            {
                "anchor": "essential-only-cookies-page",
                "kind": "usage",
                "title": "Essential-only services still need a cookies page",
                "text": "A service that sets only essential cookies may omit the banner "
                        "but must still tell users about them, for example on a cookies "
                        "page linked in the footer.",
            },
            {
                "anchor": "server-side-form",
                "kind": "accessibility",
                "title": "Support consent without JavaScript",
                "text": "Where non-essential cookies are set server-side, present the "
                        "banner inside a form so all users can submit their choice "
                        "without relying on JavaScript.",
            },
            {
                "anchor": "client-side-focus",
                "kind": "accessibility",
                "title": "Move focus to the confirmation with assistive roles",
                "text": "For a JavaScript-only banner, reveal the confirmation message by "
                        "removing the hidden attribute, give it tabindex=-1 and "
                        "role=alert, and shift focus to it so assistive technology reads "
                        "it.",
            },
            {
                "anchor": "name-the-service",
                "kind": "usage",
                "title": "Name the service in the banner heading",
                "text": "Include the service name in the banner heading so users "
                        "understand these cookies differ from those set by the main "
                        "GOV.UK platform.",
            },
            {
                "anchor": "short-accurate-text",
                "kind": "usage",
                "title": "Keep cookie text short but accurate",
                "text": "Keep the cookie banner text as short as possible while "
                        "accurately describing how cookies are used, adapting the "
                        "example text if third parties set cookies or cookies are used "
                        "beyond analytics and settings.",
            },
            {
                "anchor": "needs-cookies-page",
                "kind": "usage",
                "title": "Provide a cookies page alongside the banner",
                "text": "Provide a cookies page in the service as well as the cookie "
                        "banner.",
            },
        ],
    },
    {
        "slug": "details",
        "title": "Details",
        "ur_text": "The service uses the GOV.UK Details component to let users reveal "
                   "more detailed information only if they need it, with short "
                   "descriptive link text, for content only some users need.",
        "clauses": [
            {
                "anchor": "for-some-users",
                "kind": "usage",
                "title": "Use for information only some users need",
                "text": "Use the details component to make a page easier to scan when it "
                        "contains information that only some users will need.",
            },
            {
                "anchor": "not-for-essential",
                "kind": "usage",
                "title": "Do not hide information most users need",
                "text": "Do not use the details component to hide information that the "
                        "majority of users will need.",
            },
            {
                "anchor": "single-section-only",
                "kind": "usage",
                "title": "Use for a single section of content",
                "text": "Use the details component instead of tabs or an accordion when "
                        "there is only one section of content and it is less important "
                        "to users.",
            },
            {
                "anchor": "clear-link-text",
                "kind": "accessibility",
                "title": "Write short, descriptive link text",
                "text": "Make the details link text short and descriptive so users can "
                        "quickly work out whether they need to reveal it.",
            },
            {
                "anchor": "avoidance-research",
                "kind": "research",
                "title": "Some users avoid the reveal link",
                "text": "There is evidence some users avoid clicking the details link "
                        "because they think it will take them away from the page, and "
                        "some voice-control users may struggle to interact with it.",
            },
        ],
    },
    {
        "slug": "error-message",
        "title": "Error message",
        "ur_text": "The service uses the GOV.UK Error message component to explain, next "
                   "to each field, what went wrong and how to fix it, worded to match "
                   "the error summary and following the plain-English error guidance.",
        "clauses": [
            {
                "anchor": "show-on-validation-error",
                "kind": "usage",
                "title": "Show a message on each validation error",
                "text": "Follow the validation pattern and, when there is a validation "
                        "error, show an error message next to the field and in the error "
                        "summary explaining what went wrong and how to fix it.",
            },
            {
                "anchor": "not-for-service-problems",
                "kind": "usage",
                "title": "Do not use for problems the user cannot fix",
                "text": "Do not use an error message to tell users they are ineligible, "
                        "lack permission, or face a service problem they cannot fix; "
                        "take them to a page that explains the problem and what to do "
                        "next.",
            },
            {
                "anchor": "red-message-and-border",
                "kind": "usage",
                "title": "Style and connect the message to its question",
                "text": "Put the message in red after the question and hint text, use a "
                        "red border to connect it to the question, and if the error "
                        "relates to a specific field give that field a red border and "
                        "name it in the message.",
            },
            {
                "anchor": "keep-field-values",
                "kind": "usage",
                "title": "Do not clear the user's answers",
                "text": "Do not clear any form fields when showing an error; keep both "
                        "passing and failing answers so users can see and edit what "
                        "went wrong.",
            },
            {
                "anchor": "hidden-error-prefix",
                "kind": "accessibility",
                "title": "Include a hidden 'Error:' prefix",
                "text": "Include a visually hidden 'Error:' before the message so screen "
                        "readers announce the error state; allow the prefix to be "
                        "changed for other languages.",
            },
            {
                "anchor": "summarise-at-top",
                "kind": "usage",
                "title": "Summarise all errors at the top of the page",
                "text": "Summarise all errors at the top of the page in an error "
                        "summary component.",
            },
            {
                "anchor": "match-label-language",
                "kind": "usage",
                "title": "Match the message to the question wording",
                "text": "Word the error message using language from the question or "
                        "fieldset label so it is clear which field it belongs to.",
            },
            {
                "anchor": "clear-and-concise",
                "kind": "usage",
                "title": "Write in plain, positive English",
                "text": "Describe what happened and how to fix it in plain, positive "
                        "English; avoid technical jargon, words like 'forbidden', "
                        "'illegal' or 'you forgot', and 'please', 'sorry', 'valid', "
                        "'invalid' or humorous language.",
            },
            {
                "anchor": "no-redundant-example",
                "kind": "usage",
                "title": "Do not repeat an on-screen example",
                "text": "Do not give an example in the error message if an example is "
                        "already shown on screen, such as in hint text.",
            },
            {
                "anchor": "consistent-with-summary",
                "kind": "usage",
                "title": "Keep the field and summary messages identical",
                "text": "Use the same message next to the field and in the error summary "
                        "so they look, sound and mean the same and make sense out of "
                        "context.",
            },
            {
                "anchor": "be-specific",
                "kind": "usage",
                "title": "Give a specific message per error state",
                "text": "Avoid generic messages such as 'An error occurred' or 'This "
                        "field is required'; give a specific message for each error "
                        "state (empty, too long, wrong format, and so on).",
            },
            {
                "anchor": "instructions-and-descriptions",
                "kind": "usage",
                "title": "Use instructions and descriptions consistently",
                "text": "Use instructions for some errors and descriptions for others, "
                        "consistently — for example an instruction like 'Enter your "
                        "name' for empty fields and a description like 'Name must be 35 "
                        "characters or less' for over-long entries.",
            },
            {
                "anchor": "use-templates",
                "kind": "usage",
                "title": "Use the standard error message templates",
                "text": "Use the standard error message templates for common errors on "
                        "components and patterns such as dates, checkboxes and "
                        "addresses.",
            },
        ],
    },
]
