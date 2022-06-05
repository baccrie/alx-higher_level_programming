#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list
    new[idx] = element
    return (new)

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
