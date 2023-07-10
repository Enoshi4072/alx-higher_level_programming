#!/usr/bin/python3

""" Defining the class rectangle that inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Code for the rectangle goes here """
    def __init__(self, width, height):
        """
        Initialize the rectangle properties

        Args:
            width: The rectangles width (int)
            height: The rectangles height (int)

        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            The area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Prints the string rep of the rectangle.

        Return:
            The string rep of the rect

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
