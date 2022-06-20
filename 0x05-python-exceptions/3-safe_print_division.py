#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b

    except:
        return (None)

    finally:
        try:
            print("Inside result: {:.1f}".format(result))
            return (result)
        except:
            print("Inside result: None")
            return (None)


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
