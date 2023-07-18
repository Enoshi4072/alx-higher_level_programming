#!/usr/bin/python3
""" The class to manage id attributes of other classes """

import json


class Base:
    """
    Base class to manage the id attribute and provide
    deserialization and serialization functionality

    Private Class attributes:
        __nb_objects: Number of instantiated Base objects

    """

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a JSON string rep of a list_dict

        Args:
            list_dictionary: A list of dictionaries to be converted to JSON
        Return:
            str: A JSON string rep of the list of dicts
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string rep of list_objs to a file

        Args:
            list_objs: A list of insts to convert to JSOn and save
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_j = "[]"
        else:
            list_j = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as r_file:
            r_file.write(cls.to_json_string(list_j))

    @staticmethod
    def from_json_string(json_string):
        """
        Conversio of a JSON string to a list of dicts

        Args:
            json_string: A JSON string to convert to a list of dicts

        Return:
            list: A list of dicts converted from JSON string
        """
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as r_file:
                j_data = r_file.read()
                c_data = cls.from_json_string(j_data)
                c_i = [cls.create(**i) for i in c_data]
                return c_i
        except FileNotFoundError:
            return []
