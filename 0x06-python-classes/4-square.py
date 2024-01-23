#!/usr/bin/python3

""" square - is defining a square """


class Square:
    """ this is a square """
    def __init__(self, size=0):
        """ constructor """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area instance """
        return self.__size * self.__size

    @property
    def size(self):
        """ return size """
        return(self.__size)

    @size.setter
    def size(self, value):
        """ set new size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
