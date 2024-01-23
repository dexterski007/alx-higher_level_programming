#!/usr/bin/python3

""" square - is defining a square """


class Square:
    """ this is a square """
    def __init__(self, size=0, position=(0, 0)):
        """ constructor """
        self.size = size
        self.position = position

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
        if self.size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

    @property
    def position(self):
        """ position """
        return self.__position

    @position.setter
    def position(self, value):
        """set new position"""
        if not isinstance(value, tuple) or len(value) != 2\
           or not all(isinstance(i, int) for i in value)\
           or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """ print square with str """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        return ("")
