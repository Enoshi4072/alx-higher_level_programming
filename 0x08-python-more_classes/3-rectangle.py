#!/usr/bin/python3
""" The Rectangle class. """


class Rectangle:
    """ Code for the Rectangle """
    def __init__(self, width=0, height=0):
        """ Initialization the rectangles properties

        Args:
            width : The rectangles width (int)
            height: The rectangles height (int)

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter: It retrieves the rectangles width

        Returns:
            The width of the rectangle (int)

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter: Sets the rectangles width

        Arg:
            value: The rectangles width to be set (int)

        Raise:
            TypeError: When the value is not an integer
            ValueError: When the value is < 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter: Retrieves the rectangles height

        Returns:
            The rectangles height as a private attribute (int)

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter: The rectangles height

        Args:
            value: The value of the height of the rect to be set (int)

        Raises:
            TypeError: If the value is not an int
            ValueError: If the value is < 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the rectangles area

        Return: The rectangle's area (int)

        """
        return self.__height * self.width

    def perimeter(self):
        """
        Calculates the rectangle's perimeter

        Return: The rectangles perimeter (int)

        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Return:
            A string representation of the rectangle

        Returns:
            str: A string rep of the rect using '#' char

        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        return "\n".join(["#" * self.__width] * self.__height)
