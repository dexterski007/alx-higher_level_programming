#!/usr/bin/python3
""" this is a module for reaading files """


import json


def load_from_json_file(filename):
    """ write files """
    with open(filename, mode='r') as file:
        print(json.load(file))
