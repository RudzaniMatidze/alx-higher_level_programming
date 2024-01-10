#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_result = [[0 for _ in row] for row in matrix]
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            matrix_result[a][b] = matrix[a][b] ** 2

    return matrix_result
