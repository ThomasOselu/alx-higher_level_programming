#!/usr/bin/python3
"""creates a class square"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing the attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.__width)

    @property
    def size(self):
        """retrieving size"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets thesize attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes
        args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y":
                self.y}
