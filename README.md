# ui-kit

A small, framework-free house style for my projects: design tokens and components in plain CSS, with HTML examples and a Streamlit theme. It borrows the component, accessibility and content patterns of the [GOV.UK Design System](https://design-system.service.gov.uk/), but not its branding or look.

Status: phase 1 (design tokens) done; components arrive in phase 2. Not released yet.

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

## Tokens
`ui-kit.css` currently holds the design tokens (colours for light and dark, spacing, type, radius, shadow, focus, breakpoints) and a minimal base layer. Every token starts with `--jm-`; classes will start with `jm-`.

- Use the semantic colour tokens (`--jm-colour-text`, `--jm-colour-accent`, `--jm-colour-error-text`, ...), not the palette tokens (`--jm-blue-600`, ...).
- The theme follows the operating system. Force one with `data-theme="light"` or `data-theme="dark"` on `<html>`.
- Everything is in cascade layers (`jm.tokens`, `jm.base`, `jm.components`, `jm.utilities`), so your own CSS overrides the kit without `!important`.

See the token sheet: open `examples/index.html` in a browser, or run `python3 -m http.server` in the repository root and visit `http://localhost:8000/examples/` (palette names on the swatches only appear when served over HTTP).

## Checks
```bash
python3 tests/check_contrast.py
```
Checks every text and background pair for at least 4.5:1 contrast, and borders, focus rings and status marks for at least 3:1, in both themes (WCAG 2.2 AA). Python 3 standard library only.

## Using it (once released)
Copy the tagged `ui-kit.css` (and optionally `ui-kit.js`) into your project, for example `static/ui-kit/`. The version is in the file's header comment.

## Licence
MIT. See [LICENSE](LICENSE).
