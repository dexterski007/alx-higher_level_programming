#!/usr/bin/python3
""" Hello rectangle """


class Rectangle:
    """this is a rectangle class"""
    def __init__(self, width=0, height=0):
        """ initializing the class """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ get width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
