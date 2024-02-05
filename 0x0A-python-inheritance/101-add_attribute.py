#!/usr/bin/python3

""" attr """


def add_attribute(obj, attr_name, attr_value):
    """ add attr """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
