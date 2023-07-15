#!/usr/bin/python3
""" Returns an object (Python data structure) represented by a JSON string """
import json


def from_json_string(my_str):
    """
    Converts a json string into a Python data structure

    Args:
        str: The JSON string to convert

    """
    j_obj = json.loads(my_str)
    return j_obj
