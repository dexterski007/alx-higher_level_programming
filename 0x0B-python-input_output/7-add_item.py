#!/usr/bin/python3
""" this is a module for reaading files """


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


def add_items_to_list(filename, *items):
    """ write files """
    try:
        current_list = load_from_json_file(filename)
    except FileNotFoundError:
        current_list = []

    current_list.extend(items)
    save_to_json_file(current_list, filename)

if __name__ == "__main__":
    filename = "add_item.json"
    items = sys.argv[1:]
    add_items_to_list(filename, *items)
