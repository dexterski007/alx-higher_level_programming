#!/usr/bin/python3

"""divides a matrix by divider"""


def matrix_divided(matrix, div):
    """
    This module divides a matrix by a dividor
    Args:
        matrix: the matrix
        div: neo the divider
    Returns:  the divided matrix
    Raises:

    """

    if (not isinstance(matrix, list) or len(matrix) == 0 or
        not all(isinstance(line, list) for line in matrix) or
        not all(isinstance(i, (int, float)) for i in [n for line
                in matrix for n in line])):
        raise TypeError("matrix must be a matrix\
        (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for line in matrix:
        if len(line) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    matrix2 = [[round(i / div, 2) for i in line] for line in matrix]
    return matrix2


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
