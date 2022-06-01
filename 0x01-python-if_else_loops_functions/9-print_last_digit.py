#!/usr/bin/python3
def print_last_digit(number):
    last = int(number / 10)
    last = number - (last * 10)
    if number < 0:
        last1 = last * (-1)
        print(f"{last1}", end='')
        return last1
    else:
        print(f"{last}", end='')
        return last
