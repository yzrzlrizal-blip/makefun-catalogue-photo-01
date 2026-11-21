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
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
