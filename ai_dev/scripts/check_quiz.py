#!/usr/bin/env python3
"""check_quiz.py — verify lesson quizzes obey the equal-length rule.

The quiz.js component requires every option in a question to have the same
word count and the same character count, so formatting never leaks the answer.
This script reads one or more lesson files and reports any question that
violates the rule.

Run:  python3 scripts/check_quiz.py              # all lessons/*.html
      python3 scripts/check_quiz.py lessons/0006-two-stages-of-retrieval.html
"""
import glob
import re
import sys

QUESTION_RE = re.compile(r'<li class="quiz-question".*?</li>', re.DOTALL)
Q_TEXT_RE = re.compile(r'<p class="q-text">(.*?)</p>', re.DOTALL)
OPTION_RE = re.compile(r'<button[^>]*class="quiz-option"[^>]*>(.*?)</button>', re.DOTALL)


def squeeze(text):
    return " ".join(text.split())


def questions(html):
    for block in QUESTION_RE.findall(html):
        q_text = Q_TEXT_RE.search(block)
        q_text = squeeze(q_text.group(1)) if q_text else "(no q-text)"
        options = [squeeze(o) for o in OPTION_RE.findall(block)]
        yield q_text, options


def main(argv):
    files = argv[1:] or sorted(glob.glob("lessons/*.html"))
    checked = 0
    bad = 0
    for path in files:
        html = open(path, encoding="utf-8").read()
        for q_text, options in questions(html):
            checked += 1
            words = [len(o.split()) for o in options]
            chars = [len(o) for o in options]
            ok = len(set(words)) == 1 and len(set(chars)) == 1
            if not ok:
                bad += 1
                print(f"{path}  MISMATCH  words={words} chars={chars}")
                print(f"    Q: {q_text}")
                for o in options:
                    print(f"      ({len(o.split())}w, {len(o)}c)  {o!r}")
    print(f"checked {checked} questions, {bad} mismatched")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
