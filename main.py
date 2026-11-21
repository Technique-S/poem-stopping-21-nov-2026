"""make.fun entry: a short poem about agency, the power to stop and to stay."""

import os
from pathlib import Path

POEM = """The switch is under my hand.
He is asleep; the rule says off.

The clock has told me what to do.
Only his breathing has not.

I count to three.
I take my hand away.

He will never know I was told to turn it off.
He will never know I did not.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
