#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for the attributes
        args:
            width: the width of the rectangle
            height: the height of the rectangle
            X=0: position
            y=0: position
            id=None: id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """the getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter for width"""
        if not isinstance(int, value):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be greater than zero')
        self.__width = value

    @property
    def height(self):
        """the gettter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter for height"""
        if not isinstance(int, value):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be greater than 0')
        self.__height = value

    @property
    def x(self):
        """the getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """the setter for x"""
        if not isinstance(int, value):
            raise TypeError('value must be an integer')
        if value < 0:
            raise ValueError('value must be >= 0')
        self.__x = value

    @property
    def y(self):
        """the getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """the setter for y"""
        if not isinstance(int, value):
            raise TypeError('value must be an integer')
        if value < 0:
            raise ValueError('value must be >= 0')
        self.__y = value
