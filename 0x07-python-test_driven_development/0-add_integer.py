#!/usr/bin/python3

""" This module adds integers or floats
    Args: a (int): the first integer
        b (int): the second integer, uses 98 if not provided
    Returns:    int : the sum of 2 integers
"""


def add_integer(a, b=98):
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
