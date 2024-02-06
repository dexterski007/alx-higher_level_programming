#!/usr/bin/python3
""" this is a module for reaading files """


import json


def class_to_json(obj):
    """ class json """
    return obj.__dict__
