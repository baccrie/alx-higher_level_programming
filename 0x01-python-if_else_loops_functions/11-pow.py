#!/usr/bin/python3
def pow(a, b):
    i = 0
    if b < 0:
        power = a ** b
        return (power)
    power = 1

    while (i < b):
        power *= a
        i += 1
    return (power)
