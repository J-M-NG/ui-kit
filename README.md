# ui-kit

![test](https://github.com/J-M-NG/ui-kit/actions/workflows/test.yml/badge.svg)

A small, framework-free house style for my projects: design tokens and components in plain CSS, with HTML examples and a Streamlit theme. Accessible patterns (semantic HTML, error summaries, visible focus) with a calm product voice — serif headings, flat buttons, cool grey and blue tokens you can override with hooks.

**Status:** v1.0.1 (phases 0–4 complete). Portfolio at [https://j-m-ng.github.io/ui-kit/](https://j-m-ng.github.io/ui-kit/). Copy `ui-kit.css` from the latest [release tag](https://github.com/J-M-NG/ui-kit/releases).

## What's in the repo
- `ui-kit.css` — tokens, base styles and `jm-` components in cascade layers.
- `ui-kit.js` — optional behaviour: sortable tables, filters, tabs, dialogs.
- `index.html` — portfolio hero with theme toggle and live project-hooks demo.
- `examples/` — Foundation, Components and Composition chapters (documentation and axe targets).
- `streamlit/` — [`config.toml`](streamlit/config.toml), [`helpers.py`](streamlit/helpers.py); see [streamlit/README.md](streamlit/README.md).
- [`COMPONENT_REQUESTS.md`](COMPONENT_REQUESTS.md) — backlog for patterns not in the kit yet.

## Adopt the kit
1. Copy `ui-kit.css` (and optionally `ui-kit.js`) into your project, e.g. `static/ui-kit/`.
2. Link the stylesheet before your project CSS.
3. Override only the [documented hooks](#project-hooks) if you need a distinct accent, heading face or corner radius.
4. Run `python3 tests/check_contrast.py --project path/to/project.css` when changing colours.

## Principles
- WCAG 2.2 AA: contrast, visible focus, keyboard use, 400% zoom.
- Semantic HTML first; classes style real elements.
- No build step, no framework; system body type and distinctive heading face by default; OS-driven light/dark themes.
- Example copy uses product and dashboard language — borrow patterns, not tone.

## Tokens
Use semantic tokens (`--jm-colour-text`, `--jm-colour-accent`, …), not palette steps (`--jm-blue-600`, …). Force a theme with `data-theme` on `<html>`, or follow the OS default.

Open [`examples/index.html`](examples/index.html) for the token sheet with swatches (serve the repo over HTTP so palette names resolve).

## Components
[`examples/components.html`](examples/components.html) documents buttons, forms, feedback, tables, layout, **breadcrumbs**, **pagination**, **tabs**, **cards**, **dialogs**, and more.

[`examples/dashboard.html`](examples/dashboard.html) shows composition patterns (panels, figures, charts, trails). Sort/filter needs `ui-kit.js`.

## Streamlit
Copy `streamlit/config.toml` to `.streamlit/config.toml`, load `ui-kit.css`, use `helpers.py` for tags and figures. See [streamlit/README.md](streamlit/README.md).

## Project hooks
In your own stylesheet loaded **after** `ui-kit.css`:

```css
:root {
  --jm-radius-scale: 0;
  --jm-font-family-heading: system-ui, sans-serif;
  --jm-colour-accent: #0b6e8f;
  --jm-colour-accent-hover: #095a75;
  --jm-colour-link: #0b6e8f;
  --jm-colour-focus: #095a75;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --jm-colour-accent: #5fb6d6;
    --jm-colour-link: #5fb6d6;
  }
}
:root[data-theme="dark"] {
  --jm-colour-accent: #5fb6d6;
  --jm-colour-link: #5fb6d6;
}
```

The portfolio [`index.html`](index.html) includes a live hooks demo (accent, radius, heading font).

## Checks
```bash
npm install
npm test
```
Runs contrast pairs, Streamlit helper smoke tests, and axe on the portfolio and every example page (light/dark, desktop/phone).

```bash
python3 tests/check_contrast.py
```

## Licence
MIT. See [LICENSE](LICENSE) (copyright Matt Ng).