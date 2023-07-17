#!/usr/bin/python3
""" Code for the square inherited from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing the square instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returning a formatted rep of the square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Get the size attribute """
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
        """ Assign the attributes """
        if args and len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        """ Set the key value arguments when dealing with **kwargs """
        for k, v in kwargs.items():
            setattr(self, k, v)
