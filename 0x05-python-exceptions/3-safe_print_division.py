#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except (Exception):
        c = "None"
        break
    finally:
        print("{}".format(c))

    return (c)
