#!/usr/bin/python3

""" my print sorted class """


class MyList(list):
    """ my custom list class """
    def print_sorted(self):
        """print sorted"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
