#!/usr/bin/python3

def search_replace(my_list, search, replace):
    seek = lambda x : replace if x == search else x
    for i in my_list:
        new_list = list(map(seek, my_list))
    return new_list
