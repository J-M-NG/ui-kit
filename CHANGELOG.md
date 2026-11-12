# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Phase 2 components in a `jm.components` layer: buttons (primary, secondary, warning, disabled), text input (with widths), textarea, select, checkboxes and radios, fields with hint and error message, date input, error summary, summary list, status tags, notification banners, table, details, skip link, header, footer, page layout (`jm-page`, `jm-container`, `jm-stack`, `jm-cluster`).
- `jm.utilities` layer: `jm-visually-hidden`, `jm-num`, `jm-secondary-text`.
- Project hooks: `--jm-radius-scale`, `--jm-font-family-heading`, and accent colour overrides; `tests/check_contrast.py --project` checks a project's overrides.
- `examples/components.html`.
- `tests/a11y.mjs` (axe-core in Playwright, both themes, two widths) and `npm test`.
- `ui-kit.css` design tokens: palette; semantic colours for light and dark themes (surfaces, text, borders, accent, links, focus, success, warning, error, info); spacing, type, radius, shadow, focus ring, breakpoint and motion tokens. All prefixed `--jm-`, in cascade layers `jm.tokens`, `jm.base`, `jm.components`, `jm.utilities`.
- Minimal base layer: body font and colours, headings, links, `:focus-visible` ring, `[hidden]` fix.
- `examples/index.html` token sheet with a light, dark and system theme switch.
- `tests/check_contrast.py` contrast check (WCAG 2.2 AA) over 64 token pairs per theme.
- Repository setup: `README.md`, `LICENSE` (MIT), `CLAUDE.md` pointing to the vault project notes, `.claude/` agent configuration.

### Changed
- Token sheet status examples use a full border instead of a coloured left edge.
