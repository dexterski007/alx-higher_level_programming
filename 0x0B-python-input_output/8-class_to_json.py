#!/usr/bin/python3
""" this is a module for reaading files """


import json

def class_to_json(obj):
    """ class json """
    attr = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, bool, int)):
            attr[attr_name] = attr_value
    return attr