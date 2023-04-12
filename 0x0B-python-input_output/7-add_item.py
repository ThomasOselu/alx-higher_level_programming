#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""


import json
import sys
from os import path
from typing import List

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename: str, item: List[str]):
    """
    Add an item to a list and saves it to a file.

    Args:
        filename: The name of the file to save the list to.
        item: The item to add to the list.
    """
    my_list = []

    if path.exists(filename):
        my_list = load_from_json_file(filename)

    for arg in item:
        my_list.append(arg)

    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_item("add_item.json", sys.argv[1:])
