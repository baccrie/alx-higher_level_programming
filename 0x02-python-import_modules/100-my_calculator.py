#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == "__main__"):
    argc = len(argv)
    result = 0
    operators = ["+", "-", "*", "/"]

    if (argc != 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    elif (argv[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if (operator == "+"):
        result = add(a, b)
    elif (operator == "-"):
        result = sub(a, b)
    elif (operator == "*"):
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
