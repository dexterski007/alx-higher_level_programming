#!/usr/bin/python3
import math
""" magic - is refining a potter """


class MagicClass:
    """ this is magic """
    def __init__(self, radius):
        if not None and not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius
    
    def area(self):
        return self.radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius
