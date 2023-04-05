#!/usr/bin/python3
"""Defining a name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """prints a name
    args:
        first_name: the first name
        last_name: the last name
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
