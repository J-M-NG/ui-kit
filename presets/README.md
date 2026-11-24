# Theme presets (hooks only)

Load **`ui-kit.css` first**, then one preset. Each file overrides only [documented project hooks](../README.md#project-hooks) and semantic colours — no new components.

| File | Intent |
|------|--------|
| [`default-serif.css`](default-serif.css) | Documents the kit default (editorial serif headings, blue accent). Safe to omit if you use the stock file unchanged. |
| [`minimal-square.css`](minimal-square.css) | System sans headings, square corners, unchanged accent. |
| [`matt-warm.css`](matt-warm.css) | Slightly warmer accent and tighter heading rhythm for product dashboards. |

After linking a preset, run `python3 tests/check_contrast.py --project presets/your-preset.css` if you edit colours.