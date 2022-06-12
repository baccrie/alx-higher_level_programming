#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    l2 = len(tuple_b)

    a0, a1, b0, b1 = 0, 0, 0, 0
    if (l1 == 1):
        a0 = tuple_a[0]
    elif (l1 >= 2):
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if (l2 == 1):
        b0 = tuple_b[0]
    elif (l2 >= 2):
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    sumTupleA = a0 + b0
    sumTupleB = b1 + a1
    newTuple = (sumTupleA, sumTupleB)
    return (newTuple)
