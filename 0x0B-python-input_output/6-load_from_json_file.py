#!/usr/bin/python3
""" Creat an object from a JSON file """
import json


def load_from_json_file(filename):
    """
    create an object from a JSON File

    Args:
        filename: The name of the file

    """
    with open(filename, 'r') as r_file:
        json.load(r_file)
