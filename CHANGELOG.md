# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

No version has been tagged yet. Earlier drafts of this file listed 1.0.1 and 1.1.0 as separate releases on the same day; they were never tagged, so their changes are folded into 1.0.0 below. Tag `v1.0.0` on the commit you want to freeze.

## [Unreleased]

### Changed
- Fonts: headings use Source Serif 4 and everything else uses Source Sans 3, both self-hosted from the new `fonts/` folder (SIL Open Font License 1.1, variable WOFF2, Latin and Latin Extended). They replace system stacks that gave a different, poorly matched pairing on each operating system. Copy `fonts/` next to `ui-kit.css`; without it the tokens fall back to system fonts. Loading avoids layout shift: body text uses `font-display: swap` and headings `optional`; fallback faces (`"Source Sans 3 Fallback"`, `"Source Serif 4 Fallback"`) map Arial and Georgia onto Source's metrics with `size-adjust` and ascent, descent and line-gap overrides; the documentation pages preload the two Latin files. The variable files cover weights 200 to 900, so no weight is synthesised. `presets/minimal-square.css` now sets headings to `var(--jm-font-family)`, and the Streamlit theme sets `headingFont = "serif"` (Streamlit's built-in Source Serif).
- Surfaces: the page sits on `--jm-colour-background` (grey-50 in light) and `jm-panel`, `jm-card`, `jm-dialog` and the header sit on `--jm-colour-surface`, so raised content reads as raised in both themes. Table headers use a rule instead of a filled band; the information banner uses its own tint like the other banners; hover states use `--jm-colour-surface-sunken`.
- Type: one pairing rule. Serif (`--jm-font-family-heading`) for h1 to h3 only; h4, panel, card, dialog, caption, chart, error-summary and empty-state titles use the system sans at semibold. Headings use weight 600 (new token `--jm-font-weight-semibold`) with milder tracking; h1 scales from 2rem on phones to 2.75rem. The heading stack now ends in Noto Serif and DejaVu Serif instead of a generic serif.
- Key figures use tabular sans figures instead of monospace; numeric table headers are no longer monospace (cells still are).
- Tabs mark the selected tab with an accent underline, so they work on any surface.
- `jm-empty` centres its content properly. Buttons placed directly in a `jm-stack` keep their own width.
- Header: on phones the navigation takes its own row under the name; nav links are smaller.
- Secondary buttons are transparent, so they sit correctly on any surface.

### Removed
- `jm-empty--pattern` and `jm-loading--blocks` (never tagged): they rendered as broken-looking boxes. Use plain `jm-empty` and `jm-loading`.
- `presets/default-serif.css`, which only restated the defaults. `presets/matt-warm.css` is renamed `presets/teal.css` and its dark hover now uses a palette colour.

### Fixed
- Documentation site: one shared header with a compact theme switch on every page (`examples/site.css`, `examples/site.js`); the chosen theme now persists across all pages, including Composition and Content style.
- Portfolio rebuilt: panels had no inner padding, and the identity block, "signature" bar, placeholder metrics and duplicate links were removed. The hooks demo now really is scoped to its preview (radius and heading font previously changed the whole page).
- Foundation type scale shows the actual heading face and sizes; status samples match the banners.
- Streamlit `chartCategoricalColors` matches `--jm-colour-chart-1` again; README claims about tests corrected.

## [1.0.0] - not tagged

### Added
- Tokens: palette; semantic colours for light and dark themes (surfaces, text, borders, accent, links, focus, success, warning, error, info); chart series (`--jm-colour-chart-1` to `-5`, `-other`) and a five-step sequential heat scale; spacing, type, radius, shadow, focus ring, breakpoint and motion tokens. All prefixed `--jm-`, in cascade layers `jm.tokens`, `jm.base`, `jm.components`, `jm.utilities`.
- Project hooks: `--jm-radius-scale`, `--jm-font-family-heading` and the accent colour tokens; `tests/check_contrast.py --project` checks a project's overrides. Optional presets in `presets/`.
- Components: buttons (primary, secondary, warning, disabled), text input (with widths), textarea, select, checkboxes and radios, fields with hint and error message, date input, error summary, summary list, status tags, notification banners, table, details, skip link, header, footer, breadcrumbs, pagination, tabs, card, dialog; layout (`jm-page`, `jm-container`, `jm-stack`, `jm-cluster`).
- Dashboard patterns: sidebar layout (`jm-app`, `jm-sidenav`), panel, key figures, filter bar, sortable table headers, trail, bar chart, line chart, heat cells, sparkline, empty and loading states, warning and error banners.
- Utilities: `jm-visually-hidden`, `jm-num`, `jm-secondary-text`.
- Optional `ui-kit.js` (no dependencies): sortable tables, table filter, tabs, dialog opening. Everything works without it.
- Streamlit: `streamlit/config.toml`, `streamlit/helpers.py` and adoption notes.
- Documentation: `index.html` and the Foundation, Components, Composition and Content style chapters in `examples/`.
- Checks: `npm test` runs the contrast check (186 pairs), Streamlit helper tests and axe-core on every page in light and dark at 1280px and 375px; GitHub Actions runs it on every push and pull request. Pull request template with an accessibility checklist.
- `COMPONENT_REQUESTS.md` and `CLAUDE.md` guidance for logging missing `jm-` patterns. MIT licence, copyright Matt Ng.
