"""One-Liner Laughs entry: writes a single funny line to /output/entry.txt.

Pure Python 3 standard library only. Fully self-contained: the entry line is
defined in this file; no sibling imports, no network access.

The entry must stay exactly one line (no embedded newlines), so the file
holds the line plus a single trailing newline and stdout prints the line only.
"""

import os

LINE = "My fridge just sent me a notification: 'You opened me 14 times today. I'm not a snack machine — I'm a witness.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
