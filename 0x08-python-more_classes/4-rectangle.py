#!/usr/bin/python3
"""creating a rectangle class"""


class Rectangle:
    """ defines an empty class rectangle """

    def __init__(self, width=0, height=0):
        """ initializes height and width """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @height.setter
    def height(self, value):
        """ set height with new value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ set width with new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """prints representation of the rectangle with '#'"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__width):
            for j in range(self.__height):
                string += '#'
            if i < (self.__width - 1):
                string += '\n'
        return string

    def __repr__(self):
        """return a string representation"""
        return f"Rectangle({self.width}, {self.height})"
