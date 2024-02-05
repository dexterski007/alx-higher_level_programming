#!/usr/bin/python3

""" test classes """


class BaseGeometry:
    """ geo v2 class """
    def area(self):
        """ area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check int """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True


class Rectangle(BaseGeometry):
    """ rectangle class """
    def __init__(self, width, height):
        """ get width and height """
        bg = BaseGeometry()
        bg.integer_validator("width", width)
        bg.integer_validator("height", height)
        self.__width = width
        self.__height = height
