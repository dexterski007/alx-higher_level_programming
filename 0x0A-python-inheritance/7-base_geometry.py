#!/usr/bin/python3

""" test classes """


class BaseGeometry:
    """ geo v2 class """
    def area(self):
        """ area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check int """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
