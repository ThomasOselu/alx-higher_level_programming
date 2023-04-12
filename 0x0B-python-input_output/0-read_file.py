#!/usr/bin/python3
"""function used to read a file"""


def read_file(filename=""):
    """function used to read a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
