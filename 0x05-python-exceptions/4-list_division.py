#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while (i < list_length):
        try:
            a = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            a = 0
            print('division by 0')
        except (TypeError):
            a = 0
            print('wrong type')
        except (IndexError):
            a = 0
            print('out of range')
        finally:
            new_list.append(a)
        i += 1

    return (new_list)
