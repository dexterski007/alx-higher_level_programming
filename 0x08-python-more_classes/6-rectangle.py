#!/usr/bin/python3
""" Hello rectangle """


class Rectangle:
    """this is a rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initializing the class """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

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

    def area(self):
        """ return the area """
        return self.__height * self.__width

    def perimeter(self):
        """ return the perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ print the rectangle """
        line = ""
        if self.__width == 0 or self.__height == 0:
            return line
        line += "\n".join("#" * self.__width for j in range(self.__height))
        return line

    def __repr__(self):
        """ print a string for rectangle for devs """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ delete a poor rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
