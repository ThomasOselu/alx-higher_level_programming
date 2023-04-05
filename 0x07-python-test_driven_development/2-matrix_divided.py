#!/usr/bin/python3
"""Defines a matrix division function
Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """


def matrix_divided(matrix, div):
    """this function is used to determine the value
    when a matrix is divided by a divisor.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err_msg)
    new_matrix = []
    for listes in matrix:
        if type(listes) != list:
            raise TypeError(err_msg)
        if len(listes) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        c_newList = []
        for valor in listes:
            if type(valor) != int and type(valor) != float:
                raise TypeError(err_msg)
            c_newList.append(round(valor/div, 2))
        new_matrix.append(c_newList)
    return new_matrix
