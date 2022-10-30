#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = []
    if not my_list:
        return (0)
    new.append(my_list[0])
    for i in my_list:
        if i in new:
            pass
        else:
            new.append(i)
    for i in new:
        sum += i

    return (sum)
