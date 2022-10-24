#!/usr/bin/python3
from calculator_1 import add, div, sub, mul
from sys import argv
if __name__ == '__main__':
    operators = ["+", "-", "*", "/"]
    length = len(argv)

    if length != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b> ")
        exit(1)

    elif (argv[2]) not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        length = len(argv)
        result = 0

        if (argv[2] == '+'):
            result = add(a, b)
        elif (argv[2] == '-'):
            result = sub(a, b)
        elif (argv[2] == '*'):
            result = mul(a, b)
        elif (argv[2] == '/'):
            result = div(a, b)

        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
