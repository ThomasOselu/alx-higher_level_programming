#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """representing a rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing height and width
        args:
            height:the new rectangle height
            width:the new rectangle width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retriving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""
        if type(width)is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValuError('height must be >= 0')
        self.__height = value
