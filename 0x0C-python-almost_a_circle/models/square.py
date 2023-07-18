#!/usr/bin/python3
""" Code for the square inherited from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class rep a square shape which is inherited
    from the rect class

    Args:
        size: The size of the square (int)
        x (optional, int): The x-coordinate of the square. Set to 0 as default
        y (optional, int): The y-coordinate of the square. Default is 0
        id (int, optional): The unique identifier for the square.
                            Default set to None
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing the square instances

        Args:
            size (int): The length of one side of the square
            x (optional, int): The x-coordinate of the square. Set to 0 as default
            y (optional, int): The y-coordinate of the square. Default is 0
            id (int, optional): The unique identifier for the square.
                                Default set to None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returning a formatted rep of the square

        Returns:
            str: A str rep containing the squares info:

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get the size attribute

        Retrives the side of the square

        Return:
            int:
                The side length of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size attribute

        arg:
            value: The number to set to one side of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the squares attributes

        Args:
            *args: A variable arglist containing values (tuple)
            **kwargs: A variable-length keyword arg list
        """
        if args and len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        """ Set the key value arguments when dealing with **kwargs """
        for k, v in kwargs.items():
            setattr(self, k, v)
