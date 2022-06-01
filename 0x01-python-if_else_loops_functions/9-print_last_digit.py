def print_last_digit(number):
    last = int(number / 10)
    last = number - (last * 10)
    if number < 0:
        print("{}".format(-1 * last), end='')
    else:
        f"{last}"
