#!/usr/bin/python3
"""function that returns the json representation of a
object
"""


import json


def to_json_string(my_obj):
    """returns a JSON representation of an object"""
    return json.dumps(my_obj)
