#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    value = 0
    for i in my_list:
        if i > value:
            value = i
    return value
