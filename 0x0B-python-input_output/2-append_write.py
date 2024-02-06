#!/usr/bin/python3
""" this is a module for reaading files """


def append_write(filename="", text=""):
    """ write files """
    with open(filename, mode='a', encoding="utf-8") as file:
        num = file.write(text)
    return num
