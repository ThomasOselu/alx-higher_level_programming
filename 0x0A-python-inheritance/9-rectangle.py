#!/usr/bin/python3
"""class rectangle that inherits from BaseGeomrty"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a child class Rectangle"""

    def __init__(self, width, height):
        """initializing the class attributes"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
