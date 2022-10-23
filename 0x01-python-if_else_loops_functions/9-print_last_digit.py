#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        rem = (number * (-1))
        rem = rem - ((rem // 10) * 10)
    else:
        rem = number % 10

    print(rem, end="")
    return (rem)
