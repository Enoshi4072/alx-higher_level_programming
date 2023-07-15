#!/usr/bin/python3
""" To write an object to a text file using JSON rep """

import json


def save_to_json_file(my_obj, filename):
    """
    Writes the object to a file using JSON

    Args:
        my_obj (object): The object to be written to the file
        filename: The name of the file to save the JSON rep

    """
    with open(filename, 'w') as r_file:
        json.dump(my_obj, r_file)
