#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[a ** 2 for a in row] for row in matrix]
    return new_matrix
