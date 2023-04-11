#!/usr/bin/python3
"""a class repressentation for class Myint"""


class MyInt(int):
    """representation of class Myint inheriting form int"""
    def __eq__(self, value):
        """overrides == operator with != behaviours"""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator with == behavior."""
        return self.real == value
