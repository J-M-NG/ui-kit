# UI kit

Framework-free house style: one CSS file of design tokens and components, HTML examples, optional dependency-free JavaScript and a Streamlit theme. No build step; projects copy tagged files.

## Project memory
Long-term memory for this project lives in the `J-M-NG/obsidian-vault` repository at
`01-Projects/ui-kit/`. If that repository is attached to the session:
- Read its `CLAUDE.md`, then `01-Projects/ui-kit/README.md`, `tasks.md`, `tech.md` and recent `log.md` entries before starting.
- At the end of the session, update `log.md`, `tasks.md` and `decisions.md` there, then commit and push the vault.
If it is not attached, ask whether to attach it.

## Missing kit components
When building a UI and no `jm-` class exists in `ui-kit.css`:
1. Implement a sensible one-off in the project using kit tokens and BEM-like `jm-` naming where possible.
2. Append a row to [COMPONENT_REQUESTS.md](COMPONENT_REQUESTS.md) (date, project, need, interim markup, priority, status).
3. For backlog context, use the vault at `01-Projects/ui-kit/` in `J-M-NG/obsidian-vault` (`tasks.md`, `component-requests.md`).

## Naming
Follow the Naming section of the vault's `CLAUDE.md`: branches `ui-kit/<type>-<short-description>`, commits and pull request titles start with `ui-kit:`.
