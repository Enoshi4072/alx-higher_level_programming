#!/usr/bin/python3

""" The function checks if an object is an instance of a specified class """


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class
    Args:
        obj: The obj to be checked
        a_class: The class to be compared against.

    Return:
        True:
            If the object is an instance of the specified class
        False:
            If the objecy if not an instance of the specified class

    """
    if type(obj) == a_class:
        return True
    else:
        return False
