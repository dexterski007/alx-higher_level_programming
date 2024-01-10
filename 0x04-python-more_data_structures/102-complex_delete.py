#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] is value:
            del a_dictionary[key]
    return a_dictionary
