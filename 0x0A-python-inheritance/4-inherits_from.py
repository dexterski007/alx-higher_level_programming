#!/usr/bin/python3

""" test classes """


def inherits_from(obj, a_class):
    """ test class vs obj """
    return isinstance(obj, a_class) and type(obj) != a_class
