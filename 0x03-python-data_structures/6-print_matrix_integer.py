#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{:d} ".format(y), end = "")
        print("", end = "")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

