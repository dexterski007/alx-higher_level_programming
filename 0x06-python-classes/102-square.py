#!/usr/bin/python3

""" square - is defining a square """


class Square:
    """ this is a square """
    def __init__(self, size=0):
        """ constructor """
        self.size = size

    def area(self):
        """ area instance """
        return self.__size * self.__size

    @property
    def size(self):
        """ return size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set new size """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, compar):
        return self.area() == compar.area()

    def __gt__(self, compar):
        return self.area() > compar.area()

    def __lt__(self, compar):
        return self.area() < compar.area()

    def __ne__(self, compar):
        return self.area() != compar.area()

    def __le__(self, compar):
        return self.area() <= compar.area()

    def __qe__(self, compar):
        return self.area() >= compar.area()
