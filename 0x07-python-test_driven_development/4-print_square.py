#!/usr/bin/python3

def print_square(size):
    """
    prints a square with the character #

    Args:
        size (int): The dimenstions of the square

    Raises:
        TypeError:
            If size is not an integer
            If size is a float and is less than 0
        ValueError:
            If size if less than 0
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
