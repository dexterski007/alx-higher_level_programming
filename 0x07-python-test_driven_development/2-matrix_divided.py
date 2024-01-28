#!/usr/bin/python3

""" This module divides a matrix by a dividor
    Args: matrix: the matrix
        div: neo the divider
    Returns:  the divided matrix
"""


def matrix_divided(matrix, div):
    """
    adds 2 integers or floats
    """

    c = a
    d = b
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        c = int(a)
    if isinstance(b, float):
        d = int(b)
    return c + d


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
