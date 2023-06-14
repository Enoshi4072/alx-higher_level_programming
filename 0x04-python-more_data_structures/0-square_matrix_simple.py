#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    new_m = matrix
    new_m1 = list(map(lambda x: list(map(lambda item: item ** 2, x)), new_m))
    return new_m1
