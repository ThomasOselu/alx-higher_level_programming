#!/usr/bin/python3
"""Creating a base class"""


class Base:
    """The base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
