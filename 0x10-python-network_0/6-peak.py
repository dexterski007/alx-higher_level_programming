#!/usr/bin/python3
""" function for big o algorithms of sorting """


def find_peak(list_of_integers):
    """ fucntion to find peak """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
