#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    The function divides all the elements of a matrix

    Arguments:
        matrix: a list of lists of integers or floats
        div: May be an int or a float, the number to divide the elements
            in the matrix

    Raises:
        TypeError: If any of the following:
            If a mtrix is not provided
            Different sizes of the rows provided
            Div is not an int or a float
            If the matrix consists of non-nums
        ZeroDivisionError: If the value provided for the div is 0.

    Returns:
        matrix: a list of lists (matrix) with values that result
        after the division of elements
        
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size_row = len(matrix[0])
    if not all(len(row) == size_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    n_mat = [[round(element / div, 2) for element in row] for row in matrix]
    return n_mat
