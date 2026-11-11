# ui-kit

A small, framework-free house style for my projects: design tokens and components in plain CSS, with HTML examples and a Streamlit theme. It borrows the component, accessibility and content patterns of the [GOV.UK Design System](https://design-system.service.gov.uk/), but not its branding or look.

Status: phase 0 (repository setup). Nothing is ready to use yet.

## Planned contents
- `ui-kit.css`: design tokens (CSS custom properties) and component classes in cascade layers.
- `ui-kit.js`: optional, dependency-free behaviour (for example sortable tables). Every component works without it.
- `examples/`: pages showing every component and state; they are the documentation and the accessibility test target.
- `streamlit/`: a theme and small helpers so Streamlit dashboards match.

## Principles
- WCAG 2.2 AA: text contrast at least 4.5:1, visible focus, keyboard-only use, works at 400% zoom.
- Semantic HTML first; classes style it, they do not replace it.
- No build step, no npm, no framework.
- System font stack; light and dark themes from the same tokens.

## Using it (once released)
Copy the tagged `ui-kit.css` (and optionally `ui-kit.js`) into your project, for example `static/ui-kit/`. The version is in the file's header comment.

## Licence
MIT. See [LICENSE](LICENSE).
