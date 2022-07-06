#!/usr/python3

def remove_char_at(str, n):
    arr = []
    i = 0
    while (i < len(str)):
        if not (i == n):
            arr.append(str[i])
            i += 1
        else:
            i += 1

    string = "".join(arr)
    return (string)


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
