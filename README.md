# ui-kit

A small, framework-free house style for my projects: design tokens and components in plain CSS, with HTML examples and a Streamlit theme. It borrows the component, accessibility and content patterns of the [GOV.UK Design System](https://design-system.service.gov.uk/), but not its branding or look.

Status: phase 2 (core components) done; dashboard patterns arrive in phase 3. Not released yet.

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

## Components
Open `examples/components.html` to see every component in each state, with the classes to use. Phase 2 covers buttons, text input, textarea, select, checkboxes, radios, fields with hints and errors, date input, error summary, summary list, status tags, notification banners, tables, details, and page layout (skip link, header, footer, container, stack, cluster). Every class starts with `jm-` and styles a real HTML element.

## Project hooks
A project may change only these, in its own stylesheet loaded after `ui-kit.css`:

```css
/* project.css */
:root {
  --jm-radius-scale: 0;                 /* 0 = square corners, 1 = default */
  --jm-font-family-heading: Georgia, serif; /* optional heading face */
  --jm-colour-accent: #0b6e8f;
  --jm-colour-accent-hover: #095a75;
  --jm-colour-link: #0b6e8f;
  --jm-colour-focus: #095a75;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --jm-colour-accent: #5fb6d6; --jm-colour-link: #5fb6d6; }
}
:root[data-theme="dark"] { --jm-colour-accent: #5fb6d6; --jm-colour-link: #5fb6d6; }
```

Check a project's colours with `python3 tests/check_contrast.py --project path/to/project.css`.

## Checks
```bash
python3 tests/check_contrast.py
```
Checks every text and background pair for at least 4.5:1 contrast, and borders, focus rings and status marks for at least 3:1, in both themes (WCAG 2.2 AA). Python 3 standard library only.

```bash
npm install
npm test
```
Runs the contrast check, then [axe-core](https://github.com/dequelabs/axe-core) (WCAG 2.0 to 2.2, A and AA) on every page in `examples/`, in light and dark, at 1280px and 375px, and fails if a page scrolls sideways. Node and npm are for these checks only; using the kit needs neither.

Automated checks catch only part of the problem. Before a release, also tab through `examples/components.html` with the keyboard only, and try it at 400% zoom.

## Using it (once released)
Copy the tagged `ui-kit.css` (and optionally `ui-kit.js`) into your project, for example `static/ui-kit/`. The version is in the file's header comment.

## Licence
MIT. See [LICENSE](LICENSE).
