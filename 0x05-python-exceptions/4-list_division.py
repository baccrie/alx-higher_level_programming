#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_length = []
    for i in range(list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            num = 0
            print("division by zero")
        except (TypeError):
            print("wrong type")
            num = 0
        except (IndexError):
            print("out of range")
            num = 0
        finally:
            new_length.append(num)

    return (new_length)
