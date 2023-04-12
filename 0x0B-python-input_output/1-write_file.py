#!/usr/bin/python3
"""function that writes a string to a text file, returns
the number of characters
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file, returns
    the number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
