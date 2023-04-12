#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    a class that defines a student by first_name,last_name,age
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization of the student attributes
        args:
            first_name: the first name of student
            last_name: the last name of the student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a attributes representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
