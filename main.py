#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes one deadpan one-star review of gravity (max 160 characters) to
/output/entry.txt. Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os

REVIEW = "One star. Gravity has dropped everything I have ever owned and has never once apologised."
# Why gravity: of the candidates tried (sun, sleep, thumbs, water, oxygen),
# only gravity's grievance is literally true of everyone, every day, and its
# sting — "has never once apologised" — lands in the last three words.


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # 1-160 UTF-8 characters, not whitespace-only, exactly one line.
    if not REVIEW.strip():
        raise SystemExit("entry review is empty or whitespace-only")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise SystemExit("entry review must be a single line")
    if not 1 <= len(REVIEW) <= 160:
        raise SystemExit(f"entry review is {len(REVIEW)} characters, must be 1-160")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"Wrote {len(REVIEW)} characters to {path}")


if __name__ == "__main__":
    main()
