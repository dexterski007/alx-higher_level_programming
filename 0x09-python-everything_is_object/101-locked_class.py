#!/usr/bin/python3
""" how to lock a class """


class LockedClass:
    """ no instantiatin except for john """

    __slots__ = 'first_name'
