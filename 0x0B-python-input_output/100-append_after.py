#!/usr/bin/python3
""" this is a module for seekndestroy files """


def append_after(filename="", search_string="", new_string=""):
    """ write files """
    with open(filename, mode='r', encoding="utf-8") as file:
        lines = file.readlines()
    with open(filename, mode='w', encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
