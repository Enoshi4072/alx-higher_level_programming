#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
or JSON serialization of an object:
"""


def class_to_json(obj):
    """
    args:
        obj - an instance of a class
    """
    return obj.__dict__
