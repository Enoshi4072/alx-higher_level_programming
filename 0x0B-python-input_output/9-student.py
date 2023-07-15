#!/usr/bin/python3
""" Defining the class Student. """


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialization of the class attributes

        Args:
            first_name: The students first name (str)
            last_name: The last name of the student (str)
            age: The students age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Gets the dict rep of a studnt instance
        Return:
            dict: a dict containing the attributes of the student
        """
        return self.__dict__
