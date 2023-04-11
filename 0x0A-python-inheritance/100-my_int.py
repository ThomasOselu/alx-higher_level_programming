#!/usr/bin/python3
"""a class repressentation for class Myint"""


class MyInt(int):
    """representation of class Myint inheriting form int"""
    def __ne__(self, value):
        """Overrides != operator with == behavior."""
        return super().__ne__(value)

    def __eq__(self, value):
        """overrides == operator with != behaviours"""
        return super().__eq__(value)
