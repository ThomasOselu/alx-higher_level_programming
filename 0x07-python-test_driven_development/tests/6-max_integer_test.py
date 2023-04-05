#!/usr/bin/python3
"""unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class for testing 6-max_integer_test.py
    """
    def test_max_integer(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_float(self):
        """
        test case for a list of positive and negative floating
        without arguments
        """
        test_list = [1.2, 2.3, 3.12, 8.536, 4.6, -40.0, -400.99, -12.6, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_neg(self):
        """
        test case for a list of positive and negative integers
        without arguments
        """
        test_list = [1, 2, 3, 5, 4, -40, -400, -12, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_empty(self):
        """
        test case if an empty list if passed
        without arguments
        """
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_max_integer_one(self):
        """
        test case if a  list has one element
        without arguments
        """
        test_list = [2]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_first(self):
        """
        test case if the first element is the max
        without arguments
        """
        test_list = [5, 1, 4, 2]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_last(self):
        """
        test case if the first element is the max
        without arguments
        """
        test_list = [5, 1, 4, 2,6]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_middle(self):
        """
        test case if the middle element is the max
        without arguments
        """
        test_list = [5, 1, 7, 2,6]
        self.assertEqual(max_integer(test_list), max(test_list))
