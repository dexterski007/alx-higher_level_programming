#!/usr/bin/python3
""" this is a module for reaading files """


def write_file(filename="", text=""):
    """ write files """
    with open(filename, mode='w', encoding="utf-8") as file:
        num = file.write(text)
    return num
