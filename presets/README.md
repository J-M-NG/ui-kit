# Presets

Optional stylesheets that set only the [documented project hooks](../README.md#project-hooks). Load one **after** `ui-kit.css`. Without a preset you get the kit default: Source Serif 4 headings, rounded corners, blue accent.

| File | What it changes |
|------|-----------------|
| [`minimal-square.css`](minimal-square.css) | Sans headings (Source Sans 3, the body font) and square corners. Accent unchanged. |
| [`teal.css`](teal.css) | Teal accent (from the kit's sky palette steps) in light and dark. |

Check colour changes with `python3 tests/check_contrast.py --project presets/teal.css`.
