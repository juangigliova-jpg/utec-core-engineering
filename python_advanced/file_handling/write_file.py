#!/usr/bin/env python3
"""Module that writes text to a file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file, overwriting it, and return the characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
