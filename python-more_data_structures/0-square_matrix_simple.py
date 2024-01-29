#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in range(len(matrix)):
        row = [num**2 for num in matrix[num]]
        new_matrix.append(row)
    return (new_matrix)
