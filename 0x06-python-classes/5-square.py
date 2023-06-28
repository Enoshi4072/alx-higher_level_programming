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
        self.__size = size

    @property
    def size(self):
        """
        Gets (getter) the squares size.
        Returns:
            The squares size(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter:
            Sets the sqaures size

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """
        The area of the square.
        Returns:
            The area of the square which is an int
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Code to print square with char #
        prints empty line if size = 0
        """
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            print("#" * self.__size)
