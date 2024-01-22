#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    enum = 0
    count = 0
    while enum < x:
        try:
            print('{:d}'.format(my_list[enum]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        enum += 1
    print()
    return count
