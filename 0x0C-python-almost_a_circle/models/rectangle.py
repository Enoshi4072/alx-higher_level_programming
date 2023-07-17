#!/usr/bin/python3
""" To inherit from the Base class """

from models.base import Base


class Rectangle(Base):
    """
    Code for the rectangle and its attributes goes here
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing the rectangle instances

        Args:
            Width: The rectangles width
            height:
            The rectangles height
            x: The rectangles x-coordinate
            y: The rectangles y-coordinate
            id: The id value to be assignd to the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        To get the width attr
        Return:
            The rectangles width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width attr
        Args:
            The width value to be set
        Raise:
            ValueError: if value is a negative int or 0
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute

        Return:
            The rectangles height (int)

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height attribute

        Args:
            Value: The height value to be set

        Raise:
            ValueError: If the value is 0 or a negative
            TypeError: If the value is not an int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x attribute

        Return:
            The x coordinate of the rect
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x co-ordinate

        Raise:
            ValueError: If the value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y coordinate
        Return:
            The y coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y coordinate
        Raise:
            ValueError: If the value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display the rectangle using '#' """
        x_y = ' ' * self.x + '#' * self.width
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(x_y)

    def __str__(self):
        return f"[Rectangle] {(self.id)} {self.x}/{self.y} \
                - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Assign arguments to each attribute in order
        """
        if args and len(args) > 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns a dictionary rep of a rectangle

        """
        return {
               'id': self.id,
               'width': self.width,
               'height': self.height,
               'x': self.x,
               'y': self.y
        }
