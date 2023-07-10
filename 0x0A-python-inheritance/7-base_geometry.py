#!/usr/bin/python3
""" Defining an empty class """


class BaseGeometry:
    """ Code for the class goes here """
    def area(self):
        """
        Raises an exception with a message

        """
        raise Exception("area() is not implemented")

    def def integer_validator(self, name, value):
        """
        Validates if the value is an int or greater than 0

        Args:
            name: The values name
            value: The values name

        Raises:
            TypeError: 
                When the value is not an integer.
            ValueError:
                When the value is equal or less than 0
        """
        if not isinstance(value, int):
            raise Typeerror("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
