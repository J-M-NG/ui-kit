"""Check colour-token contrast in ui-kit.css for the light and dark themes.

Usage: python3 tests/check_contrast.py [path/to/ui-kit.css]

Standard library only. Exits with status 1 if any pair is below its minimum,
if a theme is missing a colour token, or if the two dark-theme blocks differ.

Minimums follow WCAG 2.2 AA:
- 4.5:1 for text (1.4.3 Contrast (Minimum));
- 3:1 for form-control borders, focus rings and status marks
  (1.4.11 Non-text Contrast).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TEXT = 4.5
NON_TEXT = 3.0

# (foreground token, background token, minimum ratio). Token names omit "--jm-colour-".
# --jm-colour-border is deliberately not checked: it is for decorative dividers only,
# which WCAG 1.4.11 exempts. Anything that identifies a control or its state must use
# --jm-colour-border-strong, which is checked at 3:1.
PAIRS: list[tuple[str, str, float]] = []

for bg in ("background", "surface", "surface-sunken"):
    for fg in ("text", "text-secondary", "link", "link-hover", "link-visited"):
        PAIRS.append((fg, bg, TEXT))
    for fg in ("border-strong", "focus", "accent"):
        PAIRS.append((fg, bg, NON_TEXT))
    for status in ("success", "warning", "error", "info"):
        PAIRS.append((f"{status}-text", bg, TEXT))
        PAIRS.append((status, bg, NON_TEXT))

PAIRS += [
    ("text", "accent-subtle", TEXT),
    ("link", "accent-subtle", TEXT),
    ("on-accent", "accent", TEXT),
    ("on-accent", "accent-hover", TEXT),
]
for status in ("success", "warning", "error", "info"):
    PAIRS += [
        (f"{status}-text", f"{status}-background", TEXT),
        ("text", f"{status}-background", TEXT),
        (status, f"{status}-background", NON_TEXT),
    ]


def luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip("#")
    channels = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def block_after(css: str, opener: str) -> str:
    """Return the text inside the braces that follow the first match of `opener`."""
    start = css.find(opener)
    if start == -1:
        raise SystemExit(f"Could not find block: {opener!r}")
    i = css.index("{", start) + 1
    depth = 1
    j = i
    while depth:
        if css[j] == "{":
            depth += 1
        elif css[j] == "}":
            depth -= 1
        j += 1
    return css[i : j - 1]


def declarations(block: str) -> dict[str, str]:
    block = re.sub(r"/\*.*?\*/", "", block, flags=re.S)
    return {m[0]: m[1].strip() for m in re.findall(r"(--jm-[\w-]+)\s*:\s*([^;]+);", block)}


def resolve(value: str, scope: dict[str, str], palette: dict[str, str]) -> str:
    seen = 0
    while value.startswith("var("):
        name = value[4:-1].strip()
        value = scope.get(name) or palette.get(name) or ""
        seen += 1
        if not value or seen > 10:
            raise SystemExit(f"Cannot resolve {name}")
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise SystemExit(f"Expected a 6-digit hex colour, got {value!r}")
    return value.lower()


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "ui-kit.css")
    css = path.read_text(encoding="utf-8")

    palette = {
        k: v for k, v in declarations(block_after(css, "Palette (theme independent)")).items()
        if v.startswith("#")
    }
    light = declarations(block_after(css, "Light theme (default)"))
    dark_media = declarations(block_after(css, ':root:not([data-theme="light"])'))
    dark_attr = declarations(block_after(css, ':root[data-theme="dark"]'))

    failures = 0
    if dark_media != dark_attr:
        diff = sorted(set(dark_media.items()) ^ set(dark_attr.items()))
        print("FAIL dark-theme blocks differ:", *diff, sep="\n  ")
        failures += 1

    themes = {"light": light, "dark": dark_media}
    light_colours = {k for k in light if k.startswith("--jm-colour-")}
    dark_colours = {k for k in dark_media if k.startswith("--jm-colour-")}
    if light_colours != dark_colours:
        print("FAIL colour tokens differ between themes:", sorted(light_colours ^ dark_colours))
        failures += 1

    for theme, scope in themes.items():
        print(f"\n{theme} theme")
        for fg, bg, minimum in PAIRS:
            fg_hex = resolve(f"var(--jm-colour-{fg})", scope, palette)
            bg_hex = resolve(f"var(--jm-colour-{bg})", scope, palette)
            ratio = contrast(fg_hex, bg_hex)
            ok = ratio >= minimum
            failures += not ok
            print(f"  {'pass' if ok else 'FAIL'} {ratio:5.2f}:1 (min {minimum}) {fg} on {bg} ({fg_hex} on {bg_hex})")

    total = len(PAIRS) * len(themes)
    print(f"\n{total} pairs checked; {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
