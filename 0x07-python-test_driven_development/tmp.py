#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 4, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 2))
try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)
print(matrix)
