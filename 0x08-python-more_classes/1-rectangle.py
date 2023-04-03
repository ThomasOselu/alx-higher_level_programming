#!/usr/bin/python3
"""creating a rectangle class"""


class Rectangle:
    """defines a rectangular class"""

def __init__(self, width=0, height=0):
    """defining the width and height of new rectangle
    args:
       width: width of new rectangle
       height: height of new rectangle
    """
    self.height = height
    self.width = width

    @property
    def width(self):
        """retriving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retriving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
