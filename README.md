# ui-kit

![test](https://github.com/J-M-NG/ui-kit/actions/workflows/test.yml/badge.svg)

The CSS I use for forms, tables and dashboards across my projects. It's one stylesheet with no framework and no build step, plus an optional script and a Streamlit theme. Colours pass WCAG 2.2 AA contrast in light and dark. Projects can change the accent colour, heading font and corner radius; everything else is shared.

**Status:** 1.0.0, not yet tagged. Until a release is tagged, copy `ui-kit.css` from a specific commit on `main` so your copy does not move under you. Documentation site: [https://j-m-ng.github.io/ui-kit/](https://j-m-ng.github.io/ui-kit/).

## What's in the repo
- `ui-kit.css`: tokens, base styles and `jm-` components in cascade layers.
- `fonts/`: Source Serif 4 and Source Sans 3 as variable WOFF2 files (about 400 KB in total, browsers only download the subsets a page uses), with their SIL Open Font Licences.
- `ui-kit.js`: optional script for sortable tables, filters, tabs and dialogs.
- `index.html`: documentation home with a live project-hooks demo.
- `examples/`: Foundation, Components, Composition and Content style chapters (also the axe test targets). `examples/site.css` and `site.js` are the documentation site's own chrome (theme switch, example frames), not part of the kit.
- `presets/`: optional hook-only stylesheets ([`presets/README.md`](presets/README.md)).
- `streamlit/`: [`config.toml`](streamlit/config.toml), [`helpers.py`](streamlit/helpers.py); see [streamlit/README.md](streamlit/README.md).
- [`COMPONENT_REQUESTS.md`](COMPONENT_REQUESTS.md): backlog for patterns not in the kit yet.

## Adopt the kit
1. Copy `ui-kit.css` and the `fonts/` folder (and optionally `ui-kit.js`) into your project, e.g. `static/ui-kit/`. Keep `fonts/` next to `ui-kit.css`; without it the kit falls back to system fonts.
2. Link the stylesheet before your project CSS, and preload the two fonts used above the fold so headings get the real face on a first visit:

   ```html
   <link rel="preload" href="/static/ui-kit/fonts/source-sans-3-latin.woff2" as="font" type="font/woff2" crossorigin>
   <link rel="preload" href="/static/ui-kit/fonts/source-serif-4-latin.woff2" as="font" type="font/woff2" crossorigin>
   <link rel="stylesheet" href="/static/ui-kit/ui-kit.css">
   ```

   Body text swaps in when its font arrives; headings use `font-display: optional` and keep the fallback if the font is late, so they never re-wrap after first paint. Fallback faces matched to Source's widths keep text in place while it loads.
3. Optionally link a [preset](presets/README.md) after `ui-kit.css`, or override only the [documented hooks](#project-hooks).
4. Run `python3 tests/check_contrast.py --project path/to/project.css` when changing colours.

## Principles
- WCAG 2.2 AA: contrast, visible focus, keyboard use, 400% zoom.
- Semantic HTML first; classes style real elements.
- No build step, no framework, no third-party font requests; OS-driven light and dark themes.
- Type: Source Serif 4 for page and section headings (h1 to h3), Source Sans 3 for everything else; system monospace only for code, ids, timestamps and table numbers. The two Source faces were drawn as companions, so they share proportions and x-height.
- Copy follows [`examples/content-style.html`](examples/content-style.html).

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
  --jm-font-family-heading: var(--jm-font-family); /* sans headings */
  --jm-colour-accent: #0b6e8f;
  --jm-colour-accent-hover: #095a75;
  --jm-colour-link: #0b6e8f;
  --jm-colour-focus: #095a75;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --jm-colour-accent: #5fb6d6;
    --jm-colour-accent-hover: #e8f5fa;
    --jm-colour-link: #5fb6d6;
    --jm-colour-focus: #5fb6d6;
  }
}
:root[data-theme="dark"] {
  --jm-colour-accent: #5fb6d6;
  --jm-colour-accent-hover: #e8f5fa;
  --jm-colour-link: #5fb6d6;
  --jm-colour-focus: #5fb6d6;
}
```

Set every accent token in both themes, as above. [`index.html`](index.html) has a live demo of all three hooks.

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