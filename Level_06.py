#!/usr/bin/env python3
"""
Python Challenge – Level 6 (channel)
------------------------------------

Clues:
- Page title: "now there are pairs"  → inside the ZIP, each text file has a *pair* of clues:
  (1) the text content (next file number) and (2) the file's ZIP comment (a character).
- HTML source comment: "<!-- <-- zip -->"  → replace `channel.html` with `channel.zip`.

Goal:
1) Download/open channel.zip.
2) Start at 90052.txt and follow the "Next nothing is <number>" chain.
3) Collect every file's ZIP *comment* along the way (and also the archive's own comment).
4) The concatenated comments reveal the final hint (ASCII art → read the letters).

This script keeps the code clear and production-friendly, with small functions,
type hints, and explicit error handling.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple
from zipfile import ZipFile, BadZipFile

# ----------------------------
# Configuration
# ----------------------------
ZIP_PATH = Path("channel.zip")   # Make sure this file is in the same folder as the script
START_NUMBER = "90052"           # From readme.txt inside the ZIP
NEXT_PATTERN = re.compile(r"Next nothing is (\d+)")
STOP_PATTERN = re.compile(r"Collect the comments")  # Appears near the end of the chain


def read_text_from_zip(zipf: ZipFile, member: str) -> str:
    """Read a text file inside the ZIP and return it as a UTF-8 string."""
    with zipf.open(member, "r") as f:
        # The files are small; decode the whole content safely.
        return f.read().decode("utf-8", errors="replace")


def follow_chain_and_collect_comments(zipf: ZipFile, start_number: str) -> Tuple[List[str], List[str]]:
    """
    Follow the 'nothing' chain starting at <start_number>.txt.
    Collect and return:
      - trail: the sequence of file numbers visited (for debugging/audit),
      - comments: the ZIP comments gathered from each visited file (as characters).

    The loop stops when we encounter the line "Collect the comments." or
    when we fail to find a next number.
    """
    trail: List[str] = []
    comments: List[str] = []

    current = start_number
    while True:
        member = f"{current}.txt"
        try:
            info = zipf.getinfo(member)  # Get metadata to read the *file comment*
        except KeyError:
            # If the member doesn't exist, stop to avoid infinite loops.
            break

        # Record this step and collect the file's comment character.
        trail.append(current)
        comments.append(info.comment.decode("utf-8", errors="replace"))

        # Read content to decide where to go next (or when to stop).
        text = read_text_from_zip(zipf, member)

        # If the file tells us to "Collect the comments.", we are done.
        if STOP_PATTERN.search(text):
            break

        # Otherwise, look for the next number.
        m = NEXT_PATTERN.search(text)
        if not m:
            # No "Next nothing is ..." found → stop.
            break

        current = m.group(1)

    return trail, comments


def main() -> None:
    # 1) Sanity check for the ZIP file.
    if not ZIP_PATH.exists():
        raise FileNotFoundError(
            f"Could not find {ZIP_PATH}. Download it by changing the URL "
            f"from channel.html → channel.zip on the challenge page."
        )

    try:
        with ZipFile(ZIP_PATH, "r") as zipf:
            # (Optional) Read the archive-level comment (rarely needed, but harmless to include).
            archive_comment = zipf.comment.decode("utf-8", errors="replace")

            # 2) Read the README to verify the starting number (for completeness).
            #    Not strictly required if we already know 90052, but good documentation.
            if "readme.txt" in zipf.namelist():
                readme = read_text_from_zip(zipf, "readme.txt")
                print("README:\n" + readme.strip() + "\n")

            # 3) Follow the chain and collect per-file ZIP comments.
            trail, comments = follow_chain_and_collect_comments(zipf, START_NUMBER)

        # 4) Print a brief audit of the path taken (useful when debugging).
        print(f"Visited {len(trail)} files. First 5 steps: {trail[:5]} ... Last: {trail[-1] if trail else 'N/A'}")

        # 5) Concatenate the collected comments — this produces the ASCII art hint.
        banner = "".join(comments)

        print("\n--- Collected Comments (ASCII art / hint) ---")
        print(banner)

        # 6) (Optional) Surface a gentle nudge about the usual solution path.
        #    The ASCII art spells out the word when you “look at the letters”.
        #    Historically, this reads as OXYGEN → next page uses that keyword.
        #    We don't hardcode the word; the art should make it obvious.
        if archive_comment:
            print("\n(Archive comment was present; included above if meaningful.)")

        print("\nNext step (manual): Read the letters in the banner to form the keyword "
              "and use it in place of 'channel' in the URL.")

    except BadZipFile:
        raise SystemExit("The file exists but is not a valid ZIP. Re-download channel.zip and try again.")


if __name__ == "__main__":
    main()
