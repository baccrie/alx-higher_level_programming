#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        return (None)

    finally:
        try:
            print("Inside result: {:.1f}".format(result))
            return (result)
        except NameError:
            print("Inside result: None")
            return (None)
