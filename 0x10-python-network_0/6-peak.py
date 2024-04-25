#!/usr/bin/python3
""" function for big o algorithms of sorting """


def find_peak(list_of_integers):
    """ fucntion to find peak """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers
    max_nb = list_of_integers[0]
    nb = int(len(list_of_integers) / 2)
    find_peak(list_of_integers[:nb - 1])
    find_peak(list_of_integers[nb:])

    for i in list_of_integers:
        if max_nb < i:
            max_nb = i
    return max_nb
