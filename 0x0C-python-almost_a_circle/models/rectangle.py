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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """the gettter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter for height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def width(self):
        """the getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter for width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """the getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """the setter for x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """the getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """the setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #
        """
        if self.__width == 0 and self.__height == 0:
            return ""
        for y in range(0, self.__y):
            print()
        for i in range(1, self.__height+1):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(1, self.__width+1):
                print("#", end="")
            print()

    def __str__(self):
        """returns a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute
        args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.width = arg
                elif b == 2:
                    self.height = arg
                elif b == 3:
                    self.x = arg
                elif b == 4:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
