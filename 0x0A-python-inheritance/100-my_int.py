#!/usr/bin/python3

""" my int class """


class MyInt(int):
    """ my custom int """
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
