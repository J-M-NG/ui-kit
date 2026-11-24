# ui-kit

A small, framework-free house style for my projects: design tokens and components in plain CSS, with HTML examples and a Streamlit theme. It borrows the component, accessibility and content patterns of the [GOV.UK Design System](https://design-system.service.gov.uk/), but not its branding or look.

Status: phase 3 dashboard patterns and portfolio on GitHub Pages; phase 4 (Streamlit theme, helpers, component-request workflow) pending merge. Not released yet (no git tag).

## Planned contents
- `ui-kit.css`: design tokens (CSS custom properties) and component classes in cascade layers.
- `ui-kit.js`: optional, dependency-free behaviour (for example sortable tables). Every component works without it.
- `examples/`: pages showing every component and state; they are the documentation and the accessibility test target.
- `streamlit/`: [`config.toml`](streamlit/config.toml) theme (copy to `.streamlit/config.toml`), [`helpers.py`](streamlit/helpers.py) for tags and figures via `st.html`; see [streamlit/README.md](streamlit/README.md).
- [`COMPONENT_REQUESTS.md`](COMPONENT_REQUESTS.md): backlog when adopting projects need a pattern the kit does not ship yet.

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

## Streamlit

Copy `streamlit/config.toml` to your app’s `.streamlit/config.toml`, load `ui-kit.css` in the app, and use `streamlit/helpers.py` for `jm-tag`, `jm-figures` and `jm-summary-list` HTML. Full steps and a code sample are in [streamlit/README.md](streamlit/README.md).

When a Streamlit layout needs a pattern that is not in the kit, log it in [COMPONENT_REQUESTS.md](COMPONENT_REQUESTS.md) and build an interim `jm-` solution with kit tokens (see root `CLAUDE.md`).

## Dashboard examples

Open `examples/dashboard.html` for the dashboard patterns: sidebar layout, panel, key figures, sortable and filterable table, trail of events, bar chart and sparkline, and empty, loading and error states. Sorting and filtering need the optional `ui-kit.js` (`<script src="ui-kit.js"></script>`); the table works without it.

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

## Live examples (GitHub Pages)

The portfolio walkthrough is static HTML at the repository root and in `examples/`. After merging to `main`, enable Pages once:

1. Open the repository on GitHub → **Settings** → **Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose branch **`main`**, folder **`/ (root)`**, then **Save**.

The site will be at [https://j-m-ng.github.io/ui-kit/](https://j-m-ng.github.io/ui-kit/) (root `index.html` links to the three chapters under `examples/`). A `.nojekyll` file at the root tells GitHub not to run Jekyll, so paths like `ui-kit.css` are served as-is.

Locally, run `python3 -m http.server` in the repository root and open `http://localhost:8000/`.

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
