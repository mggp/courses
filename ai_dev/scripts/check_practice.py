#!/usr/bin/env python3
"""Check metadata required by the browser-only practice widgets.

Run: python3 scripts/check_practice.py [lesson.html ...]
"""
import glob
import re
import sys


PANEL_RE = re.compile(
    r'<(?:div|section)\b(?=[^>]*\bdata-practice="([^"]+)")[^>]*>(.*?)</(?:div|section)>',
    re.DOTALL,
)


def check_panel(path, kind, html):
    errors = []
    has_message = 'data-practice-message' in html
    if not has_message:
        errors.append("missing data-practice-message target")
    if kind in {"predict", "explain"}:
        if not re.search(r'<textarea\b|<input\b[^>]*type="text"', html):
            errors.append("missing learner answer field")
        if 'data-practice-reveal' not in html:
            errors.append("missing gated reveal")
        if kind == "explain" and (
            'class="claim-list"' not in html or 'type="checkbox"' not in html
        ):
            errors.append("missing claim checklist")
    elif kind == "cloze":
        selects = re.findall(r'<select\b.*?</select>', html, re.DOTALL)
        if not selects:
            errors.append("missing select")
        for select in selects:
            options = re.findall(r'<option\b([^>]*)>', select)
            if not any('data-correct="true"' in option for option in options):
                errors.append("select missing correct option")
            if any('data-correct="true"' not in option and 'data-why=' not in option for option in options if 'value=""' not in option):
                errors.append("select has distractor without data-why")
        if 'data-practice-check' not in html:
            errors.append("missing check button")
    elif kind == "defect":
        choices = [
            attrs
            for attrs in re.findall(r'<button\b([^>]*)>', html)
            if "data-defect-choice" in attrs
        ]
        if not choices:
            errors.append("missing defect choices")
        if sum('data-correct="true"' in choice for choice in choices) != 1:
            errors.append("defect panel must have exactly one correct choice")
        if any('data-why=' not in choice for choice in choices):
            errors.append("defect choice missing data-why")
    else:
        errors.append(f"unknown practice type: {kind}")
    return errors


def main(argv):
    files = argv[1:] or sorted(glob.glob("lessons/*.html"))
    bad = 0
    checked = 0
    for path in files:
        html = open(path, encoding="utf-8").read()
        for kind, panel in PANEL_RE.findall(html):
            checked += 1
            for error in check_panel(path, kind, panel):
                bad += 1
                print(f"{path}  {kind}  {error}")
    print(f"checked {checked} practice artifacts, {bad} errors")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
