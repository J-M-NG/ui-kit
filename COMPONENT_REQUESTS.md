# Component requests

When an adopting project needs UI that is not in the kit yet, log it here so the ui-kit backlog can pick it up. Vault context lives in `J-M-NG/obsidian-vault` at `01-Projects/ui-kit/` (especially `tasks.md` and this file’s twin note `component-requests.md`).

## How to add a row

1. Build a sensible interim pattern in the project using kit tokens and BEM-like `jm-` class names where possible.
2. Append a row below (newest first).
3. Mention the gap in the project session; if the vault is attached, add a matching line to `01-Projects/ui-kit/component-requests.md` or `tasks.md`.

| Date | Project | What is needed | Interim class / markup | Priority | Status |
|------|---------|----------------|------------------------|----------|--------|
| _YYYY-MM-DD_ | _project-name_ | _Short description of the missing pattern_ | _e.g. `.jm-project-timeline` on `<ol class="jm-trail">` with extra spacing_ | low / medium / high | open / done |
| 2026-11-24 | ui-kit v1 | Breadcrumbs, pagination, tabs, card, dialog | Shipped as `.jm-breadcrumbs`, `.jm-pagination`, `.jm-tabs`, `.jm-card`, `.jm-dialog` in v1.0.0 | medium | done |