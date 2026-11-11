# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- `ui-kit.css` design tokens: palette; semantic colours for light and dark themes (surfaces, text, borders, accent, links, focus, success, warning, error, info); spacing, type, radius, shadow, focus ring, breakpoint and motion tokens. All prefixed `--jm-`, in cascade layers `jm.tokens`, `jm.base`, `jm.components`, `jm.utilities`.
- Minimal base layer: body font and colours, headings, links, `:focus-visible` ring, `[hidden]` fix.
- `examples/index.html` token sheet with a light, dark and system theme switch.
- `tests/check_contrast.py` contrast check (WCAG 2.2 AA) over 64 token pairs per theme.
- Repository setup: `README.md`, `LICENSE` (MIT), `CLAUDE.md` pointing to the vault project notes, `.claude/` agent configuration.
