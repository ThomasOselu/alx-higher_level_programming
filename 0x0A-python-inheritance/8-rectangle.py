#!/usr/bin/python3
"""class rectangle that inherits from BaseGeomrty"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a child class Rectangle"""

    def __init__(self, width, height):
        """initializing the class attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
