#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    length = len(argv)
    if (length != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        op = str(argv[2])
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
