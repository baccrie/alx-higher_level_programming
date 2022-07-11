#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = matrix
    new = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[i][j] = new[i][j] ** 2

    matrix = tmp
    return (new)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
