"""Copy the bundled catalogue photo to the grader output directory.

The image is shipped in this repository as entry.png. This program does
no rendering or generation; it simply copies that file byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable
is unset), so it runs with only the Python standard library.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isfile(source):
        print(f"error: source missing: {source}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Verify the copy: it must exist, match the source size, and start
    # with the PNG signature (89 50 4E 47 0D 0A 1A 0A).
    if not os.path.isfile(target):
        print(f"error: output missing: {target}", file=sys.stderr)
        return 1
    if os.path.getsize(target) != os.path.getsize(source):
        print(
            f"error: size mismatch: {target} "
            f"({os.path.getsize(target)} bytes) != {source} "
            f"({os.path.getsize(source)} bytes)",
            file=sys.stderr,
        )
        return 1
    with open(target, "rb") as fh:
        header = fh.read(8)
    if header != b"\x89PNG\r\n\x1a\n":
        print(f"error: not a PNG (bad signature): {target}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
