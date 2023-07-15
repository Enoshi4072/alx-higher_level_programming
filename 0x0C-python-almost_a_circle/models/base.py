#!/usr/bin/python3
""" The class to manage id attributes of other classes """


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing the base class
        Args:
            id: The value to be assinged to an instance.
                If it is None, it will be automatically generated
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
