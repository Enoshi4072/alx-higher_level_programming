#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    The function prints a name in a given sentence

    Args:
        first_name (str): The first string to be printed
        last_name (str): The last name to be printed. Default is empty

    Raises:
        TypeError: If the args provided are not strings

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
