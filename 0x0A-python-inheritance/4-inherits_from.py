#!/usr/bin/python3
""" The function checks if the object
is an instance of a class that inherited
(directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance
    of a class.

    Args:
        obj: The object to be checked
        a_class: The class to be compared against

    Returns:
        True: If the object is an instance of a class inherited
        False: If the object is not an instance of the class inherited
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
