#!/usr/bin/python3

""" Defining a function that will look of attributes of an object """


def lookup(obj):
    """
    Returns the list of available attributes of an object

    Args:
        obj: The object to be inspected.

    Returns:
        List of strings representing the attributes and methods of the obj

    """
    return dir(obj)
