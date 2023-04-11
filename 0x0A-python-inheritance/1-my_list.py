#!/usr/bin/python3
"""a class that inherts from lists"""


class MyList(list):
    """a class that returns the sorted list for the in-built list
    """

    def print_sorted(self):
        """prints the in-built list in ascending order"""
        print(sorted(self))
