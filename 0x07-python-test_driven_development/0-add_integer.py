#!/usr/bin/python3
"""a module  function that adds two integer,
after typecasting to int if float
>>> add_integer(2,5)
7
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b,type casted if float
        return int(a) + (b)
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
