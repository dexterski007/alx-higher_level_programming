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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ print square """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
