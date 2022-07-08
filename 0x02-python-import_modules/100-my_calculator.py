#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    length = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if not (length == 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        match (op):
            case '+':
                result = mul(a, b)
            case '-':
                result = sub(a, b)
            case '*':
                result = mul(a, b)
            case '/':
                result = div(a, b)
            case default:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)

        printf("{} {} {} = {}".format(a, b, op, ans))
