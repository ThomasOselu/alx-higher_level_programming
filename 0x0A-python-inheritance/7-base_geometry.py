#!/usr/bin/python3
"""a basegeomtry class"""


class BaseGeometry:
    """a class representing basegeometry"""

    def area(self):
        """a function intialization for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public method that validates value
        args:
            name: a string
            value: the parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
