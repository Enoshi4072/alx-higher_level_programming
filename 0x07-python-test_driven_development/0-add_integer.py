#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: The first number (float or int)
        b: The second number (float or int). Default is set to 98

    Raises:
        TypeError: If any or both of the args provided is not an int

    Returns:
        The sum of a and b (int)

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    answer = int(a) + int(b)
    return int(answer)
