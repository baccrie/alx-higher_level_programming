#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_list = list(map(lambda i: list(map(lambda j: j * j, i)), matrix))
    return (new_list)
