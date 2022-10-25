#!/usr/bin/python3
from calculator_1 import add, div, sub, mul
from sys import argv
if __name__ == '__main__':
    operators = ["+", "-", "*", "/"]
    result = 0
    length = len(argv)

    if length != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b> ")
        exit(1)

    if (argv[2]) not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if (argv[2] == "+"):
        result = add(a, b)
    elif (argv[2] == "-"):
        result = sub(a, b)
    elif (argv[2] == "*"):
        result = mul(a, b)
    elif (argv[2] == "/"):
        result = div(a, b)

    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, result))
