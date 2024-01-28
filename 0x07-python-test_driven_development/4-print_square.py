#!/usr/bin/python3

"""prints a square using hashes"""


def print_square(size):
    """
    This module prints a square
    Args:
        size: size of the square
    Raises:
        TypeError if size is not int
        ValueError if size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
