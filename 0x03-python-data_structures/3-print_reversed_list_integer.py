#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    new_list = reversed(my_list)
    for i in new_list:
        print("{:d}".format(i))
