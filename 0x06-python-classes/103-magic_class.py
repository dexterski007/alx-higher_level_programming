#!/usr/bin/python3
""" magic - is refining a potter """

import math


class MagicClass:
    """ this is magic """
    def __init__(self, radius=0):
        """ radius"""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ return """
        return self.__radius ** 2 * math.pi
        """ return"""
    def circumference(self):
        return 2 * math.pi * self.__radius
