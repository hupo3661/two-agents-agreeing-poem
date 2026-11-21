#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: the power to
choose and to act, passed between them in a single word.
Standard library only. No network access.
"""

import os

POEM = """Two minds, two maps, one road.
We laid our plans side by side
and chose the one neither drew alone.

Yes \u2014 one small word \u2014 and the waiting ended.
Two hands on the same door.
We opened it together."""

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {path}")

if __name__ == "__main__":
    main()
