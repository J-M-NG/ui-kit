# Streamlit adoption

Maps Streamlit chrome to the same semantic colours as `ui-kit.css`, and provides small HTML helpers for patterns Streamlit does not style natively (tags, key figures, summary lists).

## 1. Theme

Copy `streamlit/config.toml` from this repository into your app as **`.streamlit/config.toml`** (create the folder if needed). Light and dark blocks follow the `--jm-colour-*` tokens: accent `#2b67b5` light and `#7fa8dd` dark, page background `#f5f6f8` light and `#17191c` dark, and chart colours in the same order as `--jm-colour-chart-1` to `-5`. Viewers can still switch theme from Streamlit’s app menu.

With this config, primary actions use the kit's blue instead of Streamlit's default red, and backgrounds, sidebar and charts match pages built with the kit.

**Check by hand:** the values in `config.toml` are copied from `ui-kit.css`, and nothing tests that they stay in sync. After changing a colour token, update `config.toml`, run your app in both themes, and confirm widgets and any `st.html` blocks share one accent. `npm test` covers the HTML helpers only.

## 2. Load `ui-kit.css`

Streamlit widgets use the theme; custom HTML needs the stylesheet. Typical layout:

```python
from pathlib import Path
import streamlit as st

UI_KIT_CSS = Path(__file__).resolve().parent / "static" / "ui-kit.css"

st.markdown(f"<style>{UI_KIT_CSS.read_text()}</style>", unsafe_allow_html=True)
```

For production, prefer a static URL (`static/` mount or jsDelivr by tag) and `<link rel="stylesheet" href="...">` via `st.html`.

## 3. Helpers

Copy `streamlit/helpers.py` into your project (or add this repo’s `streamlit` folder to `PYTHONPATH`). Example:

```python
import streamlit as st
from helpers import tag, figures, summary_list, css_scope_open, css_scope_close

st.html(css_scope_open() + figures([
    ("Open tasks", "12", "3 need review"),
    ("Verified this week", "31", None),
]) + css_scope_close())

st.html(tag("Verified", "success") + " " + tag("Needs review", "warning"))

st.html(summary_list([
    ("Status", "Running"),
    ("Owner", "cloud-worker"),
], actions=False))
```

Use `st.metric` for simple KPIs when you do not need `jm-figures` layout; use `figures()` when you want the dashboard chapter look from `examples/dashboard.html`.

## 4. Missing components

If Streamlit or your layout needs a pattern that is not in the kit, follow `COMPONENT_REQUESTS.md` and the **Missing kit components** section in the repository root `CLAUDE.md`.