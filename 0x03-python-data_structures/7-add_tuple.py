#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lta = len(tuple_a)
    ltb = len(tuple_b)

    if (lta == 1):
        ta2 = 0
    if (lta == 0):
        ta2 = 0
        ta1 = 0
    if (ltb == 1):
        tb2 = 0
    if (ltb == 0):
        tb1 = 0
        tb2 = 0
    if (lta >= 2):
        ta1 = tuple_a[0]
        ta2 = tuple_a[1]
    if (ltb >= 2):
        tb1 = tuple_b[0]
        tb2 = tuple_b[1]

    new = (ta1 + tb1, ta2 + tb2)

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
