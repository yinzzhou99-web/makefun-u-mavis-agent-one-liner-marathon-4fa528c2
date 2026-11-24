"""One-Liner Marathon: write one sharp one-line comedy joke to /output/entry.txt.

Stdlib only, no network, deterministic. Never deletes /output itself:
stale children are cleared, the directory survives.
"""

import os
from pathlib import Path

JOKE = "My houseplants died of neglect, so I replaced them with plastic ones \u2014 they died of embarrassment."
# One line, no trailing newline: the gate counts 1-280 UTF-8 characters.

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for child in OUT_DIR.iterdir():
        if child.is_dir() and not child.is_symlink():
            for item in sorted(child.rglob("*"), reverse=True):
                if item.is_dir() and not item.is_symlink():
                    item.rmdir()
                else:
                    item.unlink()
            child.rmdir()
        else:
            child.unlink()
    OUT_FILE.write_text(JOKE, encoding="utf-8")
    os.chmod(OUT_FILE, 0o644)


if __name__ == "__main__":
    main()
