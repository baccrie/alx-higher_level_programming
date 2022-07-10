#!/usr/bin/python3
"""
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        leng = len(a) - 1
        i = 0
        for b in a:
            if i == leng:
                print("{}".format(b), end='')
            else:
                print("{} ".format(b), end='')
            i += 1
        print('')
"""


def print_matrix_integer(matrix=[[]]):
    i = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{}".format(matrix[i][j]))
            else:
                print("{} ".format(matrix[i][j]), end='')
