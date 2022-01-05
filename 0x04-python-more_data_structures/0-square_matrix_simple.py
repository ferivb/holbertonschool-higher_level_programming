#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        n_matrix = [list(map(lambda x: x ** 2, j)) for j in matrix]
        return n_matrix
    return matrix
