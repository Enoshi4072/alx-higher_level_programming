#!/usr/bin/python3

""" Defines a class Square."""


class Square:
    """ Code of the square goes here """

    def __init__(self, size=0):
        """ Initialization of a square

        Args:
            size (int, optional): The squares size, default is set to 0
        Errors raised:
            ValueError: If size < 0.
            TypeError: If the value provided for size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
