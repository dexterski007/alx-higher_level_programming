#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print(f"{value:d}".format(value))
    except ValueError:
        return False
    return True
