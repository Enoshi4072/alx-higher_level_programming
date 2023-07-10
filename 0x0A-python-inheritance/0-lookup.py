#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes of an object

    Args:
        obj: The object to be inspected.

    Returns:
        List of strings representing the attributes and methods of the obj

    """
    return dir(obj)
