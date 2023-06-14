#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [item ** 2 for item in row], matrix))
