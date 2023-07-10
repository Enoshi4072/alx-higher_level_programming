#!/usr/bin/python3
""" The function checks if the object
is an instance of, or if the object
is an instance of a class that
inherited from, the specified class """


def is_kind_of_class(obj, a_class):
    """
    Checking if a class is inherited

    Args:
        obj: The object to be checked
        a_class: The class to be compared against

    Return:
        True: If the object is an instance of the specified class
        False: If the object is not an instance of the specified class

    """
    if isinstance(obj, a_class):
        return True

    else:
        return False
