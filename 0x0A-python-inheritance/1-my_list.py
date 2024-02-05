#!/usr/bin/python3

""" my print sorted class """


class MyList(list):
    """ my custom list class """
    def print_sorted(self):
        print(sorted(self))
