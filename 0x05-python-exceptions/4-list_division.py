#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_length = []
    for i in range(list_length):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by zero")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            new_length.append(num)

    return (new_length)
