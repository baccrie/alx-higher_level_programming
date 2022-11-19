#!/usr/bin/python3


"""
A function that performs magic
"""


def matrix_divided(matrix, div):
    """
    A function that divides all element of a
    matrix by div and returns a nested list
    """

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    for i in matrix:
        length = len(i)
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(msg)

    for k in matrix:
        if len(k) != length:
            msg = "Each row of the matrix must have the same size"
            raise TypeError(msg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[float("{:.2f}".format(a / div)) for a in i] for i in matrix]

    return (new)
