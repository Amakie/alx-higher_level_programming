#!/usr/bin/python3
"""function that writes a text to a file"""


def write_file(filename="", text=""):
    """returns the written text"""

    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
