#!/usr/bin/python3
""" this is a module for reaading files """


import json


def save_to_json_file(my_obj, filename):
    """ write files """
    with open(filename, mode='w') as file:
        file.write(json.dumps(my_obj))
