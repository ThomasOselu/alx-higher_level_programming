#!/usr/bin/python3
"""function that adds an attribute to an obj"""


def add_attribute(obj, attr, value):
    """function that adds an attribute to an object
    args:
        obj: the object to add to
        attr: name of attribute
        value: value of the attribute
        """

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
