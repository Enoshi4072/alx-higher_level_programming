#!/usr/bin/python3
""" Add arguments to a Python list """
import json
import sys

""" Importing external functions """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    """ Attempting to load existing items """
    list_items = load_from_json_file(filename)

except FileNotFoundError:
    """ If the file is non_existent, create an empty list """
    list_items = []
""" Add items to the list """
list_items.extend(sys.argv[1:])

""" Save the list to the file """
save_to_json_file(list_items, filename)
