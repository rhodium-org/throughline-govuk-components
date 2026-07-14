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
        "rationale": "Users need an unambiguous, prominent way to carry out an action such as starting an application, signing in, or paying, so the main call to action stands out and they always know what to do next.",
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
        "rationale": "When a user submits answers containing validation errors, they need every problem gathered and focused at the top of the page so they can find, understand, and fix each mistake rather than hunting for what went wrong.",
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
        "rationale": "Users entering a date they already know or can look up need to type the day, month and year directly, avoiding the friction of a calendar picker for dates that are memorable rather than chosen.",
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
        "rationale": "When users benefit from an overview of related sections and want to reveal, hide, and compare only the parts relevant to them, this lets them control long or repeat-use content instead of scrolling through everything at once.",
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
        "rationale": "Because browser back buttons can break services or go unnoticed, users in a multi-page transaction need a reliable in-page way to return to the previous step without losing their progress.",
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
        "rationale": "Users navigating a site with multiple hierarchical levels need to understand where they are and move up between levels, so they can orient themselves within the wider structure.",
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
        "rationale": "When a genuine legal or technical limit caps how much a user can enter, they need live feedback on characters or words remaining so they can write their full answer and then edit it down without being cut off unexpectedly.",
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
        "rationale": "Users need to select one or more options from a list, or toggle a single option on or off, when a question genuinely allows multiple answers rather than a single mutually-exclusive choice.",
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
        "rationale": "When a service sets non-essential cookies, users must be told about them and given a clear choice to accept or reject, so the service meets its data-protection obligations before storing anything on their device.",
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
        "rationale": "Users need a page to stay easy to scan when it holds information only some of them require, so less-important detail can be tucked away and revealed on demand rather than cluttering the page.",
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
        "rationale": "When a user's answer fails validation, they need a clear, specific message beside the field explaining what went wrong and how to fix it, so they can recover and correct their own input rather than being blocked.",
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
    {
        "slug": "exit-this-page",
        "rationale": "So users who could be put at risk of abuse or retaliation by someone seeing sensitive pages, such as a victim escaping domestic abuse, can leave the service quickly and cover their tracks.",
        "title": "Exit this page",
        "ur_text": "Exit this page gives users a way to quickly and safely leave a service, website or application when a page holds sensitive information that could put them at risk.",
        "clauses": [
            {
                "anchor": "use-with-pattern",
                "kind": "usage",
                "title": "Pair with the Exit a page quickly pattern",
                "text": "For service journeys, the component must be used together with the Exit a page quickly pattern.",
            },
            {
                "anchor": "when-at-risk",
                "kind": "usage",
                "title": "Use only for at-risk pages",
                "text": "Use the component only on pages whose sensitive information could put someone at risk of abuse or retaliation, or reveal their plans to escape harm.",
            },
            {
                "anchor": "scope-choice",
                "kind": "usage",
                "title": "Apply to whole service or sensitive parts",
                "text": "Apply the component either to all pages of a service or only to the parts of the journey containing sensitive information; it can also be used on standalone content pages.",
            },
            {
                "anchor": "not-when-low-risk",
                "kind": "usage",
                "title": "Do not use when risk is unlikely",
                "text": "Do not use the component when the service or content is unlikely to put a user at risk, because showing it may discourage users who do not identify as at risk.",
            },
            {
                "anchor": "position-top",
                "kind": "usage",
                "title": "Position above the grid",
                "text": "Position the component at the top of the page, above the grid row but still within the width container.",
            },
            {
                "anchor": "safe-destination",
                "kind": "usage",
                "title": "Choose a safe redirect destination",
                "text": "The button redirects to BBC Weather by default; if changed, avoid sites that show personalised content such as frequently or last visited links, which could put the user at risk.",
            },
            {
                "anchor": "secondary-link",
                "kind": "usage",
                "title": "Add the secondary skip link",
                "text": "Add the secondary link skip-link under the default skip link at the top of the body, using the same href as the button, so the component works and is more accessible.",
            },
            {
                "anchor": "session-data",
                "kind": "usage",
                "title": "Decide how to handle session data",
                "text": "Decide whether the service stores or clears the user's session data after they activate the component, for example by first redirecting to a URL that clears the session before the external site.",
            },
            {
                "anchor": "loading-overlay",
                "kind": "usage",
                "title": "Loading overlay clears the screen",
                "text": "When JavaScript is enabled, a loading overlay appears immediately on activation to clear the screen for users on slow connections while the next page loads.",
            },
            {
                "anchor": "shift-progress-dots",
                "kind": "accessibility",
                "title": "Support shift-key activation",
                "text": "Pressing the shift key three times within five seconds activates the component, with three progress dots showing keypress progress and resetting after the timeout.",
            },
            {
                "anchor": "assistive-tech-options",
                "kind": "accessibility",
                "title": "Offer discreet assistive-tech activation",
                "text": "The keyboard shortcut and hidden secondary link in the tab order give keyboard-only and assistive technology users discreet, reliable ways to activate the component.",
            },
            {
                "anchor": "research-basis",
                "kind": "research",
                "title": "Grounded in lived-experience research",
                "text": "The design is based on research with people with lived experience of domestic abuse and accessibility needs, in consultation with government departments.",
            },
            {
                "anchor": "test-with-users",
                "kind": "research",
                "title": "Research with your own users first",
                "text": "Testing has focused mainly on users at risk of domestic abuse, so teams should do their own user research before using the component, especially on static content pages.",
            },
        ],
    },
    {
        "slug": "fieldset",
        "rationale": "So users, especially screen reader users, understand that several separate form inputs are related and belong to a single question, such as the multiple text boxes making up an address.",
        "title": "Fieldset",
        "ur_text": "The fieldset component groups related form inputs so users understand the relationship between them.",
        "clauses": [
            {
                "anchor": "group-related-inputs",
                "kind": "usage",
                "title": "Use to group related inputs",
                "text": "Use a fieldset when you need to show a relationship between multiple form inputs, such as grouping the text inputs that make up an address.",
            },
            {
                "anchor": "already-included",
                "kind": "usage",
                "title": "Reuse existing component fieldsets",
                "text": "When using the Radios, Checkboxes or Date input components, rely on the fieldset they already include rather than adding another.",
            },
            {
                "anchor": "legend-first",
                "kind": "usage",
                "title": "Legend must come first and describe the group",
                "text": "The first element inside a fieldset must be a legend describing the group of inputs, either as a question or a statement.",
            },
            {
                "anchor": "legend-as-heading",
                "kind": "accessibility",
                "title": "Set the legend as the page heading for single questions",
                "text": "When asking one question per page, set the legend as the page heading so screen reader users hear the content only once.",
            },
            {
                "anchor": "legend-conveys-relationship",
                "kind": "accessibility",
                "title": "Legend signals inputs are related",
                "text": "Including the question as the legend on question pages helps screen reader users understand that all the grouped inputs relate to that question.",
            },
            {
                "anchor": "help-text-in-legend",
                "kind": "usage",
                "title": "Keep any legend help text short",
                "text": "Include general help text in the legend only when it aids form completion and cannot be written as hint text, keeping it as short as possible.",
            },
        ],
    },
    {
        "slug": "file-upload",
        "rationale": "So users can reliably select and upload a file when providing that document is critical to delivering the service, with clear errors and drag-and-drop support that also works for assistive technology.",
        "title": "File upload",
        "ur_text": "The file upload component helps users select and upload a file within a service.",
        "clauses": [
            {
                "anchor": "only-when-critical",
                "kind": "usage",
                "title": "Ask for uploads only when critical",
                "text": "Only ask users to upload a file when it is critical to the delivery of the service.",
            },
            {
                "anchor": "two-input-methods",
                "kind": "usage",
                "title": "Support choose-file and drag-and-drop",
                "text": "Let users upload a file either by using the Choose file button or by dragging and dropping a file into the upload input area.",
            },
            {
                "anchor": "reuse-files",
                "kind": "usage",
                "title": "Let users reuse uploaded files",
                "text": "Allow users to easily reuse a previously uploaded file within a single journey unless doing so would be a major security or privacy concern, considering users on public devices before enabling preview or download.",
            },
            {
                "anchor": "error-guidance",
                "kind": "usage",
                "title": "Follow error message guidance with specific errors",
                "text": "Style and write errors following the Error message component guidance, using specific messages for specific error states.",
            },
            {
                "anchor": "error-wording",
                "kind": "usage",
                "title": "Use the prescribed error wording",
                "text": "Use the standard wording for each error state, for example 'Select a [thing]', 'The selected file must be a [types]', 'The selected file must be smaller than [size]', 'The selected file is empty', 'The selected file contains a virus', 'The selected file is password protected', and 'The selected file could not be uploaded - try again'.",
            },
            {
                "anchor": "enable-improved",
                "kind": "usage",
                "title": "Opt in to the improved component",
                "text": "Enable the improved File upload component via the javascript macro option or extra markup, recommended for a better experience while noting it is a visual change that may affect existing layouts.",
            },
            {
                "anchor": "keep-text-short",
                "kind": "accessibility",
                "title": "Keep changeable text short",
                "text": "Although the button and 'No file chosen' text can be changed for translation or specificity, keep it as short as possible because long text is hard for screen reader users.",
            },
            {
                "anchor": "html-attribute-placement",
                "kind": "accessibility",
                "title": "Keep required attributes on the original input",
                "text": "In the improved component keep name, accept, capture, accesskey and multiple on the original input, since they only work there and JavaScript hides the input behind a button.",
            },
            {
                "anchor": "no-required-attribute",
                "kind": "accessibility",
                "title": "Avoid the required attribute",
                "text": "Screen readers do not read the required attribute in the improved version, and the guidance recommends not using it.",
            },
            {
                "anchor": "dragon-support",
                "kind": "accessibility",
                "title": "Improved component supports speech recognition",
                "text": "The improved component lets Dragon speech recognition users choose files with web page control commands, though browser security may require an additional action such as a mouse click first.",
            },
            {
                "anchor": "visible-drop-zone",
                "kind": "accessibility",
                "title": "Make the drop zone visible and responsive",
                "text": "The improved drop zone is bigger, visible at all times and more responsive to interactions, unlike the earlier version which showed no visual target area when dragging and dropping.",
            },
            {
                "anchor": "brand-state-updates",
                "kind": "research",
                "title": "Interaction states refreshed for the brand",
                "text": "In February 2026 the improved component's interaction states and colours were updated so users can more easily and consistently see when a file has been added.",
            },
            {
                "anchor": "known-gap-target-area",
                "kind": "research",
                "title": "Known gap in the earlier version",
                "text": "The earlier component inherited the browser default and showed no visual target area for drag and drop; the March 2025 improved component addresses this accessibility gap.",
            },
        ],
    },
    {
        "slug": "footer",
        "rationale": "So every page of a service clearly states who owns the copyright and under what licence content may be reused, and links users to privacy, accessibility, cookies and terms information.",
        "title": "GOV.UK footer",
        "ur_text": "The GOV.UK footer provides copyright, licensing and other information about a service and sits at the bottom of every page.",
        "clauses": [
            {
                "anchor": "every-page",
                "kind": "usage",
                "title": "Use at the bottom of every page",
                "text": "Use the footer at the bottom of every page of the service.",
            },
            {
                "anchor": "copyright-notice",
                "kind": "usage",
                "title": "Add a copyright notice and coat of arms",
                "text": "Add a copyright notice clarifying who owns the copyright, and for GOV.UK services include the coat of arms for consistency.",
            },
            {
                "anchor": "licensing",
                "kind": "usage",
                "title": "State the reuse licence",
                "text": "Make clear whether content can be reused and under what licence, using the Open Government Licence unless the National Archives has permitted a different one.",
            },
            {
                "anchor": "standard-link-text",
                "kind": "usage",
                "title": "Use standard footer link text",
                "text": "Use 'Privacy', 'Accessibility', 'Cookies' and 'Terms and conditions' as the link text when adding those links.",
            },
            {
                "anchor": "consistent-help-links",
                "kind": "accessibility",
                "title": "Place help links consistently",
                "text": "Place any help links consistently within the footer and ensure they function the same way on every page, to comply with WCAG 2.2 success criterion 3.2.6 Consistent help.",
                "wcag": "3.2.6",
            },
            {
                "anchor": "secondary-navigation",
                "kind": "usage",
                "title": "Add secondary navigation only for GOV.UK services",
                "text": "Only add secondary GOV.UK navigation when building a GOV.UK service and you want users to navigate away, avoiding it for linear form-type services.",
            },
            {
                "anchor": "govuk-only",
                "kind": "usage",
                "title": "Restrict the footer to GOV.UK services",
                "text": "Only services on the GOV.UK website should use the footer; services outside the GOV.UK proposition must create their own and stop using this component.",
            },
            {
                "anchor": "brand-refresh",
                "kind": "usage",
                "title": "Use the refreshed branding",
                "text": "Use the refreshed GOV.UK branding, removing the govukRebrand feature flag once the service is on GOV.UK Frontend v6.0.0 or later.",
            },
        ],
    },
    {
        "slug": "header",
        "rationale": "So users trust they are in the right place on an official gov.uk service as they move around government websites, giving a consistent GOV.UK experience and access to GOV.UK-wide tools.",
        "title": "GOV.UK header",
        "ur_text": "The GOV.UK header tells users they are using a service on GOV.UK and gives access to GOV.UK-wide tools.",
        "clauses": [
            {
                "anchor": "govuk-domains-only",
                "kind": "usage",
                "title": "Use only on GOV.UK domains",
                "text": "Use the GOV.UK header only when the service is hosted on a gov.uk, service.gov.uk or blog.gov.uk domain.",
            },
            {
                "anchor": "every-page-top",
                "kind": "usage",
                "title": "Show on every page to maintain trust",
                "text": "Show the GOV.UK header at the top of every page to maintain user trust as they move around GOV.UK.",
            },
            {
                "anchor": "not-off-domain",
                "kind": "usage",
                "title": "Do not use off GOV.UK domains",
                "text": "If the service is not on a gov.uk domain, do not use the GOV.UK header; use the Generic header component to show your own organisation's branding instead.",
            },
            {
                "anchor": "default-header",
                "kind": "usage",
                "title": "Use the default header showing only logo and GOV.UK tools",
                "text": "Most services should use the default header showing only the GOV.UK logo and GOV.UK-wide links and tools, without adding the menu of GOV.UK topic links.",
            },
            {
                "anchor": "no-service-name",
                "kind": "usage",
                "title": "Do not show service name or navigation in the header",
                "text": "Do not show a service name or navigation links in the GOV.UK header; use the Service navigation component for those instead.",
            },
            {
                "anchor": "consistent-experience",
                "kind": "usage",
                "title": "Pair with service navigation for consistency",
                "text": "Use the GOV.UK header together with the Service navigation component to give users a consistent experience and reassure them they are in the right place.",
            },
            {
                "anchor": "brand-refresh",
                "kind": "usage",
                "title": "Use the refreshed branding",
                "text": "Use the refreshed GOV.UK branding, removing the govukRebrand feature flag once on GOV.UK Frontend v6.0.0 or later, and only use the header on GOV.UK-proposition services.",
            },
        ],
    },
    {
        "slug": "inset-text",
        "rationale": "So a block of supporting text like a quote, example or extra note is visually differentiated from surrounding content, used sparingly since it is not reliable enough for very important information.",
        "title": "Inset text",
        "ur_text": "The inset text component differentiates a block of text from the surrounding content, such as quotes, examples or additional information.",
        "clauses": [
            {
                "anchor": "differentiate-block",
                "kind": "usage",
                "title": "Use to differentiate a block of text",
                "text": "Use inset text to differentiate a block of text such as a quote, example or additional information about the page from the surrounding content.",
            },
            {
                "anchor": "not-for-important",
                "kind": "usage",
                "title": "Do not use for very important information",
                "text": "Avoid using inset text to highlight very important information users need to see, because some users do not notice it on complex or busy pages.",
            },
            {
                "anchor": "use-warning-text-instead",
                "kind": "usage",
                "title": "Use Warning text for critical content",
                "text": "To draw attention to very important content such as legal information, use the Warning text component instead of inset text.",
            },
            {
                "anchor": "use-sparingly",
                "kind": "usage",
                "title": "Use sparingly",
                "text": "Use inset text very sparingly, as it becomes less effective when overused.",
            },
        ],
    },
    {
        "slug": "notification-banner",
        "rationale": "Alerts users to something they need to know but that is not directly tied to the current task, such as a service-wide problem, an approaching deadline, or the outcome of a prior action, without cluttering the main content.",
        "title": "Notification banner",
        "ur_text": "A notification banner tells the user about something they need to know that is not directly related to the page content, and a service uses it for service-wide problems, personal alerts, or the outcome of a completed action.",
        "clauses": [
            {
                "anchor": "when-to-use",
                "kind": "usage",
                "title": "Use for information not directly relevant to the page task",
                "text": "Use a notification banner to tell the user about something not directly relevant to the task on that page, such as a service-wide problem, an alert affecting them personally, or the outcome of a previous action.",
            },
            {
                "anchor": "use-sparingly",
                "kind": "usage",
                "title": "Use notification banners sparingly",
                "text": "Use notification banners sparingly, because people often miss them and overusing them worsens this.",
            },
            {
                "anchor": "relevant-info-in-content",
                "kind": "usage",
                "title": "Put directly relevant information in the page content",
                "text": "If the information is directly relevant to the task on the page, put it in the main page content and use inset text or warning text if it needs to stand out, rather than a notification banner.",
            },
            {
                "anchor": "not-for-validation-errors",
                "kind": "usage",
                "title": "Do not use for validation errors",
                "text": "Do not use a notification banner to tell the user about validation errors; use the error message and error summary components instead.",
            },
            {
                "anchor": "not-with-error-summary",
                "kind": "usage",
                "title": "Do not show alongside an error summary",
                "text": "Do not show a notification banner and an error summary on the same page; show only the error summary.",
            },
            {
                "anchor": "position-before-h1",
                "kind": "usage",
                "title": "Position immediately before the page h1",
                "text": "Position the notification banner immediately before the page h1, at the same width as the page's other content.",
            },
            {
                "anchor": "screen-reader-navigation",
                "kind": "accessibility",
                "title": "Expose the banner as a labelled region",
                "text": "Use role=\"region\" and aria-labelledby=\"govuk-notification-banner-title\" (with a matching id on the title) so screen reader users can navigate to the notification banner.",
            },
            {
                "anchor": "single-banner-per-page",
                "kind": "usage",
                "title": "Show only one notification banner per page",
                "text": "Avoid showing more than one notification banner on a page; combine messages into one, or if too different, show only the highest priority banner.",
            },
            {
                "anchor": "headings-in-content",
                "kind": "usage",
                "title": "Use h3 headings to structure content",
                "text": "Use h3 headings within the banner content to structure it, but avoid headings for single-line notifications that do not need them.",
            },
            {
                "anchor": "neutral-blue-for-problems",
                "kind": "usage",
                "title": "Use the neutral blue version for problems and elsewhere-events",
                "text": "Use the neutral blue notification banner to tell the user about a problem with the whole service or about something happening elsewhere in the service.",
            },
            {
                "anchor": "green-for-success",
                "kind": "usage",
                "title": "Use the green version to confirm an expected outcome",
                "text": "Use the green version of the notification banner to confirm that something the user expected to happen has happened.",
            },
            {
                "anchor": "success-role-alert",
                "kind": "accessibility",
                "title": "Add role=alert so focus shifts on load",
                "text": "When reporting the outcome of a user action, add role=\"alert\" so focus shifts to the notification banner on page load.",
            },
            {
                "anchor": "remove-green-on-navigation",
                "kind": "usage",
                "title": "Remove the green banner when moving to a new page",
                "text": "Remove a green notification banner when the user moves to a new page.",
            },
            {
                "anchor": "success-heading-not-colour",
                "kind": "accessibility",
                "title": "Convey success meaning with a heading, not colour alone",
                "text": "Use a heading such as 'Success' on green banners so meaning is not conveyed by colour alone.",
                "wcag": "1.4.1",
            },
            {
                "anchor": "consistent-success-heading",
                "kind": "accessibility",
                "title": "Use the same success heading consistently",
                "text": "Use the same heading for green notification banners across a service to identify components that work the same way consistently.",
                "wcag": "3.2.4",
            },
            {
                "anchor": "research-gaps",
                "kind": "research",
                "title": "Open research questions",
                "text": "More research is needed on how often users miss important information in notification banners, including assistive technology users, and whether and how to let users dismiss notifications.",
            },
        ],
    },
    {
        "slug": "pagination",
        "rationale": "Lets users navigate forwards and backwards through a series of numbered pages so that content split for performance or usability, like search results or multi-page guidance, stays fast to load and easy to move through.",
        "title": "Pagination",
        "ur_text": "Pagination helps users navigate forwards and backwards through a series of numbered pages, and a service uses it for collections such as search results or guidance split across multiple pages.",
        "clauses": [
            {
                "anchor": "when-to-use",
                "kind": "usage",
                "title": "Use when a single page loads too slowly or most users need only early pages",
                "text": "Consider pagination when showing all content on one page makes it load too slowly, or when most users only need the first page or first few pages.",
            },
            {
                "anchor": "only-if-improves",
                "kind": "usage",
                "title": "Only paginate if it improves performance or usability",
                "text": "Only break content onto separate pages if it improves the performance or usability of the service.",
            },
            {
                "anchor": "no-infinite-scroll",
                "kind": "accessibility",
                "title": "Avoid infinite scroll",
                "text": "Avoid the infinite scroll technique that auto-loads content near the bottom of the page, because it causes problems for keyboard users.",
            },
            {
                "anchor": "not-for-linear-journeys",
                "kind": "usage",
                "title": "Do not use for linear journeys",
                "text": "Do not use pagination for linear journeys such as forms; use a Button (usually 'Continue') and a Back link instead.",
            },
            {
                "anchor": "place-after-content",
                "kind": "usage",
                "title": "Place pagination after the page content",
                "text": "Add the pagination component after the content on each page being paginated.",
            },
            {
                "anchor": "hide-if-single-page",
                "kind": "usage",
                "title": "Do not show pagination for a single page",
                "text": "Do not show pagination if there is only one page of content.",
            },
            {
                "anchor": "redirect-missing-page",
                "kind": "usage",
                "title": "Redirect to the first page for dead URLs",
                "text": "Redirect users to the first page if they enter a URL for a page that no longer exists.",
            },
            {
                "anchor": "block-style-for-content",
                "kind": "usage",
                "title": "Use block style for related content pages",
                "text": "Use the 'block' style of pagination for navigating related content split across multiple pages, stacking the links vertically so they are obvious to screen magnifier users when zoomed in.",
            },
            {
                "anchor": "link-labels-context",
                "kind": "usage",
                "title": "Use link labels for context",
                "text": "Use link labels to give context on what the neighbouring pages are about.",
            },
            {
                "anchor": "list-style-for-items",
                "kind": "usage",
                "title": "Use list style for pages of items",
                "text": "Use a list-type layout when users navigate through pages of similar items, such as search results or a list of cases.",
            },
            {
                "anchor": "page-number-in-title",
                "kind": "accessibility",
                "title": "Show the page number in the page title",
                "text": "Show the page number in the page <title>, for example 'Search results (page 1 of 4)', so screen reader users know they have navigated to a different page.",
            },
            {
                "anchor": "responsive-page-count",
                "kind": "usage",
                "title": "Show pages appropriate to screen size",
                "text": "Show an appropriate number of pages for the horizontal space: on smaller screens show current, previous, next, first and last; on larger screens show current, at least one page either side, and first and last.",
            },
            {
                "anchor": "ellipses-for-skipped",
                "kind": "usage",
                "title": "Use ellipses for skipped pages",
                "text": "Use ellipses to replace any skipped page numbers.",
            },
            {
                "anchor": "hide-prev-next-at-ends",
                "kind": "usage",
                "title": "Hide previous on first page and next on last page",
                "text": "Do not show the previous page link on the first page, and do not show the next page link on the last page.",
            },
            {
                "anchor": "filtering-sorting",
                "kind": "usage",
                "title": "Apply filtering and sorting to the whole list",
                "text": "If the user filters or sorts, apply it to the whole list rather than only the current page and redirect them to the first page of the new results.",
            },
            {
                "anchor": "set-defaults",
                "kind": "usage",
                "title": "Set defaults to reduce clicks",
                "text": "Set defaults to minimise how many pages most users must click through to find what they need.",
            },
            {
                "anchor": "research-basis",
                "kind": "research",
                "title": "Based on proven government components",
                "text": "This component is based on similar ones used successfully by GDS, the Ministry of Justice and the Home Office, and on Design System backlog feedback.",
            },
        ],
    },
    {
        "slug": "panel",
        "rationale": "Highlights that a transaction has been completed successfully on a confirmation or results page, giving users clear high-level reassurance and any reference they need once they finish.",
        "title": "Panel",
        "ur_text": "The panel component is a visible container used on confirmation or results pages to highlight important content, and a service uses it to confirm a completed transaction.",
        "clauses": [
            {
                "anchor": "use-for-completed-transaction",
                "kind": "usage",
                "title": "Use to display important information after a completed transaction",
                "text": "Use the panel component to display important information when a transaction has been completed, most often on confirmation pages telling the user they have successfully completed it.",
            },
            {
                "anchor": "not-in-body-content",
                "kind": "usage",
                "title": "Never use to highlight information in body content",
                "text": "Never use the panel component to highlight important information within body content.",
            },
            {
                "anchor": "keep-text-brief",
                "kind": "usage",
                "title": "Keep panel text brief",
                "text": "Keep panel text brief as a high-level explanation of what has happened, for example 'Application complete'.",
            },
            {
                "anchor": "short-words",
                "kind": "usage",
                "title": "Use short words to stay readable at all sizes",
                "text": "Use short words and phrases so highlighted information is easy to read across screen sizes and less likely to wrap, including when zoomed on mobile.",
            },
            {
                "anchor": "description-for-detail",
                "kind": "usage",
                "title": "Use description text for detail",
                "text": "If you need to give detailed information or more context, use the description text under the heading text.",
            },
        ],
    },
    {
        "slug": "password-input",
        "rationale": "Helps users create and enter passwords accessibly, letting them reveal what they typed to reduce errors and choose stronger, more unique passwords before submitting.",
        "title": "Password input",
        "ur_text": "The password input component helps users accessibly create and enter passwords, with an option to show what they have entered as plain text, and a service uses it whenever a password must be created or entered.",
        "clauses": [
            {
                "anchor": "when-to-use",
                "kind": "usage",
                "title": "Use whenever a password is created or entered",
                "text": "Use this component whenever you need users to create or enter a password.",
            },
            {
                "anchor": "not-for-other-info",
                "kind": "usage",
                "title": "Do not use for non-password information",
                "text": "Do not use this component to ask for anything other than a password; use a text input for MFA codes, security-question answers and other personally identifiable information.",
            },
            {
                "anchor": "show-plain-text-option",
                "kind": "usage",
                "title": "Let users show their entry as plain text",
                "text": "Allow users to show what they have entered as plain text so they can visually check the password before submitting, reducing errors and helping them choose stronger passwords.",
            },
            {
                "anchor": "generic-login-error",
                "kind": "usage",
                "title": "Do not reveal which credential was wrong",
                "text": "If account details are entered incorrectly, do not reveal whether the username or password was wrong, and clear any information entered into the password input.",
            },
            {
                "anchor": "hide-by-default",
                "kind": "usage",
                "title": "Hide passwords by default",
                "text": "Hide passwords by default until the user chooses to show them, because users may not be in a private space.",
            },
            {
                "anchor": "distinct-toggle-labels",
                "kind": "accessibility",
                "title": "Use distinct labels and toggles for multiple inputs",
                "text": "If a page has two or more password inputs, the show and hide toggles and labels for each input must be different.",
            },
            {
                "anchor": "no-confirm-field",
                "kind": "usage",
                "title": "Avoid a confirm password field",
                "text": "Do not add a second 'confirm password' field, as it is unnecessary when the component lets users show and hide passwords.",
            },
            {
                "anchor": "type-password-on-submit",
                "kind": "usage",
                "title": "Set input type to password on submit",
                "text": "On form submission the password input should automatically change its type to password if it has not already, to stop browsers offering it as an autofill value on non-password inputs.",
            },
            {
                "anchor": "autocomplete-attribute",
                "kind": "usage",
                "title": "Use the autocomplete attribute",
                "text": "Set the autocomplete attribute to new-password when the user is creating a password and current-password otherwise, to help browsers and password managers.",
            },
            {
                "anchor": "allow-copy-paste",
                "kind": "usage",
                "title": "Always allow copy and paste",
                "text": "Always allow users to copy and paste in password fields, for example when using a password manager.",
            },
            {
                "anchor": "support-all-characters",
                "kind": "usage",
                "title": "Support all characters and avoid restricting input",
                "text": "Support all characters users may need in a password, including numbers and symbols, and avoid restricting input.",
            },
            {
                "anchor": "consistent-restrictions",
                "kind": "usage",
                "title": "Keep any restrictions identical and consistent",
                "text": "If you must apply password restrictions, be clear and consistent and keep them identical wherever the user creates or enters a password; if restrictions change, continue supporting existing passwords or ask users to set a new one.",
            },
            {
                "anchor": "no-maxlength",
                "kind": "usage",
                "title": "Do not use maxlength to restrict length",
                "text": "Do not use maxlength to restrict password length because users get no feedback when truncated; if length must be limited, show an error message using the validation pattern instead.",
            },
            {
                "anchor": "no-spellcheck-autocapitalise",
                "kind": "usage",
                "title": "Disable spellcheck and autocapitalise",
                "text": "Set the spellcheck attribute to false and the autocapitalize attribute to off so browsers do not alter the input, which also avoids spell-jacking that can leak passwords to third parties.",
            },
            {
                "anchor": "known-issues-native-toggles",
                "kind": "usage",
                "title": "Native show/hide tools can duplicate or mismatch",
                "text": "Be aware that browsers, password managers and screen readers may add their own show/hide functionality, which can duplicate the button or cause the button label to mismatch the actual state.",
            },
            {
                "anchor": "research-no-second-field",
                "kind": "research",
                "title": "Research decided against a second field",
                "text": "The team decided a second field is not helpful for users, particularly on password inputs with show and hide buttons, and is seeking real-life examples from service teams to support this.",
            },
        ],
    },
    {
        "slug": "phase-banner",
        "rationale": "Signals to users that a service is still being worked on in alpha or beta and invites feedback, as required for service.gov.uk domains until they pass a live assessment.",
        "title": "Phase banner",
        "ur_text": "The phase banner shows users a service is still being worked on, and a service.gov.uk service uses it to display its alpha or beta status until it passes a live assessment.",
        "clauses": [
            {
                "anchor": "required-until-live",
                "kind": "usage",
                "title": "Required on service.gov.uk until live assessment passed",
                "text": "Services hosted on a service.gov.uk domain must use the phase banner until they pass a live assessment.",
            },
            {
                "anchor": "alpha-vs-beta",
                "kind": "usage",
                "title": "Use the alpha or beta banner to match the phase",
                "text": "Use an alpha banner when the service is in alpha, and a beta banner when it is in private or public beta.",
            },
            {
                "anchor": "position-in-header",
                "kind": "usage",
                "title": "Show inside the header after navigation or GOV.UK header",
                "text": "Show the phase banner inside the <header> element, directly after the Service navigation component, or after the GOV.UK header component if the service does not use Service navigation.",
            },
            {
                "anchor": "service-level-message",
                "kind": "usage",
                "title": "Show on all pages as a service-level message",
                "text": "Show the phase banner across all pages so users understand it as a service-level message.",
            },
            {
                "anchor": "feedback-link",
                "kind": "usage",
                "title": "Include a feedback link",
                "text": "Use a feedback link to collect on-page feedback about the service, opening an email or taking the user to a dedicated page or form.",
            },
            {
                "anchor": "preserve-place",
                "kind": "usage",
                "title": "Let users return to their place after feedback",
                "text": "Whatever feedback option is used, make sure users do not lose their place in the service and can return to the page they were on.",
            },
        ],
    },
    {
        "slug": "radios",
        "rationale": "Lets users select exactly one option from a list when the choices are mutually exclusive, making the single-answer constraint clear and preventing the confusion of allowing multiple selections.",
        "title": "Radios",
        "ur_text": "The radios component lets users select a single option from a list, and a service uses it when only one option can be chosen.",
        "clauses": [
            {
                "anchor": "when-to-use",
                "kind": "usage",
                "title": "Use when only one option can be selected",
                "text": "Use the radios component when users can only select one option from a list.",
            },
            {
                "anchor": "not-for-multiple",
                "kind": "usage",
                "title": "Do not use when multiple selections are possible",
                "text": "Do not use radios if users might need to select more than one option; use the checkboxes component instead.",
            },
            {
                "anchor": "position-left-of-labels",
                "kind": "accessibility",
                "title": "Position radios to the left of their labels",
                "text": "Always position radios to the left of their labels to make them easier to find, especially for screen magnifier users.",
            },
            {
                "anchor": "hint-single-select",
                "kind": "usage",
                "title": "Add a hint that only one option can be chosen",
                "text": "Do not assume users know only one option can be selected from the visual style alone; if needed add a hint such as 'Select one option'.",
            },
            {
                "anchor": "no-preselect",
                "kind": "usage",
                "title": "Do not pre-select an option",
                "text": "Do not pre-select radio options, as users are more likely to miss the question or submit the wrong answer.",
            },
            {
                "anchor": "include-none-option",
                "kind": "usage",
                "title": "Include a 'None of the above' option when valid",
                "text": "Because users cannot return to no selection once one is made without refreshing, include 'None of the above' or 'I do not know' when these are valid options.",
            },
            {
                "anchor": "order-alphabetically",
                "kind": "usage",
                "title": "Order options alphabetically by default",
                "text": "Order radio options alphabetically by default; only order by most-to-least common with extreme caution as it can reinforce bias, and order alphabetically if in doubt.",
            },
            {
                "anchor": "fieldset-legend",
                "kind": "accessibility",
                "title": "Group radios in a fieldset with a describing legend",
                "text": "Group radios in a <fieldset> with a <legend> that describes them, usually a question such as 'Where do you live?'.",
            },
            {
                "anchor": "legend-as-heading-single",
                "kind": "accessibility",
                "title": "Set legend as page heading when asking one question",
                "text": "If asking just one question per page, set the legend as the page heading so screen reader users hear the content only once.",
            },
            {
                "anchor": "no-legend-heading-multiple",
                "kind": "usage",
                "title": "Do not set legend as heading with multiple questions",
                "text": "If asking more than one question on the page, do not set the legend as the page heading.",
            },
            {
                "anchor": "inline-radios",
                "kind": "usage",
                "title": "Only use inline radios for two short options",
                "text": "Only use inline radios when the question has two options and both are short, remembering they still stack vertically on small screens.",
            },
            {
                "anchor": "hint-text-format",
                "kind": "accessibility",
                "title": "Keep item hints to one short sentence with no links",
                "text": "Keep each radio item hint to a single short sentence without full stops and do not use links in hint text, because screen readers read the whole text and do not usually announce that it is a link.",
            },
            {
                "anchor": "text-divider",
                "kind": "usage",
                "title": "Separate a distinct option with a text divider",
                "text": "If one or more options differ from the others, separate them with a text divider, usually the word 'or'.",
            },
            {
                "anchor": "conditional-reveal-simple",
                "kind": "usage",
                "title": "Keep conditionally revealed questions simple",
                "text": "You can conditionally reveal a related question when a radio option is selected, but keep it simple and show complicated or multi-part questions on the next page instead.",
            },
            {
                "anchor": "conditional-reveal-restrictions",
                "kind": "usage",
                "title": "Restrict conditional reveal to questions only",
                "text": "Do not conditionally reveal questions from inline radios, and only conditionally reveal questions, never showing or hiding anything that is not a question.",
            },
            {
                "anchor": "conditional-reveal-wcag",
                "kind": "accessibility",
                "title": "Conditional reveal has a known notification gap",
                "text": "Users are not always notified when a conditionally revealed question is shown or hidden, which fails WCAG success criterion 4.1.2 Name, role, value.",
                "wcag": "4.1.2",
            },
            {
                "anchor": "smaller-radios",
                "kind": "usage",
                "title": "Use smaller radios only when less prominence helps",
                "text": "Use standard-sized radios in nearly all cases; use smaller versions only where making them less prominent helps, such as search filters or information-dense caseworking screens designed for repeat use.",
            },
            {
                "anchor": "error-conditions",
                "kind": "usage",
                "title": "Show an error when no radio or revealed question is answered",
                "text": "Display an error message if the user has not selected any radios or has not answered a conditionally revealed question, following the error message component guidance with specific messages for specific error states.",
            },
            {
                "anchor": "error-wording",
                "kind": "usage",
                "title": "Word errors according to the option pattern",
                "text": "Word errors by pattern: 'Select yes if...' for yes/no questions, 'Select if...' for two non-yes/no options, and 'Select...' for more than two options; for a conditionally revealed question use an error message clearly related to the initial question.",
            },
            {
                "anchor": "research-conditional-reveal",
                "kind": "research",
                "title": "Research found simple conditional reveals workable",
                "text": "Testing found screen reader users had no difficulty answering conditionally revealed questions as long as they were kept simple, but got confused by complicated or multi-part revealed questions, and the team continues to seek research on their use.",
            },
        ],
    },
    {
        "slug": "select",
        "rationale": "Offers a last-resort way to pick one option from a long list in public services, but should be avoided because research shows many users struggle to open, scroll, and choose within selects, so ask narrowing questions or use radios instead.",
        "title": "Select",
        "ur_text": "The select component helps users choose a single item from a long list, used only as a last resort in public-facing services because some users find selects hard to use.",
        "clauses": [
            {
                "anchor": "last-resort-public",
                "kind": "usage",
                "title": "Use only as a last resort",
                "text": "Only use the select component in public-facing services as a last resort, because research shows some users find selects very difficult to use.",
            },
            {
                "anchor": "ask-questions-first",
                "kind": "usage",
                "title": "Reduce options before using select",
                "text": "Before using select, ask users questions that present them with fewer options, and consider an alternative such as radios.",
            },
            {
                "anchor": "preselect-settings",
                "kind": "usage",
                "title": "Pre-select only for settings",
                "text": "When the component is used for settings, an option may be pre-selected by default when users first see it.",
            },
            {
                "anchor": "no-preselect-questions",
                "kind": "usage",
                "title": "Do not pre-select for questions",
                "text": "When the component is used for questions, do not pre-select any option in case it influences users' answers.",
            },
            {
                "anchor": "hint-single-sentence",
                "kind": "usage",
                "title": "Keep hint text short",
                "text": "Keep hint text to a single short sentence without any full stops to help users understand and choose an option.",
            },
            {
                "anchor": "no-links-in-hint",
                "kind": "accessibility",
                "title": "No links in hint text",
                "text": "Do not use links in hint text, because screen readers read the link text but usually do not tell users it is a link.",
            },
            {
                "anchor": "error-on-no-selection",
                "kind": "usage",
                "title": "Show error when no option selected",
                "text": "Display a styled error message if the user has not selected an option.",
            },
            {
                "anchor": "no-multiple-select",
                "kind": "accessibility",
                "title": "Avoid multiple selection",
                "text": "Do not add functionality for selecting multiple options; use another method such as a list of checkboxes, because select multiple has poor usability and assistive technology support.",
            },
            {
                "anchor": "known-usability-issues",
                "kind": "research",
                "title": "Known usability struggles",
                "text": "Research shows users struggle with selects, including being unable to close them, trying to type into them, confusing focused with selected items, pinch-zooming options, and not realising they can scroll for more items.",
            },
        ],
    },
    {
        "slug": "service-navigation",
        "rationale": "Reassures users that they are in the right place within a specific service and lets them move between its parts, giving a consistent experience that shows GOV.UK functions as one coherent website.",
        "title": "Service navigation",
        "ur_text": "Service navigation helps users understand they are using your service and lets them navigate around it, showing the service name and optional navigation links.",
        "clauses": [
            {
                "anchor": "use-to-show-service",
                "kind": "usage",
                "title": "Use to identify the service",
                "text": "Use the service navigation to help users understand that they are using your service.",
            },
            {
                "anchor": "consistent-with-header",
                "kind": "usage",
                "title": "Pair with the GOV.UK header",
                "text": "Use the service navigation together with the GOV.UK header component to give users a consistent experience and assure them GOV.UK functions as one website.",
            },
            {
                "anchor": "show-service-name",
                "kind": "usage",
                "title": "Show the service name",
                "text": "Use the service navigation to display your service name.",
            },
            {
                "anchor": "navigation-links",
                "kind": "usage",
                "title": "Show navigation links",
                "text": "Show navigation links to let users move to different parts of your service and find useful links and tools.",
            },
            {
                "anchor": "slots-custom-elements",
                "kind": "usage",
                "title": "Use slots for custom elements",
                "text": "Use slots to insert custom HTML such as language selectors, providing your own styles and JavaScript and deciding on appropriate layout and positioning.",
            },
            {
                "anchor": "accurate-aria-label",
                "kind": "accessibility",
                "title": "Keep aria-label accurate",
                "text": "When a service name is shown, the section is exposed as a region landmark, so rename the aria-label as needed to accurately describe what slots add to the section.",
            },
            {
                "anchor": "test-each-update",
                "kind": "usage",
                "title": "Retest slots on each update",
                "text": "Ensure slot content still works as intended after each update of GOV.UK Frontend, because contents may look or work differently in a future release.",
            },
            {
                "anchor": "use-refreshed-branding",
                "kind": "usage",
                "title": "Use refreshed GOV.UK branding",
                "text": "Use the refreshed GOV.UK branding; on GOV.UK Frontend v6.0.0 or later remove the govukRebrand feature flag.",
            },
        ],
    },
    {
        "slug": "skip-link",
        "rationale": "Lets keyboard-only users bypass repetitive top-level navigation links and jump straight to a page's main content, removing the burden of tabbing through the header on every page.",
        "title": "Skip link",
        "ur_text": "The skip link component helps keyboard-only users skip the top-level navigation and jump straight to the main content on a page.",
        "clauses": [
            {
                "anchor": "required-all-pages",
                "kind": "accessibility",
                "title": "Include on every GOV.UK page",
                "text": "All GOV.UK pages must include a skip link.",
            },
            {
                "anchor": "placement",
                "kind": "usage",
                "title": "Place after the opening body tag",
                "text": "Place the skip link immediately after the opening body tag, or immediately after the cookie banner if a cookie banner component is used.",
            },
            {
                "anchor": "ignore-landmark-warning",
                "kind": "accessibility",
                "title": "Ignore the landmark warning",
                "text": "Ignore automated accessibility warnings that the skip link is not inside a landmark; do not wrap it in a nav region or move it inside the header.",
            },
            {
                "anchor": "bypass-navigation",
                "kind": "accessibility",
                "title": "Let users bypass navigation",
                "text": "The skip link gives keyboard users the option to bypass the top-level navigation links and jump to the main content on a page.",
            },
            {
                "anchor": "visually-hidden-until-focus",
                "kind": "accessibility",
                "title": "Hidden until keyboard activation",
                "text": "The skip link is visually hidden until a keyboard press activates it.",
            },
        ],
    },
    {
        "slug": "summary-list",
        "rationale": "Presents information as key-and-value facts, such as metadata or a user's form answers at the end of a journey, so people can review and correct their responses before submitting.",
        "title": "Summary list",
        "ur_text": "A summary list summarises information as a list of key facts, such as a user's responses at the end of a form, with an optional summary card variant for grouping multiple lists.",
        "clauses": [
            {
                "anchor": "use-for-key-facts",
                "kind": "usage",
                "title": "Use for a list of key facts",
                "text": "Use a summary list to show information as a list of key facts, such as metadata or a user's responses at the end of a form.",
            },
            {
                "anchor": "key-value-only",
                "kind": "usage",
                "title": "Only for key-and-value information",
                "text": "Only use the summary list for information that has a key and at least one value, because it uses the description list (dl) element.",
            },
            {
                "anchor": "not-tabular-or-simple-list",
                "kind": "usage",
                "title": "Do not use for tables or simple lists",
                "text": "Do not use the summary list for tabular data or a simple list of information or tasks; use a table, ul or ol instead.",
            },
            {
                "anchor": "row-key-value",
                "kind": "usage",
                "title": "Structure each row as key and value",
                "text": "Make each row a key that labels a piece of information and a value that is the information itself.",
            },
            {
                "anchor": "structure-multiple-lists",
                "kind": "usage",
                "title": "Add structure to multiple lists",
                "text": "When showing multiple summary lists on a page, add structure using headings or summary cards.",
            },
            {
                "anchor": "row-action-hidden-text",
                "kind": "accessibility",
                "title": "Add visually hidden text to row actions",
                "text": "Add visually hidden text to row action links so screen reader users hear the action and the key label it affects, such as 'Change name'.",
            },
            {
                "anchor": "prepopulate-on-return",
                "kind": "usage",
                "title": "Pre-populate when returning to answers",
                "text": "When a user goes back to a previous answer through a card or row action, pre-populate information they have already entered.",
            },
            {
                "anchor": "mixed-actions-modifier",
                "kind": "usage",
                "title": "Mark rows without actions",
                "text": "When mixing rows with and without actions, add the govuk-summary-list__row--no-actions modifier class to rows without actions so the bottom border draws correctly.",
            },
            {
                "anchor": "borders-caution",
                "kind": "accessibility",
                "title": "Think carefully before removing borders",
                "text": "Only remove separating borders when the list has no actions, and think carefully first because borders help users who zoom or magnify their screen find and read rows.",
            },
            {
                "anchor": "missing-information-link",
                "kind": "usage",
                "title": "Link to complete missing information",
                "text": "For a row with missing information, show a link to the appropriate question page in the value column instead of a 'change' link.",
            },
            {
                "anchor": "cards-same-type",
                "kind": "usage",
                "title": "Use summary cards for same-type lists",
                "text": "Use summary cards when showing multiple summary lists that describe the same type of thing, or actions that apply to all items in a list.",
            },
            {
                "anchor": "cards-not-for-small",
                "kind": "usage",
                "title": "Do not use cards for small amounts",
                "text": "Do not use summary cards for a small amount of related information; use summary lists structured with headings instead.",
            },
            {
                "anchor": "card-title-unique",
                "kind": "usage",
                "title": "Give each card a unique title",
                "text": "Give each summary card a short, relevant and unique title that identifies what the summary list describes.",
            },
            {
                "anchor": "card-action-link-text",
                "kind": "usage",
                "title": "Write clear card action link text",
                "text": "Write card action link text that says what the action does and that it applies to the entire card, keeping it as short as possible, usually two words.",
            },
            {
                "anchor": "limit-card-actions",
                "kind": "usage",
                "title": "Limit card actions",
                "text": "Do not add more than two to three actions in a summary card header.",
            },
            {
                "anchor": "confirm-serious-actions",
                "kind": "usage",
                "title": "Confirm serious card actions",
                "text": "If a card action cannot easily be undone or might have serious consequences, add a warning or ask the user for confirmation.",
            },
        ],
    },
    {
        "slug": "table",
        "rationale": "Makes information easier to compare and scan by arranging related data into rows and columns, so users can read across shared attributes rather than hunting through prose.",
        "title": "Table",
        "ur_text": "The table component presents information in rows and columns to make it easier for users to compare and scan.",
        "clauses": [
            {
                "anchor": "use-to-compare",
                "kind": "usage",
                "title": "Use to compare information",
                "text": "Use the table component to let users compare information in rows and columns.",
            },
            {
                "anchor": "not-for-layout",
                "kind": "usage",
                "title": "Never use for layout",
                "text": "Never use the table component to lay out content on a page; use the grid system instead.",
            },
            {
                "anchor": "caption-describes-table",
                "kind": "accessibility",
                "title": "Describe the table with a caption",
                "text": "Use the caption element to describe a table like a heading, helping users find, navigate and understand tables.",
            },
            {
                "anchor": "headers-with-scope",
                "kind": "accessibility",
                "title": "Use headers with scope",
                "text": "Use table headers to tell users what rows and columns represent, and use the scope attribute to help assistive technology distinguish row and column headers.",
            },
            {
                "anchor": "right-align-numbers",
                "kind": "usage",
                "title": "Right-align columns of numbers",
                "text": "When comparing columns of numbers, align the numbers to the right in table cells.",
            },
            {
                "anchor": "reduce-data",
                "kind": "usage",
                "title": "Reduce data in tables",
                "text": "Aim to have less data in tables, organising large amounts into multiple tables or multiple pages where possible.",
            },
            {
                "anchor": "small-text-only-large-data",
                "kind": "usage",
                "title": "Only shrink text for lots of data",
                "text": "Use govuk-table--small-text-until-tablet only when a table has a lot of data, because a smaller amount of data is easier to read when the text is larger.",
            },
        ],
    },
    {
        "slug": "tabs",
        "rationale": "Lets regular or expert users quickly switch between clearly labelled related sections without viewing all at once, but is avoided when users must read in order or compare content, since tabs hide information many people miss.",
        "title": "Tabs",
        "ur_text": "The tabs component lets users quickly switch between related sections of content, displaying one clearly labelled section at a time.",
        "clauses": [
            {
                "anchor": "when-tabs-help",
                "kind": "usage",
                "title": "Use for clearly separable sections",
                "text": "Use tabs when content separates into clearly labelled sections, the first section is most relevant for most users, and users do not need to view all sections at once.",
            },
            {
                "anchor": "not-for-slow-content",
                "kind": "usage",
                "title": "Do not use for heavy or navigational content",
                "text": "Do not use tabs if the content would make the page slow to load, and do not use them as a form of page navigation.",
            },
            {
                "anchor": "not-for-sequential-or-compare",
                "kind": "usage",
                "title": "Do not use for ordered or comparison content",
                "text": "Do not use tabs if users need to read content in order or compare information across different tabs.",
            },
            {
                "anchor": "test-without-tabs",
                "kind": "usage",
                "title": "Test content without tabs first",
                "text": "Test content without tabs first and consider simplifying it, splitting across pages, separating with headings, or using a table of contents.",
            },
            {
                "anchor": "choose-over-accordion-details",
                "kind": "usage",
                "title": "Choose tabs versus accordion or details",
                "text": "Prefer tabs when the user views one section at a time or switches quickly between sections without pushing content down the page, but accordions suit many sections and details suits one or two short, less important pieces.",
            },
            {
                "anchor": "no-js-fallback",
                "kind": "accessibility",
                "title": "Provide a no-JavaScript fallback",
                "text": "When JavaScript is not available, show the tabbed content on a single page in order with a table of contents linking to each section.",
            },
            {
                "anchor": "clear-labels",
                "kind": "usage",
                "title": "Use clear tab labels",
                "text": "Make tab labels clearly describe what they link to, since tabs hide content and unclear labels leave users unsure whether to click.",
            },
            {
                "anchor": "order-by-user-needs",
                "kind": "usage",
                "title": "Order tabs by user need",
                "text": "Make the first tab the most commonly needed section and arrange the others in the order that makes most sense for users.",
            },
            {
                "anchor": "do-not-disable",
                "kind": "usage",
                "title": "Do not disable tabs",
                "text": "Do not disable tabs; if there is no content, either remove the tab or explain why there is no content when the tab is selected.",
            },
            {
                "anchor": "avoid-wrapping",
                "kind": "usage",
                "title": "Avoid tabs wrapping onto multiple lines",
                "text": "Avoid too many tabs or long labels that wrap over more than one line, because this makes the connection between the selected tab and its content harder to see.",
            },
            {
                "anchor": "add-headings",
                "kind": "accessibility",
                "title": "Add a heading to each tab's content",
                "text": "Include a heading at the start of each tab that duplicates the tab label to improve navigation on smaller screens and for screen reader users.",
            },
            {
                "anchor": "not-yet-user-tested",
                "kind": "research",
                "title": "Not yet tested with users",
                "text": "This component has not yet been tried in user research and is based on external recommendations and examples from other services.",
            },
        ],
    },
    {
        "slug": "tag",
        "rationale": "Lets users see at a glance the current status of something that can hold more than one state, such as whether a task-list item is completed or a user is active, so they know where things stand without reading further.",
        "title": "Tag",
        "ur_text": "As a service, I use the Tag component to show users the status of something, such as an item on a task list or a phase banner.",
        "clauses": [
            {
                "anchor": "when-multiple-statuses-possible",
                "kind": "usage",
                "title": "Use when a thing can have more than one status",
                "text": "Use a tag when something can have more than one status and it is useful for the user to know which status applies.",
            },
            {
                "anchor": "status-only",
                "kind": "usage",
                "title": "Use tags only to indicate status",
                "text": "Use tags solely to indicate a status; do not repurpose them for other content.",
            },
            {
                "anchor": "not-interactive",
                "kind": "usage",
                "title": "Do not make tags interactive",
                "text": "Do not turn a tag into a link, button, or other interactive element, because users cannot tell interactive tags from non-interactive ones.",
            },
            {
                "anchor": "use-adjectives",
                "kind": "usage",
                "title": "Name tags with adjectives",
                "text": "Use adjectives (descriptive words) rather than verbs for tag names, so users do not think clicking them will do something.",
            },
            {
                "anchor": "minimise-status-count",
                "kind": "usage",
                "title": "Start with the fewest statuses",
                "text": "Start with the smallest number of statuses that might work and add more only if user research shows a need, because more tags are harder to remember.",
            },
            {
                "anchor": "single-status-sufficient",
                "kind": "usage",
                "title": "A single status can be enough",
                "text": "Where the absence of a tag implies the opposite state, a single status tag such as 'Completed' can be sufficient.",
            },
            {
                "anchor": "colour-not-alone",
                "kind": "accessibility",
                "title": "Do not convey information by colour alone",
                "text": "Do not use colour alone to convey information in a tag, to meet WCAG 2.2 success criterion 1.4.1 Use of colour.",
                "wcag": "1.4.1",
            },
            {
                "anchor": "consistent-colour",
                "kind": "accessibility",
                "title": "Keep tag colour consistent across uses",
                "text": "If the same tag is used in more than one place, keep its colour consistent.",
            },
            {
                "anchor": "colour-to-emphasise",
                "kind": "usage",
                "title": "Use colour to distinguish or emphasise",
                "text": "Use colour to help distinguish between different tags or to draw attention to an especially important tag, such as red for an 'Urgent' tag.",
            },
            {
                "anchor": "research-lowercase-text",
                "kind": "research",
                "title": "Tags no longer use uppercase text",
                "text": "Tag text was changed away from uppercase bold because research showed uppercase text can be harder to read, particularly for longer tag text.",
            },
            {
                "anchor": "research-lighter-background",
                "kind": "research",
                "title": "Tag styling changed to avoid looking like buttons",
                "text": "Tags were changed from white text on a dark background to darker text on a lighter background because research found users mistook them for buttons and tried to click them.",
            },
        ],
    },
    {
        "slug": "task-list",
        "rationale": "Gives users control over long, complex services they cannot or do not want to finish in one sitting, letting them choose their own order and clearly see which tasks are done and which remain.",
        "title": "Task list",
        "ur_text": "As a service, I use the task list component to display all the tasks a user needs to do and let them see which are done and which remain.",
        "clauses": [
            {
                "anchor": "when-long-complex-services",
                "kind": "usage",
                "title": "Use to give control over long, complex services",
                "text": "Use the task list to give users more control over how they complete long, complex services.",
            },
            {
                "anchor": "evidence-required",
                "kind": "usage",
                "title": "Only use with supporting evidence",
                "text": "Only use the task list if there is evidence that users cannot or do not want to complete all tasks in one sitting, or need to choose the order they complete tasks in.",
            },
            {
                "anchor": "simplify-first",
                "kind": "usage",
                "title": "Try to simplify the service first",
                "text": "Try to reduce the number of tasks or steps before using a task list, as you might not need one.",
            },
            {
                "anchor": "not-for-fixed-order",
                "kind": "usage",
                "title": "Do not use for strictly ordered services",
                "text": "Do not use the task list for a long service that must be completed in a specific order.",
            },
            {
                "anchor": "not-for-answers",
                "kind": "usage",
                "title": "Do not use to show users their answers",
                "text": "Do not use the task list to show users their answers; use the Summary list component for that instead.",
            },
            {
                "anchor": "any-order",
                "kind": "usage",
                "title": "Let users complete tasks in any order",
                "text": "Allow users to complete tasks in whatever order they like.",
            },
            {
                "anchor": "status-shows-startability",
                "kind": "usage",
                "title": "Status indicates whether a task can be started",
                "text": "Show a status alongside each task that indicates whether the user can start it, and update it to 'Completed' once the task is done.",
            },
            {
                "anchor": "complete-all-to-proceed",
                "kind": "usage",
                "title": "Only allow moving on when all tasks are completed",
                "text": "Only let users move on from the task list once all tasks are shown as 'Completed'.",
            },
            {
                "anchor": "task-has-name-and-status",
                "kind": "usage",
                "title": "Each task has a name and a status",
                "text": "Give each task a task name and a status, and optionally hint text where evidence shows it is needed.",
            },
            {
                "anchor": "whole-row-linked",
                "kind": "usage",
                "title": "Link the whole task row",
                "text": "Link the whole task row so users can select anywhere within it to start the task.",
            },
            {
                "anchor": "clear-short-task-names",
                "kind": "accessibility",
                "title": "Write clear, short task names in sentence case",
                "text": "Write task names that clearly convey what the task is about, in sentence case and kept short, because screen reader users find long task names hard to navigate.",
            },
            {
                "anchor": "split-complex-tasks",
                "kind": "usage",
                "title": "Split tasks that are hard to name concisely",
                "text": "If a task is difficult to name clearly and concisely, consider that it may be too complex and split it into smaller tasks.",
            },
            {
                "anchor": "hint-text-single-sentence",
                "kind": "accessibility",
                "title": "Keep hint text to one short sentence",
                "text": "Keep task hint text to a single short sentence without full stops, because screen readers read the entire text when users interact with the task link.",
            },
            {
                "anchor": "no-links-in-hint",
                "kind": "usage",
                "title": "Do not put links in hint text",
                "text": "Do not include links within task hint text, because the whole row is already linked to the task so hint-text links will not work.",
            },
            {
                "anchor": "group-with-headings",
                "kind": "usage",
                "title": "Group tasks under clear headings",
                "text": "When there are many tasks, group them into separate task lists on a page and give each group a short heading that clearly explains the grouping.",
            },
            {
                "anchor": "statuses-colour-and-text",
                "kind": "usage",
                "title": "Statuses use colour and a short descriptor",
                "text": "Give statuses colour and a short descriptor so users get a quick overview of how much of the task list is complete.",
            },
            {
                "anchor": "research-whole-row-linked",
                "kind": "research",
                "title": "Statuses redesigned and rows linked after feedback",
                "text": "Statuses were redesigned to look less like buttons and the whole row was linked because user feedback showed some users tried to select statuses thinking they were buttons or links.",
            },
            {
                "anchor": "research-sentence-case-statuses",
                "kind": "research",
                "title": "Statuses moved to sentence case for readability",
                "text": "Statuses were changed to sentence case and 'Completed' to black text with no background because uppercase made them harder to read and harder to scan for incomplete tasks.",
            },
            {
                "anchor": "research-known-gaps",
                "kind": "research",
                "title": "Component still needs user testing",
                "text": "This component still needs user testing of assumptions including whether linking the whole row outweighs accidental-click risk, whether status contrast is sufficient, and whether the status wording makes sense to users.",
            },
        ],
    },
    {
        "slug": "textarea",
        "rationale": "Lets users provide answers longer than a single line, giving space for detailed free-text information that would not fit in a standard single-line input field.",
        "title": "Textarea",
        "ur_text": "As a service, I use the textarea component to let users enter an amount of text that is longer than a single line.",
        "clauses": [
            {
                "anchor": "when-multiline",
                "kind": "usage",
                "title": "Use for text longer than a single line",
                "text": "Use the textarea component when you need to let users enter text that is longer than a single line.",
            },
            {
                "anchor": "consider-simpler-questions",
                "kind": "usage",
                "title": "Consider breaking up open-ended questions",
                "text": "Because users find open-ended questions hard to answer, consider breaking one complex question into simpler ones, for example using radios.",
            },
            {
                "anchor": "not-for-short-answers",
                "kind": "usage",
                "title": "Do not use for single-line answers",
                "text": "Do not use the textarea for answers no longer than a single line such as a phone number or name; use the Text input component instead.",
            },
            {
                "anchor": "must-label",
                "kind": "accessibility",
                "title": "Always label the textarea",
                "text": "Label every textarea; placeholder text is not a suitable substitute for a label because it disappears when users click inside the textarea.",
            },
            {
                "anchor": "label-position-and-style",
                "kind": "usage",
                "title": "Align labels above and use sentence case",
                "text": "Align labels above the textarea they refer to, keep them short and direct, write them in sentence case, and do not end them with colons.",
            },
            {
                "anchor": "size-proportional",
                "kind": "usage",
                "title": "Size the textarea to expected input",
                "text": "Make the height of a textarea proportional to the amount of text expected, setting it via the rows attribute.",
            },
            {
                "anchor": "allow-copy-paste",
                "kind": "usage",
                "title": "Do not disable copy and paste",
                "text": "Do not stop users copying and pasting into a textarea, as they often need to do so.",
            },
            {
                "anchor": "label-not-heading-multi-question",
                "kind": "usage",
                "title": "Label is not the page heading with multiple questions",
                "text": "If asking more than one question on the page, do not set the label as the page heading.",
            },
            {
                "anchor": "limit-via-character-count",
                "kind": "usage",
                "title": "Limit character count with the right component",
                "text": "If there is a good reason to limit the number of characters, use the Character count component.",
            },
            {
                "anchor": "specific-error-messages",
                "kind": "usage",
                "title": "Use specific error messages per state",
                "text": "Follow the Error message component guidance and provide specific error messages for specific error states, such as 'Enter [thing]' when empty or '[thing] must be [number] characters or less' when too long.",
            },
        ],
    },
    {
        "slug": "text-input",
        "rationale": "Lets users enter short, single-line information such as a name or phone number, providing an appropriately sized field so they understand what is expected without spanning multiple lines.",
        "title": "Text input",
        "ur_text": "As a service, I use the text input component to let users enter text no longer than a single line, such as their name or phone number.",
        "clauses": [
            {
                "anchor": "when-single-line",
                "kind": "usage",
                "title": "Use for single-line text",
                "text": "Use the text input component when you need to let users enter text no longer than a single line, such as their name or phone number.",
            },
            {
                "anchor": "not-for-multiline",
                "kind": "usage",
                "title": "Do not use for multi-line answers",
                "text": "Do not use the text input for longer answers that might span multiple lines; use the Textarea component instead.",
            },
            {
                "anchor": "must-have-labels",
                "kind": "accessibility",
                "title": "All inputs must have labels",
                "text": "Give every text input a label, and in most cases keep the label visible.",
            },
            {
                "anchor": "label-position-and-style",
                "kind": "usage",
                "title": "Align labels above and use sentence case",
                "text": "Align labels above the input they refer to, keep them short and direct, write them in sentence case, and do not end them with colons.",
            },
            {
                "anchor": "avoid-placeholder",
                "kind": "accessibility",
                "title": "Avoid placeholder text",
                "text": "Do not use placeholder text in place of a label, hint, or example, because it vanishes on typing, is not always read by screen readers, and its default styling often fails WCAG 2.2 success criterion 1.4.3 Contrast (minimum).",
                "wcag": "1.4.3",
            },
            {
                "anchor": "label-as-heading-single-question",
                "kind": "accessibility",
                "title": "Use label as heading for one question per page",
                "text": "If asking just one question per page, set the label as the page heading so screen reader users only hear the contents once.",
            },
            {
                "anchor": "label-not-heading-multi-question",
                "kind": "usage",
                "title": "Label is not the page heading with multiple questions",
                "text": "If asking more than one question on the page, do not set the label as the page heading.",
            },
            {
                "anchor": "size-to-content",
                "kind": "usage",
                "title": "Size inputs to the expected content",
                "text": "Make text inputs the right size for the content intended, using fixed-width inputs for content of known length and width override classes for smaller fluid inputs.",
            },
            {
                "anchor": "hint-text-use",
                "kind": "usage",
                "title": "Use hint text for widely relevant help",
                "text": "Use hint text for help relevant to the majority of users, keeping it to a single short sentence without full stops.",
            },
            {
                "anchor": "no-links-in-hint",
                "kind": "accessibility",
                "title": "Do not put links in hint text",
                "text": "Do not include links within hint text, because screen readers read the link text without telling users it is a link.",
            },
            {
                "anchor": "hint-not-for-long-text",
                "kind": "accessibility",
                "title": "Do not use hint text for long explanations",
                "text": "Do not use hint text for anything longer than a short simple sentence, because screen readers read the entire text when users interact with the field.",
            },
            {
                "anchor": "inputmode-numeric",
                "kind": "usage",
                "title": "Set inputmode numeric for whole numbers",
                "text": "When asking for a whole number, set the inputmode attribute to numeric so devices with on-screen keyboards show the numeric keypad.",
            },
            {
                "anchor": "inputmode-decimal",
                "kind": "usage",
                "title": "Set inputmode decimal for decimals",
                "text": "When asking for a number that might include decimals, set inputmode to decimal to show a numeric keypad with a decimal separator.",
            },
            {
                "anchor": "avoid-type-number",
                "kind": "usage",
                "title": "Avoid input type number",
                "text": "Do not use input type number unless user research shows a need, because users can accidentally increment values and get no feedback on invalid entries.",
            },
            {
                "anchor": "separate-code-characters",
                "kind": "usage",
                "title": "Visually separate characters in codes",
                "text": "Style the input to visually separate each character when asking for an unmemorised code or sequence such as a reference ID, account number, or security code, but not for memorable information like phone numbers and postcodes.",
            },
            {
                "anchor": "prefix-suffix-not-alone",
                "kind": "accessibility",
                "title": "Do not rely on prefixes or suffixes alone",
                "text": "Do not rely on prefixes or suffixes alone because screen readers do not read them out; also state the required information in the label or hint.",
            },
            {
                "anchor": "prefix-suffix-outside",
                "kind": "usage",
                "title": "Position prefixes and suffixes outside the input",
                "text": "Position prefixes and suffixes outside the input to avoid interfering with browser-inserted icons, and allow for users who enter the prefix or suffix into the input without showing an error.",
            },
            {
                "anchor": "autocomplete-attribute",
                "kind": "accessibility",
                "title": "Use the autocomplete attribute",
                "text": "Use the autocomplete attribute to specify an input's purpose so browsers can autofill; in production with a relevant input purpose this is needed to meet WCAG 2.2 success criterion 1.3.5 Identify input purpose.",
                "wcag": "1.3.5",
            },
            {
                "anchor": "allow-copy-paste",
                "kind": "usage",
                "title": "Do not disable copy and paste",
                "text": "Do not stop users copying and pasting into a text input, as they often need to do so.",
            },
            {
                "anchor": "avoid-maxlength",
                "kind": "accessibility",
                "title": "Avoid restricting input length",
                "text": "Avoid using the maxlength attribute because it truncates without feedback and is not reliably announced by assistive technologies; if a maximum is technically required, state it in the hint, allow more input, and only error after normalisation.",
            },
            {
                "anchor": "spellcheck-control",
                "kind": "usage",
                "title": "Disable spellcheck where inappropriate",
                "text": "Set spellcheck to false for information not appropriate to spellcheck such as reference numbers, names, email addresses, or National Insurance numbers, and to true where spellcheck would help.",
            },
            {
                "anchor": "specific-error-messages",
                "kind": "usage",
                "title": "Use specific error messages per state",
                "text": "Follow the Error message component guidance and provide specific error messages for specific states, such as 'Enter [thing]' when empty or '[thing] must be a number, like 30' when not a number.",
            },
            {
                "anchor": "support-needed-characters",
                "kind": "usage",
                "title": "Support all characters the user needs",
                "text": "Support all characters the user might need to enter, including numbers and symbols.",
            },
            {
                "anchor": "research-input-type-number",
                "kind": "research",
                "title": "Problems found with input type number",
                "text": "Research documented in a blog post surfaced the problems the team discovered with input type number.",
            },
            {
                "anchor": "research-prefix-clicking",
                "kind": "research",
                "title": "Some users clicked on prefixes",
                "text": "Although the prefix and suffix design tested well across services, some users were observed clicking on prefixes assuming it would do something.",
            },
        ],
    },
    {
        "slug": "warning-text",
        "rationale": "Draws users' attention to something genuinely important, such as the legal consequences of an action or inaction, so they do not overlook a critical warning before deciding what to do.",
        "title": "Warning text",
        "ur_text": "As a service, I use the warning text component to warn users about something important, such as legal consequences of an action or inaction.",
        "clauses": [
            {
                "anchor": "when-important-warning",
                "kind": "usage",
                "title": "Use to warn about something important",
                "text": "Use the warning text component when you need to warn users about something important, such as the legal consequences of an action or lack of action they might take.",
            },
            {
                "anchor": "rewrite-hidden-text",
                "kind": "accessibility",
                "title": "Adapt the hidden text to context",
                "text": "Rewrite the visually hidden text (for example 'Warning') where needed to make it appropriate for your context.",
            },
        ],
    },
    {
        "slug": "generic-header",
        "rationale": "Signals to users that a public-facing government service sits outside the GOV.UK website, maintaining trust and consistency across journeys while ensuring non-GOV.UK services do not misuse GOV.UK branding.",
        "title": "Generic header",
        "ur_text": "As a service, I use the Generic header component to tell users they are using a government service that is not part of the GOV.UK website.",
        "clauses": [
            {
                "anchor": "when-non-govuk-public-service",
                "kind": "usage",
                "title": "Use for public services not on GOV.UK",
                "text": "Use the Generic header component only if your service is both a public-facing government service and not on the GOV.UK website (not part of the GOV.UK proposition).",
            },
            {
                "anchor": "maintain-trust-consistency",
                "kind": "usage",
                "title": "Bring consistency across cross-government journeys",
                "text": "Use the Generic header to bring consistency and maintain user trust in journeys that move between the GOV.UK website and other government websites and services.",
            },
            {
                "anchor": "no-govuk-branding",
                "kind": "usage",
                "title": "Do not use GOV.UK branding in the header",
                "text": "Ensure the header does not identify the service as part of GOV.UK, and does not use the crown or GOV.UK logotype, the GDS Transport typeface, or the GOV.UK brand colours.",
            },
            {
                "anchor": "not-for-govuk-domains",
                "kind": "usage",
                "title": "Do not use on gov.uk domains",
                "text": "Do not use the Generic header if your service is hosted on a gov.uk domain such as gov.uk/[myservice], [myservice].service.gov.uk, or [myblog].blog.gov.uk; use the GOV.UK header component instead.",
            },
            {
                "anchor": "replace-in-page-template",
                "kind": "usage",
                "title": "Replace the default header in the page template",
                "text": "If using the page template, replace the default GOV.UK header with the Generic header component, and follow the guidance to remove other GOV.UK brand elements elsewhere in your service.",
            },
            {
                "anchor": "own-brand-elements",
                "kind": "usage",
                "title": "Display your own brand logo, link, and font",
                "text": "Use the Generic header to display your own brand logo, homepage link, and service-name font instead of GDS Transport.",
            },
            {
                "anchor": "accessible-logo",
                "kind": "accessibility",
                "title": "Make the brand logo accessible and optimised",
                "text": "Follow your organisation's guidelines and the Design System image guidance to make your brand logo as accessible and optimised as possible.",
            },
            {
                "anchor": "customise-homepage-link",
                "kind": "usage",
                "title": "Customise the homepage link",
                "text": "Customise the homepage link, which defaults to '/', to point wherever makes the most sense for your service.",
            },
            {
                "anchor": "no-navigation-links",
                "kind": "usage",
                "title": "Do not show navigation links in the header",
                "text": "Do not use the Generic header to show navigation links; use the Service navigation component instead.",
            },
        ],
    },
]
