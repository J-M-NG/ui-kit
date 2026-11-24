"""HTML fragments that match ui-kit classes. Use with st.html() or st.markdown(..., unsafe_allow_html=True).

Requires ui-kit.css loaded in the Streamlit app (see streamlit/README.md). No Streamlit dependency.
"""

from __future__ import annotations

import html
from typing import Iterable, Sequence

_TAG_VARIANTS = frozenset({"success", "warning", "error", "info"})


def escape(text: str) -> str:
    return html.escape(text, quote=True)


def tag(label: str, variant: str = "") -> str:
    """Status tag: jm-tag, optional jm-tag--success|warning|error|info."""
    classes = "jm-tag"
    if variant:
        if variant not in _TAG_VARIANTS:
            raise ValueError(f"variant must be one of {_TAG_VARIANTS!r}, got {variant!r}")
        classes += f" jm-tag--{variant}"
    return f'<span class="{classes}">{escape(label)}</span>'


def figure(label: str, value: str, note: str | None = None) -> str:
    """Key figure tile: jm-figures."""
    note_html = ""
    if note:
        note_html = f'<span class="jm-figures__note">{escape(note)}</span>'
    return (
        '<dl class="jm-figures">'
        f"<div><dt>{escape(label)}</dt><dd>{escape(value)}{note_html}</dd></div>"
        "</dl>"
    )


def figures(rows: Sequence[tuple[str, str, str | None]] | Sequence[tuple[str, str]]) -> str:
    """Row of key figures; each row is (label, value) or (label, value, note)."""
    parts = ['<dl class="jm-figures">']
    for row in rows:
        label, value = row[0], row[1]
        note = row[2] if len(row) > 2 else None
        note_html = f'<span class="jm-figures__note">{escape(note)}</span>' if note else ""
        parts.append(f"<div><dt>{escape(label)}</dt><dd>{escape(value)}{note_html}</dd></div>")
    parts.append("</dl>")
    return "".join(parts)


def summary_list(
    rows: Iterable[tuple[str, str]] | Iterable[tuple[str, str, str]],
    *,
    actions: bool = False,
) -> str:
    """Summary list: jm-summary-list with optional action column (plain text links)."""
    cls = "jm-summary-list"
    if not actions:
        cls += " jm-summary-list--no-actions"
    parts = [f'<dl class="{cls}">']
    for row in rows:
        term, detail = row[0], row[1]
        action = row[2] if len(row) > 2 else None
        parts.append('<div class="jm-summary-list__row">')
        parts.append(f"<dt>{escape(term)}</dt><dd>{escape(detail)}</dd>")
        if actions:
            action_cell = escape(action) if action else ""
            parts.append(f'<dd class="jm-summary-list__actions">{action_cell}</dd>')
        parts.append("</div>")
    parts.append("</dl>")
    return "".join(parts)


def link_stylesheet(href: str) -> str:
    """Inject ui-kit.css from a URL or path (for st.html in head-like embed)."""
    return f'<link rel="stylesheet" href="{escape(href)}">'


def css_scope_open() -> str:
    """Wrap custom HTML so kit typography applies (use with css_scope_close)."""
    return '<div class="jm-container jm-stack">'


def css_scope_close() -> str:
    return "</div>"