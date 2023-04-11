#!/usr/bin/python3
"""a function that test if an object is an instances of a class
"""


def is_same_class(obj, a_class):
    """a function to determine if the object is
    an instance of the class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to
    """
    return type(obj) == a_class
