#!/usr/bin/python3
"""a class representing a square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class that inherits from rectangle"""

    def __init__(self, size):
        """initializing the attributes
        args: size:the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
