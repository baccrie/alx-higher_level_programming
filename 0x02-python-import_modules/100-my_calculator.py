#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    length = len(argv)
    if (length != 4):
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        op = (argv[2])
        match (op):
            case "+":
                result = add(a, b)
            case "-":
                result = sub(a, b)
            case "*":
                result = mul(a, b)
            case "/":
                result = div(a, b)
            case default:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)

        print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
