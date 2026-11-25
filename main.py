"""The One-Line Exit — make.fun entry.

Writes one funny one-line resignation letter to /output/entry.txt.
"""

import os

LETTER = (
    "I hereby resign: the office printer has jammed for the last "
    "time, and frankly, so have I."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
