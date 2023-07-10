#!/usr/bin/python3

""" Defining the Class Square that inherits from Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Code for the square goes here """
    def __init__(self, size):
        """
        Initialiing the square properties

        Args:
            size: The squares size (int)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return:
            The string rep of a square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
