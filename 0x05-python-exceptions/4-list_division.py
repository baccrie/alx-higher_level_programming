#!/usr/bin/python
def list_division(my_list_1, my_list_2, list_length):
    try:
        i = 0
        while (i < list_length):
            my_list_1[i]
            my_list_2[i]
            my_list_1[i] / my_list_2[i]
            try:
                new_list[i] = my_list_1[i] / my_list_2
            except:
                new_list[i] = 0
             i += 1

    except:
        print("out of range")
