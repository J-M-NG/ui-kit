#!/usr/bin/env python3
"""Lightweight checks for streamlit/helpers.py (stdlib only)."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "streamlit"))

import helpers  # noqa: E402


class TestHelpers(unittest.TestCase):
    def test_tag_default(self):
        self.assertEqual(helpers.tag("Open"), '<span class="jm-tag">Open</span>')

    def test_tag_variant(self):
        self.assertIn("jm-tag--success", helpers.tag("Ok", "success"))

    def test_tag_rejects_unknown_variant(self):
        with self.assertRaises(ValueError):
            helpers.tag("?", "nope")

    def test_figure_escapes(self):
        html = helpers.figure("Label", "<b>1</b>")
        self.assertIn("&lt;b&gt;", html)
        self.assertIn("jm-figures", html)

    def test_summary_list_no_actions(self):
        html = helpers.summary_list([("A", "B")], actions=False)
        self.assertIn("jm-summary-list--no-actions", html)


if __name__ == "__main__":
    unittest.main()